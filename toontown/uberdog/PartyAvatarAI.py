from direct.directnotify import DirectNotifyGlobal

from panda3d.core import *

from otp.ai.AIBaseGlobal import *

class PartyAvatarAI:
    notify = DirectNotifyGlobal.directNotify.newCategory("PartyAvatarAI")

    def __init__(self):
        self.bankMoney = 0
        self.money = 0
        self.maxBankMoney = 0
        self.maxMoney = 0

    def setMoney(self, money):
        self.notify.debug("Setting money to %s." % (money[0]))
        self.money = money[0]
        self.notify.debug("money is %s." % (str(self.money)))

    def getMoney(self):
        return self.money

    def setMaxMoney(self, maxMoney):
        self.notify.debug("Setting maxMoney to %s." % (maxMoney[0]))
        self.maxMoney = maxMoney[0]
        self.notify.debug("maxMoney is %s." % (str(self.maxMoney)))

    def getMaxMoney(self):
        return self.maxMoney

    def getTotalMoney(self):
        return (self.money + self.bankMoney)

    def setBankMoney(self, bankMoney):
        self.notify.debug("Setting bankMoney to %s." % (bankMoney[0]))
        self.bankMoney = bankMoney[0]
        self.notify.debug("bankMoney is %s." % (str(self.bankMoney)))

    def getBankMoney(self):
        return self.bankMoney

    def setMaxBankMoney(self, maxBankMoney):
        self.notify.debug("Setting maxBankMoney to %s." % (maxBankMoney[0]))
        self.maxBankMoney = maxBankMoney[0]
        self.notify.debug("maxBankMoney is %s." % (str(self.maxBankMoney)))

    def getMaxBankMoney(self):
        return self.maxBankMoney

    def takeMoney(self, deltaMoney, bUseBank=True):
        totalMoney = self.money

        if bUseBank:
            totalMoney += self.bankMoney

        if (deltaMoney > totalMoney):
            self.notify.warning("Not enough money! AvId: %s Has:%s Charged:%s" % (self.doId, totalMoney, deltaMoney))
            return False

        if (bUseBank and (deltaMoney > self.money)):
            bankMoney = min(self.bankMoney - (deltaMoney - self.money), self.maxBankMoney)
            self.setBankMoney(bankMoney)
            self.setMoney(0)
        else:
            self.setMoney(self.money - deltaMoney)

        return True

    @staticmethod
    def createFromFields(fields):
        avatar = PartyAvatarAI()

        for key, value in fields.iteritems():
            getattr(avatar, key)(value)

        return avatar
