from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class DistributedMailManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedMailManagerAI")

    def sendSimpleMail(self, todo0, todo1, todo2):
        pass

    def setNumMailItems(self, todo0, todo1):
        pass

