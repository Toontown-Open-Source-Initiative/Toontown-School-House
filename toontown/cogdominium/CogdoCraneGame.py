from direct.showbase.DirectObject import DirectObject
from direct.task.Task import Task
from direct.showbase.RandomNumGen import RandomNumGen
from direct.interval.FunctionInterval import Wait
from direct.interval.IntervalGlobal import Func
from direct.interval.MetaInterval import Sequence, Parallel
from toontown.toonbase import TTLocalizer
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
        self._hints = {'targettedByEagle': False,
                       'invulnerable': False}

    def placeEntranceElevator(self, elevator):
        elevator.setPos(-10.63, 0, 6.03)
        elevator.setHpr(90, 0, 0)

    def load(self):
        self.audioMgr = CogdoGameAudioManager(Globals.MusicFiles, Globals.SfxFiles, base.localAvatar,
                                              cutoff=Globals.Cutoff)
        self.guiMgr = CogdoCraneGuiManager(self.distGame.geomRoot)

    def unload(self):
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
        base.camLens.setMinFov(ToontownGlobals.BossBattleCameraFov / (4.0 / 3.0))

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

    def exit(self):
        self.guiMgr.stopTimer()
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

    def handleLocalPlayerInvulnerable(self):
        if not self._hints['invulnerable']:
            #self.guiMgr.setMessage(TTLocalizer.CogdoFlyingGameYouAreInvincible)
            self._hints['invulnerable'] = True

    def handleLocalPlayerPickedUpFirstPropeller(self):
        #self.guiMgr.setMessage(TTLocalizer.CogdoFlyingGamePressCtrlToFly)
        #self.guiMgr.presentRefuelGui()
        return

    def gameComplete(self):
        return
