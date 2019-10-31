from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD


class DistributedDeliveryManagerUD(DistributedObjectGlobalUD):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedDeliveryManagerUD')

    def requestAck(self):
        avId = self.air.getAvatarIdFromSender()
        if not avId:
            return

        self.sendUpdateToAvatarId(avId, 'returnAck', [])
