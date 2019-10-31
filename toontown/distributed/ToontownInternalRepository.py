from direct.directnotify import DirectNotifyGlobal
from direct.distributed.AstronInternalRepository import AstronInternalRepository
from direct.distributed.PyDatagram import PyDatagram

from otp.distributed.OtpDoGlobals import *


class ToontownInternalRepository(AstronInternalRepository):
    notify = DirectNotifyGlobal.directNotify.newCategory('ToontownInternalRepository')
    GameGlobalsId = OTP_DO_ID_TOONTOWN
    dbId = 4003

    def __init__(self, baseChannel, serverId=None, dcFileNames=None, dcSuffix='AI', connectMethod=None,
                 threadedNet=None):
        AstronInternalRepository.__init__(self, baseChannel, serverId, dcFileNames, dcSuffix, connectMethod,
                                          threadedNet)

    def getAvatarIdFromSender(self):
        return self.getMsgSender() & 0xFFFFFFFF

    def getAccountIdFromSender(self):
        return (self.getMsgSender() >> 32) & 0xFFFFFFFF

    def _isValidPlayerLocation(self, parentId, zoneId):
        if zoneId < 1000 and zoneId != 1:
            return False

        return True

    def setAllowClientSend(self, avId, distObj, fieldNameList=[]):
        dg = PyDatagram()
        dg.addServerHeader(distObj.GetPuppetConnectionChannel(avId), self.ourChannel, CLIENTAGENT_SET_FIELDS_SENDABLE)
        fieldIds = []
        for fieldName in fieldNameList:
            field = distObj.dclass.getFieldByName(fieldName)
            if field:
                fieldIds.append(field.getNumber())

        dg.addUint32(distObj.getDoId())
        dg.addUint16(len(fieldIds))
        for fieldId in fieldIds:
            dg.addUint16(fieldId)

        self.send(dg)
