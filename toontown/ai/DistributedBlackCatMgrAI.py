from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class DistributedBlackCatMgrAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedBlackCatMgrAI")

    def setAvId(self, todo0):
        pass

    def doBlackCatTransformation(self):
        pass

