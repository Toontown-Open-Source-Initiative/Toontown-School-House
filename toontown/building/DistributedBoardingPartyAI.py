from otp.ai.AIBase import *
from ElevatorConstants import *
from direct.distributed import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal
from toontown.building import BoardingPartyBase
from toontown.suit.SuitDNA import suitDepts
GROUPMEMBER = 0
GROUPINVITE = 1


class DistributedBoardingPartyAI(DistributedObjectAI.DistributedObjectAI, BoardingPartyBase.BoardingPartyBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBoardingPartyAI')

    def __init__(self, air, maxSize=4, requiredDept=-1):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)
        BoardingPartyBase.BoardingPartyBase.__init__(self)
        self.setGroupSize(maxSize)
        # Boarding requires a promotion in this cog dept (if a valid dept)
        self.setRequiredDept(requiredDept)

    def delete(self):
        self.cleanup()
        DistributedObjectAI.DistributedObjectAI.delete(self)

    def generate(self):
        DistributedObjectAI.DistributedObjectAI.generate(self)

    def cleanup(self):
        BoardingPartyBase.BoardingPartyBase.cleanup(self)

    def addWatchAvStatus(self, avId):
        self.acceptOnce(self.air.getAvatarExitEvent(avId), self.handleAvatarDisco, extraArgs=[avId])
        messageToonAdded = 'Battle adding toon %s' % avId
        self.accept(messageToonAdded, self.handleToonJoinedBattle)
        messageToonReleased = 'Battle releasing toon %s' % avId
        self.accept(messageToonReleased, self.handleToonLeftBattle)

    def handleToonJoinedBattle(self, avId):
        self.notify.debug('handleToonJoinedBattle %s' % avId)

    def handleToonLeftBattle(self, avId):
        self.notify.debug('handleToonLeftBattle %s' % avId)

    def removeWatchAvStatus(self, avId):
        self.ignore(self.air.getAvatarExitEvent(avId))

    def requestInvite(self, inviteeId):
        self.notify.debug('requestInvite %s' % inviteeId)
        inviterId = self.air.getAvatarIdFromSender()
        invitee = simbase.air.doId2do.get(inviteeId)
        if invitee and invitee.battleId != 0:
            reason = BoardingPartyBase.BOARDCODE_BATTLE
            self.sendUpdateToAvatarId(inviterId, 'postInviteNotQualify', [inviteeId, reason, 0])
            self.sendUpdateToAvatarId(inviteeId, 'postMessageInvitationFailed', [inviterId])
            return
        elif self.hasActiveGroup(inviteeId):
            reason = BoardingPartyBase.BOARDCODE_DIFF_GROUP
            self.sendUpdateToAvatarId(inviterId, 'postInviteNotQualify', [inviteeId, reason, 0])
            self.sendUpdateToAvatarId(inviteeId, 'postMessageInvitationFailed', [inviterId])
            return
        elif self.hasPendingInvite(inviteeId):
            reason = BoardingPartyBase.BOARDCODE_PENDING_INVITE
            self.sendUpdateToAvatarId(inviterId, 'postInviteNotQualify', [inviteeId, reason, 0])
            self.sendUpdateToAvatarId(inviteeId, 'postMessageInvitationFailed', [inviterId])
            return
        elif self.__isInElevator(inviteeId):
            reason = BoardingPartyBase.BOARDCODE_IN_ELEVATOR
            self.sendUpdateToAvatarId(inviterId, 'postInviteNotQualify', [inviteeId, reason, 0])
            self.sendUpdateToAvatarId(inviteeId, 'postMessageInvitationFailed', [inviterId])
            return
        inviterOkay = self.checkBoard(inviterId)
        reason = 0
        if inviterOkay:
            if inviterOkay == REJECT_MINLAFF:
                reason = BoardingPartyBase.BOARDCODE_MINLAFF
            elif inviterOkay == REJECT_PROMOTION:
                reason = BoardingPartyBase.BOARDCODE_PROMOTION
            self.sendUpdateToAvatarId(inviterId, 'postInviteNotQualify', [inviterId, reason])
            return
        else:
            inviteeOkay = self.checkBoard(inviteeId)
            if inviteeOkay:
                if inviteeOkay == REJECT_MINLAFF:
                    reason = BoardingPartyBase.BOARDCODE_MINLAFF
                elif inviteeOkay == REJECT_PROMOTION:
                    reason = BoardingPartyBase.BOARDCODE_PROMOTION
                self.sendUpdateToAvatarId(inviterId, 'postInviteNotQualify', [inviteeId, reason])
                return
        if inviterId in self.avIdDict:
            self.notify.debug('old group')
            leaderId = self.avIdDict[inviterId]
            groupList = self.groupListDict.get(leaderId)
            if groupList:
                self.notify.debug('got group list')
                if inviterId == leaderId:
                    if inviteeId in groupList[2]:
                        groupList[2].remove(inviteeId)
                if len(self.getGroupMemberList(leaderId)) >= self.maxSize:
                    self.sendUpdate('postSizeReject', [inviteeId])
                elif inviterId not in groupList[1] and inviterId not in groupList[2]:
                    if inviteeId not in groupList[1]:
                        groupList[1].append(inviteeId)
                    self.groupListDict[leaderId] = groupList
                    if inviteeId in self.avIdDict:
                        self.notify.warning('inviter %s tried to invite %s who already exists in the avIdDict.' % (inviterId, inviteeId))
                        self.air.writeServerEvent('suspicious: inviter', inviterId,
                                                  ' tried to invite %s who already exists in the avIdDict.' % inviteeId)
                    self.avIdDict[inviteeId] = leaderId
                    self.sendUpdateToAvatarId(inviteeId, 'postInvite', [leaderId, inviterId])
                    for memberId in groupList[0]:
                        if not memberId == inviterId:
                            self.sendUpdateToAvatarId(memberId, 'postMessageInvited', [inviteeId, inviterId])

                elif inviterId in groupList[2]:
                    self.sendUpdate('postKickReject', [leaderId, inviteeId])
        else:
            if inviteeId in self.avIdDict:
                self.notify.warning('inviter %s tried to invite %s who already exists in avIdDict.' % (inviterId, inviteeId))
                self.air.writeServerEvent('suspicious: inviter', inviterId,
                                          ' tried to invite %s who already exists in the avIdDict.' % inviteeId)
            self.notify.debug('new group')
            leaderId = inviterId
            self.avIdDict[inviterId] = inviterId
            self.avIdDict[inviteeId] = inviterId
            self.groupListDict[leaderId] = [[leaderId], [inviteeId], []]
            self.addWatchAvStatus(leaderId)
            self.sendUpdateToAvatarId(inviteeId, 'postInvite', [leaderId, inviterId])

    def requestCancelInvite(self, inviteeId):
        inviterId = self.air.getAvatarIdFromSender()
        if inviterId in self.avIdDict:
            leaderId = self.avIdDict[inviterId]
            groupList = self.groupListDict.get(leaderId)
            if groupList:
                self.removeFromGroup(leaderId, inviteeId)
                self.sendUpdateToAvatarId(inviteeId, 'postInviteCanceled', [])

    def requestAcceptInvite(self, leaderId, inviterId):
        inviteeId = self.air.getAvatarIdFromSender()
        self.notify.debug('requestAcceptInvite leader%s inviter%s invitee%s' % (leaderId, inviterId, inviteeId))
        if inviteeId in self.avIdDict:
            if self.hasActiveGroup(inviteeId):
                self.sendUpdateToAvatarId(inviteeId, 'postAlreadyInGroup', [])
                return
            if leaderId not in self.avIdDict or not self.isInGroup(inviteeId, leaderId):
                self.sendUpdateToAvatarId(inviteeId, 'postSomethingMissing', [])
                return
            memberList = self.getGroupMemberList(leaderId)
            if self.avIdDict[inviteeId]:
                if self.avIdDict[inviteeId] == leaderId:
                    if inviteeId in memberList:
                        self.notify.debug('invitee already in group, aborting requestAcceptInvite')
                        return
                else:
                    self.air.writeServerEvent('suspicious: ', inviteeId,
                                              " accepted a second invite from %s, in %s's group,"
                                              "while he was in already in %s's group." % (inviterId, leaderId,
                                                                                          self.avIdDict[inviteeId]))
                    self.removeFromGroup(self.avIdDict[inviteeId], inviteeId, post=0)
            if len(memberList) >= self.maxSize:
                self.removeFromGroup(leaderId, inviteeId)
                self.sendUpdateToAvatarId(inviterId, 'postMessageAcceptanceFailed',
                                          [inviteeId, BoardingPartyBase.INVITE_ACCEPT_FAIL_GROUP_FULL])
                self.sendUpdateToAvatarId(inviteeId, 'postGroupAlreadyFull', [])
                return
            self.sendUpdateToAvatarId(inviterId, 'postInviteAccepted', [inviteeId])
            self.addToGroup(leaderId, inviteeId)
        else:
            self.air.writeServerEvent('suspicious: ', inviteeId,
                                      " was invited to %s's group by %s,"
                                      "but the invitee didn't have an entry in the avIdDict." % (leaderId, inviterId))

    def requestRejectInvite(self, leaderId, inviterId):
        inviteeId = self.air.getAvatarIdFromSender()
        self.removeFromGroup(leaderId, inviteeId)
        self.sendUpdateToAvatarId(inviterId, 'postInviteDeclined', [inviteeId])

    def requestKick(self, kickId):
        leaderId = self.air.getAvatarIdFromSender()
        if kickId in self.avIdDict:
            if self.avIdDict[kickId] == leaderId:
                self.removeFromGroup(leaderId, kickId, kick=1)
                self.sendUpdateToAvatarId(kickId, 'postKick', [leaderId])

    def requestLeave(self, leaderId):
        memberId = self.air.getAvatarIdFromSender()
        if memberId in self.avIdDict:
            if leaderId == self.avIdDict[memberId]:
                self.removeFromGroup(leaderId, memberId)

    def checkBoard(self, avId):
        avatar = simbase.air.doId2do.get(avId)
        if avatar:
            if avatar.getHp() <= self.currentDestinationData[1]:
                return REJECT_MINLAFF
            elif self.requiredDept in range(0, len(suitDepts) - 1):
                if not avatar.readyForPromotion(self.requiredDept):
                    return REJECT_PROMOTION

    def testBoard(self, leaderId):
        boardOkay = BoardingPartyBase.BOARDCODE_MISSING
        avatarsFailingRequirements = []
        avatarsInBattle = []
        if leaderId in self.avIdDict:
            if leaderId == self.avIdDict[leaderId]:
                boardOkay = BoardingPartyBase.BOARDCODE_OKAY
                for avId in self.getGroupMemberList(leaderId):
                    avatar = simbase.air.doId2do.get(avId)
                    if avatar:
                        if self.checkBoard(avatar):
                            if self.checkBoard(avatar) == REJECT_MINLAFF:
                                boardOkay = BoardingPartyBase.BOARDCODE_MINLAFF
                            else:
                                if self.checkBoard(avatar) == REJECT_PROMOTION:
                                    boardOkay = BoardingPartyBase.BOARDCODE_PROMOTION
                            avatarsFailingRequirements.append(avId)
                        elif avatar.battleId != 0:
                            boardOkay = BoardingPartyBase.BOARDCODE_BATTLE
                            avatarsInBattle.append(avId)

                groupSize = len(self.getGroupMemberList(leaderId))
                if groupSize > self.maxSize:
                    boardOkay = BoardingPartyBase.BOARDCODE_SPACE
        if boardOkay != BoardingPartyBase.BOARDCODE_OKAY:
            self.notify.debug('Something is wrong with the group board request')
            if boardOkay == BoardingPartyBase.BOARDCODE_MINLAFF:
                self.notify.debug('An avatar did not meet the elevator laff requirements')
            if boardOkay == BoardingPartyBase.BOARDCODE_PROMOTION:
                self.notify.debug('An avatar did not meet the elevator promotion requirements')
            elif boardOkay == BoardingPartyBase.BOARDCODE_BATTLE:
                self.notify.debug('An avatar is in battle')
        return boardOkay, avatarsFailingRequirements, avatarsInBattle

    def testGoButtonRequirements(self, leaderId):
        if leaderId in self.avIdDict:
            if leaderId == self.avIdDict[leaderId]:
                    boardOkay, avatarsFailingRequirements, avatarsInBattle = self.testBoard(leaderId)
                    if boardOkay == BoardingPartyBase.BOARDCODE_OKAY:
                        avList = self.getGroupMemberList(leaderId)
                        if 0 in avList:
                            avList.remove(0)
                        if not self.__isInElevator(leaderId):
                            return True
                        else:
                            self.notify.warning('avId: %s has hacked his/her client.' % leaderId)
                            self.air.writeServerEvent('suspicious: ', leaderId,
                                                      ' pressed the GO Button while inside the elevator.')
                    else:
                        self.sendUpdateToAvatarId(leaderId, 'rejectGoToRequest',
                                                  [boardOkay, avatarsFailingRequirements, avatarsInBattle])
        return False

    def requestGoToFirstTime(self):
        callerId = self.air.getAvatarIdFromSender()
        if self.testGoButtonRequirements(callerId):
            self.sendUpdateToAvatarId(callerId, 'acceptGoToFirstTime', [])

    def requestGoToSecondTime(self):
        callerId = self.air.getAvatarIdFromSender()
        avList = self.getGroupMemberList(callerId)
        if self.testGoButtonRequirements(callerId):
            for avId in avList:
                self.sendUpdateToAvatarId(avId, 'acceptGoToSecondTime', [])

            THREE_SECONDS = 3.0
            taskMgr.doMethodLater(THREE_SECONDS, self.sendAvatarsToDestinationTask,
                                  self.uniqueName('sendAvatarsToDestinationTask'), extraArgs=[avList], appendTask=True)

    def sendAvatarsToDestinationTask(self, avList, task):
        self.notify.debug('entering sendAvatarsToDestinationTask')
        if len(avList):
            self.notify.warning('Sending avatars %s' % avList)
            boardOkay, avatarsFailingRequirements, avatarsInBattle = self.testBoard(avList[0])
            if not boardOkay == BoardingPartyBase.BOARDCODE_OKAY:
                for avId in avatarsFailingRequirements:
                    self.air.writeServerEvent('suspicious: ',
                                              avId, ' failed requirements after the second go button request.')

                for avId in avatarsInBattle:
                    self.air.writeServerEvent('suspicious: ',
                                              avId, ' joined battle after the second go button request.')

            self.air.writeServerEvent('boarding', self.zoneId, 'Sending avatars %s' % avList)
            self.sendAvatarsToDestination(avList)
        return task.done

    def sendAvatarsToDestination(self, avList):
        if len(avList) > 0:
            for av in avList:
                if av:
                    self.sendUpdateToAvatarId(av.doId, 'setDestinationZoneForce', [self.zoneId])

    def handleAvatarDisco(self, avId):
        self.notify.debug('handleAvatarDisco %s' % avId)
        if avId in self.avIdDict:
            leaderId = self.avIdDict[avId]
            self.removeFromGroup(leaderId, avId)

    def addToGroup(self, leaderId, inviteeId, post=1):
        group = self.groupListDict.get(leaderId)
        if group:
            self.avIdDict[inviteeId] = leaderId
            if inviteeId in group[1]:
                group[1].remove(inviteeId)
            if inviteeId not in group[0]:
                group[0].append(inviteeId)
            self.groupListDict[leaderId] = group
            if post:
                self.notify.debug('Calling postGroupInfo from addToGroup')
                self.sendUpdate('postGroupInfo', [leaderId, group[0], group[1], group[2]])
            self.addWatchAvStatus(inviteeId)
        else:
            self.sendUpdate('postGroupDissolve', [leaderId, leaderId, [], 0])

    def removeFromGroup(self, leaderId, memberId, kick=0, post=1):
        self.notify.debug('')
        self.notify.debug('removeFromGroup leaderId %s memberId %s' % (leaderId, memberId))
        self.notify.debug('Groups %s' % self.groupListDict)
        self.notify.debug('avDict %s' % self.avIdDict)
        if leaderId not in self.avIdDict:
            self.sendUpdate('postGroupDissolve', [memberId, leaderId, [], kick])
            if memberId in self.avIdDict:
                self.avIdDict.pop(memberId)
            return
        self.removeWatchAvStatus(memberId)
        group = self.groupListDict.get(leaderId)
        if group:
            if memberId in group[0]:
                group[0].remove(memberId)
            if memberId in group[1]:
                group[1].remove(memberId)
            if memberId in group[2]:
                group[2].remove(memberId)
            if kick:
                group[2].append(memberId)
        else:
            return
        if memberId == leaderId or len(group[0]) < 2:
            if leaderId in self.avIdDict:
                self.avIdDict.pop(leaderId)
                for inviteeId in group[1]:
                    if inviteeId in self.avIdDict:
                        self.avIdDict.pop(inviteeId)
                        self.sendUpdateToAvatarId(inviteeId, 'postInviteCanceled', [])

            dgroup = self.groupListDict.pop(leaderId)
            for dMemberId in dgroup[0]:
                if dMemberId in self.avIdDict:
                    self.avIdDict.pop(dMemberId)

            self.notify.debug('postGroupDissolve')
            dgroup[0].insert(0, memberId)
            self.sendUpdate('postGroupDissolve', [memberId, leaderId, dgroup[0], kick])
        else:
            self.groupListDict[leaderId] = group
            if post:
                self.notify.debug('Calling postGroupInfo from removeFromGroup')
                self.sendUpdate('postGroupInfo', [leaderId, group[0], group[1], group[2]])
        if memberId in self.avIdDict:
            self.avIdDict.pop(memberId)
        self.notify.debug('Remove from group END')
        self.notify.debug('Groups %s' % self.groupListDict)
        self.notify.debug('avDict %s' % self.avIdDict)
        self.notify.debug('')

    def informDestinationInfo(self, offset):
        leaderId = self.air.getAvatarIdFromSender()
        memberList = self.getGroupMemberList(leaderId)
        self.currentDestinationData = BoardingPartyBase.DestinationData[offset]
        self.setGroupSize(self.currentDestinationData[3])
        self.setRequiredDept(self.currentDestinationData[2])
        for avId in memberList:
            if avId != leaderId:
                self.sendUpdateToAvatarId(avId, 'postDestinationInfo', [offset])

    def __isInElevator(self, avId):
        import DistributedElevatorAI
        import DistributedElevatorFSMAI
        inElevator = False
        for do in simbase.air.doId2do:
            if isinstance(do, DistributedElevatorAI.DistributedElevatorAI)\
                    or isinstance(do, DistributedElevatorFSMAI.DistributedElevatorFSMAI):
                if avId in do.seats:
                    inElevator = True

        return inElevator
