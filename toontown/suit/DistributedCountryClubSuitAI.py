from toontown.suit.DistributedMintSuitAI import DistributedMintSuitAI
from direct.directnotify import DirectNotifyGlobal

class DistributedCountryClubSuitAI(DistributedMintSuitAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedMintSuitAI')

    def isForeman(self):
        return 0

    def isSupervisor(self):
        return 0

    def isClerk(self):
        return 0

    def isClubPresident(self):
        return self.boss

    def isVirtual(self):
        return 0
