from panda3d.core import *
from direct.gui.DirectGui import *
from direct.directnotify import DirectNotifyGlobal
from direct.interval.IntervalGlobal import *
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownGlobals
from direct.task.Task import Task

class ToonTipPanel(DirectFrame):
    notify = DirectNotifyGlobal.directNotify.newCategory('ToonTipPanel')
    startPos = (-1.4, 0, 0.435)
    endPos = (0.617, 0, 0.435)
    tipOutFor = 10
    quickCloseTime = 0.4
    normalCloseTime = 1.0

    def __init__(self):
        DirectFrame.__init__(self, relief=None, sortOrder=55, parent=base.a2dBottomLeft)
        self.queuedTips = []
        self.activeTip = None
        self.currentSequence = Sequence()
        self.exclamationPoint = loader.loadTexture('phase_3/maps/tipExclaim.png')
        self.bgImage = loader.loadTexture('phase_3/maps/tipsPanel.png')
        gui = loader.loadModel('phase_3/models/gui/tt_m_gui_mat_mainGui')
        guiCancelUp = gui.find('**/tt_t_gui_mat_closeUp')
        guiCancelDown = gui.find('**/tt_t_gui_mat_closeDown')
        self.tipFrame = DirectFrame(parent=self, pos=self.startPos, image_scale=(1.056, 1.0, 0.87), image=self.bgImage, image_pos=(0.0, 0.0, -0.15), relief=None, scale=(1.0, 1.0, 0.5), text='')
        self.excFrame = DirectFrame(pos=(0.537, 0.5, 0), image=self.exclamationPoint, scale=(0.1, 1.0, 0.2), relief=None, image_color=(0.875, 0.875, 1.0, 1.0))
        self.frameText = DirectLabel(pos=(-0.07, 0.5, 0.05), scale=(0.05, 1.0, 0.1), sortOrder=55, text_align=TextNode.ALeft, relief=None, textMayChange=1)
        self.frameTitle = DirectLabel(pos=(-0.07, 0.5, 0.15), scale=(0.08, 1.0, 0.15), sortOrder=55, text_font=ToontownGlobals.getSignFont(), text=TTLocalizer.QuickTipTitle, text_fg=(0.0, 0.55, 1.0, 1.0), relief=None)
        self.bCancel = DirectButton(parent=self.tipFrame, image=(guiCancelUp, guiCancelDown, guiCancelUp, guiCancelDown), relief=None, pos=(0.62, 0.5, 0.227), command=self.__handleClose, scale=(0.26, 1.0, 0.52))
        gui.removeNode()
        self.excFrame.reparentTo(self.tipFrame)
        self.excFrame.setTransparency(1)
        self.tipFrame.setTransparency(1)
        self.frameTitle.reparentTo(self.tipFrame)
        self.frameText.reparentTo(self.tipFrame)
        self.frameText['text'] = ''
        self.frameText['text_wordwrap'] = 22.65
        self.accept('showTip', self.addNewTipToList)
        self.accept('clearAllTips', self.resetTipPanel)
        self.tipFrame.hide()
        self.startCheckQueueTask()

    def addNewTipToList(self, num):
        if num not in self.queuedTips and num != self.activeTip:
            self.queuedTips.append(num)
        else:
            self.notify.debug('ToonTipPanel: Duplicate tip was sent, but not shown to user. Num: %s' % num)

    def changeTipText(self, num):
        if num in TTLocalizer.ToonTipByNum.keys():
            self.frameText['text'] = TTLocalizer.ToonTipByNum[num]
            self.activeTip = num
        else:
            self.notify.debug('ToonTipPanel: Invalid Tip ID was sent. Num: %s' % num)

    def deleteAllTips(self):
        self.queuedTips = []
        self.currentSequence.finish()
        self.currentSequence = Sequence()
        self.activeTip = None

    def deleteATip(self, index):
        self.queuedTips[index] = None

    def deleteActiveTip(self):
        self.activeTip = None

    def __handleClose(self):
        taskMgr.remove(self.taskName('checkQueueTask'))
        self.currentSequence.pause()
        duration = self.normalCloseTime
        if self.queuedTips:
            duration = self.quickCloseTime
        self.currentSequence = self.createGoOutSeq(duration)
        self.currentSequence.start()
        self.startCheckQueueTask()

    def resetTipPanel(self):
        taskMgr.remove(self.taskName('checkQueueTask'))
        self.deleteAllTips()
        self.tipFrame.setPos(self.startPos)
        self.frameText['text'] = ''
        self.tipFrame.hide()

    def createTipSequence(self, num):
        self.currentSequence.finish()
        self.changeTipText(num)
        duration = self.normalCloseTime
        if self.queuedTips:
            duration = self.quickCloseTime
        self.tipFrame.show()
        comeInSeq = self.createComeInSeq(duration)
        goOutSeq = self.createGoOutSeq(duration)
        if not self.queuedTips:
            goOutSeq.append(Func(self.tipFrame.hide))
        self.currentSequence = Sequence(comeInSeq, Wait(self.tipOutFor), goOutSeq)
        self.currentSequence.start()

    def createComeInSeq(self, duration):
        return LerpPosInterval(self.tipFrame, pos=self.endPos, startPos=self.startPos, duration=duration, blendType='easeOut')

    def createGoOutSeq(self, duration):
        return Sequence(LerpPosInterval(self.tipFrame, pos=self.startPos, startPos=self.endPos, duration=duration, blendType='easeIn'), Func(self.deleteActiveTip))

    def startCheckQueueTask(self):
        taskMgr.remove(self.taskName('checkQueueTask'))
        queueTask = Task.loop(Task(self.checkQueueTask), Task.pause(0.5))
        taskMgr.add(queueTask, self.taskName('checkQueueTask'))

    def checkQueueTask(self, task):
        if self.currentSequence.isPlaying():
            return
        else:
            if self.queuedTips:
                self.createTipSequence(self.queuedTips.pop(0))
                return
            else:
                return

    def cleanup(self):
        self.resetTipPanel()
        self.excFrame.destroy()
        self.frameText.destroy()
        self.frameTitle.destroy()
        self.bCancel.destroy()
        self.tipFrame.destroy()
        self.tipFrame = None
        self.excFrame = None
        self.frameTitle = None
        self.frameText = None
        self.bCancel = None
        self.ignore('showTip')
        self.ignore('clearAllTips')
