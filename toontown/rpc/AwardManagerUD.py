from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD

class AwardManagerUD(DistributedObjectGlobalUD):
    notify = DirectNotifyGlobal.directNotify.newCategory("AwardManagerUD")

    def giveAwardToToon(self, todo0, todo1, todo2, todo3, todo4, todo5):
        pass

