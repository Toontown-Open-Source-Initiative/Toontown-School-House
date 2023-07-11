from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

from toontown.estate import MailboxGlobals
from toontown.toonbase import ToontownGlobals
from toontown.catalog import CatalogItem
from toontown.parties.PartyGlobals import InviteStatus


class DistributedMailboxAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedMailboxAI')

    def __init__(self, air, house):
        DistributedObjectAI.__init__(self, air)
        self.house = house
        self.houseId = self.house.doId
        self.housePos = self.house.housePos
        self.name = self.house.name
        self.busy = False
        self.user = None
        self.fullIndicator = 0

    def generate(self):
        DistributedObjectAI.generate(self)
        self.updateIndicatorFlag()

    def getHouseId(self):
        return self.houseId

    def getHousePos(self):
        return self.housePos

    def getName(self):
        return self.name

    def setFullIndicator(self, fullIndicator):
        self.fullIndicator = fullIndicator

    def d_setFullIndicator(self, fullIndicator):
        self.sendUpdate('setFullIndicator', [fullIndicator])

    def b_setFullIndicator(self, fullIndicator):
        self.setFullIndicator(fullIndicator)
        self.d_setFullIndicator(fullIndicator)

    def getFullIndicator(self):
        return self.fullIndicator

    def avatarEnter(self):
        if self.busy:
            return

        avId = self.air.getAvatarIdFromSender()
        if avId != self.house.avatarId:
            self.d_setMovie(MailboxGlobals.MAILBOX_MOVIE_NOT_OWNER, avId)
            self.resetMovie()
            return

        av = self.air.doId2do.get(avId)
        if not av:
            return

        if len(av.mailboxContents):
            self.d_setMovie(MailboxGlobals.MAILBOX_MOVIE_READY, avId)
            self.user = avId
            self.busy = True

            # The avatar has seen his items now.
            if av.mailboxNotify == ToontownGlobals.NewItems:
                av.b_setCatalogNotify(av.catalogNotify, ToontownGlobals.OldItems)
        elif len(av.awardMailboxContents):
            self.d_setMovie(MailboxGlobals.MAILBOX_MOVIE_READY, avId)
            self.user = avId
            self.busy = True

            # The avatar has seen his items now.
            if av.awardNotify == ToontownGlobals.NewItems:
                av.b_setAwardNotify(ToontownGlobals.OldItems)
        elif ((av.numMailItems > 0) or (av.getNumInvitesToShowInMailbox() > 0)):
            self.d_setMovie(MailboxGlobals.MAILBOX_MOVIE_READY, avId)
            self.user = avId
            self.busy = True
        elif len(av.onOrder):
            self.d_setMovie(MailboxGlobals.MAILBOX_MOVIE_WAITING, avId)
        else:
            self.d_setMovie(MailboxGlobals.MAILBOX_MOVIE_EMPTY, avId)

        self.resetMovie()

    def avatarExit(self):
        avId = self.air.getAvatarIdFromSender()
        if avId != self.user:
            return

        self.user = None
        self.busy = False
        self.updateIndicatorFlag()
        self.d_setMovie(MailboxGlobals.MAILBOX_MOVIE_EXIT, avId)
        self.d_freeAvatar(avId)
        self.resetMovie()

    def d_freeAvatar(self, avId):
        self.sendUpdateToAvatarId(avId, 'freeAvatar', [])

    def d_setMovie(self, movie, avId):
        self.sendUpdate('setMovie', [movie, avId])

    def acceptItemMessage(self, context, item, index, optional):
        avId = self.air.getAvatarIdFromSender()
        if avId != self.user:
            return

        av = self.air.doId2do.get(avId)
        if not av:
            return

        item = CatalogItem.getItem(item, store=CatalogItem.Customization)
        isAward = item.isAward()

        adjustedMailboxContentsIndex = index - len(av.awardMailboxContents)

        if index >= (len(av.mailboxContents) + len(av.awardMailboxContents)):
            self.sendUpdateToAvatarId(avId, 'acceptItemResponse', [context, ToontownGlobals.P_InvalidIndex])
            return

        if not self.isItemIndexInvalid(av, item, index):
            self.sendUpdateToAvatarId(avId, 'acceptItemResponse', [context, ToontownGlobals.P_InvalidIndex])
            return

        if isAward:
            del av.awardMailboxContents[index]
            av.b_setAwardMailboxContents(av.awardMailboxContents)
        else:
            del av.mailboxContents[adjustedMailboxContentsIndex]
            av.b_setMailboxContents(av.mailboxContents)

        self.sendUpdateToAvatarId(avId, 'acceptItemResponse', [context, item.recordPurchase(av, optional)])

    def discardItemMessage(self, context, item, index, optional):
        avId = self.air.getAvatarIdFromSender()
        if avId != self.user:
            return

        av = self.air.doId2do.get(avId)
        if not av:
            return

        item = CatalogItem.getItem(item, store=CatalogItem.Customization)
        isAward = item.isAward()

        adjustedMailboxContentsIndex = index - len(av.awardMailboxContents)

        if index >= (len(av.mailboxContents) + len(av.awardMailboxContents)):
            self.sendUpdateToAvatarId(avId, 'discardItemResponse', [context, ToontownGlobals.P_InvalidIndex])
            return

        if isAward:
            del av.awardMailboxContents[index]
            av.b_setAwardMailboxContents(av.awardMailboxContents)
        else:
            del av.mailboxContents[adjustedMailboxContentsIndex]
            av.b_setMailboxContents(av.mailboxContents)

        self.sendUpdateToAvatarId(avId, 'discardItemResponse', [context, ToontownGlobals.P_ItemAvailable])

    def acceptInviteMessage(self, context, inviteKey):
        DistributedMailboxAI.notify.debug("acceptInviteMessage")
        # Sent from the client code to request a particular item from
        # the mailbox.
        avId = self.air.getAvatarIdFromSender()
        validInviteKey = False
        toon = simbase.air.doId2do.get(avId)
        retcode = None
        if toon:
            for invite in toon.invites:
                if invite.inviteKey == inviteKey:
                    validInviteKey = True
                    break
        if self.user != avId:
            # The client should filter this already.
            self.air.writeServerEvent('suspicious', avId, 'DistributedMailboxAI.acceptInvite busy with %s' % (self.user))
            self.notify.warning("Got unexpected accept invite request from %s while busy with %s." % (avId, self.user))
            retcode = ToontownGlobals.P_NotAtMailbox

        elif not validInviteKey:
            self.air.writeServerEvent('suspicious', avId, 'DistributedMailboxAI.acceptInvite invalid inviteKey %s' % (inviteKey))
            retcode = ToontownGlobals.P_InvalidIndex
        else:
            # hand it off to party manager
            # it's possible the party was cancelled right before he accepted
            self.air.partyManager.respondToInviteFromMailbox(context, inviteKey, InviteStatus.Accepted, self.doId)

        if not (retcode == None):
            self.sendUpdateToAvatarId(avId, "acceptItemResponse", [context, retcode])

    def respondToAcceptInviteCallback(self, context, inviteKey, retcode):
        """Tell the client the result of accepting/rejecting the invite."""
        DistributedMailboxAI.notify.debug("respondToAcceptInviteCallback")
        if self.user:
            self.sendUpdateToAvatarId(self.user, "acceptItemResponse", [context, retcode])
        pass

    def markInviteReadButNotReplied(self, inviteKey):
        """Mark the invite as read but not replied in the db."""
        avId = self.air.getAvatarIdFromSender()
        validInviteKey = False
        toon = simbase.air.doId2do.get(avId)
        for invite in toon.invites:
            if invite.inviteKey == inviteKey and \
               invite.status == InviteStatus.NotRead:
                validInviteKey = True
                break
        if validInviteKey:
            self.air.partyManager.markInviteReadButNotReplied(inviteKey)

    def rejectInviteMessage(self, context, inviteKey):
        DistributedMailboxAI.notify.debug("rejectInviteMessage")
        # Sent from the client code to request a particular item from
        # the mailbox.
        avId = self.air.getAvatarIdFromSender()
        validInviteKey = False
        toon = simbase.air.doId2do.get(avId)
        retcode = None
        if toon:
            for invite in toon.invites:
                if invite.inviteKey == inviteKey:
                    validInviteKey = True
                    break
        if self.user != avId:
            # The client should filter this already.
            self.air.writeServerEvent('suspicious', avId, 'DistributedMailboxAI.rejectInvite busy with %s' % (self.user))
            DistributedMailboxAI.notify.warning("Got unexpected reject invite request from %s while busy with %s." % (avId, self.user))
            retcode = ToontownGlobals.P_NotAtMailbox

        elif not validInviteKey:
            self.air.writeServerEvent('suspicious', avId, 'DistributedMailboxAI.rejectInvite invalid inviteKey %s' % (inviteKey))
            retcode = ToontownGlobals.P_InvalidIndex
        else:
            # hand it off to party manager
            # it's possible the party was cancelled right before he rejected
            self.air.partyManager.respondToInviteFromMailbox(context, inviteKey, InviteStatus.Rejected, self.doId)

        if not (retcode == None):
            self.sendUpdateToAvatarId(avId, "discardItemResponse", [context, retcode])

    def respondToRejectInviteCallback(self, context, inviteKey, retcode):
        DistributedMailboxAI.notify.debug("respondToRejectInviteCallback")
        """Tell the client the result of accepting/rejecting the invite."""
        if self.user:
            self.sendUpdateToAvatarId(self.user, "discardItemResponse", [context, retcode])
        pass

    def updateIndicatorFlag(self):
        av = self.air.doId2do.get(self.house.avatarId)
        if av:
            self.b_setFullIndicator(len(av.mailboxContents) != 0 or av.numMailItems or av.getNumInvitesToShowInMailbox() or len(av.awardMailboxContents) != 0)
        else:
            self.b_setFullIndicator(0)

    def resetMovie(self):
        taskMgr.doMethodLater(2, self.d_setMovie, 'resetMovie-%d' % self.doId,
                              extraArgs=[MailboxGlobals.MAILBOX_MOVIE_CLEAR, 0])

    def isItemIndexInvalid(self, av, item, itemIndex):
        """Return True if itemIndex is valid and matches mailboxContents or awardMailboxContents."""
        result = True
        adjustedMailboxContentsIndex = itemIndex - len(av.awardMailboxContents)

        if itemIndex < 0 or itemIndex >= (len(av.mailboxContents) + len(av.awardMailboxContents)):
            result = False

        if result:
            if not item.isAward():
                if adjustedMailboxContentsIndex < 0:
                    result = False
                elif adjustedMailboxContentsIndex >= len(av.mailboxContents):
                    result = False
                else:
                    if av.mailboxContents[adjustedMailboxContentsIndex] != item:
                        result = False
            else:
                if av.awardMailboxContents[itemIndex] != item:
                    result = False

        return result
