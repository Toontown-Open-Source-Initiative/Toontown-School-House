import ShtikerPage
from toontown.battle.BattleProps import *
from toontown.toon.InventoryNew import *

class GagSkinsPage(ShtikerPage.ShtikerPage):
    listXorigin = -0.1
    listFrameSizeX = 0.45
    listZorigin = -0.96
    listFrameSizeZ = 1.04
    arrowButtonScale = 1.1
    itemFrameXorigin = -0.237
    itemFrameZorigin = 0.365
    buttonXstart = itemFrameXorigin + 0.125
    gagModelsByTrack = globalPropPool.getGagsByTrack()

    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)
        self.skinsButtons = []
        self.scrollList = None
        self.textRolloverColor = Vec4(1, 1, 0, 1)
        self.textDownColor = Vec4(0.5, 0.9, 1, 1)
        self.textDisabledColor = Vec4(0.4, 0.8, 0.4, 1)
        self.textAppliedColor = Vec4(0, 0.7, 0, 1)
        self.toonGagSkins = base.localAvatar.getGagSkins()
        self.toonGagSkinsApplied = base.localAvatar.getGagSkinsApplied()
        self.selectedTrack = 0
        self.selectedLevel = 0
        self.selectedIndex = 0
        self.gagIval = None
        self.currentGagModel = None
        return

    def load(self):
        ShtikerPage.ShtikerPage.load(self)
        self.title = DirectLabel(parent=self, relief=None, text=TTLocalizer.GagSkinsPageTitle, text_scale=0.12, textMayChange=1, pos=(0, 0, 0.62))
        self.gagRenderFrame = DirectFrame(parent=self, relief=DGG.SUNKEN, pos=(0.25, 0, 0.3), frameColor=(0.85, 0.95, 1, 1), borderWidth=(0.01, 0.01), frameSize=(-0.62,
         0.62,
         -0.23,
         0.146))
        self.selectAGagHint = DirectLabel(parent=self, relief=None, text=TTLocalizer.GagSkinsSelectGagHint, text_scale=0.08, textMayChange=1, pos=(0.25, 0, 0.265))
        self.currentGagText = DirectLabel(parent=self, relief=None, text=(TTLocalizer.GagSkinsCurrentGagText % 'None'), text_scale=0.08, textMayChange=1, pos=(-0.45, 0, -0.67), text_align=TextNode.ALeft)

        self.gui = loader.loadModel('phase_3.5/models/gui/friendslist_gui')
        self.regenerateScrollList(None, None, None)
        self.accept('update-gag-skin-buttons', self.regenerateScrollList)
        return

    def unload(self):
        del self.title
        del self.selectAGagHint
        del self.currentGagText
        self.scrollList.destroy()
        del self.scrollList
        del self.skinsButtons
        del self.gagRenderFrame
        del self.currentGagModel
        self.ignore('update-gag-skin-buttons')
        ShtikerPage.ShtikerPage.unload(self)

    def updateSkinsButtons(self, track, level, num, isapplied):
        gagSkinButtonParent = DirectFrame()
        gagSkinButton = DirectButton(parent=gagSkinButtonParent, relief=None, text=ToontownGlobals.AvPropsSkinsToName[track][level][num], text_scale=0.06,
                                    text_align=TextNode.ALeft, text1_bg=self.textDownColor,
                                    text2_bg=self.textRolloverColor, text3_fg=self.textDisabledColor,
                                    textMayChange=1, command=self.regenerateScrollList, extraArgs=[track, level, num], text_pos=(-0.07, 0, 0))
        if isapplied == 1:
            gagSkinButton['text_fg'] = self.textAppliedColor
            gagSkinButton['text1_fg'] = self.textAppliedColor
            gagSkinButton['text2_fg'] = self.textAppliedColor
            gagSkinButton['text3_fg'] = self.textAppliedColor
        return gagSkinButton

    def regenerateScrollList(self, track, level, num):
        if track is None or level is None:
            self.currentGagText.setText(TTLocalizer.GagSkinsCurrentGagText % 'None')
        else:
            self.updateCurrentGagText(track, level)
        selectedIndex = num
        if self.scrollList:
            if self.selectedTrack != track or self.selectedLevel != level:
                selectedIndex = 0
            self.selectedTrack = track
            self.selectedLevel = level
            self.selectedIndex = selectedIndex
            for button in self.skinsButtons:
                button.detachNode()

            self.scrollList.destroy()
            self.scrollList = None
        self.skinsButtons = []
        if track is not None and level is not None:
            for skin in range(len(self.toonGagSkins[track][level])):
                if self.toonGagSkins[track][level][skin] == 1:
                    if self.toonGagSkinsApplied[track][level] == skin:
                        self.skinsButtons.append(self.updateSkinsButtons(track, level, skin, isapplied=1))
                    else:
                        self.skinsButtons.append(self.updateSkinsButtons(track, level, skin, isapplied=0))

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
        if track is not None and level is not None and num is not None:
            self.updateChosenGagSkin(track, level, num)
        if len(self.skinsButtons) > 0:
            self.skinsButtons[selectedIndex]['text_bg'] = Vec4(1, 0.5, 0, 0.7)
        return

    def updateCurrentGagText(self, track, level):
        self.currentGagText.setText(TTLocalizer.GagSkinsCurrentGagText % TTLocalizer.BattleGlobalAvPropStrings[track][level])

    def enter(self):
        ShtikerPage.ShtikerPage.enter(self)
        base.localAvatar.inventory.setActivateMode('bookSkins')
        base.localAvatar.inventory.show()
        base.localAvatar.inventory.reparentTo(self)
        messenger.send('showTip1')

    def exit(self):
        ShtikerPage.ShtikerPage.exit(self)
        self.makePageWhite(None)
        base.localAvatar.inventory.hide()
        base.localAvatar.inventory.reparentTo(hidden)
        return

    def updateChosenGagSkin(self, track, level, num):
        if self.gagIval:
            self.gagIval.finish()
            del self.gagIval
        if self.currentGagModel:
            self.currentGagModel.destroy()
        self.currentGagModel, self.gagIval = self.makeFrameModel(track, level, num)
        if self.currentGagModel:
            self.currentGagModel.setScale(0.14)
        self.gagIval.loop()
        self.selectAGagHint.hide()

    def makeFrameModel(self, track, level, num):
        frame = self.makeFrame()
        ival = None
        model = self.gagModelsByTrack[track][level]
        if AvPropsSkins[track][level][num] is not None:
            gagtexture = loader.loadTexture(AvPropsSkins[track][level][num])
            gagtexture.setMinfilter(Texture.FTLinearMipmapLinear)
            gagtexture.setMagfilter(Texture.FTLinear)
            model.setTexture(gagtexture)
            print('gag texture: %s' % AvPropsSkins[track][level][num])
            print('reached here with num of: %s' % num)
        if model:
            model.setDepthTest(1)
            model.setDepthWrite(1)
            pitch = frame.attachNewNode('pitch')
            rotate = pitch.attachNewNode('rotate')
            scale = rotate.attachNewNode('scale')
            model.reparentTo(scale)
            bMin, bMax = model.getTightBounds()
            center = (bMin + bMax) / 2.0
            model.setPos(-center[0], -center[1], -center[2])
            pitch.setP(20)
            bMin, bMax = pitch.getTightBounds()
            center = (bMin + bMax) / 2.0
            corner = Vec3(bMax - center)
            scale.setScale(0.8 / max(corner[0], corner[1], corner[2]))
            pitch.setY(1)
            ival = LerpHprInterval(rotate, 10, VBase3(-270, 0, 0), startHpr=VBase3(90, 0, 0))
        return (frame, ival)

    def makeFrame(self):
        frame = DirectFrame(parent=self, relief=DGG.SUNKEN, pos=(0.25, 0, 0.3), frameColor=(0.85, 0.95, 1, 1), borderWidth=(0.01, 0.01), frameSize=(-0.62, 0.62, -0.23, 0.146))
        return frame