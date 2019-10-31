from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectUD import DistributedObjectUD

class SnapshotRendererUD(DistributedObjectUD):
    notify = DirectNotifyGlobal.directNotify.newCategory("SnapshotRendererUD")

    def online(self):
        pass

    def requestRender(self, todo0, todo1, todo2):
        pass

