from toontown.cogdominium.CogdoCraneGameConsts import SpotlightObstacleWait
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal
from random import randint

class DistCogdoCraneObstacleAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistCogdoCraneObstacleAI')

    def __init__(self, air, craneGame):
        DistributedObjectAI.__init__(self, air)
        self.craneGame = craneGame

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)
        taskMgr.doMethodLater(CogdoCraneGameConsts.SpotlightObstacleWait, self.determineBasePointTask, 'determine_base_point')

    def determineBasePointTask(self, task):
        self.determineBasePoint(randint(0, 3))
        return task.again

    def determineBasePoint(self, point):
        self.sendUpdate('determineBasePoint', [point])

    def requestFreeCrane(self):
        avId = self.air.getAvatarIdFromSender()
        for crane in self.craneGame._cranes:
            crane.removeToon(avId)

    def requestDelete(self):
        taskMgr.remove('determine_base_point')
        DistributedObjectAI.requestDelete(self)