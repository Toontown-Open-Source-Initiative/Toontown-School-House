from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class DistributedProjectileAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedProjectileAI")

    def setInitTime(self, todo0):
        pass

    def setPos(self, todo0, todo1, todo2):
        pass

    def setRace(self, todo0):
        pass

    def setOwnerId(self, todo0):
        pass

    def setType(self, todo0):
        pass

    def hitSomebody(self, todo0, todo1):
        pass

