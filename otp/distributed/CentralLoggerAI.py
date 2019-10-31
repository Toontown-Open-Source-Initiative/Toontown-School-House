from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class CentralLoggerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("CentralLoggerAI")

    def sendMessage(self, todo0, todo1, todo2, todo3):
        pass

    def logAIGarbage(self):
        pass

