from direct.directnotify.DirectNotifyGlobal import directNotify

from panda3d.core import *

from toontown.parties import PartyGlobals

import pymysql
from pymysql import ProgrammingError, OperationalError

SERVER_GONE_ERROR = pymysql.constants.CR.CR_SERVER_GONE_ERROR
SERVER_LOST = pymysql.constants.CR.CR_SERVER_LOST


class TTInviteDB:
    notify = directNotify.newCategory("TTInviteDB")

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
            self.notify.warning("Failed to connect to MySQL. Database=%s at %s:%d. Invite Database is disabled (Parties will not function)." %
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
                    CREATE TABLE `invite_statuses` (
                        `statusId` TINYINT NOT NULL,
                        `description` VARCHAR(20) NOT NULL,
                        `lastUpdate` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP() ON UPDATE CURRENT_TIMESTAMP(),
                        PRIMARY KEY (`statusId`),
                        UNIQUE INDEX `description` (`description`)
                    )
                    COMMENT='Holds all Invite Statuses (Informational)'
                    COLLATE='utf8mb3_general_ci'
                    ENGINE=InnoDB;
                    """
                )

                # this ensure that the table values come directly from PartyGlobals.InviteStatus
                for index in range(len(PartyGlobals.InviteStatus)):
                    cursor.execute(
                        """
                        INSERT INTO `invite_statuses` (`statusId`, `description`) VALUES (%d, '%s');
                        """ % (index, PartyGlobals.InviteStatus.getString(index))
                    )

                cursor.execute(
                    """
                    CREATE TABLE  `invites` (
                        `inviteId` BIGINT(20) NOT NULL AUTO_INCREMENT,
                        `partyId` BIGINT(20) NOT NULL,
                        `guestId` BIGINT(20) NOT NULL,
                        `statusId` TINYINT(4) NOT NULL DEFAULT '0',
                        `lastUpdate` TIMESTAMP NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
                        PRIMARY KEY (`inviteId`),
                        INDEX `guestId` (`guestId`),
                        INDEX `partyId` (`partyId`),
                        CONSTRAINT `partyId` FOREIGN KEY (`partyId`) REFERENCES `parties` (`partyId`) ON UPDATE RESTRICT ON DELETE CASCADE
                    )
                    COMMENT='Used for all Invites'
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

    def getInvites(self, avatarId, isRetry=False):
        """
        Attempts to get all invites for given avatar Id.

        If records are found, a tuple is returned containing all invites

        If none are found, a empty tuple is returned
        """
        assert self.notify.debugCall()

        if not self.sqlAvailable:
            self.notify.warning("MySQL database is unavailable. Unable to find invites for avatar %s" % avatarId)
            return ()

        cursor = self.database.cursor(pymysql.cursors.DictCursor)

        try:
            cursor.execute(
                """
                SELECT * FROM `invites` WHERE `guestId`='%s';
                """ % (avatarId)
            )

            res = cursor.fetchall()

            return tuple(res)
        except OperationalError as e:
            if isRetry == True:
                self.notify.warning("Error on getInvites retry, giving up:\n%s" % str(e))
                return ()
            elif e[0] == SERVER_GONE_ERROR or e[0] == SERVER_LOST:
                self.reconnect()
                return self.getInvites(avatarId, True)
            else:
                self.notify.warning("Unknown error in getInvites, retrying:\n%s" % str(e))
                self.reconnect()
                return self.getInvites(avatarId, True)
        except Exception as e:
            self.notify.warning("Unknown error in getInvites, giving up:\n%s" % str(e))
            return ()

    def putInvite(self, partyId, inviteeId, isRetry=False):
        """
        Attempts to save an invite into the invites database

        Returns nothing
        """
        assert self.notify.debugCall()

        if not self.sqlAvailable:
            self.notify.warning("MySQL database is unavailable. Unable to store invite for partyId: %s, inviteeId: %s" % (partyId, inviteeId))
            return

        cursor = self.database.cursor(pymysql.cursors.DictCursor)

        try:
            cursor.execute(
                """
                INSERT INTO `invites` (`partyId`, `guestId`) VALUES (%s,%s);
                """ % (partyId, inviteeId)
            )

            self.database.commit()
        except OperationalError as e:
            if isRetry == True:
                self.notify.warning("Error on putInvite retry, giving up:\n%s" % str(e))
                return
            elif e[0] == SERVER_GONE_ERROR or e[0] == SERVER_LOST:
                self.reconnect()
                self.putInvite(partyId, inviteeId, True)
            else:
                self.notify.warning("Unknown error in putInvite, retrying:\n%s" % str(e))
                self.reconnect()
                self.putInvite(partyId, inviteeId, True)
        except Exception as e:
            self.notify.warning("Unknown error in putInvite, giving up:\n%s" % str(e))
            return

    def deleteInviteByParty(self, partyId, isRetry=False):
        """
        Attempts to delete all invites in the invites database based on partyId.

        This currently goes unused in any of the TTO party code

        Returns nothing
        """
        assert self.notify.debugCall()

        if not self.sqlAvailable:
            self.notify.warning("MySQL database is unavailable. Unable to delete any invites for partyId: %s" % (partyId))
            return

        cursor = self.database.cursor(pymysql.cursors.DictCursor)

        try:
            cursor.execute(
                """
                DELETE FROM `invites` WHERE `partyId`=%s;
                """ % (partyId)
            )

            if cursor.rowcount < 1:
                self.notify.warning("Tried to delete invites for party %d which didn't exist!" % (partyId))

            self.database.commit()
        except OperationalError as e:
            if isRetry == True:
                self.notify.warning("Error in deleteInviteByParty retry, giving up:\n%s" % str(e))
                return
            elif e[0] == SERVER_GONE_ERROR or e[0] == SERVER_LOST:
                self.reconnect()
                self.deleteInviteByParty(partyId, True)
            else:
                self.notify.warning("Unnown error in deleteInviteByParty, retrying:\n%s" % str(e))
                self.reconnect()
                self.deleteInviteByParty(partyId, True)
        except Exception as e:
            self.notify.warning("Unknown error in deleteInviteByParty, giving up:\n%s" % str(e))
            return

    def getReplies(self, partyId, isRetry=False):
        """
        Attempts to get all replies for the invites for the given party Id

        If records are found, a tuple is returned containing all invites

        If none are found, will return an empty tuple
        """
        assert self.notify.debugCall()

        if not self.sqlAvailable:
            self.notify.warning("MySQL database is unavailable. Unable to find invites for party %s" % partyId)
            return ()

        cursor = self.database.cursor(pymysql.cursors.DictCursor)

        try:
            cursor.execute(
                """
                SELECT * FROM `invites` WHERE `partyId`='%s';
                """ % (partyId)
            )

            res = cursor.fetchall()

            return tuple(res)
        except OperationalError as e:
            if isRetry == True:
                self.notify.warning("Error on getReplies retry, giving up:\n%s" % str(e))
                return ()
            elif e[0] == SERVER_GONE_ERROR or e[0] == SERVER_LOST:
                self.reconnect()
                return self.getReplies(partyId, True)
            else:
                self.notify.warning("Unknown error in getReplies, retrying:\n%s" % str(e))
                self.reconnect()
                return self.getReplies(partyId, True)
        except Exception as e:
            self.notify.warning("Unknown error in getReplies, giving up:\n%s" % str(e))
            return ()

    def getOneInvite(self, inviteKey, isRetry=False):
        """
        Attempts to get an invite for the given invite key

        If a record/records are found, a tuple is returned containing the invite/invites

        If none are found, will return an empty tuple
        """
        assert self.notify.debugCall()

        if not self.sqlAvailable:
            self.notify.warning("MySQL database is unavailable. Unable to find invite for invite key %s" % inviteKey)
            return ()

        cursor = self.database.cursor(pymysql.cursors.DictCursor)

        try:
            cursor.execute(
                """
                SELECT * FROM `invites` WHERE `inviteId`='%s';
                """ % (inviteKey)
            )

            res = cursor.fetchall()

            return tuple(res)
        except OperationalError as e:
            if isRetry == True:
                self.notify.warning("Error on getOneInvite retry, giving up:\n%s" % str(e))
                return ()
            elif e[0] == SERVER_GONE_ERROR or e[0] == SERVER_LOST:
                self.reconnect()
                return self.getOneInvite(inviteKey, True)
            else:
                self.notify.warning("Unknown error in getOneInvite, retrying:\n%s" % str(e))
                self.reconnect()
                return self.getOneInvite(inviteKey, True)
        except Exception as e:
            self.notify.warning("Unknown error in getOneInvite, giving up:\n%s" % str(e))
            return ()

    def updateInvite(self, inviteKey, newStatus, isRetry=False):
        """
        Attempts to update an invite for the given invite key  to the new status given

        If a record/records are updated/found, a tuple is returned containing the invite/invites

        If none are updated/found, will return an empty tuple
        """
        assert self.notify.debugCall()

        if not self.sqlAvailable:
            self.notify.warning("MySQL database is unavailable. Unable to update invite for invite key %s to new status %s" % (inviteKey, newStatus))
            return ()

        cursor = self.database.cursor(pymysql.cursors.DictCursor)

        try:
            cursor.execute(
                """
                UPDATE `invites` SET `statusId`=%s WHERE `inviteId`=%s;
                """ % (newStatus, inviteKey)
            )

            self.database.commit()

            res = cursor.fetchall()

            return res
        except OperationalError as e:
            if isRetry == True:
                self.notify.warning("Error on updateInvite retry, giving up:\n%s" % str(e))
                return ()
            elif e[0] == SERVER_GONE_ERROR or e[0] == SERVER_LOST:
                self.reconnect()
                return self.updateInvite(newStatus, inviteKey, True)
            else:
                self.notify.warning("Unknown error in updateInvite, retrying:\n%s" % str(e))
                self.reconnect()
                return self.updateInvite(newStatus, inviteKey, True)
        except Exception as e:
            self.notify.warning("Unknown error in updateInvite, giving up:\n%s" % str(e))
            return ()

    def getInviteesOfParty(self, partyId, isRetry=False):
        """
        Attempts to get all invites for the given party Id

        If records are found, a tuple is returned containing all invites

        If none are found, will return an empty tuple
        """
        assert self.notify.debugCall()

        if not self.sqlAvailable:
            self.notify.warning("MySQL database is unavailable. Unable to find invites for party %s" % partyId)
            return ()

        cursor = self.database.cursor(pymysql.cursors.DictCursor)

        try:
            cursor.execute(
                """
                SELECT `guestId` FROM `invites` WHERE `partyId`='%s';
                """ % (partyId)
            )

            res = cursor.fetchall()

            return tuple(res)
        except OperationalError as e:
            if isRetry == True:
                self.notify.warning("Error on getInviteesOfParty retry, giving up:\n%s" % str(e))
                return ()
            elif e[0] == SERVER_GONE_ERROR or e[0] == SERVER_LOST:
                self.reconnect()
                return self.getInviteesOfParty(partyId, True)
            else:
                self.notify.warning("Unknown error in getInviteesOfParty, retrying:\n%s" % str(e))
                self.reconnect()
                return self.getInviteesOfParty(partyId, True)
        except Exception as e:
            self.notify.warning("Unknown error in getInviteesOfParty, giving up:\n%s" % str(e))
            return ()
