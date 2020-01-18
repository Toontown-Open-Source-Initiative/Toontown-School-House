from toontown.toonbase import TTLocalizer, ToontownGlobals
import copy

BOARDCODE_OKAY = 1
BOARDCODE_MISSING = 0
BOARDCODE_MINLAFF = -1
BOARDCODE_PROMOTION = -2
BOARDCODE_BATTLE = -3
BOARDCODE_SPACE = -4
BOARDCODE_NOT_PAID = -5
BOARDCODE_DIFF_GROUP = -6
BOARDCODE_PENDING_INVITE = -7
BOARDCODE_IN_ELEVATOR = -8
INVITE_ACCEPT_FAIL_GROUP_FULL = -1

LaffLimits = ToontownGlobals.FactoryLaffMinimums

# [Destination name, laff limit, required dept promotion (-1 if not required), groupSize,
# loader, where, how, interiorIdName, interiorId] (These last few are used for the loading process;
# refer to setDestinationZoneForce() in DistributedBoardingParty.)
DestinationData = [[TTLocalizer.ElevatorSellBotFactory0, LaffLimits[0][0], -1, 4, 'cogHQLoader', 'factoryInterior',
                    'teleportIn', '', 0],
                   [TTLocalizer.ElevatorSellBotFactory1, LaffLimits[0][1], -1, 4, 'cogHQLoader', 'factoryInterior',
                    'teleportIn', '', 0],
                   [TTLocalizer.ElevatorCashBotMint0, LaffLimits[1][0], -1, 4, 'cogHQLoader', 'mintInterior',
                    'teleportIn', 'mintId', ToontownGlobals.CashbotMintIntA],
                   [TTLocalizer.ElevatorCashBotMint1, LaffLimits[1][1], -1, 4, 'cogHQLoader', 'mintInterior',
                    'teleportIn', 'mintId', ToontownGlobals.CashbotMintIntB],
                   [TTLocalizer.ElevatorCashBotMint2, LaffLimits[1][2], -1, 4, 'cogHQLoader', 'mintInterior',
                    'teleportIn', 'mintId', ToontownGlobals.CashbotMintIntC],
                   [TTLocalizer.ElevatorLawBotCourse0, LaffLimits[2][0], -1, 4, 'cogHQLoader', 'stageInterior',
                    'teleportIn', 'stageId', ToontownGlobals.LawbotStageIntA],
                   [TTLocalizer.ElevatorLawBotCourse1, LaffLimits[2][1], -1, 4, 'cogHQLoader', 'stageInterior',
                    'teleportIn', 'stageId', ToontownGlobals.LawbotStageIntB],
                   [TTLocalizer.ElevatorLawBotCourse2, LaffLimits[2][2], -1, 4, 'cogHQLoader', 'stageInterior',
                    'teleportIn', 'stageId', ToontownGlobals.LawbotStageIntC],
                   [TTLocalizer.ElevatorLawBotCourse3, LaffLimits[2][3], -1, 4, 'cogHQLoader', 'stageInterior',
                    'teleportIn', 'stageId', ToontownGlobals.LawbotStageIntD],
                   [TTLocalizer.ElevatorBossBotCourse0, LaffLimits[3][0], -1, 4, 'cogHQLoader', 'countryClubInterior',
                    'teleportIn', 'countryClubId', ToontownGlobals.BossbotCountryClubIntA],
                   [TTLocalizer.ElevatorBossBotCourse1, LaffLimits[3][1], -1, 4, 'cogHQLoader', 'countryClubInterior',
                    'teleportIn', 'countryClubId', ToontownGlobals.BossbotCountryClubIntB],
                   [TTLocalizer.ElevatorBossBotCourse2, LaffLimits[3][2], -1, 4, 'cogHQLoader', 'countryClubInterior',
                    'teleportIn', 'countryClubId', ToontownGlobals.BossbotCountryClubIntC],
                   [TTLocalizer.ElevatorSellBotBoss, 0, 3, 8, 'cogHQLoader', 'cogHQBossBattle', 'movie', '', 0],
                   [TTLocalizer.ElevatorCashBotBoss, 0, 2, 8, 'cogHQLoader', 'cogHQBossBattle', 'movie', '', 0],
                   [TTLocalizer.ElevatorLawBotBoss, 0, 1, 8, 'cogHQLoader', 'cogHQBossBattle', 'movie', '', 0],
                   [TTLocalizer.ElevatorBossBotBoss, 0, 0, 8, 'cogHQLoader', 'cogHQBossBattle', 'movie', '', 0]]


class BoardingPartyBase:

    def __init__(self):
        self.groupListDict = {}
        self.avIdDict = {}
        self.currentDestinationData = DestinationData[0]

    def cleanup(self):
        del self.groupListDict
        del self.avIdDict
        del self.currentDestinationData

    def getGroupSize(self):
        return self.maxSize

    def setGroupSize(self, groupSize):
        self.maxSize = groupSize

    def getRequiredDept(self):
        return self.requiredDept

    def setRequiredDept(self, dept):
        self.requiredDept = dept

    def getGroupLeader(self, avatarId):
        if avatarId in self.avIdDict:
            leaderId = self.avIdDict[avatarId]
            return leaderId
        else:
            return None

    def isGroupLeader(self, avatarId):
        leaderId = self.getGroupLeader(avatarId)
        if avatarId == leaderId:
            return True
        else:
            return False

    def getGroupMemberList(self, avatarId):
        if avatarId in self.avIdDict:
            leaderId = self.avIdDict[avatarId]
            group = self.groupListDict.get(leaderId)
            if group:
                returnList = copy.copy(group[0])
                if 0 in returnList:
                    returnList.remove(0)
                return returnList
        return []

    def getGroupInviteList(self, avatarId):
        if avatarId in self.avIdDict:
            leaderId = self.avIdDict[avatarId]
            group = self.groupListDict.get(leaderId)
            if group:
                returnList = copy.copy(group[1])
                if 0 in returnList:
                    returnList.remove(0)
                return returnList
        return []

    def getGroupKickList(self, avatarId):
        if avatarId in self.avIdDict:
            leaderId = self.avIdDict[avatarId]
            group = self.groupListDict.get(leaderId)
            if group:
                returnList = copy.copy(group[2])
                if 0 in returnList:
                    returnList.remove(0)
                return returnList
        return []

    def hasActiveGroup(self, avatarId):
        memberList = self.getGroupMemberList(avatarId)
        if avatarId in memberList:
            if len(memberList) > 1:
                return True
        return False

    def hasPendingInvite(self, avatarId):
        pendingInvite = False
        if avatarId in self.avIdDict:
            leaderId = self.avIdDict[avatarId]
            leaderInviteList = self.getGroupInviteList(leaderId)
            if leaderId == avatarId:
                if len(leaderInviteList):
                    pendingInvite = True
                else:
                    pendingInvite = False
            elif avatarId in leaderInviteList:
                pendingInvite = True
            else:
                pendingInvite = False
        if pendingInvite:
            return True
        else:
            return False

    def isInGroup(self, memberId, leaderId):
        if memberId in self.getGroupMemberList(leaderId) or memberId in self.getGroupInviteList(leaderId):
            return True
        else:
            return False
