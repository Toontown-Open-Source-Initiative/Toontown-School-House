from toontown.toonbase import ToontownGlobals, TTLocalizer
from direct.directnotify import DirectNotifyGlobal
from direct.showbase import DirectObject
import __builtin__

if hasattr(__builtin__, 'simbase'):
    from toontown.suit.DistributedSellbotBossAI import DistributedSellbotBossAI
    from toontown.suit.DistributedCashbotBossAI import DistributedCashbotBossAI
    from toontown.suit.DistributedLawbotBossAI import DistributedLawbotBossAI
    from toontown.suit.DistributedBossbotBossAI import DistributedBossbotBossAI

LaffLimits = ToontownGlobals.FactoryLaffMinimums


class BoardingPartyDestination(DirectObject.DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('BoardingPartyDestination')

    def __init__(self, loaderName='safeZoneLoader', where='', name='Unknown', groupSize=4, how='teleportIn',
                 useReqLeave=True):
        DirectObject.DirectObject.__init__(self)
        self.name = name
        self.groupSize = groupSize
        self.loaderName = loaderName
        self.where = where
        self.how = how
        self.useReqLeave = useReqLeave

    def __del__(self):
        del self.name
        del self.groupSize
        del self.loaderName
        del self.where
        del self.how
        del self.useReqLeave

    if hasattr(__builtin__, 'simbase'):
        def sendToDestFunction(self, avIdList):
            raise NotImplementedError('This must be implemented in subclasses.')

    elif hasattr(__builtin__, 'base'):
        def signalDone(self, doneStatus):
            place = base.cr.playGame.place
            if not self.useReqLeave:
                place.doneStatus = doneStatus
                messenger.send(place.doneEvent)
            else:
                place.requestLeave(doneStatus)


# Cog HQs


class CogHQBoardingPartyDestination(BoardingPartyDestination):
    # interiorId has a second context here: hood identifier, which is why it's required
    def __init__(self, where, name, laffLimit, interiorId, groupSize=4, interiorIdName='id',
                 disguiseRequirement=-1, how='teleportIn', useReqLeave=True):
        self.laffLimit = laffLimit
        self.interiorIdName = interiorIdName
        self.interiorId = interiorId
        self.disguiseRequirement = disguiseRequirement
        BoardingPartyDestination.__init__(self, 'cogHQLoader', where, name, groupSize, how, useReqLeave=useReqLeave)

    def __del__(self):
        del self.laffLimit
        del self.interiorIdName
        del self.interiorId
        del self.disguiseRequirement
        BoardingPartyDestination.__del__(self)

    if hasattr(__builtin__, 'simbase'):
        def sendToDestFunction(self, avIdList):
            raise NotImplementedError('This must be implemented in subclasses.')


# SBHQ Facilities


class FactoryBoardingPartyDestination(CogHQBoardingPartyDestination):
    def __init__(self, name, laffLimit, entranceId):
        self.entranceId = entranceId
        CogHQBoardingPartyDestination.__init__(self, 'factoryInterior', name, laffLimit,
                                               interiorId=ToontownGlobals.SellbotFactoryInt)

    def __del__(self):
        del self.entranceId
        CogHQBoardingPartyDestination.__del__(self)

    if hasattr(__builtin__, 'simbase'):
        def sendToDestFunction(self, avIdList):
            return simbase.air.factoryMgr.createFactory(ToontownGlobals.SellbotFactoryInt, self.entranceId, avIdList)


class FactoryFrontEntranceBoardingPartyDestination(FactoryBoardingPartyDestination):
    def __init__(self):
        FactoryBoardingPartyDestination.__init__(self, TTLocalizer.ElevatorSellBotFactory0, LaffLimits[0][0], 0)


class FactorySideEntranceBoardingPartyDestination(FactoryBoardingPartyDestination):
    def __init__(self):
        FactoryBoardingPartyDestination.__init__(self, TTLocalizer.ElevatorSellBotFactory1, LaffLimits[0][1], 1)


# CBHQ Facilities


class MintBoardingPartyDestination(CogHQBoardingPartyDestination):
    def __init__(self, name, laffLimit, interiorId):
        CogHQBoardingPartyDestination.__init__(self, 'mintInterior', name, laffLimit, interiorIdName='mintId',
                                               interiorId=interiorId)

    def __del__(self):
        CogHQBoardingPartyDestination.__del__(self)

    if hasattr(__builtin__, 'simbase'):
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


class StageBoardingPartyDestination(CogHQBoardingPartyDestination):
    def __init__(self, name, laffLimit, interiorId, entranceId):
        self.entranceId = entranceId
        CogHQBoardingPartyDestination.__init__(self, 'stageInterior', name, laffLimit, interiorIdName='stageId',
                                               interiorId=interiorId)

    def __del__(self):
        del self.entranceId
        CogHQBoardingPartyDestination.__del__(self)

    if hasattr(__builtin__, 'simbase'):
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


class CountryClubBoardingPartyDestination(CogHQBoardingPartyDestination):
    def __init__(self, name, laffLimit, interiorId):
        CogHQBoardingPartyDestination.__init__(self, 'countryClubInterior', name, laffLimit,
                                               interiorIdName='countryClubId', interiorId=interiorId)

    def __del__(self):
        CogHQBoardingPartyDestination.__del__(self)

    if hasattr(__builtin__, 'simbase'):
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


class BossBoardingPartyDestination(CogHQBoardingPartyDestination):
    def __init__(self, name, disguiseRequirement, bossConstructor=None):
        self.bossConstructor = bossConstructor
        CogHQBoardingPartyDestination.__init__(self, 'cogHQBossBattle', name, 0,
                                               ToontownGlobals.dept2cogHQ(
                                                   ToontownGlobals.cogIndex2dept[disguiseRequirement]), 8, how='movie',
                                               disguiseRequirement=disguiseRequirement, useReqLeave=False)

    def __del__(self):
        del self.bossConstructor
        CogHQBoardingPartyDestination.__del__(self)

    if hasattr(__builtin__, 'simbase'):
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
        if hasattr(__builtin__, 'simbase'):
            BossBoardingPartyDestination.__init__(self, TTLocalizer.ElevatorSellBotBoss, 3,
                                                  DistributedSellbotBossAI)
        else:
            BossBoardingPartyDestination.__init__(self, TTLocalizer.ElevatorSellBotBoss, 3)


class CFOBoardingPartyDestination(BossBoardingPartyDestination):
    def __init__(self):
        if hasattr(__builtin__, 'simbase'):
            BossBoardingPartyDestination.__init__(self, TTLocalizer.ElevatorCashBotBoss, 2,
                                                  DistributedCashbotBossAI)
        else:
            BossBoardingPartyDestination.__init__(self, TTLocalizer.ElevatorCashBotBoss, 2)


class CJBoardingPartyDestination(BossBoardingPartyDestination):
    def __init__(self):
        if hasattr(__builtin__, 'simbase'):
            BossBoardingPartyDestination.__init__(self, TTLocalizer.ElevatorLawBotBoss, 1,
                                                  DistributedLawbotBossAI)
        else:
            BossBoardingPartyDestination.__init__(self, TTLocalizer.ElevatorLawBotBoss, 1)


class CEOBoardingPartyDestination(BossBoardingPartyDestination):
    def __init__(self):
        if hasattr(__builtin__, 'simbase'):
            BossBoardingPartyDestination.__init__(self, TTLocalizer.ElevatorBossBotBoss, 0,
                                                  DistributedBossbotBossAI)
        else:
            BossBoardingPartyDestination.__init__(self, TTLocalizer.ElevatorBossBotBoss, 0)
