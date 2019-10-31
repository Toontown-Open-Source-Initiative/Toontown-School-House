import anydbm
import dumbdbm
import sys
import time
from datetime import datetime

from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD
from direct.distributed.PyDatagram import *
from direct.fsm.FSM import FSM

from otp.distributed import OtpDoGlobals
from otp.otpbase import OTPGlobals


# --- ACCOUNT DATABASES ---
# These classes make up the available account database interfaces for Toontown Online.
# At the moment, we have two functional account database interfaces: DeveloperAccountDB, and LocalAccountDB.
# These will be explained further in their respective class definition.
class AccountDB:
    """
    AccountDB is the base class for all account database interface implementations. Inherit from this class when
    creating new account database interfaces, but DO NOT try to use this class on its own; you'll have a bad time!
    """
    notify = DirectNotifyGlobal.directNotify.newCategory('AccountDB')

    def __init__(self, gameServicesManager):
        self.gameServicesManager = gameServicesManager

        # This uses dbm, so we open the DB file:
        accountDbFile = simbase.config.GetString('accountdb-local-file', 'astron/databases/accounts.db')

        if sys.platform == 'darwin':
            dbm = dumbdbm
        else:
            dbm = anydbm

        self.dbm = dbm.open(accountDbFile, 'c')

    def lookup(self, playToken, callback):
        raise NotImplementedError('lookup')  # Must be overridden by subclass.

    def storeAccountID(self, databaseId, accountId, callback):
        self.dbm[databaseId] = str(accountId)
        if getattr(self.dbm, 'sync', None):
            self.dbm.sync()
            callback(True)
        else:
            self.notify.warning('Unable to associate user %s with account %d!' % (databaseId, accountId))
            callback(False)


class DeveloperAccountDB(AccountDB):
    """
    DeveloperAccountDB is a special account database interface implementation designed for use on developer builds of
    the game. This is the default account database interface when running the server locally via source code, which is
    assumed to be a development environment. DeveloperAccountDB accepts a username, and assigns each new user with
    "TTOFF_DEVELOPER" access automatically upon login.
    """
    notify = DirectNotifyGlobal.directNotify.newCategory('DeveloperAccountDB')

    def lookup(self, playToken, callback):
        # Check if this play token exists in the dbm:
        if str(playToken) not in self.dbm:
            # It is not, so we'll associate them with a brand new account object.
            callback({'success': True,
                      'accountId': 0,
                      'databaseId': playToken,
                      'accessLevel': "TTOFF_DEVELOPER"})
        else:
            def handleAccount(dclass, fields):
                if dclass != self.gameServicesManager.air.dclassesByName['AccountUD']:
                    result = {'success': False,
                              'reason': 'Your account object (%s) was not found in the database!' % dclass}
                else:
                    # We already have an account object, so we'll just return what we have.
                    result = {'success': True,
                              'accountId': int(self.dbm[playToken]),
                              'databaseId': playToken,
                              'accessLevel': fields.get('ACCESS_LEVEL', 'NO_ACCESS')}

                callback(result)

            self.gameServicesManager.air.dbInterface.queryObject(self.gameServicesManager.air.dbId,
                                                                 int(self.dbm[playToken]), handleAccount)


class GameOperation(FSM):
    """
    GameOperation is the base class for all other operations used by the GameServicesManager.
    """
    notify = DirectNotifyGlobal.directNotify.newCategory('GameOperation')
    targetConnection = False

    def __init__(self, gameServicesManager, target):
        FSM.__init__(self, self.__class__.__name__)
        self.gameServicesManager = gameServicesManager
        self.target = target

    def enterOff(self):
        # Deletes the target from either connection2fsm or account2fsm
        # depending on the value of self.targetConnection.
        if self.targetConnection:
            del self.gameServicesManager.connection2fsm[self.target]
        else:
            del self.gameServicesManager.account2fsm[self.target]

    def enterKill(self, reason=''):
        # Kills either the target connection or the target account
        # depending on the value of self.targetConnection, and then
        # sets this FSM's state to Off.
        if self.targetConnection:
            self.gameServicesManager.killConnection(self.target, reason)
        else:
            self.gameServicesManager.killAccount(self.target, reason)

        self.demand('Off')


