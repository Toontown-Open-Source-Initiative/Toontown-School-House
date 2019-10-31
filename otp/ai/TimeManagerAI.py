import time

from direct.directnotify import DirectNotifyGlobal
from direct.distributed.ClockDelta import globalClockDelta
from direct.distributed.DistributedObjectAI import DistributedObjectAI

from otp.otpbase import OTPGlobals


class TimeManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('TimeManagerAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.avId2disconnectcode = {}
        self.avId2exceptioninfo = {}

    def requestServerTime(self, context):
        avId = self.air.getAvatarIdFromSender()
        if not avId:
            return

        self.sendUpdateToAvatarId(avId, 'serverTime',
                                  [context, globalClockDelta.getRealNetworkTime(bits=32), int(time.time())])

    def setDisconnectReason(self, disconnectCode):
        avId = self.air.getAvatarIdFromSender()
        if not avId:
            return

        self.avId2disconnectcode[avId] = disconnectCode
        self.air.writeServerEvent('disconnect-reason', avId=avId,
                                  reason=OTPGlobals.DisconnectReasons.get(disconnectCode, 'unknown'))

    def setExceptionInfo(self, info):
        avId = self.air.getAvatarIdFromSender()
        if not avId:
            return

        self.avId2exceptioninfo[avId] = info
        self.air.writeServerEvent('client-exception', avId=avId, info=info)

    def setSignature(self, todo0, todo1, todo2):
        pass

    def setFrameRate(self, todo0, todo1, todo2, todo3, todo4, todo5, todo6, todo7, todo8, todo9, todo10, todo11, todo12,
                     todo13, todo14, todo15, todo16, todo17):
        pass

    def setCpuInfo(self, todo0, todo1):
        pass

    def checkForGarbageLeaks(self, todo0):
        pass

    def setClientGarbageLeak(self, todo0, todo1):
        pass

    def checkAvOnDistrict(self, todo0, todo1):
        pass
