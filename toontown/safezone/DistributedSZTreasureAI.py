import DistributedTreasureAI
from toontown.toonbase import ToontownGlobals

class DistributedSZTreasureAI(DistributedTreasureAI.DistributedTreasureAI):

    def __init__(self, air, treasurePlanner, x, y, z):
        DistributedTreasureAI.DistributedTreasureAI.__init__(self, air, treasurePlanner, x, y, z)
        self.healAmount = treasurePlanner.healAmount

    def validAvatar(self, av):
        return av.hp > 0 and av.hp < av.maxHp

    def d_setGrab(self, avId):
        DistributedTreasureAI.DistributedTreasureAI.d_setGrab(self, avId)
        if avId in self.air.doId2do:
            av = self.air.doId2do[avId]
            if av.hp > 0 and av.hp < av.maxHp:
                if ToontownGlobals.VALENTINES_DAY in simbase.air.holidayManager.currentHolidays:
                    av.toonUp(self.healAmount * 2)
                else:
                    av.toonUp(self.healAmount)
