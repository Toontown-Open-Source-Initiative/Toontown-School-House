from direct.directnotify import DirectNotifyGlobal
from direct.fsm import StateData
import CogHQLoader
from toontown.toonbase import ToontownGlobals
from direct.gui import DirectGui
from direct.task.Task import Task
from toontown.toonbase import TTLocalizer
from toontown.toon import Toon
from direct.fsm import State
import FactoryExterior
import random
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
        return

    def load(self, zoneId):
        CogHQLoader.CogHQLoader.load(self, zoneId)
        Toon.loadSellbotHQAnims()

    def unloadPlaceGeom(self):
        if self.geom:
            self.geom.removeNode()
            self.geom = None
            taskMgr.remove('hide-show-train-light-task')
        CogHQLoader.CogHQLoader.unloadPlaceGeom(self)
        return

    def loadPlaceGeom(self, zoneId):
        self.notify.info('loadPlaceGeom: %s' % zoneId)
        zoneId = zoneId - zoneId % 100
        if zoneId == ToontownGlobals.SellbotHQ:
            self.geom = loader.loadModel(self.cogHQExteriorModelPath)
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

            self.vpBodyModel = loader.loadModel('phase_9/models/char/sellbotBoss-torso-zero')
            self.vpBodyModel.reparentTo(self.geom)
            self.vpBodyModel.setPos(30.8499, -160.209, -17.5944)
            self.vpBodyModel.setHpr(30, 20, 325)

            self.vpHeadModel = loader.loadModel('phase_9/models/char/sellbotBoss-head-zero')
            self.vpHeadModel.reparentTo(self.vpBodyModel)
            self.vpHeadModel.setPos(0, 0, 8)
            self.vpHeadModel.setHpr(90, 0, 270)

            self.vpTreadsModel = loader.loadModel('phase_9/models/char/bossCog-treads')
            self.vpTreadsModel.reparentTo(self.geom)
            self.vpTreadsModel.setPos(-20, -165.209, -13.8944)
            self.vpTreadsModel.setHpr(70, 20, 130)

            self.vpLegsModel = loader.loadModel('phase_9/models/char/bossCog-legs-zero')
            self.vpLegsModel.reparentTo(self.vpTreadsModel)

            self.gearModel1 = loader.loadModel('phase_9/models/cogHQ/FactoryGearB')
            self.gearModel1.reparentTo(self.geom)
            self.gearModel1.setScale(10)
            self.gearModel1.setPos(45, -183, -13)
            self.gearModel1.setHpr(290, 35, 0)

            self.gearModel2 = loader.loadModel('phase_9/models/cogHQ/FactoryGearB')
            self.gearModel2.reparentTo(self.geom)
            self.gearModel2.setScale(5)
            self.gearModel2.setPos(45, -195, -15.5)
            self.gearModel2.setHpr(316, 35, 0)

            self.trainModel = loader.loadModel('phase_10/models/cogHQ/CashBotLocomotive')
            self.trainModel.reparentTo(self.geom)
            self.trainModel.setPos(-35, -205, -20)
            self.trainModel.setScale(0.4)
            self.trainModel.setHpr(80, 330, 0)

            self.trainLight = self.trainModel.find('**/LMBigLtBeam')
            self.trainLightPiece = self.trainModel.find('**/LMBigLight')
            self.applyNewTrainLightTask()

            self.trainCarModel = loader.loadModel('phase_10/models/cogHQ/CashBotBoxCar')
            self.trainCarModel.reparentTo(self.geom)
            self.trainCarModel.setPos(-10, -229, -13)
            self.trainCarModel.setScale(0.4)
            self.trainCarModel.setHpr(0, 20, 0)

            self.trainTankModel = loader.loadModel('phase_10/models/cogHQ/CashBotTankCar')
            self.trainTankModel.reparentTo(self.geom)
            self.trainTankModel.setPos(80.874, -130.546, 4)
            self.trainTankModel.setScale(0.4)
            self.trainTankModel.setHpr(70, 70, 20)

            self.cashMoneyModel = loader.loadModel('phase_10/models/cogHQ/DoubleMoneyStack')
            self.cashMoneyModel.reparentTo(self.geom)
            self.cashMoneyModel.setPos(21, -206, -19.594)
            self.cashMoneyModel.setHpr(67, 0, 0)

            self.cashMoneyLegalFeesModel = loader.loadModel('phase_11/models/lawbotHQ/LB_paper_big_stacks2')
            self.cashMoneyLegalFeesModel.reparentTo(self.geom)
            self.cashMoneyLegalFeesModel.setPos(-10, -207, -19.594)
            self.cashMoneyLegalFeesModel.setHpr(243, 0, 0)

            self.golfKartModel = loader.loadModel('phase_12/models/bossbotHQ/Coggolf_cart3')
            self.golfKartModel.reparentTo(self.geom)
            self.golfKartModel.setPos(7, -196, -19.594)
            self.golfKartModel.setHpr(149, 0, 0)

            self.banquetTableModel = loader.loadModel('phase_12/models/bossbotHQ/BanquetTableChairs')
            self.banquetTableModel.reparentTo(self.geom)
            self.banquetTableModel.setPos(0, -176, -19.594)
            self.banquetTableModel.setHpr(97, 0, 0)

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

    def hideTrainLightTask(self, task):
        self.trainLight.reparentTo(hidden)
        self.trainLightPiece.setColorScale(0.25, 0.25, 0.25, 1)
        return Task.done

    def applyNewTrainLightTask(self):
        hideShowTrainLight = Task.loop(Task.pause(random.uniform(0.05, 1.5)), Task(self.hideTrainLightTask), Task.pause(0.1), Task(self.showTrainLightTask))
        taskMgr.add(hideShowTrainLight, 'hide-show-train-light-task')

    def showTrainLightTask(self, task):
        self.trainLight.reparentTo(self.trainModel)
        self.trainLightPiece.setColorScale(1, 1, 1, 1)
        taskMgr.remove('hide-show-train-light-task')
        self.applyNewTrainLightTask()
        return Task.done

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
