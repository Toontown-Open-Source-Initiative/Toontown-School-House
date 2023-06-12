from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD

from panda3d.core import *

from otp.otpbase import OTPLocalizer

from toontown.catalog import CatalogItemList
from toontown.catalog import CatalogItem
from toontown.catalog import CatalogItemTypes
from toontown.catalog import CatalogClothingItem
from toontown.catalog import CatalogAccessoryItem
from toontown.catalog import CatalogAccessoryItemGlobals
from toontown.catalog import CatalogFurnitureItem
from toontown.catalog import CatalogChatItem
from toontown.catalog import CatalogEmoteItem
from toontown.catalog import CatalogGenerator
from toontown.catalog import CatalogBeanItem
from toontown.catalog import CatalogWallpaperItem
from toontown.catalog import CatalogWindowItem
from toontown.catalog import CatalogFlooringItem
from toontown.catalog import CatalogWainscotingItem
from toontown.catalog import CatalogMouldingItem
from toontown.catalog import CatalogPetTrickItem
from toontown.catalog import CatalogRentalItem
from toontown.catalog import CatalogAnimatedFurnitureItem
from toontown.catalog import CatalogNametagItem
from toontown.catalog import CatalogGardenStarterItem
from toontown.catalog import CatalogPoleItem
from toontown.catalog import CatalogGardenItem
from toontown.catalog import CatalogToonStatueItem

from toontown.fishing import FishGlobals

from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownGlobals
from toontown.rpc import AwardManagerConsts
from toontown.rpc.AwardAvatarUD import AwardAvatarUD

import time

WrongGenderStr = "wrong gender"
JellybeanRewardValues = (1, 5, 10, 15, 20, 25, 50, 100, 150, 200, 250, 500, 750, 1000)

# How long does an Award sit on the awardOnOrder
AwardManagerDelayMinutes = ConfigVariableInt("award-delay-minutes", 30).getValue()

GiveAfterDelayTime = 1
GiveImmediately = 2
TryToRemove = 3
GiveAfterOneMinute = 4
NukeAllAwards = 5


