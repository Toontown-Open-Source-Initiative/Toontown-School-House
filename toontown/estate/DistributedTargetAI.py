from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

from toontown.estate import CannonGlobals


class DistributedTargetAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedTargetAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.enabled = 0
        self.power = 0
        self.time = 0
        self.highScore = 0

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)
        taskMgr.doMethodLater(10, self.__startGame, self.uniqueName('startGame'))

    def __startGame(self, task):
        self.enabled = 1
        self.power = 1
        self.time = CannonGlobals.CANNON_TIMEOUT
        self.d_setState()
        taskMgr.doMethodLater(self.time, self.__endGame, self.uniqueName('endGame'))
        return task.done

    def __endGame(self, task):
        for avId in self.air.estateMgr.zone2toons.get(self.zoneId, []):
            av = self.air.doId2do.get(avId)
            if av:
                if av.zoneId == self.zoneId:
                    av.toonUp(self.getToonUpAmount())

        self.enabled = 0
        self.power = 0
        self.time = 0
        self.sendUpdate('setReward', [self.getToonUpAmount()])
        self.d_setState()
        taskMgr.doMethodLater(10, self.__startGame, self.uniqueName('startGame'))
        return task.done

    def getPosition(self):
        return 0, 0, 40

    def d_setState(self):
        self.sendUpdate('setState', self.getState())

    def getState(self):
        return self.enabled, self.getToonUpAmount(), self.time

    def setResult(self, avId):
        if self.enabled and avId:
            self.power += 1
            self.time = int(CannonGlobals.CANNON_TIMEOUT / self.power)
            taskMgr.remove(self.uniqueName('endGame'))
            taskMgr.doMethodLater(self.time, self.__endGame, self.uniqueName('endGame'))
            self.d_setState()

    def setBonus(self, bonus):
        pass

    def setCurPinballScore(self, avId, score, multiplier):
        av = self.air.doId2do.get(avId)
        if not av:
            return

        newScore = score * multiplier
        if newScore > self.highScore:
            self.highScore = newScore
            self.sendUpdate('setPinballHiScorer', [av.getName()])
            self.sendUpdate('setPinballHiScore', [newScore])

    def delete(self):
        DistributedObjectAI.delete(self)
        taskMgr.remove(self.uniqueName('startGame'))
        taskMgr.remove(self.uniqueName('endGame'))

    def getToonUpAmount(self):
        return 2 ** self.power
