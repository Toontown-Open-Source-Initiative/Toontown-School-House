from panda3d.core import *
from direct.interval.IntervalGlobal import *
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals, TTLocalizer
import FactoryGameGlobals
from toontown.suit import DistributedSuitBase
from direct.task.Task import Task
from toontown.suit import Suit
from direct.fsm import ClassicFSM, State


class DistributedFactoryCog(DistributedSuitBase.DistributedSuitBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedFactoryCog')

    def __init__(self, cr):
        try:
            self.DistributedFactoryCog_initialized
        except:
            self.DistributedFactoryCog_initialized = 1
            DistributedSuitBase.DistributedSuitBase.__init__(self, cr)
            self.fsm = ClassicFSM.ClassicFSM('DistributedFactoryCog', [State.State('Off', self.enterOff, self.exitOff, ['Stand']),
                                              State.State('Stand', self.enterStand, self.exitStand, ['Chase']),
                                              State.State('Chase', self.enterChase, self.exitChase, ['Return']),
                                              State.State('Return', self.enterReturn, self.exitReturn, ['Stand', 'Chase'])], 'Off', 'Off')
            self.path = None
            self.walkTrack = None
            self.chaseTrack = None
            self.returnTrack = None
            self.fsm.enterInitialState()
            self.chasing = 0
            self.startChasePos = 0
            self.startChaseH = 0

    def generate(self):
        DistributedSuitBase.DistributedSuitBase.generate(self)

    def announceGenerate(self):
        DistributedSuitBase.DistributedSuitBase.announceGenerate(self)
        self.hideName()
        self.setPickable(False)

    def disable(self):
        self.notify.debug('DistributedSuit %d: disabling' % self.getDoId())
        self.setState('Off')
        DistributedSuitBase.DistributedSuitBase.disable(self)
        return

    def delete(self):
        try:
            self.DistributedSuit_deleted
        except:
            self.DistributedSuit_deleted = 1
            self.notify.debug('DistributedSuit %d: deleting' % self.getDoId())
            del self.fsm
            DistributedSuitBase.DistributedSuitBase.delete(self)

    def enterStand(self):
        self.loop('neutral', 0)

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

    def setHit(self, avId):
        if avId == 0:
            return
        if self.fly or avId != base.localAvatar.getDoId():
            self.handleHit(avId)

    def handleHit(self, avId):
        pass

    def getParentNodePath(self):
        return render

    def setPosition(self, x, y, z):
        self.reparentTo(self.getParentNodePath())
        self.setPos(x, y, z)

