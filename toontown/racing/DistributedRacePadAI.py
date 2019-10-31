from direct.directnotify import DirectNotifyGlobal
from direct.distributed.ClockDelta import globalClockDelta
from direct.fsm.FSM import FSM

from toontown.racing import RaceGlobals
from toontown.racing.DistributedKartPadAI import DistributedKartPadAI
from toontown.racing.KartShopGlobals import KartGlobals
from toontown.toonbase import ToontownGlobals


class DistributedRacePadAI(DistributedKartPadAI, FSM):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedRacePadAI')
    defaultTransitions = {'Off': ['WaitEmpty'],
                          'WaitEmpty': ['WaitCountdown', 'Off'],
                          'WaitCountdown': ['WaitEmpty',
                                            'WaitBoarding',
                                            'Off',
                                            'AllAboard'],
                          'WaitBoarding': ['AllAboard', 'WaitEmpty', 'Off'],
                          'AllAboard': ['Off', 'WaitEmpty', 'WaitCountdown']}

    def __init__(self, air):
        DistributedKartPadAI.__init__(self, air)
        FSM.__init__(self, 'DistributedRacePadAI')
        self.genre = 'urban'
        self.state = 'Off'
        self.trackInfo = [0, 0]
        self.laps = 3
        self.avIds = []

    def enterAllAboard(self):
        taskMgr.doMethodLater(KartGlobals.ENTER_RACE_TIME, self.enterRace, self.uniqueName('enterRaceTask'))

    def exitAllAboard(self):
        self.avIds = []

    def considerAllAboard(self, task=None):
        for block in self.startingBlocks:
            if block.currentMovie:
                if not self.state == 'WaitBoarding':
                    self.request('WaitBoarding')

                return

        if self.trackInfo[1] in (RaceGlobals.ToonBattle, RaceGlobals.Circuit):
            if len(self.avIds) < 2:
                for block in self.startingBlocks:
                    if block.avId != 0:
                        block.normalExit()

                self.request('WaitEmpty')
                return

        self.request('AllAboard')

        if task:
            return task.done

    def enterWaitCountdown(self):
        taskMgr.doMethodLater(KartGlobals.COUNTDOWN_TIME, self.considerAllAboard, self.uniqueName('countdownTask'))

    def exitWaitCountdown(self):
        taskMgr.remove(self.uniqueName('countdownTask'))

    def enterWaitBoarding(self):
        pass

    def enterWaitEmpty(self):
        taskMgr.doMethodLater(RaceGlobals.TrackSignDuration, self.changeTrack, self.uniqueName('changeTrack'))

    def exitWaitEmpty(self):
        taskMgr.remove(self.uniqueName('changeTrack'))

    def changeTrack(self, task):
        trackInfo = RaceGlobals.getNextRaceInfo(self.trackInfo[0], self.genre, self.index)
        trackId, raceType = trackInfo[0], trackInfo[1]
        if raceType == RaceGlobals.ToonBattle:
            if ToontownGlobals.CIRCUIT_RACING in self.air.holidayManager.currentHolidays or \
                    ToontownGlobals.CIRCUIT_RACING_EVENT in self.air.holidayManager.currentHolidays or \
                    ToontownGlobals.SILLY_SATURDAY_CIRCUIT in self.air.holidayManager.currentHolidays:
                raceType = RaceGlobals.Circuit

        self.setTrackInfo([trackId, raceType])
        self.laps = trackInfo[2]
        self.sendUpdate('setTrackInfo', [self.trackInfo])
        return task.again

    def enterRace(self, task):
        trackId, raceType = self.trackInfo
        circuitLoop = []
        if raceType == RaceGlobals.Circuit:
            circuitLoop = RaceGlobals.getCircuitLoop(trackId)

        raceZone = self.air.raceMgr.createRace(trackId, raceType, self.laps, self.avIds, circuitLoop=circuitLoop[1:],
                                               circuitPoints={}, circuitTimes={})
        for block in self.startingBlocks:
            self.sendUpdateToAvatarId(block.avId, 'setRaceZone', [raceZone])
            block.raceExit()

        return task.done

    def addAvBlock(self, avId, startingBlock, paid):
        av = self.air.doId2do.get(avId)
        if not av:
            return

        if not av.hasKart():
            return KartGlobals.ERROR_CODE.eNoKart
        elif self.state == 'Off':
            return KartGlobals.ERROR_CODE.eTrackClosed
        elif self.state in ('AllAboard', 'WaitBoarding'):
            return KartGlobals.ERROR_CODE.eBoardOver
        elif startingBlock.avId != 0:
            return KartGlobals.ERROR_CODE.eOcuppied
        elif RaceGlobals.getEntryFee(self.trackInfo[0], self.trackInfo[1]) > av.getTickets():
            return KartGlobals.ERROR_CODE.eTickets

        self.avIds.append(avId)
        if not self.state == 'WaitCountdown':
            self.request('WaitCountdown')

        return KartGlobals.ERROR_CODE.success

    def removeAvBlock(self, avId, startingBlock):
        if avId in self.avIds:
            self.avIds.remove(avId)

    def kartMovieDone(self):
        if len(self.avIds) == 0 and not self.state == 'WaitEmpty':
            self.request('WaitEmpty')

        if self.state == 'WaitBoarding':
            self.considerAllAboard()

    def getState(self):
        return self.state, globalClockDelta.getRealNetworkTime()

    def getTrackInfo(self):
        return self.trackInfo

    def request(self, state):
        FSM.request(self, state)
        self.state = state
        self.sendUpdate('setState', [state, globalClockDelta.getRealNetworkTime()])

    def setRaceZone(self, todo0):
        pass

    def setTrackInfo(self, trackInfo):
        self.trackInfo = [trackInfo[0], trackInfo[1]]
