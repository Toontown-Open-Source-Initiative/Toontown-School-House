from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

from toontown.building import DoorTypes
from toontown.catalog.CatalogFurnitureItem import *
from toontown.catalog.CatalogItemList import CatalogItemList
from toontown.estate.DistributedHouseDoorAI import DistributedHouseDoorAI
from toontown.estate.DistributedHouseInteriorAI import DistributedHouseInteriorAI
from toontown.estate.DistributedMailboxAI import DistributedMailboxAI
from toontown.estate.GardenManagerAI import GardenManagerAI


class DistributedHouseAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedHouseAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.estate = None
        self.housePos = 0
        self.houseType = 0
        self.gardenPos = 0
        self.avatarId = 0
        self.name = ''
        self.color = 0
        self.atticItems = CatalogItemList(store=CatalogItem.Customization)
        self.interiorItems = CatalogItemList(store=CatalogItem.Customization)
        self.atticWallpaper = CatalogItemList(store=CatalogItem.Customization)
        self.interiorWallpaper = CatalogItemList(store=CatalogItem.Customization)
        self.atticWindows = CatalogItemList(store=CatalogItem.Customization)
        self.interiorWindows = CatalogItemList(store=CatalogItem.Customization)
        self.deletedItems = CatalogItemList(store=CatalogItem.Customization)
        self.cannonEnabled = 0
        self.interiorZone = None
        self.exteriorDoor = None
        self.interiorDoor = None
        self.interior = None
        self.mailbox = None
        self.gardenManager = None

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)

        # Allocate a zone for this house's interior:
        self.interiorZone = self.air.allocateZone()

        # Setup interior & exterior doors:
        self.exteriorDoor = DistributedHouseDoorAI(self.air, self.getDoId(), DoorTypes.EXT_STANDARD)
        self.exteriorDoor.setSwing(3)
        self.exteriorDoor.generateWithRequired(self.zoneId)
        self.interiorDoor = DistributedHouseDoorAI(self.air, self.getDoId(), DoorTypes.INT_STANDARD)
        self.interiorDoor.setSwing(3)
        self.interiorDoor.setOtherDoor(self.exteriorDoor)
        self.interiorDoor.generateWithRequired(self.interiorZone)
        self.exteriorDoor.setOtherDoor(self.interiorDoor)

        # Setup interior:
        self.interior = DistributedHouseInteriorAI(self.air, self)
        self.interior.setHouseIndex(self.housePos)
        self.interior.setHouseId(self.getDoId())
        self.interior.generateWithRequired(self.interiorZone)

        # Generate our mailbox:
        if self.avatarId:
            self.mailbox = DistributedMailboxAI(self.air, self)
            self.mailbox.generateWithRequired(self.zoneId)

        # Send the house ready update:
        self.d_setHouseReady()

    def delete(self):
        self.exteriorDoor.requestDelete()
        self.interiorDoor.requestDelete()
        if self.interior.furnitureManager:
            self.interior.furnitureManager.requestDelete()

        self.interior.requestDelete()
        if self.avatarId:
            self.mailbox.requestDelete()

        if self.gardenManager:
            self.gardenManager.destroy()

        self.air.deallocateZone(self.interiorZone)
        self.estate = None
        DistributedObjectAI.delete(self)

    def setHousePos(self, housePos):
        self.housePos = housePos

    def d_setHousePos(self, housePos):
        self.sendUpdate('setHousePos', [housePos])

    def b_setHousePos(self, housePos):
        self.setHousePos(housePos)
        self.d_setHousePos(housePos)

    def getHousePos(self):
        return self.housePos

    def setHouseType(self, houseType):
        self.houseType = houseType

    def d_setHouseType(self, houseType):
        self.sendUpdate('setHouseType', [houseType])

    def b_setHouseType(self, houseType):
        self.setHouseType(houseType)
        self.d_setHouseType(houseType)

    def getHouseType(self):
        return self.houseType

    def setGardenPos(self, gardenPos):
        self.gardenPos = gardenPos

    def d_setGardenPos(self, gardenPos):
        self.sendUpdate('setGardenPos', [gardenPos])

    def b_setGardenPos(self, gardenPos):
        self.setGardenPos(gardenPos)
        self.d_setGardenPos(gardenPos)

    def getGardenPos(self):
        return self.gardenPos

    def setAvatarId(self, avatarId):
        self.avatarId = avatarId

    def d_setAvatarId(self, avatarId):
        self.sendUpdate('setAvatarId', [avatarId])

    def b_setAvatarId(self, avatarId):
        self.setAvatarId(avatarId)
        self.d_setAvatarId(avatarId)

    def getAvatarId(self):
        return self.avatarId

    def setName(self, name):
        self.name = name

    def d_setName(self, name):
        self.sendUpdate('setName', [name])

    def b_setName(self, name):
        self.setName(name)
        self.d_setName(name)

    def getName(self):
        return self.name

    def setColor(self, color):
        self.color = color

    def d_setColor(self, color):
        self.sendUpdate('setColor', [color])

    def b_setColor(self, color):
        self.setColor(color)
        self.d_setColor(color)

    def getColor(self):
        return self.color

    def setAtticItems(self, atticItems):
        self.atticItems = CatalogItemList(atticItems, store=CatalogItem.Customization)

    def d_setAtticItems(self, atticItems):
        self.sendUpdate('setAtticItems', [atticItems])

    def b_setAtticItems(self, atticItems):
        self.setAtticItems(atticItems)
        self.d_setAtticItems(atticItems)

    def getAtticItems(self):
        return self.atticItems.getBlob()

    def setInteriorItems(self, interiorItems):
        self.interiorItems = CatalogItemList(interiorItems, store=CatalogItem.Customization | CatalogItem.Location)

    def d_setInteriorItems(self, interiorItems):
        self.sendUpdate('setInteriorItems', [interiorItems])

    def b_setInteriorItems(self, interiorItems):
        self.setInteriorItems(interiorItems)
        self.d_setInteriorItems(interiorItems)

    def getInteriorItems(self):
        return self.interiorItems.getBlob()

    def setAtticWallpaper(self, atticWallpaper):
        self.atticWallpaper = CatalogItemList(atticWallpaper, store=CatalogItem.Customization)

    def d_setAtticWallpaper(self, atticWallpaper):
        self.sendUpdate('setAtticWallpaper', [atticWallpaper])

    def b_setAtticWallpaper(self, atticWallpaper):
        self.setAtticWallpaper(atticWallpaper)
        self.d_setAtticWallpaper(atticWallpaper)

    def getAtticWallpaper(self):
        return self.atticWallpaper.getBlob()

    def setInteriorWallpaper(self, interiorWallpaper):
        self.interiorWallpaper = CatalogItemList(interiorWallpaper, store=CatalogItem.Customization)

    def d_setInteriorWallpaper(self, interiorWallpaper):
        self.sendUpdate('setInteriorWallpaper', [interiorWallpaper])

    def b_setInteriorWallpaper(self, interiorWallpaper):
        self.setInteriorWallpaper(interiorWallpaper)
        self.d_setInteriorWallpaper(interiorWallpaper)

    def getInteriorWallpaper(self):
        return self.interiorWallpaper.getBlob()

    def setAtticWindows(self, atticWindows):
        self.atticWindows = CatalogItemList(atticWindows, store=CatalogItem.Customization)

    def d_setAtticWindows(self, atticWindows):
        self.sendUpdate('setAtticWindows', [atticWindows])

    def b_setAtticWindows(self, atticWindows):
        self.setAtticWindows(atticWindows)
        self.d_setAtticWindows(atticWindows)

    def getAtticWindows(self):
        return self.atticWindows.getBlob()

    def setInteriorWindows(self, interiorWindows):
        self.interiorWindows = CatalogItemList(interiorWindows,
                                               store=CatalogItem.Customization | CatalogItem.WindowPlacement)

    def d_setInteriorWindows(self, interiorWindows):
        self.sendUpdate('setInteriorWindows', [interiorWindows])

    def b_setInteriorWindows(self, interiorWindows):
        self.setInteriorWindows(interiorWindows)
        self.d_setInteriorWindows(interiorWindows)

    def getInteriorWindows(self):
        return self.interiorWindows.getBlob()

    def setDeletedItems(self, deletedItems):
        self.deletedItems = CatalogItemList(deletedItems, store=CatalogItem.Customization)

    def d_setDeletedItems(self, deletedItems):
        self.sendUpdate('setDeletedItems', [deletedItems])

    def b_setDeletedItems(self, deletedItems):
        self.setDeletedItems(deletedItems)
        self.d_setDeletedItems(deletedItems)

    def getDeletedItems(self):
        return self.deletedItems.getBlob()

    def setCannonEnabled(self, cannonEnabled):
        self.cannonEnabled = cannonEnabled

    def d_setCannonEnabled(self, cannonEnabled):
        self.sendUpdate('setCannonEnabled', [cannonEnabled])

    def b_setCannonEnabled(self, cannonEnabled):
        self.setCannonEnabled(cannonEnabled)
        self.d_setCannonEnabled(cannonEnabled)

    def getCannonEnabled(self):
        return self.cannonEnabled

    def d_setHouseReady(self):
        self.sendUpdate('setHouseReady')

    def addAtticItem(self, item):
        if item.replacesExisting and item.hasExisting():
            if item.getFlags() & FLCloset:
                closet = ClosetToClothes.keys()
                for atticItem in self.atticItems:
                    if atticItem.furnitureType in closet:
                        self.interior.furnitureManager.atticItems.remove(atticItem)
                        break

                for interiorItem in self.interior.furnitureManager.items[:]:
                    if interiorItem.catalogItem.furnitureType in closet:
                        interiorItem.requestDelete()
                        self.interior.furnitureManager.items.remove(interiorItem)
                        item.posHpr = interiorItem.catalogItem.posHpr
                        self.interior.furnitureManager.generateItem(item)
                        self.interior.furnitureManager.saveFurniture()
                        return

        self.interior.furnitureManager.atticItems.append(item)
        self.interior.furnitureManager.saveFurniture()

    def addWallpaper(self, item):
        self.interior.furnitureManager.atticWallpaper.append(item)
        self.interior.furnitureManager.saveFurniture()

    def addWindow(self, item):
        self.interior.furnitureManager.atticWindows.append(item)
        self.interior.furnitureManager.saveFurniture()

    def placeStarterGarden(self):
        if not config.GetBool('want-gardening', False):
            return

        if not self.estate:
            return

        av = self.air.doId2do.get(self.getAvatarId())
        if av is None:
            return

        if av.getGardenStarted():
            self.notify.warning('Avatar %s tried to start their garden twice!' % self.getAvatarId())
            return

        # Set the avatar's garden to started:
        av.b_setGardenStarted(1)

        # Create the GardenManagerAI:
        self.gardenManager = GardenManagerAI(self.air, self.estate)
        self.gardenManager.loadGarden(av.doId)

    def createGardenManager(self):
        if not config.GetBool('want-gardening', False):
            return

        if not self.estate:
            return

        if not self.getAvatarId():
            return

        av = self.air.doId2do.get(self.getAvatarId())
        if av is not None:
            if av.getGardenStarted():
                self.gardenManager = GardenManagerAI(self.air, self.estate)
                self.gardenManager.loadGarden(av.doId)

            return

        def __gotOwner(dclass, fields, self=self):
            if dclass != self.air.dclassesByName['DistributedToonAI']:
                return

            gardenStarted = fields['setGardenStarted'][0]
            if gardenStarted:
                self.gardenManager = GardenManagerAI(self.air, self.estate)
                self.gardenManager.loadGarden(self.getAvatarId())

        self.air.dbInterface.queryObject(self.air.dbId, self.getAvatarId(), __gotOwner)
