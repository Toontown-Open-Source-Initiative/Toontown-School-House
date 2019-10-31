from direct.directnotify import DirectNotifyGlobal
from toontown.classicchars.DistributedDonaldAI import DistributedDonaldAI

class DistributedFrankenDonaldAI(DistributedDonaldAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedFrankenDonaldAI")

