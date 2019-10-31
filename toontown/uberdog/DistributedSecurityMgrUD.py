from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD

class DistributedSecurityMgrUD(DistributedObjectGlobalUD):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedSecurityMgrUD")

    def requestAccountId(self, todo0, todo1, todo2):
        pass

    def requestAccountIdResponse(self, todo0, todo1):
        pass

