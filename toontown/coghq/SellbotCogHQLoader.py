from direct.directnotify import DirectNotifyGlobal
from direct.fsm import StateData
import CogHQLoader
from toontown.toonbase import ToontownGlobals
from direct.gui import DirectGui
from toontown.toonbase import TTLocalizer
#from direct.task.Task import Task
from toontown.toon import Toon
from direct.fsm import State
import FactoryExterior
import FactoryInterior
import SellbotHQExterior
import SellbotHQBossBattle
from panda3d.core import DecalEffect
aspectSF = 0.7227

class SellbotCogHQLoader(CogHQLoader.CogHQLoader):
    notify = DirectNotifyGlobal.directNotify.newCategory('SellbotCogHQLoader')

    def __init__(self, hood, parentFSMState, doneEvent):
        CogHQLoader.CogHQLoader.__init__(self, hood, parentFSMState, doneEvent)
        self.fsm.addState(State.State('factoryExterior', self.enterFactoryExterior, self.exitFactoryExterior, ['quietZone', 'factoryInterior', 'cogHQExterior']))
        for stateName in ['start', 'cogHQExterior', 'quietZone']:
            state = self.fsm.getStateNamed(stateName)
            state.addTransition('factoryExterior')

        self.fsm.addState(State.State('factoryInterior', self.enterFactoryInterior, self.exitFactoryInterior, ['quietZone', 'factoryExterior']))
        for stateName in ['quietZone']:
            state = self.fsm.getStateNamed(stateName)
            state.addTransition('factoryInterior')

        self.musicFile = 'phase_9/audio/bgm/encntr_suit_HQ_nbrhood.ogg'
        self.cogHQExteriorModelPath = 'phase_9/models/cogHQ/SellbotHQExterior'
        self.cogHQLobbyModelPath = 'phase_9/models/cogHQ/SellbotHQLobby'
        self.factoryExteriorModelPath = 'phase_9/models/cogHQ/SellbotFactoryExterior'
        self.geom = None
