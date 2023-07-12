from direct.directnotify.DirectNotifyGlobal import directNotify

from panda3d.core import *

from toontown.parties.PartyGlobals import PartyStatus, InviteTheme, AddPartyErrorCode, MaxHostedPartiesPerToon

import pymysql
import json
from pymysql import ProgrammingError, OperationalError

SERVER_GONE_ERROR = pymysql.constants.CR.CR_SERVER_GONE_ERROR
SERVER_LOST = pymysql.constants.CR.CR_SERVER_LOST


class TTPartyDB:
    notify = directNotify.newCategory("TTPartyDB")

    def __init__(self, host, port, user, password, databaseName):
        self.sqlAvailable = True
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.databaseName = databaseName

        try:
            self.database = pymysql.connect(
                host=host,
                port=port,
                user=user,
                passwd=password,
            )
        except OperationalError as e:
            self.notify.warning("Failed to connect to MySQL. Database=%s at %s:%d. Party Database is disabled (Parties will not function)." %
                                (databaseName, host, port))
            self.notify.warning("Error detail: %s" % str(e))
            self.sqlAvailable = False
            return

        self.notify.info("Connected to Database %s at %s:%d." % (databaseName, host, port))

        # temp hack for initial dev, create DB structure if it doesn't exist already

        initDb = ConfigVariableBool('want-parties-init-db', False).getValue()

        cursor = self.database.cursor()

        if initDb:
            try:
                cursor.execute(
                    """
                    CREATE DATABASE `%s`;
                    """ % self.databaseName
                )
                self.notify.info("Database '%s' did not exist, created a new one!" % self.databaseName)
            except ProgrammingError as e:
                # self.notify.info('%s' % str(e))
                pass
            except OperationalError as e:
                self.notify.info('%s' % str(e))
                pass

        cursor.execute(
            """
            USE `%s`;
            """ % self.databaseName
        )
        self.notify.debug("Using database '%s'" % self.databaseName)

        if initDb:
            try:
                cursor.execute(
                    """
                    CREATE TABLE `party_statuses` (
                        `statusId` TINYINT NOT NULL,
                        `description` VARCHAR(20) NOT NULL,
                        `lastUpdate` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP() ON UPDATE CURRENT_TIMESTAMP(),
                        PRIMARY KEY (`statusId`),
                        UNIQUE INDEX `description` (`description`)
                    )
                    COMMENT='Holds all Party Statuses (Informational)'
                    COLLATE='utf8mb3_general_ci'
                    ENGINE=InnoDB;
                    """
                )

                # this ensure that the table values come directly from PartyGlobals.PartyStatus
                for index in range(len(PartyStatus)):
                    cursor.execute(
                        """
                        INSERT INTO `party_statuses` (`statusId`, `description`) VALUES (%d, '%s');
                        """ % (index, PartyStatus.getString(index))
                    )

                cursor.execute(
                    """
                    CREATE TABLE `parties` (
                        `partyId` BIGINT(20) NOT NULL AUTO_INCREMENT,
                        `hostId` BIGINT(20) NOT NULL,
                        `startTime` TIMESTAMP NOT NULL DEFAULT '0000-00-00 00:00:00',
                        `endTime` TIMESTAMP NOT NULL DEFAULT '0000-00-00 00:00:00',
                        `isPrivate` TINYINT(1) NULL DEFAULT '0',
                        `inviteTheme` TINYINT(4) NULL,
                        `activities` LONGTEXT NULL COLLATE 'utf8mb4_bin',
                        `decorations` LONGTEXT NULL COLLATE 'utf8mb4_bin',
                        `statusId` TINYINT(4) NULL DEFAULT '0',
                        `creationTime` TIMESTAMP NOT NULL DEFAULT '0000-00-00 00:00:00',
                        `lastUpdate` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP() ON UPDATE CURRENT_TIMESTAMP(),
                        `refunded` TINYINT(1) NULL DEFAULT '0',
                        PRIMARY KEY (`partyId`),
                        INDEX `hostId` (`hostId`),
                        INDEX `statusId` (`statusId`),
                        CONSTRAINT `activities` CHECK (json_valid(`activities`)),
                        CONSTRAINT `decorations` CHECK (json_valid(`decorations`))
                    )
                    COMMENT='Used for all Parties'
                    COLLATE='utf8mb3_general_ci'
                    ENGINE=InnoDB;
                    """
                )
            except OperationalError as e:
                pass

        try:
            cursor = self.database.cursor()
            cursor.execute(
                """
                USE `%s`;
                """ % self.databaseName
            )

            self.notify.debug("Using database '%s'" % self.databaseName)
        except:
            self.notify.debug("%s database not found, Invite Database is disabled (Parties will not function)." % self.databaseName)
            self.sqlAvailable = False

    def reconnect(self):
        """
        Reconnects to the database
        """
        self.notify.debug("MySQL server was missing, attempting to reconnect.")

        try:
            self.database.close()
        except:
            pass

        self.database = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.password
        )

        cursor = self.database.cursor()
        cursor.execute(
            """
            USE `%s`;
            """ % (self.databaseName)
        )

        self.notify.debug("Reconnected to MySQL server at %s:%d." % (self.host, self.port))

    def disconnect(self):
        """
        Disconnects from the database
        """
        if not self.sqlAvailable:
            return

        self.database.close()
        self.database = None

    def getParty(self, partyId, isRetry=False):
        """
        Attempts to get a party for the given party id.

        If a record are found, a tuple is returned containing party

        If none are found, a empty tuple is returned
        """
        assert self.notify.debugCall()

        if not self.sqlAvailable:
            self.notify.warning("MySQL database is unavailable. Unable to find party for partyId %s" % partyId)
            return ()

        cursor = self.database.cursor(pymysql.cursors.DictCursor)

        try:
            cursor.execute(
                """
                SELECT * FROM `parties` WHERE `partyId`='%s';
                """ % (partyId)
            )

            res = cursor.fetchall()

            return tuple(res)
        except OperationalError as e:
            if isRetry == True:
                self.notify.warning("Error on getParty retry, giving up:\n%s" % str(e))
                return ()
            elif e[0] == SERVER_GONE_ERROR or e[0] == SERVER_LOST:
                self.reconnect()
                return self.getParty(partyId, True)
            else:
                self.notify.warning("Unknown error in getParty, retrying:\n%s" % str(e))
                self.reconnect()
                return self.getParty(partyId, True)
        except Exception as e:
            self.notify.warning("Unknown error in getParty, giving up:\n%s" % str(e))
            return ()

    def putParty(self, hostId, startTime, endTime, isPrivate, inviteTheme, activities, decorations, status, isRetry=False):
        """
        Attempts to save an invite into the invites database

        Returns a tuple containing: SUCCESSFUL (boolean) and ERRORCODE (If errored)
        """
        self.notify.debug("putParty( hostId=%s, startTime=%s, endTime=%s, isPrivate=%s, inviteTheme=%s, ... status=%s, isRetry=%s )" % (hostId, startTime, endTime, isPrivate, InviteTheme.getString(inviteTheme), PartyStatus.getString(status), isRetry))

        if not self.sqlAvailable:
            self.notify.warning("MySQL database is unavailable. Unable to store party for hostId: %s. Data: (hostId=%s, startTime=%s, endTime=%s, isPrivate=%s, inviteTheme=%s, ... status=%s, isRetry=%s)" % (hostId, hostId, startTime, endTime, isPrivate, InviteTheme.getString(inviteTheme), PartyStatus.getString(status), isRetry))
            return (False, AddPartyErrorCode.DatabaseError)

        cursor = self.database.cursor()

        try:
            cursor.execute(
                """
                SELECT * FROM `parties` WHERE `hostId`='%s' AND `statusId`='%s';
                """ % (hostId, PartyStatus.Pending)
            )

            if cursor.rowcount >= MaxHostedPartiesPerToon:
                self.notify.debug("%d can't host another party, over the limit " % (hostId))
                return (False, AddPartyErrorCode.TooManyHostedParties)
            
            cursor = self.database.cursor(pymysql.cursors.DictCursor)

            cursor.execute(
                """
                INSERT INTO `parties` (`hostId`, `startTime`, `endTime`, `isPrivate`, `inviteTheme`, `activities`, `decorations`, `statusId`, `creationTime`) VALUES (%s, '%s', '%s', %s, %s, '%s', '%s', %s, NOW());
                """ % (hostId, startTime, endTime, isPrivate, inviteTheme, json.dumps(activities), json.dumps(decorations), status)
            )

            self.database.commit()
        except OperationalError as e:
            if isRetry == True:
                self.notify.warning("Error on putParty retry, giving up:\n%s" % str(e))
                return (False, AddPartyErrorCode.DatabaseError)
            elif e[0] == SERVER_GONE_ERROR or e[0] == SERVER_LOST:
                self.reconnect()
                return self.putParty(hostId, startTime, endTime, isPrivate, inviteTheme, activities, decorations, status, True)
            else:
                self.notify.warning("Unknown error in putParty, retrying:\n%s" % str(e))
                self.reconnect()
                return self.putParty(hostId, startTime, endTime, isPrivate, inviteTheme, activities, decorations, status, True)
        except Exception as e:
            self.notify.warning("Unknown error in putParty, giving up:\n%s" % str(e))
            return (False, AddPartyErrorCode.DatabaseError)

        # if we got this far without an exception, we're good
        return (True, AddPartyErrorCode.AllOk)

    def deleteParty(self, hostId, partyId, isRetry=False):
        """
        Attempts to delete party in the parties database based on partyId.

        This currently goes unused in any of the TTO party code

        Returns nothing
        """
        assert self.notify.debugCall()

        if not self.sqlAvailable:
            self.notify.warning("MySQL database is unavailable. Unable to delete partyId: %s for host %d" % (partyId, hostId))
            return

        cursor = self.database.cursor(pymysql.cursors.DictCursor)

        try:
            cursor.execute(
                """
                DELETE FROM `parties` WHERE `partyId`=%s;
                """ % (partyId)
            )

            if cursor.rowcount < 1:
                self.notify.warning("Avatar %d tried to delete party %d which didn't exist or wasn't his/hers!" % (hostId, partyId))

            self.database.commit()
        except OperationalError as e:
            if isRetry == True:
                self.notify.warning("Error in deleteParty retry, giving up:\n%s" % str(e))
                return
            elif e[0] == SERVER_GONE_ERROR or e[0] == SERVER_LOST:
                self.reconnect()
                self.deleteParty(hostId, partyId, True)
            else:
                self.notify.warning("Unnown error in deleteParty, retrying:\n%s" % str(e))
                self.reconnect()
                self.deleteParty(hostId, partyId, True)
        except Exception as e:
            self.notify.warning("Unknown error in deleteParty, giving up:\n%s" % str(e))
            return

    def getPartiesAvailableToStart(self, currentTime, isRetry=False):
        """
        Attempts to get all the parties that can currently start.

        Returns a list of tuples of partyId and hostId of all parties allowed to
        start.  A party is allowed to start if its status is Pending and server
        time is past it's start time.
        """
        assert self.notify.debugCall()

        if not self.sqlAvailable:
            self.notify.warning("MySQL database is unavailable. Unable to get any parties available to be started at currentTime: %s" % (currentTime))
            return ()

        cursor = self.database.cursor(pymysql.cursors.DictCursor)

        try:
            cursor.execute(
                """
                SELECT `partyId`, `hostId` FROM `parties` WHERE `startTime` <= '%s' AND `statusId`='%s';
                """ % (currentTime, PartyStatus.Pending)
            )
            res = cursor.fetchall()

            # Ok, these parties can start, go ahead and set their status to CanStart
            self._setPartyStatusToCanStart(res)

            return tuple(res)
        except OperationalError as e:
            if isRetry:
                self.notify.warning("Error on getPartiesAvailableToStart retry, giving up:\n%s" % str(e))
                return ()
            elif e[0] == SERVER_GONE_ERROR or e[0] == SERVER_LOST:
                self.reconnect()
                return self.getPartiesAvailableToStart(currentTime, True)
            else:
                self.notify.warning("Unknown error in getPartiesAvailableToStart, retrying:\n%s" % str(e))
                self.reconnect()
                return self.getPartiesAvailableToStart(currentTime, True)
        except Exception as e:
            self.notify.warning("Unknown error in getPartiesAvailableToStart, giving up:\n%s" % str(e))
            return ()

    def _setPartyStatusToCanStart(self, partiesThatCanStart):
        """ Set the status on the following parties to CanStart """
        for party in partiesThatCanStart:
            self.changePartyStatus(party['partyId'], PartyStatus.CanStart)

    def getPartiesOfHost(self, hostId, sortByStartTime=False, isRetry=False):
        """
        Attempts to get all parties for the given host id

        If records are found, a tuple is returned containing all parties

        If none are found, will return an empty tuple
        """
        assert self.notify.debugCall()

        if not self.sqlAvailable:
            self.notify.warning("MySQL database is unavailable. Unable to get any parties for given host id: %s" % (hostId))
            return ()

        cursor = self.database.cursor(pymysql.cursors.DictCursor)

        try:
            if sortByStartTime:
                cursor.execute(
                    """
                    SELECT * FROM `parties` WHERE `hostId`='%s' ORDER BY `startTime`;
                    """ % (hostId)
                )
            else:
                cursor.execute(
                    """
                    SELECT * FROM `parties` WHERE `hostId`='%s';
                    """ % (hostId)
                )

            res = cursor.fetchall()

            return tuple(res)
        except OperationalError as e:
            if isRetry:
                self.notify.warning("Error on getPartiesOfHost retry, giving up:\n%s" % str(e))
                return ()
            elif e[0] == SERVER_GONE_ERROR or e[0] == SERVER_LOST:
                self.reconnect()
                return self.getPartiesOfHost(hostId, sortedByStartTime, True)
            else:
                self.notify.warning("Unknown error in getPartiesOfHost, retrying:\n%s" % str(e))
                self.reconnect()
                return self.getPartiesOfHost(hostId, sortedByStartTime, True)
        except Exception as e:
            self.notify.warning("Unknown error in getPartiesOfHost, giving up:\n%s" % str(e))
            return ()

    def getPartiesOfHostThatCanStart(self, hostId, isRetry=False):
        """
        Attempts to get all parties that can start for the given host id

        If records are found, a tuple is returned containing all parties that can start

        If none are found, will return an empty tuple
        """
        assert self.notify.debugCall()

        if not self.sqlAvailable:
            self.notify.warning("MySQL database is unavailable. Unable to get any parties that can start for given host id: %s" % (hostId))
            return ()

        cursor = self.database.cursor(pymysql.cursors.DictCursor)

        try:
            cursor.execute(
                """
                SELECT * FROM `parties` WHERE `hostId`='%s' AND `statusId`='%s';
                """ % (hostId, PartyStatus.CanStart)
            )

            res = cursor.fetchall()

            return tuple(res)
        except OperationalError as e:
            if isRetry:
                self.notify.warning("Error on getPartiesOfHostThatCanStart retry, giving up:\n%s" % str(e))
                return ()
            elif e[0] == SERVER_GONE_ERROR or e[0] == SERVER_LOST:
                self.reconnect()
                return self.getPartiesOfHostThatCanStart(hostId, True)
            else:
                self.notify.warning("Unknown error in getPartiesOfHostThatCanStart, retrying:\n%s" % str(e))
                self.reconnect()
                return self.getPartiesOfHostThatCanStart(hostId, True)
        except Exception as e:
            self.notify.warning("Unknown error in getPartiesOfHostThatCanStart, giving up:\n%s" % str(e))
            return ()

    def changePrivate(self, partyId, newPrivateStatus, isRetry=False):
        """
        Attempts to update the given party with the new private status

        If records are found and updated, a tuple is returned containing the party

        If none are found, will return an empty tuple
        """
        assert self.notify.debugCall()

        if not self.sqlAvailable:
            self.notify.warning("MySQL database is unavailable. Unable to update party %s with new private status %s" % (partyId, newPrivateStatus))
            return ()

        cursor = self.database.cursor(pymysql.cursors.DictCursor)

        try:
            cursor.execute(
                """
                UPDATE `parties` SET `isPrivate`=%s WHERE `partyId`=%s;
                """ % (newPrivateStatus, partyId)
            )

            self.database.commit()

            res = cursor.fetchall()

            return tuple(res)
        except OperationalError as e:
            if isRetry:
                self.notify.warning("Error on changePrivate retry, giving up:\n%s" % str(e))
                return ()
            elif e[0] == SERVER_GONE_ERROR or e[0] == SERVER_LOST:
                self.reconnect()
                return self.changePrivate(newPrivateStatus, partyId, True)
            else:
                self.notify.warning("Unknown error in changePrivate, retrying:\n%s" % str(e))
                self.reconnect()
                return self.changePrivate(newPrivateStatus, partyId, True)
        except Exception as e:
            self.notify.warning("Unknown error in changePrivate, giving up:\n%s" % str(e))
            return ()

    def changePartyStatus(self, partyId, newPartyStatus, isRetry=False):
        """
        Attempts to update the given party with the new party status

        If records are found and updated, a tuple is returned containing the party

        If none are found, will return an empty tuple
        """
        assert self.notify.debugCall()

        if not self.sqlAvailable:
            self.notify.warning("MySQL database is unavailable. Unable to update party %s with new party status %s" % (partyId, newPartyStatus))
            return ()

        cursor = self.database.cursor(pymysql.cursors.DictCursor)

        try:
            cursor.execute(
                """
                UPDATE `parties` SET `statusId`=%s WHERE `partyId`=%s;
                """ % (newPartyStatus, partyId)
            )

            self.database.commit()

            res = cursor.fetchall()

            return tuple(res)
        except OperationalError as e:
            if isRetry:
                self.notify.warning("Error on changePartyStatus retry, giving up:\n%s" % str(e))
                return ()
            elif e[0] == SERVER_GONE_ERROR or e[0] == SERVER_LOST:
                self.reconnect()
                return self.changePartyStatus(newPartyStatus, partyId, True)
            else:
                self.notify.warning("Unknown error in changePartyStatus, retrying:\n%s" % str(e))
                self.reconnect()
                return self.changePartyStatus(newPartyStatus, partyId, True)
        except Exception as e:
            self.notify.warning("Unknown error in changePartyStatus, giving up:\n%s" % str(e))
            return ()

    def convertListToSQLString(self, partyIds):
        """Convert a list of integers to a string sql recognizes."""
        # string version of partyIds is so close to what we need, but it adds the L
        inClause = "("
        for index in range(len(partyIds)):
            inClause += "%d" % partyIds[index]
            if index < len(partyIds) - 1:
                inClause += ","
        inClause += ")"
        return inClause

    def getMultipleParties(self, partyIds, sortByStartTime=False, isRetry=False):
        """
        Attempts to get all parties given the partyIds

        If records are found and updated, a tuple is returned containing the parties

        If none are found, will return an empty tuple
        """
        assert self.notify.debugCall()

        if not self.sqlAvailable:
            self.notify.warning("MySQL database is unavailable. Unable to find parties from party ids %s" % (partyIds))
            return ()

        if not partyIds:
            self.notify.debug("No party Ids passed to getMultipleParties")
            return ()

        cursor = self.database.cursor(pymysql.cursors.DictCursor)

        try:
            inClause = self.convertListToSQLString(partyIds)

            if sortByStartTime:
                cursor.execute(
                    """
                    SELECT * FROM `parties` WHERE (`partyId` IN %s) ORDER BY `startTime`;
                    """ % (inClause)
                )
            else:
                cursor.execute(
                    """
                    SELECT * FROM `parties` WHERE (`partyId` IN %s);
                    """ % (inClause)
                )
            res = cursor.fetchall()

            return tuple(res)
        except OperationalError as e:
            if isRetry:
                self.notify.warning("Error on getMultipleParties retry, giving up:\n%s" % str(e))
                return ()
            elif e[0] == SERVER_GONE_ERROR or e[0] == SERVER_LOST:
                self.reconnect()
                return self.getMultipleParties(partyIds, sortByStartTime, True)
            else:
                self.notify.warning("Unknown error in getMultipleParties, retrying:\n%s" % str(e))
                self.reconnect()
                return self.getMultipleParties(partyIds, sortByStartTime, True)
        except Exception as e:
            self.notify.warning("Unknown error in getMultipleParties, giving up:\n%s" % str(e))
            return ()

    def getPrioritizedParties(self, partyIds, thresholdTime, limit, future, cancelled, isRetry=False):
        """
        Attempts to get all parties given the partyIds along with filter options

        If records are found and updated, a tuple is returned containing the parties

        If none are found, will return an empty tuple
        """
        assert self.notify.debugCall()

        if not self.sqlAvailable:
            self.notify.warning("MySQL database is unavailable. Unable to find parties from party ids %s" % (partyIds))
            return ()

        if not partyIds:
            self.notify.debug("No party Ids passed to getPrioritizedParties")
            return()

        cursor = self.database.cursor(pymysql.cursors.DictCursor)

        try:
            inClause = self.convertListToSQLString(partyIds)

            if future and cancelled:
                cursor.execute(
                    """
                    SELECT * FROM `parties` WHERE (`partyId` IN %s) AND (`startTime` >= '%s') AND `statusId` = %s ORDER BY `startTime` LIMIT %s;
                    """ % (inClause, thresholdTime, PartyStatus.Cancelled, str(limit))
                )
            elif future and not cancelled:
                cursor.execute(
                    """
                    SELECT * FROM `parties` WHERE (`partyId` IN %s) AND (`startTime` >= '%s') AND `statusId` != %s ORDER BY `startTime` LIMIT %s;
                    """ % (inClause, thresholdTime, PartyStatus.Cancelled, str(limit))
                )
            elif not future and cancelled:
                cursor.execute(
                    """
                    SELECT * FROM `parties` WHERE (`partyId` IN %s) AND (`startTime` < '%s') AND `statusId` = %s ORDER BY `startTime` DESC LIMIT %s;
                    """ % (inClause, thresholdTime, PartyStatus.Cancelled, str(limit))
                )
            else:
                cursor.execute(
                    """
                    SELECT * FROM `parties` WHERE (`partyId` IN %s) AND (`startTime` < '%s') AND `statusId` != %s ORDER BY `startTime` DESC LIMIT %s;
                    """ % (inClause, thresholdTime, PartyStatus.Cancelled, str(limit))
                )
            res = cursor.fetchall()

            return tuple(res)
        except OperationalError as e:
            if isRetry:
                self.notify.warning("Error on getPrioritizedParties retry. Giving up:\n%s" % str(e))
                return ()
            elif e[0] == SERVER_GONE_ERROR or e[0] == SERVER_LOST:
                self.reconnect()
                return self.getPrioritizedParties(partyIds, thresholdTime, limit, future, cancelled, isRetry=True)
            else:
                self.notify.warning("Unknown error in getPrioritizedParties, retrying:\n%s" % str(e))
                self.reconnect()
                return self.getPrioritizedParties(partyIds, thresholdTime, limit, future, cancelled, isRetry=True)
        except Exception as e:
            self.notify.warning("Unknown error in getPrioritizedParties, giving up:\n%s" % str(e))
            return ()

    def getHostPrioritizedParties(self, hostId, thresholdTime, limit, future, cancelled, isRetry=False):
        """
        Attempts to get all parties given the hostId along with filter options

        If records are found and updated, a tuple is returned containing the parties

        If none are found, will return an empty tuple
        """
        assert self.notify.debugCall()

        if not self.sqlAvailable:
            self.notify.warning("MySQL database is unavailable. Unable to find parties from host ID %s" % (hostId))
            return ()

        if not hostId:
            self.notify.debug("empty hostId for getHostPrioritizedParties")
            return ()

        cursor = self.database.cursor(pymysql.cursors.DictCursor)

        try:
            if future and cancelled:
                cursor.execute(
                    """
                    SELECT * FROM `parties` WHERE (`hostId` = %s) AND (`startTime` >= '%s') AND `statusId` = %s ORDER BY `startTime` LIMIT %s;
                    """ % (hostId, thresholdTime, PartyStatus.Cancelled, str(limit))
                )
            elif future and not cancelled:
                cursor.execute(
                    """
                    SELECT * FROM `parties` WHERE (`hostId` = %s) AND (`startTime` >= '%s') AND `statusId` != %s ORDER BY `startTime` LIMIT %s;
                    """ % (hostId, thresholdTime, PartyStatus.Cancelled, str(limit))
                )
            elif not future and cancelled:
                cursor.execute(
                    """
                    SELECT * FROM `parties` WHERE (`hostId` = %s) AND (`startTime` < '%s') AND `statusId` = %s ORDER BY `startTime` DESC LIMIT %s;
                    """ % (hostId, thresholdTime, PartyStatus.Cancelled, str(limit))
                )
            else:
                cursor.execute(
                    """
                    SELECT * FROM `parties` WHERE (`hostId` = %s) AND (`startTime` < '%s') AND `statusId` != %s ORDER BY `startTime` DESC LIMIT %s;
                    """ % (hostId, thresholdTime, PartyStatus.Cancelled, str(limit))
                )
            res = cursor.fetchall()

            return tuple(res)
        except OperationalError as e:
            if isRetry:
                self.notify.warning("Error on getHostPrioritizedParties retry. Giving up:\n%s" % str(e))
                return ()
            elif e[0] == SERVER_GONE_ERROR or e[0] == SERVER_LOST:
                self.reconnect()
                return self.getHostPrioritizedParties(hostId, thresholdTime, limit, future, cancelled, isRetry=True)
            else:
                self.notify.warning("Unknown error in getHostPrioritizedParties, retrying:\n%s" % str(e))
                self.reconnect()
                return self.getHostPrioritizedParties(hostId, thresholdTime, limit, future, cancelled, isRetry=True)
        except Exception as e:
            self.notify.warning("Unknown error in getHostPrioritizedParties, giving up:\n%s" % str(e))
            return ()

    def forceFinishForStarted(self, thresholdTime, isRetry=False):
        """
        Attempts to force the given parties in the threshold time to completed

        If records are found and updated, a list of (partyId,hostId)

        If none are found, will return an empty tuple
        """
        assert self.notify.debugCall()

        if not self.sqlAvailable:
            self.notify.warning("MySQL database is unavailable. Unable to force complete any parties within the given threshold time %s" % (thresholdTime))
            return ()

        cursor = self.database.cursor(pymysql.cursors.DictCursor)

        try:
            cursor.execute(
                """
                SELECT `partyId`, `hostId` FROM `parties` WHERE `statusId` = '%s' AND `endTime` < '%s';
                """ % (PartyStatus.Started, thresholdTime)
            )

            res = cursor.fetchall()
            cursor.execute(
                """
                UPDATE `parties` SET `statusId` = %s WHERE `statusId` = '%s' AND `endTime` < '%s';
                """ % (PartyStatus.Finished, PartyStatus.Started, thresholdTime)
            )

            self.database.commit()

            return tuple(res)
        except OperationalError as e:
            if isRetry:
                self.notify.warning("Error on forceFinishForStarted retry, giving up:\n%s" % str(e))
                return ()
            elif e[0] == SERVER_GONE_ERROR or e[0] == SERVER_LOST:
                self.reconnect()
                return self.forceFinishForStarted(thresholdTime, True)
            else:
                self.notify.warning("Unknown error in forceFinishForStarted, retrying:\n%s" % str(e))
                self.reconnect()
                return self.forceFinishForStarted(thresholdTime, True)
        except Exception as e:
            self.notify.warning("Unknown error in forceFinishForStarted, giving up:\n%s" % str(e))
            return ()

    def forceNeverStartedForCanStart(self, thresholdTime, isRetry=False):
        """
        Attempts to force the selected parties in the threshold time to 'Never Started' status

        If records are found and updated, a list of (partyId,hostId)

        If none are found, will return an empty tuple
        """
        assert self.notify.debugCall()

        if not self.sqlAvailable:
            self.notify.warning("MySQL database is unavailable. Unable to force 'Never Started' status any parties within the given threshold time %s" % (thresholdTime))
            return ()

        cursor = self.database.cursor(pymysql.cursors.DictCursor)

        try:
            cursor.execute(
                """
                SELECT `partyId`, `hostId` FROM `parties` WHERE `statusId` = '%s' and `endTime` < '%s';
                """ % (PartyStatus.CanStart, thresholdTime)
            )

            res = cursor.fetchall()
            cursor.execute(
                """
                UPDATE `parties` SET `statusId` = %s WHERE `statusId` = '%s' and `endTime` < '%s';
                """ % (PartyStatus.NeverStarted, PartyStatus.CanStart, thresholdTime)
            )

            self.database.commit()

            return tuple(res)
        except OperationalError as e:
            if isRetry:
                self.notify.warning("Error on forceNeverStartedForCanStart retry, giving up:\n%s" % str(e))
                return ()
            elif e[0] == SERVER_GONE_ERROR or e[0] == SERVER_LOST:
                self.reconnect()
                return self.forceNeverStartedForCanStart(thresholdTime, True)
            else:
                self.notify.warning("Unknown error in forceNeverStartedForCanStart, retrying:\n%s" % str(e))
                self.reconnect()
                return self.forceNeverStartedForCanStart(thresholdTime, True)
        except Exception as e:
            self.notify.warning("Unknown error in forceNeverStartedForCanStart, giving up:\n%s" % str(e))
            return ()

    def changeMultiplePartiesStatus(self, partyIds, newPartyStatus, isRetry=False):
        """
        Attempts to update the given party with the new party status

        If records are found and updated, a tuple is returned containing parties

        If none are found, will return an empty tuple
        """
        assert self.notify.debugCall()

        if not self.sqlAvailable:
            self.notify.warning("MySQL database is unavailable. Unable to update parties %s with new party status %s" % (partyIds, newPartyStatus))
            return ()

        if not partyIds:
            self.notify.debug("No party Ids passed to changeMultiplePartiesStatus")
            return()

        cursor = self.database.cursor(pymysql.cursors.DictCursor)

        try:
            inClause = self.convertListToSQLString(partyIds)
            cursor.execute(
                """
                UPDATE `parties` SET `statusId`=%s WHERE (`partyId` IN %s);
                """ % (newPartyStatus, inClause)
            )

            self.database.commit()

            res = cursor.fetchall()

            return tuple(res)
        except OperationalError as e:
            if isRetry:
                self.notify.warning("Error on changeMultiplePartiesStatus retry, giving up:\n%s" % str(e))
                return ()
            elif e[0] == SERVER_GONE_ERROR or e[0] == SERVER_LOST:
                self.reconnect()
                return self.changeMultiplePartiesStatus(newPartyStatus, partyIds, True)
            else:
                self.notify.warning("Unknown error in changeMultiplePartiesStatus, retrying:\n%s" % str(e))
                self.reconnect()
                return self.changeMultiplePartiesStatus(newPartyStatus, partyIds, True)
        except Exception as e:
            self.notify.warning("Unknown error in changeMultiplePartiesStatus, giving up:\n%s" % str(e))
            return ()

    def getPartiesThatAreNeverStarted(self, isRetry=False):
        """
        Attempts to get all the parties that can currently start.

        Returns a list of tuples of partyId and hostId of all parties allowed to
        start.  A party is allowed to start if its status is Pending and server
        time is past it's start time.
        """
        assert self.notify.debugCall()

        if not self.sqlAvailable:
            self.notify.warning("MySQL database is unavailable. Unable to get any parties that have the 'Never Started' status")
            return ()

        cursor = self.database.cursor(pymysql.cursors.DictCursor)

        try:
            cursor.execute(
                """
                SELECT * FROM `parties` WHERE `statusId`='%s';
                """ % (PartyStatus.NeverStarted)
            )
            res = cursor.fetchall()

            return tuple(res)
        except OperationalError as e:
            if isRetry:
                self.notify.warning("Error on getPartiesThatAreNeverStarted retry, giving up:\n%s" % str(e))
                return ()
            elif e[0] == SERVER_GONE_ERROR or e[0] == SERVER_LOST:
                self.reconnect()
                return self.getPartiesThatAreNeverStarted(True)
            else:
                self.notify.warning("Unknown error in getPartiesThatAreNeverStarted, retrying:\n%s" % str(e))
                self.reconnect()
                return self.getPartiesThatAreNeverStarted(True)
        except Exception as e:
            self.notify.warning("Unknown error in getPartiesThatAreNeverStarted, giving up:\n%s" % str(e))
            return ()
        
    def changePartyRefundedStatus(self, partyId, beansRefunded, isRetry=False):
        """
        Attempts to update the given party with the new refund

        If records are found and updated, a tuple is returned containing the party

        If none are found, will return an empty tuple
        """
        assert self.notify.debugCall()

        if not self.sqlAvailable:
            self.notify.warning("MySQL database is unavailable. Unable to update party %s with new refund status %s" % (partyId, beansRefunded))
            return ()

        cursor = self.database.cursor(pymysql.cursors.DictCursor)

        try:
            cursor.execute(
                """
                UPDATE `parties` SET `refunded`=%s WHERE `partyId`=%s;
                """ % (beansRefunded, partyId)
            )

            self.database.commit()

            res = cursor.fetchall()

            return tuple(res)
        except OperationalError as e:
            if isRetry:
                self.notify.warning("Error on changePartyRefundedStatus retry, giving up:\n%s" % str(e))
                return ()
            elif e[0] == SERVER_GONE_ERROR or e[0] == SERVER_LOST:
                self.reconnect()
                return self.changePartyRefundedStatus(beansRefunded, partyId, True)
            else:
                self.notify.warning("Unknown error in changePartyRefundedStatus, retrying:\n%s" % str(e))
                self.reconnect()
                return self.changePartyRefundedStatus(beansRefunded, partyId, True)
        except Exception as e:
            self.notify.warning("Unknown error in changePartyRefundedStatus, giving up:\n%s" % str(e))
            return ()