import time

from direct.directnotify import DirectNotifyGlobal

from toontown.estate import GardenGlobals
from toontown.estate.DistributedPlantBaseAI import DistributedPlantBaseAI
from toontown.estate.FlowerBase import FlowerBase

ONE_DAY = 86400

# X position offsets for flowers & flower plots:
FLOWER_X_OFFSETS = (None, (0,), (-1.5, 1.5), (-3.4, 0, 3.5))


class DistributedFlowerAI(DistributedPlantBaseAI, FlowerBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedFlowerAI')

    def setTypeIndex(self, value):
        DistributedPlantBaseAI.setTypeIndex(self, value)
        FlowerBase.setSpecies(self, value)

    def setFlowerIndex(self, flowerIndex):
        self.flowerIndex = flowerIndex

    def getFlowerIndex(self):
        return self.flowerIndex

    def calculate(self, lastCheck):
        now = int(time.time())
        if lastCheck == 0:
            lastCheck = now

        grown = 0

        # Water level
        elapsed = now - lastCheck
        while elapsed > ONE_DAY:
            if self.waterLevel >= 0:
                grown += 1

            elapsed -= ONE_DAY
            self.waterLevel -= 1

        self.waterLevel = max(self.waterLevel, -2)

        # Growth level
        maxGrowth = self.growthThresholds[2]
        newGrowthLevel = min(self.growthLevel + grown, maxGrowth)
        self.setGrowthLevel(newGrowthLevel)
        self.lastCheck = now - elapsed
        self.update()

    def update(self):
        mapData = map(list, self.mgr.data['flowers'])
        mapData[self.getFlowerIndex()] = [self.getSpecies(), self.waterLevel, self.lastCheck, self.getGrowthLevel(),
                                          self.getVariety()]
        self.mgr.data['flowers'] = mapData
        self.mgr.update()

    def removeItem(self, usingPickAll=0):
        avId = self.air.getAvatarIdFromSender()
        if not avId:
            return

        if not usingPickAll:
            if avId != self.ownerDoId:
                self.air.writeServerEvent('suspicious', avId, 'tried to remove someone else\'s flower!')
                return

            self.d_setMovie(GardenGlobals.MOVIE_REMOVE)

        action = 'remove'
        if self.getGrowthLevel() >= self.growthThresholds[2]:
            action = 'pick'

        def handleRemoveItem(task):
            if not self.air:
                return

            av = self.air.doId2do.get(self.ownerDoId)
            if not av:
                return

            plot = self.mgr.placePlot(self.getFlowerIndex())
            plot.setFlowerIndex(self.getFlowerIndex())
            plot.setPlot(self.plot)
            plot.setOwnerIndex(self.ownerIndex)

            # <hack>
            index = (0, 1, 2, 2, 2, 3, 3, 3, 4, 4)[self.getFlowerIndex()]
            idx = (0, 0, 0, 1, 2, 0, 1, 2, 0, 1)[self.getFlowerIndex()]
            zOffset = 1.2
            gardenBox = self.mgr._estateBoxes[index]
            xOffset = FLOWER_X_OFFSETS[gardenBox.getTypeIndex()][idx]
            plot.setPos(gardenBox, 0, 0, 0)
            plot.setZ(gardenBox, zOffset)
            plot.setX(gardenBox, xOffset)
            plot.setH(gardenBox, 0)
            # </hack>

            plot.generateWithRequired(self.zoneId)
            if not usingPickAll:
                plot.d_setMovie(GardenGlobals.MOVIE_FINISHREMOVING, avId)
                plot.d_setMovie(GardenGlobals.MOVIE_CLEAR, avId)

            self.air.writeServerEvent('%s-flower' % action, avId, plot=self.plot)
            self.requestDelete()
            self.mgr.flowers.remove(self)
            mapData = map(list, self.mgr.data['flowers'])
            mapData[self.getFlowerIndex()] = self.mgr.getNullPlant()
            self.mgr.data['flowers'] = mapData
            self.mgr.update()
            if action == 'pick':
                av.b_setShovelSkill(av.getShovelSkill() + self.getValue())
                av.addFlowerToBasket(self.getSpecies(), self.getVariety())

            if task:
                return task.done

        if usingPickAll:
            handleRemoveItem(None)
        else:
            taskMgr.doMethodLater(7, handleRemoveItem, self.uniqueName('handle-remove-item'))
