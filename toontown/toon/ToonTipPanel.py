from panda3d.core import *
from direct.gui.DirectGui import *
from direct.directnotify import DirectNotifyGlobal
from direct.interval.IntervalGlobal import *
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownGlobals
from direct.task.Task import Task

class ToonTipPanel(DirectFrame):
    notify = DirectNotifyGlobal.directNotify.newCategory('ToonTipPanel')
    startPos = (-1.4, 0., 0.435)
    endPos = (0.617, 0, 0.435)
    tipOutFor = 10
    quickCloseTime = 0.4
    normalCloseTime = 1.0
    bgImage = DGG.getDefaultDialogGeom()

    def __init__(self):
        DirectFrame.__init__(self, relief=None, sortOrder=55, parent=base.a2dBottomLeft)
        self.queuedTips = []
        self.activeTip = None
        self.currentSequence = Sequence()
        self.exclamationPoint = loader.loadTexture('phase_3/maps/quest_exclaim.png')
        self.tipFrame = DirectFrame(parent=self, pos=self.startPos, image_scale=(1.3, 1.0, 0.6), image=self.bgImage, relief=None, scale=(1.0, 1.0, 0.5), image_color=(0.75, 0.75, 1.0, 1.0), text='')
        self.excFrame = DirectFrame(pos=(0.55, 0.5, 0), image=self.exclamationPoint, scale=(0.1, 1.0, 0.2), relief=None, image_color=(0.875, 0.875, 1.0, 1.0))
        self.frameText = DirectLabel(pos=(-0.07, 0.5, 0.05), scale=(0.05, 1.0, 0.1), sortOrder=55, text_align=TextNode.ACenter, relief=None)
        self.frameTitle = DirectLabel(pos=(-0.07, 0.5, 0.15), scale=(0.08, 1.0, 0.15), sortOrder=55, text_font=ToontownGlobals.getSignFont(), text=TTLocalizer.QuickTipTitle, text_fg=(0.6, 0.6, 1.0, 1.0), relief=None)
        buttons = loader.loadModel('phase_3/models/gui/dialog_box_buttons_gui')
        self.bCancel = DirectButton(parent=self.tipFrame, image=(
        buttons.find('**/CloseBtn_UP'), buttons.find('**/CloseBtn_DN'), buttons.find('**/CloseBtn_Rllvr')), relief=None, text='', pos=(0.61, 0.5, 0.22), command=self.__handleClose, scale=(0.9, 1.0, 1.5))
        buttons.removeNode()
        self.excFrame.reparentTo(self.tipFrame)
        self.excFrame.setTransparency(1)
        self.frameTitle.reparentTo(self.tipFrame)
        self.frameText.reparentTo(self.tipFrame)
        self.frameText['text'] = ''
        self.frameText['text_wordwrap'] = 22.65
        self.accept('showTip', self.addNewTipToList)
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
        self.currentSequence = None
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
