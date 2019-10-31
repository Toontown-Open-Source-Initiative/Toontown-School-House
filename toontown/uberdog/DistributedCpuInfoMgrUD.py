from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD

class DistributedCpuInfoMgrUD(DistributedObjectGlobalUD):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedCpuInfoMgrUD")

    def setCpuInfoToUd(self, todo0, todo1, todo2, todo3):
        pass

