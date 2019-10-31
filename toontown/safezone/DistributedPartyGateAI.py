from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class DistributedPartyGateAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedPartyGateAI")

    def getPartyList(self, todo0):
        pass

    def partyChoiceRequest(self, todo0, todo1, todo2):
        pass

    def listAllPublicParties(self, todo0):
        pass

    def partyRequestDenied(self, todo0):
        pass

    def setParty(self, todo0):
        pass

