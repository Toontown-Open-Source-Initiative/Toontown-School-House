from direct.directnotify import DirectNotifyGlobal
from direct.showbase import DirectObject


class CImpulse(DirectObject.DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('CImpulse')

    def __init__(self):
        self.mover = None
        self.nodePath = None
        self.VecType = None

    def destroy(self):
        self.mover = None
        self.nodePath = None
        self.VecType = None

    def process(self, dt):
        pass

    def setMover(self, mover):
        if self.mover != mover:
            self.mover = mover
            self.nodePath = self.mover.getNodePath()
            self.VecType = self.mover.VecType

    def getNodePath(self):
        return self.nodePath

    def clearMover(self, mover):
        if self.mover == mover:
            self.mover = None
            self.nodePath = None
            self.VecType = None
        else:
            self.notify.warning('clearMover: unknown CMover')

    def isCpp(self):
        return 1
