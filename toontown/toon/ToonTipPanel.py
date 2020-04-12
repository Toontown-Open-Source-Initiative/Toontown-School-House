from panda3d.core import *
from direct.gui.DirectGui import *
from direct.directnotify import DirectNotifyGlobal
from direct.interval.IntervalGlobal import *
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownGlobals

class ToonTipPanel(DirectFrame):
    notify = DirectNotifyGlobal.directNotify.newCategory('ToonTipPanel')
    initPos = (0.5, 0, 0.5)
    bgImage = DGG.getDefaultDialogGeom()

    def __init__(self):
        DirectFrame.__init__(self, relief=None, sortOrder=55)
        self.activeTips = []
        self.exclamationPoint = loader.loadTexture('phase_3/maps/quest_exclaim.png')
        for number in TTLocalizer.ToonTipByNum.keys():
            self.accept('showTip%s' % number, self.createNewTip, extraArgs=[number])

    def createNewTip(self, num):
        newFrame = DirectFrame(parent=self, pos=self.initPos, image_scale=(1.3, 1.0, 0.6), image=self.bgImage, relief=None, scale=(1.0, 1.0, 0.5), image_color=(0.75, 0.75, 1.0, 1.0), text='')
        excFrame = DirectFrame(pos=(0.54, 0.5, 0), image=self.exclamationPoint, scale=(0.1, 1.0, 0.2), relief=None, image_color=(0.35, 0.35, 1.0, 1.0))
        frameText = DirectLabel(pos=(-0.05, 0.5, 0.05), scale=(0.05, 1.0, 0.1), sortOrder=55, text_align=TextNode.ALeft, relief=None)
        frameTitle = DirectLabel(pos=(-0.05, 0.5, 0.15), scale=(0.1, 1.0, 0.15), sortOrder=55, text_font=ToontownGlobals.getSignFont(), text='Quick Tip', text_fg=(0.6, 0.6, 1.0, 1.0), relief=None)
        excFrame.reparentTo(newFrame)
        excFrame.setTransparency(1)
        frameTitle.reparentTo(newFrame)
        frameText.reparentTo(newFrame)
        frameText['text'] = TTLocalizer.ToonTipByNum[num]
        frameText['text_wordwrap'] = 23
        self.addNewTipToList(newFrame)

    def addNewTipToList(self, frame):
        self.activeTips.append(frame)

    def deleteAllTips(self):
        for tip in self.activeTips:
            del tip
        self.activeTips = []

    def deleteATip(self, index):
        del self.activeTips[index]
