from direct.directnotify import DirectNotifyGlobal

from toontown.safezone.DistributedSZTreasureAI import DistributedSZTreasureAI


class DistributedETreasureAI(DistributedSZTreasureAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedETreasureAI')
