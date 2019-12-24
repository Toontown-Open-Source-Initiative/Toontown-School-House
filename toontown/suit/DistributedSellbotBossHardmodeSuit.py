from panda3d.core import *
from direct.interval.IntervalGlobal import *
from direct.fsm import ClassicFSM, State
from direct.fsm import State
from direct.directnotify import DirectNotifyGlobal
import DistributedSuitBase
from toontown.toonbase import ToontownGlobals
from toontown.battle import MovieUtil
from toontown.battle import BattleProps

class DistributedSellbotBossHardmodeSuit(DistributedSuitBase.DistributedSuitBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedSellbotBossHardmodeSuit')

    def __init__(self, cr):
        try:
            self.DistributedSuit_initialized
        except:
            self.DistributedSuit_initialized = 1
            DistributedSuitBase.DistributedSuitBase.__init__(self, cr)
            self.activeIntervals = {}
            self.boss = None
            self.flyLoopTrack = Sequence()
            self.propellerTrack = Sequence()
            self.fsm = ClassicFSM.ClassicFSM('DistributedSellbotBossHardmodeSuit', [
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
                                'neutral']),
                State.State('Death',
                            self.enterDeath,
                            self.exitDeath, [
                                'Off'])],
                'Off', 'Off')
            self.fsm.enterInitialState()

        return

    def generate(self):
        self.notify.debug('DSBHS.generate:')
        DistributedSuitBase.DistributedSuitBase.generate(self)

    def announceGenerate(self):
        DistributedSuitBase.DistributedSuitBase.announceGenerate(self)
        self.notify.debug('DSBHS.announceGenerate')
        colNode = self.find('**/distAvatarCollNode*')
        colNode.setTag('pieCode', str(ToontownGlobals.PieCodeLawyer))
        self.hideName()
        self.setPickable(False)

    def disable(self):
        self.notify.debug('DistributedSuit %d: disabling' % self.getDoId())
        self.setState('Off')
        DistributedSuitBase.DistributedSuitBase.disable(self)
        self.cleanupIntervals()
        self.boss = None
        return

    def delete(self):
        try:
            self.DistributedSuit_deleted
        except:
            self.DistributedSuit_deleted = 1
            self.notify.debug('DistributedSuit %d: deleting' % self.getDoId())
            del self.fsm
            del self.flyLoopTrack
            DistributedSuitBase.DistributedSuitBase.delete(self)

    def initializeBodyCollisions(self, collIdStr):
        DistributedSuitBase.DistributedSuitBase.initializeBodyCollisions(self, collIdStr)
        self.sSphere = CollisionSphere(0, 0, 0, 2.85)
        name = self.uniqueName('toonSphere')
        self.sSphereNode = CollisionNode(name)
        self.sSphereNode.addSolid(self.sSphere)
        self.sSphereNodePath = self.attachNewNode(self.sSphereNode)
        self.sSphereNodePath.hide()
        self.sSphereBitMask = ToontownGlobals.WallBitmask
        self.sSphereNode.setCollideMask(self.sSphereBitMask)
        self.sSphere.setTangible(0)

    def cleanupIntervals(self):
        for interval in self.activeIntervals.values():
            interval.finish()

        self.activeIntervals = {}

    def clearInterval(self, name, finish = 1):
        if name in self.activeIntervals:
            ival = self.activeIntervals[name]
            if finish:
                ival.finish()
            else:
                ival.pause()
            if name in self.activeIntervals:
                del self.activeIntervals[name]
        else:
            self.notify.debug('interval: %s already cleared' % name)

    def setBossCogId(self, bossCogId):
        self.bossCogId = bossCogId
        self.boss = base.cr.doId2do[bossCogId]

    def requestStateIfNotInFlux(self, state):
        if not self.fsm._ClassicFSM__internalStateInFlux:
            self.fsm.request(state)

    def makeFlyLoopTrack(self):
        track = Sequence()
        currentPos = self.getPos()
        upPos = currentPos + (0, 0, 5)
        downPos = currentPos - (0, 0, 5)
        track.append(Sequence(LerpPosInterval(self, 4, upPos, blendType='easeInOut'), LerpPosInterval(self, 4, downPos, blendType='easeInOut')))
        return track

    def makePropellerTrack(self):
        self.pose('landing', 0)
        self.propellerTrack = Sequence(ActorInterval(self.prop, 'propeller', startFrame=8, endFrame=25))

    def makeSwoopTrack(self, toon):
        track = Parallel()
        currentPos = self.getPos()
        downPos = toon.getPos()
        endX = downPos.x + 10
        downTrack = Sequence(LerpPosInterval(self, 2, (currentPos.x, currentPos.y, downPos.z), blendType='easeIn'), LerpPosInterval(self, 2, ))
        return track

    def attachPropeller(self):
        if self.prop == None:
            self.prop = BattleProps.globalPropPool.getProp('propeller')
            head = self.suit.find('**/joint_head')
            self.prop.reparentTo(head)
        return

    def detachPropeller(self):
        if self.prop:
            self.prop.cleanup()
            self.prop.removeNode()
            self.prop = None
        return

    def requestDamageToon(self):
        self.sendUpdate('requestDamageToon')

    def enterInitialFall(self):
        self.makePropellerTrack()
        self.propellerTrack.loop()

    def enterNeutral(self):
        self.notify.debug('enterNeutral')
        self.notify.debug('DistributedSellbotBossHardmodeSuit: Neutral')
        if not self.flyLoopTrack:
            self.flyLoopTrack = self.makeFlyLoopTrack()
            self.flyLoopTrack.loop()

    def exitNeutral(self):
        self.notify.debug('exitNeutral')

    def exitInitialFall(self):
        pass

    def enterSwoop(self):
        pass

    def exitSwoop(self):
        pass

    def enterFall(self):
        pass

    def exitFall(self):
        pass

    def enterDeath(self):
        pass

    def exitDeath(self):
        pass

