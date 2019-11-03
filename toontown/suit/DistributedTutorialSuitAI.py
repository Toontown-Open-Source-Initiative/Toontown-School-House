from direct.directnotify import DirectNotifyGlobal
from panda3d.core import *

from toontown.suit.DistributedSuitBaseAI import DistributedSuitBaseAI
from toontown.suit.SuitDNA import SuitDNA
from toontown.tutorial.DistributedBattleTutorialAI import DistributedBattleTutorialAI


class TutorialBattleManager:
    notify = DirectNotifyGlobal.directNotify.newCategory('TutorialBattleManager')

    def __init__(self, avId):
        self.avId = avId

    def destroy(self, battle):
        if battle.suitsKilledThisBattle:
            if self.avId in simbase.air.tutorialManager.avId2fsm.keys():
                simbase.air.tutorialManager.avId2fsm[self.avId].demand('HQ')

        battle.requestDelete()


class DistributedTutorialSuitAI(DistributedSuitBaseAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedTutorialSuitAI')

    def __init__(self, air):
        DistributedSuitBaseAI.__init__(self, air, None)
        suitDNA = SuitDNA()
        suitDNA.newSuit('m')
        self.dna = suitDNA
        self.setLevel(1)
        self.confrontPosHpr = (0, 0, 0, 0, 0, 0)

    def destroy(self):
        del self.dna

    def requestBattle(self, x, y, z, h, p, r):
        avId = self.air.getAvatarIdFromSender()
        if not avId:
            return

        self.confrontPosHpr = (LPoint3f(x, y, z), LPoint3f(h, p, r))
        battle = DistributedBattleTutorialAI(self.air, TutorialBattleManager(avId), LPoint3f(x, y, z), self, avId,
                                             20001, maxSuits=1, tutorialFlag=1)
        battle.generateWithRequired(self.zoneId)
        battle.battleCellId = 0

    def getConfrontPosHpr(self):
        return self.confrontPosHpr
