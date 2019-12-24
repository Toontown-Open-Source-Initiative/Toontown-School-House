from otp.ai.AIBaseGlobal import *
from direct.distributed.ClockDelta import *
from direct.directnotify import DirectNotifyGlobal
from toontown.battle import SuitBattleGlobals
from toontown.toonbase import ToontownGlobals
import DistributedSuitBaseAI
import random
from direct.fsm import ClassicFSM, State
from direct.fsm import State

class DistributedSellbotBossHardmodeSuitAI(DistributedSuitBaseAI.DistributedSuitBaseAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedSellbotBossHardmodeSuitAI')

    def __init__(self, air, suitPlanner):
        DistributedSuitBaseAI.DistributedSuitBaseAI.__init__(self, air, suitPlanner)
        self.fsm = ClassicFSM.ClassicFSM('DistributedSellbotBossHardmodeSuitAI', [
            State.State('Off',
                        self.enterOff,
                        self.exitOff, [
                            'InitialFall',
                            'Swoop',
                            'neutral']),
            State.State('InitialFall',
                        self.enterInitialFall,
                        self.exitInitialFall, [
                            'neutral']),
            State.State('Swoop',
                        self.enterSwoop,
                        self.exitSwoop, [
                            'neutral',
                            'Fall'
                        ]),
            State.State('neutral',
                        self.enterNeutral,
                        self.exitNeutral, [
                            'Fall',
                            'PreThrowAttack',
                            'Stunned']),
            State.State('Fall',
                        self.enterFall,
                        self.exitFall, [
                            'neutral',
                            'Death']),
            State.State('Death',
                        self.enterDeath,
                        self.exitDeath, [
                            'Off'])],
                                         'Off', 'Off')
        self.fsm.enterInitialState()

    def delete(self):
        self.notify.debug('delete %s' % self.doId)
        self.ignoreAll()
        DistributedSuitBaseAI.DistributedSuitBaseAI.delete(self)
        self.notify.debug('setting self.boss to None')
        self.boss = None
        self.fsm = None
        return

    def getPosHpr(self):
        return (self.getX(),
         self.getY(),
         self.getZ(),
         self.getH(),
         self.getP(),
         self.getR())

    def getConfrontPosHpr(self):
        return (self.confrontPos, self.confrontHpr)

    def _logDeath(self, toonId):
        pass

    def doNextTarget(self):
        chanceToDoTarget = ToontownGlobals.SellbotBossHardmodeSuitTargetChance
        action = random.randrange(1, 101)
        if action <= chanceToDoTarget:
            self.doTargetLock()
        else:
            return

    def d_doAttack(self, x1, y1, z1, x2, y2, z2):
        self.notify.debug('doAttack: x1=%.2f y1=%.2f z2=%.2f x2=%.2f y2=%.2f z2=%.2f' % (x1,
         y1,
         z1,
         x2,
         y2,
         z2))
        self.sendUpdate('doAttack', [x1,
         y1,
         z1,
         x2,
         y2,
         z2])

    def setBoss(self, boss):
        self.boss = boss

    def hitByToon(self):
        self.notify.debug('I got hit by a toon')
        self.setState('fall')

    def requestDamageToon(self):
        avId = self.air.getAvatarIdFromSender()
        avatar = self.air.doId2do.get(avId)
        if avatar:
            self.boss.damageToon(avatar, ToontownGlobals.SellbotBossHardmodeSuitDamage)

    def enterInitialFall(self):
        pass

    def exitInitialFall(self):
        pass

    def enterSwoop(self):
        pass

    def exitSwoop(self):
        pass

    def enterNeutral(self):
        pass

    def exitNeutral(self):
        pass

    def enterFall(self):
        pass

    def exitFall(self):
        pass

    def enterDeath(self):
        pass

    def exitDeath(self):
        pass

