from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.showbase.DirectObject import DirectObject
from direct.showbase.RandomNumGen import RandomNumGen
from direct.task.Task import Task

from otp.otpbase import OTPGlobals

from panda3d.core import *
from panda3d.physics import *

from toontown.toonbase import ToontownGlobals

import CogdoCraneGameGlobals as Globals
from CogdoGameAudioManager import CogdoGameAudioManager
from CogdoCraneGameMovies import CogdoCraneGameIntro, CogdoCraneGameFinish
from CogdoCraneGuiManager import CogdoCraneGuiManager


class CogdoCraneGame(DirectObject):
    notify = directNotify.newCategory('CogdoCraneGame')
    UpdateTaskName = 'CogdoCraneGameUpdate'
    FirstPressOfCtrlTaskName = 'FirstPressOfCtrlTask'

    def __init__(self, distGame):
        self.distGame = distGame
        self.toonId2Player = {}
        self.players = []
        self.isGameComplete = False
        self._hints = {'targettedByBags': False}

    def placeEntranceElevator(self, elevator):
        elevator.setPos(-10.63, 0, 6.03)
        elevator.setHpr(90, 0, 0)

    def load(self):
        self.audioMgr = CogdoGameAudioManager(Globals.MusicFiles, Globals.SfxFiles, base.localAvatar,
                                              cutoff=Globals.Cutoff)

        self.lightning = loader.loadModel('phase_10/models/cogHQ/CBLightning.bam')
        self.magnet = loader.loadModel('phase_10/models/cogHQ/CBMagnet.bam')
        self.craneArm = loader.loadModel('phase_10/models/cogHQ/CBCraneArm.bam')
        self.controls = loader.loadModel('phase_10/models/cogHQ/CBCraneControls.bam')
        self.stick = loader.loadModel('phase_10/models/cogHQ/CBCraneStick.bam')
        self.cableTex = self.craneArm.findTexture('MagnetControl')
        self.moneyBag = loader.loadModel('phase_10/models/cashbotHQ/MoneyBag')
        self.geomRoot = NodePath('geom')
        self.sceneRoot = self.geomRoot.attachNewNode('sceneRoot')
        self.physicsMgr = PhysicsManager()
        integrator = LinearEulerIntegrator()
        self.physicsMgr.attachLinearIntegrator(integrator)
        fn = ForceNode('gravity')
        self.fnp = self.geomRoot.attachNewNode(fn)
        gravity = LinearVectorForce(0, 0, Globals.Settings.Gravity.get()) # Will this fuck up? Who knows
        fn.addForce(gravity)
        self.physicsMgr.addLinearForce(gravity)
        self._gravityForce = gravity
        self._gravityForceNode = fn

        self.level = loader.loadModel(Globals.LevelFilePath)
        self.level.reparentTo(self.geomRoot)
        self.level.findAllMatches('**/MagnetArms').detach()
        self.level.findAllMatches('**/Safes').detach()
        self.level.findAllMatches('**/MagnetControlsAll').detach()
        cn = self.level.find('**/wallsCollision').node()
        cn.setIntoCollideMask(OTPGlobals.WallBitmask | ToontownGlobals.PieBitmask | BitMask32.lowerOn(3) << 21)
        walls = self.level.find('**/RollUpFrameCillison')
        walls.detachNode()
        floor = self.level.find('**/EndVaultFloorCollision')
        floor.detachNode()
        self.evFloor = self.replaceCollisionPolysWithPlanes(floor)
        self.evFloor.reparentTo(self.level)
        self.evFloor.setName('floor')
        plane = CollisionPlane(Plane(Vec3(0, 0, 1), Point3(0, 0, -50)))
        planeNode = CollisionNode('dropPlane')
        planeNode.addSolid(plane)
        planeNode.setCollideMask(ToontownGlobals.PieBitmask)
        self.geomRoot.attachNewNode(planeNode)
        self.guiMgr = CogdoCraneGuiManager(self.geomRoot)

    def getSceneRoot(self):
        return self.sceneRoot

    def replaceCollisionPolysWithPlanes(self, model):
        newCollisionNode = CollisionNode('collisions')
        newCollideMask = BitMask32(0)
        planes = []
        collList = model.findAllMatches('**/+CollisionNode')
        if not collList:
            collList = [model]
        for cnp in collList:
            cn = cnp.node()
            if not isinstance(cn, CollisionNode):
                self.notify.warning('Not a collision node: %s' % repr(cnp))
                break
            newCollideMask = newCollideMask | cn.getIntoCollideMask()
            for i in xrange(cn.getNumSolids()):
                solid = cn.getSolid(i)
                if isinstance(solid, CollisionPolygon):
                    plane = Plane(solid.getPlane())
                    planes.append(plane)
                else:
                    self.notify.warning('Unexpected collision solid: %s' % repr(solid))
                    newCollisionNode.addSolid(plane)

        newCollisionNode.setIntoCollideMask(newCollideMask)
        threshold = 0.1
        planes.sort(lambda p1, p2: p1.compareTo(p2, threshold))
        lastPlane = None
        for plane in planes:
            if lastPlane == None or plane.compareTo(lastPlane, threshold) != 0:
                cp = CollisionPlane(plane)
                newCollisionNode.addSolid(cp)
                lastPlane = plane

        return NodePath(newCollisionNode)

    def unload(self):
        self.fnp.removeNode()
        self.physicsMgr.clearLinearForces()
        self.geomRoot.removeNode()
        self._gravityForce = None
        self._gravityForceNode = None

        for player in self.players:
            player.unload()

        del self.players[:]
        self.toonId2Player.clear()

        self.audioMgr.destroy()
        del self.audioMgr
        self.ignoreAll()
        del self.distGame

    def onstage(self):
        return

    def offstage(self):
        return

    def startIntro(self):
        self._movie = CogdoCraneGameIntro(RandomNumGen(self.distGame.doId))
        self._movie.load()
        self._movie.play()
        self.audioMgr.playMusic('normal')

    def endIntro(self):
        self._movie.end()
        self._movie.unload()
        del self._movie

    def startFinish(self):
        self._movie = CogdoCraneGameFinish(self.players)
        self._movie.load()
        self._movie.play()
        self.audioMgr.playMusic('end')

    def endFinish(self):
        self._movie.end()
        self._movie.unload()
        del self._movie
        self.audioMgr.stopMusic()

    def start(self):
        timeLeft = Globals.GameDuration
        self.guiMgr.startTimer(timeLeft)
        self._physicsTask = taskMgr.add(self._doPhysics, self.distGame.uniqueName('physics'), priority=25)
        base.camLens.setMinFov(ToontownGlobals.BossBattleCameraFov / (4.0 / 3.0))

    def _doPhysics(self, task):
        dt = globalClock.getDt()
        self.physicsMgr.doPhysics(dt)
        return Task.cont

    def exit(self):
        self.guiMgr.stopTimer()
        self._physicsTask.remove()
        base.camLens.setMinFov(ToontownGlobals.DefaultCameraFov / (4.0 / 3.0))

    def _handleTimerExpired(self):
        return

    def _addPlayer(self, player):
        self.players.append(player)
        self.toonId2Player[player.toon.doId] = player
        toon = player.toon
        self.accept(toon.uniqueName('disable'), self._removePlayer, extraArgs=[toon.doId])

    def _removePlayer(self, toonId):
        if toonId in self.toonId2Player:
            player = self.toonId2Player[toonId]
            self.players.remove(player)
            del self.toonId2Player[toonId]
            player.exit()
            player.unload()

    def setToonSad(self, toonId):
        player = self.toonId2Player[toonId]
        if player == base.localAvatar.getDoId():
            player.goSad()
            self.exit()
        else:
            player.exit()

    def setToonDisconnect(self, toonId):
        player = self.toonId2Player[toonId]
        if player == base.localAvatar.getDoId():
            self.exit()
        else:
            player.exit()

    def toonDied(self, toonId, elapsedTime):
        player = self.toonId2Player[toonId]
        if player is not None:
            player.died(elapsedTime)
        return

    def toonSpawn(self, toonId, elapsedTime):
        player = self.toonId2Player[toonId]
        if player is not None:
            player.spawn(elapsedTime)
        return

    def handleTimeRunningOut(self):
        self.audioMgr.playMusic('timeRunningOut')
        #self.guiMgr.presentTimerGui()
        #self.guiMgr.setTemporaryMessage(TTLocalizer.CogdoFlyingGameTimeIsRunningOut)

    def handlePlayWaitingMusic(self):
        self.audioMgr.playMusic('waiting')

    def handleLocalPlayerFirstPressOfCtrl(self):
        #self.doMethodLater(3.0, self.guiMgr.setMessage, CogdoCraneGame.FirstPressOfCtrlTaskName, extraArgs=[''])
        return

    def handleLocalPlayerRanOutOfTime(self):
        #self.guiMgr.setMemoCount(0)
        self.distGame.d_sendRequestAction(Globals.AI.GameActions.RanOutOfTimePenalty, 0)
        #self.guiMgr.setMessage(TTLocalizer.CogdoFlyingGameTakingMemos)

    def handleClearGuiMessage(self):
        #if not self.localPlayer.isInvulnerable():
            #self.guiMgr.setMessage('')
        return

    def gameComplete(self):
        return
