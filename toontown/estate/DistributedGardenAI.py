from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class DistributedGardenAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedGardenAI")

    def sendNewProp(self, todo0, todo1, todo2, todo3):
        pass