class LoginOperation(GameOperation):
    notify = DirectNotifyGlobal.directNotify.newCategory('LoginOperation')
    targetConnection = True

    def __init__(self, gameServicesManager, target):
        GameOperation.__init__(self, gameServicesManager, target)
        self.playToken = None
        self.account = None

    def enterStart(self, playToken):
        # Sets self.playToken, then enters the QueryAccountDB state.
        self.playToken = playToken
        self.demand('QueryAccountDB')

    def enterQueryAccountDB(self):
        # Calls the lookup function on the GameServicesManager's defined account DB interface.
        self.gameServicesManager.accountDb.lookup(self.playToken, self.__handleLookup)

    def __handleLookup(self, result):
        # This is a callback function that will be called by the lookup function
        # of the GameServicesManager's account DB interface. It processes the
        # lookup function's result & determines which operation should run next.
        if not result.get('success'):
            # The play token was rejected! Kill the connection.
            self.gameServicesManager.air.writeServerEvent('play-token-rejected', self.target, self.playToken)
            self.demand('Kill', result.get('reason', 'The accounts database rejected your play token.'))
            return

        # Grab the databaseId, accessLevel, and accountId from the result.
        self.databaseId = result.get('databaseId', 0)
        self.accessLevel = result.get('accessLevel', 'NO_ACCESS')
        accountId = result.get('accountId', 0)

        if accountId:
            # There is an account ID, so let's retrieve the associated account.
            self.accountId = accountId
            self.demand('RetrieveAccount')
        else:
            # There is no account ID, so let's create a new account.
            self.demand('CreateAccount')

    def enterCreateAccount(self):
        # Creates a brand new account & stores it in the database.
        self.account = {'ACCOUNT_AV_SET': [0] * 6,
                        'ESTATE_ID': 0,
                        'ACCOUNT_AV_SET_DEL': [],
                        'CREATED': time.ctime(),
                        'LAST_LOGIN': time.ctime(),
                        'ACCOUNT_ID': str(self.databaseId),
                        'ACCESS_LEVEL': self.accessLevel}

        # Create the account object in the database using the data from self.account.
        # self.__handleCreate is the callback which will be called after createObject has completed.
        self.gameServicesManager.air.dbInterface.createObject(self.gameServicesManager.air.dbId,
                                                              self.gameServicesManager.air.dclassesByName['AccountUD'],
                                                              self.account, self.__handleCreate)

    def __handleCreate(self, accountId):
        # This function handles successful & unsuccessful account creations.
        if self.state != 'CreateAccount':
            # If we're not in the CreateAccount state, this request is invalid.
            self.notify.warning('Received CreateAccount response outside of the CreateAccount state.')
            return

        if not accountId:
            # If we don't have an accountId, then that means the database was unable
            # to create an account object for us, for whatever reason. Kill the connection.
            self.notify.warning('Database failed to create an account object!')
            self.demand('Kill', 'Your account object could not be created in the game database.')
            return

        # Otherwise, the account object was created successfully!
        self.gameServicesManager.air.writeServerEvent('account-created', accountId)

        # We can now enter the StoreAccountID state.
        self.accountId = accountId
        self.demand('StoreAccountID')

    def enterStoreAccountID(self):
        # Stores the account ID in the account bridge.
        # self.__handleStored is the callback which
        # will be called after storeAccountID has completed.
        self.gameServicesManager.accountDb.storeAccountID(self.databaseId, self.accountId, self.__handleStored)

    def __handleStored(self, success=True):
        if not success:
            # The account bridge was unable to store the account ID,
            # for whatever reason. Kill the connection.
            self.demand('Kill', 'The account server could not save your account DB ID!')
            return

        # We are all set with account creation now! It's time to enter the SetAccount state.
        self.demand('SetAccount')

    def enterRetrieveAccount(self):
        # Query the database object associated with self.accountId.
        # self.__handleRetrieve is the callback which will be called
        # after queryObject has completed.
        self.gameServicesManager.air.dbInterface.queryObject(self.gameServicesManager.air.dbId, self.accountId,
                                                             self.__handleRetrieve)

    def __handleRetrieve(self, dclass, fields):
        # Checks if the queried object is valid and if it is, enters
        # the SetAccount state. Otherwise, the connection is killed.
        if dclass != self.gameServicesManager.air.dclassesByName['AccountUD']:
            # This is not an account object! Kill the connection.
            self.demand('Kill', 'Your account object (%s) was not found in the database!' % dclass)
            return

        # We can now enter the SetAccount state.
        self.account = fields
        self.demand('SetAccount')

    def enterSetAccount(self):
        # If somebody's already logged into this account, disconnect them.
        datagram = PyDatagram()
        datagram.addServerHeader(self.gameServicesManager.GetAccountConnectionChannel(self.accountId),
                                 self.gameServicesManager.air.ourChannel, CLIENTAGENT_EJECT)
        datagram.addUint16(OTPGlobals.BootedLoggedInElsewhere)
        datagram.addString('This account has been logged into elsewhere.')
        self.gameServicesManager.air.send(datagram)

        # Now we'll add this connection to the account channel.
        datagram = PyDatagram()
        datagram.addServerHeader(self.target, self.gameServicesManager.air.ourChannel, CLIENTAGENT_OPEN_CHANNEL)
        datagram.addChannel(self.gameServicesManager.GetAccountConnectionChannel(self.accountId))
        self.gameServicesManager.air.send(datagram)

        # Set their sender channel to represent their account affiliation.
        datagram = PyDatagram()
        datagram.addServerHeader(self.target, self.gameServicesManager.air.ourChannel, CLIENTAGENT_SET_CLIENT_ID)
        datagram.addChannel(self.accountId << 32)  # accountId in high 32 bits, 0 in low (no avatar).
        self.gameServicesManager.air.send(datagram)

        # We can now un-sandbox the sender.
        self.gameServicesManager.air.setClientState(self.target, 2)  # ESTABLISHED state.

        # Update the last login timestamp.
        self.gameServicesManager.air.dbInterface.updateObject(self.gameServicesManager.air.dbId, self.accountId,
                                                              self.gameServicesManager.air.dclassesByName['AccountUD'],
                                                              {'LAST_LOGIN': time.ctime(),
                                                               'ACCOUNT_ID': str(self.databaseId),
                                                               'ACCESS_LEVEL': self.accessLevel})

        # We're done.
        self.gameServicesManager.air.writeServerEvent('account-login', clientId=self.target, accId=self.accountId,
                                                      dbId=self.databaseId, playToken=self.playToken)

        # Send the acceptLogin update through the GameServicesManager & set this operation's state to Off.
        self.gameServicesManager.sendUpdateToChannel(self.target, 'acceptLogin', [])
        self.demand('Off')


