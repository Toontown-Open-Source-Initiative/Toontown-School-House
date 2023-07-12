from direct.directnotify.DirectNotifyGlobal import directNotify

from panda3d.core import *

from toontown.uberdog.TTPartyDBConsts import *

import os
import json
import datetime
import time


class TTInviteDB:
    notify = directNotify.newCategory('TTInviteDB')

    def __init__(self, air):
        self.air = air

        self.filePath = ConfigVariableString('parties-data-folder', 'data/parties/').getValue()
        self.invitesFileName = ConfigVariableString('invites-file', 'invites').getValue()

    @staticmethod
    def _getNowString():
        nowStr = str(datetime.datetime.fromtimestamp(time.time()))
        # leave off the fractional seconds
        if '.' in nowStr:
            nowStr = nowStr[:nowStr.index('.')]
        return nowStr

    def getInvites(self, avatarId):
        """
        Attempts to get all invites for given avatar Id.

        If records are found, a tuple is returned containing all invites

        If none are found, a empty tuple is returned
        """
        assert self.notify.debugCall()

        inviteData = self.loadInvitesFile(self.getFileName(self.invitesFileName))
        invites = []

        for invite in inviteData[InvitesFieldName]:
            if (invite[GuestIdFieldName] == avatarId):
                invites.append(invite)

        return tuple(invites)

    def putInvite(self, partyId, inviteeId):
        """
        Attempts to save an invite into the invites database

        Returns nothing
        """
        assert self.notify.debugCall()

        invitesFile = self.getFileName(self.invitesFileName)
        inviteData = self.loadInvitesFile(invitesFile)

        inviteId = inviteData[NextInviteIdFieldName]

        party = {
            InviteIdFieldName: inviteId,
            PartyIdFieldName: partyId,
            GuestIdFieldName: inviteeId,
            StatusIdFieldName: 0,
            LastUpdateFieldName: self._getNowString()
        }

        inviteData[InvitesFieldName].append(party)
        inviteData[NextInviteIdFieldName] = partyId + 1

        self.saveFile(invitesFile, inviteData)

        return

    def deleteInviteByParty(self, partyId):
        """
        Attempts to delete all invites in the invites database based on partyId.

        This currently goes unused in any of the TTO party code

        Returns nothing
        """
        assert self.notify.debugCall()

        invitesFile = self.getFileName(self.invitesFileName)
        inviteData = self.loadPartiesFile(invitesFile)
        removedInvite = False

        for idx, invite in enumerate(inviteData[InvitesFieldName]):
            if invite[PartyIdFieldName] == partyId:
                inviteData[InvitesFieldName].pop(idx)
                removedInvite = True

        if not removedInvite:
            self.notify.warning("Tried to delete invites for party %d which didn't exist!" % (partyId))

        self.saveFile(invitesFile, inviteData)
        return

    def getReplies(self, partyId):
        """
        Attempts to get all replies for the invites for the given party Id

        If records are found, a tuple is returned containing all invites

        If none are found, will return an empty tuple
        """
        assert self.notify.debugCall()

        inviteData = self.loadInvitesFile(self.getFileName(self.invitesFileName))
        invites = []

        for invite in inviteData[InvitesFieldName]:
            if (invite[PartyIdFieldName] == partyId):
                invites.append(invite)

        return tuple(invites)

    def getOneInvite(self, inviteKey):
        """
        Attempts to get an invite for the given invite key

        If a record/records are found, a tuple is returned containing the invite/invites

        If none are found, will return an empty tuple
        """
        assert self.notify.debugCall()

        inviteData = self.loadInvitesFile(self.getFileName(self.invitesFileName))
        invites = []

        for invite in inviteData[InvitesFieldName]:
            if (invite[InviteIdFieldName] == inviteKey):
                invites.append(invite)

        return tuple(invites)

    def updateInvite(self, inviteKey, newStatus):
        """
        Attempts to update an invite for the given invite key  to the new status given

        If a record/records are updated/found, a tuple is returned containing the invite/invites

        If none are updated/found, will return an empty tuple
        """
        assert self.notify.debugCall()

        invitesFile = self.getFileName(self.invitesFileName)
        inviteData = self.loadInvitesFile(invitesFile)

        for invite in inviteData[InvitesFieldName]:
            if (invite[InviteIdFieldName] == inviteKey):
                invite[StatusIdFieldName] = newStatus
                invite[LastUpdateFieldName] = self._getNowString()

        self.saveFile(invitesFile, inviteData)

        return ()

    def getInviteesOfParty(self, inviteKey):
        """
        Attempts to get all invites for the given party Id

        If records are found, a tuple is returned containing all invites

        If none are found, will return an empty tuple
        """
        assert self.notify.debugCall()

        inviteData = self.loadInvitesFile(self.getFileName(self.invitesFileName))
        invites = []

        for invite in inviteData[InvitesFieldName]:
            if (invite[InviteIdFieldName] == inviteKey):
                invites.append(invite)

        return tuple(invites)

    # Custom for JSONs
    def loadInvitesFile(self, fileName):
        data = {
            InvitesFieldName: [],
            NextInviteIdFieldName: 0
        }

        try:
            with open(self.filePath + fileName, 'r') as f:
                data = json.load(f)

            fileExists = True
        except:
            fileExists = False

        if not fileExists:
            # Use self.update() to setup initial db:
            self.saveFile(fileName, data)

        return data

    def saveFile(self, fileName, jsonData):
        if not os.path.exists(self.filePath):
            os.makedirs(self.filePath)

        with open(self.filePath + fileName, 'w+') as f:
            json.dump(jsonData, f, indent=4)

    def getFileName(self, fileName):
        return '%s.json' % (fileName)
