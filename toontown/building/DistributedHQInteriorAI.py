from direct.distributed import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal

class DistributedHQInteriorAI(DistributedObjectAI.DistributedObjectAI):

    def __init__(self, block, air, zoneId):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)
        self.block = block
        self.zoneId = zoneId
        self.tutorial = 0
        self.isDirty = False
        self.accept('leaderboardChanged', self.leaderboardChanged)
        self.accept('leaderboardFlush', self.leaderboardFlush)

    def delete(self):
        self.ignore('leaderboardChanged')
        self.ignore('leaderboardFlush')
        self.ignore('setLeaderBoard')
        self.ignore('AIStarted')
        DistributedObjectAI.DistributedObjectAI.delete(self)

    def getZoneIdAndBlock(self):
        r = [self.zoneId, self.block]
        return r

    def leaderboardChanged(self):
        self.isDirty = True

    def leaderboardFlush(self):
        if self.isDirty:
            self.sendNewLeaderBoard()

    def sendNewLeaderBoard(self):
        if self.air:
            self.isDirty = False
            self.sendUpdate('setLeaderBoard', self.air.trophyMgr.getLeaderInfo())

    def getLeaderBoard(self):
        return self.air.trophyMgr.getLeaderInfo()

    def getTutorial(self):
        return self.tutorial

    def setTutorial(self, flag):
        if self.tutorial != flag:
            self.tutorial = flag
            self.sendUpdate('setTutorial', [self.tutorial])
