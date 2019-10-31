from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectUD import DistributedObjectUD

class ObjectServerUD(DistributedObjectUD):
    notify = DirectNotifyGlobal.directNotify.newCategory("ObjectServerUD")

    def setName(self, todo0):
        pass

    def setDcHash(self, todo0):
        pass

    def setDateCreated(self, todo0):
        pass

