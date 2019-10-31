from direct.directnotify import DirectNotifyGlobal
from toontown.classicchars.DistributedMickeyAI import DistributedMickeyAI

class DistributedWitchMinnieAI(DistributedMickeyAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedWitchMinnieAI")

