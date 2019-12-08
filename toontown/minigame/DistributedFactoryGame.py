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
import FactoryGameGlobals
from toontown.toonbase import TTLocalizer
from otp.otpbase import OTPGlobals
import Trajectory

class DistributedFactoryGame(DistributedMinigame):
    DURATION = FactoryGameGlobals.FactoryGameDuration
    IT_SPEED_INCREASE = 1.3
    IT_ROT_INCREASE = 1.3

    def __init__(self, cr):
        DistributedMinigame.__init__(self, cr)
        self.gameFSM = ClassicFSM.ClassicFSM('DistributedFactoryGame', [State.State('off', self.enterOff, self.exitOff, ['play']), State.State('play', self.enterPlay, self.exitPlay, ['showScores']), State.State('showScores', self.enterShowScores, self.exitShowScores, ['cleanup']), State.State('cleanup', self.enterCleanup, self.exitCleanup, ['off'])], 'off', 'cleanup')
        self.addChildGameFSM(self.gameFSM)
        self.walkStateData = Walk.Walk('walkDone')
        self.scorePanels = []
        self.initialPosition = (20.5, 33, 3.751, 0, 0, 0)
        self.modelCount = 4
        self.victoryTrack = None
        self.EndGameTaskName = 'endFactoryGame'

    def getTitle(self):
        return TTLocalizer.FactoryGameTitle

    def getInstructions(self):
        return TTLocalizer.FactoryGameInstructions

    def getMaxDuration(self):
        return self.DURATION

    def load(self):
        exitPos = FactoryGameGlobals.FactoryGameSiloExitPos
        self.notify.debug('load')
        DistributedMinigame.load(self)
        self.sky = loader.loadModel('phase_9/models/cogHQ/cog_sky')
        self.sky.setScale(5)
        self.ground = loader.loadModel('phase_9/models/cogHQ/SelbotLegFactory')
        self.music = base.loader.loadMusic('phase_9/audio/bgm/CHQ_FACT_bg.ogg')
        self.sSphere = CollisionSphere(exitPos[0], exitPos[1], exitPos[2] + 10, 25)
        name = self.uniqueName('victorySphere')
        self.sSphereNode = CollisionNode(name)
        self.sSphereNode.addSolid(self.sSphere)
        self.sSphereNodePath = render.attachNewNode(self.sSphereNode)
        self.sSphereNodePath.hide()
        self.sSphereBitMask = ToontownGlobals.WallBitmask
        self.sSphereNode.setCollideMask(self.sSphereBitMask)
        self.sSphere.setTangible(0)
        self.accept(self.uniqueName('entervictorySphere'), self.requestToonVictory)
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
        for i in xrange(self.numPlayers):
            avId = self.avIdList[i]
            avName = self.getAvatarName(avId)
            scorePanel = MinigameAvatarScorePanel.MinigameAvatarScorePanel(avId, avName)
            scorePanel.setPos(-0.213, 0.0, 0.28 * i + 0.66)
            scorePanel.reparentTo(base.a2dBottomRight)
            self.scorePanels.append(scorePanel)

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

        base.setCellsAvailable(base.rightCells, 1)
        base.mouseInterfaceNode.setForwardSpeed(ToontownGlobals.ToonForwardSpeed)
        base.mouseInterfaceNode.setRotateSpeed(ToontownGlobals.ToonRotateSpeed)
        base.localAvatar.cameraIndex = 0
        base.localAvatar.setCameraPositionByIndex(0)

    def enterShowScores(self):
        self.notify.debug('enterShowScores')
        lerpTrack = Parallel()
        lerpDur = 0.5
        bY = -.6
        cX = 0
        scorePanelLocs = (cX, bY)
        for i in xrange(self.numPlayers):
            panel = self.scorePanels[i]
            pos = scorePanelLocs
            panel.wrtReparentTo(aspect2d)
            lerpTrack.append(Parallel(LerpPosInterval(panel, lerpDur, Point3(pos[0], 0, pos[1]), blendType='easeInOut'), LerpScaleInterval(panel, lerpDur, Vec3(panel.getScale()) * 1.5, blendType='easeInOut')))

        self.showScoreTrack = Parallel(lerpTrack, Sequence(Wait(FactoryGameGlobals.FactoryGameShowScoresDuration), Func(self.gameOver)))
        self.showScoreTrack.start()

    def exitShowScores(self):
        self.showScoreTrack.pause()
        del self.showScoreTrack

    def timerExpired(self):
        self.notify.debug('local timer expired')
        self.setEveryoneDone()

    def enterCleanup(self):
        self.notify.debug('enterCleanup')
        self.music.stop()
        self.timer.destroy()
        del self.sSphereNode
        del self.sSphere
        del self.sSphereBitMask
        self.sSphereNodePath.removeNode()
        del self.sSphereNodePath
        del self.timer
        for panel in self.scorePanels:
            panel.cleanup()

        self.scorePanels = []
        if self.victoryTrack:
            self.victoryTrack.finish()
            del self.victoryTrack
        self.gameFSM.request('off')

    def exitCleanup(self):
        pass

    def setTreasureScore(self, scores):
        if not self.hasLocalToon:
            return
        self.notify.debug('setTreasureScore: %s' % scores)
        for i in xrange(len(self.scorePanels)):
            self.scorePanels[i].setScore(scores[i])

    def setEveryoneDone(self, delay=1):
        if not self.hasLocalToon:
            return
        if self.gameFSM.getCurrentState().getName() != 'play':
            self.notify.warning('ignoring setEveryoneDone msg')
            return
        self.notify.debug('setEveryoneDone')

        def endGame(task, self = self):
            self.gameFSM.request('showScores')
            return Task.done

        self.timer.hide()
        taskMgr.doMethodLater(delay, endGame, self.EndGameTaskName)

    def requestToonVictory(self, collEntry):
        if base.localAvatar.doId not in self.avIdList:
            return
        self.sendUpdate('handleToonVictory', [base.localAvatar.doId])

    def startVictoryMovie(self):
        self.setEveryoneDone()
        self.walkStateData.exit()
        toon = self.getAvatar(self.avIdList[0])
        track = Parallel(Func(toon.headsUp, FactoryGameGlobals.FactoryGameSiloExitPos),
                         Func(toon.loop, 'run'),
                         Sequence(LerpPosInterval(toon, 1, FactoryGameGlobals.FactoryGameSiloExitPos), Func(toon.loop, 'victory')))
        self.victoryTrack = track
        self.victoryTrack.start()

