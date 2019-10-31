from direct.directnotify import DirectNotifyGlobal
from direct.distributed.ClockDelta import globalClockDelta

from toontown.estate import ClosetGlobals
from toontown.estate.DistributedFurnitureItemAI import DistributedFurnitureItemAI
from toontown.toon import ToonDNA


class DistributedClosetAI(DistributedFurnitureItemAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedClosetAI')

    def __init__(self, air, house, furnitureMgr, catalogItem):
        DistributedFurnitureItemAI.__init__(self, air, house, furnitureMgr, catalogItem)
        self.ownerId = self.house.avatarId
        self.customerId = 0
        self.customerDNA = None
        self.gender = ''
        self.topList = []
        self.bottomList = []
        self.removedShirts = []
        self.removedBottoms = []

    def delete(self):
        taskMgr.remove('closet-timeout-%d' % self.customerId)
        self.ignore(self.air.getAvatarExitEvent(self.customerId))
        DistributedFurnitureItemAI.delete(self)

    def setOwnerId(self, ownerId):
        self.ownerId = ownerId

    def d_setOwnerId(self, ownerId):
        self.sendUpdate('setOwnerId', [ownerId])

    def b_setOwnerId(self, ownerId):
        self.setOwnerId(ownerId)
        self.d_setOwnerId(ownerId)

    def getOwnerId(self):
        return self.ownerId

    def enterAvatar(self):
        avId = self.air.getAvatarIdFromSender()
        if self.customerId:
            self.sendUpdateToAvatarId(avId, 'freeAvatar', [])
            return

        av = self.air.doId2do.get(avId)
        if not av:
            return

        self.customerId = avId
        self.customerDNA = av.dna
        owner = self.air.doId2do.get(self.ownerId)
        if not owner:
            self.air.dbInterface.queryObject(self.air.dbId, self.ownerId, self.__handleOwnerQuery,
                                             self.air.dclassesByName['DistributedToonAI'])
            return

        self.gender = owner.dna.gender
        self.topList = owner.getClothesTopsList()
        self.bottomList = owner.getClothesBottomsList()

        # Set the state:
        self.d_setState(ClosetGlobals.OPEN, self.customerId, self.ownerId, self.gender, self.topList, self.bottomList)
        self.acceptOnce(self.air.getAvatarExitEvent(avId), self.__handleUnexpectedExit, extraArgs=[avId])

        # Add a 200 second timeout that'll kick the avatar out:
        taskMgr.doMethodLater(ClosetGlobals.TIMEOUT_TIME, self.__handleClosetTimeout, 'closet-timeout-%d' % avId,
                              extraArgs=[avId])

    def __handleOwnerQuery(self, dclass, fields):
        self.topList = fields['setClothesTopsList'][0]
        self.bottomList = fields['setClothesBottomsList'][0]
        style = ToonDNA.ToonDNA()
        style.makeFromNetString(fields['setDNAString'][0])
        self.gender = style.gender

        # Set the state:
        self.d_setState(ClosetGlobals.OPEN, self.customerId, self.ownerId, self.gender, self.topList, self.bottomList)

        # Add a 200 second timeout that'll kick the avatar out:
        taskMgr.doMethodLater(ClosetGlobals.TIMEOUT_TIME, self.__handleClosetTimeout,
                              'closet-timeout-%d' % self.customerId, extraArgs=[self.customerId])

    def __handleClosetTimeout(self, avId):
        self.d_setMovie(ClosetGlobals.CLOSET_MOVIE_TIMEOUT, avId)
        self.d_setMovie(ClosetGlobals.CLOSET_MOVIE_CLEAR, 0)
        self.d_setState(ClosetGlobals.CLOSED, avId, self.ownerId, self.gender, self.topList, self.bottomList)

    def d_setState(self, mode, avId, ownerId, gender, topList, bottomList):
        self.sendUpdate('setState', [mode, avId, ownerId, gender, topList, bottomList])

    def removeItem(self, dnaString, itemType):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)
        if not av:
            self.air.writeServerEvent('suspicious', avId, 'av not in same shard as closet!')
            return

        if av.getLocation() != self.getLocation():
            self.air.writeServerEvent('suspicious', avId, 'av not in same zone as closet!')
            return

        testDNA = ToonDNA.ToonDNA()
        if not testDNA.isValidNetString(dnaString):
            self.air.writeServerEvent('suspicious', avId, 'DistributedClosetAI.removeItem: invalid dna: %s' % dnaString)
            return

        testDNA.makeFromNetString(dnaString)
        if itemType == ClosetGlobals.SHIRT:
            self.removedShirts.append((testDNA.topTex, testDNA.topTexColor, testDNA.sleeveTex, testDNA.sleeveTexColor))
        elif itemType == ClosetGlobals.SHORTS:
            self.removedBottoms.append((testDNA.botTex, testDNA.botTexColor))

    def setDNA(self, dnaString, finished, whichItems):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)
        if not av:
            self.air.writeServerEvent('suspicious', avId, 'av not in same shard as closet!')
            return

        if av.getLocation() != self.getLocation():
            self.air.writeServerEvent('suspicious', avId, 'av not in same zone as closet!')
            return

        if avId != self.customerId:
            if self.customerId:
                self.air.writeServerEvent('suspicious', avId,
                                          'DistributedNPCTailorAI.setDNA customer is %s' % self.customerId)
                self.notify.warning('customerId: %s, but got setDNA for: %s' % (self.customerId, avId))

            return

        testDNA = ToonDNA.ToonDNA()
        if not testDNA.isValidNetString(dnaString):
            self.air.writeServerEvent('suspicious', avId, 'DistributedClosetAI.setDNA: invalid dna: %s' % dnaString)
            return

        testDNA.makeFromNetString(dnaString)
        if finished == 0:
            if not self.__validChange(testDNA):
                # THAT IS IT NO BODY MODS
                self.air.writeServerEvent('suspicious', avId, 'DistributedClosetAI.setDNA: av tried to switch body dna')
                return

            self.sendUpdate('setCustomerDNA', [avId, dnaString])
            return
        elif finished == 1:
            # Avatar hit the cancel button.
            av.b_setDNAString(self.customerDNA.makeNetString())
            self.customerId = 0
            self.customerDNA = None
            self.gender = ''
            self.__resetItemLists()
            self.d_setMovie(ClosetGlobals.CLOSET_MOVIE_COMPLETE, avId)
            self.d_setMovie(ClosetGlobals.CLOSET_MOVIE_CLEAR, 0)
            self.sendUpdate('setCustomerDNA', [0, ''])
            self.d_setState(ClosetGlobals.CLOSED, 0, self.ownerId, self.gender, self.topList, self.bottomList)
        elif finished == 2:
            # Avatar is done.
            if avId != self.ownerId:
                self.air.writeServerEvent('suspicious', avId, 'av tried to steal clothing!')
                return

            if whichItems & ClosetGlobals.SHIRT:
                if av.replaceItemInClothesTopsList(testDNA.topTex, testDNA.topTexColor, testDNA.sleeveTex,
                                                   testDNA.sleeveTexColor, self.customerDNA.topTex,
                                                   self.customerDNA.topTexColor, self.customerDNA.sleeveTex,
                                                   self.customerDNA.sleeveTexColor):
                    self.customerDNA.topTex = testDNA.topTex
                    self.customerDNA.topTexColor = testDNA.topTexColor
                    self.customerDNA.sleeveTex = testDNA.sleeveTex
                    self.customerDNA.sleeveTexColor = testDNA.sleeveTexColor
                else:
                    self.air.writeServerEvent('suspicious', avId, 'av tried to put on shirt they don\'t own')
                    return

            if whichItems & ClosetGlobals.SHORTS:
                if av.replaceItemInClothesBottomsList(testDNA.botTex, testDNA.botTexColor, self.customerDNA.botTex,
                                                      self.customerDNA.botTexColor):
                    self.customerDNA.botTex = testDNA.botTex
                    self.customerDNA.botTexColor = testDNA.botTexColor
                else:
                    self.air.writeServerEvent('suspicious', avId, 'av tried to put on shorts they don\'t own')
                    return

            for item in self.removedShirts[:]:
                if not av.removeItemInClothesTopsList(*item):
                    self.air.writeServerEvent('suspicious', avId, 'av tried to delete shirt they don\'t own')
                    return

                self.removedShirts.remove(item)

            for item in self.removedBottoms[:]:
                if not av.removeItemInClothesBottomsList(*item):
                    self.air.writeServerEvent('suspicious', avId, 'av tried to delete bottom they don\'t own')
                    return

                self.removedBottoms.remove(item)

            av.b_setClothesTopsList(av.getClothesTopsList())
            av.b_setClothesBottomsList(av.getClothesBottomsList())
            av.b_setDNAString(self.customerDNA.makeNetString())
            self.customerId = 0
            self.customerDNA = None
            self.gender = ''
            self.__resetItemLists()
            self.d_setMovie(ClosetGlobals.CLOSET_MOVIE_COMPLETE, avId)
            self.d_setMovie(ClosetGlobals.CLOSET_MOVIE_CLEAR, 0)
            self.sendUpdate('setCustomerDNA', [0, ''])
            self.d_setState(ClosetGlobals.CLOSED, avId, self.ownerId, self.gender, self.topList, self.bottomList)

        taskMgr.remove('closet-timeout-%d' % avId)
        self.ignore(self.air.getAvatarExitEvent(avId))

    def d_setMovie(self, mode, avId):
        self.sendUpdate('setMovie', [mode, avId, globalClockDelta.getRealNetworkTime()])

    def __resetItemLists(self):
        self.topList = []
        self.bottomList = []
        self.removedShirts = []
        self.removedBottoms = []

    def __handleUnexpectedExit(self, avId):
        if avId != self.customerId:
            self.notify.warning('received unexpected exit for av %s that is not using the closet!' % avId)
            return

        self.customerId = 0
        self.customerDNA = None
        self.gender = ''
        self.__resetItemLists()
        self.d_setMovie(ClosetGlobals.CLOSET_MOVIE_CLEAR, 0)
        self.sendUpdate('setCustomerDNA', [0, ''])
        self.d_setState(ClosetGlobals.CLOSED, 0, self.ownerId, self.gender, self.topList, self.bottomList)

    def __validChange(self, style):
        # sad
        if style.head != self.customerDNA.head:
            return

        if style.torso != self.customerDNA.torso:
            return

        if style.legs != self.customerDNA.legs:
            return

        if style.gender != self.customerDNA.gender:
            return

        if style.armColor != self.customerDNA.armColor:
            return

        if style.gloveColor != self.customerDNA.gloveColor:
            return

        if style.legColor != self.customerDNA.legColor:
            return

        if style.headColor != self.customerDNA.headColor:
            return

        return True
