from otp.ai.AIBaseGlobal import *
from direct.directnotify import DirectNotifyGlobal
from toontown.battle import SuitBattleGlobals
from toontown.suit import DistributedSuitBaseAI
from toontown.suit import SuitDialog

class DistributedFactoryCogAI(DistributedSuitBaseAI.DistributedSuitBaseAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedFactoryCogAI')

    def __init__(self, air, suitPlanner, x, y, z):
        DistributedSuitBaseAI.DistributedSuitBaseAI.__init__(self, air, None)
        self.chasing = 0
        self.pos = (x, y, z)
        self.suitPlanner = suitPlanner
        return

    def generate(self):
        DistributedSuitBaseAI.DistributedSuitBaseAI.generate(self)

    def setAlert(self, avId):
        if avId == self.air.getAvatarIdFromSender():
            av = self.air.doId2do.get(avId)
            if av:
                self.chasing = avId
                self.sendUpdate('setConfrontToon', [avId])

    def setStrayed(self):
        if self.chasing > 0:
            self.chasing = 0
            self.sendUpdate('setReturn', [])

    def resume(self):
        self.notify.debug('Suit %s resume' % self.doId)
        self.sendUpdate('setReturn', [])
        return None

    def requestHit(self):
        avId = self.air.getAvatarIdFromSender()
        self.suitPlanner.hitAttempt(avId, self.getDoId())

    def validAvatar(self, av):
        return 1

    def d_setHit(self, avId):
        self.sendUpdate('setHit', [avId])

    def getPosition(self):
        return self.pos

    def setPosition(self, x, y, z):
        self.pos = (x, y, z)

    def b_setPosition(self, x, y, z):
        self.setPosition(x, y, z)
        self.d_setPosition(x, y, z)

    def d_setPosition(self, x, y, z):
        self.sendUpdate('setPosition', [x, y, z])

    def d_setState(self, state):
        self.sendUpdate('setState', [state])

    def enterStand(self):
        pass

    def exitStand(self):
        pass

    def enterChase(self):
        pass

    def exitChase(self):
        pass

    def enterReturn(self):
        pass

    def exitReturn(self):
        pass

