from toontown.toonbase import ToontownGlobals, TTLocalizer
from direct.directnotify import DirectNotifyGlobal
from direct.showbase import DirectObject
from toontown.suit import DistributedBossbotBossAI, DistributedLawbotBossAI
from toontown.suit import DistributedCashbotBossAI, DistributedSellbotBossAI

LaffLimits = ToontownGlobals.FactoryLaffMinimums


class BoardingPartyDestination(DirectObject.DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('BoardingPartyDestination')

    def __init__(self, loaderName, where, name='Unknown', laffLimit=0, disguiseRequirement=-1,
                 groupSize=4, how='teleportIn', interiorIdName='id', interiorId=0):
        DirectObject.DirectObject.__init__(self)
        self.name = name
        self.laffLimit = laffLimit
        self.disguiseRequirement = disguiseRequirement
        self.groupSize = groupSize
        self.loaderName = loaderName
        self.where = where
        self.how = how
        self.interiorIdName = interiorIdName
        self.interiorId = interiorId

    def sendToDestFunction(self, avIdList):
        raise NotImplementedError('This must be implemented in subclasses.')


# SBHQ Facilities


class FactoryBoardingPartyDestination(BoardingPartyDestination):
    def __init__(self, name, laffLimit, entranceId):
        self.entranceId = entranceId
        BoardingPartyDestination.__init__(self, 'cogHQLoader', 'factoryInterior', name, laffLimit)

    def sendToDestFunction(self, avIdList):
        return simbase.air.factoryMgr.createFactory(ToontownGlobals.SellbotFactoryInt, self.entranceId, avIdList)


class FactoryFrontEntranceBoardingPartyDestination(FactoryBoardingPartyDestination):
    def __init__(self):
        FactoryBoardingPartyDestination.__init__(self, TTLocalizer.ElevatorSellBotFactory0, LaffLimits[0][0], 0)


class FactorySideEntranceBoardingPartyDestination(FactoryBoardingPartyDestination):
    def __init__(self):
        FactoryBoardingPartyDestination.__init__(self, TTLocalizer.ElevatorSellBotFactory0, LaffLimits[0][1], 1)


# CBHQ Facilities


class MintBoardingPartyDestination(BoardingPartyDestination):
    def __init__(self, name, laffLimit, interiorId):
        self.interiorId = interiorId
        BoardingPartyDestination.__init__(self, 'cogHQLoader', 'mintInterior', name, laffLimit,
                                          interiorIdName='mintId', interiorId=interiorId)

    def sendToDestFunction(self, avIdList):
        return simbase.air.mintMgr.createMint(self.interiorId, avIdList)


class CoinBoardingPartyDestination(MintBoardingPartyDestination):
    def __init__(self):
        MintBoardingPartyDestination.__init__(self, TTLocalizer.ElevatorCashBotMint0, LaffLimits[1][0],
                                              ToontownGlobals.CashbotMintIntA)


class DollarBoardingPartyDestination(MintBoardingPartyDestination):
    def __init__(self):
        MintBoardingPartyDestination.__init__(self, TTLocalizer.ElevatorCashBotMint1, LaffLimits[1][1],
                                              ToontownGlobals.CashbotMintIntB)


class BullBoardingPartyDestination(MintBoardingPartyDestination):
    def __init__(self):
        MintBoardingPartyDestination.__init__(self, TTLocalizer.ElevatorCashBotMint2, LaffLimits[1][2],
                                              ToontownGlobals.CashbotMintIntC)

# LBHQ Facilities


class StageBoardingPartyDestination(BoardingPartyDestination):
    def __init__(self, name, laffLimit, interiorId, entranceId):
        self.entranceId = entranceId
        self.interiorId = interiorId
        BoardingPartyDestination.__init__(self, 'cogHQLoader', 'stageInterior', name, laffLimit,
                                          interiorIdName='stageId', interiorId=interiorId)

    def sendToDestFunction(self, avIdList):
        return simbase.air.lawMgr.createLawOffice(self.interiorId, self.entranceId, avIdList)


class ABoardingPartyDestination(StageBoardingPartyDestination):
    def __init__(self):
        StageBoardingPartyDestination.__init__(self, TTLocalizer.ElevatorLawBotCourse0, LaffLimits[2][0],
                                               ToontownGlobals.LawbotStageIntA, 0)


class BBoardingPartyDestination(StageBoardingPartyDestination):
    def __init__(self):
        StageBoardingPartyDestination.__init__(self, TTLocalizer.ElevatorLawBotCourse1, LaffLimits[2][1],
                                               ToontownGlobals.LawbotStageIntB, 1)


class CBoardingPartyDestination(StageBoardingPartyDestination):
    def __init__(self):
        StageBoardingPartyDestination.__init__(self, TTLocalizer.ElevatorLawBotCourse2, LaffLimits[2][2],
                                               ToontownGlobals.LawbotStageIntC, 2)


class DBoardingPartyDestination(StageBoardingPartyDestination):
    def __init__(self):
        StageBoardingPartyDestination.__init__(self, TTLocalizer.ElevatorLawBotCourse3, LaffLimits[2][3],
                                               ToontownGlobals.LawbotStageIntD, 3)

# BBHQ Facilities


class CountryClubBoardingPartyDestination(BoardingPartyDestination):
    def __init__(self, name, laffLimit, interiorId):
        self.interiorId = interiorId
        BoardingPartyDestination.__init__(self, 'cogHQLoader', 'countryClubInterior', name, laffLimit,
                                          interiorIdName='countryClubId', interiorId=interiorId)

    def sendToDestFunction(self, avIdList):
        return simbase.air.countryClubMgr.createCountryClub(self.interiorId, avIdList)


class FrontBoardingPartyDestination(CountryClubBoardingPartyDestination):
    def __init__(self):
        CountryClubBoardingPartyDestination.__init__(self, TTLocalizer.ElevatorBossBotCourse0, LaffLimits[3][0],
                                              ToontownGlobals.BossbotCountryClubIntA)


class MidBoardingPartyDestination(CountryClubBoardingPartyDestination):
    def __init__(self):
        CountryClubBoardingPartyDestination.__init__(self, TTLocalizer.ElevatorBossBotCourse1, LaffLimits[3][1],
                                              ToontownGlobals.BossbotCountryClubIntB)


class BackBoardingPartyDestination(CountryClubBoardingPartyDestination):
    def __init__(self):
        CountryClubBoardingPartyDestination.__init__(self, TTLocalizer.ElevatorBossBotCourse2, LaffLimits[3][2],
                                              ToontownGlobals.BossbotCountryClubIntC)


# Bosses


class BossBoardingPartyDestination(BoardingPartyDestination):
    def __init__(self, name, disguiseRequirement, bossConstructor):
        self.bossConstructor = bossConstructor
        BoardingPartyDestination.__init__(self, 'cogHQLoader', 'cogHQBossBattle', name, 0,
                                          disguiseRequirement, 8, 'movie')

    def sendToDestFunction(self, avIdList):
        return self.createBossOffice(avIdList)

    def createBossOffice(self, avIdList):
        bossZone = simbase.air.allocateZone()
        self.notify.info('createBossOffice: %s' % bossZone)
        bossCog = self.bossConstructor(simbase.air)
        for avId in avIdList:
            if avId:
                bossCog.addToon(avId)

        bossCog.generateWithRequired(bossZone)
        self.acceptOnce(bossCog.uniqueName('BossDone'), self.destroyBossOffice, extraArgs=[bossCog])
        bossCog.b_setState('WaitForToons')
        return bossZone

    def destroyBossOffice(self, bossCog):
        bossZone = bossCog.zoneId
        self.notify.info('destroyBossOffice: %s' % bossZone)
        bossCog.requestDelete()
        simbase.air.deallocateZone(bossZone)


class VPBoardingPartyDestination(BossBoardingPartyDestination):
    def __init__(self):
        BossBoardingPartyDestination.__init__(self, TTLocalizer.ElevatorSellBotBoss, 3,
                                              DistributedSellbotBossAI.DistributedSellbotBossAI)


class CFOBoardingPartyDestination(BossBoardingPartyDestination):
    def __init__(self):
        BossBoardingPartyDestination.__init__(self, TTLocalizer.ElevatorCashBotBoss, 2,
                                              DistributedCashbotBossAI.DistributedCashbotBossAI)


class CJBoardingPartyDestination(BossBoardingPartyDestination):
    def __init__(self):
        BossBoardingPartyDestination.__init__(self, TTLocalizer.ElevatorLawBotBoss, 1,
                                              DistributedLawbotBossAI.DistributedLawbotBossAI)


class CEOBoardingPartyDestination(BossBoardingPartyDestination):
    def __init__(self):
        BossBoardingPartyDestination.__init__(self, TTLocalizer.ElevatorBossBotBoss, 0,
                                              DistributedBossbotBossAI.DistributedBossbotBossAI)
