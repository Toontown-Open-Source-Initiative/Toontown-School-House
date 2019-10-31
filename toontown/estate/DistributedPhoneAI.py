import time
from datetime import datetime

from direct.directnotify import DirectNotifyGlobal
from direct.distributed.ClockDelta import globalClockDelta

from toontown.catalog import CatalogItem
from toontown.catalog.CatalogInvalidItem import CatalogInvalidItem
from toontown.catalog.CatalogItemList import CatalogItemList
from toontown.catalog.GiftAvatarAI import GiftAvatarAI
from toontown.estate import PhoneGlobals
from toontown.estate.DistributedFurnitureItemAI import DistributedFurnitureItemAI
from toontown.toonbase import ToontownGlobals


class LoadGiftAvatar:

    def __init__(self, phone, avId, targetId, optional, callback):
        self.air = phone.air
        self.phone = phone
        self.avId = avId
        self.targetId = targetId
        self.optional = optional
        self.callback = callback

    def start(self):
        self.air.dbInterface.queryObject(self.air.dbId, self.targetId, self.__gotAvatar)

    def copyDict(self, aDict, *keys):
        return {key: aDict[key] for key in keys}

    def __gotAvatar(self, dclass, fields):
        if dclass != self.air.dclassesByName['DistributedToonAI']:
            return

        for key in (
                'setDNAString', 'setMailboxContents', 'setAwardMailboxContents', 'setGiftSchedule',
                'setDeliverySchedule', 'setAwardSchedule'):
            fields[key] = fields[key][0].encode('base64')

        newDict = self.copyDict(fields, 'setDNAString', 'setMailboxContents', 'setAwardMailboxContents',
                                'setGiftSchedule', 'setDeliverySchedule', 'setAwardSchedule', 'setHat', 'setGlasses',
                                'setBackpack', 'setShoes', 'setHatList', 'setGlassesList', 'setBackpackList',
                                'setShoesList', 'setCustomMessages', 'setEmoteAccess', 'setClothesTopsList',
                                'setClothesBottomsList', 'setPetTrickPhrases')

        self.callback(self.avId, self.targetId, newDict, self.optional)
        del self.phone.giftingOperations[self.avId]


