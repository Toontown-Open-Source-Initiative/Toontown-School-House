import datetime
import json
import os
import random

from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.distributed.PyDatagram import *

from otp.otpbase import OTPGlobals


class FriendManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('FriendManagerAI')
    serverDataFolder = simbase.config.GetString('server-data-folder', '')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.currentContext = 0
        self.requests = {}
        self.shard = str(air.districtId)
        self.filename = self.getFilename()
        self.tfCodes = self.loadTrueFriendCodes()
        taskMgr.add(self.__trueFriendCodesTask, 'tf-codes-clear-task')

    def friendQuery(self, inviteeId):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)
        if not av:
            return

        if inviteeId not in self.air.doId2do:
            self.air.writeServerEvent('suspicious', avId, 'Player tried to friend a player that does not exist!')
            return

        context = self.currentContext
        self.requests[context] = [[avId, inviteeId], 'friendQuery']
        self.currentContext += 1
        self.sendUpdateToAvatarId(inviteeId, 'inviteeFriendQuery', [avId, av.getName(), av.getDNAString(), context])

    def cancelFriendQuery(self, context):
        avId = self.air.getAvatarIdFromSender()
        if not avId:
            return

        if context not in self.requests:
            self.air.writeServerEvent('suspicious', avId, 'Player tried to cancel a request that doesn\'t exist!')
            return

        if avId != self.requests[context][0][0]:
            self.air.writeServerEvent('suspicious', avId, 'Player tried to cancel someone else\'s request!')
            return

        self.requests[context][1] = 'cancelled'
        self.sendUpdateToAvatarId(self.requests[context][0][1], 'inviteeCancelFriendQuery', [context])

    def inviteeFriendConsidering(self, yesNo, context):
        avId = self.air.getAvatarIdFromSender()
        if not avId:
            return

        if context not in self.requests:
            self.air.writeServerEvent('suspicious', avId,
                                      'Player tried to consider a friend request that doesn\'t exist!')
            return

        if avId != self.requests[context][0][1]:
            self.air.writeServerEvent('suspicious', avId, 'Player tried to consider for someone else!')
            return

        if self.requests[context][1] != 'friendQuery':
            self.air.writeServerEvent('suspicious', avId, 'Player tried to reconsider friend request!')
            return

        if yesNo != 1:
            self.sendUpdateToAvatarId(self.requests[context][0][0], 'friendConsidering', [yesNo, context])
            del self.requests[context]
            return

        self.requests[context][1] = 'friendConsidering'
        self.sendUpdateToAvatarId(self.requests[context][0][0], 'friendConsidering', [yesNo, context])

    def inviteeFriendResponse(self, response, context):
        avId = self.air.getAvatarIdFromSender()
        if not avId:
            return

        if context not in self.requests:
            self.air.writeServerEvent('suspicious', avId,
                                      'Player tried to respond to a friend request that doesn\'t exist!')
            return

        if avId != self.requests[context][0][1]:
            self.air.writeServerEvent('suspicious', avId, 'Player tried to respond to someone else\'s request!')
            return

        if self.requests[context][1] == 'cancelled':
            self.air.writeServerEvent('suspicious', avId, 'Player tried to respond to a non-active friend request!')
            return

        self.sendUpdateToAvatarId(self.requests[context][0][0], 'friendResponse', [response, context])
        if response == 1:
            requestedAv = self.air.doId2do.get(self.requests[context][0][1])
            if not requestedAv:
                del self.requests[context]
                return

            requesterAv = self.air.doId2do.get(self.requests[context][0][0])
            if not requesterAv:
                del self.requests[context]
                return

            dg = PyDatagram()
            dg.addServerHeader(self.GetPuppetConnectionChannel(requestedAv.getDoId()), self.air.ourChannel,
                               CLIENTAGENT_DECLARE_OBJECT)
            dg.addUint32(requesterAv.getDoId())
            dg.addUint16(self.air.dclassesByName['DistributedToonAI'].getNumber())
            self.air.send(dg)

            dg = PyDatagram()
            dg.addServerHeader(self.GetPuppetConnectionChannel(requesterAv.getDoId()), self.air.ourChannel,
                               CLIENTAGENT_DECLARE_OBJECT)
            dg.addUint32(requestedAv.getDoId())
            dg.addUint16(self.air.dclassesByName['DistributedToonAI'].getNumber())
            self.air.send(dg)

            requestedAv.extendFriendsList(requesterAv.getDoId(), 0)
            requesterAv.extendFriendsList(requestedAv.getDoId(), 0)

            requestedAv.d_setFriendsList(requestedAv.getFriendsList())
            requesterAv.d_setFriendsList(requesterAv.getFriendsList())

        del self.requests[context]

    def inviteeAcknowledgeCancel(self, context):
        avId = self.air.getAvatarIdFromSender()
        if not avId:
            return

        if context not in self.requests:
            self.air.writeServerEvent('suspicious', avId,
                                      'Player tried to acknowledge the cancel of a friend request that doesn\'t exist!')
            return

        if avId != self.requests[context][0][1]:
            self.air.writeServerEvent('suspicious', avId, 'Player tried to acknowledge someone else\'s cancel!')
            return

        if self.requests[context][1] != 'cancelled':
            self.air.writeServerEvent('suspicious', avId, 'Player tried to cancel non-cancelled request!')
            return

        del self.requests[context]

    def requestSecret(self):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)
        if not av:
            return

        if len(av.getFriendsList()) >= OTPGlobals.MaxFriends:
            self.d_requestSecretResponse(avId, 0, '')
        else:
            day = datetime.datetime.now().day
            tfCode = self.generateTrueFriendCode()
            self.tfCodes[tfCode] = (avId, day)
            self.updateTrueFriendCodesFile()
            self.d_requestSecretResponse(avId, 1, tfCode)
            self.air.writeServerEvent('tf-code-requested', avId=avId, tfCode=tfCode)

    def generateTrueFriendCode(self):
        chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        def randomChar():
            return random.choice(chars)

        tfCode = '%s%s%s %s%s%s' % (randomChar(), randomChar(), randomChar(), randomChar(), randomChar(), randomChar())
        return tfCode

    def d_requestSecretResponse(self, avId, result, secret):
        if not avId:
            return

        self.sendUpdateToAvatarId(avId, 'requestSecretResponse', [result, secret])

    def submitSecret(self, secret):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)
        if not av:
            return

        secretInfo = self.tfCodes.get(secret)
        if not secretInfo:
            self.d_submitSecretResponse(avId, 0, 0)
            return

        friendId = secretInfo[0]
        friend = self.air.doId2do.get(friendId)
        if av:
            if friend:
                if avId == friendId:
                    self.d_submitSecretResponse(avId, 3, 0)
                    self.removeSecret(secret)
                elif len(friend.getFriendsList()) >= OTPGlobals.MaxFriends or len(
                        av.getFriendsList()) >= OTPGlobals.MaxFriends:
                    self.d_submitSecretResponse(avId, 2, friendId)
                else:
                    dg = PyDatagram()
                    dg.addServerHeader(self.GetPuppetConnectionChannel(friendId), self.air.ourChannel,
                                       CLIENTAGENT_DECLARE_OBJECT)
                    dg.addUint32(avId)
                    dg.addUint16(self.air.dclassesByName['DistributedToonAI'].getNumber())
                    self.air.send(dg)

                    dg = PyDatagram()
                    dg.addServerHeader(self.GetPuppetConnectionChannel(avId), self.air.ourChannel,
                                       CLIENTAGENT_DECLARE_OBJECT)
                    dg.addUint32(friendId)
                    dg.addUint16(self.air.dclassesByName['DistributedToonAI'].getNumber())
                    self.air.send(dg)

                    friend.extendFriendsList(avId, 1)
                    av.extendFriendsList(friendId, 1)

                    friend.d_setFriendsList(friend.getFriendsList())
                    av.d_setFriendsList(av.getFriendsList())

                    self.d_submitSecretResponse(avId, 1, friendId)
                    self.removeSecret(secret)
            else:
                # Friend is offline!
                def handleAvatar(dclass, fields):
                    if dclass != self.air.dclassesByName['DistributedToonAI']:
                        return

                    newFriendsList = []
                    oldFriendsList = fields['setFriendsList'][0]
                    if len(oldFriendsList) >= OTPGlobals.MaxFriends:
                        self.d_submitSecretResponse(avId, 2, friendId)
                        return

                    for oldFriend in oldFriendsList:
                        newFriendsList.append(oldFriend)

                    newFriendsList.append((avId, 1))
                    self.air.dbInterface.updateObject(self.air.dbId, friendId,
                                                      self.air.dclassesByName['DistributedToonAI'],
                                                      {'setFriendsList': [newFriendsList]})
                    av.extendFriendsList(friendId, 1)
                    av.d_setFriendsList(av.getFriendsList())
                    self.d_submitSecretResponse(avId, 1, friendId)
                    self.removeSecret(secret)

                self.air.dbInterface.queryObject(self.air.dbId, friendId, handleAvatar)

        self.air.writeServerEvent('tf-code-submitted', avId=avId, friendId=friendId, tfCode=secret)

    def d_submitSecretResponse(self, avId, result, friendId):
        if not avId:
            return

        self.sendUpdateToAvatarId(avId, 'submitSecretResponse', [result, friendId])

    def removeSecret(self, secret):
        if secret in self.tfCodes:
            del self.tfCodes[secret]
            self.updateTrueFriendCodesFile()

    def getFilename(self):
        return '%s%s%s%s.json' % (self.serverDataFolder, 'trueFriendCodes/', 'trueFriendCodes_', self.shard)

    def loadTrueFriendCodes(self):
        try:
            tfCodesFile = open(self.filename, 'r')
            tfCodesData = json.load(tfCodesFile)
            return tfCodesData
        except:
            return {}

    def updateTrueFriendCodesFile(self):
        try:
            if not os.path.exists(os.path.dirname(self.filename)):
                os.makedirs(os.path.dirname(self.filename))

            tfCodesFile = open(self.filename, 'w')
            tfCodesFile.seek(0)
            json.dump(self.tfCodes, tfCodesFile)
            tfCodesFile.close()
        except:
            pass

    def __trueFriendCodesTask(self, task):
        for tfCode in self.tfCodes.keys():
            tfCodeInfo = self.tfCodes[tfCode]
            tfCodeDay = tfCodeInfo[1]
            today = datetime.datetime.now().day
            if tfCodeDay + 2 == today:
                self.notify.info('Removing 2-day-old True Friend code: %s' % tfCode)
                self.removeSecret(tfCode)

        return task.again
