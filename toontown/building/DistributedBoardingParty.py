from libotp import WhisperPopup
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import TTLocalizer
from direct.distributed import DistributedObject
from toontown.toon import GroupInvitee
from toontown.toon import GroupPanel
from toontown.toon import BoardingGroupInviterPanels
from toontown.building import BoardingPartyBase
from direct.interval.IntervalGlobal import *
import BoardingGroupShow


class DistributedBoardingParty(DistributedObject.DistributedObject, BoardingPartyBase.BoardingPartyBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBoardingParty')
    neverDisable = 1
    InvitationFailedTimeout = 60.0

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        BoardingPartyBase.BoardingPartyBase.__init__(self)
        self.groupInviteePanel = None
        self.groupPanel = None
        self.inviterPanels = BoardingGroupInviterPanels.BoardingGroupInviterPanels()
        self.lastInvitationFailedMessage = {}
        self.goToPreShowTrack = None
        self.goToShowTrack = None
        return

    def generate(self):
        DistributedObject.DistributedObject.generate(self)
        localAvatar.boardingParty = self

    def announceGenerate(self):
        DistributedObject.DistributedObject.announceGenerate(self)

    def delete(self):
        DistributedObject.DistributedObject.delete(self)

    def disable(self):
        self.finishGoToPreShowTrack()
        self.finishGoToShowTrack()
        self.forceCleanupInviteePanel()
        self.forceCleanupInviterPanels()
        self.inviterPanels = None
        if self.groupPanel:
            self.groupPanel.cleanup()
        self.groupPanel = None
        DistributedObject.DistributedObject.disable(self)
        BoardingPartyBase.BoardingPartyBase.cleanup(self)
        localAvatar.boardingParty = None
        self.lastInvitationFailedMessage = {}
        return

    def postGroupInfo(self, leaderId, memberList, inviteeList, kickedList):
        self.notify.debug('postgroupInfo')
        isMyGroup = 0
        removedMemberIdList = []
        if leaderId in self.groupListDict:
            oldGroupEntry = self.groupListDict[leaderId]
        else:
            oldGroupEntry = [[], [], []]
        oldMemberList = oldGroupEntry[0]
        newGroupEntry = [memberList, inviteeList, kickedList]
        self.groupListDict[leaderId] = newGroupEntry
        if not len(oldMemberList) == len(memberList):
            for oldMember in oldMemberList:
                if oldMember not in memberList:
                    if oldMember in self.avIdDict:
                        if self.avIdDict[oldMember] == leaderId:
                            self.avIdDict.pop(oldMember)
                            removedMemberIdList.append(oldMember)

        self.avIdDict[leaderId] = leaderId
        if leaderId == localAvatar.doId:
            isMyGroup = 1
        for memberId in memberList:
            self.avIdDict[memberId] = leaderId
            if memberId == localAvatar.doId:
                isMyGroup = 1

        if newGroupEntry[0] == [0] or not newGroupEntry[0]:
            dgroup = self.groupListDict.pop(leaderId)
            for memberId in dgroup[0]:
                if memberId in self.avIdDict:
                    self.avIdDict.pop(memberId)

        if isMyGroup:
            self.notify.debug('new info posted on my group')
            if not self.groupPanel:
                self.groupPanel = GroupPanel.GroupPanel(self)
            messenger.send('updateGroupStatus')
            for removedMemberId in removedMemberIdList:
                removedMember = base.cr.doId2do.get(removedMemberId)
                if not removedMember:
                    removedMember = base.cr.identifyFriend(removedMemberId)
                if removedMember:
                    removedMemberName = removedMember.name
                    messageText = TTLocalizer.BoardingMessageLeftGroup % removedMemberName
                    localAvatar.setSystemMessage(0, messageText, WhisperPopup.WTToontownBoardingGroup)

        elif localAvatar.doId in oldMemberList and localAvatar.doId not in memberList:
            messenger.send('updateGroupStatus')
            if self.groupPanel:
                self.groupPanel.cleanup()
            self.groupPanel = None
        else:
            self.notify.debug('new info posted on some other group')
        return

    def postInvite(self, leaderId, inviterId):
        self.notify.debug('post Invite')
        if not base.cr.avatarFriendsManager.checkIgnored(inviterId):
            inviter = base.cr.doId2do.get(inviterId)
            if inviter:
                if self.inviterPanels.isInvitingPanelUp() or self.inviterPanels.isInvitationRejectedPanelUp():
                    self.inviterPanels.forceCleanup()
                self.groupInviteePanel = GroupInvitee.GroupInvitee()
                self.groupInviteePanel.make(self, inviter, leaderId)
                if base.config.GetBool('reject-boarding-group-invites', 0):
                    self.groupInviteePanel.forceCleanup()
                    self.groupInviteePanel = None
        return

    def postKick(self, leaderId):
        self.notify.debug('%s was kicked out of the Boarding Group by %s' % (localAvatar.doId, leaderId))
        localAvatar.setSystemMessage(0, TTLocalizer.BoardingMessageKickedOut, WhisperPopup.WTToontownBoardingGroup)

    def postSizeReject(self, inviteeId):
        self.notify.debug('%s was not invited because the group is full' % inviteeId)

    def postKickReject(self, leaderId, inviteeId):
        self.notify.debug('%s was not invited because %s has kicked them from the group' % (inviteeId, leaderId))

    def postInviteDeclined(self, inviteeId):
        self.notify.debug("%s declined %s's Boarding Group invitation." % (inviteeId, localAvatar.doId))
        invitee = base.cr.doId2do.get(inviteeId)
        if invitee:
            self.inviterPanels.createInvitationRejectedPanel(self, inviteeId)

    def postInviteAccepted(self, inviteeId):
        self.notify.debug("%s accepted %s's Boarding Group invitation." % (inviteeId, localAvatar.doId))
        if self.inviterPanels.isInvitingPanelIdCorrect(inviteeId):
            self.inviterPanels.destroyInvitingPanel()

    def postInviteCanceled(self):
        self.notify.debug('The invitation to the Boarding Group was canceled')
        if self.isInviteePanelUp():
            self.groupInviteePanel.cleanup()
            self.groupInviteePanel = None
        return

    def postInviteNotQualify(self, avId, reason):
        messenger.send('updateGroupStatus')
        rejectText = ''
        minLaff = TTLocalizer.BoardingMore
        if avId == localAvatar.doId:
            if reason == BoardingPartyBase.BOARDCODE_MINLAFF:
                rejectText = TTLocalizer.BoardingInviteMinLaffInviter % minLaff
            elif reason == BoardingPartyBase.BOARDCODE_PROMOTION:
                rejectText = TTLocalizer.BoardingInvitePromotionInviter
        else:
            avatar = base.cr.doId2do.get(avId)
            if avatar:
                avatarNameText = avatar.name
            else:
                avatarNameText = ''
            if reason == BoardingPartyBase.BOARDCODE_MINLAFF:
                rejectText = TTLocalizer.BoardingInviteMinLaffInvitee % (avatarNameText, minLaff)
            elif reason == BoardingPartyBase.BOARDCODE_PROMOTION:
                rejectText = TTLocalizer.BoardingInvitePromotionInvitee % avatarNameText
            elif reason == BoardingPartyBase.BOARDCODE_BATTLE:
                rejectText = TTLocalizer.TeleportPanelNotAvailable % avatarNameText
            elif reason == BoardingPartyBase.BOARDCODE_NOT_PAID:
                rejectText = TTLocalizer.BoardingInviteNotPaidInvitee % avatarNameText
            elif reason == BoardingPartyBase.BOARDCODE_DIFF_GROUP:
                rejectText = TTLocalizer.BoardingInviteeInDiffGroup % avatarNameText
            elif reason == BoardingPartyBase.BOARDCODE_PENDING_INVITE:
                rejectText = TTLocalizer.BoardingInviteePendingIvite % avatarNameText
            elif reason == BoardingPartyBase.BOARDCODE_IN_ELEVATOR:
                rejectText = TTLocalizer.BoardingInviteeInElevator % avatarNameText
        if self.inviterPanels.isInvitingPanelIdCorrect(avId) or avId == localAvatar.doId:
            self.inviterPanels.destroyInvitingPanel()
        self.showMe(rejectText)

    def postAlreadyInGroup(self):
        self.showMe(TTLocalizer.BoardingAlreadyInGroup)

    def postGroupAlreadyFull(self):
        self.showMe(TTLocalizer.BoardingGroupAlreadyFull)

    def postSomethingMissing(self):
        self.showMe(TTLocalizer.BoardcodeMissing)

    def postRejectBoard(self, reason, avatarsFailingRequirements, avatarsInBattle):
        self.showRejectMessage(reason, avatarsFailingRequirements, avatarsInBattle)
        self.enableGoButton()

    def postRejectGoto(self, reason, avatarsFailingRequirements, avatarsInBattle):
        self.showRejectMessage(reason, avatarsFailingRequirements, avatarsInBattle)

    def postMessageInvited(self, inviteeId, inviterId):
        inviterName = ''
        inviteeName = ''
        inviter = base.cr.doId2do.get(inviterId)
        if inviter:
            inviterName = inviter.name
        invitee = base.cr.doId2do.get(inviteeId)
        if invitee:
            inviteeName = invitee.name
        messageText = TTLocalizer.BoardingMessageInvited % (inviterName, inviteeName)
        localAvatar.setSystemMessage(0, messageText, WhisperPopup.WTToontownBoardingGroup)

    def postMessageInvitationFailed(self, inviterId):
        inviterName = ''
        inviter = base.cr.doId2do.get(inviterId)
        if inviter:
            inviterName = inviter.name
        if self.invitationFailedMessageOk(inviterId):
            messageText = TTLocalizer.BoardingMessageInvitationFailed % inviterName
            localAvatar.setSystemMessage(0, messageText, WhisperPopup.WTToontownBoardingGroup)

    def postMessageAcceptanceFailed(self, inviteeId, reason):
        inviteeName = ''
        messageText = ''
        invitee = base.cr.doId2do.get(inviteeId)
        if invitee:
            inviteeName = invitee.name
        if reason == BoardingPartyBase.INVITE_ACCEPT_FAIL_GROUP_FULL:
            messageText = TTLocalizer.BoardingMessageGroupFull % inviteeName
        localAvatar.setSystemMessage(0, messageText, WhisperPopup.WTToontownBoardingGroup)
        if self.inviterPanels.isInvitingPanelIdCorrect(inviteeId):
            self.inviterPanels.destroyInvitingPanel()

    def invitationFailedMessageOk(self, inviterId):
        now = globalClock.getFrameTime()
        lastTime = self.lastInvitationFailedMessage.get(inviterId, None)
        if lastTime:
            elapsedTime = now - lastTime
            if elapsedTime < self.InvitationFailedTimeout:
                return False
        self.lastInvitationFailedMessage[inviterId] = now
        return True

    def showRejectMessage(self, reason, avatarsFailingRequirements, avatarsInBattle):
        leaderId = localAvatar.doId
        rejectText = ''

        def getAvatarText(avIdList):
            avatarText = ''
            nameList = []
            for avId in avIdList:
                avatar = base.cr.doId2do.get(avId)
                if avatar:
                    nameList.append(avatar.name)

            if len(nameList) > 0:
                lastName = nameList.pop()
                avatarText = lastName
                if len(nameList) > 0:
                    secondLastName = nameList.pop()
                    for name in nameList:
                        avatarText = name + ', '

                    avatarText += secondLastName + ' ' + TTLocalizer.And + ' ' + lastName
            return avatarText

        if reason == BoardingPartyBase.BOARDCODE_MINLAFF:
            self.notify.debug("%s 's group cannot board because it does not have enough laff points." % leaderId)
            minLaffPoints = TTLocalizer.BoardingMore
            if leaderId in avatarsFailingRequirements:
                rejectText = TTLocalizer.BoardcodeMinLaffLeader % minLaffPoints
            else:
                avatarNameText = getAvatarText(avatarsFailingRequirements)
                if len(avatarsFailingRequirements) == 1:
                    rejectText = TTLocalizer.BoardcodeMinLaffNonLeaderSingular % (avatarNameText, minLaffPoints)
                else:
                    rejectText = TTLocalizer.BoardcodeMinLaffNonLeaderPlural % (avatarNameText, minLaffPoints)
        elif reason == BoardingPartyBase.BOARDCODE_PROMOTION:
            self.notify.debug("%s 's group cannot board because it does not have enough promotion merits." % leaderId)
            if leaderId in avatarsFailingRequirements:
                rejectText = TTLocalizer.BoardcodePromotionLeader
            else:
                avatarNameText = getAvatarText(avatarsFailingRequirements)
                if len(avatarsFailingRequirements) == 1:
                    rejectText = TTLocalizer.BoardcodePromotionNonLeaderSingular % avatarNameText
                else:
                    rejectText = TTLocalizer.BoardcodePromotionNonLeaderPlural % avatarNameText
        elif reason == BoardingPartyBase.BOARDCODE_BATTLE:
            self.notify.debug("%s 's group cannot board because it is in a battle" % leaderId)
            if leaderId in avatarsInBattle:
                rejectText = TTLocalizer.BoardcodeBattleLeader
            else:
                avatarNameText = getAvatarText(avatarsInBattle)
                if len(avatarsInBattle) == 1:
                    rejectText = TTLocalizer.BoardcodeBattleNonLeaderSingular % avatarNameText
                else:
                    rejectText = TTLocalizer.BoardcodeBattleNonLeaderPlural % avatarNameText
        elif reason == BoardingPartyBase.BOARDCODE_SPACE:
            self.notify.debug("%s 's group cannot board there was not enough room" % leaderId)
            rejectText = TTLocalizer.BoardcodeSpace
        elif reason == BoardingPartyBase.BOARDCODE_MISSING:
            self.notify.debug("%s 's group cannot board because something was missing" % leaderId)
            rejectText = TTLocalizer.BoardcodeMissing
        base.localAvatar.elevatorNotifier.showMe(rejectText)

    def postGroupDissolve(self, quitterId, leaderId, memberList, kick):
        self.notify.debug('%s group has dissolved' % leaderId)
        isMyGroup = 0
        if localAvatar.doId == quitterId or localAvatar.doId == leaderId:
            isMyGroup = 1
        if leaderId in self.groupListDict:
            if leaderId == localAvatar.doId:
                isMyGroup = 1
                if leaderId in self.avIdDict:
                    self.avIdDict.pop(leaderId)
            self.groupListDict.pop(leaderId)
            for memberId in memberList:
                if memberId == localAvatar.doId:
                    isMyGroup = 1
                if memberId in self.avIdDict:
                    self.avIdDict.pop(memberId)

        if isMyGroup:
            self.notify.debug('new info posted on my group')
            messenger.send('updateGroupStatus')
            groupFormed = False
            if self.groupPanel:
                groupFormed = True
                self.groupPanel.cleanup()
            self.groupPanel = None
            if groupFormed:
                if leaderId == quitterId:
                    if not localAvatar.doId == leaderId:
                        localAvatar.setSystemMessage(0, TTLocalizer.BoardingMessageGroupDissolved, WhisperPopup.WTToontownBoardingGroup)
                elif not kick:
                    if not localAvatar.doId == quitterId:
                        quitter = base.cr.doId2do.get(quitterId)
                        if quitter:
                            quitterName = quitter.name
                            messageText = TTLocalizer.BoardingMessageLeftGroup % quitterName
                            localAvatar.setSystemMessage(0, messageText, WhisperPopup.WTToontownBoardingGroup)
                        else:
                            messageText = TTLocalizer.BoardingMessageGroupDisbandedGeneric
                            localAvatar.setSystemMessage(0, messageText, WhisperPopup.WTToontownBoardingGroup)
        return

    def requestInvite(self, inviteeId):
        self.notify.debug('requestInvite %s' % inviteeId)
        if inviteeId in self.getGroupKickList(localAvatar.doId):
            if not self.isGroupLeader(localAvatar.doId):
                avatar = base.cr.doId2do.get(inviteeId)
                if avatar:
                    avatarNameText = avatar.name
                else:
                    avatarNameText = ''
                rejectText = TTLocalizer.BoardingInviteeInKickOutList % avatarNameText
                self.showMe(rejectText)
                return
        if self.inviterPanels.isInvitingPanelUp():
            self.showMe(TTLocalizer.BoardingPendingInvite)
        elif len(self.getGroupMemberList(localAvatar.doId)) >= self.maxSize:
            self.showMe(TTLocalizer.BoardingInviteGroupFull)
        else:
            invitee = base.cr.doId2do.get(inviteeId)
            if invitee:
                self.inviterPanels.createInvitingPanel(self, inviteeId)
                self.sendUpdate('requestInvite', [inviteeId])

    def requestCancelInvite(self, inviteeId):
        self.sendUpdate('requestCancelInvite', [inviteeId])

    def requestAcceptInvite(self, leaderId, inviterId):
        self.notify.debug('requestAcceptInvite %s %s' % (leaderId, inviterId))
        self.sendUpdate('requestAcceptInvite', [leaderId, inviterId])

    def requestRejectInvite(self, leaderId, inviterId):
        self.sendUpdate('requestRejectInvite', [leaderId, inviterId])

    def requestKick(self, kickId):
        self.sendUpdate('requestKick', [kickId])

    def requestLeave(self):
        if self.goToShowTrack and self.goToShowTrack.isPlaying():
            return
        place = base.cr.playGame.getPlace()
        if place:
            if not place.getState() == 'elevator':
                if localAvatar.doId in self.avIdDict:
                    leaderId = self.avIdDict[localAvatar.doId]
                    self.sendUpdate('requestLeave', [leaderId])

    def informDestChange(self, offset):
        self.sendUpdate('informDestinationInfo', [offset])

    def postDestinationInfo(self, offset):
        self.currentDestinationData = BoardingPartyBase.DestinationData[offset]
        if self.groupPanel:
            self.groupPanel.changeDestination(offset)

    def enableGoButton(self):
        if self.groupPanel:
            self.groupPanel.enableGoButton()
            self.groupPanel.enableDestinationScrolledList()

    def disableGoButton(self):
        if self.groupPanel:
            self.groupPanel.disableGoButton()
            self.groupPanel.disableDestinationScrolledList()

    def isInviteePanelUp(self):
        if self.groupInviteePanel:
            if not self.groupInviteePanel.isEmpty():
                return True
            self.groupInviteePanel = None
        return False

    def requestGoToFirstTime(self):
        self.waitingForFirstResponse = True
        self.firstRequestAccepted = False
        self.sendUpdate('requestGoToFirstTime', [])
        self.startGoToPreShow()

    def acceptGoToFirstTime(self):
        self.waitingForFirstResponse = False
        self.firstRequestAccepted = True

    def requestGoToSecondTime(self):
        if not self.waitingForFirstResponse:
            if self.firstRequestAccepted:
                self.firstRequestAccepted = False
                self.disableGoButton()
                self.sendUpdate('requestGoToSecondTime', [])
        else:
            self.postRejectGoto(BoardingPartyBase.BOARDCODE_MISSING, [], [])
            self.cancelGoToElevatorDest()

    def acceptGoToSecondTime(self):
        self.startGoToShow()

    def rejectGoToRequest(self, reason, avatarsFailingRequirements, avatarsInBattle):
        self.firstRequestAccepted = False
        self.waitingForFirstResponse = False
        self.cancelGoToElevatorDest()
        self.postRejectGoto(reason, avatarsFailingRequirements, avatarsInBattle)

    def startGoToPreShow(self):
        self.notify.debug('Starting Go Pre Show.')
        place = base.cr.playGame.getPlace()
        if place:
            place.setState('stopped')
        goButtonPreShow = BoardingGroupShow.BoardingGroupShow(localAvatar)
        goButtonPreShowTrack = goButtonPreShow.getGoButtonPreShow()
        if self.groupPanel:
            self.groupPanel.changeGoToCancel()
            self.groupPanel.disableQuitButton()
            self.groupPanel.disableDestinationScrolledList()
        self.finishGoToPreShowTrack()
        self.goToPreShowTrack = Sequence()
        self.goToPreShowTrack.append(goButtonPreShowTrack)
        self.goToPreShowTrack.append(Func(self.requestGoToSecondTime))
        self.goToPreShowTrack.start()

    def finishGoToPreShowTrack(self):
        if self.goToPreShowTrack:
            self.goToPreShowTrack.finish()
            self.goToPreShowTrack = None
        return

    def startGoToShow(self):
        self.notify.debug('Starting Go Show.')
        localAvatar.boardingParty.forceCleanupInviterPanels()
        destName = self.__getDestName()
        if self.groupPanel:
            self.groupPanel.disableQuitButton()
        goButtonShow = BoardingGroupShow.BoardingGroupShow(localAvatar)
        place = base.cr.playGame.getPlace()
        if place:
            place.setState('stopped')
        self.goToShowTrack = goButtonShow.getGoButtonShow(destName)
        self.goToShowTrack.start()

    def finishGoToShowTrack(self):
        if self.goToShowTrack:
            self.goToShowTrack.finish()
            self.goToShowTrack = None
        return

    def cancelGoToElevatorDest(self):
        self.notify.debug('%s cancelled the GoTo Button.' % localAvatar.doId)
        self.firstRequestAccepted = False
        self.waitingForFirstResponse = False
        self.finishGoToPreShowTrack()
        place = base.cr.playGame.getPlace()
        if place:
            place.setState('walk')
        if self.groupPanel:
            self.groupPanel.changeCancelToGo()
            self.groupPanel.enableGoButton()
            self.groupPanel.enableQuitButton()
            self.groupPanel.enableDestinationScrolledList()

    def __getDestName(self):
        return self.currentDestinationData.name

    def showMe(self, message):
        base.localAvatar.elevatorNotifier.showMeWithoutStopping(message)

    def forceCleanupInviteePanel(self):
        if self.isInviteePanelUp():
            self.groupInviteePanel.forceCleanup()
            self.groupInviteePanel = None
        return

    def forceCleanupInviterPanels(self):
        if self.inviterPanels:
            self.inviterPanels.forceCleanup()

    def setDestinationZoneForce(self, zoneId):
        place = self.cr.playGame.getPlace()
        if place:
            hoodId = self.cr.playGame.hood.hoodId
            loader = self.currentDestinationData.loaderName
            where = self.currentDestinationData.where
            how = self.currentDestinationData.how
            # These last 2 are only used for facilities w/ multiple types
            # Ex: Mints, DA, CGCs
            interiorIdName = self.currentDestinationData.interiorIdName
            interiorId = self.currentDestinationData.interiorId
            doneStatus = {'loader': loader,
                          'where': where,
                          'how': how,
                          interiorIdName: interiorId,
                          'zoneId': zoneId,
                          'hoodId': hoodId}
            place.requestLeave(doneStatus)
        else:
            self.notify.warning("setDestinationZoneForce: Couldn't find playGame.getPlace(), zoneId: %s" % zoneId)
