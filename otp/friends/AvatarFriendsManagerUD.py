from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectUD import DistributedObjectUD

class AvatarFriendsManagerUD(DistributedObjectUD):
    notify = DirectNotifyGlobal.directNotify.newCategory("AvatarFriendsManagerUD")

    def online(self):
        pass

    def requestInvite(self, todo0):
        pass

    def friendConsidering(self, todo0):
        pass

    def invitationFrom(self, todo0, todo1):
        pass

    def retractInvite(self, todo0):
        pass

    def rejectInvite(self, todo0, todo1):
        pass

    def requestRemove(self, todo0):
        pass

    def rejectRemove(self, todo0, todo1):
        pass

    def updateAvatarFriend(self, todo0, todo1):
        pass

    def removeAvatarFriend(self, todo0):
        pass

    def updateAvatarName(self, todo0, todo1):
        pass

    def avatarOnline(self, todo0, todo1, todo2, todo3, todo4, todo5, todo6):
        pass

    def avatarOffline(self, todo0):
        pass

