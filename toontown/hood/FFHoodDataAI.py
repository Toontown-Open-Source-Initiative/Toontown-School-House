from direct.directnotify import DirectNotifyGlobal
import HoodDataAI, ZoneUtil
from toontown.toonbase import ToontownGlobals
from toontown.safezone import OZTreasurePlannerAI
from panda3d.core import *
from panda3d.toontown import *
import string



class FFHoodDataAI(HoodDataAI.HoodDataAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('FFHoodDataAI')
    
    def __init__(self,air,zoneId=None):
        hoodId = ToontownGlobals.FunnyFarm
        if zoneId is None:
            zoneId = hoodId
        HoodDataAI.HoodDataAI.__init__(self,air,zoneId,hoodId)
    
    def startup(self):
        HoodDataAI.HoodDataAI.startup(self)
        trolley = DistributedTrolleyAI.DistributedTrolleyAI(self.air)
        trolley.generateWithRequired(self.zoneId)
        trolley.start()
        self.addDistObj(trolley)
        self.treasurePlanner = DLTreasurePlannerAI.DLTreasurePlannerAI(self.zoneId)
        self.treasurePlanner.start()