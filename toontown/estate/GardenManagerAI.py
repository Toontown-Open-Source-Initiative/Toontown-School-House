import json
import os

from direct.directnotify import DirectNotifyGlobal

from toontown.estate import GardenGlobals
from toontown.estate.DistributedAnimatedStatuaryAI import DistributedAnimatedStatuaryAI
from toontown.estate.DistributedChangingStatuaryAI import DistributedChangingStatuaryAI
from toontown.estate.DistributedFlowerAI import DistributedFlowerAI
from toontown.estate.DistributedGagTreeAI import DistributedGagTreeAI
from toontown.estate.DistributedGardenBoxAI import DistributedGardenBoxAI
from toontown.estate.DistributedGardenPlotAI import DistributedGardenPlotAI
from toontown.estate.DistributedStatuaryAI import DistributedStatuaryAI
from toontown.estate.DistributedToonStatuaryAI import DistributedToonStatuaryAI

# Structure for NULL_PLANT:
# [planted, waterLevel, lastCheck, growthLevel, optional]
NULL_PLANT = [-1, -1, 0, 0, 0]
NULL_TREES = [NULL_PLANT] * 8
NULL_FLOWERS = [NULL_PLANT] * 10
NULL_STATUARY = 0

# NULL_DATA is just a dictionary containing all the null values that are
# defined above; this makes up a default garden with nothing in it.
NULL_DATA = {'flowers': NULL_FLOWERS, 'trees': NULL_TREES, 'statuary': NULL_STATUARY}

# X position offsets for flowers & flower plots:
FLOWER_X_OFFSETS = (None, (0,), (-1.5, 1.5), (-3.4, 0, 3.5))


