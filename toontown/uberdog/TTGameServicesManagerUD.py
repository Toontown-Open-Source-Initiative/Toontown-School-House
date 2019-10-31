from otp.uberdog.GameServicesManagerUD import *
from toontown.makeatoon.NameGenerator import NameGenerator
from toontown.toon.ToonDNA import ToonDNA
from toontown.toonbase import TTLocalizer


def judgeName(name):
    return True  # TODO: Make this useful.


class SetNamePatternOperation(AvatarOperation):
    notify = DirectNotifyGlobal.directNotify.newCategory('SetNamePatternOperation')
    postAccountState = 'RetrieveAvatar'

    def __init__(self, gameServicesManager, target):
        AvatarOperation.__init__(self, gameServicesManager, target)
        self.avId = None
        self.pattern = None

    def enterStart(self, avId, pattern):
        # Store these values.
        self.avId = avId
        self.pattern = pattern

        # Retrieve the account.
        self.demand('RetrieveAccount')

    def enterRetrieveAvatar(self):
        # Retrieves the avatar from the database.
        if self.avId and self.avId not in self.avList:
            # The avatar exists, but it's not an avatar that is
            # associated with this account. Kill the connection.
            self.demand('Kill', 'Tried to name an avatar not in the account!')
            return

        # Query the database for the avatar. self.__handleAvatar is
        # our callback which will be called upon queryObject's completion.
        self.gameServicesManager.air.dbInterface.queryObject(self.gameServicesManager.air.dbId, self.avId,
                                                             self.__handleAvatar)

    def __handleAvatar(self, dclass, fields):
        if dclass != self.gameServicesManager.air.dclassesByName['DistributedToonUD']:
            # This dclass is not a valid avatar! Kill the connection.
            self.demand('Kill', 'One of the account\'s avatars is invalid!')
            return

        if fields['WishNameState'][0] != 'OPEN':
            # This avatar's wish name state is not set
            # to a nameable state. Kill the connection.
            self.demand('Kill', 'Avatar is not in a nameable state!')

        # Otherwise, we can set the name, so let's enter the SetName state.
        self.demand('SetName')

    def enterSetName(self):
        # Stringify this pattern.
        parts = []
        for p, f in self.pattern:
            part = self.gameServicesManager.nameGenerator.nameDictionary.get(p, ('', ''))[1]
            if f:
                part = part[:1].upper() + part[1:]
            else:
                part = part.lower()

            parts.append(part)

        # This will merge 2 & 3 (the last name), as there should be no space.
        parts[2] += parts.pop(3)
        while '' in parts:
            parts.remove('')

        # Construct the final name string.
        name = ' '.join(parts)

        # We can now update the avatar object with the name.
        self.gameServicesManager.air.dbInterface.updateObject(self.gameServicesManager.air.dbId, self.avId,
                                                              self.gameServicesManager.air.dclassesByName[
                                                                  'DistributedToonUD'], {'WishNameState': ('LOCKED',),
                                                                                         'WishName': ('',),
                                                                                         'setName': (name,)})

        # We're done. We can now send off the namePatternResponse update through
        # the GameServicesManager, and set this operation's state to Off.
        self.gameServicesManager.air.writeServerEvent('avatar-named', self.avId, name)
        self.gameServicesManager.sendUpdateToAccountId(self.target, 'namePatternResponse', [self.avId, 1])
        self.demand('Off')


class SetNameTypedOperation(AvatarOperation):
    notify = DirectNotifyGlobal.directNotify.newCategory('SetNameTypedOperation')
    postAccountState = 'RetrieveAvatar'

    def __init__(self, gameServicesManager, target):
        AvatarOperation.__init__(self, gameServicesManager, target)
        self.avId = None
        self.name = None

    def enterStart(self, avId, name):
        # SetNameTypedOperation judges the submitted name
        # & then sets the avatars wish name state accordingly.
        self.avId = avId
        self.name = name

        if self.avId:
            # If avId is not 0, the user is submitting this name,
            # so we need to retrieve the account.
            self.demand('RetrieveAccount')
            return

        # Otherwise, avId is 0, meaning that a check request was sent.
        self.demand('JudgeName')

    def enterRetrieveAvatar(self):
        # Retrieves the avatar from the database.
        if self.avId and self.avId not in self.avList:
            # The avatar exists, but it's not an avatar that is
            # associated with this account. Kill the connection.
            self.demand('Kill', 'Tried to name an avatar not in the account!')
            return

        # Query the database for the avatar. self.__handleAvatar is
        # our callback which will be called upon queryObject's completion.
        self.gameServicesManager.air.dbInterface.queryObject(self.gameServicesManager.air.dbId, self.avId,
                                                             self.__handleAvatar)

    def __handleAvatar(self, dclass, fields):
        if dclass != self.gameServicesManager.air.dclassesByName['DistributedToonUD']:
            # This dclass is not a valid avatar! Kill the connection.
            self.demand('Kill', 'One of the account\'s avatars is invalid!')
            return

        if fields['WishNameState'][0] != 'OPEN':
            # This avatar's wish name state is not set
            # to a nameable state. Kill the connection.
            self.demand('Kill', 'Avatar is not in a nameable state!')

        # Now we can move on to the judging!
        self.demand('JudgeName')

    def enterJudgeName(self):
        # Let's see if the name is valid.
        status = judgeName(self.name)

        if self.avId and status:
            # Cool, this is a valid name, and we have an avId.
            # Let's update their avatar with the new wish name & status.
            self.gameServicesManager.air.dbInterface.updateObject(self.gameServicesManager.air.dbId, self.avId,
                                                                  self.gameServicesManager.air.dclassesByName[
                                                                      'DistributedToonUD'],
                                                                  {'WishNameState': ('PENDING',),
                                                                   'WishName': (self.name,)})

        if self.avId:
            # If the avId is not 0, log this server event, as the avatar's
            # wish name & state have been modified.
            self.gameServicesManager.air.writeServerEvent('avatar-wish-name', self.avId, self.name)

        # Otherwise, we're done! We can now send the response update
        # through the GameServicesManager & set our state to Off.
        self.gameServicesManager.sendUpdateToAccountId(self.target, 'nameTypedResponse', [self.avId, status])
        self.demand('Off')


