from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class DistributedPhaseEventMgrAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedPhaseEventMgrAI")

    def setNumPhases(self, todo0):
        pass

    def setDates(self, todo0):
        pass

    def setCurPhase(self, todo0):
        pass

    def setIsRunning(self, todo0):
        pass