class AvatarOperation(GameOperation):
    notify = DirectNotifyGlobal.directNotify.newCategory('AvatarOperation')
    postAccountState = 'Off'  # Must be overridden by subclass.

    def enterRetrieveAccount(self):
        # Query the account. self.__handleRetrieve is the callback
        # which will be called after queryObject has completed.
        self.gameServicesManager.air.dbInterface.queryObject(self.gameServicesManager.air.dbId, self.target,
                                                             self.__handleRetrieve)

    def __handleRetrieve(self, dclass, fields):
        if dclass != self.gameServicesManager.air.dclassesByName['AccountUD']:
            # This is not an account object! Kill the connection.
            self.demand('Kill', 'Your account object (%s) was not found in the database!' % dclass)
            return

        # Set the account & avList.
        self.account = fields
        self.avList = self.account['ACCOUNT_AV_SET']

        # Sanitize the avList, just in case it is too long/short.
        self.avList = self.avList[:6]
        self.avList += [0] * (6 - len(self.avList))

        # We're done; enter the postAccountState.
        self.demand(self.postAccountState)


class GetAvatarsOperation(AvatarOperation):
    notify = DirectNotifyGlobal.directNotify.newCategory('GetAvatarsOperation')
    postAccountState = 'QueryAvatars'

    def __init__(self, gameServicesManager, target):
        AvatarOperation.__init__(self, gameServicesManager, target)
        self.pendingAvatars = None
        self.avatarFields = None

    def enterStart(self):
        # First, retrieve the account.
        self.demand('RetrieveAccount')

    def enterQueryAvatars(self):
        # Now, we will query the avatars that exist in the account.
        self.pendingAvatars = set()
        self.avatarFields = {}

        # Loop through the list of avatars:
        for avId in self.avList:
            if avId:
                # This index contains an avatar! Add it to the pending avatars.
                self.pendingAvatars.add(avId)

                # This is our callback function that queryObject
                # will call when done querying each avatar object.
                def response(dclass, fields, avId=avId):
                    if self.state != 'QueryAvatars':
                        # We're not in the QueryAvatars state, so this request is invalid.
                        return

                    if dclass != self.gameServicesManager.air.dclassesByName[self.gameServicesManager.avatarDclass]:
                        # The dclass is invalid! Kill the connection.
                        self.demand('Kill', 'One of the account\'s avatars is invalid! dclass = %s, expected = %s' % (
                            dclass, self.gameServicesManager.avatarDclass))
                        return

                    # Otherwise, we're all set! Add the queried avatar fields to the
                    # avatarFields array, remove from the pending list, and set our
                    # state to SendAvatars.
                    self.avatarFields[avId] = fields
                    self.pendingAvatars.remove(avId)
                    if not self.pendingAvatars:
                        self.demand('SendAvatars')

                # Query the avatar object.
                self.gameServicesManager.air.dbInterface.queryObject(self.gameServicesManager.air.dbId, avId, response)

        if not self.pendingAvatars:
            # No pending avatars! Set our state to SendAvatars.
            self.demand('SendAvatars')

    def enterSendAvatars(self):
        # Here is where we'll construct a list of potential avatars,
        # given the data from self.avatarFields, and send that to the client.
        potentialAvatars = []

        # Loop through the avatarFields array:
        for avId, fields in self.avatarFields.items():
            # Get the appropriate values.
            index = self.avList.index(avId)
            wishNameState = fields.get('WishNameState', [''])[0]
            name = fields['setName'][0]
            nameState = 0
            if wishNameState == 'OPEN':
                nameState = 1
            elif wishNameState == 'PENDING':
                nameState = 2
            elif wishNameState == 'APPROVED':
                nameState = 3
                name = fields['WishName'][0]
            elif wishNameState == 'REJECTED':
                nameState = 4
            elif wishNameState == 'LOCKED':
                nameState = 0
            else:
                self.gameServicesManager.notify.warning(
                    'Avatar %s is in unknown name state %s.' % (avId, wishNameState))
                nameState = 0

            # Add those to potentialAvatars.
            potentialAvatars.append([avId, name, fields['setDNAString'][0], index, nameState])

        # We're done; send the avatarListResponse update through the
        # GameServicesManager, then we can set this operation's
        # state to Off.
        self.gameServicesManager.sendUpdateToAccountId(self.target, 'avatarListResponse', [potentialAvatars])
        self.demand('Off')


