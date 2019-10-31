from direct.directnotify import DirectNotifyGlobal
from toontown.parties.DistributedPartyTeamActivityAI import DistributedPartyTeamActivityAI

class DistributedPartyTugOfWarActivityAI(DistributedPartyTeamActivityAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedPartyTugOfWarActivityAI")

    def reportKeyRateForce(self, todo0, todo1):
        pass

    def reportFallIn(self, todo0):
        pass

    def setToonsPlaying(self, todo0, todo1):
        pass

    def updateToonKeyRate(self, todo0, todo1):
        pass

    def updateToonPositions(self, todo0):
        pass

