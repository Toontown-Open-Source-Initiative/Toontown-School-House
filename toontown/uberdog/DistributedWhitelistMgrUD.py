from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD

class DistributedWhitelistMgrUD(DistributedObjectGlobalUD):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedWhitelistMgrUD")

    def updateWhitelist(self):
        pass

    def whitelistMgrAIStartingUp(self, todo0, todo1):
        pass

    def newListUDtoAI(self):
        pass

