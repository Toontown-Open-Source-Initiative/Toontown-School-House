from panda3d.core import *
from direct.directnotify.DirectNotifyGlobal import directNotify
from toontown.cogdominium.DistCogdoLevelGameAI import DistCogdoLevelGameAI
from toontown.cogdominium.DistCogdoCraneAI import DistCogdoCraneAI
from toontown.cogdominium import CogdoCraneGameConsts as GameConsts
from toontown.cogdominium.CogdoCraneGameBase import CogdoCraneGameBase
from toontown.cogdominium import CogdoGameConsts
from toontown.cogdominium.DistCogdoCraneMoneyBagAI import DistCogdoCraneMoneyBagAI
from toontown.cogdominium.DistCogdoCraneCogAI import DistCogdoCraneCogAI
from toontown.cogdominium.DistCogdoCraneObstacleAI import DistCogdoCraneObstacleAI
from toontown.suit.SuitDNA import SuitDNA
import random


class DistCogdoCraneGameAI(DistCogdoLevelGameAI, CogdoCraneGameBase, NodePath):
    notify = directNotify.newCategory('DistCogdoCraneGameAI')

    def __init__(self, air, interior):
        DistCogdoLevelGameAI.__init__(self, air, interior)
        NodePath.__init__(self, uniqueName('CraneGameAI'))

        self._cranes = [None] * CogdoGameConsts.MaxPlayers
        self._moneyBags = [None] * 4

        self._moneyBagsRespawnEvent = None
        self._gameDoneEvent = None
        self._finishDoneEvent = None

    def delete(self):
        DistCogdoLevelGameAI.delete(self)
        self.removeNode()

    def enterLoaded(self):
        DistCogdoLevelGameAI.enterLoaded(self)

        self.scene = NodePath('scene')
        cn = CollisionNode('walls')
        cs = CollisionSphere(0, 0, 0, 13)
        cn.addSolid(cs)
        cs = CollisionInvSphere(0, 0, 0, 42)
        cn.addSolid(cs)
        self.attachNewNode(cn)

        for i in xrange(CogdoGameConsts.MaxPlayers):
            crane = DistCogdoCraneAI(self.air, self, i)
            crane.generateWithRequired(self.zoneId)
            self._cranes[i] = crane

        for i in xrange(len(self._moneyBags)):
            mBag = DistCogdoCraneMoneyBagAI(self.air, self, i)
            mBag.generateWithRequired(self.zoneId)
            self._moneyBags[i] = mBag

    def exitLoaded(self):
        for i in xrange(len(self._moneyBags)):
            if self._moneyBags[i]:
                self._moneyBags[i].requestDelete()
                self._moneyBags[i] = None

        for i in xrange(CogdoGameConsts.MaxPlayers):
            if self._cranes[i]:
                self._cranes[i].requestDelete()
                self._cranes[i] = None

        DistCogdoLevelGameAI.exitLoaded(self)

    def enterGame(self):
        DistCogdoLevelGameAI.enterGame(self)
        for i in xrange(self.getNumPlayers()):
            self._cranes[i].request('Controlled', self.getToonIds()[i])

        for i in xrange(len(self._moneyBags)):
            if self._moneyBags[i]:
                self._moneyBags[i].request('Initial')

        self._moneyBagsRespawnEvent = taskMgr.doMethodLater(GameConsts.MoneyBagsRespawnRate, self.generateMoneyBags,
                                                             self.uniqueName('generateMoneyBags'))

        self._cog = DistCogdoCraneCogAI(self.air, self, self.getDroneCogDNA(), random.randrange(4), globalClock.getFrameTime())
        self._cog.generateWithRequired(self.zoneId)

        self._spotlightObstacle = DistCogdoCraneObstacleAI(self.air, self)
        self._spotlightObstacle.generateWithRequired(self.zoneId)

        self._scheduleGameDone()

    def generateMoneyBags(self, task):
        moneyBagsToSpawn = range(0, 4)
        availableMoneyBags = []
        for moneyBag in self._moneyBags:
            index = moneyBag.getIndex()
            availableMoneyBags.append(index)

        moneyBagsToSpawn = [x for x in moneyBagsToSpawn if x not in availableMoneyBags]

        for i in moneyBagsToSpawn:
            mBag = DistCogdoCraneMoneyBagAI(self.air, self, i)
            mBag.generateWithRequired(self.zoneId)
            mBag.request('Join')
            self._moneyBags.insert(i, mBag)

        return task.again

    def _scheduleGameDone(self):
        timeLeft = GameConsts.Settings.GameDuration.get() - (globalClock.getRealTime() - self.getStartTime())
        if timeLeft > 0:
            self._gameDoneEvent = taskMgr.doMethodLater(timeLeft, self._gameDoneDL, self.uniqueName('boardroomGameDone'))
        else:
            self._gameDoneDL()

    def exitGame(self):
        self._cog.requestDelete()
        self._cog = None

        self._spotlightObstacle.requestDelete()
        del self._spotlightObstacle

        taskMgr.remove(self._moneyBagsRespawnEvent)
        self._moneyBagsRespawnEvent = None

        taskMgr.remove(self._gameDoneEvent)
        self._gameDoneEvent = None

    def _gameDoneDL(self, task = None):
        self._handleGameFinished()
        return task.done

    def enterFinish(self):
        DistCogdoLevelGameAI.enterFinish(self)
        self._finishDoneEvent = taskMgr.doMethodLater(10.0, self._finishDoneDL, self.uniqueName('boardroomFinishDone'))

    def exitFinish(self):
        taskMgr.remove(self._finishDoneEvent)
        self._finishDoneEvent = None

    def _finishDoneDL(self, task):
        self.announceGameDone()
        return task.done
