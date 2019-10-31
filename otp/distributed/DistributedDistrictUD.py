from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectUD import DistributedObjectUD

class DistributedDistrictUD(DistributedObjectUD):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedDistrictUD")

    def setName(self, todo0):
        pass

    def setAvailable(self, todo0):
        pass

