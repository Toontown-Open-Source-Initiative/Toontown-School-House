from direct.directnotify import DirectNotifyGlobal
from direct.fsm import StateData
import CogHQLoader
from toontown.toonbase import ToontownGlobals
from direct.gui import DirectGui
from toontown.toonbase import TTLocalizer
from toontown.toon import Toon
from direct.fsm import State
import FactoryExterior
import FactoryInterior
import SellbotHQExterior
import SellbotHQBossBattle
from panda3d.core import DecalEffect
from direct.actor.Actor import Actor
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
        return

    def load(self, zoneId):
        CogHQLoader.CogHQLoader.load(self, zoneId)
        Toon.loadSellbotHQAnims()

    def unloadPlaceGeom(self):
        if self.geom:
            self.geom.removeNode()
            self.geom = None
        self.VPHead.removeNode()
        del self.VPHead
        self.VPTorso.removeNode()
        del self.VPTorso
        self.VPTank.removeNode()
        del self.VPTank
        self.VPTreads.removeNode()
        del self.VPTreads
        self.GoonGuard1.removeNode()
        del self.GoonGuard1
        self.GoonGuard2.removeNode()
        del self.GoonGuard2
        self.GoonGuard3.removeNode()
        del self.GoonGuard3
        self.HollySuit1.removeNode()
        del self.HollySuit1
        self.HollySuit2.removeNode()
        del self.HollySuit2
        self.HollySuit3.removeNode()
        del self.HollySuit3
        self.HollySuit4.removeNode()
        del self.HollySuit4
        CogHQLoader.CogHQLoader.unloadPlaceGeom(self)
        return

    def loadPlaceGeom(self, zoneId):
        self.notify.info('loadPlaceGeom: %s' % zoneId)
        zoneId = zoneId - zoneId % 100
        if zoneId == ToontownGlobals.SellbotHQ:
            self.geom = loader.loadModel(self.cogHQExteriorModelPath)
            self.VPHead = loader.loadModel('phase_9/models/char/sellbotBoss-head-zero')
            self.VPHead.reparentTo(self.geom)
            self.VPHead.setPosHpr(0.123, -196.741, -18.594, -1170.522, 0, 0)

            self.VPTorso = loader.loadModel('phase_9/models/char/sellbotBoss-torso-zero')
            self.VPTorso.reparentTo(self.geom)
            self.VPTorso.setPosHpr(0.386, -188.850, -19.594, -543.251, -450, 0)

            self.VPTank = loader.loadModel('phase_9/models/char/bossCog-legs-zero')
            self.VPTank.reparentTo(self.geom)
            self.VPTank.setPosHpr(0.239, -179.500, -19.594, -543.251, -450, 0)

            self.VPTreads = loader.loadModel('phase_9/models/char/bossCog-treads')
            self.VPTreads.reparentTo(self.geom)
            self.VPTreads.setPosHpr(0.239, -179.500, -21, -543.251, -450, 0)

            self.GoonGuard1 = loader.loadModel('phase_9/models/char/Cog_Goonie-zero')
            self.GoonGuard1.reparentTo(self.geom)
            self.GoonGuard1.setPosHpr(5.955, -292.554, 1.243, 360.889, 0, 0)
            self.GoonGuard1.setScale(2)

            self.GoonGuard2 = loader.loadModel('phase_9/models/char/Cog_Goonie-zero')
            self.GoonGuard2.reparentTo(self.geom)
            self.GoonGuard2.setPosHpr(-0.562, -292.554, 1.243, 0, 0, 0)
            self.GoonGuard2.setScale(2)

            self.GoonGuard3 = loader.loadModel('phase_9/models/char/Cog_Goonie-zero')
            self.GoonGuard3.reparentTo(self.geom)
            self.GoonGuard3.setPosHpr(-6.057, -292.554, 1.243, 361.054, 0, 0)
            self.GoonGuard3.setScale(2)

            self.HollySuit1 = Actor('phase_3.5/models/char/SuitA-mod',
                                    {'suitA-squirt-large': 'phase_5/models/char/suitA-squirt-large'})
            self.HollySuit1.reparentTo(self.geom)
            self.HollySuit1.sellBlazer1 = loader.loadTexture('phase_3.5/maps/s_blazer.jpg')
            self.sellBlazer1 = self.HollySuit1.find('**/torso').setTexture(self.HollySuit1.sellBlazer1, 1)
            self.HollySuit1.sellLeg1 = loader.loadTexture('phase_3.5/maps/s_leg.jpg')
            self.sellLeg1 = self.HollySuit1.find('**/legs').setTexture(self.HollySuit1.sellLeg1, 1)
            self.HollySuit1.sellSleeve1 = loader.loadTexture('phase_3.5/maps/s_sleeve.jpg')
            self.sellSleeve1 = self.HollySuit1.find('**/arms').setTexture(self.HollySuit1.sellSleeve1, 1)
            self.HollySuit1.setPosHpr(-1.614, -194.110, -19.594, -27.220, 0, 0)
            self.HollySuit1.loop('suitA-squirt-large', restart = 0, fromFrame = 20, toFrame = 60)

            self.HollySuit2 = Actor('phase_3.5/models/char/SuitA-mod',
                                    {'suitA-squirt-large': 'phase_5/models/char/suitA-squirt-large'})
            self.HollySuit2.reparentTo(self.geom)
            self.HollySuit2.sellBlazer2 = loader.loadTexture('phase_3.5/maps/s_blazer.jpg')
            self.sellBlazer2 = self.HollySuit2.find('**/torso').setTexture(self.HollySuit2.sellBlazer2, 1)
            self.HollySuit2.sellLeg2 = loader.loadTexture('phase_3.5/maps/s_leg.jpg')
            self.sellLeg2 = self.HollySuit2.find('**/legs').setTexture(self.HollySuit2.sellLeg2, 1)
            self.HollySuit2.sellSleeve2 = loader.loadTexture('phase_3.5/maps/s_sleeve.jpg')
            self.sellSleeve2 = self.HollySuit2.find('**/arms').setTexture(self.HollySuit2.sellSleeve2, 1)
            self.HollySuit2.setPosHpr(-0.229, -194.023, -19.594, -4.022, 0, 0)
            self.HollySuit2.loop('suitA-squirt-large', restart = 0, fromFrame = 20, toFrame = 60)

            self.HollySuit3 = Actor('phase_3.5/models/char/SuitA-mod',
                                    {'suitA-squirt-large': 'phase_5/models/char/suitA-squirt-large'})
            self.HollySuit3.reparentTo(self.geom)
            self.HollySuit3.sellBlazer3 = loader.loadTexture('phase_3.5/maps/s_blazer.jpg')
            self.sellBlazer3 = self.HollySuit3.find('**/torso').setTexture(self.HollySuit3.sellBlazer3, 1)
            self.HollySuit3.sellLeg3 = loader.loadTexture('phase_3.5/maps/s_leg.jpg')
            self.sellLeg3 = self.HollySuit3.find('**/legs').setTexture(self.HollySuit3.sellLeg3, 1)
            self.HollySuit3.sellSleeve3 = loader.loadTexture('phase_3.5/maps/s_sleeve.jpg')
            self.sellSleeve3 = self.HollySuit3.find('**/arms').setTexture(self.HollySuit3.sellSleeve3, 1)
            self.HollySuit3.setPosHpr(1.892, -194.297, -19.594, 15.977, 0, 0)
            self.HollySuit3.loop('suitA-squirt-large', restart=0, fromFrame=20, toFrame=60)

            self.HollySuit4 = Actor('phase_3.5/models/char/SuitA-mod',
                                    {'suitA-squirt-large': 'phase_5/models/char/suitA-squirt-large'})
            self.HollySuit4.reparentTo(self.geom)
            self.HollySuit4.sellBlazer4 = loader.loadTexture('phase_3.5/maps/s_blazer.jpg')
            self.sellBlazer4 = self.HollySuit4.find('**/torso').setTexture(self.HollySuit4.sellBlazer4, 1)
            self.HollySuit4.sellLeg4 = loader.loadTexture('phase_3.5/maps/s_leg.jpg')
            self.sellLeg4 = self.HollySuit4.find('**/legs').setTexture(self.HollySuit4.sellLeg4, 1)
            self.HollySuit4.sellSleeve4 = loader.loadTexture('phase_3.5/maps/s_sleeve.jpg')
            self.sellSleeve4 = self.HollySuit4.find('**/arms').setTexture(self.HollySuit4.sellSleeve4, 1)
            self.HollySuit4.setPosHpr(3.398, -194.494, -19.594, 36.625, 0, 0)
            self.HollySuit4.loop('suitA-squirt-large', restart = 0, fromFrame = 20, toFrame = 60)

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

        elif zoneId == ToontownGlobals.SellbotFactoryExt:
            self.geom = loader.loadModel(self.factoryExteriorModelPath)
            factoryLinkTunnel = self.geom.find('**/tunnel_group2')
            factoryLinkTunnel.setName('linktunnel_sellhq_11000_DNARoot')
            factoryLinkTunnel.find('**/tunnel_sphere').setName('tunnel_trigger')
            cogSignModel = loader.loadModel('phase_4/models/props/sign_sellBotHeadHQ')
            cogSign = cogSignModel.find('**/sign_sellBotHeadHQ')
            cogSignSF = 23
            elevatorSignSF = 15
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
