from direct.directnotify import DirectNotifyGlobal
from direct.distributed.ClockDelta import globalClockDelta
from direct.distributed.DistributedObjectAI import DistributedObjectAI


class DistributedGagAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedGagAI')

    def __init__(self, air, avId, race, todo1, x, y, z, type):
        DistributedObjectAI.__init__(self, air)
        self.ownerId = avId
        self.race = race
        self.pos = (x, y, z)
        self.type = type
        self.initTime = globalClockDelta.getFrameNetworkTime()
        self.activateTime = 0

    def getInitTime(self):
        return self.initTime

    def getActivateTime(self):
        return self.activateTime

    def getPos(self):
        return self.pos

    def getRace(self):
        return self.race.getDoId()

    def getOwnerId(self):
        return self.ownerId

    def getType(self):
        return self.type

    def hitSomebody(self, avId, time):
        self.race.thrownGags.remove(self)
        self.requestDelete()
