from direct.directnotify import DirectNotifyGlobal
from direct.distributed.ClockDelta import globalClockDelta

from toontown.estate import BankGlobals
from toontown.estate.DistributedFurnitureItemAI import DistributedFurnitureItemAI


class DistributedBankAI(DistributedFurnitureItemAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBankAI')

    def __init__(self, air, house, furnitureMgr, catalogItem):
        DistributedFurnitureItemAI.__init__(self, air, house, furnitureMgr, catalogItem)
        self.ownerId = self.house.avatarId
        self.avId = 0

    def avatarEnter(self):
        avId = self.air.getAvatarIdFromSender()
        if avId != self.ownerId:
            self.d_setMovie(BankGlobals.BANK_MOVIE_NOT_OWNER, avId)
            return

        # Display the GUI:
        self.d_setMovie(BankGlobals.BANK_MOVIE_GUI, avId)

    def d_setMovie(self, mode, avId):
        self.sendUpdate('setMovie', [mode, avId, globalClockDelta.getRealNetworkTime()])

    def transferMoney(self, amount):
        avId = self.air.getAvatarIdFromSender()
        if avId != self.ownerId:
            self.air.writeServerEvent('suspicious', avId, 'av tried to transfer money with bank they don\'t own')
            return

        av = self.air.doId2do.get(avId)
        if not av:
            self.air.writeServerEvent('suspicious', avId, 'av tried to transfer money with bank not on their shard')
            return

        if av.getLocation() != self.getLocation():
            self.air.writeServerEvent('suspicious', avId, 'av tried to transfer money with bank not in their zone')
            return

        bankMoney = av.getBankMoney()
        money = av.getMoney()
        if amount < 0 and amount < av.getMaxMoney():
            if bankMoney + amount < 0:
                self.air.writeServerEvent('suspicious', avId, 'av tried to withdraw more money than they have')
                return

            av.b_setMoney(money - amount)
            av.b_setBankMoney(bankMoney + amount)
            self.d_setMovie(BankGlobals.BANK_MOVIE_WITHDRAW, avId)
        elif amount > 0 and money < av.getMaxBankMoney():
            if money < amount:
                self.air.writeServerEvent('suspicious', avId, 'av tried to deposit more money than they have')
                return

            av.b_setMoney(money - amount)
            av.b_setBankMoney(bankMoney + amount)
            self.d_setMovie(BankGlobals.BANK_MOVIE_DEPOSIT, avId)
        elif amount == 0:
            self.d_setMovie(BankGlobals.BANK_MOVIE_NO_OP, avId)