class CreateAvatarOperation(GameOperation):
    notify = DirectNotifyGlobal.directNotify.newCategory('CreateAvatarOperation')

    def __init__(self, gameServicesManager, target):
        GameOperation.__init__(self, gameServicesManager, target)
        self.index = None
        self.dna = None

    def enterStart(self, dna, index):
        # First, perform some basic sanity checking.
        if index >= 6:
            # This index is invalid! Kill the connection.
            self.demand('Kill', 'Invalid index specified!')
            return

        if not ToonDNA().isValidNetString(dna):
            # This DNA string is invalid! Kill the connection.
            self.demand('Kill', 'Invalid DNA specified!')
            return

        # Store these values.
        self.index = index
        self.dna = dna

        # Now we can query their account.
        self.demand('RetrieveAccount')

    def enterRetrieveAccount(self):
        # Query the sender's account. self.__handleRetrieve is the
        # callback that will be called upon queryObject's competion.
        self.gameServicesManager.air.dbInterface.queryObject(self.gameServicesManager.air.dbId, self.target,
                                                             self.__handleRetrieve)

    def __handleRetrieve(self, dclass, fields):
        if dclass != self.gameServicesManager.air.dclassesByName['AccountUD']:
            # This is not an account object! Kill the connection.
            self.demand('Kill', 'Your account object (%s) was not found in the database!' % dclass)
            return

        # Now we will get our avList.
        self.account = fields
        self.avList = self.account['ACCOUNT_AV_SET']

        # We will now sanitize the avList.
        self.avList = self.avList[:6]
        self.avList += [0] * (6 - len(self.avList))

        # Check if the index is open:
        if self.avList[self.index]:
            # This index is not open! Kill the connection.
            self.demand('Kill', 'This avatar slot is already taken by another avatar!')
            return

        # All set, now let's create the avatar!
        self.demand('CreateAvatar')

    def enterCreateAvatar(self):
        # We will now construct a new Toon with the given values.
        dna = ToonDNA()
        dna.makeFromNetString(self.dna)
        colorString = TTLocalizer.NumToColor[dna.headColor]
        animalType = TTLocalizer.AnimalToSpecies[dna.getAnimal()]
        name = ' '.join((colorString, animalType))
        toonFields = {'setName': (name,),
                      'WishNameState': ('OPEN',),
                      'WishName': ('',),
                      'setDNAString': (self.dna,),
                      'setDISLid': (self.target,)}

        # Create this new Toon object in the database. self.__handleCreate is the
        # callback that will be called upon the completion of createObject.
        self.gameServicesManager.air.dbInterface.createObject(self.gameServicesManager.air.dbId,
                                                              self.gameServicesManager.air.dclassesByName[
                                                                  'DistributedToonUD'], toonFields, self.__handleCreate)

    def __handleCreate(self, avId):
        if not avId:
            # The database was unable to create a new avatar object! Kill the connection.
            self.demand('Kill', 'Database failed to create the new avatar object!')
            return

        # We can now store the avatar.
        self.avId = avId
        self.demand('StoreAvatar')

    def enterStoreAvatar(self):
        # We will now associate the avatar with the account. self.__handleStoreAvatar is the
        # callback which will be called upon the completion of updateObject.
        self.avList[self.index] = self.avId
        self.gameServicesManager.air.dbInterface.updateObject(self.gameServicesManager.air.dbId, self.target,
                                                              self.gameServicesManager.air.dclassesByName['AccountUD'],
                                                              {'ACCOUNT_AV_SET': self.avList},
                                                              {'ACCOUNT_AV_SET': self.account['ACCOUNT_AV_SET']},
                                                              self.__handleStoreAvatar)

    def __handleStoreAvatar(self, fields):
        if fields:
            # The new avatar was not associated with the account! Kill the connection.
            self.demand('Kill', 'Database failed to associate the new avatar to your account!')
            return

        # Otherwise, we're done! We can now send the createAvatarResponse update
        # through the GameServicesManager & set this operation's state to Off.
        self.gameServicesManager.air.writeServerEvent('avatar-created', self.avId, self.target, self.dna.encode('hex'),
                                                      self.index)
        self.gameServicesManager.sendUpdateToAccountId(self.target, 'createAvatarResponse', [self.avId])
        self.demand('Off')