class DistributedPhoneAI(DistributedFurnitureItemAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPhoneAI')

    def __init__(self, air, house, furnitureMgr, catalogItem):
        DistributedFurnitureItemAI.__init__(self, air, house, furnitureMgr, catalogItem)
        self.house = house
        self.furnitureMgr = furnitureMgr
        self.sx = 1
        self.sy = 1
        self.sz = 1
        self.initialScale = (self.sx, self.sy, self.sz)
        self.newScale = None
        self.avId = 0
        self.giftingOperations = {}

    def getInitialScale(self):
        return self.initialScale

    def setNewScale(self, sx, sy, sz):
        (self.sx, self.sy, self.sz) = (sx, sy, sz)
        self.newScale = (self.sx, self.sy, self.sz)

    def getNewScale(self):
        return self.newScale

    def avatarEnter(self):
        avId = self.air.getAvatarIdFromSender()
        if self.avId:
            self.sendUpdateToAvatarId(avId, 'freeAvatar', [])
            return

        av = self.air.doId2do.get(avId)
        if not av:
            return

        if not any((av.weeklyCatalog, av.backCatalog, av.monthlyCatalog)):
            self.d_setMovie(PhoneGlobals.PHONE_MOVIE_EMPTY, avId)
            self.d_setMovie(PhoneGlobals.PHONE_MOVIE_CLEAR, 0)
            return

        houseId = av.getHouseId()
        if not houseId:
            self.sendUpdateToAvatarId(avId, 'freeAvatar', [])
            return

        self.air.questManager.toonCalledClarabelle(av)
        house = self.air.doId2do.get(houseId)
        self.avId = avId
        self.d_setMovie(PhoneGlobals.PHONE_MOVIE_PICKUP, avId)
        if house:
            numItems = self.furnitureMgr.getNumItems()
            self.sendUpdateToAvatarId(avId, 'setLimits', [numItems])
        else:
            self.air.dbInterface.queryObject(self.air.dbId, houseId, self.__handleHouse)

        # Remove the "new catalog" icon:
        av.b_setCatalogNotify(ToontownGlobals.NoItems, av.mailboxNotify)
        self.acceptOnce(self.air.getAvatarExitEvent(avId), self.__handleUnexpectedExit, extraArgs=[avId])

    def __handleHouse(self, dclass, fields):
        if dclass != self.air.dclassesByName['DistributedHouseAI']:
            return

        interiorItems = CatalogItemList(fields['setInteriorItems'][0], store=CatalogItem.Customization)
        atticItems = CatalogItemList(fields['setAtticItems'][0], store=CatalogItem.Customization)
        atticWallpaper = CatalogItemList(fields['setAtticWallpaper'][0], store=CatalogItem.Customization)
        atticWindows = CatalogItemList(fields['setAtticWindows'][0], store=CatalogItem.Customization)
        interiorWallpaper = CatalogItemList(fields['setInteriorWallpaper'][0], store=CatalogItem.Customization)
        interiorWindows = CatalogItemList(fields['setInteriorWindows'][0], store=CatalogItem.Customization)
        numItems = len(interiorItems) + len(atticItems) + len(atticWallpaper) + len(atticWindows) + len(
            interiorWallpaper) + len(interiorWindows)
        self.sendUpdateToAvatarId(fields['setAvatarId'][0], 'setLimits', [numItems])

    def __handleUnexpectedExit(self, avId):
        if avId != self.avId:
            self.notify.warning('accepted exit event for av %s not using phone' % avId)
            return

        self.avId = 0
        self.d_setMovie(PhoneGlobals.PHONE_MOVIE_CLEAR, 0)

    def avatarExit(self):
        avId = self.air.getAvatarIdFromSender()
        if avId != self.avId:
            self.notify.warning('av %s tried to exit phone they were not using' % avId)
            return

        self.d_setMovie(PhoneGlobals.PHONE_MOVIE_HANGUP, avId)
        self.d_setMovie(PhoneGlobals.PHONE_MOVIE_CLEAR, 0)
        self.avId = 0
        self.ignore(self.air.getAvatarExitEvent(avId))

    def d_setMovie(self, mode, avId):
        self.sendUpdate('setMovie', [mode, avId, globalClockDelta.getRealNetworkTime(bits=32)])

    def requestPurchaseMessage(self, context, blob, optional):
        avId = self.air.getAvatarIdFromSender()
        accId = self.air.getAccountIdFromSender()
        av = self.air.doId2do.get(avId)
        if not av:
            self.air.writeServerEvent('suspicious', avId,
                                      'av tried to purchase something but they are not on the district!')
            return

        if avId != self.avId:
            self.air.writeServerEvent('suspicious', avId, 'av tried to purchase item while not at phone')
            self.sendUpdateToAvatarId(avId, 'requestPurchaseResponse', [context, ToontownGlobals.P_NotShopping])
            return

        item = CatalogItem.getItem(blob, store=CatalogItem.Customization)
        if isinstance(item, CatalogInvalidItem):
            self.air.writeServerEvent('suspicious', avId, 'av tried to purchase something but item is invalid!')
            self.sendUpdateToAvatarId(avId, 'requestPurchaseResponse', [context, ToontownGlobals.P_ItemAvailable])
            return

        if not any(item in catalog for catalog in (av.weeklyCatalog, av.backCatalog, av.monthlyCatalog)):
            self.air.writeServerEvent('suspicious', avId, 'av tried to purchase item not in catalog')
            self.sendUpdateToAvatarId(avId, 'requestPurchaseResponse', [context, ToontownGlobals.P_NotInCatalog])
            return

        def handleAccount(dclass, fields):
            if dclass != self.air.dclassesByName['AccountAI']:
                return

            # Based on game creation date:
            creationDate = fields['CREATED']
            try:
                creationDate = datetime.fromtimestamp(time.mktime(time.strptime(creationDate)))
            except ValueError:
                creationDate = ''

            accountDays = -1
            if creationDate:
                now = datetime.fromtimestamp(time.mktime(time.strptime(time.ctime())))
                accountDays = abs((now - creationDate).days)

            if accountDays < 0 or accountDays > 4294967295:
                accountDays = 100000

            daysToGo = item.loyaltyRequirement() - accountDays
            if daysToGo < 0:
                daysToGo = 0

            if daysToGo and config.GetBool('want-loyalty-requirement', False):
                self.air.writeServerEvent('suspicious', avId,
                                          'av tried to purchase a loyalty item before it is available!')
                return

            if item in av.backCatalog:
                price = item.getPrice(CatalogItem.CatalogTypeBackorder)
            else:
                price = item.getPrice(0)

            if price == 0:
                self.air.writeServerEvent('suspicious', avId,
                                          'av tried to purchase something but the price is invalid!')
                return

            # Take the jellybeans away:
            if price > av.getTotalMoney():
                self.air.writeServerEvent('suspicious', avId, 'Failed to take away the jellybeans from the avatar')
                self.sendUpdateToAvatarId(avId, 'requestPurchaseResponse', [context, ToontownGlobals.P_NotEnoughMoney])
                return

            if len(av.mailboxContents) >= ToontownGlobals.MaxMailboxContents:
                self.sendUpdateToAvatarId(avId, 'requestPurchaseResponse', [context, ToontownGlobals.P_MailboxFull])
                return

            if len(av.onOrder) + len(av.mailboxContents) + len(
                    av.onGiftOrder) + 1 >= ToontownGlobals.MaxMailboxContents:
                self.sendUpdateToAvatarId(avId, 'requestPurchaseResponse', [context, ToontownGlobals.P_OnOrderListFull])
                return

            retCode = ToontownGlobals.P_ItemOnOrder
            if not item.getDeliveryTime():
                retCode = item.recordPurchase(av, optional)
                deliveryTime = 0
            elif config.GetBool('want-instant-delivery', False):
                # Do we want instant delivery?
                deliveryTime = int(time.time() / 60) + 1
            else:
                deliveryTime = int(time.time() / 60) + item.getDeliveryTime()

            # Place the item for order:
            if deliveryTime:
                item.deliveryDate = deliveryTime
                av.onOrder.append(item)
                av.b_setDeliverySchedule(av.onOrder)

            self.sendUpdateToAvatarId(avId, 'requestPurchaseResponse', [context, retCode])
            if retCode in (ToontownGlobals.P_ItemOnOrder, ToontownGlobals.P_ItemAvailable):
                av.takeMoney(price)

        self.air.dbInterface.queryObject(self.air.dbId, accId, handleAccount)

    def requestGiftPurchaseMessage(self, context, targetId, blob, optional):
        avId = self.air.getAvatarIdFromSender()
        accId = self.air.getAccountIdFromSender()
        av = self.air.doId2do.get(avId)
        if not av:
            self.air.writeServerEvent('suspicious', avId,
                                      'av tried to gift something but they are not on the district!')
            return

        if avId != self.avId:
            self.air.writeServerEvent('suspicious', avId, 'av tried to gift item while not at phone')
            self.sendUpdateToAvatarId(avId, 'requestGiftPurchaseResponse', [context, ToontownGlobals.P_NotShopping])
            return

        item = CatalogItem.getItem(blob, store=CatalogItem.Customization)
        if isinstance(item, CatalogInvalidItem):
            self.air.writeServerEvent('suspicious', avId, 'av tried to gift something but item is invalid!')
            self.sendUpdateToAvatarId(avId, 'requestGiftPurchaseResponse', [context, ToontownGlobals.P_ItemAvailable])
            return

        if not any(item in catalog for catalog in (av.weeklyCatalog, av.backCatalog, av.monthlyCatalog)):
            self.air.writeServerEvent('suspicious', avId, 'av tried to gift item not in catalog')
            self.sendUpdateToAvatarId(avId, 'requestGiftPurchaseResponse', [context, ToontownGlobals.P_NotInCatalog])
            return

        def handleAccount(dclass, fields):
            if dclass != self.air.dclassesByName['AccountAI']:
                return

            # Based on game creation date:
            creationDate = fields['CREATED']
            try:
                creationDate = datetime.fromtimestamp(time.mktime(time.strptime(creationDate)))
            except ValueError:
                creationDate = ''

            accountDays = -1
            if creationDate:
                now = datetime.fromtimestamp(time.mktime(time.strptime(time.ctime())))
                accountDays = abs((now - creationDate).days)

            if accountDays < 0 or accountDays > 4294967295:
                accountDays = 100000

            daysToGo = item.loyaltyRequirement() - accountDays
            if daysToGo < 0:
                daysToGo = 0

            if daysToGo and config.GetBool('want-loyalty-requirement', False):
                self.air.writeServerEvent('suspicious', avId,
                                          'av tried to gift a loyalty item before it is available!')
                return

            if not item.isGift():
                self.air.writeServerEvent('suspicious', avId, 'av tried to gift an item that isn\'t a gift!')
                self.sendUpdateToAvatarId(avId, 'requestGiftPurchaseResponse', [context, ToontownGlobals.P_NotAGift])
                return

            if item in av.backCatalog:
                price = item.getPrice(CatalogItem.CatalogTypeBackorder)
            else:
                price = item.getPrice(0)

            # Take the jellybeans away:
            if price > av.getTotalMoney():
                self.air.writeServerEvent('suspicious', avId, 'Failed to take away the jellybeans from the avatar')
                self.sendUpdateToAvatarId(avId, 'requestGiftPurchaseResponse',
                                          [context, ToontownGlobals.P_NotEnoughMoney])
                return

            self.requestGiftAvatarOperation(avId, targetId, [context, item, price], self.attemptGiftPurchase)

        self.air.dbInterface.queryObject(self.air.dbId, accId, handleAccount)

    def requestGiftAvatarOperation(self, avId, doId, optional, callback):
        if avId in self.giftingOperations:
            return

        newGiftingOperation = LoadGiftAvatar(self, avId, doId, optional, callback)
        newGiftingOperation.start()
        self.giftingOperations[avId] = newGiftingOperation

    def attemptGiftPurchase(self, avId, targetId, avatar, optional):
        av = self.air.doId2do.get(avId)
        if not av:
            return

        recipient = GiftAvatarAI.createFromFields(avatar)
        context = optional[0]
        item = optional[1]
        if len(recipient.mailboxContents) >= ToontownGlobals.MaxMailboxContents:
            self.sendUpdateToAvatarId(avId, 'requestGiftPurchaseResponse', [context, ToontownGlobals.P_MailboxFull])
            return

        if len(recipient.onOrder) + len(recipient.mailboxContents) + len(
                recipient.onGiftOrder) + 1 >= ToontownGlobals.MaxMailboxContents:
            self.sendUpdateToAvatarId(avId, 'requestGiftPurchaseResponse', [context, ToontownGlobals.P_OnOrderListFull])
            return

        if item.reachedPurchaseLimit(recipient):
            self.sendUpdateToAvatarId(avId, 'requestGiftPurchaseResponse',
                                      [context, ToontownGlobals.P_ReachedPurchaseLimit])
            return

        retCode = ToontownGlobals.P_ItemOnOrder
        av.takeMoney(optional[2])
        recipient.addToGiftSchedule(avId, targetId, item, item.getDeliveryTime())
        self.sendUpdateToAvatarId(avId, 'requestGiftPurchaseResponse', [context, retCode])
