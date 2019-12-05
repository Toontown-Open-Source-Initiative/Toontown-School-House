from panda3d.core import *
from toontown.toonbase.ToonBaseGlobal import *
from DistributedMinigame import *
from direct.interval.IntervalGlobal import *
from direct.fsm import ClassicFSM, State
from direct.fsm import State
from toontown.safezone import Walk
from toontown.toonbase import ToontownTimer
from direct.gui import OnscreenText
import MinigameAvatarScorePanel
from direct.distributed import DistributedSmoothNode
import random
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from otp.otpbase import OTPGlobals
import Trajectory

class DistributedFactoryGame(DistributedMinigame):
    DURATION = 180
    IT_SPEED_INCREASE = 1.3
    IT_ROT_INCREASE = 1.3

    def __init__(self, cr):
        DistributedMinigame.__init__(self, cr)
        self.gameFSM = ClassicFSM.ClassicFSM('DistributedFactoryGame', [State.State('off', self.enterOff, self.exitOff, ['play']), State.State('play', self.enterPlay, self.exitPlay, ['cleanup']), State.State('cleanup', self.enterCleanup, self.exitCleanup, ['off'])], 'off', 'off')
        self.addChildGameFSM(self.gameFSM)
        self.walkStateData = Walk.Walk('walkDone')
        self.initialPosition = (20.5, 33, 3.751, 0, 0, 0)
        self.modelCount = 4

    def getTitle(self):
        return TTLocalizer.FactoryGameTitle

    def getInstructions(self):
        return TTLocalizer.FactoryGameInstructions

    def getMaxDuration(self):
        return self.DURATION

    def load(self):
        self.notify.debug('load')
        DistributedMinigame.load(self)
        self.sky = loader.loadModel('phase_9/models/cogHQ/cog_sky')
        self.sky.setScale(5)
        self.ground = loader.loadModel('phase_9/models/cogHQ/SelbotLegFactory')
        self.music = base.loader.loadMusic('phase_9/audio/bgm/CHQ_FACT_bg.ogg')
        self.tracks = []
        return

    def unload(self):
        self.notify.debug('unload')
        DistributedMinigame.unload(self)
        self.ignoreAll()
        del self.tracks
        self.ground.removeNode()
        del self.ground
        del self.music
        self.removeChildGameFSM(self.gameFSM)
        del self.gameFSM

    def onstage(self):
        self.notify.debug('onstage')
        DistributedMinigame.onstage(self)
        self.ground.reparentTo(render)
        self.sky.reparentTo(render)
        base.localAvatar.setPosHpr(*self.initialPosition)
        base.localAvatar.reparentTo(render)
        base.localAvatar.loop('neutral')
        camera.reparentTo(render)
        camera.setPosHpr(20, 10, 16, 0, -30, 0)
        base.camLens.setFar(450.0)
        base.transitions.irisIn(0.4)
        NametagGlobals.setMasterArrowsOn(1)
        DistributedSmoothNode.activateSmoothing(1, 1)
        return

    def offstage(self):
        self.notify.debug('offstage')
        DistributedSmoothNode.activateSmoothing(1, 0)
        NametagGlobals.setMasterArrowsOn(0)
        DistributedMinigame.offstage(self)
        self.sky.reparentTo(hidden)
        self.ground.reparentTo(hidden)
        base.camLens.setFar(ToontownGlobals.DefaultCameraFar)

    def setGameReady(self):
        if not self.hasLocalToon:
            return
        self.notify.debug('setGameReady')
        if DistributedMinigame.setGameReady(self):
            return

        for i in xrange(self.numPlayers):
            avId = self.avIdList[i]
            avatar = self.getAvatar(avId)
            if avatar:
                avatar.startSmooth()

        base.localAvatar.setPosHpr(*self.initialPosition)
        base.localAvatar.d_clearSmoothing()
        base.localAvatar.sendCurrentPosition()
        base.localAvatar.b_setAnimState('neutral', 1)
        base.localAvatar.b_setParent(ToontownGlobals.SPRender)

    def setGameStart(self, timestamp):
        if not self.hasLocalToon:
            return
        self.notify.debug('setGameStart')
        DistributedMinigame.setGameStart(self, timestamp)
        self.gameFSM.request('play')

    def enterOff(self):
        self.notify.debug('enterOff')

    def exitOff(self):
        pass

    def enterPlay(self):
        self.notify.debug('enterPlay')

        base.setCellsAvailable(base.rightCells, 0)
        self.walkStateData.enter()
        self.walkStateData.fsm.request('walking')
        self.timer = ToontownTimer.ToontownTimer()
        self.timer.posInTopRightCorner()
        self.timer.setTime(self.DURATION)
        self.timer.countdown(self.DURATION, self.timerExpired)
        base.playMusic(self.music, looping=1, volume=0.9)
        base.localAvatar.setIdealCameraPos(Point3(0, -24, 8))

    def exitPlay(self):
        for task in self.tracks:
            task.finish()

        self.tracks = []
        for avId in self.avIdList:
            toon = self.getAvatar(avId)
            if toon:
                toon.getGeomNode().clearMat()
                toon.scale = 1.0
                toon.rescaleToon()

        self.walkStateData.exit()
        self.music.stop()
        self.timer.destroy()
        del self.timer

        base.setCellsAvailable(base.rightCells, 1)
        base.mouseInterfaceNode.setForwardSpeed(ToontownGlobals.ToonForwardSpeed)
        base.mouseInterfaceNode.setRotateSpeed(ToontownGlobals.ToonRotateSpeed)
        base.localAvatar.cameraIndex = 0
        base.localAvatar.setCameraPositionByIndex(0)

    def timerExpired(self):
        self.notify.debug('local timer expired')
        self.gameOver()

    def enterCleanup(self):
        self.notify.debug('enterCleanup')
        self.gameFSM.request('off')

    def exitCleanup(self):
        pass

