from DistributedMinigameAI import *
from direct.fsm import ClassicFSM, State
from direct.fsm import State
from direct.task import Task
from toontown.toonbase import ToontownGlobals
import FactoryTreasurePlannerAI
import FactoryGameSuitPlannerAI
import FactoryGameGlobals
import random
TTG = ToontownGlobals


class DistributedFactoryGameAI(DistributedMinigameAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedFactoryGameAI')
    DURATION = FactoryGameGlobals.FactoryGameDuration

    def __init__(self, air, minigameId):
        try:
            self.DistributedFactoryGameAI_initialized
        except:
            self.DistributedFactoryGameAI_initialized = 1
            DistributedMinigameAI.__init__(self, air, minigameId)
            self.gameFSM = ClassicFSM.ClassicFSM('DistributedFactoryGameAI', [State.State('inactive', self.enterInactive, self.exitInactive, ['play']), State.State('play', self.enterPlay, self.exitPlay, ['cleanup']), State.State('cleanup', self.enterCleanup, self.exitCleanup, ['inactive'])], 'inactive', 'inactive')
            self.treasureScores = {}
            self.addChildGameFSM(self.gameFSM)
        return

    def delete(self):
        self.notify.debug('delete')
        del self.gameFSM
        DistributedMinigameAI.delete(self)

    def setGameReady(self):
        self.notify.debug('setGameReady')
        DistributedMinigameAI.setGameReady(self)
        for avId in self.avIdList:
            self.treasureScores[avId] = 0

    def setGameStart(self, timestamp):
        self.notify.debug('setGameStart')
        DistributedMinigameAI.setGameStart(self, timestamp)
        self.gameFSM.request('play')

    def setGameAbort(self):
        self.notify.debug('setGameAbort')
        if self.gameFSM.getCurrentState():
            self.gameFSM.request('cleanup')
        DistributedMinigameAI.setGameAbort(self)

    def gameOver(self):
        self.notify.debug('gameOver')
        self.gameFSM.request('cleanup')
        DistributedMinigameAI.gameOver(self)

    def enterInactive(self):
        self.notify.debug('enterInactive')

    def exitInactive(self):
        pass

    def enterPlay(self):
        self.notify.debug('enterPlay')
        taskMgr.doMethodLater(self.DURATION, self.timerExpired, self.taskName('gameTimer'))
        self.treasurePlanner = FactoryTreasurePlannerAI.FactoryTreasurePlannerAI(self.zoneId, self.treasureGrabCallback)
        self.treasurePlanner.placeAllTreasures()
        self.suitPlanner = FactoryGameSuitPlannerAI.FactoryGameSuitPlannerAI(self.zoneId, self.suitHitCallback)
        self.suitPlanner.placeAllSuits()

    def timerExpired(self, task):
        self.notify.debug('timer expired')
        self.gameOver()
        return Task.done

    def exitPlay(self):
        pass

    def treasureGrabCallback(self, avId):
        if avId not in self.avIdList:
            self.air.writeServerEvent('suspicious', avId, 'FactoryGameAI.treasureGrabCallback non-player avId')
            return
        self.treasureScores[avId] += 1
        self.notify.debug('treasureGrabCallback: ' + str(avId) + ' grabbed a treasure, new score: ' + str(self.treasureScores[avId]))
        self.scoreDict[avId] = self.treasureScores[avId]
        treasureScoreParams = []
        for avId in self.avIdList:
            treasureScoreParams.append(self.treasureScores[avId])

        self.sendUpdate('setTreasureScore', [treasureScoreParams])

    def suitHitCallback(self, avId):
        if avId not in self.avIdList:
            self.air.writeServerEvent('suspipcious', avId, 'FactoryGameAI.suitHitCallback non-player avId')
            return
        av = simbase.air.doId2do.get(avId)
        self.treasureScores[avId] -= 5
        if self.treasureScores[avId] < 0:
            self.treasureScores[avId] = 0
        self.notify.debug('suitHitCallback: ' + str(avId) + ' hit a suit, new score: ' + str(self.treasureScores[avId]))
        self.scoreDict[avId] = self.treasureScores[avId]
        treasureScoreParams = []
        for avId in self.avIdList:
            treasureScoreParams.append(self.treasureScores[avId])

        self.sendUpdate('setTreasureScore', [treasureScoreParams])

    def enterCleanup(self):
        self.notify.debug('enterCleanup')
        self.gameFSM.request('inactive')

    def exitCleanup(self):
        pass

