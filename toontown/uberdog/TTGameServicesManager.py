from direct.directnotify import DirectNotifyGlobal

from otp.uberdog.GameServicesManager import GameServicesManager


class TTGameServicesManager(GameServicesManager):
    notify = DirectNotifyGlobal.directNotify.newCategory('TTGameServicesManager')

    def sendSetNamePattern(self, avId, p1, f1, p2, f2, p3, f3, p4, f4, callback):
        self._callback = callback
        self.sendUpdate('setNamePattern', [avId, p1, f1, p2, f2, p3, f3, p4, f4])

    def namePatternResponse(self, avId, status):
        self._callback(avId, status)

    def sendSetNameTyped(self, avId, name, callback):
        self._callback = callback
        self.sendUpdate('setNameTyped', [avId, name])

    def nameTypedResponse(self, avId, status):
        self._callback(avId, status)

    def sendCreateAvatar(self, avDNA, _, index):
        self.sendUpdate('createAvatar', [avDNA.makeNetString(), index])

    def createAvatarResponse(self, avId):
        messenger.send('nameShopCreateAvatarDone', [avId])

    def sendAcknowledgeAvatarName(self, avId, callback):
        self._callback = callback
        self.sendUpdate('acknowledgeAvatarName', [avId])

    def acknowledgeAvatarNameResponse(self):
        self._callback()
