from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectUD import DistributedObjectUD

class StatusDatabaseUD(DistributedObjectUD):
    notify = DirectNotifyGlobal.directNotify.newCategory("StatusDatabaseUD")

    def requestOfflineAvatarStatus(self, todo0):
        pass

    def recvOfflineAvatarStatus(self, todo0, todo1):
        pass

