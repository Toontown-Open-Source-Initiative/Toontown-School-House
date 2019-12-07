from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals
from toontown.safezone import TreasurePlannerAI
import DistributedFactoryTreasureAI
import FactoryGameGlobals
import random


class FactoryTreasurePlannerAI(TreasurePlannerAI.TreasurePlannerAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('FactoryTreasurePlannerAI')

    def __init__(self, zoneId, callback):
        self.numPlayers = 0
        TreasurePlannerAI.TreasurePlannerAI.__init__(self, zoneId, DistributedFactoryTreasureAI.DistributedFactoryTreasureAI, callback)
        return None

    def initSpawnPoints(self):
        self.spawnPoints = []
        totalSpawnPoints = FactoryGameGlobals.FactoryGameTreasureSpawns[:]
        for spawn in xrange(FactoryGameGlobals.FactoryGameTreasuresWanted):
            random.shuffle(totalSpawnPoints)
            randSpawn = totalSpawnPoints.pop(0)
            self.spawnPoints.append(randSpawn)
        return self.spawnPoints

