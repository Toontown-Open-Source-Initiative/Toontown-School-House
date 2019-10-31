from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectUD import DistributedObjectUD

class SnapshotDispatcherUD(DistributedObjectUD):
    notify = DirectNotifyGlobal.directNotify.newCategory("SnapshotDispatcherUD")

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

