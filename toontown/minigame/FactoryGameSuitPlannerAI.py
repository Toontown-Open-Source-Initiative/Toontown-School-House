from direct.distributed.ClockDelta import *
from direct.showbase import DirectObject
from direct.directnotify import DirectNotifyGlobal
from direct.task import Task
import DistributedFactoryCogAI
from toontown.suit import SuitDNA
import FactoryGameGlobals
import random


class FactoryGameSuitPlannerAI(DirectObject.DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('FactoryGameSuitPlannerAI')

    def __init__(self, zoneId, callback):
        self.zoneId = zoneId
        self.suitConstructor = DistributedFactoryCogAI.DistributedFactoryCogAI
        self.callback = callback
        self.initSpawnPoints()
        self.suits = []
        for spawnPoint in self.spawnPoints:
            self.suits.append(None)

        self.deleteTaskNames = set()
        return

    def initSpawnPoints(self):
        self.spawnPoints = []
        totalSpawnPoints = FactoryGameGlobals.FactoryGameCogSpawns[:]
        for spawn in xrange(FactoryGameGlobals.FactoryGameCogsWanted):
            random.shuffle(totalSpawnPoints)
            randSpawn = totalSpawnPoints.pop(0)
            self.spawnPoints.append(randSpawn)
        return self.spawnPoints

    def numSuits(self):
        counter = 0
        for suit in self.suits:
            if suit:
                counter += 1

        return counter

    def countEmptySpawnPoints(self):
        counter = 0
        for suit in self.suits:
            if suit == None:
                counter += 1

        return counter

    def nthEmptyIndex(self, n):
        emptyCounter = -1
        spawnPointCounter = -1
        while emptyCounter < n:
            spawnPointCounter += 1
            if self.suits[spawnPointCounter] == None:
                emptyCounter += 1

        return spawnPointCounter

    def findIndexOfSuitId(self, suitId):
        counter = 0
        for suit in self.suits:
            if suit == None:
                pass
            elif suitId == suit.getDoId():
                return counter
            counter += 1

        return

    def placeAllSuits(self):
        index = 0
        for suit in self.suits:
            if not suit:
                self.placeSuit(index)
            index += 1

    def placeSuit(self, index):
        spawnPoint = self.spawnPoints[index]
        suit = self.suitConstructor(simbase.air, self, spawnPoint[0], spawnPoint[1], spawnPoint[2])
        suit.dna = SuitDNA.SuitDNA()
        dnaChoice = random.choice(FactoryGameGlobals.FactoryGameSuitDNAList)
        suit.dna.newSuit(dnaChoice)
        suit.generateWithRequired(self.zoneId)
        suit.b_setPosition(spawnPoint[0], spawnPoint[1], spawnPoint[2])
        suit.d_setState('Stand')
        self.suits[index] = suit

    def deleteSuitSoon(self, suit):
        taskName = suit.uniqueName('deletingSuit')
        taskMgr.doMethodLater(5, self.__deleteSuitNow, taskName, extraArgs=(suit, taskName))
        self.deleteTaskNames.add(taskName)

    def deleteAllSuitsNow(self):
        for suit in self.suits:
            if suit:
                suit.requestDelete()

        for taskName in self.deleteTaskNames:
            tasks = taskMgr.getTasksNamed(taskName)
            if len(tasks):
                suit = tasks[0].getArgs()[0]
                suit.requestDelete()
                taskMgr.remove(taskName)

        self.deleteTaskNames = set()
        self.treasures = []
        for spawnPoint in self.spawnPoints:
            self.treasures.append(None)

        return

    def __deleteSuitNow(self, suit, taskName):
        suit.requestDelete()
        self.deleteTaskNames.remove(taskName)

    def hitAttempt(self, avId, suitId):
        index = self.findIndexOfSuitId(suitId)
        if index == None:
            pass
        else:
            av = simbase.air.doId2do.get(avId)
            if av == None:
                simbase.air.writeServerEvent('suspicious', avId, 'FactoryGameSuitPlannerAI.hitAttempt unknown avatar')
                self.notify.warning('avid: %s does not exist' % avId)
            else:
                suit = self.suits[index]
                self.suits[index] = None
                if self.callback:
                    self.callback(avId)
                suit.d_setHit(avId)

