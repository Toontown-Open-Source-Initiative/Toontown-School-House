from panda3d.core import *
from direct.distributed import DistributedObjectAI
from toontown.toonbase import ToontownGlobals
from otp.otpbase import OTPGlobals
from direct.fsm import FSM

class DistCogdoCraneAI(DistributedObjectAI.DistributedObjectAI, FSM.FSM):

    def __init__(self, air, craneGame, index):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)
        FSM.FSM.__init__(self, 'DistCogdoCraneAI')
        self.craneGame = craneGame
        self.index = index
        self.avId = 0
        self.objectId = 0

    def getCraneGameId(self):
        return self.craneGame.doId

    def getIndex(self):
        return self.index

    def generate(self):
        DistributedObjectAI.DistributedObjectAI.generate(self)
        self.request('Free')

    def d_setState(self, state, avId):
        self.sendUpdate('setState', [
            state,
            avId])

    def requestControl(self):
        avId = self.air.getAvatarIdFromSender()
        if self.avId == 0:
            craneId = self.__getCraneId(avId)
            if craneId == 0:
                self.request('Controlled', avId)

    def requestFree(self):
        avId = self.air.getAvatarIdFromSender()
        if avId == self.avId:
            self.request('Free')

    def removeToon(self, avId):
        if avId == self.avId:
            self.request('Free')

    def __getCraneId(self, avId):
        if self.craneGame and self.craneGame._cranes != None:
            for crane in self.craneGame._cranes:
                if crane.avId == avId:
                    return crane.doId

        return 0

    def enterOff(self):
        pass

    def exitOff(self):
        pass

    def enterControlled(self, avId):
        self.avId = avId
        self.d_setState('C', avId)

    def exitControlled(self):
        if self.objectId:
            obj = self.air.doId2do[self.objectId]
            obj.request('Dropped', self.avId, self.doId)

    def enterFree(self):
        self.avId = 0
        self.d_setState('F', 0)

    def exitFree(self):
        pass