# n.b.: We inherit from GetAvatarsOperation here as the remove
# operation ends in a setAvatars message being sent to the client.
class RemoveAvatarOperation(GetAvatarsOperation):
    notify = DirectNotifyGlobal.directNotify.newCategory('RemoveAvatarOperation')
    postAccountState = 'ProcessRemove'

    def __init__(self, gameServicesManager, target):
        GetAvatarsOperation.__init__(self, gameServicesManager, target)
        self.avId = None

    def enterStart(self, avId):
        # Store this value & call the base function.
        self.avId = avId
        GetAvatarsOperation.enterStart(self)

    def enterProcessRemove(self):
        # Make sure that the target avatar is part of the account:
        if self.avId not in self.avList:
            # The sender tried to remove an avatar not on the account! Kill the connection.
            self.demand('Kill', 'Tried to remove an avatar not on the account!')
            return

        # Get the index of this avatar.
        index = self.avList.index(self.avId)
        self.avList[index] = 0

        # We will now add this avatar to ACCOUNT_AV_SET_DEL.
        avatarsRemoved = list(self.account.get('ACCOUNT_AV_SET_DEL', []))
        avatarsRemoved.append([self.avId, int(time.time())])

        # Get the estate ID of this account.
        estateId = self.account.get('ESTATE_ID', 0)

        if estateId != 0:
            # The following will assume that the house already exists,
            # however it shouldn't be a problem if it doesn't.
            self.gameServicesManager.air.dbInterface.updateObject(self.gameServicesManager.air.dbId, estateId,
                                                                  self.gameServicesManager.air.dclassesByName[
                                                                      'DistributedEstateAI'],
                                                                  {'setSlot%sToonId' % index: [0],
                                                                   'setSlot%sItems' % index: [[]]})

        if self.gameServicesManager.air.ttoffFriendsManager:
            self.gameServicesManager.air.ttoffFriendsManager.clearList(self.avId)
        else:
            friendsManagerDoId = OtpDoGlobals.OTP_DO_ID_TTOFF_FRIENDS_MANAGER
            friendsManagerDclass = self.gameServicesManager.air.dclassesByName['TTOffFriendsManagerUD']
            datagram = friendsManagerDclass.aiFormatUpdate('clearList', friendsManagerDoId, friendsManagerDoId,
                                                           self.gameServicesManager.air.ourChannel, [self.avId])
            self.gameServicesManager.air.send(datagram)

        # We can now update the account with the new data. self.__handleRemove is the
        # callback which will be called upon completion of updateObject.
        self.gameServicesManager.air.dbInterface.updateObject(self.gameServicesManager.air.dbId, self.target,
                                                              self.gameServicesManager.air.dclassesByName['AccountUD'],
                                                              {'ACCOUNT_AV_SET': self.avList,
                                                               'ACCOUNT_AV_SET_DEL': avatarsRemoved},
                                                              {'ACCOUNT_AV_SET': self.account['ACCOUNT_AV_SET'],
                                                               'ACCOUNT_AV_SET_DEL': self.account[
                                                                   'ACCOUNT_AV_SET_DEL']},
                                                              self.__handleRemove)

    def __handleRemove(self, fields):
        if fields:
            # The avatar was unable to be removed from the account! Kill the account.
            self.demand('Kill', 'Database failed to mark the avatar as removed!')
            return

        # Otherwise, we're done! We'll enter the QueryAvatars state now so that
        # the user is sent back to the avatar chooser.
        self.gameServicesManager.air.writeServerEvent('avatar-deleted', self.avId, self.target)
        self.demand('QueryAvatars')


