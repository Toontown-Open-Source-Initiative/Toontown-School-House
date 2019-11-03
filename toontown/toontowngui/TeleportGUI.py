from panda3d.core import *
from direct.directnotify import DirectNotifyGlobal
from direct.gui.DirectGui import *
from direct.fsm import StateData
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from toontown.spellbook.MagicWordIndex import *


class TeleportGUI(DirectFrame, StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('TeleportGUI')

    def __init__(self, toon):
        DirectFrame.__init__(self, parent=aspect2d, relief=None, image=DGG.getDefaultDialogGeom(), pos=(0.0, 0.0, 0.05),
                             image_scale=(1.8, 1, 1.4), image_pos=(0, 0, -0.05),
                             image_color=ToontownGlobals.GlobalDialogColor, text=TTLocalizer.TeleportGUITitle,
                             text_scale=0.12, text_pos=(0, 0.5), borderWidth=(0.01, 0.01))
        StateData.StateData.__init__(self, 'teleport-gui-done')
        self.isLoaded = False
        self.setBin('gui-popup', 0)
        self.initialiseoptions(TeleportGUI)
        self.toon = toon
        self.textRolloverColor = Vec4(1, 1, 0, 1)
        self.textDownColor = Vec4(0.5, 0.9, 1, 1)
        self.textDisabledColor = Vec4(0.4, 0.8, 0.4, 1)
        self.descPos = (0.485, 0, -0.2)

    def unload(self):
        if not self.isLoaded:
            return
        self.isLoaded = False
        self.exit()
        DirectFrame.destroy(self)

    def load(self):
        if self.isLoaded:
            return
        self.isLoaded = True
        self.zones = []
        self.thumbnails = []

        teleportZones = []
        zonesForTeleport = ToontownGlobals.hood2Id.values()
        for zonePair in zonesForTeleport:
            if len(zonePair) == 2:
                zone = zonePair[1]
            else:
                zone = zonePair[0]
            zoneInfo = (zone, ToontownGlobals.hood2Id.keys()[zonesForTeleport.index(zonePair)])
            if zoneInfo not in teleportZones:
                try:
                    if not zonePair[2]:
                        continue
                except:
                    pass
                teleportZones.append(zoneInfo)

        for zone in teleportZones:
            zoneText = TTLocalizer.GlobalStreetNames.get(zone[0])[2]
            if zoneText == 'Playground':
                zoneText = ToontownGlobals.hoodNameMap.get(zone[0])[2]
            zoneName = DirectButton(parent=self, relief=None, text=zoneText,
                                    text_align=TextNode.ALeft, text_pos=(-0.05, 0, 0), text_scale=0.05,
                                    text1_bg=self.textDownColor, text2_bg=self.textRolloverColor,
                                    text3_fg=self.textDisabledColor, textMayChange=0, command=self.selectZone,
                                    extraArgs=[zone])
            self.zones.append(zoneName)
            setattr(self, '{0}Name'.format(zone[0]), zoneName)
            zoneThumb = OnscreenImage(image='phase_3/maps/zones/zone_' + str(zone[0]) + '.jpg', scale=(0.45, 0.25, 0.25),
                                      pos=(0.4, 0, 0), parent=hidden)
            self.thumbnails.append(zoneThumb)
            setattr(self, '{0}Thumbnail'.format(zone[0]), zoneThumb)
        gui = loader.loadModel('phase_3.5/models/gui/friendslist_gui')
        guiButton = loader.loadModel('phase_3/models/gui/quit_button')
        guiClose = loader.loadModel('phase_3.5/models/gui/avatar_panel_gui')
        self.scrollList = DirectScrolledList(parent=self, relief=None, forceHeight=0.07, pos=(-0.5, 0, -0.05),
                                             incButton_image=(gui.find('**/FndsLst_ScrollUp'),
                                                              gui.find('**/FndsLst_ScrollDN'),
                                                              gui.find('**/FndsLst_ScrollUp_Rllvr'),
                                                              gui.find('**/FndsLst_ScrollUp')), incButton_relief=None,
                                             incButton_scale=(1.3, 1.3, -1.3), incButton_pos=(0.025, 0, -0.60),
                                             incButton_image3_color=Vec4(1, 1, 1, 0.2),
                                             decButton_image=(gui.find('**/FndsLst_ScrollUp'),
                                                              gui.find('**/FndsLst_ScrollDN'),
                                                              gui.find('**/FndsLst_ScrollUp_Rllvr'),
                                                              gui.find('**/FndsLst_ScrollUp')), decButton_relief=None,
                                             decButton_scale=(1.3, 1.3, 1.3), decButton_pos=(0.025, 0, 0.52),
                                             decButton_image3_color=Vec4(1, 1, 1, 0.2), itemFrame_pos=(-0.237, 0, 0.41),
                                             itemFrame_scale=1.0, itemFrame_relief=DGG.SUNKEN,
                                             itemFrame_frameSize=(-0.10,
                                                                  0.66,
                                                                  -0.98,
                                                                  0.07), itemFrame_frameColor=(0.85, 0.95, 1, 1),
                                             itemFrame_borderWidth=(0.01, 0.01), numItemsVisible=14,
                                             items=self.zones)
        self.cancel = DirectButton(parent=self, relief=None,
                                   image=(guiClose.find('**/CloseBtn_UP'),
                                          guiClose.find('**/CloseBtn_DN'),
                                          guiClose.find('**/CloseBtn_Rllvr'),
                                          guiClose.find('**/CloseBtn_UP')),
                                   pos=(0.78, 0, -0.65), scale=1.5, command=self.__cancel)
        self.play = DirectButton(parent=hidden, relief=None, text=TTLocalizer.TeleportGUITeleport, image=(
            guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')),
                                 image_scale=(0.6, 1, 1), text_scale=TTLocalizer.DSDcancel,
                                 text_pos=TTLocalizer.DSDcancelPos, pos=(0.40, 0, -0.5), scale=1.5)
        gui.removeNode()
        guiButton.removeNode()
        guiClose.removeNode()
        self.hide()

    def enter(self):
        if self.isEntered == 1:
            return
        self.isEntered = 1
        if self.isLoaded == 0:
            self.load()
        base.transitions.fadeScreen(0.5)
        self.show()

    def exit(self):
        if self.isEntered == 0:
            return
        self.isEntered = 0
        self.scrollList.destroy()
        del self.scrollList
        base.transitions.noTransitions()
        self.ignoreAll()
        self.hide()

    def __cancel(self):
        self.unload()

    def selectZone(self, zone):
        messenger.send('wakeup')
        for zoneName in self.zones:
            if zoneName['state'] != DGG.NORMAL:
                zoneName['state'] = DGG.NORMAL

        for thumbnail in self.thumbnails:
            if thumbnail:
                thumbnail.reparentTo(hidden)

        getattr(self, '{0}Name'.format(zone[0]))['state'] = DGG.DISABLED
        getattr(self, '{0}Thumbnail'.format(zone[0])).reparentTo(self)
        self.play['text'] = TTLocalizer.TeleportGUITeleport
        self.play['command'] = self.__handleTeleport
        self.play['extraArgs'] = [zone[1]]
        self.play.reparentTo(self)

    def __handleTeleport(self, zone):
        self.unload()
        if base.localAvatar.getTransitioning():
            return

        self.toon.doTeleport(zone)
