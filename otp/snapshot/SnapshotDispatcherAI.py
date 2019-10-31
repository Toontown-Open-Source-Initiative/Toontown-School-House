from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class SnapshotDispatcherAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("SnapshotDispatcherAI")

    def online(self):
        pass

    def requestRender(self, todo0):
        pass

    def avatarDeleted(self, todo0):
        pass

    def requestNewWork(self, todo0):
        pass

    def errorFetchingAvatar(self, todo0, todo1):
        pass

    def errorRenderingAvatar(self, todo0, todo1):
        pass

    def renderSuccessful(self, todo0, todo1):
        pass

