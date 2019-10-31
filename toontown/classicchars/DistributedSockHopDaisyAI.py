from direct.directnotify import DirectNotifyGlobal
from toontown.classicchars.DistributedDaisyAI import DistributedDaisyAI

class DistributedSockHopDaisyAI(DistributedDaisyAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedSockHopDaisyAI")

