import time

from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

from toontown.toonbase import ToontownGlobals


class DistributedPolarPlaceEffectMgrAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPolarPlaceEffectMgrAI')

    def addPolarPlaceEffect(self):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)
        if not av:
            return

        if av.getCheesyEffect()[0] != ToontownGlobals.CEBigWhite:
            expireTime = int(time.time() / 60 + 0.5) + 3600
            av.b_setCheesyEffect(ToontownGlobals.CEBigWhite, ToontownGlobals.TheBrrrgh, expireTime)
