from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class ObjectServerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("ObjectServerAI")

    def setName(self, todo0):
        pass

    def setDcHash(self, todo0):
        pass

    def setDateCreated(self, todo0):
        pass

