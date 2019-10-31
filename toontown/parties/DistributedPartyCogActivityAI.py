from direct.directnotify import DirectNotifyGlobal
from toontown.parties.DistributedPartyTeamActivityAI import DistributedPartyTeamActivityAI

class DistributedPartyCogActivityAI(DistributedPartyTeamActivityAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedPartyCogActivityAI")

    def pieThrow(self, todo0, todo1, todo2, todo3, todo4, todo5, todo6):
        pass

    def pieHitsToon(self, todo0, todo1, todo2, todo3, todo4):
        pass

    def pieHitsCog(self, todo0, todo1, todo2, todo3, todo4, todo5, todo6, todo7):
        pass

    def setCogDistances(self, todo0):
        pass

    def setHighScore(self, todo0, todo1):
        pass

