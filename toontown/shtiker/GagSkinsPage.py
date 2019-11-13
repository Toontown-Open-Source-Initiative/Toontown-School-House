import ShtikerPage
from toontown.toonbase import ToontownBattleGlobals
from direct.gui.DirectGui import *
from panda3d.core import *
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer

class GagSkinsPage(ShtikerPage.ShtikerPage):

    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)
        self.skinsButtons = []
        self.scrollList = None
        self.textRolloverColor = Vec4(1, 1, 0, 1)
        self.textDownColor = Vec4(0.5, 0.9, 1, 1)
        self.textDisabledColor = Vec4(0.4, 0.8, 0.4, 1)
        return

    def load(self):
        ShtikerPage.ShtikerPage.load(self)
        self.title = DirectLabel(parent=self, relief=None, text=TTLocalizer.GagSkinsPageTitle, text_scale=0.12, textMayChange=1, pos=(0, 0, 0.62))
        self.selectAGagHint = DirectLabel(parent=self, relief=None, text=TTLocalizer.GagSkinsSelectGagHint, text_scale=0.08, textMayChange=1, pos=(0.25, 0, 0.3))

        self.gui = loader.loadModel('phase_3.5/models/gui/friendslist_gui')
        self.listXorigin = -0.1
        self.listFrameSizeX = 0.45
        self.listZorigin = -0.96
        self.listFrameSizeZ = 1.04
        self.arrowButtonScale = 1.1
        self.itemFrameXorigin = -0.237
        self.itemFrameZorigin = 0.365
        self.buttonXstart = self.itemFrameXorigin + 0.125
        self.regenerateScrollList()
        return

    def unload(self):
        del self.title
        del self.selectAGagHint
        self.scrollList.destroy()
        del self.scrollList
        del self.skinsButtons
        ShtikerPage.ShtikerPage.unload(self)

    def regenerateScrollList(self):
        selectedIndex = 0
        if self.scrollList:
            selectedIndex = self.scrollList.getSelectedIndex()
            for button in self.skinsButtons:
                button.detachNode()

            self.scrollList.destroy()
            self.scrollList = None
        self.scrollList = DirectScrolledList(parent=self, relief=None, pos=(-0.5, 0, 0), incButton_image=(self.gui.find('**/FndsLst_ScrollUp'),
         self.gui.find('**/FndsLst_ScrollDN'),
         self.gui.find('**/FndsLst_ScrollUp_Rllvr'),
         self.gui.find('**/FndsLst_ScrollUp')), incButton_relief=None, incButton_scale=(self.arrowButtonScale, self.arrowButtonScale, -self.arrowButtonScale), incButton_pos=(self.buttonXstart, 0, self.itemFrameZorigin - 0.999), incButton_image3_color=Vec4(1, 1, 1, 0.2), decButton_image=(self.gui.find('**/FndsLst_ScrollUp'),
         self.gui.find('**/FndsLst_ScrollDN'),
         self.gui.find('**/FndsLst_ScrollUp_Rllvr'),
         self.gui.find('**/FndsLst_ScrollUp')), decButton_relief=None, decButton_scale=(self.arrowButtonScale, self.arrowButtonScale, self.arrowButtonScale), decButton_pos=(self.buttonXstart, 0, self.itemFrameZorigin + 0.12), decButton_image3_color=Vec4(1, 1, 1, 0.2), itemFrame_pos=(self.itemFrameXorigin, 0, self.itemFrameZorigin), itemFrame_scale=1.0, itemFrame_relief=DGG.SUNKEN, itemFrame_frameSize=(self.listXorigin,
         self.listXorigin + self.listFrameSizeX,
         self.listZorigin,
         self.listZorigin + self.listFrameSizeZ), itemFrame_frameColor=(0.85, 0.95, 1, 1), itemFrame_borderWidth=(0.01, 0.01), numItemsVisible=15, forceHeight=0.065, items=self.skinsButtons)
        self.scrollList.scrollTo(selectedIndex)
        return

    def enter(self):
        ShtikerPage.ShtikerPage.enter(self)
        base.localAvatar.inventory.setActivateMode('bookSkins')
        base.localAvatar.inventory.show()
        base.localAvatar.inventory.reparentTo(self)

    def exit(self):
        ShtikerPage.ShtikerPage.exit(self)
        self.makePageWhite(None)
        base.localAvatar.inventory.hide()
        base.localAvatar.inventory.reparentTo(hidden)
        return
