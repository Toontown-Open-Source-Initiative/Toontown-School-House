from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectUD import DistributedObjectUD

class CentralLoggerUD(DistributedObjectUD):
    notify = DirectNotifyGlobal.directNotify.newCategory("CentralLoggerUD")

    def sendMessage(self, todo0, todo1, todo2, todo3):
        pass

    def logAIGarbage(self):
        pass

