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


class TTPartyDB:
    notify = directNotify.newCategory('TTPartyDB')

    def __init__(self, air):
        self.air = air

        self.filePath = ConfigVariableString('parties-data-folder', 'data/parties/').getValue()
        self.partiesFileName = ConfigVariableString('parties-file', 'parties').getValue()
        self.implemented = ConfigVariableBool('enable-party-db', False).getValue()

    @staticmethod
    def _getNowString():
        nowStr = str(datetime.datetime.fromtimestamp(time.time()))
        # leave off the fractional seconds
        if '.' in nowStr:
            nowStr = nowStr[:nowStr.index('.')]
        return nowStr

    def getParty(self, partyId):
        """
        Search for party with the given partyId
        """
        assert self.notify.debugCall()

        if not self.implemented:
            self.notify.debug("implemented was false when calling getParty")
            return ()

        partyData = self.loadPartiesFile(self.getFileName(self.partiesFileName))
        parties = []

        for party in partyData[PartiesFieldName]:
            if (party[PartyIdFieldName] == partyId):
                # party[StartTimeFieldName] = datetime.datetime.strptime(party[StartTimeFieldName], '%Y-%m-%d %H:%M:%S')
                # party[EndTimeFieldName] = datetime.datetime.strptime(party[EndTimeFieldName], '%Y-%m-%d %H:%M:%S')
                parties.append(party)

        # Unable to find a party.
        if len(parties) == 0:
            self.notify.warning("Unable to find a party with partyId: %s" % partyId)
        else:
            self.notify.info("Found party with id: %s" % partyId)

        return tuple(parties)

    def putParty(self, hostId, startTime, endTime, isPrivate, inviteTheme, activities, decorations, status):
        """
        Returns False if the operation failed for any reason.
        """
        assert self.notify.debugCall()
        self.notify.debug("putParty: inviteTheme=%s status=%s" % (InviteTheme.getString(inviteTheme), PartyStatus.getString(status)))

        if not self.implemented:
            self.notify.warning("implemented is False in putParty call.")
            return (False, AddPartyErrorCode.DatabaseError)

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
                LastUpdateFieldName: self._getNowString()
            }

            partyData[PartiesFieldName].append(party)
            partyData[NextPartyIdFieldName] = partyId + 1

            self.saveFile(partyFile, partyData)
        except:
            return (False, AddPartyErrorCode.DatabaseError)

        # if we got this far without an exception, we're good
        return (True, AddPartyErrorCode.AllOk)

    def deleteParty(self, partyId):
        assert self.notify.debugCall()

        if not self.implemented:
            return

        partyFile = self.getFileName(self.partiesFileName)
        partyData = self.loadPartiesFile(partyFile)
        removedParty = False

        for idx, party in enumerate(partyData[PartiesFieldName]):
            if party[PartyIdFieldName] == partyId:
                partyData[PartiesFieldName].pop(idx)
                removedParty = True

        if not removedParty:
            self.notify.warning("Tried to delete party %d which didn't exist or wasn't his!" % (partyId))

        self.saveFile(partyFile, partyData)
        return

    def getPartiesAvailableToStart(self, currentTime):
        """
        Returns a list of tuples of partyId and hostId of all parties allowed to
        start.  A party is allowed to start if its status is Pending and server
        time is past it's start time.
        """
        assert self.notify.debugCall()

        if not self.implemented:
            self.notify.warning("implemented was false when calling getPartiesAvailableToStart")
            return ()

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

    def getPartiesOfHost(self, hostId):
        """
        Returns a tuple, which could be empty.
        """
        assert self.notify.debugCall()

        if not self.implemented:
            self.notify.warning("implemented was false when calling getPartiesOfHost")
            return ()

        partyData = self.loadPartiesFile(self.getFileName(self.partiesFileName))
        parties = []

        for party in partyData[PartiesFieldName]:
            if (party[HostIdFieldName] == hostId):
                # party[StartTimeFieldName] = datetime.datetime.strptime(party[StartTimeFieldName], '%Y-%m-%d %H:%M:%S')
                # party[EndTimeFieldName] = datetime.datetime.strptime(party[EndTimeFieldName], '%Y-%m-%d %H:%M:%S')
                parties.append(party)

        return tuple(parties)

    def getPartiesOfHostThatCanStart(self, hostId):
        """
        Returns a tuple, which could be empty.
        """
        assert self.notify.debugCall()

        if not self.implemented:
            self.notify.warning("implemented was false when calling getPartiesOfHostThatCanStart")
            return ()

        partyData = self.loadPartiesFile(self.getFileName(self.partiesFileName))
        parties = []

        for party in partyData[PartiesFieldName]:
            if (party[HostIdFieldName] == hostId and party[StatusIdFieldName] == PartyStatus.CanStart):
                # party[StartTimeFieldName] = datetime.datetime.strptime(party[StartTimeFieldName], '%Y-%m-%d %H:%M:%S')
                # party[EndTimeFieldName] = datetime.datetime.strptime(party[EndTimeFieldName], '%Y-%m-%d %H:%M:%S')
                parties.append(party)

        return tuple(parties)

    def changePrivate(self, partyId, newPrivateStatus):
        assert self.notify.debugCall()

        if not self.implemented:
            self.notify.warning("implemented was false when calling changePrivate")
            return ()

        partyFile = self.getFileName(self.partiesFileName)
        partyData = self.loadPartiesFile(partyFile)

        for party in partyData[PartiesFieldName]:
            if(party[PartyIdFieldName] == partyId):
                party[IsPrivateFieldName] = newPrivateStatus
                party[LastUpdateFieldName] = self._getNowString()

        self.saveFile(partyFile, partyData)

        # Determine return response
        return ()

    def changePartyStatus(self, partyId, newPartyStatus):
        assert self.notify.debugCall()

        if not self.implemented:
            self.notify.debug("implemented was false when calling changePartyStatus")
            return ()

        partyFile = self.getFileName(self.partiesFileName)
        partyData = self.loadPartiesFile(partyFile)

        for party in partyData[PartiesFieldName]:
            if(party[PartyIdFieldName] == partyId):
                party[StatusIdFieldName] = newPartyStatus
                party[LastUpdateFieldName] = self._getNowString()

        self.saveFile(partyFile, partyData)

        # Determine return response
        return ()

    def getMultipleParties(self, partyIds):
        """
        Return all the partyInfo matching the partyIds list,
        It may return nothing if there are no matches.
        """
        assert self.notify.debugCall()

        if not self.implemented:
            self.notify.debug("implemented was false when calling getMultipleParties")
            return ()

        if not partyIds:
            self.notify.debug("empty list in partyIds for getMultipleParties")
            return()

        partyData = self.loadPartiesFile(self.getFileName(self.partiesFileName))
        parties = []

        for party in partyData[PartiesFieldName]:
            if str(party[PartyIdFieldName]) in str(partyIds):
                # party[StartTimeFieldName] = datetime.datetime.strptime(party[StartTimeFieldName], '%Y-%m-%d %H:%M:%S')
                # party[EndTimeFieldName] = datetime.datetime.strptime(party[EndTimeFieldName], '%Y-%m-%d %H:%M:%S')
                parties.append(party)

        if len(parties) >= 1:
            self.notify.debug("Select was successful in getMultipleParties, returning %s" % str(parties))
        else:
            self.notify.debug("Select was unsuccessful in getMultipleParties")

        return tuple(parties)

    def getPrioritizedParties(self, partyIds, thresholdTime, limit, future, cancelled):
        """
        Return parties from the database using the criteria specified in future and cancelled.
        """
        assert self.notify.debugCall()

        if not self.implemented:
            self.notify.debug("implemented was false when calling getCancelledFutureParties")
            return ()

        if not partyIds:
            self.notify.debug("empty list in partyIds for getCancelledFutureParties")
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
                    if counter < limit:
                        # party[StartTimeFieldName] = datetime.datetime.strptime(party[StartTimeFieldName], '%Y-%m-%d %H:%M:%S')
                        # party[EndTimeFieldName] = datetime.datetime.strptime(party[EndTimeFieldName], '%Y-%m-%d %H:%M:%S')
                        parties.append(party)
        elif future and not cancelled:
            for party in partyData[PartiesFieldName]:
                if str(party[PartyIdFieldName]) in str(partyIds) and \
                   party[StartTimeFieldName] >= thresholdTime and \
                   party[StatusIdFieldName] != PartyStatus.Cancelled:
                    if counter < limit:
                        # party[StartTimeFieldName] = datetime.datetime.strptime(party[StartTimeFieldName], '%Y-%m-%d %H:%M:%S')
                        # party[EndTimeFieldName] = datetime.datetime.strptime(party[EndTimeFieldName], '%Y-%m-%d %H:%M:%S')
                        parties.append(party)
        elif not future and not cancelled:
            for party in partyData[PartiesFieldName]:
                if str(party[PartyIdFieldName]) in str(partyIds) and \
                   party[StartTimeFieldName] < thresholdTime and \
                   party[StatusIdFieldName] == PartyStatus.Cancelled:
                    if counter < limit:
                        # party[StartTimeFieldName] = datetime.datetime.strptime(party[StartTimeFieldName], '%Y-%m-%d %H:%M:%S')
                        # party[EndTimeFieldName] = datetime.datetime.strptime(party[EndTimeFieldName], '%Y-%m-%d %H:%M:%S')
                        parties.append(party)
        else:
            for party in partyData[PartiesFieldName]:
                if str(party[PartyIdFieldName]) in str(partyIds) and \
                   party[StartTimeFieldName] < thresholdTime and \
                   party[StatusIdFieldName] != PartyStatus.Cancelled:
                    if counter < limit:
                        # party[StartTimeFieldName] = datetime.datetime.strptime(party[StartTimeFieldName], '%Y-%m-%d %H:%M:%S')
                        # party[EndTimeFieldName] = datetime.datetime.strptime(party[EndTimeFieldName], '%Y-%m-%d %H:%M:%S')
                        parties.append(party)

        return tuple(parties)

    def getHostPrioritizedParties(self, hostId, thresholdTime, limit, future, cancelled):
        """
        Return parties from the database using the criteria specified in future and cancelled.
        """
        assert self.notify.debugCall()

        if not self.implemented:
            self.notify.debug("implemented was false when calling getCancelledFutureParties")
            return ()

        if not hostId:
            self.notify.debug("empty list in hostId for getCancelledFutureParties")
            return()

        partyFile = self.getFileName(self.partiesFileName)
        partyData = self.loadPartiesFile(partyFile)
        counter = 0
        parties = []

        if future and cancelled:
            for party in partyData[PartiesFieldName]:
                if str(party[HostIdFieldName]) in str(hostId) and \
                   party[StartTimeFieldName] >= thresholdTime and \
                   party[StatusIdFieldName] == PartyStatus.Cancelled:
                    if counter < limit:
                        # party[StartTimeFieldName] = datetime.datetime.strptime(party[StartTimeFieldName], '%Y-%m-%d %H:%M:%S')
                        # party[EndTimeFieldName] = datetime.datetime.strptime(party[EndTimeFieldName], '%Y-%m-%d %H:%M:%S')
                        parties.append(party)
        elif future and not cancelled:
            for party in partyData[PartiesFieldName]:
                if str(party[HostIdFieldName]) in str(hostId) and \
                   party[StartTimeFieldName] >= thresholdTime and \
                   party[StatusIdFieldName] != PartyStatus.Cancelled:
                    if counter < limit:
                        # party[StartTimeFieldName] = datetime.datetime.strptime(party[StartTimeFieldName], '%Y-%m-%d %H:%M:%S')
                        # party[EndTimeFieldName] = datetime.datetime.strptime(party[EndTimeFieldName], '%Y-%m-%d %H:%M:%S')
                        parties.append(party)
        elif not future and not cancelled:
            for party in partyData[PartiesFieldName]:
                if str(party[HostIdFieldName]) in str(hostId) and \
                   party[StartTimeFieldName] < thresholdTime and \
                   party[StatusIdFieldName] == PartyStatus.Cancelled:
                    if counter < limit:
                        # party[StartTimeFieldName] = datetime.datetime.strptime(party[StartTimeFieldName], '%Y-%m-%d %H:%M:%S')
                        # party[EndTimeFieldName] = datetime.datetime.strptime(party[EndTimeFieldName], '%Y-%m-%d %H:%M:%S')
                        parties.append(party)
        else:
            for party in partyData[PartiesFieldName]:
                if str(party[HostIdFieldName]) in str(hostId) and \
                   party[StartTimeFieldName] < thresholdTime and \
                   party[StatusIdFieldName] != PartyStatus.Cancelled:
                    if counter < limit:
                        # party[StartTimeFieldName] = datetime.datetime.strptime(party[StartTimeFieldName], '%Y-%m-%d %H:%M:%S')
                        # party[EndTimeFieldName] = datetime.datetime.strptime(party[EndTimeFieldName], '%Y-%m-%d %H:%M:%S')
                        parties.append(party)

        return tuple(parties)

    def forceFinishForStarted(self, thresholdTime):
        """
        Returns a list of (partyId,hostId) for the ones that were forced to finished
        """
        assert self.notify.debugCall()

        if not self.implemented:
            self.notify.debug("implemented was false when calling forceFinishForStarted")
            return ()

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
        assert self.notify.debugCall()

        if not self.implemented:
            self.notify.debug("implemented was false when calling forceNeverStartedForCanStart")
            return ()

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
        assert self.notify.debugCall()

        if not self.implemented:
            self.notify.debug("implemented was false when calling changeMultiplePartiesStatus")
            return ()

        if not partyIds:
            self.notify.debug("empty list in partyIds for changeMultiplePartiesStatus")
            return ()

        partyFile = self.getFileName(self.partiesFileName)
        partyData = self.loadPartiesFile(partyFile)

        for party in partyData[PartiesFieldName]:
            if party[PartyIdFieldName] in partyIds:
                party[StatusIdFieldName] = newPartyStatus
                party[LastUpdateFieldName] = self._getNowString()

        self.saveFile(partyFile, partyData)

        return ()

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
