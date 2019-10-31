from operator import itemgetter

from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

from toontown.toonbase import TTLocalizer


class DistributedTrophyMgrAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedTrophyMgrAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.leaderInfo = ([], [], [])

    def requestTrophyScore(self):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)
        if not av:
            return

        if avId not in self.leaderInfo[0]:
            return
        else:
            i = self.leaderInfo[0].index(avId)
            av.d_setTrophyScore(self.leaderInfo[2][i])

    def getLeaderInfo(self):
        return self.leaderInfo

    def sort(self):
        scores = []
        for avId in self.leaderInfo[0]:
            i = self.leaderInfo[0].index(avId)
            scores.append((avId, self.leaderInfo[1][i], self.leaderInfo[2][i]))

        scores.sort(key=itemgetter(2), reverse=True)
        avIds = []
        names = []
        numFloors = []
        for avId, name, score in scores:
            avIds.append(avId)
            names.append(name)
            numFloors.append(score)

        self.leaderInfo = (avIds, names, numFloors)

    def addTrophy(self, avId, name, numFloors):
        if avId not in self.leaderInfo[0]:
            self.leaderInfo[0].append(avId)
            self.leaderInfo[1].append(name)
            self.leaderInfo[2].append(numFloors)
        else:
            i = self.leaderInfo[0].index(avId)
            self.leaderInfo[1][i] = name
            self.leaderInfo[2][i] += numFloors

        self.sort()

        messenger.send('leaderboardChanged')
        messenger.send('leaderboardFlush')

        av = self.air.doId2do.get(avId)
        if av:
            i = self.leaderInfo[0].index(avId)
            av.d_setTrophyScore(self.leaderInfo[2][i])

    def removeTrophy(self, avId, numFloors):
        if avId in self.leaderInfo[0]:
            i = self.leaderInfo[0].index(avId)
            self.leaderInfo[2][i] -= numFloors
            av = self.air.doId2do.get(avId)
            if av:
                av.d_setTrophyScore(max(0, self.leaderInfo[2][i]))

            if self.leaderInfo[2][i] <= 0:
                del self.leaderInfo[0][i]
                del self.leaderInfo[1][i]
                del self.leaderInfo[2][i]

            self.sort()

            av = self.air.doId2do.get(avId)
            if av:
                av.d_setSystemMessage(0, TTLocalizer.RemoveTrophy)

            messenger.send('leaderboardChanged')
            messenger.send('leaderboardFlush')
        else:
            self.notify.warning('removeTrophy for av %s when av had no score!' % avId)
