from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI


class DistributedPartyManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPartyManagerAI')

    def addParty(self, todo0, todo1, todo2, todo3, todo4, todo5, todo6, todo7, todo8, todo9):
        pass

    def addPartyRequest(self, todo0, todo1, todo2, todo3, todo4, todo5, todo6, todo7):
        pass

    def addPartyResponse(self, todo0, todo1):
        pass

    def addPartyResponseUdToAi(self, todo0, todo1, todo2):
        pass

    def markInviteAsReadButNotReplied(self, todo0, todo1):
        pass

    def respondToInvite(self, todo0, todo1, todo2, todo3, todo4):
        pass

    def respondToInviteResponse(self, todo0, todo1, todo2, todo3, todo4):
        pass

    def changePrivateRequest(self, todo0, todo1):
        pass

    def changePrivateRequestAiToUd(self, todo0, todo1, todo2):
        pass

    def changePrivateResponseUdToAi(self, todo0, todo1, todo2, todo3):
        pass

    def changePrivateResponse(self, todo0, todo1, todo2):
        pass

    def changePartyStatusRequest(self, todo0, todo1):
        pass

    def changePartyStatusRequestAiToUd(self, todo0, todo1, todo2):
        pass

    def changePartyStatusResponseUdToAi(self, todo0, todo1, todo2, todo3):
        pass

    def changePartyStatusResponse(self, todo0, todo1, todo2, todo3):
        pass

    def partyInfoOfHostRequestAiToUd(self, todo0, todo1):
        pass

    def partyInfoOfHostFailedResponseUdToAi(self, todo0):
        pass

    def partyInfoOfHostResponseUdToAi(self, todo0, todo1):
        pass

    def givePartyRefundResponse(self, todo0, todo1, todo2, todo3, todo4):
        pass

    def getPartyZone(self, todo0, todo1, todo2):
        pass

    def receivePartyZone(self, todo0, todo1, todo2):
        pass

    def freeZoneIdFromPlannedParty(self, todo0, todo1):
        pass

    def sendAvToPlayground(self, todo0, todo1):
        pass

    def exitParty(self, todo0):
        pass

    def removeGuest(self, todo0, todo1):
        pass

    def partyManagerAIStartingUp(self, todo0, todo1):
        pass

    def partyManagerAIGoingDown(self, todo0, todo1):
        pass

    def partyHasStartedAiToUd(self, todo0, todo1, todo2, todo3, todo4):
        pass

    def toonHasEnteredPartyAiToUd(self, todo0):
        pass

    def toonHasExitedPartyAiToUd(self, todo0):
        pass

    def partyHasFinishedUdToAllAi(self, todo0):
        pass

    def updateToPublicPartyInfoUdToAllAi(self, todo0, todo1, todo2, todo3, todo4, todo5, todo6, todo7, todo8):
        pass

    def updateToPublicPartyCountUdToAllAi(self, todo0, todo1):
        pass

    def requestShardIdZoneIdForHostId(self, todo0):
        pass

    def sendShardIdZoneIdToAvatar(self, todo0, todo1):
        pass

    def partyManagerUdStartingUp(self):
        pass

    def updateAllPartyInfoToUd(self, todo0, todo1, todo2, todo3, todo4, todo5, todo6, todo7, todo8):
        pass

    def forceCheckStart(self):
        pass

    def requestMw(self, todo0, todo1, todo2, todo3):
        pass

    def mwResponseUdToAllAi(self, todo0, todo1, todo2, todo3):
        pass

    def canBuyParties(self):
        return False
