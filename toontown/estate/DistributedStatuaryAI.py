import time

from direct.directnotify import DirectNotifyGlobal

from toontown.estate import GardenGlobals
from toontown.estate.DistributedLawnDecorAI import DistributedLawnDecorAI

FOUR_DAYS = 86400 * 4


class DistributedStatuaryAI(DistributedLawnDecorAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedStatuaryAI')

    def __init__(self, mgr):
        DistributedLawnDecorAI.__init__(self, mgr)
        self.attributes = None
        self.growthThresholds = None
        self.lastCheck = 0
        self.growthLevel = 0
        self.data = None

    def calculate(self, lastCheck):
        self.attributes = GardenGlobals.PlantAttributes[self.index]
        self.growthThresholds = self.attributes.get('growthThresholds', (0, 0))
        now = int(time.time())
        self.lastCheck = lastCheck
        if self.lastCheck == 0:
            self.lastCheck = now

        self.growthLevel = min((now - self.lastCheck) // FOUR_DAYS, self.growthThresholds[-1] + 1)
        self.update()

    def setTypeIndex(self, typeIndex):
        self.index = typeIndex

    def getTypeIndex(self):
        return self.index

    def getWaterLevel(self):
        return 1

    def setGrowthLevel(self, growthLevel):
        self.growthLevel = growthLevel

    def getGrowthLevel(self):
        return self.growthLevel

    def setOptional(self, data):
        self.data = data

    def getOptional(self):
        return self.data

    def update(self):
        self.mgr.data['statuary'] = self.mgr.S_pack(self.data, self.lastCheck, self.index, self.growthLevel)
        self.mgr.update()

    def removeItem(self):
        avId = self.air.getAvatarIdFromSender()
        if not avId:
            return

        self.d_setMovie(GardenGlobals.MOVIE_REMOVE)

        def handleRemoveItem(task):
            if not self.air:
                return

            plot = self.mgr.placePlot(-1)
            plot.setPlot(self.plot)
            plot.setPos(self.getPos())
            plot.setH(self.getH())
            plot.setOwnerIndex(self.ownerIndex)
            plot.generateWithRequired(self.zoneId)
            plot.d_setMovie(GardenGlobals.MOVIE_FINISHREMOVING, avId)
            plot.d_setMovie(GardenGlobals.MOVIE_CLEAR, avId)
            self.air.writeServerEvent('remove-statuary', avId, plot=self.plot)
            self.requestDelete()
            self.mgr.objects.remove(self)
            self.mgr.data['statuary'] = 0
            self.mgr.update()
            return task.done

        taskMgr.doMethodLater(7, handleRemoveItem, self.uniqueName('handle-remove-item'))
