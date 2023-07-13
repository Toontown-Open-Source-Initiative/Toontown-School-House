from direct.directnotify import DirectNotifyGlobal

from panda3d.core import *

from otp.ai.AIBaseGlobal import *
from otp.otpbase import OTPGlobals

from toontown.catalog import CatalogItemList
from toontown.catalog import CatalogItem
from toontown.catalog import CatalogItemTypes
from toontown.catalog import CatalogClothingItem
from toontown.catalog import CatalogAccessoryItemGlobals
from toontown.estate import GardenGlobals
from toontown.toonbase import ToontownGlobals
from toontown.toon import ToonDNA


class AwardAvatarUD:
    notify = DirectNotifyGlobal.directNotify.newCategory("AwardAvatarUD")

    def __init__(self):
        self.dna = ToonDNA.ToonDNA()

        self.onOrder = CatalogItemList.CatalogItemList(store=CatalogItem.Customization | CatalogItem.DeliveryDate)
        self.onGiftOrder = CatalogItemList.CatalogItemList(store=CatalogItem.Customization | CatalogItem.DeliveryDate)
        self.mailboxContents = CatalogItemList.CatalogItemList(store=CatalogItem.Customization)
        self.awardMailboxContents = CatalogItemList.CatalogItemList(store=CatalogItem.Customization)
        self.onAwardOrder = CatalogItemList.CatalogItemList(store=CatalogItem.Customization | CatalogItem.DeliveryDate)

        self.hatList = []
        self.glassesList = []
        self.backpackList = []
        self.shoesList = []
        self.hat = (0, 0, 0)
        self.glasses = (0, 0, 0)
        self.backpack = (0, 0, 0)
        self.shoes = (0, 0, 0)

        self.customMessages = []
        self.clothesTopsList = []
        self.clothesBottomsList = []
        self.emoteAccess = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.petTrickPhrases = []

        self.nametagStyle = 0
        self.fishingRod = 0

        self.gardenStarted = False
        self.shovel = 0
        self.shovelSkill = 0

    def setDeliverySchedule(self, onOrder):
        self.notify.debug("Setting onOrder to %s." % (onOrder.decode('base64')))
        self.onOrder = CatalogItemList.CatalogItemList(onOrder.decode('base64'), store=CatalogItem.Customization | CatalogItem.DeliveryDate)
        self.notify.debug("onOrder is %s." % (self.mailboxContents))

    def getDeliverySchedule(self):
        return self.onOrder.getBlob(store=CatalogItem.Customization | CatalogItem.DeliveryDate)

    def setGiftSchedule(self, onGiftOrder):
        self.notify.debug("Setting onGiftOrder to %s." % (onGiftOrder.decode('base64')))
        self.onGiftOrder = CatalogItemList.CatalogItemList(onGiftOrder.decode('base64'), store=CatalogItem.Customization | CatalogItem.DeliveryDate)
        self.notify.debug("onGiftOrder is %s." % (self.mailboxContents))

    def getGiftSchedule(self):
        return self.onGiftOrder.getBlob(store=CatalogItem.Customization | CatalogItem.DeliveryDate)

    def setMailboxContents(self, mailboxContents):
        self.notify.debug("Setting mailboxContents to %s." % (mailboxContents.decode('base64')))
        self.mailboxContents = CatalogItemList.CatalogItemList(mailboxContents.decode('base64'), store=CatalogItem.Customization)
        self.notify.debug("mailboxContents is %s." % (self.mailboxContents))

    def getMailboxContents(self):
        return self.mailboxContents.getBlob(store=CatalogItem.Customization)

    def setAwardMailboxContents(self, awardMailboxContents):
        self.notify.debug("Setting awardMailboxContents to %s." % (awardMailboxContents.decode('base64')))
        self.awardMailboxContents = CatalogItemList.CatalogItemList(awardMailboxContents.decode('base64'), store=CatalogItem.Customization)
        self.notify.debug("awardMailboxContents is %s." % (self.awardMailboxContents))

    def getAwardMailboxContents(self):
        return self.awardMailboxContents.getBlob(store=CatalogItem.Customization)

    def setAwardSchedule(self, onAwardOrder):
        self.notify.debug("Setting onAwardOrder to %s." % (onAwardOrder.decode('base64')))
        self.onAwardOrder = CatalogItemList.CatalogItemList(onAwardOrder.decode('base64'), store=CatalogItem.Customization | CatalogItem.DeliveryDate)
        self.notify.debug("onAwardOrder is %s." % (self.onAwardOrder))

    def getAwardSchedule(self):
        return self.onAwardOrder.getBlob(store=CatalogItem.Customization | CatalogItem.DeliveryDate)

    def setDNAString(self, string):
        self.dna.makeFromNetString(string.decode('base64'))

    def getDNAString(self):
        """
        Function:    retrieve the dna information from this suit, called
                     whenever a client needs to create this suit
        Returns:     netString representation of this suit's dna
        """
        return self.dna.makeNetString()

    def getStyle(self):
        return self.dna

    def setClothesTopsList(self, clothesTopsList):
        self.notify.debug("Setting clothesTopsList to %s." % (clothesTopsList[0]))
        self.clothesTopsList = clothesTopsList[0]
        self.notify.debug("clothesTopsList is %s." % (self.clothesTopsList))

    def getClothesTopsList(self):
        return self.clothesTopsList

    def setClothesBottomsList(self, clothesBottomsList):
        self.notify.debug("Setting clothesBottomsList to %s." % (clothesBottomsList[0]))
        self.clothesBottomsList = clothesBottomsList[0]
        self.notify.debug("clothesBottomsList is %s." % (self.clothesBottomsList))

    def getClothesBottomsList(self):
        return self.clothesBottomsList

    def setEmoteAccess(self, emoteAccess):
        self.notify.debug("Setting emoteAccess to %s." % (emoteAccess[0]))
        self.emoteAccess = emoteAccess[0]
        self.notify.debug("emoteAccess is %s." % (self.emoteAccess))

    def getEmoteAccess(self):
        return self.emoteAccess

    def setCustomMessages(self, customMessages):
        self.notify.debug("Setting customMessages to %s." % (customMessages[0]))
        self.customMessages = customMessages[0]
        self.notify.debug("customMessages is %s." % (self.customMessages))

    def getCustomMessages(self):
        return self.customMessages

    def setPetTrickPhrases(self, petTrickPhrases):
        self.notify.debug("Setting petTrickPhrases to %s." % (petTrickPhrases[0]))
        self.petTrickPhrases = petTrickPhrases[0]
        self.notify.debug("petTrickPhrases is %s." % (self.petTrickPhrases))

    def getPetTrickPhrases(self):
        return self.petTrickPhrases

    # Accessories List
    def setHatList(self, hatList):
        self.notify.debug("Setting hatList to %s." % (hatList[0]))
        self.hatList = hatList[0]
        self.notify.debug("hatList is %s." % (self.hatList))

    def getHatList(self):
        return self.hatList

    def setGlassesList(self, glassesList):
        self.notify.debug("Setting glassesList to %s." % (glassesList[0]))
        self.glassesList = glassesList[0]
        self.notify.debug("glassesList is %s." % (self.glassesList))

    def getGlassesList(self):
        return self.glassesList

    def setBackpackList(self, backpackList):
        self.notify.debug("Setting backpackList to %s." % (backpackList[0]))
        self.backpackList = backpackList[0]
        self.notify.debug("backpackList is %s." % (self.backpackList))

    def getBackpackList(self):
        return self.backpackList

    def setShoesList(self, shoesList):
        self.notify.debug("Setting shoesList to %s." % (shoesList[0]))
        self.shoesList = shoesList[0]
        self.notify.debug("shoesList is %s." % (self.shoesList))

    def getShoesList(self):
        return self.shoesList

    # Accessories
    def setHat(self, hat):
        self.notify.debug("Setting hat to %s." % (str(hat)))
        self.hat = hat
        self.notify.debug("hat is %s." % (str(self.hat)))

    def getHat(self):
        return self.hat

    def setGlasses(self, glasses):
        self.notify.debug("Setting glasses to %s." % (str(glasses)))
        self.glasses = glasses
        self.notify.debug("glasses is %s." % (str(self.glasses)))

    def getGlasses(self):
        return self.glasses

    def setBackpack(self, backpack):
        self.notify.debug("Setting backpack to %s." % (str(backpack)))
        self.backpack = backpack
        self.notify.debug("backpack is %s." % (str(self.backpack)))

    def getBackpack(self):
        return self.backpack

    def setShoes(self, shoes):
        self.notify.debug("Setting shoes to %s." % (str(shoes)))
        self.shoes = shoes
        self.notify.debug("shoes is %s." % (str(self.shoes)))

    def getShoes(self):
        return self.shoes

    def setFishingRod(self, rodId):
        self.notify.debug("Setting fishingRod to %s." % (rodId[0]))
        self.fishingRod = rodId[0]
        self.notify.debug("fishingRod is %s." % (str(self.fishingRod)))

    def getFishingRod(self):
        return self.fishingRod

    def setNametagStyle(self, nametagStyle):
        self.notify.debug("Setting nametagStyle to %s." % (nametagStyle[0]))
        self.nametagStyle = nametagStyle[0]
        self.notify.debug("nametagStyle is %s." % (str(self.nametagStyle)))

    def getNametagStyle(self):
        return self.nametagStyle

    def setGardenStarted(self, gardenStarted):
        self.notify.debug("Setting gardenStarted to %s." % (gardenStarted[0]))
        self.gardenStarted = gardenStarted[0]
        self.notify.debug("gardenStarted is %s." % (str(self.gardenStarted)))

    def getGardenStarted(self):
        return self.gardenStarted

    def setShovel(self, shovelId):
        self.notify.debug("Setting shovel to %s." % (shovelId[0]))
        self.shovel = shovelId[0]
        self.notify.debug("shovel is %s." % (str(self.shovel)))

    def getShovel(self):
        return self.shovel

    def setShovelSkill(self, skillLevel):
        self.notify.debug("Setting shovelSkill to %s." % (skillLevel[0]))
        self.shovelSkill = skillLevel[0]
        self.notify.debug("shovelSkill is %s." % (str(self.shovelSkill)))

    def getShovelSkill(self):
        return self.shovelSkill

    def checkForItemInCloset(self, clothingItem):
        """Returns None if the clothing item is not in the closet."""
        result = None
        clothingTypeInfo = CatalogClothingItem.ClothingTypes[clothingItem.clothingType]
        styleStr = clothingTypeInfo[1]
        if clothingItem.isShirt():
            # ok check the tops list
            # we have the style str, check TOON DNA to get shirt and sleeve indices
            shirtStyleInfo = ToonDNA.ShirtStyles[styleStr]
            topTex = shirtStyleInfo[0]
            sleeveTex = shirtStyleInfo[1]
            topTexColor = shirtStyleInfo[2][clothingItem.colorIndex][0]
            sleeveTexColor = shirtStyleInfo[2][clothingItem.colorIndex][1]
            # See if this top is already there
            for i in range(0, len(self.clothesTopsList), 4):
                if (self.clothesTopsList[i] == topTex and
                    self.clothesTopsList[i+1] == topTexColor and
                    self.clothesTopsList[i+2] == sleeveTex and
                        self.clothesTopsList[i+3] == sleeveTexColor):
                    result = ToontownGlobals.P_ItemInCloset
                    break
        else:
            bottomStyleInfo = ToonDNA.BottomStyles[styleStr]
            botTex = bottomStyleInfo[0]
            botTexColor = bottomStyleInfo[1][clothingItem.colorIndex]
            # See if this bottom is already there
            for i in range(0, len(self.clothesBottomsList), 2):
                if (self.clothesBottomsList[i] == botTex and
                        self.clothesBottomsList[i+1] == botTexColor):
                    result = ToontownGlobals.P_ItemInCloset
                    break
        return result

    def checkForItemAlreadyWorn(self, clothingItem):
        """Returns None if the toon is not wearing the clothing item."""
        result = None
        clothingTypeInfo = CatalogClothingItem.ClothingTypes[clothingItem.clothingType]
        styleStr = clothingTypeInfo[1]
        if clothingItem.isShirt():
            # ok check the tops list
            # we have the style str, check TOON DNA to get shirt and sleeve indices
            shirtStyleInfo = ToonDNA.ShirtStyles[styleStr]
            topTex = shirtStyleInfo[0]
            sleeveTex = shirtStyleInfo[1]
            topTexColor = shirtStyleInfo[2][clothingItem.colorIndex][0]
            sleeveTexColor = shirtStyleInfo[2][clothingItem.colorIndex][1]
            # See if this top is already being worn
            if self.dna.topTex == topTex and \
               self.dna.sleeveTex == sleeveTex and \
               self.dna.topTexColor == topTexColor and \
               self.dna.sleeveTexColor == sleeveTexColor:
                result = ToontownGlobals.P_ItemAlreadyWorn
        else:
            bottomStyleInfo = ToonDNA.BottomStyles[styleStr]
            bottomTex = bottomStyleInfo[0]
            bottomTexColor = bottomStyleInfo[1][clothingItem.colorIndex]
            # See if this bottom is already being worn
            if self.dna.botTex == bottomTex and \
                    self.dna.botTexColor == bottomTexColor:
                result = ToontownGlobals.P_ItemAlreadyWorn
        return result

    def checkForAccessoryItemInTrunk(self, accessoryItem):
        """Returns None if the accessory item is not in the trunk."""
        result = None
        accessoryInfoType = CatalogAccessoryItemGlobals.AccessoryTypes[accessoryItem.accessoryType]
        styleStr = accessoryInfoType[1]
        if accessoryItem.isHat():
            hatStyleInfo = ToonDNA.HatStyles[styleStr]
            itemIdx = hatStyleInfo[0]
            textureIdx = hatStyleInfo[1]
            colorIdx = hatStyleInfo[2]
            for i in range(0, len(self.hatList), 3):
                if(self.hatList[i] == itemIdx and self.hatList[i+1] == textureIdx and self.hatList[i+2] == colorIdx):
                    result = ToontownGlobals.P_ItemInTrunk
                    break
        elif accessoryItem.areGlasses():
            glassesStyleInfo = ToonDNA.GlassesStyles[styleStr]
            itemIdx = glassesStyleInfo[0]
            textureIdx = glassesStyleInfo[1]
            colorIdx = glassesStyleInfo[2]
            for i in range(0, len(self.glassesList), 3):
                if(self.glassesList[i] == itemIdx and self.glassesList[i+1] == textureIdx and self.glassesList[i+2] == colorIdx):
                    result = ToontownGlobals.P_ItemInTrunk
                    break
        elif accessoryItem.isBackpack():
            backpackStyleInfo = ToonDNA.BackpackStyles[styleStr]
            itemIdx = backpackStyleInfo[0]
            textureIdx = backpackStyleInfo[1]
            colorIdx = backpackStyleInfo[2]
            for i in range(0, len(self.backpackList), 3):
                if(self.backpackList[i] == itemIdx and self.backpackList[i+1] == textureIdx and self.backpackList[i+2] == colorIdx):
                    result = ToontownGlobals.P_ItemInTrunk
                    break
        else:
            shoesStyleInfo = ToonDNA.ShoesStyles[styleStr]
            itemIdx = shoesStyleInfo[0]
            textureIdx = shoesStyleInfo[1]
            colorIdx = shoesStyleInfo[2]
            for i in range(0, len(self.shoesList), 3):
                if(self.shoesList[i] == itemIdx and self.shoesList[i+1] == textureIdx and self.shoesList[i+2] == colorIdx):
                    result = ToontownGlobals.P_ItemInTrunk
                    break
        return result

    def checkForAccessoryItemAlreadyWorn(self, accessoryItem):
        """Returns None if the toon is not wearing the accessory item."""
        result = None
        accessoryInfoType = CatalogAccessoryItemGlobals.AccessoryTypes[accessoryItem.accessoryType]
        styleStr = accessoryInfoType[1]
        if accessoryItem.isHat():
            hatStyleInfo = ToonDNA.HatStyles[styleStr]
            hat = self.getHat()
            itemIdx = hatStyleInfo[0]
            textureIdx = hatStyleInfo[1]
            colorIdx = hatStyleInfo[2]
            if hat[0] == itemIdx and \
               hat[1] == textureIdx and \
               hat[2] == colorIdx:
                result = ToontownGlobals.P_ItemAlreadyWorn
        elif accessoryItem.areGlasses():
            glassesStyleInfo = ToonDNA.GlassesStyles[styleStr]
            glasses = self.getGlasses()
            itemIdx = glassesStyleInfo[0]
            textureIdx = glassesStyleInfo[1]
            colorIdx = glassesStyleInfo[2]
            if glasses[0] == itemIdx and \
               glasses[1] == textureIdx and \
               glasses[2] == colorIdx:
                result = ToontownGlobals.P_ItemAlreadyWorn
        elif accessoryItem.isBackpack():
            backpackStyleInfo = ToonDNA.BackpackStyles[styleStr]
            backpack = self.getBackpack()
            itemIdx = backpackStyleInfo[0]
            textureIdx = backpackStyleInfo[1]
            colorIdx = backpackStyleInfo[2]
            if backpack[0] == itemIdx and \
               backpack[1] == textureIdx and \
               backpack[2] == colorIdx:
                result = ToontownGlobals.P_ItemAlreadyWorn
        else:
            shoesStyleInfo = ToonDNA.ShoesStyles[styleStr]
            shoes = self.getShoes()
            itemIdx = shoesStyleInfo[0]
            textureIdx = shoesStyleInfo[1]
            colorIdx = shoesStyleInfo[2]
            if shoes[0] == itemIdx and \
               shoes[1] == textureIdx and \
               shoes[2] == colorIdx:
                result = ToontownGlobals.P_ItemAlreadyWorn
        return result

    def checkGardenSkillLevel(self, catalogItem):
        recipeKey = GardenGlobals.getRecipeKeyUsingSpecial(catalogItem.gardenIndex)
        recipe = GardenGlobals.Recipes[recipeKey]
        numBeansRequired = len(recipe['beans'])
        canPlant = GardenGlobals.getShovelPower(self.getShovel(), self.getShovelSkill())
        result = False

        if canPlant < numBeansRequired:
            result = True

        if not result and catalogItem.gardenIndex in GardenGlobals.Specials and 'minSkill' in GardenGlobals.Specials[catalogItem.gardenIndex]:
            minSkill = GardenGlobals.Specials[catalogItem.gardenIndex]['minSkill']
            if self.getShovelSkill() < minSkill:
                result = True
            else:
                result = False

        return result

    def checkForDuplicateItem(self, catalogItem):
        """Return None if the catalog item is not in his mailbox, or on him somehow"""
        result = None
        # go through his mailbox
        if catalogItem in self.mailboxContents:
            result = ToontownGlobals.P_ItemInMailbox
        elif catalogItem in self.onOrder:
            result = ToontownGlobals.P_ItemOnOrder
        elif catalogItem in self.onGiftOrder:
            result = ToontownGlobals.P_ItemOnGiftOrder
        elif catalogItem in self.awardMailboxContents:
            result = ToontownGlobals.P_ItemInAwardMailbox
        elif catalogItem in self.onAwardOrder:
            result = ToontownGlobals.P_ItemOnAwardOrder

        # now based on the item type do some other checking
        if not result:
            if catalogItem.getTypeCode() == CatalogItemTypes.CLOTHING_ITEM:
                result = self.checkForItemInCloset(catalogItem)
                if not result:
                    result = self.checkForItemAlreadyWorn(catalogItem)
            elif catalogItem.getTypeCode() == CatalogItemTypes.ACCESSORY_ITEM:
                result = self.checkForAccessoryItemInTrunk(catalogItem)
                if not result:
                    result = self.checkForAccessoryItemAlreadyWorn(catalogItem)
            elif catalogItem.getTypeCode() == CatalogItemTypes.CHAT_ITEM:
                speedChatIndex = catalogItem.customIndex
                if speedChatIndex in self.customMessages:
                    result = ToontownGlobals.P_ItemInMyPhrases
            elif catalogItem.getTypeCode() == CatalogItemTypes.PET_TRICK_ITEM:
                trickId = catalogItem.trickId
                if trickId in self.petTrickPhrases:
                    result = ToontownGlobals.P_ItemInPetTricks
            elif catalogItem.getTypeCode() == CatalogItemTypes.NAMETAG_ITEM:
                nametagStyle = catalogItem.nametagStyle
                if nametagStyle == self.nametagStyle:
                    result = ToontownGlobals.P_ItemAlreadyWorn
            elif catalogItem.getTypeCode() == CatalogItemTypes.GARDENSTARTER_ITEM:
                if self.getGardenStarted():
                    result = ToontownGlobals.P_ItemAlreadyUsed
            elif catalogItem.getTypeCode() == CatalogItemTypes.POLE_ITEM:
                rodId = catalogItem.rodId
                if rodId < self.getFishingRod():
                    result = ToontownGlobals.P_FishingRodAlreadyOwned
            elif catalogItem.getTypeCode() == CatalogItemTypes.GARDEN_ITEM:
                if not self.getGardenStarted():
                    result = ToontownGlobals.P_NoGardenStarted
                else:
                    if self.checkGardenSkillLevel(catalogItem):
                        result = ToontownGlobals.P_GardenSkillTooLow
            elif catalogItem.getTypeCode() == CatalogItemTypes.TOON_STATUE_ITEM:
                if not self.getGardenStarted():
                    result = ToontownGlobals.P_NoGardenStarted
                else:
                    if self.checkGardenSkillLevel(catalogItem):
                        result = ToontownGlobals.P_GardenSkillTooLow
        return result

    @staticmethod
    def createFromFields(fields):
        avatar = AwardAvatarUD()

        for key, value in fields.iteritems():
            getattr(avatar, key)(value)

        return avatar
