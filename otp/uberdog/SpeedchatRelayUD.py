from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectUD import DistributedObjectUD

class SpeedchatRelayUD(DistributedObjectUD):
    notify = DirectNotifyGlobal.directNotify.newCategory("SpeedchatRelayUD")

    def forwardSpeedchat(self, todo0, todo1, todo2, todo3, todo4, todo5):
        pass

