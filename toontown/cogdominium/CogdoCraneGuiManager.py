from panda3d.core import NodePath
from toontown.toonbase import ToontownIntervals
from toontown.toonbase.ToontownTimer import ToontownTimer
from CogdoGameMessageDisplay import CogdoGameMessageDisplay
from CogdoMemoGui import CogdoMemoGui


class CogdoCraneGuiManager:
    ClearMessageDisplayEventName = 'ClearMessageDisplayEvent'
    FirstPressOfCtrlEventName = 'FirstPressOfCtrlEvent'
    StartRunningOutOfTimeMusicEventName = 'StartRunningOutOfTimeEvent'

    def __init__(self, geom):
        self.geom = geom
        self.root = NodePath('CogdoCraneGui')
        self.root.reparentTo(aspect2d)
        self.root.stash()
        self._initTimer()
        self._initHud()
        self._initMessageDisplay()
        self.sentTimeRunningOutMessage = False

    def _initHud(self):
        self._memoGui = CogdoMemoGui(self.root, 'memo_card')
        self._memoGui.posNextToLaffMeter()

    def _initTimer(self):
        self._timer = ToontownTimer()
        self._timer.hide()
        self._timer.posInTopRightCorner()

    def _initMessageDisplay(self):
        audioMgr = base.cogdoGameAudioMgr
        sound = audioMgr.createSfx('popupHelpText')
        self._messageDisplay = CogdoGameMessageDisplay('CogdoCraneMessageDisplay', self.root, sfx=sound)

    def destroyTimer(self):
        if self._timer is not None:
            self._timer.stop()
            self._timer.destroy()
            self._timer = None
        return

    def onstage(self):
        self.root.unstash()

    def presentTimerGui(self):
        ToontownIntervals.start(ToontownIntervals.getPresentGuiIval(self._timer, 'present_timer_gui'))

    def offstage(self):
        self.root.stash()
        self.hideTimer()

    def startTimer(self, duration, timerExpiredCallback = None, keepHidden = False):
        if self._timer is None:
            self._initTimer()
        self._timer.setTime(duration)
        self._timer.countdown(duration, timerExpiredCallback)
        if keepHidden:
            self.hideTimer()
        else:
            self.showTimer()
        return

    def stopTimer(self):
        if hasattr(self, '_timer') and self._timer is not None:
            self.hideTimer()
            self._timer.stop()
        return

    def showTimer(self):
        self._timer.show()

    def hideTimer(self):
        self._timer.hide()

    def forceTimerDone(self):
        if self._timer.countdownTask != None:
            self._timer.countdownTask.duration = 0
        return

    def setMessage(self, text, color = None, transition = 'fade'):
        self._messageDisplay.updateMessage(text, color, transition)

    def setTemporaryMessage(self, text, duration = 3.0, color = None):
        self._messageDisplay.showMessageTemporarily(text, duration, color)

    def setMemoCount(self, score):
        self._memoGui.setCount(score)

    def destroy(self):
        ToontownIntervals.cleanup('present_timer_gui')
        ToontownIntervals.cleanup('present_memo_gui')
        self._memoGui.destroy()
        self._memoGui = None
        self.destroyTimer()
        self._messageDisplay.destroy()
        self._messageDisplay = None
        self.root.removeNode()
        self.root = None
        return
