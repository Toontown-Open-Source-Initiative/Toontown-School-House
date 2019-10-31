from direct.directnotify import DirectNotifyGlobal
from panda3d.core import *


class CMover:
    notify = DirectNotifyGlobal.directNotify.newCategory('CMover')

    def __init__(self, objNodePath, fwdSpeed=1, rotSpeed=1):
        self.objNodePath = objNodePath
        self.fwdSpeed = fwdSpeed
        self.rotSpeed = rotSpeed
        self.VecType = Vec3(0, 0, 0)
        self.dt = 1.0
        self.dtClock = globalClock.getFrameTime()
        self.movement = Vec3(0, 0, 0)
        self.rotation = Vec3(0, 0, 0)
        self.cImpulses = {}

    def setFwdSpeed(self, fwdSpeed):
        self.fwdSpeed = fwdSpeed

    def getFwdSpeed(self):
        return self.fwdSpeed

    def setRotSpeed(self, rotSpeed):
        self.rotSpeed = rotSpeed

    def getRotSpeed(self):
        return self.rotSpeed

    def getNodePath(self):
        return self.objNodePath

    def processCImpulses(self, dt):
        self.dt = dt
        if self.getDt() == -1.0:
            clockDelta = globalClock.getFrameTime()
            self.dt = clockDelta - self.dtClock
            self.dtClock = clockDelta

        for cImpulse in self.cImpulses.values():
            cImpulse.process(self.getDt())

    def getDt(self):
        return self.dt

    def integrate(self):
        if not self.objNodePath or self.objNodePath.isEmpty():
            return

        self.movement *= self.getDt()
        self.objNodePath.setFluidPos(self.objNodePath, self.movement)
        self.rotation *= self.getDt()
        self.objNodePath.setHpr(self.objNodePath, self.rotation)
        self.movement = Vec3(0, 0, 0)
        self.rotation = Vec3(0, 0, 0)

    def addCImpulse(self, name, cImpulse):
        self.removeCImpulse(name)
        self.cImpulses[name] = cImpulse
        cImpulse.setMover(self)

    def removeCImpulse(self, name):
        if name in self.cImpulses:
            cImpulse = self.cImpulses[name]
            cImpulse.clearMover(self)
            del self.cImpulses[name]
            return True

        return False

    def addShove(self, shove):
        self.movement += shove

    def addRotShove(self, rotShove):
        self.rotation += rotShove
