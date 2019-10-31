from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI


class DistributedDirectoryAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedDirectoryAI')

    def setParentingRules(self, todo0, todo1):
        pass
