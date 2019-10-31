from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectGlobalAI import DistributedObjectGlobalAI

class DistributedWhitelistMgrAI(DistributedObjectGlobalAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedWhitelistMgrAI")

    def updateWhitelist(self):
        pass

    def whitelistMgrAIStartingUp(self, todo0, todo1):
        pass

    def newListUDtoAI(self):
        pass

