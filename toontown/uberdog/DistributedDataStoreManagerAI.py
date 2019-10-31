from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class DistributedDataStoreManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedDataStoreManagerAI")

    def startStore(self, todo0):
        pass

    def stopStore(self, todo0):
        pass

    def queryStore(self, todo0, todo1):
        pass

    def receiveResults(self, todo0, todo1):
        pass

    def deleteBackupStores(self):
        pass

