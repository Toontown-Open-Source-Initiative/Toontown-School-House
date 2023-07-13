from direct.directnotify import DirectNotifyGlobal

from panda3d.core import *

from otp.ai.AIBaseGlobal import *

from toontown.catalog import CatalogItemList
from toontown.catalog import CatalogItem

class PartyAvatarUD:
    notify = DirectNotifyGlobal.directNotify.newCategory("PartyAvatarUD")

    def __init__(self):
        self.onOrder = CatalogItemList.CatalogItemList(store=CatalogItem.Customization | CatalogItem.DeliveryDate)
        self.onGiftOrder = CatalogItemList.CatalogItemList(store=CatalogItem.Customization | CatalogItem.DeliveryDate)
        self.mailboxContents = CatalogItemList.CatalogItemList(store=CatalogItem.Customization)
        self.awardMailboxContents = CatalogItemList.CatalogItemList(store=CatalogItem.Customization)
        self.onAwardOrder = CatalogItemList.CatalogItemList(store=CatalogItem.Customization | CatalogItem.DeliveryDate)
    
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

    @staticmethod
    def createFromFields(fields):
        avatar = PartyAvatarUD()

        for key, value in fields.iteritems():
            getattr(avatar, key)(value)

        return avatar
