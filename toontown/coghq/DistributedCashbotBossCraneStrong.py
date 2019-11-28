from direct.task import Task
from toontown.toonbase import ToontownGlobals
from panda3d.core import *
from panda3d.direct import *
from panda3d.physics import *
from direct.distributed.ClockDelta import *
import DistributedCashbotBossCrane

class DistributedCashbotBossCraneStrong(DistributedCashbotBossCrane.DistributedCashbotBossCrane):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedCashbotBossCraneStrong')
    emptySlideSpeed = 20
    emptyRotateSpeed = 40

    def __init__(self, cr):
        DistributedCashbotBossCrane.DistributedCashbotBossCrane.__init__(self, cr)
        self.cableLength = 25
