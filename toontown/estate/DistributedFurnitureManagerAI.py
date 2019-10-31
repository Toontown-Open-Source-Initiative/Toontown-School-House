import datetime
import json
import os
import time

from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

from toontown.catalog import CatalogFurnitureItem
from toontown.catalog import CatalogInvalidItem
from toontown.catalog import CatalogItem
from toontown.catalog import CatalogSurfaceItem
from toontown.catalog import CatalogWindowItem
from toontown.catalog.CatalogItemList import CatalogItemList
from toontown.estate.DistributedBankAI import DistributedBankAI
from toontown.estate.DistributedClosetAI import DistributedClosetAI
from toontown.estate.DistributedFurnitureItemAI import DistributedFurnitureItemAI
from toontown.estate.DistributedPhoneAI import DistributedPhoneAI
from toontown.estate.DistributedTrunkAI import DistributedTrunkAI
from toontown.toonbase import ToontownGlobals

MINUTE = 60
HOUR = 60 * MINUTE
DAY = 24 * HOUR


def getDayId():
    return int(time.time() // DAY)


class DistributedFurnitureManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedFurnitureManagerAI')
    serverDataFolder = simbase.config.GetString('server-data-folder', '')

    def __init__(self, air, house, interior):
        DistributedObjectAI.__init__(self, air)
        self.house = house
        self.interior = interior
        self.ownerId = 0
        self.ownerName = ''
        self.interiorId = 0
        self.atticItems = CatalogItemList(store=CatalogItem.Customization)
        self.atticWallpaper = CatalogItemList(store=CatalogItem.Customization)
        self.atticWindows = CatalogItemList(store=CatalogItem.Customization)
        self.deletedItems = CatalogItemList(store=CatalogItem.Customization)
        self.wallpaper = CatalogItemList(store=CatalogItem.Customization)
        self.windows = CatalogItemList(store=CatalogItem.Customization | CatalogItem.WindowPlacement)
        self.items = []
        self.director = 0
        self.deletedItemsFilename = ''
        self.day2deletedItems = {}

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)
        self.deletedItemsFilename = self.getDeletedItemsFilename()
        self.day2deletedItems = self.loadDeletedItems()
        taskMgr.add(self.__deletedItemsTask, self.uniqueName('deleted-items-task'))

    def delete(self):
        for item in self.items[:]:
            item.requestDelete()
            self.items.remove(item)

        taskMgr.remove(self.uniqueName('deleted-items-task'))
        DistributedObjectAI.delete(self)

    def setOwnerId(self, ownerId):
        self.ownerId = ownerId

    def d_setOwnerId(self, ownerId):
        self.sendUpdate('setOwnerId', [ownerId])

    def b_setOwnerId(self, ownerId):
        self.setOwnerId(ownerId)
        self.d_setOwnerId(ownerId)

    def getOwnerId(self):
        return self.ownerId

    def setOwnerName(self, ownerName):
        self.ownerName = ownerName

    def d_setOwnerName(self, ownerName):
        self.sendUpdate('setOwnerName', [ownerName])

    def b_setOwnerName(self, ownerName):
        self.setOwnerName(ownerName)
        self.d_setOwnerName(ownerName)

    def getOwnerName(self):
        return self.ownerName

    def setInteriorId(self, interiorId):
        self.interiorId = interiorId

    def d_setInteriorId(self, interiorId):
        self.sendUpdate('setInteriorId', [interiorId])

    def b_setInteriorId(self, interiorId):
        self.setInteriorId(interiorId)
        self.d_setInteriorId(interiorId)

    def getInteriorId(self):
        return self.interiorId

    def setAtticItems(self, atticItems):
        self.atticItems = CatalogItemList(atticItems, store=CatalogItem.Customization)

    def d_setAtticItems(self, atticItems):
        self.sendUpdate('setAtticItems', [atticItems])

    def b_setAtticItems(self, atticItems):
        self.setAtticItems(atticItems)
        self.d_setAtticItems(atticItems)

    def getAtticItems(self):
        return self.atticItems.getBlob()

    def setAtticWallpaper(self, atticWallpaper):
        self.atticWallpaper = CatalogItemList(atticWallpaper, store=CatalogItem.Customization)

    def d_setAtticWallpaper(self, atticWallpaper):
        self.sendUpdate('setAtticWallpaper', [atticWallpaper])

    def b_setAtticWallpaper(self, atticWallpaper):
        self.setAtticWallpaper(atticWallpaper)
        self.d_setAtticWallpaper(atticWallpaper)

    def getAtticWallpaper(self):
        return self.atticWallpaper.getBlob()

    def setAtticWindows(self, atticWindows):
        self.atticWindows = CatalogItemList(atticWindows, store=CatalogItem.Customization)

    def d_setAtticWindows(self, atticWindows):
        self.sendUpdate('setAtticWindows', [atticWindows])

    def b_setAtticWindows(self, atticWindows):
        self.setAtticWindows(atticWindows)
        self.d_setAtticWindows(atticWindows)

    def getAtticWindows(self):
        return self.atticWindows.getBlob()

    def setDeletedItems(self, deletedItems):
        self.deletedItems = CatalogItemList(deletedItems, store=CatalogItem.Customization)

    def d_setDeletedItems(self, deletedItems):
        self.sendUpdate('setDeletedItems', [deletedItems])

    def b_setDeletedItems(self, deletedItems):
        self.setDeletedItems(deletedItems)
        self.d_setDeletedItems(deletedItems)

    def getDeletedItems(self):
        return self.deletedItems.getBlob()

    def suggestDirector(self, avId):
        if avId and avId != self.ownerId:
            self.air.writeServerEvent('suspicious', avId, 'av tried to manage furniture in someone else\'s house')
            return

        av = self.air.doId2do.get(avId)
        director = self.air.doId2do.get(self.director)
        if director:
            director.b_setGhostMode(0)
        else:
            av.b_setGhostMode(1)

        self.b_setDirector(avId)
        self.saveFurniture()

    def setDirector(self, director):
        self.director = director

    def d_setDirector(self, director):
        self.sendUpdate('setDirector', [director])

    def b_setDirector(self, director):
        self.setDirector(director)
        self.d_setDirector(director)

    def getDirector(self):
        return self.director

    def moveItemToAtticMessage(self, itemId, context):
        avId = self.air.getAvatarIdFromSender()
        owner = self._verifyOwner(avId, 'moveItemToAttic', context)
        if not owner:
            return

        item = self.air.doId2do.get(itemId)
        if not item or item not in self.items:
            self.sendUpdateToAvatarId(avId, 'moveItemToAtticResponse', [ToontownGlobals.FM_InvalidItem, context])

        self.atticItems.append(item.catalogItem)
        self.b_setAtticItems(self.getAtticItems())
        item.requestDelete()
        self.items.remove(item)
        self.sendUpdateToAvatarId(avId, 'moveItemToAtticResponse', [ToontownGlobals.FM_MovedItem, context])

    def moveItemFromAtticMessage(self, index, x, y, z, h, p, r, context):
        avId = self.air.getAvatarIdFromSender()
        owner = self._verifyOwner(avId, 'moveItemFromAttic', context)
        if not owner:
            return

        try:
            item = self.atticItems[index]
        except KeyError:
            self.air.writeServerEvent('suspicious', avId, 'av tried to move nonexistent attic item')
            self.sendUpdateToAvatarId(avId, 'moveItemFromAtticResponse', [ToontownGlobals.FM_InvalidIndex, context])
            return

        del self.atticItems[index]
        self.b_setAtticItems(self.getAtticItems())
        item.posHpr = (x, y, z, h, p, r)
        obj = self.generateItem(item)
        self.sendUpdateToAvatarId(avId, 'moveItemFromAtticResponse', [ToontownGlobals.FM_MovedItem, obj.doId, context])

    def deleteItemFromAtticMessage(self, blob, index, context):
        # blob is USELESS
        avId = self.air.getAvatarIdFromSender()
        owner = self._verifyOwner(avId, 'deleteItemFromAttic', context)
        if not owner:
            return

        try:
            item = self.atticItems[index]
        except KeyError:
            self.air.writeServerEvent('suspicious', avId, 'av tried to delete nonexistent attic item')
            self.sendUpdateToAvatarId(avId, 'deleteItemFromAtticResponse', [ToontownGlobals.FM_InvalidIndex, context])
            return

        if not item.isDeletable():
            self.sendUpdateToAvatarId(avId, 'deleteItemFromAtticResponse',
                                      [ToontownGlobals.FM_NondeletableItem, context])
            return

        del self.atticItems[index]
        self.b_setAtticItems(self.getAtticItems())
        self._deleteItem(item)
        self.sendUpdateToAvatarId(avId, 'deleteItemFromAtticResponse', [ToontownGlobals.FM_DeletedItem, context])

    def deleteItemFromRoomMessage(self, blob, itemId, context):
        # blob has no use here either
        avId = self.air.getAvatarIdFromSender()
        owner = self._verifyOwner(avId, 'deleteItemFromRoom', context)
        if not owner:
            return

        item = self.air.doId2do.get(itemId)
        if not item or item not in self.items:
            self.sendUpdateToAvatarId(avId, 'deleteItemFromRoomResponse', [ToontownGlobals.FM_InvalidItem, context])
            return

        if not item.catalogItem.isDeletable():
            self.sendUpdateToAvatarId(avId, 'deleteItemFromRoomResponse',
                                      [ToontownGlobals.FM_NondeletableItem, context])
            return

        self.items.remove(item)
        self._deleteItem(item.catalogItem)
        item.requestDelete()
        self.sendUpdateToAvatarId(avId, 'deleteItemFromRoomResponse', [ToontownGlobals.FM_DeletedItem, context])

    def moveWallpaperFromAtticMessage(self, index, room, context):
        avId = self.air.getAvatarIdFromSender()
        owner = self._verifyOwner(avId, 'moveWallpaperFromAttic', context)
        if not owner:
            return

        try:
            item = self.atticWallpaper[index]
        except KeyError:
            self.air.writeServerEvent('suspicious', avId, 'av tried to move nonexistent wallpaper')
            self.sendUpdateToAvatarId(avId, 'moveWallpaperFromAtticResponse',
                                      [ToontownGlobals.FM_InvalidIndex, context])
            return

        slot = room * CatalogSurfaceItem.NUM_ST_TYPES + item.getSurfaceType()
        self.atticWallpaper[index] = self.wallpaper[slot]
        self.b_setAtticWallpaper(self.getAtticWallpaper())
        self.wallpaper[slot] = item
        self.house.interior.b_setWallpaper(self.wallpaper.getBlob())
        self.sendUpdateToAvatarId(avId, 'moveWallpaperFromAtticResponse', [ToontownGlobals.FM_SwappedItem, context])

    def deleteWallpaperFromAtticMessage(self, blob, index, context):
        # you didn't expect blob to be used, right?
        avId = self.air.getAvatarIdFromSender()
        owner = self._verifyOwner(avId, 'deleteWallpaperFromAttic', context)
        if not owner:
            return

        try:
            item = self.atticWallpaper[index]
        except KeyError:
            self.air.writeServerEvent('suspicious', avId, 'av tried to delete nonexistent wallpaper')
            self.sendUpdateToAvatarId(avId, 'deleteWallpaperFromAtticResponse',
                                      [ToontownGlobals.FM_InvalidIndex, context])
            return

        del self.atticWallpaper[index]
        self.b_setAtticWallpaper(self.getAtticWallpaper())
        self._deleteItem(item)
        self.sendUpdateToAvatarId(avId, 'deleteWallpaperFromAtticResponse', [ToontownGlobals.FM_DeletedItem, context])

    def moveWindowToAtticMessage(self, slot, context):
        # meme
        pass

    def moveWindowFromAtticMessage(self, index, slot, context):
        avId = self.air.getAvatarIdFromSender()
        owner = self._verifyOwner(avId, 'moveWindowFromAttic', context)
        if not owner:
            return

        try:
            item = self.atticWindows[index]
        except KeyError:
            self.air.writeServerEvent('suspicious', avId, 'av tried to move nonexistent window')
            self.sendUpdateToAvatarId(avId, 'moveWindowFromAtticResponse', [ToontownGlobals.FM_InvalidIndex, context])
            return

        if slot > 5:
            self.air.writeServerEvent('suspicious', avId, 'av tried to put window in invalid slot!')
            return

        item.placement = slot
        oldWindow = None
        windowIndex = None
        for i, window in enumerate(self.windows):
            if window.placement == slot:
                oldWindow = window
                windowIndex = i

        if not oldWindow:
            self.sendUpdateToAvatarId(avId, 'moveWindowFromAtticResponse', [ToontownGlobals.FM_InvalidIndex, context])
            return

        self.atticWindows[index] = oldWindow
        self.d_setAtticWindows(self.getAtticWindows())
        self.windows[windowIndex] = item
        self.house.interior.b_setWindows(self.windows.getBlob())
        self.sendUpdateToAvatarId(avId, 'moveWindowFromAtticResponse', [ToontownGlobals.FM_SwappedItem, context])

    def moveWindowMessage(self, fromSlot, toSlot, context):
        # yes
        pass

    def deleteWindowFromAtticMessage(self, blob, index, context):
        # what is blob
        avId = self.air.getAvatarIdFromSender()
        owner = self._verifyOwner(avId, 'deleteWindowFromAttic', context)
        if not owner:
            return

        try:
            item = self.atticWindows[index]
        except KeyError:
            self.air.writeServerEvent('suspicious', avId, 'av tried to delete nonexistent window')
            self.sendUpdateToAvatarId(avId, 'deleteWindowFromAtticResponse', [ToontownGlobals.FM_InvalidIndex, context])
            return

        del self.atticWindows[index]
        self.d_setAtticWindows(self.getAtticWindows())
        self._deleteItem(item)
        self.sendUpdateToAvatarId(avId, 'deleteWindowFromAtticResponse', [ToontownGlobals.FM_DeletedItem, context])

    def recoverDeletedItemMessage(self, blob, index, context):
        # blob.
        avId = self.air.getAvatarIdFromSender()
        owner = self._verifyOwner(avId, 'recoverDeletedItem', context)
        if not owner:
            return

        numItems = len(self.atticItems) + len(self.atticWallpaper) + len(self.atticWindows) + len(self.items)
        if numItems + 1 > ToontownGlobals.MaxHouseItems:
            self.sendUpdateToAvatarId(avId, 'recoverDeletedItemResponse', [ToontownGlobals.FM_HouseFull, context])
            return

        try:
            item = self.deletedItems[index]
        except KeyError:
            self.air.writeServerEvent('suspicious', avId, 'av tried to recover nonexistent item')
            self.sendUpdateToAvatarId(avId, 'recoverDeletedItemResponse', [ToontownGlobals.FM_InvalidIndex, context])
            return

        type2attic = {
            CatalogSurfaceItem.CatalogSurfaceItem: (
                self.atticWallpaper, self.b_setAtticWallpaper, self.getAtticWallpaper),
            CatalogFurnitureItem.CatalogFurnitureItem: (self.atticItems, self.b_setAtticItems, self.getAtticItems),
            CatalogWindowItem.CatalogWindowItem: (self.atticWindows, self.b_setAtticWindows, self.getAtticWindows)
        }

        for itemType in type2attic.keys():
            if isinstance(item, itemType):
                attic, setter, getter = type2attic[itemType]
                attic.append(item)
                setter(getter())
                del self.deletedItems[index]
                self.b_setDeletedItems(self.getDeletedItems())
                self.removeDeletedItemBlob(item.getBlob().encode('base64'))
                self.sendUpdateToAvatarId(avId, 'recoverDeletedItemResponse',
                                          [ToontownGlobals.FM_RecoveredItem, context])

    def loadFurniture(self):
        for item in CatalogItemList(self.house.getInteriorItems(),
                                    store=CatalogItem.Customization | CatalogItem.Location):
            self.generateItem(item)

        self.wallpaper = CatalogItemList(self.house.getInteriorWallpaper(), store=CatalogItem.Customization)
        self.house.b_setInteriorWallpaper(self.house.getInteriorWallpaper())
        self.interior.b_setWallpaper(self.house.getInteriorWallpaper())
        self.windows = CatalogItemList(self.house.getInteriorWindows(),
                                       store=CatalogItem.Customization | CatalogItem.WindowPlacement)
        self.house.b_setInteriorWindows(self.house.getInteriorWindows())
        self.interior.b_setWindows(self.house.getInteriorWindows())
        self.b_setAtticItems(self.house.getAtticItems())
        self.b_setAtticWallpaper(self.house.getAtticWallpaper())
        self.b_setAtticWindows(self.house.getAtticWindows())
        self.b_setDeletedItems(self.house.getDeletedItems())

    def generateItem(self, item):
        itemId = item.furnitureType
        if itemId == 1399:
            furnitureClass = DistributedPhoneAI
        elif item.getFlags() & CatalogFurnitureItem.FLCloset:
            furnitureClass = DistributedClosetAI
        elif item.getFlags() & CatalogFurnitureItem.FLBank:
            furnitureClass = DistributedBankAI
        elif item.getFlags() & CatalogFurnitureItem.FLTrunk:
            furnitureClass = DistributedTrunkAI
        else:
            furnitureClass = DistributedFurnitureItemAI

        obj = furnitureClass(self.air, self.house, self, item)
        obj.generateWithRequired(self.interior.zoneId)
        self.items.append(obj)
        return obj

    def saveFurniture(self):
        self.house.b_setInteriorItems(self.getNewItems())
        self.house.b_setInteriorWallpaper(self.wallpaper.getBlob())
        self.house.b_setInteriorWindows(self.windows.getBlob())
        self.interior.b_setWindows(self.windows.getBlob())
        self.interior.b_setWallpaper(self.wallpaper.getBlob())
        self.house.b_setAtticItems(self.getAtticItems())
        self.b_setAtticItems(self.getAtticItems())
        self.house.b_setAtticWallpaper(self.getAtticWallpaper())
        self.b_setAtticWallpaper(self.getAtticWallpaper())
        self.house.b_setAtticWindows(self.getAtticWindows())
        self.b_setAtticWindows(self.getAtticWindows())
        self.house.b_setDeletedItems(self.getDeletedItems())
        self.b_setDeletedItems(self.getDeletedItems())

    def getNewItems(self):
        items = CatalogItemList(store=CatalogItem.Customization | CatalogItem.Location)
        for item in self.items:
            items.append(item.catalogItem)

        return items.getBlob()

    def _verifyOwner(self, avId, message, context):
        if self.house.avatarId != avId:
            self.air.writeServerEvent('suspicious', avId,
                                      'av tried to send perform furniture management operation %s while not owner!' % message)
            self.sendUpdateToAvatarId(avId, message + 'Response', [ToontownGlobals.FM_NotOwner, context])
            return False
        elif self.director != avId:
            self.sendUpdateToAvatarId(avId, message + 'Response', [ToontownGlobals.FM_NotDirector, context])
            return False

        return True

    def _deleteItem(self, item):
        self.deletedItems.append(item)
        if len(self.deletedItems) > ToontownGlobals.ExtraDeletedItems:
            del self.deletedItems[0]

        self.b_setDeletedItems(self.getDeletedItems())
        self.addDeletedItemBlob(item.getBlob().encode('base64'))

    def getNumItems(self):
        numItems = len(self.house.interiorItems) + len(self.house.atticItems) + len(self.house.atticWallpaper) + len(
            self.house.atticWindows) + len(self.house.interiorWallpaper) + len(self.house.interiorWindows)
        return numItems

    def getDeletedItemsFilename(self):
        return '%s%s%s%s.json' % (self.serverDataFolder, 'houses/', 'deletedItems_', self.house.getDoId())

    def loadDeletedItems(self):
        try:
            deletedItemsFile = open(self.deletedItemsFilename, 'r')
            deletedItemsData = json.load(deletedItemsFile)
            return deletedItemsData
        except:
            return {}

    def updateDeletedItemsFile(self):
        try:
            if not os.path.exists(os.path.dirname(self.deletedItemsFilename)):
                os.makedirs(os.path.dirname(self.deletedItemsFilename))

            deletedItemsFile = open(self.deletedItemsFilename, 'w')
            deletedItemsFile.seek(0)
            json.dump(self.day2deletedItems, deletedItemsFile)
            deletedItemsFile.close()
        except:
            pass

    def addDeletedItemBlob(self, deletedItemBlob, dayId=None):
        if dayId is None:
            dayId = getDayId()

        dayId = str(dayId)
        if dayId not in self.day2deletedItems.keys():
            self.day2deletedItems[dayId] = []

        self.day2deletedItems[dayId].append(deletedItemBlob)
        self.updateDeletedItemsFile()

    def removeDeletedItemBlob(self, deletedItemBlob, dayId=None):
        if not self.day2deletedItems.keys():
            return

        if dayId is None:
            dayId = getDayId()

        dayId = str(dayId)
        if dayId not in self.day2deletedItems.keys():
            dayId = min(self.day2deletedItems.keys())
        elif not self.day2deletedItems[dayId]:
            del self.day2deletedItems[dayId]
            dayId = min(self.day2deletedItems.keys())

        dayId = str(dayId)
        if dayId in self.day2deletedItems.keys() and deletedItemBlob in self.day2deletedItems[dayId]:
            self.day2deletedItems[dayId].remove(deletedItemBlob)

        if not self.day2deletedItems[dayId]:
            del self.day2deletedItems[dayId]

        self.updateDeletedItemsFile()

    def __deletedItemsTask(self, task):
        changesMade = False
        dayId = getDayId()
        for deletedItemDay, deletedItemBlobs in self.day2deletedItems.items():
            if not deletedItemBlobs or type(deletedItemBlobs) != list:
                del self.day2deletedItems[deletedItemDay]
                changesMade = True
                continue

            try:
                deletedItemDayId = int(deletedItemDay)
            except:
                del self.day2deletedItems[deletedItemDay]
                changesMade = True
                continue

            if deletedItemDayId + int(ToontownGlobals.DeletedItemLifetime / 60 / 24) <= dayId:
                for deletedItemBlob in deletedItemBlobs[:]:
                    try:
                        deletedItem = CatalogItem.getItem(deletedItemBlob.decode('base64'))
                    except:
                        self.day2deletedItems[deletedItemDay].remove(deletedItemBlob)
                        if not self.day2deletedItems[deletedItemDay]:
                            del self.day2deletedItems[deletedItemDay]

                        changesMade = True
                        continue

                    if isinstance(deletedItem, CatalogInvalidItem.CatalogInvalidItem):
                        self.day2deletedItems[deletedItemDay].remove(deletedItemBlob)
                        if not self.day2deletedItems[deletedItemDay]:
                            del self.day2deletedItems[deletedItemDay]

                        changesMade = True
                        continue

                    if deletedItem not in self.deletedItems:
                        self.day2deletedItems[deletedItemDay].remove(deletedItemBlob)
                        if not self.day2deletedItems[deletedItemDay]:
                            del self.day2deletedItems[deletedItemDay]

                        changesMade = True
                        continue

                    index = self.deletedItems.index(deletedItem)
                    del self.deletedItems[index]
                    self.b_setDeletedItems(self.getDeletedItems())
                    self.day2deletedItems[deletedItemDay].remove(deletedItemBlob)
                    if not self.day2deletedItems[deletedItemDay]:
                        del self.day2deletedItems[deletedItemDay]

                    changesMade = True

        if changesMade:
            self.updateDeletedItemsFile()

        # We want this task to run again at midnight. We'll calculate the seconds until midnight, then
        # delay the task from running again until then.
        tomorrow = self.air.toontownTimeManager.getCurServerDateTime().now(
            tz=self.air.toontownTimeManager.serverTimeZone) + datetime.timedelta(1)
        midnight = datetime.datetime(year=tomorrow.year, month=tomorrow.month, day=tomorrow.day, hour=0, minute=0,
                                     second=0, tzinfo=self.air.toontownTimeManager.serverTimeZone)
        secondsUntilMidnight = (midnight - self.air.toontownTimeManager.getCurServerDateTime().now(
            tz=self.air.toontownTimeManager.serverTimeZone)).seconds
        task.delayTime = secondsUntilMidnight
        return task.again
