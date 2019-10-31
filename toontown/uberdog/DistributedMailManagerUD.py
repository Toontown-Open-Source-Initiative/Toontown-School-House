from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectUD import DistributedObjectUD

class DistributedMailManagerUD(DistributedObjectUD):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedMailManagerUD")

    def sendSimpleMail(self, todo0, todo1, todo2):
        pass

    def setNumMailItems(self, todo0, todo1):
        pass

