from panda3d.core import *
from direct.interval.IntervalGlobal import *
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals
import FactoryGameGlobals
from toontown.toonbase import TTLocalizer
from otp.level import DistributedEntity
from direct.task.Task import Task
from toontown.suit import Suit
from direct.fsm import FSM

class DistributedFactoryCog(DistributedEntity.DistributedEntity, Suit.Suit, FSM.FSM):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedFactoryCog')

    def __init__(self, cr):
        try:
            self.DistributedFactoryCog_initialized
        except:
            self.DistributedFactoryCog_initialized = 1
        DistributedEntity.DistributedEntity.__init__(self, cr)

    def announceGenerate(self):
        DistributedEntity.DistributedEntity.announceGenerate(self)

    def generate(self):
        DistributedEntity.DistributedEntity.generate(self)

    def disable(self):
        DistributedEntity.DistributedEntity.disable(self)

