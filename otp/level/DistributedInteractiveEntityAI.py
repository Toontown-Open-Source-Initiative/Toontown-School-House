from direct.directnotify import DirectNotifyGlobal
from otp.level.DistributedEntityAI import DistributedEntityAI

class DistributedInteractiveEntityAI(DistributedEntityAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedInteractiveEntityAI")

    def setAvatarInteract(self, todo0):
        pass

    def requestInteract(self):
        pass

    def rejectInteract(self):
        pass

    def requestExit(self):
        pass

    def avatarExit(self, todo0):
        pass

    def setState(self, todo0, todo1):
        pass

