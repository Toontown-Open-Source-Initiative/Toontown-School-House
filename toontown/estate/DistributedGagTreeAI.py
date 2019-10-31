import time

from direct.directnotify import DirectNotifyGlobal

from toontown.estate import GardenGlobals
from toontown.estate.DistributedPlantBaseAI import DistributedPlantBaseAI

ONE_DAY = 86400
PROBLEM_WILTED = 1
PROBLEM_NOT_GROWN = 2
PROBLEM_HARVESTED_LATELY = 4


class DistributedGagTreeAI(DistributedPlantBaseAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedGagTreeAI")
    GrowRate = config.GetBool('trees-grow-rate', 2)

    def __init__(self, mgr):
        DistributedPlantBaseAI.__init__(self, mgr)
        self.wilted = 0
        self.waterLevel = 0
        self.lastCheck = 0
        self.lastHarvested = 0
        self.treeIndex = 0

    def announceGenerate(self):
        DistributedPlantBaseAI.announceGenerate(self)
        messenger.send(self.getEventName('generate'))

    def setWilted(self, wilted):
        self.wilted = wilted

    def d_setWilted(self, wilted):
        self.sendUpdate('setWilted', [wilted])

    def b_setWilted(self, wilted):
        self.setWilted(wilted)
        self.d_setWilted(wilted)

    def getWilted(self):
        return self.wilted

    def setTreeIndex(self, treeIndex):
        self.treeIndex = treeIndex

    def getTreeIndex(self):
        return self.treeIndex

    def calculate(self, lastHarvested, lastCheck):
        now = int(time.time())
        if lastCheck == 0:
            lastCheck = now

        grown = 0

        # Water level
        elapsed = now - lastCheck
        while elapsed > ONE_DAY:
            if self.waterLevel >= 0:
                grown += self.GrowRate

            elapsed -= ONE_DAY
            self.waterLevel -= 1

        self.waterLevel = max(self.waterLevel, -2)

        # Growth level
        maxGrowth = self.growthThresholds[2]
        newGrowthLevel = min(self.growthLevel + grown, maxGrowth)
        self.setGrowthLevel(newGrowthLevel)
        self.setWilted(self.waterLevel == -2)
        self.lastCheck = now - elapsed
        self.lastHarvested = lastHarvested
        self.update()

    def calcDependencies(self):
        if self.getWilted():
            return

        track, value = GardenGlobals.getTreeTrackAndLevel(self.typeIndex)
        while value:
            value -= 1
            if not self.mgr.hasTree(track, value):
                self.b_setWilted(1)
                continue

            tree = self.mgr.getTree(track, value)
            if not tree:
                self.b_setWilted(1)
                continue

            self.accept(self.getEventName('going-down', id(self.mgr.gardenMgr)), self.ignoreAll)
            self.accept(self.getEventName('remove', track * 7 + value), self.calcDependencies)

    def getEventName(self, string, typeIndex=None):
        typeIndex = typeIndex if typeIndex is not None else self.typeIndex
        return 'garden-%d-%d-%s' % (self.ownerDoId, typeIndex, string)

    def delete(self):
        messenger.send(self.getEventName('remove'))
        self.ignoreAll()
        DistributedPlantBaseAI.delete(self)

    def update(self):
        mapData = map(list, self.mgr.data['trees'])
        mapData[self.getTreeIndex()] = [self.typeIndex, self.waterLevel, self.lastCheck, self.getGrowthLevel(),
                                        self.lastHarvested]
        self.mgr.data['trees'] = mapData
        self.mgr.update()

    def isFruiting(self):
        problem = 0
        if self.getWilted():
            problem |= PROBLEM_WILTED

        if self.getGrowthLevel() < self.growthThresholds[2]:
            problem |= PROBLEM_NOT_GROWN

        if (self.lastCheck - self.lastHarvested) < ONE_DAY:
            problem |= PROBLEM_HARVESTED_LATELY

        return problem

    def getFruiting(self):
        return self.isFruiting() == 0

    def requestHarvest(self):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)
        if not av:
            return

        if avId != self.ownerDoId:
            self.air.writeServerEvent('suspicious', avId, 'tried to harvest someone else\'s tree!')
            return

        problem = self.isFruiting()
        if problem:
            self.air.writeServerEvent('suspicious', avId, 'tried to harvest a tree that\'s not fruiting!',
                                      problem=problem)
            return

        harvested = 0
        track, level = GardenGlobals.getTreeTrackAndLevel(self.typeIndex)
        while av.inventory.addItem(track, level) > 0 and harvested < 10:
            harvested += 1

        av.d_setInventory(av.getInventory())
        self.lastHarvested = int(time.time())
        self.d_setMovie(GardenGlobals.MOVIE_HARVEST)
        self.update()

    def removeItem(self):
        avId = self.air.getAvatarIdFromSender()
        if not avId:
            return

        self.d_setMovie(GardenGlobals.MOVIE_REMOVE)

        def handleRemove(task):
            if not self.air:
                return

            plot = self.mgr.placePlot(self.getTreeIndex())
            plot.setPlot(self.plot)
            plot.setPos(self.getPos())
            plot.setH(self.getH())
            plot.setOwnerIndex(self.ownerIndex)
            plot.generateWithRequired(self.zoneId)
            plot.d_setMovie(GardenGlobals.MOVIE_FINISHREMOVING, avId)
            plot.d_setMovie(GardenGlobals.MOVIE_CLEAR, avId)
            self.air.writeServerEvent('remove-tree', avId, plot=self.plot)
            self.requestDelete()
            self.mgr.trees.remove(self)
            mapData = map(list, self.mgr.data['trees'])
            mapData[self.getTreeIndex()] = self.mgr.getNullPlant()
            self.mgr.data['trees'] = mapData
            self.mgr.update()
            self.mgr.reconsiderAvatarOrganicBonus()
            return task.done

        taskMgr.doMethodLater(7, handleRemove, self.uniqueName('do-remove'))

    def doGrow(self, grown):
        maxGrowth = self.growthThresholds[2]
        newGrowthLevel = max(0, min(self.growthLevel + grown, maxGrowth))
        oldGrowthLevel = self.growthLevel
        self.b_setGrowthLevel(newGrowthLevel)
        self.update()
        return newGrowthLevel - oldGrowthLevel
