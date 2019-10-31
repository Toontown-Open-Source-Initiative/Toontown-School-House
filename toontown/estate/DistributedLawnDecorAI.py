from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedNodeAI import DistributedNodeAI


class DistributedLawnDecorAI(DistributedNodeAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedLawnDecorAI')

    def __init__(self, mgr):
        DistributedNodeAI.__init__(self, mgr.air)
        self.mgr = mgr
        self.plot = 0
        self.ownerIndex = 0
        self.ownerDoId = 0
        self.owner = None

    def setPlot(self, plot):
        self.plot = plot

    def getPlot(self):
        return self.plot

    def getHeading(self):
        return self.getH()

    def getPosition(self):
        return self.getPos()

    def setOwnerIndex(self, ownerIndex):
        self.ownerIndex = ownerIndex
        self.ownerDoId = self.mgr.gardenMgr.estate.activeToons[ownerIndex]
        self.owner = self.air.doId2do.get(self.ownerDoId)

    def getOwnerIndex(self):
        return self.ownerIndex

    def d_setMovie(self, mode, avId=None):
        if avId is None:
            avId = self.air.getAvatarIdFromSender()

        self.sendUpdate('setMovie', [mode, avId])

    def d_interactionDenied(self):
        avId = self.air.getAvatarIdFromSender()
        if not avId:
            return

        self.sendUpdate('interactionDenied', [avId])
