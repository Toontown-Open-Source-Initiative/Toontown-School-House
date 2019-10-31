import os
import sys
import time
import types

ltime = 1 and time.localtime()
logSuffix = '%02d%02d%02d_%02d%02d%02d' % (ltime[0] - 2000,  ltime[1], ltime[2],
                                           ltime[3], ltime[4], ltime[5])

logfile = os.path.join('logs', 'ttoffD-' + logSuffix + '.log')

class LogAndOutput:
    def __init__(self, orig, log):
        self.orig = orig
        self.log = log

    def write(self, str):
        self.log.write(str)
        self.log.flush()
        self.orig.write(str)
        self.orig.flush()

    def flush(self):
        self.log.flush()
        self.orig.flush()

if not os.path.exists('logs/'):
    os.mkdir('logs/')

log = open(logfile, 'a')
logOut = LogAndOutput(sys.__stdout__, log)
logErr = LogAndOutput(sys.__stderr__, log)
sys.stdout = logOut
sys.stderr = logErr

print('\n\nStarting Toontown Online...')

if 1:
    print 'Current time: ' + time.asctime(time.localtime(time.time())) + ' ' + time.tzname[0]
    print 'sys.path = ', sys.path
    print 'sys.argv = ', sys.argv

from otp.otpbase import OTPLauncherGlobals
from panda3d.core import *
from toontown.launcher.TTOffLauncherBase import TTOffLauncherBase
from toontown.toonbase import TTLocalizer

class TTOffLauncher(TTOffLauncherBase):
    GameName = 'Toontown Online'
    LauncherPhases = [3, 3.5, 4, 5, 5.5, 6, 7, 8, 9, 10, 11, 12, 13]
    TmpOverallMap = [0.25, 0.15, 0.12, 0.17, 0.08, 0.07, 0.05, 0.05, 0.017,
                     0.011, 0.01, 0.012, 0.01]
    ForegroundSleepTime = 0.01
    Localizer = TTLocalizer
    VerifyFiles = 1
    DecompressMultifiles = True

    def __init__(self):
        self.ttoffPlayTokenKey = 'TTOFF_PLAYTOKEN'
        self.launcherMessageKey = 'LAUNCHER_MESSAGE'
        self.game1DoneKey = 'GAME1_DONE'
        self.game2DoneKey = 'GAME2_DONE'
        self.tutorialCompleteKey = 'TUTORIAL_DONE'
        TTOffLauncherBase.__init__(self)
        self.parseWebAcctParams()
        self.mainLoop()

    def getValue(self, key, default=None):
        try:
            return self.getRegistry(key, default)
        except:
            return self.getRegistry(key)

    def setValue(self, key, value):
        self.setRegistry(key, value)

    def getVerifyFiles(self):
        return 1

    def getTestServerFlag(self):
        return self.testServerFlag

    def getGameServer(self):
        return self.gameServer

    def getLogFileName(self):
        return 'ttoff'

    def parseWebAcctParams(self):
        self.secretNeedsParentPasswordKey = 0
        self.notify.info('secretNeedsParentPassword = %d' % self.secretNeedsParentPasswordKey)
        self.chatEligibleKey = 1
        self.notify.info('chatEligibleKey = %d' % self.chatEligibleKey)

    def getBlue(self):
        return None

    def getPlayToken(self):
        playToken = self.getValue(self.ttoffPlayTokenKey)
        self.setValue(self.ttoffPlayTokenKey, '')
        if playToken == 'NO PLAYTOKEN':
            playToken = None
        return playToken

    def setRegistry(self, name, value):
        pass

    def getRegistry(self, name, missingValue=None):
        self.notify.info('getRegistry%s' % ((name, missingValue),))
        if missingValue == None:
            missingValue = ''
        value = os.environ.get(name, missingValue)
        try:
            value = int(value)
        except: pass
        return value

    def getCDDownloadPath(self, origPath, serverFilePath):
        return '%s/%s%s/CD_%d/%s' % (origPath, self.ServerVersion, self.ServerVersionSuffix, self.fromCD, serverFilePath)

    def getDownloadPath(self, origPath, serverFilePath):
        return '%s/%s%s/%s' % (origPath, self.ServerVersion, self.ServerVersionSuffix, serverFilePath)

    def getPercentPatchComplete(self, bytesWritten):
        if self.totalPatchDownload:
            return TTOffLauncherBase.getPercentPatchComplete(self, bytesWritten)
        else:
            return 0

    def hashIsValid(self, serverHash, hashStr):
        return serverHash.setFromDec(hashStr) or serverHash.setFromHex(hashStr)

    def launcherMessage(self, msg):
        TTOffLauncherBase.launcherMessage(self, msg)
        self.setRegistry(self.launcherMessageKey, msg)

    def getAccountServer(self):
        return self.accountServer

    def setTutorialComplete(self):
        self.setRegistry(self.tutorialCompleteKey, 0)

    def getTutorialComplete(self):
        return self.getRegistry(self.tutorialCompleteKey, 0)

    def getGame2Done(self):
        return self.getRegistry(self.game2DoneKey, 0)

    def getNeedPwForSecretKey(self):
        return self.secretNeedsParentPasswordKey

    def getParentPasswordSet(self):
        return self.chatEligibleKey

    def startGame(self):
        self.newTaskManager()

        from direct.showbase.EventManagerGlobal import eventMgr
        eventMgr.restart()

        from toontown.toonbase import ToontownStart
