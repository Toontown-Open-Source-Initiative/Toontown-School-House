from direct.directnotify import DirectNotifyGlobal
from toontown.parties.DistributedPartyActivityAI import DistributedPartyActivityAI

class DistributedPartyTrampolineActivityAI(DistributedPartyActivityAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedPartyTrampolineActivityAI")

    def awardBeans(self, todo0, todo1):
        pass

    def setBestHeightInfo(self, todo0, todo1):
        pass

    def reportHeightInformation(self, todo0):
        pass

    def leaveTrampoline(self):
        pass

    def requestAnim(self, todo0):
        pass

    def requestAnimEcho(self, todo0):
        pass

    def removeBeans(self, todo0):
        pass

    def removeBeansEcho(self, todo0):
        pass

