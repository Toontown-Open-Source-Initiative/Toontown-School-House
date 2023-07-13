from direct.directnotify.DirectNotifyGlobal import directNotify

from panda3d.core import *

from otp.ai.AIBaseGlobal import *

from toontown.parties import PartyGlobals
from toontown.parties.PartyGlobals import PartyStatus, InviteTheme, AddPartyErrorCode
from toontown.uberdog.TTPartyDBConsts import *

import os
import json
import datetime
import time
from operator import itemgetter


class TTPartyDB:
    notify = directNotify.newCategory('TTPartyDB')

    def __init__(self, air):
        self.air = air

        self.filePath = ConfigVariableString('parties-data-folder', 'backups/parties/').getValue()
        self.partiesFileName = ConfigVariableString('parties-file', 'parties').getValue()

    @staticmethod
    def _getNowString():
        nowStr = str(datetime.datetime.fromtimestamp(time.time()))
        # leave off the fractional seconds
        if '.' in nowStr:
            nowStr = nowStr[:nowStr.index('.')]
        return nowStr

    def getParty(self, partyId):
        """
        Attempts to get a party for the given party id.

        If a record are found, a tuple is returned containing party

        If none are found, a empty tuple is returned
        """
        assert self.notify.debugCall()

        partyData = self.loadPartiesFile(self.getFileName(self.partiesFileName))
        parties = []

        for party in partyData[PartiesFieldName]:
            if (party[PartyIdFieldName] == partyId):
                parties.append(party)

        return tuple(parties)

    def putParty(self, hostId, startTime, endTime, isPrivate, inviteTheme, activities, decorations, status):
        """
        Attempts to save an invite into the invites database

        Returns a tuple containing: SUCCESSFUL (boolean) and ERRORCODE (If errored)
        """
        assert self.notify.debugCall()
        self.notify.debug("putParty( hostId=%s, startTime=%s, endTime=%s, isPrivate=%s, inviteTheme=%s, ... status=%s )" % (hostId, startTime, endTime, isPrivate, InviteTheme.getString(inviteTheme), PartyStatus.getString(status)))

        partyFile = self.getFileName(self.partiesFileName)
        partyData = self.loadPartiesFile(partyFile)
        partyCount = 0

        for party in partyData[PartiesFieldName]:
            if(party[HostIdFieldName] == hostId and party[StatusIdFieldName] == PartyStatus.Pending):
                partyCount = partyCount + 1

        if partyCount >= PartyGlobals.MaxHostedPartiesPerToon:
            self.notify.debug("%d can't host another party, over the limit. Number of parties: %d" % (hostId, partyCount))
            return (False, AddPartyErrorCode.TooManyHostedParties)

        try:
            partyId = partyData[NextPartyIdFieldName]

            party = {
                PartyIdFieldName: partyId,
                HostIdFieldName: hostId,
                StatusIdFieldName: status,
                StartTimeFieldName: startTime,
                EndTimeFieldName: endTime,
                IsPrivateFieldName: isPrivate,
                InviteThemeFieldName: inviteTheme,
                ActivitiesFieldName: activities,
                DecorationsFieldName: decorations,
                CreationTimeFieldName: self._getNowString(),
                LastUpdateFieldName: self._getNowString(),
                RefundedFieldName: False
            }

            partyData[PartiesFieldName].append(party)
            partyData[NextPartyIdFieldName] = partyId + 1

            self.saveFile(partyFile, partyData)
        except:
            return (False, AddPartyErrorCode.DatabaseError)

        # if we got this far without an exception, we're good
        return (True, AddPartyErrorCode.AllOk)

    def deleteParty(self, hostId, partyId):
        """
        Attempts to delete party in the parties database based on partyId.

        This currently goes unused in any of the TTO party code

        Returns nothing
        """
        assert self.notify.debugCall()

        partyFile = self.getFileName(self.partiesFileName)
        partyData = self.loadPartiesFile(partyFile)
        removedParty = False

        for idx, party in enumerate(partyData[PartiesFieldName]):
            if party[PartyIdFieldName] == partyId:
                partyData[PartiesFieldName].pop(idx)
                removedParty = True

        if not removedParty:
            self.notify.warning("Avatar %d tried to delete party %d which didn't exist or wasn't his/hers!" % (hostId, partyId))

        self.saveFile(partyFile, partyData)
        return

    def getPartiesAvailableToStart(self, currentTime):
        """
        Attempts to get all the parties that can currently start.

        Returns a list of tuples of partyId and hostId of all parties allowed to
        start.  A party is allowed to start if its status is Pending and server
        time is past it's start time.
        """
        assert self.notify.debugCall()

        partyData = self.loadPartiesFile(self.getFileName(self.partiesFileName))
        partiesThatCanStart = []

        for party in partyData[PartiesFieldName]:
            if(party[StartTimeFieldName] <= currentTime and party[StatusIdFieldName] == PartyStatus.Pending):
                partiesThatCanStart.append({
                    PartyIdFieldName: party[PartyIdFieldName],
                    HostIdFieldName: party[HostIdFieldName],
                })

        # Ok, these parties can start, go ahead and set their status to CanStart
        self._setPartyStatusToCanStart(partiesThatCanStart)

        return tuple(partiesThatCanStart)

    def _setPartyStatusToCanStart(self, partiesThatCanStart):
        """
        Set the status on the following parties to CanStart
        """
        assert self.notify.debugCall()

        for party in partiesThatCanStart:
            self.changePartyStatus(party[PartyIdFieldName], PartyStatus.CanStart)

    def getPartiesOfHost(self, hostId, sortedByStartTime=False):
        """
        Attempts to get all parties for the given host id

        If records are found, a tuple is returned containing all parties

        If none are found, will return an empty tuple
        """
        assert self.notify.debugCall()

        partyData = self.loadPartiesFile(self.getFileName(self.partiesFileName))
        parties = []

        for party in partyData[PartiesFieldName]:
            if (party[HostIdFieldName] == hostId):
                parties.append(party)

        if sortedByStartTime:
            parties = sorted(parties, key=itemgetter(StartTimeFieldName))

        return tuple(parties)

    def getPartiesOfHostThatCanStart(self, hostId):
        """
        Attempts to get all the parties that can currently start.

        Returns a list of tuples of partyId and hostId of all parties allowed to
        start.  A party is allowed to start if its status is Pending and server
        time is past it's start time.
        """
        assert self.notify.debugCall()

        partyData = self.loadPartiesFile(self.getFileName(self.partiesFileName))
        parties = []

        for party in partyData[PartiesFieldName]:
            if (party[HostIdFieldName] == hostId and party[StatusIdFieldName] == PartyStatus.CanStart):
                parties.append(party)

        return tuple(parties)

    def changePrivate(self, partyId, newPrivateStatus):
        """
        Attempts to update the given party with the new private status

        If records are found and updated, a tuple is returned containing the party

        If none are found, will return an empty tuple
        """
        assert self.notify.debugCall()

        partyFile = self.getFileName(self.partiesFileName)
        partyData = self.loadPartiesFile(partyFile)
        parties = []

        for party in partyData[PartiesFieldName]:
            if(party[PartyIdFieldName] == partyId):
                party[IsPrivateFieldName] = newPrivateStatus
                party[LastUpdateFieldName] = self._getNowString()
                parties.append(party)

        self.saveFile(partyFile, partyData)

        return tuple(parties)

    def changePartyStatus(self, partyId, newPartyStatus):
        """
        Attempts to update the given party with the new party status

        If records are found and updated, a tuple is returned containing the party

        If none are found, will return an empty tuple
        """
        assert self.notify.debugCall()

        partyFile = self.getFileName(self.partiesFileName)
        partyData = self.loadPartiesFile(partyFile)
        parties = []

        for party in partyData[PartiesFieldName]:
            if(party[PartyIdFieldName] == partyId):
                party[StatusIdFieldName] = newPartyStatus
                party[LastUpdateFieldName] = self._getNowString()
                parties.append(party)

        self.saveFile(partyFile, partyData)

        return tuple(parties)

    def getMultipleParties(self, partyIds, sortByStartTime=False):
        """
        Attempts to get all parties given the partyIds

        If records are found and updated, a tuple is returned containing the parties

        If none are found, will return an empty tuple
        """
        assert self.notify.debugCall()

        if not partyIds:
            self.notify.debug("No party Ids passed to getMultipleParties")
            return ()

        partyData = self.loadPartiesFile(self.getFileName(self.partiesFileName))
        parties = []

        for party in partyData[PartiesFieldName]:
            if str(party[PartyIdFieldName]) in str(partyIds):
                parties.append(party)

        if sortByStartTime:
            parties = sorted(parties, key=itemgetter(StartTimeFieldName))

        return tuple(parties)

    def getPrioritizedParties(self, partyIds, thresholdTime, limit, future, cancelled):
        """
        Attempts to get all parties given the partyIds along with filter options

        If records are found and updated, a tuple is returned containing the parties

        If none are found, will return an empty tuple
        """
        assert self.notify.debugCall()

        if not partyIds:
            self.notify.debug("No party Ids passed to getPrioritizedParties")
            return()

        partyFile = self.getFileName(self.partiesFileName)
        partyData = self.loadPartiesFile(partyFile)
        counter = 0
        parties = []

        if future and cancelled:
            for party in partyData[PartiesFieldName]:
                if str(party[PartyIdFieldName]) in str(partyIds) and \
                   party[StartTimeFieldName] >= thresholdTime and \
                   party[StatusIdFieldName] == PartyStatus.Cancelled:
                    if counter <= limit:
                        parties.append(party)
                        counter = counter + 1

            parties = sorted(parties, key=itemgetter(StartTimeFieldName))
        elif future and cancelled:
            for party in partyData[PartiesFieldName]:
                if str(party[PartyIdFieldName]) in str(partyIds) and \
                   party[StartTimeFieldName] >= thresholdTime and \
                   party[StatusIdFieldName] != PartyStatus.Cancelled:
                    if counter <= limit:
                        parties.append(party)
                        counter = counter + 1

            parties = sorted(parties, key=itemgetter(StartTimeFieldName))
        elif not future and not cancelled:
            for party in partyData[PartiesFieldName]:
                if str(party[PartyIdFieldName]) in str(partyIds) and \
                   party[StartTimeFieldName] < thresholdTime and \
                   party[StatusIdFieldName] == PartyStatus.Cancelled:
                    if counter <= limit:
                        parties.append(party)
                        counter = counter + 1

            parties = sorted(parties, key=itemgetter(StartTimeFieldName), reverse=True)
        else:
            for party in partyData[PartiesFieldName]:
                if str(party[PartyIdFieldName]) in str(partyIds) and \
                   party[StartTimeFieldName] < thresholdTime and \
                   party[StatusIdFieldName] != PartyStatus.Cancelled:
                    if counter <= limit:
                        parties.append(party)
                        counter = counter + 1

            parties = sorted(parties, key=itemgetter(StartTimeFieldName), reverse=True)

        return tuple(parties)

    def getHostPrioritizedParties(self, hostId, thresholdTime, limit, future, cancelled):
        """
        Attempts to get all parties given the hostId along with filter options

        If records are found and updated, a tuple is returned containing the parties

        If none are found, will return an empty tuple
        """
        assert self.notify.debugCall()

        if not hostId:
            self.notify.debug("empty hostId for getHostPrioritizedParties")
            return ()

        partyFile = self.getFileName(self.partiesFileName)
        partyData = self.loadPartiesFile(partyFile)
        counter = 0
        parties = []

        if future and cancelled:
            for party in partyData[PartiesFieldName]:
                if str(party[HostIdFieldName]) in str(hostId) and \
                   party[StartTimeFieldName] >= thresholdTime and \
                   party[StatusIdFieldName] == PartyStatus.Cancelled:
                    if counter <= limit:
                        parties.append(party)
                        counter = counter + 1

            parties = sorted(parties, key=itemgetter(StartTimeFieldName))
        elif future and not cancelled:
            for party in partyData[PartiesFieldName]:
                if str(party[HostIdFieldName]) in str(hostId) and \
                   party[StartTimeFieldName] >= thresholdTime and \
                   party[StatusIdFieldName] != PartyStatus.Cancelled:
                    if counter <= limit:
                        parties.append(party)
                        counter = counter + 1

            parties = sorted(parties, key=itemgetter(StartTimeFieldName))
        elif not future and cancelled:
            for party in partyData[PartiesFieldName]:
                if str(party[HostIdFieldName]) in str(hostId) and \
                   party[StartTimeFieldName] < thresholdTime and \
                   party[StatusIdFieldName] == PartyStatus.Cancelled:
                    if counter <= limit:
                        parties.append(party)
                        counter = counter + 1

            parties = sorted(parties, key=itemgetter(StartTimeFieldName), reverse=True)
        else:
            for party in partyData[PartiesFieldName]:
                if str(party[HostIdFieldName]) in str(hostId) and \
                   party[StartTimeFieldName] < thresholdTime and \
                   party[StatusIdFieldName] != PartyStatus.Cancelled:
                    if counter <= limit:
                        parties.append(party)
                        counter = counter + 1

            parties = sorted(parties, key=itemgetter(StartTimeFieldName), reverse=True)

        return tuple(parties)

    def forceFinishForStarted(self, thresholdTime):
        """
        Attempts to force the given parties in the threshold time to completed

        If records are found and updated, a list of (partyId,hostId)

        If none are found, will return an empty tuple
        """
        assert self.notify.debugCall()

        partyFile = self.getFileName(self.partiesFileName)
        partyData = self.loadPartiesFile(partyFile)
        partiesForcedToFinish = []

        for party in partyData[PartiesFieldName]:
            if party[StatusIdFieldName] == PartyStatus.Started and party[StatusIdFieldName] < thresholdTime:
                partiesForcedToFinish.append({
                    PartyIdFieldName: party[PartyIdFieldName],
                    HostIdFieldName: party[HostIdFieldName],
                })
                party[StatusIdFieldName] = PartyStatus.Finished
                party[LastUpdateFieldName] = self._getNowString()

        self.saveFile(partyFile, partyData)

        return tuple(partiesForcedToFinish)

    def forceNeverStartedForCanStart(self, thresholdTime):
        """
        Attempts to force the selected parties in the threshold time to 'Never Started' status

        If records are found and updated, a list of (partyId,hostId)

        If none are found, will return an empty tuple
        """
        assert self.notify.debugCall()

        partyFile = self.getFileName(self.partiesFileName)
        partyData = self.loadPartiesFile(partyFile)
        partiesNeverStarted = []

        for party in partyData[PartiesFieldName]:
            if party[StatusIdFieldName] == PartyStatus.CanStart and party[EndTimeFieldName] < thresholdTime:
                partiesNeverStarted.append({
                    PartyIdFieldName: party[PartyIdFieldName],
                    HostIdFieldName: party[HostIdFieldName],
                })
                party[StatusIdFieldName] = PartyStatus.NeverStarted
                party[LastUpdateFieldName] = self._getNowString()

        self.saveFile(partyFile, partyData)

        return tuple(partiesNeverStarted)

    def changeMultiplePartiesStatus(self, partyIds, newPartyStatus):
        """
        Attempts to update the given party with the new party status

        If records are found and updated, a tuple is returned containing parties

        If none are found, will return an empty tuple
        """
        assert self.notify.debugCall()

        if not partyIds:
            self.notify.debug("No party Ids passed to changeMultiplePartiesStatus")
            return()

        partyFile = self.getFileName(self.partiesFileName)
        partyData = self.loadPartiesFile(partyFile)
        parties = []

        for party in partyData[PartiesFieldName]:
            if party[PartyIdFieldName] in partyIds:
                party[StatusIdFieldName] = newPartyStatus
                party[LastUpdateFieldName] = self._getNowString()
                parties.append(party)

        self.saveFile(partyFile, partyData)

        return tuple(parties)
    
    def getPartiesThatAreNeverStarted(self):
        """
        Attempts to get all the parties that can currently start.

        Returns a list of tuples of partyId and hostId of all parties allowed to
        start.  A party is allowed to start if its status is Pending and server
        time is past it's start time.
        """
        assert self.notify.debugCall()

        partyData = self.loadPartiesFile(self.getFileName(self.partiesFileName))
        parties = []

        for party in partyData[PartiesFieldName]:
            if (party[StatusIdFieldName] == PartyStatus.NeverStarted):
                parties.append(party)

        return tuple(parties)

    def changePartyRefundedStatus(self, partyId, beansRefunded):
        """
        Attempts to update the given party with the new refund

        If records are found and updated, a tuple is returned containing the party

        If none are found, will return an empty tuple
        """
        assert self.notify.debugCall()

        partyFile = self.getFileName(self.partiesFileName)
        partyData = self.loadPartiesFile(partyFile)
        parties = []

        for party in partyData[PartiesFieldName]:
            if(party[PartyIdFieldName] == partyId):
                party[RefundedFieldName] = beansRefunded
                party[LastUpdateFieldName] = self._getNowString()
                parties.append(party)

        self.saveFile(partyFile, partyData)

        return tuple(parties)

    # Custom for JSONs
    def loadPartiesFile(self, fileName):
        data = {
            PartiesFieldName: [],
            NextPartyIdFieldName: 0
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
