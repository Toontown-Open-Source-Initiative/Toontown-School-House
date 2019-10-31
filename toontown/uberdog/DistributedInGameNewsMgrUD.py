from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD

class DistributedInGameNewsMgrUD(DistributedObjectGlobalUD):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedInGameNewsMgrUD")

    def setLatestIssueStr(self, todo0):
        pass

    def inGameNewsMgrAIStartingUp(self, todo0, todo1):
        pass

    def newIssueUDtoAI(self, todo0):
        pass