class LoadAvatarOperation(AvatarOperation):
    notify = DirectNotifyGlobal.directNotify.newCategory('LoadAvatarOperation')
    postAccountState = 'GetTargetAvatar'

    def __init__(self, gameServicesManager, target):
        AvatarOperation.__init__(self, gameServicesManager, target)
        self.avId = None

    def enterStart(self, avId):
        # Store this value & move on to RetrieveAccount
        self.avId = avId
        self.demand('RetrieveAccount')

    def enterGetTargetAvatar(self):
        # Make sure that the target avatar is part of the account:
        if self.avId not in self.avList:
            # The sender tried to play on an avatar not on the account! Kill the connection.
            self.demand('Kill', 'Tried to play on an avatar not on the account!')
            return

        # Query the database for the avatar. self.__handleAvatar is
        # our callback which will be called upon queryObject's completion.
        self.gameServicesManager.air.dbInterface.queryObject(self.gameServicesManager.air.dbId, self.avId,
                                                             self.__handleAvatar)

    def __handleAvatar(self, dclass, fields):
        if dclass != self.gameServicesManager.air.dclassesByName[self.gameServicesManager.avatarDclass]:
            # This dclass is not a valid avatar! Kill the connection.
            self.demand('Kill', 'One of the account\'s avatars is invalid!')
            return

        # Store the avatar & move on to SetAvatar.
        self.avatar = fields
        self.demand('SetAvatar')

    def enterSetAvatar(self):
        # Get the client channel.
        channel = self.gameServicesManager.GetAccountConnectionChannel(self.target)

        # We will first assign a POST_REMOVE that will unload the
        # avatar in the event of them disconnecting while we are working.
        cleanupDatagram = PyDatagram()
        cleanupDatagram.addServerHeader(self.avId, channel, STATESERVER_OBJECT_DELETE_RAM)
        cleanupDatagram.addUint32(self.avId)
        datagram = PyDatagram()
        datagram.addServerHeader(channel, self.gameServicesManager.air.ourChannel, CLIENTAGENT_ADD_POST_REMOVE)
        datagram.addString(cleanupDatagram.getMessage())
        self.gameServicesManager.air.send(datagram)

        # We will now set the account's days since creation on the client.
        creationDate = self.getCreationDate()
        accountDays = -1
        if creationDate:
            now = datetime.fromtimestamp(time.mktime(time.strptime(time.ctime())))
            accountDays = abs((now - creationDate).days)

        if accountDays < 0 or accountDays > 4294967295:
            accountDays = 100000

        self.gameServicesManager.sendUpdateToAccountId(self.target, 'receiveAccountDays', [accountDays])

        # Get the avatar's "true" access (that is, the integer value that corresponds to the assigned string value).
        accessLevel = self.account.get('ACCESS_LEVEL', 'NO_ACCESS')
        accessLevel = OTPGlobals.accessLevelValues.get(accessLevel, 0)

        # We will now activate the avatar on the DBSS.
        self.gameServicesManager.air.sendActivate(self.avId, 0, 0, self.gameServicesManager.air.dclassesByName[
            self.gameServicesManager.avatarDclass], {'setAccessLevel': [accessLevel]})

        # Next, we will add them to the avatar channel.
        datagram = PyDatagram()
        datagram.addServerHeader(channel, self.gameServicesManager.air.ourChannel, CLIENTAGENT_OPEN_CHANNEL)
        datagram.addChannel(self.gameServicesManager.GetPuppetConnectionChannel(self.avId))
        self.gameServicesManager.air.send(datagram)

        # We will now set the avatar as the client's session object.
        self.gameServicesManager.air.clientAddSessionObject(channel, self.avId)

        # Now we need to set their sender channel to represent their account affiliation.
        datagram = PyDatagram()
        datagram.addServerHeader(channel, self.gameServicesManager.air.ourChannel, CLIENTAGENT_SET_CLIENT_ID)
        datagram.addChannel(self.target << 32 | self.avId)  # accountId in high 32 bits, avatar in low.
        self.gameServicesManager.air.send(datagram)

        # We will now grant ownership.
        self.gameServicesManager.air.setOwner(self.avId, channel)

        # Tell the friends manager that an avatar is coming online.
        friendsList = [x for x, y in self.avatar['setFriendsList'][0]]
        self.gameServicesManager.air.ttoffFriendsManager.comingOnline(self.avId, friendsList)

        # Now we'll assign a POST_REMOVE that will tell the friends manager
        # that an avatar has gone offline, in the event that they disconnect
        # unexpectedly.
        if self.gameServicesManager.air.ttoffFriendsManager:
            friendsManagerDclass = self.gameServicesManager.air.ttoffFriendsManager.dclass
            cleanupDatagram = friendsManagerDclass.aiFormatUpdate('goingOffline',
                                                                  self.gameServicesManager.air.ttoffFriendsManager.doId,
                                                                  self.gameServicesManager.air.ttoffFriendsManager.doId,
                                                                  self.gameServicesManager.air.ourChannel, [self.avId])
        else:
            friendsManagerDoId = OtpDoGlobals.OTP_DO_ID_TTOFF_FRIENDS_MANAGER
            friendsManagerDclass = self.gameServicesManager.air.dclassesByName['TTOffFriendsManagerUD']
            cleanupDatagram = friendsManagerDclass.aiFormatUpdate('goingOffline', friendsManagerDoId,
                                                                  friendsManagerDoId,
                                                                  self.gameServicesManager.air.ourChannel, [self.avId])

        datagram = PyDatagram()
        datagram.addServerHeader(channel, self.gameServicesManager.air.ourChannel, CLIENTAGENT_ADD_POST_REMOVE)
        datagram.addString(cleanupDatagram.getMessage())
        self.gameServicesManager.air.send(datagram)

        # We can now finally shut down this operation.
        self.gameServicesManager.air.writeServerEvent('avatar-chosen', avId=self.avId, accId=self.target)
        self.demand('Off')

    def getCreationDate(self):
        # Based on game creation date:
        creationDate = self.account.get('CREATED', '')
        try:
            creationDate = datetime.fromtimestamp(time.mktime(time.strptime(creationDate)))
        except ValueError:
            creationDate = ''

        return creationDate


