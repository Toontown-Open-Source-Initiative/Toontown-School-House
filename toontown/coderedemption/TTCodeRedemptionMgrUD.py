from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectUD import DistributedObjectUD

class TTCodeRedemptionMgrUD(DistributedObjectUD):
    notify = DirectNotifyGlobal.directNotify.newCategory("TTCodeRedemptionMgrUD")

    def giveAwardToToonResult(self, todo0, todo1):
        pass

    def redeemCode(self, todo0, todo1):
        pass

    def redeemCodeAiToUd(self, todo0, todo1, todo2, todo3, todo4):
        pass

    def redeemCodeResultUdToAi(self, todo0, todo1, todo2, todo3, todo4):
        pass

    def redeemCodeResult(self, todo0, todo1, todo2):
        pass