class AcknowledgeNameOperation(AvatarOperation):
    notify = DirectNotifyGlobal.directNotify.newCategory('AcknowledgeNameFSM')
    postAccountState = 'GetTargetAvatar'

    def __init__(self, gameServicesManager, target):
        AvatarOperation.__init__(self, gameServicesManager, target)
        self.avId = None

    def enterStart(self, avId):
        # Store this value & move on to RetrieveAccount.
        self.avId = avId
        self.demand('RetrieveAccount')

    def enterGetTargetAvatar(self):
        # Make sure that the target avatar is part of the account:
        if self.avId not in self.avList:
            # The sender tried to acknowledge name on an avatar not on the account!
            # Kill the connection.
            self.demand('Kill', 'Tried to acknowledge name on an avatar not in the account!')
            return

        # We can now query the database for the avatar. self.__handleAvatar is the
        # callback which will be called upon the completion of queryObject.
        self.gameServicesManager.air.dbInterface.queryObject(self.gameServicesManager.air.dbId, self.avId,
                                                             self.__handleAvatar)

    def __handleAvatar(self, dclass, fields):
        if dclass != self.gameServicesManager.air.dclassesByName['DistributedToonUD']:
            # This dclass is not a valid avatar! Kill the connection.
            self.demand('Kill', 'One of the account\'s avatars is invalid!')
            return

        # Process the WishNameState change.
        wishNameState = fields['WishNameState'][0]
        wishName = fields['WishName'][0]
        name = fields['setName'][0]

        if wishNameState == 'APPROVED':
            wishNameState = 'LOCKED'
            name = wishName
            wishName = ''
        elif wishNameState == 'REJECTED':
            wishNameState = 'OPEN'
            wishName = ''
        else:
            # The sender is trying to acknowledge name on avatar in invalid state! Kill the connection.
            self.demand('Kill', 'Tried to acknowledge name on an avatar in invalid state (%s) !' % wishNameState)
            return

        # We can now update the avatar object in the database with the changes!
        self.gameServicesManager.air.dbInterface.updateObject(self.gameServicesManager.air.dbId, self.avId,
                                                              self.gameServicesManager.air.dclassesByName[
                                                                  'DistributedToonUD'],
                                                              {'WishNameState': (wishNameState,),
                                                               'WishName': (wishName,),
                                                               'setName': (name,)},
                                                              {'WishNameState': fields['WishNameState'],
                                                               'WishName': fields['WishName'],
                                                               'setName': fields['setName']})

        # We're done. We can now send off the acknowledgeAvatarNameResponse update
        # through the GameServicesManager, and set this operation's state to Off.
        self.gameServicesManager.sendUpdateToAccountId(self.target, 'acknowledgeAvatarNameResponse', [])
        self.demand('Off')


class TTGameServicesManagerUD(GameServicesManagerUD):
    notify = DirectNotifyGlobal.directNotify.newCategory('TTGameServicesManagerUD')
    avatarDclass = 'DistributedToonUD'

    def __init__(self, air):
        GameServicesManagerUD.__init__(self, air)
        self.nameGenerator = None

    def announceGenerate(self):
        GameServicesManagerUD.announceGenerate(self)

        # This is for processing name patterns.
        self.nameGenerator = NameGenerator()

    def setNamePattern(self, avId, p1, f1, p2, f2, p3, f3, p4, f4):
        # Someone has used a pattern name; run a SetNamePatternOperation.
        self.runOperation(SetNamePatternOperation, avId, [(p1, f1), (p2, f2),
                                                          (p3, f3), (p4, f4)])

    def setNameTyped(self, avId, name):
        # Someone has typed a name; run a SetNameTypedOperation.
        self.runOperation(SetNameTypedOperation, avId, name)

    def createAvatar(self, dna, index):
        # Someone wants to create a new avatar;
        # run a CreateAvatarOperation.
        self.runOperation(CreateAvatarOperation, dna, index)

    def acknowledgeAvatarName(self, avId):
        # Someone has acknowledged their name; run an AcknowledgeNameOperation.
        self.runOperation(AcknowledgeNameOperation, avId)
