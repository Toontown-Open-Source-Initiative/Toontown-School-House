import random

from toontown.safezone.DistributedEFlyingTreasureAI import DistributedEFlyingTreasureAI
from toontown.safezone.TreasurePlannerAI import TreasurePlannerAI


class EFlyingTreasurePlannerAI(TreasurePlannerAI):

    def __init__(self, zoneId, callback=None):
        self.healAmount = 9
        self.spawnPoints = []
        TreasurePlannerAI.__init__(self, zoneId, DistributedEFlyingTreasureAI, callback)

    def initSpawnPoints(self):
        z = 35
        self.spawnPoints = [(random.randint(100, 300) - 200,
                             random.randint(100, 300) - 200,
                             z) for _ in xrange(20)]
        return self.spawnPoints
