from direct.directnotify import DirectNotifyGlobal
from direct.gui import DirectGui
from direct.fsm import ClassicFSM, State
from direct.fsm import State
from panda3d.core import *
from toontown.hood import ZoneUtil
from toontown.safezone.SafeZoneLoader import SafeZoneLoader
from toontown.safezone.GZPlayground import GZPlayground
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownGlobals
import random
from direct.interval.IntervalGlobal import *

class GZSafeZoneLoader(SafeZoneLoader):

    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.musicFile = 'phase_6/audio/bgm/GZ_SZ.ogg'
        self.activityMusicFile = 'phase_6/audio/bgm/GS_KartShop.ogg'
        self.dnaFile = 'phase_6/dna/golf_zone_sz.pdna'
        self.safeZoneStorageDNAFile = 'phase_6/dna/storage_GZ_sz.pdna'
        del self.fsm
        self.fsm = ClassicFSM.ClassicFSM('SafeZoneLoader', [State.State('start', self.enterStart, self.exitStart, ['quietZone', 'playground', 'toonInterior']),
         State.State('playground', self.enterPlayground, self.exitPlayground, ['quietZone', 'golfcourse']),
         State.State('toonInterior', self.enterToonInterior, self.exitToonInterior, ['quietZone']),
         State.State('quietZone', self.enterQuietZone, self.exitQuietZone, ['playground', 'toonInterior', 'golfcourse']),
         State.State('golfcourse', self.enterGolfCourse, self.exitGolfCourse, ['quietZone', 'playground']),
         State.State('final', self.enterFinal, self.exitFinal, ['start'])], 'start', 'final')

    def load(self):
        SafeZoneLoader.load(self)
        self.birdSound = map(base.loadSfx, ['phase_4/audio/sfx/SZ_TC_bird1.ogg', 'phase_4/audio/sfx/SZ_TC_bird2.ogg', 'phase_4/audio/sfx/SZ_TC_bird3.ogg'])

        self.roamingkart = loader.loadModel('phase_6/models/golf/golf_cart3')
        self.roamingkart.reparentTo(self.geom)
        self.roamingkart.setPos(-28,-29,0.026)
        self.golfball = loader.loadModel('phase_6/models/golf/golf_ball')
        self.golfball.reparentTo(self.geom)
        self.golfball.setPos(2,74,11)
        self.interval = Sequence(LerpHprInterval(self.roamingkart, 0.00001, (94,0,0)),
                LerpPosInterval(self.roamingkart, 0.01, (-28, -29, 0.026)),
                LerpPosInterval(self.roamingkart, 9, (38, -27, 0.026)),
                LerpHprInterval(self.roamingkart, 1, (145,0,0)),
                LerpPosInterval(self.roamingkart, 7, (66, 16, 0.026)),
                LerpHprInterval(self.roamingkart, 1, (225,0,0)),
                LerpPosInterval(self.roamingkart, 7, (24, 56, 0.026)),
                LerpHprInterval(self.roamingkart, 1, (295,0,0)),
                LerpPosInterval(self.roamingkart, 7, (-44, 26, 0.026)), 
                LerpHprInterval(self.roamingkart, 1, (336,0,0)),
                LerpPosInterval(self.roamingkart, 7, (-60, -13, 0.026)),
                LerpColorScaleInterval(self.roamingkart, 0.00001, (1.0, 0, 0, 1.0)),
                LerpScaleInterval(self.roamingkart, 0.5, (1.3)),
                LerpScaleInterval(self.roamingkart, 0.5, (0.00001)),
                LerpColorScaleInterval(self.roamingkart, 0.1, (1, 1, 1, 1)),
				LerpPosInterval(self.roamingkart, 0.00001, (-28, -29, 300)),
                LerpScaleInterval(self.roamingkart, 0.00001, (1)),
                LerpHprInterval(self.roamingkart, 0.00001, (94,0,0)),
                LerpPosInterval(self.roamingkart, 1, (-28, -29, 0.026)),
                LerpPosInterval(self.roamingkart, 0.3, (-28, -29, 2)),
                LerpPosInterval(self.roamingkart, 0.2, (-28, -29, 0.026)),
                LerpPosInterval(self.roamingkart, 0.50, (-28, -29, 0.026)),
            )
        self.interval.loop()

    def unload(self):
        del self.birdSound
        del self.roamingkart
        del self.golfball
        SafeZoneLoader.unload(self)

    def enterPlayground(self, requestStatus):
        self.playgroundClass = GZPlayground
        SafeZoneLoader.enterPlayground(self, requestStatus)
        top = self.geom.find('**/linktunnel_bosshq_10000_DNARoot')
        sign = top.find('**/Sign_5')
        sign.node().setEffect(DecalEffect.make())
        locator = top.find('**/sign_origin')
        signText = DirectGui.OnscreenText(text=TextEncoder.upper(TTLocalizer.BossbotHQ[-1]), font=ToontownGlobals.getSuitFont(), scale=TTLocalizer.GZSZLsignText, fg=(0, 0, 0, 1), mayChange=False, parent=sign)
        signText.setPosHpr(locator, 0, 0, -0.3, 0, 0, 0)
        signText.setDepthWrite(0)

    def exitPlayground(self):
        taskMgr.remove('titleText')
        self.hood.hideTitleText()
        SafeZoneLoader.exitPlayground(self)
        self.playgroundClass = None
        return

    def handlePlaygroundDone(self):
        status = self.place.doneStatus
        if self.enteringAGolfCourse(status) and status.get('shardId') == None:
            zoneId = status['zoneId']
            self.fsm.request('quietZone', [status])
        elif ZoneUtil.getBranchZone(status['zoneId']) == self.hood.hoodId and status['shardId'] == None:
            self.fsm.request('quietZone', [status])
        else:
            self.doneStatus = status
            messenger.send(self.doneEvent)
        return

    def enteringARace(self, status):
        if not status['where'] == 'golfcourse':
            return 0
        if ZoneUtil.isDynamicZone(status['zoneId']):
            return status['hoodId'] == self.hood.hoodId
        else:
            return ZoneUtil.getHoodId(status['zoneId']) == self.hood.hoodId

    def enteringAGolfCourse(self, status):
        if not status['where'] == 'golfcourse':
            return 0
        if ZoneUtil.isDynamicZone(status['zoneId']):
            return status['hoodId'] == self.hood.hoodId
        else:
            return ZoneUtil.getHoodId(status['zoneId']) == self.hood.hoodId

    def enterGolfCourse(self, requestStatus):
        if 'curseId' in requestStatus:
            self.golfCourseId = requestStatus['courseId']
        else:
            self.golfCourseId = 0
        self.accept('raceOver', self.handleRaceOver)
        self.accept('leavingGolf', self.handleLeftGolf)
        base.transitions.irisOut(t=0.2)

    def exitGolfCourse(self):
        del self.golfCourseId

    def handleRaceOver(self):
        print 'you done!!'

    def handleLeftGolf(self):
        req = {'loader': 'safeZoneLoader',
         'where': 'playground',
         'how': 'teleportIn',
         'zoneId': 17000,
         'hoodId': 17000,
         'shardId': None}
        self.fsm.request('quietZone', [req])
        return