class UnloadAvatarOperation(GameOperation):
    notify = DirectNotifyGlobal.directNotify.newCategory('UnloadAvatarOperation')

    def __init__(self, gameServicesManager, target):
        GameOperation.__init__(self, gameServicesManager, target)
        self.avId = None

    def enterStart(self, avId):
        # Store the avId.
        self.avId = avId

        # We actually don't even need to query the account, as we know
        # that the avatar is being played, so let's just unload the avatar.
        self.demand('UnloadAvatar')

    def enterUnloadAvatar(self):
        # Get the client channel.
        channel = self.gameServicesManager.GetAccountConnectionChannel(self.target)

        # Tell the friends manager that we're logging off.
        self.gameServicesManager.air.ttoffFriendsManager.goingOffline(self.avId)

        # First, remove our POST_REMOVES.
        datagram = PyDatagram()
        datagram.addServerHeader(channel, self.gameServicesManager.air.ourChannel, CLIENTAGENT_CLEAR_POST_REMOVES)
        self.gameServicesManager.air.send(datagram)

        # Next, remove the avatar channel.
        datagram = PyDatagram()
        datagram.addServerHeader(channel, self.gameServicesManager.air.ourChannel, CLIENTAGENT_CLOSE_CHANNEL)
        datagram.addChannel(self.gameServicesManager.GetPuppetConnectionChannel(self.avId))
        self.gameServicesManager.air.send(datagram)

        # Next, reset the sender channel.
        datagram = PyDatagram()
        datagram.addServerHeader(channel, self.gameServicesManager.air.ourChannel, CLIENTAGENT_SET_CLIENT_ID)
        datagram.addChannel(self.target << 32)  # accountId in high 32 bits, no avatar in low.
        self.gameServicesManager.air.send(datagram)

        # Reset the session object.
        datagram = PyDatagram()
        datagram.addServerHeader(channel, self.gameServicesManager.air.ourChannel, CLIENTAGENT_REMOVE_SESSION_OBJECT)
        datagram.addUint32(self.avId)
        self.gameServicesManager.air.send(datagram)

        # Unload the avatar object.
        datagram = PyDatagram()
        datagram.addServerHeader(self.avId, channel, STATESERVER_OBJECT_DELETE_RAM)
        datagram.addUint32(self.avId)
        self.gameServicesManager.air.send(datagram)

        # We're done! We can now shut down this operation.
        self.gameServicesManager.air.writeServerEvent('avatar-unloaded', avId=self.avId)
        self.demand('Off')


