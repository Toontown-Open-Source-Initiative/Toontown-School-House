from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectUD import DistributedObjectUD

class PlayerFriendsManagerUD(DistributedObjectUD):
    notify = DirectNotifyGlobal.directNotify.newCategory("PlayerFriendsManagerUD")

    def requestInvite(self, todo0, todo1, todo2):
        pass

    def invitationFrom(self, todo0, todo1):
        pass

    def retractInvite(self, todo0):
        pass

    def invitationResponse(self, todo0, todo1, todo2):
        pass

    def requestDecline(self, todo0, todo1):
        pass

    def requestDeclineWithReason(self, todo0, todo1, todo2):
        pass

    def requestRemove(self, todo0, todo1):
        pass

    def secretResponse(self, todo0):
        pass

    def rejectSecret(self, todo0):
        pass

    def rejectUseSecret(self, todo0):
        pass

    def updatePlayerFriend(self, todo0, todo1, todo2):
        pass

    def removePlayerFriend(self, todo0):
        pass

