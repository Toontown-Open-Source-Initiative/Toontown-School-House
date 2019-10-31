import random

from direct.distributed.ClockDelta import *
from direct.distributed.DistributedNodeAI import DistributedNodeAI

from toontown.fishing import FishingTargetGlobals


class DistributedFishingTargetAI(DistributedNodeAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedFishingTargetAI')

    def __init__(self, air):
        DistributedNodeAI.__init__(self, air)
        self.pondDoId = 0
        self.angle = 0
        self.radius = 0
        self.time = 0
        self.centerPoint = None

    def generate(self):
        DistributedNodeAI.generate(self)
        pond = self.air.doId2do.get(self.pondDoId)
        if pond:
            pond.addTarget(self)

        self.centerPoint = FishingTargetGlobals.getTargetCenter(pond.getArea())
        self.__updateState()

    def delete(self):
        taskMgr.remove('update-fishing-target-%d' % self.doId)
        DistributedNodeAI.delete(self)

    def setPondDoId(self, pondDoId):
        self.pondDoId = pondDoId

    def d_setPondDoId(self, pondDoId):
        self.sendUpdate('setPondDoId', [pondDoId])

    def b_setPondDoId(self, pondDoId):
        self.setPondDoId(pondDoId)
        self.d_setPondDoId(pondDoId)

    def getPondDoId(self):
        return self.pondDoId

    def setState(self, stateIndex, angle, radius, time, timeStamp):
        self.angle = angle
        self.radius = radius
        self.time = time

    def d_setState(self, stateIndex, angle, radius, time, timeStamp):
        self.sendUpdate('setState', [stateIndex, angle, radius, time, timeStamp])

    def b_setState(self, stateIndex, angle, radius, time, timeStamp):
        self.setState(stateIndex, angle, radius, time, timeStamp)
        self.d_setState(stateIndex, angle, radius, time, timeStamp)

    def getState(self):
        return [0, self.angle, self.radius, self.time, globalClockDelta.getRealNetworkTime()]

    def __updateState(self, task=None):
        # The targets should be moved at random speeds.
        self.b_setPosHpr(self.radius * math.cos(self.angle) + self.centerPoint[0],
                         self.radius * math.sin(self.angle) + self.centerPoint[1], self.centerPoint[2], 0, 0, 0)

        # Their angle, radius, and time should be random as well.
        angle = random.randrange(359)
        pond = self.air.doId2do.get(self.pondDoId)
        if not pond:
            return

        area = pond.getArea()
        radius = random.uniform(FishingTargetGlobals.getTargetRadius(area), 0)
        time = random.uniform(10.0, 5.0)
        self.b_setState(0, angle, radius, time, globalClockDelta.getRealNetworkTime())
        taskMgr.doMethodLater(time + random.uniform(5, 2.5), self.__updateState, 'update-fishing-target-%d' % self.doId)
        if task:
            return task.done
