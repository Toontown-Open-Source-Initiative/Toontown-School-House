from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class DistributedPartyAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedPartyAI")

    def setPartyClockInfo(self, todo0, todo1, todo2):
        pass

    def setInviteeIds(self, todo0):
        pass

    def setPartyState(self, todo0):
        pass

    def setPartyInfoTuple(self, todo0):
        pass

    def setAvIdsAtParty(self, todo0):
        pass

    def setPartyStartedTime(self, todo0):
        pass

    def setHostName(self, todo0):
        pass

    def avIdEnteredParty(self, todo0):
        pass

