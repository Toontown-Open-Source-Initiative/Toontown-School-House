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
    bgImage = DGG.getDefaultDialogGeom()

    def __init__(self):
        DirectFrame.__init__(self, relief=None, sortOrder=55, parent=base.a2dBottomLeft)
        self.queuedTips = []
        self.activeTip = None
        self.currentSequence = Sequence()
        self.exclamationPoint = loader.loadTexture('phase_3/maps/quest_exclaim.png')
        self.accept('showTip', self.createNewTip)

    def createNewTip(self, num):
        newFrame = DirectFrame(parent=self, pos=self.startPos, image_scale=(1.3, 1.0, 0.6), image=self.bgImage, relief=None, scale=(1.0, 1.0, 0.5), image_color=(0.75, 0.75, 1.0, 1.0), text='')
        excFrame = DirectFrame(pos=(0.55, 0.5, 0), image=self.exclamationPoint, scale=(0.1, 1.0, 0.2), relief=None, image_color=(0.875, 0.875, 1.0, 1.0))
        frameText = DirectLabel(pos=(-0.07, 0.5, 0.05), scale=(0.05, 1.0, 0.1), sortOrder=55, text_align=TextNode.ACenter, relief=None)
        frameTitle = DirectLabel(pos=(-0.07, 0.5, 0.15), scale=(0.08, 1.0, 0.15), sortOrder=55, text_font=ToontownGlobals.getSignFont(), text=TTLocalizer.QuickTipTitle, text_fg=(0.6, 0.6, 1.0, 1.0), relief=None)
        excFrame.reparentTo(newFrame)
        excFrame.setTransparency(1)
        frameTitle.reparentTo(newFrame)
        frameText.reparentTo(newFrame)
        frameText['text'] = TTLocalizer.ToonTipByNum[num]
        frameText['text_wordwrap'] = 22.65
        buttons = loader.loadModel('phase_3/models/gui/dialog_box_buttons_gui')
        self.bCancel = DirectButton(parent=newFrame, image=(
            buttons.find('**/CloseBtn_UP'), buttons.find('**/CloseBtn_DN'), buttons.find('**/CloseBtn_Rllvr')),
                                    relief=None, text='', pos=(0.5, 0.5, 0.18), command=self.__handleClose, scale=(0.6, 1.0, 1.0))
        buttons.removeNode()
        if self.activeTip is not None:
            self.addNewTipToList(newFrame)
        else:
            self.createTipSequence(newFrame)

    def addNewTipToList(self, frame):
        self.queuedTips.append(frame)
        self.startCheckQueueTask()

    def deleteAllTips(self):
        for tip in self.queuedTips:
            del tip
        self.queuedTips = []
        self.currentSequence.finish()
        self.currentSequence = None
        del self.activeTip
        self.activeTip = None

    def deleteATip(self, index):
        tip = self.queuedTips.pop(index)
        del tip

    def deleteActiveTip(self):
        del self.activeTip
        self.activeTip = None

    def __handleClose(self):
        taskMgr.remove(self.taskName('checkQueueTask'))
        self.currentSequence.finish()
        self.currentSequence = Sequence(LerpPosInterval(self.activeTip, pos=self.startPos, duration=1, blendType='easeIn'), Wait(0.2), Func(self.deleteActiveTip))
        self.currentSequence.start()
        self.startCheckQueueTask()

    def createTipSequence(self, frame):
        self.activeTip = frame
        self.currentSequence.finish()
        comeInSeq = LerpPosInterval(frame, pos=self.endPos, startPos=self.startPos, duration=1, blendType='easeOut')
        goOutSeq = Sequence(LerpPosInterval(frame, pos=self.startPos, startPos=self.endPos, duration=1, blendType='easeIn'), Wait(0.2), Func(self.deleteActiveTip))
        self.currentSequence = Sequence(comeInSeq, Wait(self.tipOutFor), goOutSeq)
        self.currentSequence.start()

    def startCheckQueueTask(self):
        taskMgr.remove(self.taskName('checkQueueTask'))
        queueTask = Task.loop(Task(self.checkQueueTask), Task.pause(1.0))
        taskMgr.add(queueTask, self.taskName('checkQueueTask'))

    def checkQueueTask(self, task):
        if self.currentSequence.isPlaying():
            return
        else:
            if self.queuedTips:
                self.createTipSequence(self.queuedTips.pop(0))
                return
            else:
                return Task.done
