from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedSmoothNodeAI import DistributedSmoothNodeAI

from toontown.catalog import CatalogItem
from toontown.estate import HouseGlobals


class DistributedFurnitureItemAI(DistributedSmoothNodeAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedFurnitureItemAI')

    def __init__(self, air, house, furnitureMgr, catalogItem):
        DistributedSmoothNodeAI.__init__(self, air)
        self.house = house
        self.furnitureMgr = furnitureMgr
        self.catalogItem = catalogItem
        self.mode = 0
        self.avId = 0

    def announceGenerate(self):
        DistributedSmoothNodeAI.announceGenerate(self)
        self.b_setPosHpr(*self.catalogItem.posHpr)

    def getItem(self):
        return [self.furnitureMgr.doId, self.catalogItem.getBlob(store=CatalogItem.Customization)]

    def requestPosHpr(self, final, x, y, z, h, p, r, t):
        senderId = self.air.getAvatarIdFromSender()
        posHpr = (x, y, z, h, p, r)
        if senderId != self.house.avatarId:
            # Hey! What are you doing!?
            self.notify.warning('%d tried to move furniture of house owned by %d!' % (senderId, self.house.ownerId))
            return

        if not final and self.mode != HouseGlobals.FURNITURE_MODE_START:
            self.b_setMode(HouseGlobals.FURNITURE_MODE_START, senderId)
        elif final and self.mode == HouseGlobals.FURNITURE_MODE_START:
            self.b_setMode(HouseGlobals.FURNITURE_MODE_STOP, senderId)
            self.b_setMode(HouseGlobals.FURNITURE_MODE_OFF, senderId)
            self.b_setPosHpr(*posHpr)

        self.catalogItem.posHpr = posHpr
        self.sendUpdate('setSmPosHpr', [x, y, z, h, p, r, t])

    def setMode(self, mode, avId):
        self.mode = mode
        self.avId = avId

    def d_setMode(self, mode, avId):
        self.sendUpdate('setMode', [mode, avId])

    def b_setMode(self, mode, avId):
        self.setMode(mode, avId)
        self.d_setMode(mode, avId)

    def getMode(self):
        return self.mode, self.avId