#        self.ground = ground
        return

    def load(self, zoneId):
        CogHQLoader.CogHQLoader.load(self, zoneId)
        Toon.loadSellbotHQAnims()
        self.underwaterSound = base.loader.loadSfx('phase_4/audio/sfx/AV_ambient_water.ogg')
        self.swimSound = base.loader.loadSfx('phase_4/audio/sfx/AV_swim_single_stroke.ogg')
        self.submergeSound = base.loader.loadSfx('phase_5.5/audio/sfx/AV_jump_in_water.ogg')

    def unloadPlaceGeom(self):
        if self.geom:
            self.geom.removeNode()
            self.geom = None
        CogHQLoader.CogHQLoader.unloadPlaceGeom(self)
        return

    def loadPlaceGeom(self, zoneId):
        self.notify.info('loadPlaceGeom: %s' % zoneId)
        zoneId = zoneId - zoneId % 100
        if zoneId == ToontownGlobals.SellbotHQ:
            self.geom = loader.loadModel(self.cogHQExteriorModelPath)
            ground = self.geom.find('**/polySurface81')
            dgLinkTunnel = self.geom.find('**/Tunnel1')
            dgLinkTunnel.setName('linktunnel_dg_5316_DNARoot')
            factoryLinkTunnel = self.geom.find('**/Tunnel2')
            factoryLinkTunnel.setName('linktunnel_sellhq_11200_DNARoot')
            cogSignModel = loader.loadModel('phase_4/models/props/sign_sellBotHeadHQ')
            cogSign = cogSignModel.find('**/sign_sellBotHeadHQ')
            cogSignSF = 23
            dgSign = cogSign.copyTo(dgLinkTunnel)
            dgSign.setPosHprScale(0.0, -291.5, 29, 180.0, 0.0, 0.0, cogSignSF, cogSignSF, cogSignSF * aspectSF)
            dgSign.node().setEffect(DecalEffect.make())
            dgText = DirectGui.OnscreenText(text=TTLocalizer.DaisyGardens[-1], font=ToontownGlobals.getSuitFont(), pos=(0, -0.3), scale=TTLocalizer.SCHQLdgText, mayChange=False, parent=dgSign)
            dgText.setDepthWrite(0)
            factorySign = cogSign.copyTo(factoryLinkTunnel)
            factorySign.setPosHprScale(148.625, -155, 27, -90.0, 0.0, 0.0, cogSignSF, cogSignSF, cogSignSF * aspectSF)
            factorySign.node().setEffect(DecalEffect.make())
            factoryTypeText = DirectGui.OnscreenText(text=TTLocalizer.Sellbot, font=ToontownGlobals.getSuitFont(), pos=(0, -0.25), scale=0.075, mayChange=False, parent=factorySign)
            factoryTypeText.setDepthWrite(0)
            factoryText = DirectGui.OnscreenText(text=TTLocalizer.Factory, font=ToontownGlobals.getSuitFont(), pos=(0, -0.34), scale=0.12, mayChange=False, parent=factorySign)
            factoryText.setDepthWrite(0)
            doors = self.geom.find('**/doors')
            door0 = doors.find('**/door_0')
            door1 = doors.find('**/door_1')
            door2 = doors.find('**/door_2')
            door3 = doors.find('**/door_3')
            index = 0
            for door in [door0,
             door1,
             door2,
             door3]:
                doorFrame = door.find('**/doorDoubleFlat/+GeomNode')
                door.find('**/doorFrameHoleLeft').wrtReparentTo(doorFrame)
                door.find('**/doorFrameHoleRight').wrtReparentTo(doorFrame)
                doorFrame.node().setEffect(DecalEffect.make())
                index += 1

            self.acidPool = loader.loadModel('phase_14/models/cogHQ/acidPool')
            self.acidPool.reparentTo(self.geom)
            self.acidPool.setPos(4, -190, -1)
            self.acidPool.setScale(1.5)
            self.acid = loader.loadTexture('phase_14/maps/inkAnim_1.png')
            self.acidPool.setTexture(self.acid, 1)
            self.acidPool.setTransparency(1)
            self.acidPool.setColorScale(1, 1, 1, 0.98)

            self.crate = loader.loadTexture('phase_14/maps/CrateByShadowrunner27.jpg')

            self.crate_1 = loader.loadModel('phase_14/models/props/crate')
            self.crate_1.setTexture(self.crate, 1)
            self.crate_1.reparentTo(self.geom)
            self.crate_1.setPosHprScale(1.1, -155, -3, -8, 0.5, -3.5, 0.92, 0.92, 0.92)

            self.crate_2 = loader.loadModel('phase_14/models/props/crate')
            self.crate_2.setTexture(self.crate, 1)
            self.crate_2.reparentTo(self.geom)
            self.crate_2.setPosHprScale(-13, -166, -5, 8.5, -12, 1, 1, 1, 1)

            self.crate_3 = loader.loadModel('phase_14/models/props/crate')
            self.crate_3.setTexture(self.crate, 1)
            self.crate_3.reparentTo(self.geom)
            self.crate_3.setPosHprScale(34, -172, -5.4, 5.2, 80, 6, 1.2, 1.2, 1.2)

            self.crate_4 = loader.loadModel('phase_14/models/props/crate')
            self.crate_4.setTexture(self.crate, 1)
            self.crate_4.reparentTo(self.geom)
            self.crate_4.setPosHprScale(-30, -164, -4, -0.8, 37, 6.8, 1, 1, 1)

            self.crate_5 = loader.loadModel('phase_14/models/props/crate')
            self.crate_5.setTexture(self.crate, 1)
            self.crate_5.reparentTo(self.geom)
            self.crate_5.setPosHprScale(48, -170, -4, -32, -73, -37, 1, 1, 1)

            self.crate_6 = loader.loadModel('phase_14/models/props/crate')
            self.crate_6.setTexture(self.crate, 1)
            self.crate_6.reparentTo(self.geom)
            self.crate_6.setPosHprScale(1.7, -180, -4.7, -6.5, -8, 4.4, 1.2, 1.2, 1.2)

            self.crate_7 = loader.loadModel('phase_14/models/props/crate')
            self.crate_7.setTexture(self.crate, 1)
            self.crate_7.reparentTo(self.geom)
            self.crate_7.setPosHprScale(21.4, -190, -5.35, -8.5, -25.4, 25.1, 1.2, 1.2, 1.2)

            self.crate_8 = loader.loadModel('phase_14/models/props/crate')
            self.crate_8.setTexture(self.crate, 1)
            self.crate_8.reparentTo(self.geom)
            self.crate_8.setPosHprScale(-26.5, -181, -4.7, -5.9, -9.9, 5.5, 1, 1, 1)

            self.crate_9 = loader.loadModel('phase_14/models/props/crate')
            self.crate_9.setTexture(self.crate, 1)
            self.crate_9.reparentTo(self.geom)
            self.crate_9.setPosHprScale(-42.2, -197, -4.76, -12, 10, 0.9, 1, 1, 1)

            self.crate_10 = loader.loadModel('phase_14/models/props/crate')
            self.crate_10.setTexture(self.crate, 1)
            self.crate_10.reparentTo(self.geom)
            self.crate_10.setPosHprScale(-11.1, -197, -5.34, -1.6, -19.3, -7.7, 0.9, 0.9, 0.9)

            self.crate_11 = loader.loadModel('phase_14/models/props/crate')
            self.crate_11.setTexture(self.crate, 1)
            self.crate_11.reparentTo(self.geom)
            self.crate_11.setPosHprScale(44, 210.8, -6, -65.3, -81.4, -54.6, 1, 1, 1)

            self.crate_12 = loader.loadModel('phase_14/models/props/crate')
            self.crate_12.setTexture(self.crate, 1)
            self.crate_12.reparentTo(self.geom)
            self.crate_12.setPosHprScale(23.2, -208.9, -5.34, -3.5, 62, -0.7, 1.1, 1.1, 1.1)

            self.crate_13 = loader.loadModel('phase_14/models/props/crate')
            self.crate_13.setTexture(self.crate, 1)
            self.crate_13.reparentTo(self.geom)
            self.crate_13.setPosHprScale(3.8, -209.75, -5.34, -94.7, 73.2, -105, 1, 1, 1)

            self.crate_14 = loader.loadModel('phase_14/models/props/crate')
            self.crate_14.setTexture(self.crate, 1)
            self.crate_14.reparentTo(self.geom)
            self.crate_14.setPosHprScale(31.69, -223.85, -5.25, 190.7, 54, 188, 0.8, 0.8, 0.8)

