from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectUD import DistributedObjectUD

class DistributedAvatarUD(DistributedObjectUD):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedAvatarUD")

    def setName(self, todo0):
        pass

    def friendsNotify(self, todo0, todo1):
        pass

    def checkAvOnShard(self, todo0):
        pass

    def confirmAvOnShard(self, todo0, todo1):
        pass

