from direct.directnotify import DirectNotifyGlobal
from toontown.parties.DistributedPartyActivityAI import DistributedPartyActivityAI

class DistributedPartyDanceActivityBaseAI(DistributedPartyActivityAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedPartyDanceActivityBaseAI")

    def updateDancingToon(self, todo0, todo1):
        pass

    def setToonsPlaying(self, todo0, todo1):
        pass

    def setDancingToonState(self, todo0, todo1, todo2):
        pass

