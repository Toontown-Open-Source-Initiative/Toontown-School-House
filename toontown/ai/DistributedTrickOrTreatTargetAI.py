from direct.directnotify import DirectNotifyGlobal
from toontown.ai.DistributedScavengerHuntTargetAI import DistributedScavengerHuntTargetAI

class DistributedTrickOrTreatTargetAI(DistributedScavengerHuntTargetAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedTrickOrTreatTargetAI")

