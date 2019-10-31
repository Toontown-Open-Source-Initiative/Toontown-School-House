from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

from toontown.toonbase import TTLocalizer


class DistributedLeaderBoardAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedLeaderBoardAI')

    def __init__(self, air, name, x, y, z, h, p, r):
        DistributedObjectAI.__init__(self, air)
        self.name = name
        self.records = {}
        self.subscriptions = []
        self.currentIndex = -1
        self.posHpr = (x, y, z, h, p, r)
        self.accept('UpdateRaceRecord', self.updateRaceRecord)

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)
        self.accept('GS_LeaderBoardSwap' + str(self.zoneId), self.setDisplay)

    def getName(self):
        return self.name

    def updateRaceRecord(self, record):
        trackId, period = record
        if trackId not in self.records:
            return

        self.records[trackId][period] = [(x[0], x[3]) for x in self.air.raceMgr.getRecords(trackId, period)]

    def subscribeTo(self, subscription):
        self.records.setdefault(subscription[0], {})[subscription[1]] = [(x[0], x[3]) for x in
                                                                         self.air.raceMgr.getRecords(subscription[0],
                                                                                                     subscription[1])]
        self.subscriptions.append(subscription)

    def getPosHpr(self):
        return self.posHpr

    def setDisplay(self):
        self.currentIndex += 1
        if self.currentIndex >= len(self.subscriptions):
            self.currentIndex = 0

        trackName = TTLocalizer.KartRace_TrackNames[self.subscriptions[self.currentIndex][0]]
        periodName = TTLocalizer.RecordPeriodStrings[self.subscriptions[self.currentIndex][1]]
        leaderList = self.records[self.subscriptions[self.currentIndex][0]][self.subscriptions[self.currentIndex][1]]

        self.sendUpdate('setDisplay', [trackName, periodName, leaderList])