class GardenAI:
    notify = DirectNotifyGlobal.directNotify.newCategory('GardenAI')
    WANT_FLOWERS = True
    WANT_TREES = True
    WANT_STATUARY = True

    def __init__(self, air, gardenMgr, avId):
        self.air = air
        self.gardenMgr = gardenMgr
        self.avId = avId
        self.estate = None
        self._estateBoxes = None
        self.trees = set()
        self.flowers = set()
        self.objects = set()
        self.fileName = 'garden_%s.json' % avId
        self.filePath = 'backups/gardens/'
        try:
            with open(self.filePath + self.fileName, 'r') as f:
                self.data = json.load(f)

            self.dbExists = True
        except:
            self.data = NULL_DATA.copy()
            self.dbExists = False

        if not self.dbExists:
            # Use self.update() to setup initial db:
            self.update()

        self.data.pop('_id', None)

    def destroy(self):
        messenger.send('garden-%d-%d-going-down' % (id(self.gardenMgr), self.avId))
        for tree in self.trees:
            tree.requestDelete()

        for flower in self.flowers:
            flower.requestDelete()

        for obj in self.objects:
            obj.requestDelete()

        self.air = None
        self.estate = None

    def load(self, estate):
        self.estate = estate
        if self.avId not in estate.activeToons:
            self.notify.warning('Garden associated with unknown avatar %d, deleting...' % self.avId)
            return False

        houseIndex = estate.activeToons.index(self.avId)
        if self.WANT_FLOWERS:
            estateBoxIndex = 0
            estateBoxes = []
            estateBoxData = GardenGlobals.estateBoxes[houseIndex]
            for x, y, h, estateBoxType in estateBoxData:
                gardenBox = DistributedGardenBoxAI(self)
                gardenBox.setTypeIndex(estateBoxType)
                gardenBox.setPos(x, y, 0)
                gardenBox.setH(h)
                gardenBox.setOwnerIndex(houseIndex)
                gardenBox.generateWithRequired(estate.zoneId)
                self.objects.add(gardenBox)
                estateBoxes.append(gardenBox)
                estateBoxIndex += 1

            self._estateBoxes = estateBoxes

        estatePlots = GardenGlobals.estatePlots[houseIndex]
        treeIndex = 0
        flowerIndex = 0
        for estatePlot, (x, y, h, estatePlotType) in enumerate(estatePlots):
            if estatePlotType == GardenGlobals.GAG_TREE_TYPE and self.WANT_TREES:
                data = self.data['trees'][treeIndex]
                planted, waterLevel, lastCheck, growthLevel, lastHarvested = data
                if planted != -1:
                    obj = self.plantTree(treeIndex, planted, waterLevel=waterLevel, lastCheck=lastCheck,
                                         growthLevel=growthLevel, lastHarvested=lastHarvested, generate=False)
                    self.trees.add(obj)
                else:
                    obj = self.placePlot(treeIndex)

                obj.setPos(x, y, 0)
                obj.setH(h)
                obj.setPlot(estatePlot)
                obj.setOwnerIndex(houseIndex)
                obj.generateWithRequired(estate.zoneId)
                treeIndex += 1
            elif estatePlotType == GardenGlobals.FLOWER_TYPE and self.WANT_FLOWERS:
                data = self.data['flowers'][flowerIndex]
                planted, waterLevel, lastCheck, growthLevel, variety = data
                if planted != -1:
                    obj = self.plantFlower(flowerIndex, planted, variety, waterLevel=waterLevel, lastCheck=lastCheck,
                                           growthLevel=growthLevel, generate=False)
                    zOffset = 1.5
                else:
                    obj = self.placePlot(flowerIndex)
                    obj.setFlowerIndex(flowerIndex)
                    zOffset = 1.2

                obj.setPlot(estatePlot)
                obj.setOwnerIndex(houseIndex)

                # <hack>
                index = (0, 1, 2, 2, 2, 3, 3, 3, 4, 4)[flowerIndex]
                idx = (0, 0, 0, 1, 2, 0, 1, 2, 0, 1)[flowerIndex]
                gardenBox = self._estateBoxes[index]
                xOffset = FLOWER_X_OFFSETS[gardenBox.getTypeIndex()][idx]
                obj.setPos(gardenBox, 0, 0, 0)
                obj.setZ(gardenBox, zOffset)
                obj.setX(gardenBox, xOffset)
                obj.setH(gardenBox, 0)
                # </hack>

                obj.generateWithRequired(estate.zoneId)
                flowerIndex += 1
            elif estatePlotType == GardenGlobals.STATUARY_TYPE and self.WANT_STATUARY:
                data = self.data['statuary']
                if data == 0:
                    obj = self.placePlot(-1)
                else:
                    obj = self.placeStatuary(data, generate=False)

                obj.setPos(x, y, 0)
                obj.setH(h)
                obj.setPlot(estatePlot)
                obj.setOwnerIndex(houseIndex)
                obj.generateWithRequired(estate.zoneId)

        for tree in self.trees:
            tree.calcDependencies()

        self.reconsiderAvatarOrganicBonus()
        return True

    def placePlot(self, treeIndex):
        obj = DistributedGardenPlotAI(self)
        obj.setTreeIndex(treeIndex)
        self.objects.add(obj)
        return obj

    def getNullPlant(self):
        return NULL_PLANT

    def reconsiderAvatarOrganicBonus(self):
        av = self.air.doId2do.get(self.avId)
        if not av:
            return

        bonus = [-1] * 7
        for track in xrange(7):
            for level in xrange(8):
                if not self.hasTree(track, level):
                    break

                tree = self.getTree(track, level)
                if tree.getGrowthLevel() < tree.growthThresholds[1] or tree.getWilted():
                    break

            bonus[track] = level - 1

        av.b_setTrackBonusLevel(bonus)

    def hasTree(self, track, index):
        treeTypeIndex = GardenGlobals.getTreeTypeIndex(track, index)
        for tree in self.data['trees']:
            if tree[0] == treeTypeIndex:
                return True

        return False

    def getTree(self, track, index):
        for tree in self.trees:
            if tree.getTypeIndex() == GardenGlobals.getTreeTypeIndex(track, index):
                return tree

    def plantTree(self, treeIndex, value, plot=None, waterLevel=-1, lastCheck=0, growthLevel=0, lastHarvested=0,
                  ownerIndex=-1, plotId=-1, pos=None, generate=True):
        if not self.air:
            return

        if plot:
            if plot not in self.objects:
                return

            plot.requestDelete()
            self.objects.remove(plot)

        tree = DistributedGagTreeAI(self)
        tree.setTypeIndex(value)
        tree.setWaterLevel(waterLevel)
        tree.setGrowthLevel(growthLevel)
        if ownerIndex != -1:
            tree.setOwnerIndex(ownerIndex)

        if plotId != -1:
            tree.setPlot(plotId)

        if pos is not None:
            pos, h = pos
            tree.setPos(pos)
            tree.setH(h)

        tree.setTreeIndex(treeIndex)
        tree.calculate(lastHarvested, lastCheck)
        self.trees.add(tree)
        if generate:
            tree.generateWithRequired(self.estate.zoneId)

        return tree

    def placeStatuary(self, data, plot=None, plotId=-1, ownerIndex=-1, pos=None, generate=True):
        if not self.air:
            return

        if plot:
            if plot not in self.objects:
                return

            plot.requestDelete()
            self.objects.remove(plot)

        data, lastCheck, index, growthLevel = self.S_unpack(data)
        dclass = DistributedStatuaryAI
        if index in GardenGlobals.ToonStatuaryTypeIndices:
            dclass = DistributedToonStatuaryAI
        elif index in GardenGlobals.ChangingStatuaryTypeIndices:
            dclass = DistributedChangingStatuaryAI
        elif index in GardenGlobals.AnimatedStatuaryTypeIndices:
            dclass = DistributedAnimatedStatuaryAI

        obj = dclass(self)
        obj.setGrowthLevel(growthLevel)
        obj.setTypeIndex(index)
        obj.setOptional(data)
        if ownerIndex != -1:
            obj.setOwnerIndex(ownerIndex)

        if plotId != -1:
            obj.setPlot(plotId)

        if pos is not None:
            pos, h = pos
            obj.setPos(pos)
            obj.setH(h)

        obj.calculate(lastCheck)
        self.objects.add(obj)
        if generate:
            obj.announceGenerate()

        return obj

    def plantFlower(self, flowerIndex, species, variety, plot=None, waterLevel=-1, lastCheck=0, growthLevel=0,
                    ownerIndex=-1, plotId=-1, generate=True):
        if not self.air:
            return

        if plot:
            if plot not in self.objects:
                return

            plot.requestDelete()
            self.objects.remove(plot)

        flower = DistributedFlowerAI(self)
        flower.setTypeIndex(species)
        flower.setVariety(variety)
        flower.setWaterLevel(waterLevel)
        flower.setGrowthLevel(growthLevel)
        if ownerIndex != -1:
            flower.setOwnerIndex(ownerIndex)

        if plotId != -1:
            flower.setPlot(plotId)

        flower.setFlowerIndex(flowerIndex)
        flower.calculate(lastCheck)
        self.flowers.add(flower)
        if generate:
            flower.generateWithRequired(self.estate.zoneId)

        return flower

    # Data structure
    # VERY HIGH (vh) (64-bit)
    #    high high (H) = data (32-bit)
    #    high low (L) = lastCheck (32-bit)
    # VERY LOW (vl) (16-bit)
    #    low high (h) = index (8-bit)
    #    low low (l) = growthLevel (8-bit)

    @staticmethod
    def S_pack(data, lastCheck, index, growthLevel):
        vh = data << 32 | lastCheck
        vl = index << 8 | growthLevel
        return vh << 16 | vl

    @staticmethod
    def S_unpack(x):
        vh = x >> 16
        vl = x & 0xFFFF
        data = vh >> 32
        lastCheck = vh & 0xFFFFFFFF
        index = vl >> 8
        growthLevel = vl & 0xFF
        return data, lastCheck, index, growthLevel

    def update(self):
        if not os.path.exists(self.filePath):
            os.makedirs(self.filePath)

        with open(self.filePath + self.fileName, 'w+') as f:
            json.dump(self.data, f)


class GardenManagerAI:
    notify = DirectNotifyGlobal.directNotify.newCategory('GardenManagerAI')

    def __init__(self, air, estate):
        self.air = air
        self.estate = estate
        self.gardens = {}

    def loadGarden(self, avId):
        garden = GardenAI(self.air, self, avId)
        result = garden.load(self.estate)
        if result:
            self.gardens[avId] = garden

    def destroy(self):
        for garden in self.gardens.values():
            garden.destroy()

        del self.gardens