class GameServicesManagerUD(DistributedObjectGlobalUD):
    notify = DirectNotifyGlobal.directNotify.newCategory('GameServicesManagerUD')
    avatarDclass = None  # Must be overridden by subclass.

    def __init__(self, air):
        DistributedObjectGlobalUD.__init__(self, air)
        self.connection2fsm = {}
        self.account2fsm = {}
        self.accountDb = None

    def announceGenerate(self):
        DistributedObjectGlobalUD.announceGenerate(self)

        # The purpose of connection2fsm & account2fsm are to
        # keep track of the connection & account IDs that are
        # currently running an operation on the GameServicesManager.
        # Ideally, this will help us prevent clients from running
        # more than one operation at a time which could potentially
        # lead to race conditions & the exploitation of them.
        self.connection2fsm = {}
        self.account2fsm = {}

        # Instantiate the account database interface.
        # TODO: In the future, add more database interfaces & make this configurable.
        self.accountDb = DeveloperAccountDB(self)

    def login(self, playToken):
        # Get the connection ID.
        sender = self.air.getMsgSender()

        self.notify.debug('Play token %s received from %s' % (playToken, sender))

        if sender >> 32:
            # This account is already logged in.
            self.killConnection(sender, 'This account is already logged in.')
            return

        if sender in self.connection2fsm:
            # This account is already currently running an operation. Kill this connection.
            self.killConnectionFSM(sender)
            return

        # Run the login operation.
        self.connection2fsm[sender] = LoginOperation(self, sender)
        self.connection2fsm[sender].request('Start', playToken)

    def killConnection(self, connectionId, reason):
        # Sends CLIENTAGENT_EJECT to the given connectionId with the given reason.
        datagram = PyDatagram()
        datagram.addServerHeader(connectionId, self.air.ourChannel, CLIENTAGENT_EJECT)
        datagram.addUint16(OTPGlobals.BootedConnectionKilled)
        datagram.addString(reason)
        self.air.send(datagram)

    def killConnectionFSM(self, connectionId):
        # Kills the connection for duplicate FSMs.
        fsm = self.connection2fsm.get(connectionId)
        if not fsm:
            self.notify.warning('Tried to kill connection %s for duplicate FSMs, but none exist!' % connectionId)
            return

        self.killConnection(connectionId, 'An operation is already running: %s' % fsm.name)

    def killAccount(self, accountId, reason):
        # Kills the account's connection given an accountId & a reason.
        self.killConnection(self.GetAccountConnectionChannel(accountId), reason=reason)

    def killAccountFSM(self, accountId):
        # Kills the account for duplicate FSMs.
        fsm = self.account2fsm.get(accountId)
        if not fsm:
            self.notify.warning('Tried to kill account %s for duplicate FSMs, but none exist!' % accountId)
            return

        self.killAccount(accountId, 'An operation is already running: %s' % fsm.name)

    def runOperation(self, operationType, *args):
        # Runs an operation on the sender. First, get the sender.
        sender = self.air.getAccountIdFromSender()

        if not sender:
            # If the sender doesn't exist, they're not
            # logged in, so kill the connection.
            self.killAccount(sender, 'Client is not logged in.')

        if sender in self.account2fsm:
            # This account is already currently running an operation. Kill this connection.
            self.killAccountFSM(sender)
            return

        self.account2fsm[sender] = operationType(self, sender)
        self.account2fsm[sender].request('Start', *args)

    def requestAvatarList(self):
        # An account is requesting their avatar list;
        # let's run a GetAvatarsOperation.
        self.runOperation(GetAvatarsOperation)

    def requestRemoveAvatar(self, avId):
        # Someone is requesting to have an avatar removed; run a RemoveAvatarOperation.
        self.runOperation(RemoveAvatarOperation, avId)

    def requestPlayAvatar(self, avId):
        # Someone is requesting to play on an avatar.
        # First, let's get the senders avId & accId.
        currentAvId = self.air.getAvatarIdFromSender()
        accountId = self.air.getAccountIdFromSender()
        if currentAvId and avId:
            # An avatar has already been chosen! Kill the account.
            self.killAccount(accountId, 'An avatar is already chosen!')
            return
        elif not currentAvId and not avId:
            # The client is likely making sure that none of its
            # avatars are active, so this isn't really an error.
            return

        if avId:
            # If the avId is not a NoneType, that means the client wants
            # to load an avatar; run a LoadAvatarOperation.
            self.runOperation(LoadAvatarOperation, avId)
        else:
            # Otherwise, the client wants to unload the avatar; run an UnloadAvatarOperation.
            self.runOperation(UnloadAvatarOperation, currentAvId)
