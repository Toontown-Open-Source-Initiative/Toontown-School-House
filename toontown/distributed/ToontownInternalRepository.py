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

    def handleConnected(self):
        self.netMessenger.register(0, 'avatarOnline')
        self.netMessenger.register(1, 'avatarOffline')

    def getAvatarIdFromSender(self):
        return self.getMsgSender() & 0xFFFFFFFF

    def getAccountIdFromSender(self):
        return (self.getMsgSender() >> 32) & 0xFFFFFFFF

    def _isValidPlayerLocation(self, parentId, zoneId):
        if zoneId < 1000 and zoneId != 1:
            return False

        return True

    def setAllowClientSend(self, avId, distObj, fieldNameList=[]):
        """
        Allow an AI to temporarily give a client 'clsend' privileges
        on a particular fields on a particular object.  This should
        be used on fields that are 'ownsend' by default. When you want
        to revoke these privileges, use clearAllowClientSend() to end
        these privileges.
        """
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

    def createDgUpdateToDoId(self, dclassName, fieldName, doId, args,
                             channelId=None):
        """
        channelId can be used as a recipient if you want to bypass the normal
        airecv, ownrecv, broadcast, etc.  If you don't include a channelId
        or if channelId == doId, then the normal broadcast options will
        be used.
        This is just like sendUpdateToDoId, but just returns
        the datagram instead of immediately sending it.
        """
        result = None

        dclass = self.dclassesByName.get(dclassName+self.dcSuffix)

        assert dclass is not None

        if channelId is None:
            channelId = doId

        if dclass is not None:
            dg = dclass.aiFormatUpdate(fieldName, doId, channelId, self.ourChannel, args)
            result = dg

        return result

    def sendUpdateToDoId(self, dclassName, fieldName, doId, args, channelId=None):
        """
        channelId can be used as a recipient if you want to bypass the normal
        airecv, ownrecv, broadcast, etc.  If you don't include a channelId
        or if channelId == doId, then the normal broadcast options will
        be used.

        See Also: def queryObjectField
        """
        dclass = self.dclassesByName.get(dclassName+self.dcSuffix)

        assert dclass is not None

        if channelId is None:
            channelId = doId

        if dclass is not None:
            dg = dclass.aiFormatUpdate(fieldName, doId, channelId, self.ourChannel, args)
            self.send(dg)

    def sendUpdateToGlobalDoId(self, dclassName, fieldName, doId, args):
        """
        Used for sending messages from an AI directly to an
        uber object.
        """
        dclass = self.dclassesByName.get(dclassName)
        assert dclass, 'dclass %s not found in DC files' % dclassName
        dg = dclass.aiFormatUpdate(fieldName, doId, doId, self.ourChannel, args)
        self.send(dg)

    def dispatchUpdateToDoId(self, dclassName, fieldName, doId, args, channelId=None):
        # dispatch immediately to local object if it's local, otherwise send
        # it over the wire
        obj = self.doId2do.get(doId)
        if obj is not None:
            assert obj.__class__.__name__ == (dclassName + self.dcSuffix)
            method = getattr(obj, fieldName)
            method(*args)
        else:
            self.sendUpdateToDoId(dclassName, fieldName, doId, args, channelId)

    def dispatchUpdateToGlobalDoId(self, dclassName, fieldName, doId, args):
        # dispatch immediately to local object if it's local, otherwise send
        # it over the wire
        obj = self.doId2do.get(doId)

        if obj is not None:
            assert obj.__class__.__name__ == dclassName
            method = getattr(obj, fieldName)
            method(*args)
        else:
            self.sendUpdateToGlobalDoId(dclassName, fieldName, doId, args)
