from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectGlobalAI import DistributedObjectGlobalAI

class DistributedCpuInfoMgrAI(DistributedObjectGlobalAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedCpuInfoMgrAI")

    def setCpuInfoToUd(self, todo0, todo1, todo2, todo3):
        pass

