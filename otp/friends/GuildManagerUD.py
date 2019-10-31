from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectUD import DistributedObjectUD

class GuildManagerUD(DistributedObjectUD):
    notify = DirectNotifyGlobal.directNotify.newCategory("GuildManagerUD")

    def online(self):
        pass

    def guildRejectInvite(self, todo0, todo1):
        pass

    def invitationFrom(self, todo0, todo1, todo2, todo3):
        pass

    def requestInvite(self, todo0):
        pass

    def memberList(self):
        pass

    def createGuild(self):
        pass

    def acceptInvite(self):
        pass

    def declineInvite(self):
        pass

    def setWantName(self, todo0):
        pass

    def removeMember(self, todo0):
        pass

    def changeRank(self, todo0, todo1):
        pass

    def changeRankAvocate(self, todo0):
        pass

    def statusRequest(self):
        pass

    def requestLeaderboardTopTen(self):
        pass

    def guildStatusUpdate(self, todo0, todo1, todo2):
        pass

    def guildNameReject(self, todo0):
        pass

    def guildNameChange(self, todo0, todo1):
        pass

    def receiveMember(self, todo0):
        pass

    def receiveMembersDone(self):
        pass

    def guildAcceptInvite(self, todo0):
        pass

    def guildDeclineInvite(self, todo0):
        pass

    def updateRep(self, todo0, todo1):
        pass

    def leaderboardTopTen(self, todo0):
        pass

    def recvAvatarOnline(self, todo0, todo1, todo2, todo3):
        pass

    def recvAvatarOffline(self, todo0, todo1):
        pass

    def sendChat(self, todo0, todo1, todo2):
        pass

    def sendWLChat(self, todo0, todo1, todo2):
        pass

    def sendSC(self, todo0):
        pass

    def sendSCQuest(self, todo0, todo1, todo2):
        pass

    def recvChat(self, todo0, todo1, todo2, todo3):
        pass

    def recvWLChat(self, todo0, todo1, todo2, todo3):
        pass

    def recvSC(self, todo0, todo1):
        pass

    def recvSCQuest(self, todo0, todo1, todo2, todo3):
        pass

    def sendTokenRequest(self):
        pass

    def recvTokenGenerated(self, todo0):
        pass

    def recvTokenInviteValue(self, todo0, todo1):
        pass

    def sendTokenForJoinRequest(self, todo0, todo1):
        pass

    def recvTokenRedeemMessage(self, todo0):
        pass

    def recvTokenRedeemedByPlayerMessage(self, todo0):
        pass

    def sendTokenRValue(self, todo0, todo1):
        pass

    def sendPermToken(self):
        pass

    def sendNonPermTokenCount(self):
        pass

    def recvPermToken(self, todo0):
        pass

    def recvNonPermTokenCount(self, todo0):
        pass

    def sendClearTokens(self, todo0):
        pass

    def sendAvatarBandId(self, todo0, todo1, todo2):
        pass

    def recvMemberAdded(self, todo0, todo1, todo2):
        pass

    def notifyGuildKicksMaxed(self):
        pass

    def recvMemberRemoved(self, todo0, todo1, todo2, todo3):
        pass

    def recvMemberUpdateName(self, todo0, todo1):
        pass

    def recvMemberUpdateRank(self, todo0, todo1, todo2, todo3, todo4, todo5):
        pass

    def recvMemberUpdateBandId(self, todo0, todo1, todo2):
        pass

    def avatarOnline(self, todo0, todo1):
        pass

    def avatarOffline(self, todo0):
        pass

    def reflectTeleportQuery(self, todo0, todo1, todo2, todo3, todo4):
        pass

    def teleportQuery(self, todo0, todo1, todo2, todo3, todo4):
        pass

    def reflectTeleportResponse(self, todo0, todo1, todo2, todo3, todo4):
        pass

    def teleportResponse(self, todo0, todo1, todo2, todo3, todo4):
        pass

    def requestGuildMatesList(self, todo0, todo1, todo2):
        pass

    def updateAvatarName(self, todo0, todo1):
        pass

    def avatarDeleted(self, todo0):
        pass

