from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectGlobalAI import DistributedObjectGlobalAI


class DistributedInGameNewsMgrAI(DistributedObjectGlobalAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedInGameNewsMgrAI')

    def __init__(self, air):
        DistributedObjectGlobalAI.__init__(self, air)
        self.latestIssueStr = ''

    def setLatestIssueStr(self, latestIssueStr):
        self.latestIssueStr = latestIssueStr

    def d_setLatestIssueStr(self, latestIssueStr):
        self.sendUpdate('setLatestIssueStr', [latestIssueStr])

    def b_setLatestIssueStr(self, latestIssueStr):
        self.setLatestIssueStr(latestIssueStr)
        self.d_setLatestIssueStr(latestIssueStr)

    def getLatestIssueStr(self):
        return self.latestIssueStr

    def inGameNewsMgrAIStartingUp(self, todo0, todo1):
        pass

    def newIssueUDtoAI(self, todo0):
        pass
