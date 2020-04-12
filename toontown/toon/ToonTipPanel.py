from panda3d.core import *
from direct.gui.DirectGui import *
from direct.showbase import DirectObject
from direct.directnotify import DirectNotifyGlobal
from direct.interval.IntervalGlobal import *
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import ToonTipGlobals

class ToonTipPanel(DirectFrame):
    notify = DirectNotifyGlobal.directNotify.newCategory('ToonTipPanel')
    initPos = (0.5, 0, 0.5)
    bgImage = DGG.getDefaultDialogGeom()

    def __init__(self):
        DirectFrame.__init__(self, relief=None, sortOrder=55)
        self.activeTips = []
        self.exclamationPoint = loader.loadTexture('phase_3/maps/quest_exclaim.png')
        for number in ToonTipGlobals.TipByNum.keys():
            self.accept('showTip%s' % number, self.createNewTip, extraArgs=[number])

    def createNewTip(self, num):
        newFrame = DirectFrame(parent=self, pos=self.initPos, image_scale=(1.0, 1.0, 0.6), image=self.bgImage, relief=None, scale=(1.0, 1.0, 0.5), image_color=(0.75, 0.75, 1.0, 1.0), text='')
        excFrame = DirectFrame(pos=(0.39, 0.5, 0), image=self.exclamationPoint, scale=(0.1, 1.0, 0.2), relief=None)
        frameText = DirectLabel(pos=(0.15, 0.5, 0), scale=0.05, sortOrder=55, text_shadow=(0, 0, 0, 1))
        excFrame.reparentTo(newFrame)
        excFrame.setTransparency(1)
        frameText.reparentTo(newFrame)
        frameText['text'] = ToonTipGlobals.TipByNum[num]
        self.addNewTipToList(newFrame)

    def addNewTipToList(self, frame):
        self.activeTips.append(frame)

    def deleteAllTips(self):
        for tip in self.activeTips:
            del tip
        self.activeTips = []

    def deleteATip(self, index):
        del self.activeTips[index]
