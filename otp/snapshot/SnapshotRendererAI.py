from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class SnapshotRendererAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("SnapshotRendererAI")

    def online(self):
        pass

    def requestRender(self, todo0, todo1, todo2):
        pass

