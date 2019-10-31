from direct.directnotify import DirectNotifyGlobal
from toontown.classicchars.DistributedGoofySpeedwayAI import DistributedGoofySpeedwayAI

class DistributedSuperGoofyAI(DistributedGoofySpeedwayAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedSuperGoofyAI")