#            self.crate_15 = loader.loadModel('phase_14/models/props/crate')
#            self.crate_15.setTexture(self.crate, 1)
#            self.crate_15.reparentTo(self.geom)
#            self.crate_15.setPosHprScale(-6.66, -223.66 -5.34, -2.8, 4.7, 8, 0.9, 0.9, 0.9)

            self.crate_16 = loader.loadModel('phase_14/models/props/crate')
            self.crate_16.setTexture(self.crate, 1)
            self.crate_16.reparentTo(self.geom)
            self.crate_16.setPosHprScale(-6.5, -230.64, -5.34, 10.4, -41.4, -12, 1, 1, 1)

            self.crate_17 = loader.loadModel('phase_14/models/props/crate')
            self.crate_17.setTexture(self.crate, 1)
            self.crate_17.reparentTo(self.geom)
            self.crate_17.setPosHprScale(-23.9, -211.05, -4.75, -9.8, 16.6, 0, 1.3, .3, 1.3)

            self.crate_18 = loader.loadModel('phase_14/models/props/crate')
            self.crate_18.setTexture(self.crate, 1)
            self.crate_18.reparentTo(self.geom)
            self.crate_18.setPosHprScale(-44.85, -212.6, -4.75, 3.69, 58.15, 1.5, 1.15, 1.15, 1.15)

        elif zoneId == ToontownGlobals.SellbotFactoryExt:
            self.geom = loader.loadModel(self.factoryExteriorModelPath)
            factoryLinkTunnel = self.geom.find('**/tunnel_group2')
            factoryLinkTunnel.setName('linktunnel_sellhq_11000_DNARoot')
            factoryLinkTunnel.find('**/tunnel_sphere').setName('tunnel_trigger')
            cogSignModel = loader.loadModel('phase_4/models/props/sign_sellBotHeadHQ')
            cogSign = cogSignModel.find('**/sign_sellBotHeadHQ')
            cogSignSF = 23
            elevatorSignSF = 1
            hqSign = cogSign.copyTo(factoryLinkTunnel)
            hqSign.setPosHprScale(0.0, -353, 27.5, -180.0, 0.0, 0.0, cogSignSF, cogSignSF, cogSignSF * aspectSF)
            hqSign.node().setEffect(DecalEffect.make())
            hqTypeText = DirectGui.OnscreenText(text=TTLocalizer.Sellbot, font=ToontownGlobals.getSuitFont(), pos=(0, -0.25), scale=0.075, mayChange=False, parent=hqSign)
            hqTypeText.setDepthWrite(0)
            hqText = DirectGui.OnscreenText(text=TTLocalizer.Headquarters, font=ToontownGlobals.getSuitFont(), pos=(0, -0.34), scale=0.1, mayChange=False, parent=hqSign)
            hqText.setDepthWrite(0)
            frontDoor = self.geom.find('**/doorway1')
            fdSign = cogSign.copyTo(frontDoor)
            fdSign.setPosHprScale(62.74, -87.99, 17.26, 2.72, 0.0, 0.0, elevatorSignSF, elevatorSignSF, elevatorSignSF * aspectSF)
            fdSign.node().setEffect(DecalEffect.make())
            fdTypeText = DirectGui.OnscreenText(text=TTLocalizer.Factory, font=ToontownGlobals.getSuitFont(), pos=(0, -0.25), scale=TTLocalizer.SCHQLfdTypeText, mayChange=False, parent=fdSign)
            fdTypeText.setDepthWrite(0)
            fdText = DirectGui.OnscreenText(text=TTLocalizer.SellbotFrontEntrance, font=ToontownGlobals.getSuitFont(), pos=(0, -0.34), scale=TTLocalizer.SCHQLdgText, mayChange=False, parent=fdSign)
            fdText.setDepthWrite(0)
            sideDoor = self.geom.find('**/doorway2')
            sdSign = cogSign.copyTo(sideDoor)
            sdSign.setPosHprScale(-164.78, 26.28, 17.25, -89.89, 0.0, 0.0, elevatorSignSF, elevatorSignSF, elevatorSignSF * aspectSF)
            sdSign.node().setEffect(DecalEffect.make())
            sdTypeText = DirectGui.OnscreenText(text=TTLocalizer.Factory, font=ToontownGlobals.getSuitFont(), pos=(0, -0.25), scale=0.075, mayChange=False, parent=sdSign)
            sdTypeText.setDepthWrite(0)
            sdText = DirectGui.OnscreenText(text=TTLocalizer.SellbotSideEntrance, font=ToontownGlobals.getSuitFont(), pos=(0, -0.34), scale=0.1, mayChange=False, parent=sdSign)
            sdText.setDepthWrite(0)
        elif zoneId == ToontownGlobals.SellbotLobby:
            if base.config.GetBool('want-qa-regression', 0):
                self.notify.info('QA-REGRESSION: COGHQ: Visit SellbotLobby')
            self.geom = loader.loadModel(self.cogHQLobbyModelPath)
            front = self.geom.find('**/frontWall')
            front.node().setEffect(DecalEffect.make())
            door = self.geom.find('**/door_0')
            parent = door.getParent()
            door.wrtReparentTo(front)
            doorFrame = door.find('**/doorDoubleFlat/+GeomNode')
            door.find('**/doorFrameHoleLeft').wrtReparentTo(doorFrame)
            door.find('**/doorFrameHoleRight').wrtReparentTo(doorFrame)
            doorFrame.node().setEffect(DecalEffect.make())
            door.find('**/leftDoor').wrtReparentTo(parent)
            door.find('**/rightDoor').wrtReparentTo(parent)
        else:
            self.notify.warning('loadPlaceGeom: unclassified zone %s' % zoneId)
        CogHQLoader.CogHQLoader.loadPlaceGeom(self, zoneId)

    def unload(self):
        CogHQLoader.CogHQLoader.unload(self)
        Toon.unloadSellbotHQAnims()

    def enterFactoryExterior(self, requestStatus):
        self.placeClass = FactoryExterior.FactoryExterior
        self.enterPlace(requestStatus)
        self.hood.spawnTitleText(requestStatus['zoneId'])

    def exitFactoryExterior(self):
        taskMgr.remove('titleText')
        self.hood.hideTitleText()
        self.exitPlace()
        self.placeClass = None
        return

    def enterFactoryInterior(self, requestStatus):
        self.placeClass = FactoryInterior.FactoryInterior
        self.enterPlace(requestStatus)

    def exitFactoryInterior(self):
        self.exitPlace()
        self.placeClass = None
        return

    def getExteriorPlaceClass(self):
        return SellbotHQExterior.SellbotHQExterior

    def getBossPlaceClass(self):
        return SellbotHQBossBattle.SellbotHQBossBattle
'''
    def checkTintTrue(self, task):
        if  self.groundTint == 1:
            self.addGroundTint()
        else:
            self.removeGroundTint()
        return Task.cont

    def addGroundTint(self):
        self.ground = self.geom.find('**/polySurface81')
        self.ground.setColorScale(66/255, 46/255, 146/255, 1.0)

    def removeGroundTint(self):
        if self.groundTint == 0:
            return
        self.ground = self.geom.find('**/polySurface81')
        self.ground.clearColorScale()
'''
