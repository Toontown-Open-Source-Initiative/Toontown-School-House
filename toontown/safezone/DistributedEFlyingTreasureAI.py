from direct.directnotify import DirectNotifyGlobal

from toontown.safezone.DistributedSZTreasureAI import DistributedSZTreasureAI


class DistributedEFlyingTreasureAI(DistributedSZTreasureAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedEFlyingTreasureAI')
