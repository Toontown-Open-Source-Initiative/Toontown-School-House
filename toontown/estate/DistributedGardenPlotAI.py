from direct.directnotify import DirectNotifyGlobal

from toontown.estate import GardenGlobals
from toontown.estate.DistributedLawnDecorAI import DistributedLawnDecorAI

# X position offsets for flowers & flower plots:
FLOWER_X_OFFSETS = (None, (0,), (-1.5, 1.5), (-3.4, 0, 3.5))


class DistributedGardenPlotAI(DistributedLawnDecorAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedGardenPlotAI')

    def __init__(self, mgr):
        DistributedLawnDecorAI.__init__(self, mgr)
        self.plotType = 0
        self.__plantingAvId = 0
        self.treeIndex = 0
        self.flowerIndex = 0

    def announceGenerate(self):
        DistributedLawnDecorAI.announceGenerate(self)
        self.plotType = GardenGlobals.whatCanBePlanted(self.ownerIndex, self.plot)
        self.__plantingAvId = 0

    def setTreeIndex(self, treeIndex):
        self.treeIndex = treeIndex

    def getTreeIndex(self):
        return self.treeIndex

    def setFlowerIndex(self, flowerIndex):
        self.flowerIndex = flowerIndex

    def getFlowerIndex(self):
        return self.flowerIndex

    def __initialSanityCheck(self, wantedType=None, forceOwner=False):
        if self.__plantingAvId:
            # Busy, silently ignore:
            return

        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)
        if not av:
            self.air.writeServerEvent('suspicious', avId, 'called DistributedGardenPlotAI method outside shard!')
            return

        if wantedType is not None and self.plotType != wantedType:
            self.air.writeServerEvent('suspicious', avId, 'called incorrect DistributedGardenPlotAI method!',
                                      plotType=self.plotType,
                                      wantedType=wantedType)
            return self.d_interactionDenied()

        if avId != self.ownerDoId and not forceOwner:
            self.air.writeServerEvent('suspicious', avId,
                                      'called someone else\'s DistributedGardenPlotAI plant method!',
                                      ownerDoId=self.ownerDoId)
            return self.d_interactionDenied()

        return av

    def plantFlower(self, species, variety, usingFlowerAll=False):
        av = self.__initialSanityCheck(GardenGlobals.FLOWER_TYPE if not usingFlowerAll else None, usingFlowerAll)
        if not av:
            return

        def invalid(problem):
            msg = 'tried to plant flower but something went wrong: %s' % problem
            self.notify.warning('%d %s' % (av.doId, msg))
            self.air.writeServerEvent('suspicious', av.doId, msg)
            if not usingFlowerAll:
                return self.d_setMovie(GardenGlobals.MOVIE_PLANT_REJECTED)

        plantAttributes = GardenGlobals.PlantAttributes.get(species, {})
        if plantAttributes.get('plantType') != GardenGlobals.FLOWER_TYPE:
            return invalid('invalid species: %d' % species)

        if variety >= len(plantAttributes['varieties']):
            return invalid('invalid variety: %d' % variety)

        if not usingFlowerAll:
            cost = len(GardenGlobals.Recipes[plantAttributes['varieties'][variety][0]]['beans'])
            av.takeMoney(cost)
            self.d_setMovie(GardenGlobals.MOVIE_PLANT)

        def handlePlantFlower(task):
            flower = self.mgr.plantFlower(self.getFlowerIndex(), species, variety, plot=self,
                                          ownerIndex=self.ownerIndex, plotId=self.plot,
                                          waterLevel=0, generate=False)

            # <hack>
            index = (0, 1, 2, 2, 2, 3, 3, 3, 4, 4)[self.getFlowerIndex()]
            idx = (0, 0, 0, 1, 2, 0, 1, 2, 0, 1)[self.getFlowerIndex()]
            zOffset = 1.5
            gardenBox = self.mgr._estateBoxes[index]
            xOffset = FLOWER_X_OFFSETS[gardenBox.getTypeIndex()][idx]
            flower.setPos(gardenBox, 0, 0, 0)
            flower.setZ(gardenBox, zOffset)
            flower.setX(gardenBox, xOffset)
            flower.setH(gardenBox, 0)
            # </hack>

            flower.generateWithRequired(self.mgr.estate.zoneId)
            if not usingFlowerAll:
                flower.d_setMovie(GardenGlobals.MOVIE_FINISHPLANTING, self.__plantingAvId)
                flower.d_setMovie(GardenGlobals.MOVIE_CLEAR, self.__plantingAvId)

            self.air.writeServerEvent('plant-flower', self.__plantingAvId, species=species, variety=variety,
                                      plot=self.plot, name=plantAttributes.get('name', 'unknown flower'))
            if task:
                return task.done

        if usingFlowerAll:
            handlePlantFlower(None)
        else:
            taskMgr.doMethodLater(7, handlePlantFlower, self.uniqueName('handle-plant-flower'))

        self.__plantingAvId = av.doId
        return 1

    def plantGagTree(self, track, index):
        av = self.__initialSanityCheck(GardenGlobals.GAG_TREE_TYPE)
        if not av:
            return

        for i in xrange(index):
            if not self.mgr.hasTree(track, i):
                msg = 'tried to plant tree but an index is missing: %d' % index
                self.notify.warning('%d %s' % (av.doId, msg))
                self.air.writeServerEvent('suspicious', av.doId, msg)
                return self.d_setMovie(GardenGlobals.MOVIE_PLANT_REJECTED)

        if self.mgr.hasTree(track, index):
            msg = 'tried to plant tree but gag already planted'
            self.notify.warning('%d %s' % (av.doId, msg))
            self.air.writeServerEvent('suspicious', av.doId, msg)
            return self.d_setMovie(GardenGlobals.MOVIE_PLANT_REJECTED)

        if av.inventory.useItem(track, index) == -1:
            msg = 'tried to plant tree but not carrying selected gag'
            self.notify.warning('%d %s' % (av.doId, msg))
            self.air.writeServerEvent('suspicious', av.doId, msg)
            return self.d_setMovie(GardenGlobals.MOVIE_PLANT_REJECTED)

        av.d_setInventory(av.getInventory())
        self.d_setMovie(GardenGlobals.MOVIE_PLANT)

        def handlePlantTree(task):
            if not self.air:
                return

            tree = self.mgr.plantTree(self.getTreeIndex(), GardenGlobals.getTreeTypeIndex(track, index), plot=self,
                                      ownerIndex=self.ownerIndex, plotId=self.plot, pos=(self.getPos(), self.getH()))
            tree.d_setMovie(GardenGlobals.MOVIE_FINISHPLANTING, self.__plantingAvId)
            tree.d_setMovie(GardenGlobals.MOVIE_CLEAR, self.__plantingAvId)
            self.air.writeServerEvent('plant-tree', self.__plantingAvId, track=track, index=index, plot=self.plot)
            return task.done

        taskMgr.doMethodLater(7, handlePlantTree, self.uniqueName('handle-plant-tree'))
        self.__plantingAvId = av.doId

    def plantStatuary(self, species):
        av = self.__initialSanityCheck(GardenGlobals.STATUARY_TYPE)
        if not av:
            return

        def invalid(problem):
            msg = 'tried to plant statuary but something went wrong: %s' % problem
            self.notify.warning('%d %s' % (av.doId, msg))
            self.air.writeServerEvent('suspicious', av.doId, msg)
            return self.d_setMovie(GardenGlobals.MOVIE_PLANT_REJECTED)

        plantAttributes = GardenGlobals.PlantAttributes.get(species, {})
        if plantAttributes.get('plantType') != GardenGlobals.STATUARY_TYPE:
            return invalid('invalid species: %d' % species)

        gardenItem = species - 100
        if gardenItem == 134:
            gardenItem = 135

        if not av.removeGardenItem(gardenItem, 1):
            return invalid('av doesn\'t own item: %d' % species)

        self.d_setMovie(GardenGlobals.MOVIE_PLANT)

        def handlePlaceStatuary(task):
            if not self.air:
                return

            statuary = self.mgr.placeStatuary(self.mgr.S_pack(0, 0, species, 0), plot=self,
                                              ownerIndex=self.ownerIndex, plotId=self.plot,
                                              pos=(self.getPos(), self.getH()), generate=False)
            statuary.generateWithRequired(self.zoneId)
            statuary.d_setMovie(GardenGlobals.MOVIE_FINISHPLANTING, self.__plantingAvId)
            statuary.d_setMovie(GardenGlobals.MOVIE_CLEAR, self.__plantingAvId)
            self.air.writeServerEvent('plant-statuary', self.__plantingAvId, species=species, plot=self.plot)
            return task.done

        taskMgr.doMethodLater(7, handlePlaceStatuary, self.uniqueName('handle-place-statuary'))
        self.__plantingAvId = av.doId

    def plantToonStatuary(self, species, dnaCode):
        av = self.__initialSanityCheck(GardenGlobals.STATUARY_TYPE)
        if not av:
            return

        def invalid(problem):
            msg = 'tried to plant statuary but something went wrong: %s' % problem
            self.notify.warning('%d %s' % (av.doId, msg))
            self.air.writeServerEvent('suspicious', av.doId, msg)
            return self.d_setMovie(GardenGlobals.MOVIE_PLANT_REJECTED)

        plantAttributes = GardenGlobals.PlantAttributes.get(species, {})
        if plantAttributes.get('plantType') != GardenGlobals.STATUARY_TYPE:
            return invalid('invalid species: %d' % species)

        if not av.removeGardenItem(species - 100, 1):
            return invalid('av doesn\'t own item: %d' % species)

        self.d_setMovie(GardenGlobals.MOVIE_PLANT)

        def handlePlaceStatuary(task):
            if not self.air:
                return

            statuary = self.mgr.placeStatuary(self.mgr.S_pack(dnaCode, 0, species, 0), plot=self,
                                              ownerIndex=self.ownerIndex, plotId=self.plot,
                                              pos=(self.getPos(), self.getH()), generate=False)
            statuary.generateWithRequired(self.zoneId)
            statuary.d_setMovie(GardenGlobals.MOVIE_FINISHPLANTING, self.__plantingAvId)
            self.air.writeServerEvent('plant-statuary', self.__plantingAvId, species=species, plot=self.plot)
            return task.done

        taskMgr.doMethodLater(7, handlePlaceStatuary, self.uniqueName('handle-place-statuary'))
        self.__plantingAvId = av.doId

    def plantNothing(self, burntBeans):
        av = self.__initialSanityCheck()
        if av:
            av.takeMoney(burntBeans)
