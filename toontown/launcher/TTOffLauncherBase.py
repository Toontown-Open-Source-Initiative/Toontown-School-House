import __builtin__
import os
import string
import sys
import time

from panda3d.core import *
from direct.directnotify.DirectNotifyGlobal import *
from direct.showbase import DConfig
from direct.task.MiniTask import MiniTask, MiniTaskManager
from otp.launcher.LauncherBase import LauncherBase, LogAndOutput

class TTOffLauncherBase(LauncherBase):

    def __init__(self):
        self.started = False
        self.taskMgrStarted = False
        self._downloadComplete = True
        self.pandaErrorCode = 0
        self.WIN32 = os.name == 'nt'
        ltime = time.localtime()
        logSuffix = '%02d%02d%02d_%02d%02d%02d' % (ltime[0] - 2000,
            ltime[1],
            ltime[2],
            ltime[3],
            ltime[4],
            ltime[5])
        if not os.path.exists('logs/'):
            os.makedirs('logs/')
        logfile = os.path.join('logs', self.getLogFileName() + '-' + logSuffix + '.log')
        self.errorfile = 'errorCode'
        log = open(logfile, 'a')
        logOut = LogAndOutput(sys.__stdout__, log)
        logErr = LogAndOutput(sys.__stderr__, log)
        sys.stdout = logOut
        sys.stderr = logErr
        print '\n\nStarting %s...' % self.GameName
        print 'Current time: ' + time.asctime(time.localtime(time.time())) + ' ' + time.tzname[0]
        print 'sys.path = ', sys.path
        print 'sys.argv = ', sys.argv
        print 'generating standard configrc'
        launcherConfig = DConfig
        __builtin__.config = launcherConfig
        if config.GetBool('log-private-info', 0):
            print 'os.environ = ', os.environ
        self.miniTaskMgr = MiniTaskManager()
        self.setServerVersion(launcherConfig.GetString('server-version', 'no_version_set'))
        self.ServerVersionSuffix = launcherConfig.GetString('server-version-suffix', '')
        self.nout = MultiplexStream()
        Notify.ptr().setOstreamPtr(self.nout, 0)
        self.nout.addFile(Filename(logfile))
        if launcherConfig.GetBool('console-output', 0):
            self.nout.addStandardOutput()
            sys.stdout.console = True
            sys.stderr.console = True
        self.notify = directNotify.newCategory('TTOffLauncher')
        self.clock = TrueClock.getGlobalPtr()
        self.logPrefix = self.getLogFileName() + '-'
        self.testServerFlag = self.getTestServerFlag()
        self.notify.info('isTestServer: %s' % self.testServerFlag)
        self.gameServer = self.getGameServer()
        if self.gameServer:
            gameServer = self.gameServer
        else:
            gameServer = '127.0.0.1'
        self.notify.info('Game Server %s' % gameServer)
        self.goUserName = ''
        self.lastLauncherMsg = None
        self.setRegistry(self.GameLogFilenameKey, logfile)
        self.currentPhase = 4
        if self.getServerVersion() == 'no_version_set':
            self.setPandaErrorCode(10)
            self.notify.info('Aborting, Configrc did not run!')
            sys.exit()
        self.launcherMessage(self.Localizer.LauncherStartingMessage)
        self.http = HTTPClient()
        if self.http.getProxySpec() == '':
            self.http.setProxySpec(self.getValue(self.ProxyServerKey, ''))
            self.http.setDirectHostSpec(self.getValue(self.ProxyDirectHostsKey, ''))
        if self.http.getProxySpec() != '':
            self.notify.info('Proxy spec is: %s' % self.http.getProxySpec())
        if self.http.getDirectHostSpec() != '':
            self.notify.info('Direct hosts list is: %s' % self.http.getDirectHostSpec())

        self.foreground()
        return

    def getPhaseComplete(self, phase):
        # don't know how well this is gonna be
        # but, the basic idea is-
        return True
