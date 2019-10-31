from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectUD import DistributedObjectUD

class OtpAvatarManagerUD(DistributedObjectUD):
    notify = DirectNotifyGlobal.directNotify.newCategory("OtpAvatarManagerUD")

    def online(self):
        pass

    def requestAvatarList(self, todo0):
        pass

    def rejectAvatarList(self, todo0):
        pass

    def avatarListResponse(self, todo0):
        pass

    def requestAvatarSlot(self, todo0, todo1, todo2):
        pass

    def rejectAvatarSlot(self, todo0, todo1, todo2):
        pass

    def avatarSlotResponse(self, todo0, todo1):
        pass

    def requestPlayAvatar(self, todo0, todo1, todo2):
        pass

    def rejectPlayAvatar(self, todo0, todo1):
        pass

    def playAvatarResponse(self, todo0, todo1, todo2, todo3):
        pass

    def rejectCreateAvatar(self, todo0):
        pass

    def createAvatarResponse(self, todo0, todo1, todo2, todo3):
        pass

    def requestRemoveAvatar(self, todo0, todo1, todo2, todo3):
        pass

    def rejectRemoveAvatar(self, todo0):
        pass

    def removeAvatarResponse(self, todo0, todo1):
        pass

    def requestShareAvatar(self, todo0, todo1, todo2, todo3):
        pass

    def rejectShareAvatar(self, todo0):
        pass

    def shareAvatarResponse(self, todo0, todo1, todo2):
        pass

