from direct.directnotify import DirectNotifyGlobal
from toontown.classicchars.DistributedDaleAI import DistributedDaleAI

class DistributedJailbirdDaleAI(DistributedDaleAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedJailbirdDaleAI")

