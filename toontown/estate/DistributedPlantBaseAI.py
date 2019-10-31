from direct.directnotify import DirectNotifyGlobal

from toontown.estate import GardenGlobals
from toontown.estate.DistributedLawnDecorAI import DistributedLawnDecorAI


class DistributedPlantBaseAI(DistributedLawnDecorAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedPlantBaseAI")

    def __init__(self, mgr):
        DistributedLawnDecorAI.__init__(self, mgr)
        self.typeIndex = 0
        self.waterLevel = 0
        self.growthLevel = 0
        self.attributes = None
        self.growthThresholds = None

    def setTypeIndex(self, typeIndex):
        self.typeIndex = typeIndex
        self.attributes = GardenGlobals.PlantAttributes[typeIndex]
        self.growthThresholds = self.attributes['growthThresholds']

    def d_setTypeIndex(self, typeIndex):
        self.sendUpdate('setTypeIndex', [typeIndex])

    def b_setTypeIndex(self, typeIndex):
        self.setTypeIndex(typeIndex)
        self.d_setTypeIndex(typeIndex)

    def getTypeIndex(self):
        return self.typeIndex

    def setWaterLevel(self, waterLevel):
        self.waterLevel = waterLevel

    def d_setWaterLevel(self, waterLevel):
        self.sendUpdate('setWaterLevel', [waterLevel])

    def b_setWaterLevel(self, waterLevel):
        self.setWaterLevel(waterLevel)
        self.d_setWaterLevel(waterLevel)

    def getWaterLevel(self):
        return self.waterLevel

    def setGrowthLevel(self, growthLevel):
        self.growthLevel = growthLevel

    def d_setGrowthLevel(self, growthLevel):
        self.sendUpdate('setGrowthLevel', [growthLevel])

    def b_setGrowthLevel(self, growthLevel):
        self.setGrowthLevel(growthLevel)
        self.d_setGrowthLevel(growthLevel)

    def getGrowthLevel(self):
        return self.growthLevel

    def waterPlant(self):
        avId = self.air.getAvatarIdFromSender()
        if not avId:
            return

        av = self.air.doId2do.get(avId)
        if not av:
            return

        waterLevel = max(1, self.getWaterLevel() + av.getWateringCan() + 1)
        waterLevel = min(20, waterLevel)
        self.b_setWaterLevel(waterLevel)
        self.d_setMovie(GardenGlobals.MOVIE_WATER)
        self.update()

    def waterPlantDone(self):
        avId = self.air.getAvatarIdFromSender()
        if not avId:
            return

        av = self.air.doId2do.get(avId)
        if not av:
            return

        if self.waterLevel < 6:
            av.b_setWateringCanSkill(av.getWateringCanSkill() + 1)
        else:
            av.b_setWateringCanSkill(av.getWateringCanSkill())

        self.d_setMovie(GardenGlobals.MOVIE_CLEAR)

    def update(self):
        pass
