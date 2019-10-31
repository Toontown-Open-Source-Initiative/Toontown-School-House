from direct.directnotify import DirectNotifyGlobal
from toontown.parties.DistributedPartyActivityAI import DistributedPartyActivityAI

class DistributedPartyFireworksActivityAI(DistributedPartyActivityAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedPartyFireworksActivityAI")

    def setEventId(self, todo0):
        pass

    def setShowStyle(self, todo0):
        pass

