from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class DistributedScavengerHuntTargetAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedScavengerHuntTargetAI")

    def attemptScavengerHunt(self):
        pass

