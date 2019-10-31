import time

from toontown.catalog import CatalogItem
from toontown.catalog import CatalogItemList
from toontown.toon import ToonDNA


class GiftAvatarAI:

    def __init__(self):
        self.style = None
        self.mailboxContents = None
        self.awardMailboxContents = None
        self.onGiftOrder = None
        self.onOrder = None
        self.onAwardOrder = None
        self.hat = None
        self.glasses = None
        self.backpack = None
        self.shoes = None
        self.hatList = None
        self.glassesList = None
        self.backpackList = None
        self.shoesList = None
        self.customMessages = None
        self.clothesTopsList = None
        self.clothesBottomsList = None
        self.emoteAccess = None
        self.petTrickPhrases = None

    def getStyle(self):
        return self.style

    def getHat(self):
        return self.hat

    def getGlasses(self):
        return self.glasses

    def getBackpack(self):
        return self.backpack

    def getShoes(self):
        return self.shoes

    def getGiftScheduleBlob(self):
        return self.onGiftOrder.getBlob(store=CatalogItem.Customization | CatalogItem.DeliveryDate)

    def setDNAString(self, dnaString):
        self.style = ToonDNA.ToonDNA()
        self.style.makeFromNetString(dnaString.decode('base64'))

    def setMailboxContents(self, mailboxContents):
        self.mailboxContents = CatalogItemList.CatalogItemList(mailboxContents.decode('base64'),
                                                               store=CatalogItem.Customization)

    def setAwardMailboxContents(self, awardMailboxContents):
        self.awardMailboxContents = CatalogItemList.CatalogItemList(awardMailboxContents.decode('base64'),
                                                                    store=CatalogItem.Customization)

    def setGiftSchedule(self, onOrder):
        self.onGiftOrder = CatalogItemList.CatalogItemList(onOrder.decode('base64'),
                                                           store=CatalogItem.Customization | CatalogItem.DeliveryDate)

    def setDeliverySchedule(self, onOrder):
        self.onOrder = CatalogItemList.CatalogItemList(onOrder.decode('base64'),
                                                       store=CatalogItem.Customization | CatalogItem.DeliveryDate)

    def setAwardSchedule(self, onOrder):
        self.onAwardOrder = CatalogItemList.CatalogItemList(onOrder.decode('base64'),
                                                            store=CatalogItem.Customization | CatalogItem.DeliveryDate)

    def setHat(self, hat):
        self.hat = hat

    def setGlasses(self, glasses):
        self.glasses = glasses

    def setBackpack(self, backpack):
        self.backpack = backpack

    def setShoes(self, shoes):
        self.shoes = shoes

    def setHatList(self, hatList):
        self.hatList = hatList[0]

    def setGlassesList(self, glassesList):
        self.glassesList = glassesList[0]

    def setBackpackList(self, backpackList):
        self.backpackList = backpackList[0]

    def setShoesList(self, shoesList):
        self.shoesList = shoesList[0]

    def setCustomMessages(self, customMessages):
        self.customMessages = customMessages[0]

    def setClothesTopsList(self, clothesList):
        self.clothesTopsList = clothesList[0]

    def setClothesBottomsList(self, clothesList):
        self.clothesBottomsList = clothesList[0]

    def setEmoteAccess(self, emoteAccess):
        self.emoteAccess = emoteAccess[0]

    def setPetTrickPhrases(self, tricks):
        self.petTrickPhrases = tricks[0]

    def addToGiftSchedule(self, avId, targetId, item, minutes=0):
        if config.GetBool('want-instant-delivery', False):
            minutes = 0

        item.giftTag = avId
        item.deliveryDate = int(time.time() / 60. + minutes + .5)
        self.onGiftOrder.append(item)
        simbase.air.send(
            simbase.air.dclassesByName['DistributedToonAI'].aiFormatUpdate('setGiftSchedule', targetId, targetId,
                                                                           simbase.air.ourChannel,
                                                                           [self.getGiftScheduleBlob()]))

    @staticmethod
    def createFromFields(fields):
        avatar = GiftAvatarAI()
        for key, value in fields.iteritems():
            getattr(avatar, key)(value)

        return avatar