class AwardManagerUD(DistributedObjectGlobalUD):
    """
    Uberdog object for making promo awards to Toons
    """
    notify = directNotify.newCategory('AwardManagerUD')

    def __init__(self, air):
        """Construct ourselves."""
        assert self.notify.debugCall()
        DistributedObjectGlobalUD.__init__(self, air)

        self.air = air

        self._dcRequestSerialGen = SerialNumGen(1)
        self._dcId2info = {}

        self.awardChoices = self.getAwardChoices()  # award Choices is a dict of dicts
        self.reverseDictAwardChoices = self.getReversedAwardChoices()

    def announceGenerate(self):
        """Start accepting http requests."""
        assert self.notify.debugCall()
        DistributedObjectGlobalUD.announceGenerate(self)

    def copyDict(self, aDict, *keys):
        return {key: aDict[key] for key in keys}

    def _getCatalogItemObj(self, itemType, itemIndex):
        if itemType == CatalogItemTypes.CLOTHING_ITEM:
            clothingNumber = itemIndex
            # for now always the first color choice
            itemObj = CatalogClothingItem.CatalogClothingItem(clothingNumber, 0)
            itemObj.giftTag = 0
            itemObj.giftCode = 1
        elif itemType == CatalogItemTypes.ACCESSORY_ITEM:
            accessoryNumber = itemIndex
            itemObj = CatalogAccessoryItem.CatalogAccessoryItem(accessoryNumber)
            itemObj.giftTag = 0
            itemObj.giftCode = 1
        elif itemType == CatalogItemTypes.FURNITURE_ITEM:
            furnitureNumber = itemIndex
            itemObj = CatalogFurnitureItem.CatalogFurnitureItem(furnitureNumber, colorOption=0)
        elif itemType == CatalogItemTypes.CHAT_ITEM:
            chatIndex = itemIndex
            itemObj = CatalogChatItem.CatalogChatItem(chatIndex)
        elif itemType == CatalogItemTypes.EMOTE_ITEM:
            emoteIndex = itemIndex
            itemObj = CatalogEmoteItem.CatalogEmoteItem(emoteIndex)
        elif itemType == CatalogItemTypes.BEAN_ITEM:
            numBeans = itemIndex
            if not numBeans in JellybeanRewardValues:
                self.air.writeServerEvent("suspicious", "giving %s beans" % numBeans)
            # an assertion exception will occur so the jellybean won't get rewarded
            assert (numBeans in JellybeanRewardValues)
            itemObj = CatalogBeanItem.CatalogBeanItem(numBeans)
        elif itemType == CatalogItemTypes.WALLPAPER_ITEM:
            wallPaperNumber = itemIndex
            itemObj = CatalogWallpaperItem.CatalogWallpaperItem(wallPaperNumber, colorIndex=0)
        elif itemType == CatalogItemTypes.WINDOW_ITEM:
            windowNumber = itemIndex
            itemObj = CatalogWindowItem.CatalogWindowItem(windowNumber,  placement=0)
        elif itemType == CatalogItemTypes.FLOORING_ITEM:
            flooringNumber = itemIndex
            itemObj = CatalogFlooringItem.CatalogFlooringItem(flooringNumber,  colorIndex=0)
        elif itemType == CatalogItemTypes.MOULDING_ITEM:
            mouldingNumber = itemIndex
            itemObj = CatalogMouldingItem.CatalogMouldingItem(mouldingNumber,  colorIndex=0)
        elif itemType == CatalogItemTypes.WAINSCOTING_ITEM:
            wainscotingNumber = itemIndex
            itemObj = CatalogWainscotingItem.CatalogWainscotingItem(wainscotingNumber,  colorIndex=0)
        elif itemType == CatalogItemTypes.PET_TRICK_ITEM:
            trickId = itemIndex
            itemObj = CatalogPetTrickItem.CatalogPetTrickItem(trickId)
        elif itemType == CatalogItemTypes.RENTAL_ITEM:
            # TODO since all we offer so far is 48 hours of cannons, values pulled for CatalogGenerator
            # do something else if we have different durations
            rentalType = itemIndex
            itemObj = CatalogRentalItem.CatalogRentalItem(rentalType, 2880, 1000)
        elif itemType == CatalogItemTypes.ANIMATED_FURNITURE_ITEM:
            furnitureNumber = itemIndex
            itemObj = CatalogAnimatedFurnitureItem.CatalogAnimatedFurnitureItem(furnitureNumber, colorOption=0)
        elif itemType == CatalogItemTypes.NAMETAG_ITEM:
            nameTagType = itemIndex
            itemObj = CatalogNametagItem.CatalogNametagItem(nameTagType)
        elif itemType == CatalogItemTypes.GARDENSTARTER_ITEM:
            itemObj = CatalogGardenStarterItem.CatalogGardenStarterItem()
        elif itemType == CatalogItemTypes.POLE_ITEM:
            rodId = itemIndex
            itemObj = CatalogPoleItem.CatalogPoleItem(rodId)
        elif itemType == CatalogItemTypes.GARDEN_ITEM:
            gardenType = itemIndex
            itemObj = CatalogGardenItem.CatalogGardenItem(gardenType, 1)
        elif itemType == CatalogItemTypes.TOON_STATUE_ITEM:
            gardenType = itemIndex
            itemObj = CatalogToonStatueItem.CatalogToonStatueItem(gardenType)
        else:
            self.notify.warning("Invalid item (%s, %s) being redeemed, Giving a bean instead!" % (str(itemType), str(itemIndex)))
            itemObj = CatalogBeanItem.CatalogBeanItem(1)
        return itemObj

    def checkGender(self, toon, catalogItem):
        """Return None if everything is ok and we don't have mismatched sex."""
        if ((catalogItem.forBoysOnly() and toon.dna.getGender() == 'f') or (catalogItem.forGirlsOnly() and toon.dna.getGender() == 'm')):
            return ToontownGlobals.P_WillNotFit

        return None

    def checkRewardable(self, catalogItem):
        """Return None if everything is ok and the item is rewardable."""
        if not catalogItem.isRewardable():
            return ToontownGlobals.P_NotAGift

        return None

    def checkFullMailbox(self, toon, catalogItem):
        """Return None if he has space in his mailbox."""
        rAv = toon
        result = None

        if len(rAv.awardMailboxContents) + len(rAv.onAwardOrder) >= ToontownGlobals.MaxMailboxContents:
            if len(rAv.awardMailboxContents) == 0:
                result = ToontownGlobals.P_OnAwardOrderListFull
            else:
                result = ToontownGlobals.P_AwardMailboxFull
        return result

    def checkDuplicate(self, toon, catalogItem):
        """Return None if he doesn't have this item yet. an error code from GiveAwardErrors otherwise"""
        result = None
        checkDup = toon.checkForDuplicateItem(catalogItem)

        if checkDup == ToontownGlobals.P_ItemInMailbox:
            result = AwardManagerConsts.GiveAwardErrors.AlreadyInMailbox
        elif checkDup == ToontownGlobals.P_ItemOnGiftOrder:
            result = AwardManagerConsts.GiveAwardErrors.AlreadyInGiftQueue
        elif checkDup == ToontownGlobals.P_ItemOnOrder:
            result = AwardManagerConsts.GiveAwardErrors.AlreadyInOrderedQueue
        elif checkDup == ToontownGlobals.P_ItemInCloset:
            result = AwardManagerConsts.GiveAwardErrors.AlreadyInCloset
        elif checkDup == ToontownGlobals.P_ItemInTrunk:
            result = AwardManagerConsts.GiveAwardErrors.AlreadyInTrunk
        elif checkDup == ToontownGlobals.P_ItemAlreadyWorn:
            result = AwardManagerConsts.GiveAwardErrors.AlreadyBeingWorn
        elif checkDup == ToontownGlobals.P_ItemInAwardMailbox:
            result = AwardManagerConsts.GiveAwardErrors.AlreadyInAwardMailbox
        elif checkDup == ToontownGlobals.P_ItemOnAwardOrder:
            result = AwardManagerConsts.GiveAwardErrors.AlreadyInThirtyMinuteQueue
        elif checkDup == ToontownGlobals.P_ItemInMyPhrases:
            result = AwardManagerConsts.GiveAwardErrors.AlreadyInMyPhrases
        elif checkDup == ToontownGlobals.P_ItemInPetTricks:
            result = AwardManagerConsts.GiveAwardErrors.AlreadyKnowDoodleTraining
        elif checkDup == ToontownGlobals.P_ItemAlreadyUsed:
            result = AwardManagerConsts.GiveAwardErrors.AlreadyStartedGarden
        elif checkDup == ToontownGlobals.P_FishingRodAlreadyOwned:
            result = AwardManagerConsts.GiveAwardErrors.AlreadyOwnFishingRod
        elif checkDup == ToontownGlobals.P_GardenSkillTooLow:
            result = AwardManagerConsts.GiveAwardErrors.GardenSkillTooLow
        elif checkDup == ToontownGlobals.P_NoGardenStarted:
            result = AwardManagerConsts.GiveAwardErrors.NoGardenStarted
        elif checkDup:
            # HACK: store the catalog error on self
            # this will not work properly if the error checking happens after a second call to this method
            self._catalogError = checkDup
            result = AwardManagerConsts.GiveAwardErrors.GenericAlreadyHaveError

        return result

    def validateItem(self, toon, catalogItem):
        """Returns (True, AwardManagerConsts.GiveAwardErrors.Success) if everything is ok, otherwise returns (False,<error reason>)"""
        retcode = None

        retcode = self.checkGender(toon, catalogItem)
        if retcode:
            return (False, AwardManagerConsts.GiveAwardErrors.WrongGender)

        retcode = self.checkRewardable(catalogItem)
        if retcode:
            return (False, AwardManagerConsts.GiveAwardErrors.NotRewardable)

        retcode = self.checkFullMailbox(toon, catalogItem)
        if retcode:
            return (False, AwardManagerConsts.GiveAwardErrors.FullAwardMailbox)

        result = self.checkDuplicate(toon, catalogItem)
        if result:
            return (False, result)

        return (True, "success")
        # add other checks here

    def giveItemToToon(self, toon, checkedAvId, fields, activated, catalogItem, specialEventId, specialCommands):
        """All checks passed, give the toon the item. Returns True if all ok"""
        self.giveToonResult = True
        catalogItem.specialEventId = specialEventId

        if specialCommands == GiveImmediately:
            curItemList = toon.awardMailboxContents
            curItemList.append(catalogItem)
            newBlob = curItemList.getBlob(store=CatalogItem.Customization)

            if activated:
                self.air.sendUpdateToDoId("DistributedToon", "setAwardMailboxContents", checkedAvId, [newBlob])
            else:
                def __handleSetAwardMailboxContents(fields):
                    if fields:
                        self.giveToonResult = False

                self.air.dbInterface.updateObject(self.air.dbId, checkedAvId, self.air.dclassesByName['DistributedToonUD'], {'setAwardMailboxContents': (newBlob,)}, {
                                                  'setAwardMailboxContents': (fields['setAwardMailboxContents'],)}, __handleSetAwardMailboxContents)
        else:
            now = int(time.time() / 60 + 0.5)

            if specialCommands == GiveAfterOneMinute:
                delay = 1
            else:
                delay = AwardManagerDelayMinutes

            future = now + delay

            curOnAwardOrderList = toon.onAwardOrder
            catalogItem.deliveryDate = future
            curOnAwardOrderList.append(catalogItem)
            newBlob = curOnAwardOrderList.getBlob(store=CatalogItem.Customization | CatalogItem.DeliveryDate)

            if activated:
                self.air.sendUpdateToDoId("DistributedToon", "setAwardSchedule", checkedAvId, [newBlob])
            else:
                def __handleSetAwardSchedule(fields):
                    if fields:
                        self.giveToonResult = False

                self.air.dbInterface.updateObject(self.air.dbId, checkedAvId, self.air.dclassesByName['DistributedToonUD'], {
                                                  'setAwardSchedule': (newBlob,)}, {'setAwardSchedule': (fields['setAwardSchedule'],)}, __handleSetAwardSchedule)

        return self.giveToonResult

    def giveAwardToToon(self, context, replyToDoId, replyToClass, avId, awardType, awardItemId):
        assert self.notify.debugStateCall(self)

        self.air.writeServerEvent('giveAwardCodeRequest', avId, '%s|%s' % (str(awardType), str(awardItemId)))
        dcId = next(self._dcRequestSerialGen)
        self._dcId2info[dcId] = ScratchPad(replyToClass=replyToClass,
                                           replyToDoId=replyToDoId,
                                           context=context)

        catalogItem = self._getCatalogItemObj(awardType, awardItemId)
        specialEventId = 1
        specialCommands = GiveAfterOneMinute

        def handleAvatar(dclass, fields):
            if dclass != self.air.dclassesByName['DistributedToonUD']:
                self.notify.warning("Got not a toon account!")
                self.sendGiveAwardToToonReply(dcId, AwardManagerConsts.GiveAwardErrors.NonToon)
                return

            """Validate then give the catalog item to the toons."""
            def __avatarOnlineResp(checkedAvId, activated):
                giveAwardErrors = {}
                newFields = fields

                for key in ('setDeliverySchedule', 'setGiftSchedule', 'setMailboxContents', 'setAwardMailboxContents', 'setAwardSchedule', 'setDNAString'):
                    newFields[key] = newFields[key][0].encode('base64')

                avatarFields = self.copyDict(newFields,
                                             'setDeliverySchedule', 'setGiftSchedule', 'setMailboxContents',
                                             'setAwardMailboxContents', 'setAwardSchedule', 'setDNAString',
                                             'setClothesTopsList', 'setClothesBottomsList', 'setEmoteAccess',
                                             'setCustomMessages', 'setPetTrickPhrases', 'setHatList',
                                             'setGlassesList', 'setBackpackList', 'setShoesList',
                                             'setHat', 'setGlasses', 'setBackpack', 'setShoes',
                                             'setNametagStyle', 'setFishingRod',
                                             'setGardenStarted', 'setShovelSkill', 'setShovel'
                                             )

                toon = AwardAvatarUD.createFromFields(avatarFields)

                if toon:
                    success, error = self.validateItem(toon, catalogItem)
                    if success:
                        self.notify.debug('Hit success for item: %s' % (catalogItem))
                        success = self.giveItemToToon(toon, checkedAvId, fields, activated, catalogItem, specialEventId, specialCommands)
                        if success:
                            self.notify.debug('Hit success for AvID: %s' % (checkedAvId))
                            giveAwardErrors[checkedAvId] = AwardManagerConsts.GiveAwardErrors.Success
                        else:
                            self.notify.warning('Hit Unknown error for AvID: %s' % (checkedAvId))
                            giveAwardErrors[checkedAvId] = AwardManagerConsts.GiveAwardErrors.UnknownError
                    else:
                        self.notify.warning('Hit %s error for AvID: %s' % (AwardManagerConsts.GiveAwardErrorStrings[error], checkedAvId))
                        giveAwardErrors[checkedAvId] = error
                else:
                    self.notify.warning('Hit Unknown Toon error for AvID: %s' % (checkedAvId))
                    giveAwardErrors[checkedAvId] = AwardManagerConsts.GiveAwardErrors.UnknownToon

                assert len(giveAwardErrors) == 1
                errorCode = giveAwardErrors[list(giveAwardErrors.keys())[0]]
                self.sendGiveAwardToToonReply(dcId, errorCode)

            self.air.getActivated(avId, __avatarOnlineResp)

        self.air.dbInterface.queryObject(self.air.dbId, avId, handleAvatar)

    def sendGiveAwardToToonReply(self, dcId, result):
        info = self._dcId2info.pop(dcId)
        self.air.dispatchUpdateToGlobalDoId(info.replyToClass, "giveAwardToToonResult",
                                            info.replyToDoId, [info.context, result])

    @classmethod
    def getClothingChoices(cls):
        """Return a dictionary of clothing choices. Key is the description, clothingtype are values."""
        values = {}
        for key in list(CatalogClothingItem.ClothingTypes.keys()):
            clothingItem = CatalogClothingItem.ClothingTypes[key]
            typeOfClothes = clothingItem[0]
            styleString = clothingItem[1]
            if typeOfClothes in (CatalogClothingItem.AShirt,
                                 CatalogClothingItem.ABoysShirt, CatalogClothingItem.AGirlsShirt):
                textString = TTLocalizer.AwardMgrShirt
                # if its an exclusive boy or girl item, then say so
                if typeOfClothes == CatalogClothingItem.ABoysShirt:
                    textString += ' ' + TTLocalizer.AwardMgrBoy
                elif typeOfClothes == CatalogClothingItem.AGirlsShirt:
                    textString += ' ' + TTLocalizer.AwardMgrGirl
                else:
                    textString += ' ' + TTLocalizer.AwardMgrUnisex
                textString += ' ' + TTLocalizer.ShirtStylesDescriptions[styleString]
                if textString in values:
                    cls.notify.error("Fix %s, descriptions must be unique" % textString)
                values[textString] = key

        # do a 2nd for loop to ensure bottoms always goes last
        for key in list(CatalogClothingItem.ClothingTypes.keys()):
            clothingItem = CatalogClothingItem.ClothingTypes[key]
            typeOfClothes = clothingItem[0]
            styleString = clothingItem[1]
            if typeOfClothes in (CatalogClothingItem.AShorts, CatalogClothingItem.ABoysShorts,
                                 CatalogClothingItem.AGirlsShorts, CatalogClothingItem.AGirlsSkirt):
                textString = ""
                if typeOfClothes == CatalogClothingItem.AGirlsSkirt:
                    textString = TTLocalizer.AwardMgrSkirt
                else:
                    textString = TTLocalizer.AwardMgrShorts
                # if its an exclusive boy or girl item, then say so
                if typeOfClothes == CatalogClothingItem.ABoysShorts:
                    textString += ' ' + TTLocalizer.AwardMgrBoy
                elif typeOfClothes in (CatalogClothingItem.AGirlsShorts, CatalogClothingItem.AGirlsSkirt):
                    textString += ' ' + TTLocalizer.AwardMgrGirl
                else:
                    textString += ' ' + TTLocalizer.AwardMgrUnisex
                textString += ' ' + TTLocalizer.BottomStylesDescriptions[styleString]
                if textString in values:
                    cls.notify.error("Fix %s, descriptions must be unique" % textString)
                values[textString] = key
        return values

    @classmethod
    def getAccessoryChoices(cls):
        """Return a dictionary of accessories choices. Key is the description, accessorytype are values."""
        values = {}
        for key in list(CatalogAccessoryItemGlobals.AccessoryTypes.keys()):
            accessoryItem = CatalogAccessoryItemGlobals.AccessoryTypes[key]
            typeOfAccessory = accessoryItem[0]
            descString = TTLocalizer.AccessoryNamePrefix[typeOfAccessory] + TTLocalizer.AccessoryTypeNames[key]
            if descString in values:
                cls.notify.error("Fix %s, descriptions must be unique" % descString)
            values[descString] = key
        return values

    @classmethod
    def getFurnitureChoices(cls):
        """Return a dictionary of furniture choices. Key is the description , values is the furniture type key"""
        values = {}
        for key in list(CatalogFurnitureItem.FurnitureTypes.keys()):
            furnitureItem = CatalogFurnitureItem.FurnitureTypes[key]
            typeOfFurniture = key
            # we must not give animted furniture choices, the item type is wrong for it
            if typeOfFurniture in CatalogAnimatedFurnitureItem.AnimatedFurnitureItemKeys:
                continue
            descString = TTLocalizer.AwardManagerFurnitureNames[typeOfFurniture]
            if descString in values:
                cls.notify.error("Fix %s, descriptions must be unique" % descString)
            values[descString] = key
        return values

    @classmethod
    def getSpeedChatChoices(cls):
        """Return a dictionary of speed chat choices. Key is the description , values is the chat id"""
        values = {}
        allChatItems = CatalogGenerator.getAllChatItemsSold()
        for chatItem in allChatItems:
            speedChatKey = chatItem.customIndex
            textString = OTPLocalizer.CustomSCStrings[speedChatKey]
            # I really can't mess with the strings, I'll add the speedChatKey at the end
            keyStr = "%5d" % speedChatKey
            textString = keyStr + " " + textString
            # javascript messes up with a " in the string
            textString = textString.replace('"', "'")
            if textString in values:
                cls.notify.error("fix duplicate %s" % textString)
            values[textString] = speedChatKey
        return values

    @classmethod
    def getEmoteChoices(cls):
        """Return a dictionary of emote choices. Key is the description , values is the emote id"""
        values = {}
        for key in list(OTPLocalizer.EmoteFuncDict.keys()):
            descString = key
            emoteIndex = OTPLocalizer.EmoteFuncDict[key]
            if descString in values:
                cls.notify.error("Fix %s, descriptions must be unique" % descString)
            values[descString] = emoteIndex
        return values

    @classmethod
    def getBeanChoices(cls):
        """Return a dictionary of bean choices. Key is the description , values is the amount of beans"""
        values = {}
        for key in JellybeanRewardValues:
            descString = "%3d" % key
            if descString in values:
                cls.notify.error("Fix %s, descriptions must be unique" % descString)
            values[descString] = key
        return values

    @classmethod
    def getWallpaperChoices(cls):
        """Return a dictionary of wallpaper choices. Key is the description , values is the wallpaper id"""
        values = {}
        for key in list(CatalogWallpaperItem.WallpaperTypes.keys()):
            # the comments on CatalogWallpaperItem say 2920 to 2980 are problematic, so don't include them
            if key in (2920, 2930, 2940, 2950, 2960, 2970, 2980):
                continue
            # we have duplicate names, just add the key to be unique
            descString = "%5d " % key
            # ok it looks like some items are never offered, so if there's no name for it
            # lets not include it
            if key in TTLocalizer.WallpaperNames:
                descString += TTLocalizer.WallpaperNames[key]
                if descString in values:
                    cls.notify.error("Fix %s, descriptions must be unique" % descString)
                values[descString] = key
        return values

    @classmethod
    def getWindowViewChoices(cls):
        """Return a dictionary of window choices. Key is the description , values is the wallpaper id"""
        values = {}
        for key in list(CatalogWindowItem.WindowViewTypes.keys()):
            descString = ""
            descString += TTLocalizer.WindowViewNames[key]
            if descString in values:
                cls.notify.error("Fix %s, descriptions must be unique" % descString)
            values[descString] = key
        return values

    @classmethod
    def getFlooringChoices(cls):
        """Return a dictionary of flooring choices. Key is the description , values is the wallpaper id"""
        values = {}
        for key in list(CatalogFlooringItem.FlooringTypes.keys()):
            descString = "%5d " % key  # add key to make it unique
            descString += TTLocalizer.FlooringNames[key]
            if descString in values:
                cls.notify.error("Fix %s, descriptions must be unique" % descString)
            values[descString] = key
        return values

    @classmethod
    def getMouldingChoices(cls):
        """Return a dictionary of moulding choices. Key is the description , values is the wallpaper id"""
        values = {}
        for key in list(CatalogMouldingItem.MouldingTypes.keys()):
            descString = "%5d " % key  # add key to make it unique
            descString += TTLocalizer.MouldingNames[key]
            if descString in values:
                cls.notify.error("Fix %s, descriptions must be unique" % descString)
            values[descString] = key
        return values

    @classmethod
    def getWainscotingChoices(cls):
        """Return a dictionary of wainscotting choices. Key is the description , values is the wallpaper id"""
        values = {}
        for key in list(CatalogWainscotingItem.WainscotingTypes.keys()):
            descString = ""  # %5d " % key # add key to make it unique
            descString += TTLocalizer.WainscotingNames[key]
            if descString in values:
                cls.notify.error("Fix %s, descriptions must be unique" % descString)
            values[descString] = key
        return values

    @classmethod
    def getPetTrickChoices(cls):
        """Return a dictionary of pet trick choices. Key is the description , values is the trick id"""
        values = {}
        allTricks = CatalogPetTrickItem.getAllPetTricks()
        for oneTrick in allTricks:
            descString = ""  # %5d " % key # add key to make it unique
            descString += oneTrick.getName()
            key = oneTrick.trickId
            if descString in values:
                cls.notify.error("Fix %s, descriptions must be unique" % descString)
            values[descString] = key
        return values

    @classmethod
    def getRentalChoices(cls):
        """Return a dictionary of rental choices. Key is the description , values is the rental id"""
        values = {}
        allRentals = CatalogRentalItem.getAllRentalItems()
        for oneRental in allRentals:
            descString = ""  # %5d " % key # add key to make it unique
            descString += oneRental.getName()
            key = oneRental.typeIndex
            if descString in values:
                cls.notify.error("Fix %s, descriptions must be unique" % descString)
            values[descString] = key
        return values

    @classmethod
    def getAnimatedFurnitureChoices(cls):
        """Return a dictionary of furniture choices. Key is the description , values is the furniture type key"""
        values = {}
        for key in CatalogAnimatedFurnitureItem.AnimatedFurnitureItemKeys:
            furnitureItem = CatalogFurnitureItem.FurnitureTypes[key]
            typeOfFurniture = key
            descString = TTLocalizer.AwardManagerFurnitureNames[typeOfFurniture]
            if descString in values:
                cls.notify.error("Fix %s, descriptions must be unique" % descString)
            values[descString] = key
        return values

    @classmethod
    def getNametagChoices(cls):
        """Return a dictionary of nametag choices. Key is the description , values is the nametag type key"""
        values = {}

        for key in CatalogNametagItem.NametagItemKeys:
            descString = TTLocalizer.AwardManagerNametagNames[key]
            if descString in values:
                cls.notify.error("Fix %s, descriptions must be unique" % descString)
            values[descString] = key

        return values

    @classmethod
    def getGardenStarterChoices(cls):
        """Return a dictionary of garden starter choices. Key is the description , values is nothing"""
        values = {
            'garden starter': 0
        }

        return values

    @classmethod
    def getFishingRodChoices(cls):
        """Return a dictionary of Fishing Rod choices. Key is the description , values is the nametag type key"""
        values = {}

        for rodId in range(0, FishGlobals.MaxRodId + 1):
            descString = TTLocalizer.FishingRod % TTLocalizer.FishingRodNameDict[rodId]
            if descString in values:
                cls.notify.error("Fix %s, descriptions must be unique" % descString)
            values[descString] = rodId

        return values

    @classmethod
    def getGardenItemChoices(cls):
        """Return a dictionary of Garden Item choices. Key is the description , values is the nametag type key"""
        values = {}

        for key in CatalogGardenItem.GardenItemKeys:
            descString = TTLocalizer.AwardManagerGardenItemNames[key]
            if descString in values:
                cls.notify.error("Fix %s, descriptions must be unique" % descString)
            values[descString] = key

        return values

    @classmethod
    def getToonStatueChoices(cls):
        """Return a dictionary of Toon Statue choices. Key is the description , values is the nametag type key"""
        values = {}

        for key in CatalogToonStatueItem.GardenStatueKeys:
            descString = TTLocalizer.AwardManagerToonStatueNames[key]
            if descString in values:
                cls.notify.error("Fix %s, descriptions must be unique" % descString)
            values[descString] = key

        return values

    @classmethod
    def getReversedAwardChoices(cls):
        """The key in the returned dictionaries should be catalog item numbers, the value should be desc strings."""
        if hasattr(cls, '_revAwardChoices'):
            return cls._revAwardChoices
        result = {}
        awardChoices = cls.getAwardChoices()
        for itemType in awardChoices:
            reversedDict = {}
            curDict = awardChoices[itemType]
            for descString in curDict:
                itemId = curDict[descString]
                if itemId in reversedDict:
                    cls.notify.error("item %s already in %s" % (itemId, reversedDict))
                reversedDict[itemId] = descString
            result[itemType] = reversedDict
        cls._revAwardChoices = result
        return result

    @classmethod
    def getAwardChoicesArray(cls):
        """Return a JSON Object containing all reward types, their names, the rewards associated and if its a manual reward or not"""
        if hasattr(cls, '_awardChoicesArray'):
            return cls._awardChoicesArray

        def _isValidManualCodeRewardType(rewardType):
            isPermanent = rewardType not in CatalogItemTypes.NonPermanentItemTypes
            multipleAllowed = CatalogItemTypes.CatalogItemType2multipleAllowed[rewardType]
            return (isPermanent and (not multipleAllowed))

        result = []

        awardChoices = cls.getAwardChoices()

        for itemType in awardChoices:
            rewardArray = []

            curDict = awardChoices[itemType]
            for descString in curDict:
                itemId = curDict[descString]
                if any(obj['itemId'] == itemId for obj in rewardArray):
                    cls.notify.error("item %s already in %s" % (itemId, rewardArray))

                rewardArray.append({
                    'itemId': itemId,
                    'description': descString
                })

            result.append({
                'rewardType': itemType,
                'rewardName': AwardManagerUD.getAwardTypeName(itemType),
                'rewards': rewardArray,
                'manualReward': _isValidManualCodeRewardType(itemType)
            })

        cls._awardChoicesArray = result
        return result

    @classmethod
    def getAwardChoices(cls):
        """Return a tree of the choices for our drop down list."""
        # static data, cache it
        if hasattr(cls, '_awardChoices'):
            return cls._awardChoices
        result = {}
        for itemType in list(CatalogItemTypes.CatalogItemTypes.values()):
            if itemType == CatalogItemTypes.INVALID_ITEM:
                # we really can't give this out as awards, so don't add them to the choices
                continue
            if itemType == CatalogItemTypes.CLOTHING_ITEM:
                values = cls.getClothingChoices()
                result[itemType] = values
            elif itemType == CatalogItemTypes.ACCESSORY_ITEM:
                values = cls.getAccessoryChoices()
                result[itemType] = values
            elif itemType == CatalogItemTypes.FURNITURE_ITEM:
                values = cls.getFurnitureChoices()
                result[itemType] = values
            elif itemType == CatalogItemTypes.CHAT_ITEM:
                values = cls.getSpeedChatChoices()
                result[itemType] = values
            elif itemType == CatalogItemTypes.EMOTE_ITEM:
                values = cls.getEmoteChoices()
                result[itemType] = values
            elif itemType == CatalogItemTypes.BEAN_ITEM:
                values = cls.getBeanChoices()
                result[itemType] = values
            elif itemType == CatalogItemTypes.WALLPAPER_ITEM:
                values = cls.getWallpaperChoices()
                result[itemType] = values
            elif itemType == CatalogItemTypes.WINDOW_ITEM:
                values = cls.getWindowViewChoices()
                result[itemType] = values
            elif itemType == CatalogItemTypes.FLOORING_ITEM:
                values = cls.getFlooringChoices()
                result[itemType] = values
            elif itemType == CatalogItemTypes.MOULDING_ITEM:
                values = cls.getMouldingChoices()
                result[itemType] = values
            elif itemType == CatalogItemTypes.WAINSCOTING_ITEM:
                values = cls.getWainscotingChoices()
                result[itemType] = values
            elif itemType == CatalogItemTypes.PET_TRICK_ITEM:
                values = cls.getPetTrickChoices()
                result[itemType] = values
            elif itemType == CatalogItemTypes.RENTAL_ITEM:
                values = cls.getRentalChoices()
                result[itemType] = values
            elif itemType == CatalogItemTypes.ANIMATED_FURNITURE_ITEM:
                values = cls.getAnimatedFurnitureChoices()
                result[itemType] = values
            elif itemType == CatalogItemTypes.NAMETAG_ITEM:
                values = cls.getNametagChoices()
                result[itemType] = values
            elif itemType == CatalogItemTypes.GARDENSTARTER_ITEM:
                values = cls.getGardenStarterChoices()
                result[itemType] = values
            elif itemType == CatalogItemTypes.POLE_ITEM:
                values = cls.getFishingRodChoices()
                result[itemType] = values
            elif itemType == CatalogItemTypes.GARDEN_ITEM:
                values = cls.getGardenItemChoices()
                result[itemType] = values
            elif itemType == CatalogItemTypes.TOON_STATUE_ITEM:
                values = cls.getToonStatueChoices()
                result[itemType] = values
            else:
                values = {"choice1": "Unimplemented One", "choice2": "Unimplemented Two"}
                result[itemType] = values

        cls._awardChoices = result
        return result

    @staticmethod
    def getAwardTypeName(awardType):
        return TTLocalizer.CatalogItemTypeNames[awardType]

    @classmethod
    def getAwardText(cls, awardType, awardId):
        rAwardChoices = cls.getReversedAwardChoices()
        return rAwardChoices[awardType][awardId]
