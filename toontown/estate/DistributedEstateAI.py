import time

from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

from toontown.estate import CannonGlobals
from toontown.estate import GardenGlobals
from toontown.estate import HouseGlobals
from toontown.estate.DistributedCannonAI import DistributedCannonAI
from toontown.estate.DistributedTargetAI import DistributedTargetAI
from toontown.fishing.DistributedFishingPondAI import DistributedFishingPondAI
from toontown.safezone.DistributedFishingSpotAI import DistributedFishingSpotAI
from toontown.safezone.EFlyingTreasurePlannerAI import EFlyingTreasurePlannerAI
from toontown.safezone.ETreasurePlannerAI import ETreasurePlannerAI
from toontown.toonbase import ToontownGlobals


class DistributedEstateAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedEstateAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.houses = [None] * 6
        self.estateType = 0
        self.closestHouse = 0
        self.treasureIds = []
        self.dawnTime = 0
        self.decorData = []
        self.lastEpochTimeStamp = 0
        self.rentalType = 0
        self.clouds = 0
        self.cannons = []
        self.rentalTimeStamp = 0
        self.lawnItems = [[], [], [], [], [], []]
        self.activeToons = [0, 0, 0, 0, 0, 0]
        self.idList = []
        self.spotPosHpr = [(49.1029, -124.805, 0.344704, 90, 0, 0),
                           (46.5222, -134.739, 0.390713, 75, 0, 0),
                           (41.31, -144.559, 0.375978, 45, 0, 0),
                           (46.8254, -113.682, 0.46015, 135, 0, 0)]
        self.pond = None
        self.treasurePlanner = None
        self.flyingTreasurePlanner = None

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)

        # Spawn our treasures:
        self.treasurePlanner = ETreasurePlannerAI(self.zoneId)
        self.treasurePlanner.start()

        # Generate our fishing pond:
        self.pond = DistributedFishingPondAI(self.air)
        self.pond.setArea(ToontownGlobals.MyEstate)
        self.pond.generateWithRequired(self.zoneId)
        self.pond.generateTargets()

        # Generate our fishing spots:
        for i in xrange(len(self.spotPosHpr)):
            spot = DistributedFishingSpotAI(self.air)
            spot.setPondDoId(self.pond.doId)
            spot.setPosHpr(*self.spotPosHpr[i])
            if not isinstance(spot, DistributedFishingSpotAI):
                self.notify.warning('Failed to generate spot for pond %d!' % self.pond.doId)
                continue

            spot.generateWithRequired(self.zoneId)
            self.pond.addSpot(spot)

        # Start the collision loop:
        taskMgr.add(self.__collisionLoop, self.uniqueName('collisionLoop'), sort=30)

    def setEstateType(self, estateType):
        self.estateType = estateType

    def d_setEstateType(self, estateType):
        self.sendUpdate('setEstateType', [estateType])

    def b_setEstateType(self, estateType):
        self.setEstateType(estateType)
        self.d_setEstateType(estateType)

    def getEstateType(self):
        return self.estateType

    def setClosestHouse(self, closestHouse):
        self.closestHouse = closestHouse

    def setTreasureIds(self, treasureIds):
        self.treasureIds = treasureIds

    def d_setTreasureIds(self, treasureIds):
        self.sendUpdate('setTreasureIds', [treasureIds])

    def b_setTreasureIds(self, treasureIds):
        self.setTreasureIds(treasureIds)
        self.d_setTreasureIds(treasureIds)

    def getTreasureIds(self):
        return self.treasureIds

    def requestServerTime(self):
        avId = self.air.getAvatarIdFromSender()
        if not avId:
            return

        self.sendUpdateToAvatarId(avId, 'setServerTime', [time.time() % HouseGlobals.DAY_NIGHT_PERIOD])

    def setDawnTime(self, dawnTime):
        self.dawnTime = dawnTime

    def d_setDawnTime(self, dawnTime):
        self.sendUpdate('setDawnTime', [dawnTime])

    def b_setDawnTime(self, dawnTime):
        self.setDawnTime(dawnTime)
        self.d_setDawnTime(dawnTime)

    def getDawnTime(self):
        return self.dawnTime

    def placeOnGround(self, obj):
        pass  # TODO?

    def setDecorData(self, decorData):
        self.decorData = decorData

    def getDecorData(self):
        return self.decorData

    def setLastEpochTimeStamp(self, lastEpochTimeStamp):
        self.lastEpochTimeStamp = lastEpochTimeStamp

    def getLastEpochTimeStamp(self):
        return self.lastEpochTimeStamp

    def setRentalTimeStamp(self, rentalTimeStamp):
        self.rentalTimeStamp = rentalTimeStamp

    def d_setRentalTimeStamp(self, rentalTimeStamp):
        self.sendUpdate('setRentalTimeStamp', [rentalTimeStamp])

    def b_setRentalTimeStamp(self, rentalTimeStamp):
        self.setRentalTimeStamp(rentalTimeStamp)
        self.d_setRentalTimeStamp(rentalTimeStamp)

    def getRentalTimeStamp(self):
        return self.rentalTimeStamp

    def setRentalType(self, rentalType):
        self.rentalType = rentalType
        if rentalType:
            if time.time() >= self.rentalTimeStamp:
                self.b_setRentalType(0)
                self.b_setRentalTimeStamp(0)
                return

            if rentalType == ToontownGlobals.RentalCannon:
                target = DistributedTargetAI(self.air)
                target.generateWithRequired(self.zoneId)
                self.cannons.append(target)
                for posHpr in CannonGlobals.cannonDrops:
                    cannon = DistributedCannonAI(self.air, self.doId, target.doId, *posHpr)
                    cannon.generateWithRequired(self.zoneId)
                    self.cannons.append(cannon)

                self.b_setClouds(1)
                self.flyingTreasurePlanner = EFlyingTreasurePlannerAI(self.zoneId, callback=self.__treasureGrabbed)
                self.flyingTreasurePlanner.placeAllTreasures()
                self.b_setTreasureIds([treasure.doId for treasure in self.flyingTreasurePlanner.treasures])

            taskMgr.doMethodLater(self.rentalTimeStamp - time.time(), self.__rentalExpire,
                                  self.uniqueName('rentalExpire'))

    def b_setRentalType(self, rentalType):
        self.setRentalType(rentalType)
        self.d_setRentalType(rentalType)

    def d_setRentalType(self, rentalType):
        self.sendUpdate('setRentalType', [rentalType])

    def __treasureGrabbed(self, _):
        self.b_setTreasureIds([treasure.doId for treasure in self.flyingTreasurePlanner.treasures if treasure])

    def __rentalExpire(self, task):
        if self.getRentalType() == ToontownGlobals.RentalCannon:
            for cannon in self.cannons[:]:
                cannon.requestDelete()
                self.cannons.remove(cannon)

            self.b_setClouds(0)
            self.b_setRentalTimeStamp(0)
            self.b_setRentalType(0)
            self.b_setTreasureIds([])
            self.flyingTreasurePlanner.deleteAllTreasuresNow()
            self.flyingTreasurePlanner = None

        return task.done

    def getRentalType(self):
        return self.rentalType

    def setSlot0ToonId(self, avId):
        self.activeToons[0] = avId

    def getSlot0ToonId(self):
        return self.activeToons[0]

    def setSlot0Items(self, item):
        self.lawnItems[0] = item

    def getSlot0Items(self):
        return self.lawnItems[0]

    def setSlot1ToonId(self, avId):
        self.activeToons[1] = avId

    def getSlot1ToonId(self):
        return self.activeToons[1]

    def setSlot1Items(self, item):
        self.lawnItems[1] = item

    def getSlot1Items(self):
        return self.lawnItems[1]

    def setSlot2ToonId(self, avId):
        self.activeToons[2] = avId

    def getSlot2ToonId(self):
        return self.activeToons[2]

    def setSlot2Items(self, item):
        self.lawnItems[2] = item

    def getSlot2Items(self):
        return self.lawnItems[2]

    def setSlot3ToonId(self, avId):
        self.activeToons[3] = avId

    def getSlot3ToonId(self):
        return self.activeToons[3]

    def setSlot3Items(self, item):
        self.lawnItems[3] = item

    def getSlot3Items(self):
        return self.lawnItems[3]

    def setSlot4ToonId(self, avId):
        self.activeToons[4] = avId

    def getSlot4ToonId(self):
        return self.activeToons[4]

    def setSlot4Items(self, item):
        self.lawnItems[4] = item

    def getSlot4Items(self):
        return self.lawnItems[4]

    def setSlot5ToonId(self, avId):
        self.activeToons[5] = avId

    def getSlot5ToonId(self):
        return self.activeToons[5]

    def setSlot5Items(self, item):
        self.lawnItems[5] = item

    def getSlot5Items(self):
        return self.lawnItems[5]

    def setIdList(self, idList):
        self.idList = idList

    def d_setIdList(self, idList):
        self.sendUpdate('setIdList', [idList])

    def b_setIdList(self, idList):
        self.setIdList(idList)
        self.d_setIdList(idList)

    def getIdList(self):
        return self.idList

    def completeFlowerSale(self, flag):
        if not flag:
            return

        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)
        if not av:
            return

        collection = av.flowerCollection
        earning = 0
        newSpecies = 0
        for flower in av.flowerBasket.getFlower():
            if collection.collectFlower(flower) == GardenGlobals.COLLECT_NEW_ENTRY:
                newSpecies += 1

            earning += flower.getValue()

        av.b_setFlowerBasket([], [])
        av.d_setFlowerCollection(*av.flowerCollection.getNetLists())
        av.addMoney(earning)
        oldSpecies = len(collection) - newSpecies
        dt = abs(len(collection) // 10 - oldSpecies // 10)
        if dt:
            self.notify.info('%d is getting a gardening trophy!' % avId)
            maxHp = av.getMaxHp()
            maxHp = min(ToontownGlobals.MaxHpLimit, maxHp + dt)
            av.b_setMaxHp(maxHp)
            av.toonUp(maxHp)
            self.sendUpdate('awardedTrophy', [avId])

        av.b_setGardenTrophies(range(len(collection) // 10))

    def setClouds(self, clouds):
        self.clouds = clouds

    def d_setClouds(self, clouds):
        self.sendUpdate('setClouds', [clouds])

    def b_setClouds(self, clouds):
        self.setClouds(clouds)
        self.d_setClouds(clouds)

    def getClouds(self):
        return self.clouds

    def rentItem(self, typeIndex, duration):
        self.b_setRentalTimeStamp(time.time() + duration * 60)
        self.b_setRentalType(typeIndex)

    def cannonsOver(self):
        pass  # TODO

    def gameTableOver(self):
        pass  # TODO

    def placeStarterGarden(self, avId):
        if not avId:
            return

        for house in self.houses:
            if house is not None:
                if house.getAvatarId() == avId:
                    house.placeStarterGarden()
                    return

        self.notify.warning('Avatar %s tried to place a starter garden when they didn\'t own a house!' % avId)

    def delete(self):
        if self.treasurePlanner:
            self.treasurePlanner.stop()
            self.treasurePlanner.deleteAllTreasuresNow()
            self.treasurePlanner = None

        if self.flyingTreasurePlanner:
            self.flyingTreasurePlanner.deleteAllTreasuresNow()
            self.flyingTreasurePlanner = None

        if self.pond is not None:
            self.pond.requestDelete()
            self.pond = None

        for cannon in self.cannons[:]:
            cannon.requestDelete()
            self.cannons.remove(cannon)

        taskMgr.remove(self.uniqueName('rentalExpire'))
        taskMgr.remove(self.uniqueName('collisionLoop'))
        DistributedObjectAI.delete(self)

    def destroy(self):
        for house in self.houses:
            if house is not None:
                house.requestDelete()

        del self.houses[:]
        self.requestDelete()

    def __collisionLoop(self, task):
        if hasattr(self, 'pets'):
            for pet in self.pets:
                if not pet:
                    continue

                collTrav = pet.getCollTrav()
                if collTrav:
                    collTrav.traverse(self.getRender())

        return task.cont
