from otp.ai.AIBaseGlobal import *
from direct.directnotify import DirectNotifyGlobal
from toontown.battle import SuitBattleGlobals
from otp.level import DistributedEntityAI
from otp.ai.AIBase import AIBase
from toontown.suit import SuitDialog

class DistributedFactoryCogAI(DistributedEntityAI.DistributedEntityAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedFactoryCogAI')

    def __init__(self, air):
        DistributedEntityAI.DistributedEntityAI.__init__(self, air)
        self.chasing = 0
        return

    def delete(self):
        DistributedEntityAI.DistributedEntityAI.delete(self)
        return

    def setAlert(self, avId):
        if avId == self.air.getAvatarIdFromSender():
            av = self.air.doId2do.get(avId)
            if av:
                self.chasing = avId
                self.sendUpdate('setConfrontToon', [avId])

    def setStrayed(self):
        if self.chasing > 0:
            self.chasing = 0
            self.sendUpdate('setReturn', [])

    def resume(self):
        self.notify.debug('Suit %s resume' % self.doId)
        self.sendUpdate('setReturn', [])
        return None

