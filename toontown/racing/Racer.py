from direct.directnotify import DirectNotifyGlobal
from direct.distributed.ClockDelta import globalClockDelta


class Racer:
    notify = DirectNotifyGlobal.directNotify.newCategory('Racer')

    def __init__(self, race, air, avId, zoneId):
        self.race = race
        self.air = air
        self.avId = avId
        self.zoneId = zoneId
        self.avatar = self.air.doId2do.get(self.avId)
        self.avatar.takeOutKart(self.zoneId)
        self.kart = self.avatar.kart
        self.anvilTarget = False
        self.baseTime = 0.0
        self.hasGag = False
        self.gagType = None
        self.exited = False
        self.finished = False
        self.lapT = 0.0
        self.totalTime = 0.0
        self.maxLap = 1
        self.timestamp = globalClockDelta.getRealNetworkTime()
        self.exitEvent = self.air.getAvatarExitEvent(self.avId)
        self.race.accept(self.exitEvent, self.race.unexpectedExit, [self.avId])

    def setLapT(self, numLaps, t, timestamp):
        self.maxLap = numLaps
        self.lapT = t
        self.timestamp = timestamp
        self.totalTime += t
