from toontown.suit import DistributedFactorySuitAI
from direct.directnotify import DirectNotifyGlobal

class DistributedStageSuitAI(DistributedFactorySuitAI.DistributedFactorySuitAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedStageSuitAI')

    def isForeman(self):
        return 0

    def isSupervisor(self):
        return 0

    def isClerk(self):
        return self.boss

    def isClubPresident(self):
        return 0

    def isVirtual(self):
        return self.virtual
