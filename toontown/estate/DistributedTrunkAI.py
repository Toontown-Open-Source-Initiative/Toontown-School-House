from direct.directnotify import DirectNotifyGlobal

from toontown.estate import ClosetGlobals
from toontown.estate.DistributedClosetAI import DistributedClosetAI
from toontown.toon import ToonDNA


class DistributedTrunkAI(DistributedClosetAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedTrunkAI')

    def __init__(self, air, house, furnitureMgr, catalogItem):
        DistributedClosetAI.__init__(self, air, house, furnitureMgr, catalogItem)
        self.hatList = []
        self.glassesList = []
        self.backpackList = []
        self.shoesList = []
        self.removedItems = []

    def enterAvatar(self):
        avId = self.air.getAvatarIdFromSender()
        if self.customerId:
            self.sendUpdateToAvatarId(avId, 'freeAvatar', [])
            return

        av = self.air.doId2do.get(avId)
        if not av:
            return

        self.customerId = avId
        self.customerDNA = (av.getHat(), av.getGlasses(), av.getBackpack(), av.getShoes())
        owner = self.air.doId2do.get(self.ownerId)
        if not owner:
            self.air.dbInterface.queryObject(self.air.dbId, self.ownerId, self.__handleOwnerQuery,
                                             self.air.dclassesByName['DistributedToonAI'])
            return

        self.hatList = owner.getHatList()
        self.glassesList = owner.getGlassesList()
        self.backpackList = owner.getBackpackList()
        self.shoesList = owner.getShoesList()
        self.gender = owner.dna.gender

        # Set the state and movie:
        self.d_setState(ClosetGlobals.OPEN, avId, self.ownerId, self.gender, self.hatList, self.glassesList,
                        self.backpackList, self.shoesList)
        self.acceptOnce(self.air.getAvatarExitEvent(avId), self.__handleUnexpectedExit, extraArgs=[avId])

        # Add a 200 second timeout that'll kick the avatar out:
        taskMgr.doMethodLater(ClosetGlobals.TIMEOUT_TIME, self.__handleClosetTimeout, 'closet-timeout-%d' % avId,
                              extraArgs=[avId])

    def __handleOwnerQuery(self, dclass, fields):
        # Set accessory lists from db fields:
        self.hatList = fields['setHatList'][0]
        self.glassesList = fields['setGlassesList'][0]
        self.backpackList = fields['setBackpackList'][0]
        self.shoesList = fields['setShoesList'][0]
        style = ToonDNA.ToonDNA()
        style.makeFromNetString(fields['setDNAString'][0])
        self.gender = style.gender

        # Set the state and movie:
        self.d_setMovie(ClosetGlobals.CLOSET_MOVIE_CLEAR, self.customerId)
        self.d_setState(ClosetGlobals.OPEN, self.customerId, self.ownerId, self.gender, self.hatList, self.glassesList,
                        self.backpackList, self.shoesList)

        # Add a 200 second timeout that'll kick the avatar out:
        taskMgr.doMethodLater(ClosetGlobals.TIMEOUT_TIME, self.__handleClosetTimeout,
                              'closet-timeout-%d' % self.customerId, extraArgs=[self.customerId])

    def __handleClosetTimeout(self, avId):
        self.d_setMovie(ClosetGlobals.CLOSET_MOVIE_TIMEOUT, avId)
        self.d_setMovie(ClosetGlobals.CLOSET_MOVIE_CLEAR, avId)
        self.d_setState(ClosetGlobals.CLOSED, avId, self.ownerId, self.gender, self.hatList, self.glassesList,
                        self.backpackList, self.shoesList)

    def d_setState(self, mode, avId, ownerId, gender, hatList, glassesList, backpackList, shoesList):
        self.sendUpdate('setState', [mode, avId, ownerId, gender, hatList, glassesList, backpackList, shoesList])

    def removeItem(self, idx, texture, color, which):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)
        if not av:
            self.air.writeServerEvent('suspicious', avId, 'av not in same shard as trunk!')
            return

        if av.getLocation() != self.getLocation():
            self.air.writeServerEvent('suspicious', avId, 'av not in same zone as trunk!')
            return

        if avId != self.ownerId:
            self.air.writeServerEvent('suspicious', avId, 'av tried to delete someone else\'s accessory')
            return

        self.removedItems.append((which, idx, texture, color))

    def setDNA(self, hatIdx, hatTexture, hatColor, glassesIdx, glassesTexture, glassesColor, backpackIdx,
               backpackTexture, backpackColor, shoesIdx, shoesTexture, shoesColor, finished, which):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)
        if not av:
            self.air.writeServerEvent('suspicious', avId, 'av not in same shard as trunk!')
            return

        if av.getLocation() != self.getLocation():
            self.air.writeServerEvent('suspicious', avId, 'av not in same zone as trunk!')
            return

        if avId != self.customerId:
            if self.customerId:
                self.air.writeServerEvent('suspicious', avId,
                                          'DistributedNPCTailorAI.setDNA customer is %s' % self.customerId)
                self.notify.warning('customerId: %s, but got setDNA for: %s' % (self.customerId, avId))

            return

        hat = (hatIdx, hatTexture, hatColor)
        glasses = (glassesIdx, glassesTexture, glassesColor)
        backpack = (backpackIdx, backpackTexture, backpackColor)
        shoes = (shoesIdx, shoesTexture, shoesColor)
        accessories = (hat, glasses, backpack, shoes)
        if avId != self.customerId:
            if self.customerId:
                self.air.writeServerEvent('suspicious', avId,
                                          'DistributedNPCTailorAI.setDNA customer is %s' % self.customerId)
                self.notify.warning('customerId: %s, but got setDNA for: %s' % (self.customerId, avId))

            return

        types = (ToonDNA.HAT, ToonDNA.GLASSES, ToonDNA.BACKPACK, ToonDNA.SHOES)
        for i, accessory in enumerate(accessories):
            if not av.checkAccessorySanity(types[i], *accessory):
                return

        if finished == 0:
            self.sendUpdate('setCustomerDNA',
                            [avId, hatIdx, hatTexture, hatColor, glassesIdx, glassesTexture, glassesColor, backpackIdx,
                             backpackTexture, backpackColor, shoesIdx, shoesTexture, shoesColor, which])
            return
        elif finished == 1:
            # Avatar hit the cancel button.
            av.b_setHat(*self.customerDNA[0])
            av.b_setGlasses(*self.customerDNA[1])
            av.b_setBackpack(*self.customerDNA[2])
            av.b_setShoes(*self.customerDNA[3])
            self.customerId = 0
            self.customerDNA = None
            self.gender = ''
            self.__resetItemLists()
            self.d_setMovie(ClosetGlobals.CLOSET_MOVIE_COMPLETE, avId)
            self.d_setMovie(ClosetGlobals.CLOSET_MOVIE_CLEAR, 0)
            self.sendUpdate('setCustomerDNA', [0 for _ in xrange(14)])
            self.d_setState(ClosetGlobals.CLOSED, 0, self.ownerId, self.gender, self.hatList, self.glassesList,
                            self.backpackList, self.shoesList)
        elif finished == 2:
            # Avatar is done.
            if avId != self.ownerId:
                self.air.writeServerEvent('suspicious', avId, 'av tried to steal accessories!')
                return

            oldNew = tuple([accessories[i] + self.customerDNA[i] for i in xrange(len(self.customerDNA))])
            if which & ToonDNA.HAT:
                if av.replaceItemInAccessoriesList(ToonDNA.HAT, *oldNew[0]):
                    av.b_setHat(*hat)

            if which & ToonDNA.GLASSES:
                if av.replaceItemInAccessoriesList(ToonDNA.GLASSES, *oldNew[1]):
                    av.b_setGlasses(*glasses)

            if which & ToonDNA.BACKPACK:
                if av.replaceItemInAccessoriesList(ToonDNA.BACKPACK, *oldNew[2]):
                    av.b_setBackpack(*backpack)

            if which & ToonDNA.SHOES:
                if av.replaceItemInAccessoriesList(ToonDNA.SHOES, *oldNew[3]):
                    av.b_setShoes(*shoes)

            for item in self.removedItems[:]:
                self.removedItems.remove(item)
                if not av.removeItemInAccessoriesList(*item):
                    self.air.writeServerEvent('suspicious', avId, 'av tried to delete accessory they don\'t own!')

            av.b_setHatList(av.getHatList())
            av.b_setGlassesList(av.getGlassesList())
            av.b_setBackpackList(av.getBackpackList())
            av.b_setShoesList(av.getShoesList())
            self.customerId = 0
            self.customerDNA = None
            self.gender = ''
            self.__resetItemLists()
            self.d_setMovie(ClosetGlobals.CLOSET_MOVIE_COMPLETE, avId)
            self.d_setMovie(ClosetGlobals.CLOSET_MOVIE_CLEAR, 0)
            self.sendUpdate('setCustomerDNA', [0 for _ in xrange(14)])
            self.d_setState(ClosetGlobals.CLOSED, 0, self.ownerId, self.gender, self.hatList, self.glassesList,
                            self.backpackList, self.shoesList)

        taskMgr.remove('closet-timeout-%d' % avId)
        self.ignore(self.air.getAvatarExitEvent(avId))

    def __resetItemLists(self):
        self.hatList = []
        self.glassesList = []
        self.backpackList = []
        self.shoesList = []
        self.removedItems = []

    def __handleUnexpectedExit(self, avId):
        if avId != self.customerId:
            self.notify.warning('received unexpected exit for av %s that is not using the trunk!' % avId)
            return

        self.customerId = 0
        self.customerDNA = None
        self.gender = ''
        self.__resetItemLists()
        self.d_setMovie(ClosetGlobals.CLOSET_MOVIE_CLEAR, 0)
        self.sendUpdate('setCustomerDNA', [0 for _ in xrange(14)])
        self.d_setState(ClosetGlobals.CLOSED, 0, self.ownerId, self.gender, self.hatList, self.glassesList,
                        self.backpackList, self.shoesList)
