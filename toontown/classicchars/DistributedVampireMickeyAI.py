from direct.directnotify import DirectNotifyGlobal
from toontown.classicchars.DistributedMickeyAI import DistributedMickeyAI

class DistributedVampireMickeyAI(DistributedMickeyAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedVampireMickeyAI")

