import random

from direct.directnotify import DirectNotifyGlobal

from toontown.fishing import FishGlobals
from toontown.fishing.DistributedFishingPondAI import DistributedFishingPondAI
from toontown.fishing.FishBase import FishBase
from toontown.safezone.DistributedFishingSpotAI import DistributedFishingSpotAI


class FishManagerAI:
    notify = DirectNotifyGlobal.directNotify.newCategory('FishManagerAI')

    def __init__(self, air):
        self.air = air
        self.requestedFish = {}

    def generatePond(self, area, zoneId):
        # Generate our fishing pond.
        fishingPond = DistributedFishingPondAI(self.air)
        fishingPond.setArea(area)
        fishingPond.generateWithRequired(zoneId)
        fishingPond.generateTargets()
        return fishingPond

    def generateSpots(self, dnaData, fishingPond):
        # Generate our fishing spots.
        zoneId = fishingPond.zoneId
        doId = fishingPond.doId
        fishingSpot = DistributedFishingSpotAI(self.air)
        fishingSpot.setPondDoId(doId)
        x, y, z = dnaData.getPos()
        h, p, r = dnaData.getHpr()
        fishingSpot.setPosHpr(x, y, z, h, p, r)
        fishingSpot.generateWithRequired(zoneId)
        return fishingSpot

    def generateCatch(self, av, zoneId):
        # Generate our catch.
        if len(av.fishTank) >= av.getMaxFishTank():
            return [FishGlobals.OverTankLimit, 0, 0, 0]

        caughtItem = self.air.questManager.toonFished(av, zoneId)
        if caughtItem:
            return [FishGlobals.QuestItem, caughtItem, 0, 0]

        rand = random.random() * 100.0
        for cutoff in FishGlobals.SortedProbabilityCutoffs:
            if rand <= cutoff:
                itemType = FishGlobals.ProbabilityDict[cutoff]
                break

        if av.doId in self.requestedFish:
            genus, species = self.requestedFish[av.doId]
            weight = FishGlobals.getRandomWeight(genus, species)
            fish = FishBase(genus, species, weight)
            fishType = av.fishCollection.collectFish(fish)
            if fishType == FishGlobals.COLLECT_NEW_ENTRY:
                itemType = FishGlobals.FishItemNewEntry
            elif fishType == FishGlobals.COLLECT_NEW_RECORD:
                itemType = FishGlobals.FishItemNewRecord
            else:
                itemType = FishGlobals.FishItem

            collectionNetList = av.fishCollection.getNetLists()
            av.d_setFishCollection(collectionNetList[0], collectionNetList[1], collectionNetList[2])
            av.fishTank.addFish(fish)
            tankNetList = av.fishTank.getNetLists()
            av.d_setFishTank(tankNetList[0], tankNetList[1], tankNetList[2])
            del self.requestedFish[av.doId]
            return [itemType, genus, species, weight]

        if itemType == FishGlobals.FishItem:
            success, genus, species, weight = FishGlobals.getRandomFishVitals(zoneId, av.getFishingRod())
            fish = FishBase(genus, species, weight)
            fishType = av.fishCollection.collectFish(fish)
            if fishType == FishGlobals.COLLECT_NEW_ENTRY:
                itemType = FishGlobals.FishItemNewEntry
            elif fishType == FishGlobals.COLLECT_NEW_RECORD:
                itemType = FishGlobals.FishItemNewRecord
            else:
                itemType = FishGlobals.FishItem

            collectionNetList = av.fishCollection.getNetLists()
            av.d_setFishCollection(collectionNetList[0], collectionNetList[1], collectionNetList[2])
            av.fishTank.addFish(fish)
            tankNetList = av.fishTank.getNetLists()
            av.d_setFishTank(tankNetList[0], tankNetList[1], tankNetList[2])
            return [itemType, genus, species, weight]
        elif itemType == FishGlobals.BootItem:
            return [itemType, 0, 0, 0]
        else:
            money = FishGlobals.Rod2JellybeanDict[av.getFishingRod()]
            av.addMoney(money)
            return [itemType, money, 0, 0]

    def creditFishTank(self, av):
        totalFish = len(av.fishCollection)
        trophies = int(totalFish / 10)
        curTrophies = len(av.fishingTrophies)
        av.addMoney(av.fishTank.getTotalValue())
        av.b_setFishTank([], [], [])
        if trophies > curTrophies:
            av.b_setMaxHp(av.getMaxHp() + trophies - curTrophies)
            av.toonUp(av.getMaxHp())
            av.b_setFishingTrophies(range(trophies))
            return True

        return False
