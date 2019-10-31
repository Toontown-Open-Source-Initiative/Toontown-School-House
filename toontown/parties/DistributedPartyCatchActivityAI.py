from direct.directnotify import DirectNotifyGlobal
from toontown.parties.DistributedPartyActivityAI import DistributedPartyActivityAI

class DistributedPartyCatchActivityAI(DistributedPartyActivityAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedPartyCatchActivityAI")

    def setStartTimestamp(self, todo0):
        pass

    def setGenerations(self, todo0):
        pass

    def requestActivityStart(self):
        pass

    def startRequestResponse(self, todo0):
        pass

    def claimCatch(self, todo0, todo1, todo2):
        pass

    def setObjectCaught(self, todo0, todo1, todo2):
        pass

