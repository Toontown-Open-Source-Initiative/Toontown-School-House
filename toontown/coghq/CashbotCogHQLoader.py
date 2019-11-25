from direct.directnotify import DirectNotifyGlobal
from direct.fsm import StateData
import CogHQLoader, MintInterior
from toontown.toonbase import ToontownGlobals
from direct.gui import DirectGui
from toontown.toonbase import TTLocalizer
from toontown.toon import Toon
from direct.fsm import State
import CashbotHQExterior
import CashbotHQBossBattle
import CashbotHQBossBattleHardmode
from panda3d.core import DecalEffect
from toontown.battle.BattleProps import *
from direct.interval.IntervalGlobal import *

class CashbotCogHQLoader(CogHQLoader.CogHQLoader):
    notify = DirectNotifyGlobal.directNotify.newCategory('CashbotCogHQLoader')

    def __init__(self, hood, parentFSMState, doneEvent):
        CogHQLoader.CogHQLoader.__init__(self, hood, parentFSMState, doneEvent)
        self.fsm.addState(State.State('mintInterior', self.enterMintInterior, self.exitMintInterior, ['quietZone', 'cogHQExterior']))
        for stateName in ['start', 'cogHQExterior', 'quietZone']:
            state = self.fsm.getStateNamed(stateName)
            state.addTransition('mintInterior')

        self.musicFile = 'phase_9/audio/bgm/encntr_suit_HQ_nbrhood.ogg'
        self.cogHQExteriorModelPath = 'phase_10/models/cogHQ/CashBotShippingStation'
        self.cogHQLobbyModelPath = 'phase_10/models/cogHQ/VaultLobby'
        self.geom = None
        self.sceneSeq = None
        return

    def load(self, zoneId):
        CogHQLoader.CogHQLoader.load(self, zoneId)
        Toon.loadCashbotHQAnims()

    def unloadPlaceGeom(self):
        if self.geom:
            self.geom.removeNode()
            self.geom = None
        if self.sceneSeq:
            self.sceneSeq.finish()
            self.sceneSeq = None
        self.trainModel = None
        self.trainTunnel = None
        self.geyserModel = None
        CogHQLoader.CogHQLoader.unloadPlaceGeom(self)
        return

    def loadPlaceGeom(self, zoneId):
        self.notify.info('loadPlaceGeom: %s' % zoneId)
        zoneId = zoneId - zoneId % 100
        if zoneId == ToontownGlobals.CashbotHQ:
            self.geom = loader.loadModel(self.cogHQExteriorModelPath)
            ddLinkTunnel = self.geom.find('**/LinkTunnel1')
            ddLinkTunnel.setName('linktunnel_dl_9252_DNARoot')
            locator = self.geom.find('**/sign_origin')
            backgroundGeom = self.geom.find('**/EntranceFrameFront')
            backgroundGeom.node().setEffect(DecalEffect.make())
            signText = DirectGui.OnscreenText(text=TTLocalizer.DonaldsDreamland[-1], font=ToontownGlobals.getSuitFont(), scale=3, fg=(0.87, 0.87, 0.87, 1), mayChange=False, parent=backgroundGeom)
            signText.setPosHpr(locator, 0, 0, 0, 0, 0, 0)
            signText.setDepthWrite(0)

            sceneNode = self.geom.attachNewNode('sceneNode')

            self.trainModel = loader.loadModel('phase_10/models/cogHQ/CashBotLocomotive')
            self.trainModel.setPosHprScale(470, -441, -23.5, 0, 0, 0, 0.8, 0.8, 0.8)
            self.trainModel.reparentTo(sceneNode)
            self.trainModel.hide()

            self.trainTunnel = loader.loadModel('phase_5/models/props/traintrack2').find('**/tunnel3')
            self.trainTunnel.setPosHprScale(371, -443, -23.5, 0, 0, 0, 0.1, 0.05, 0.05)
            self.trainTunnel.reparentTo(sceneNode)
            self.trainTunnel.hide()

            self.geyserModel = globalPropPool.getProp('geyser')
            self.geyserModel.setPosHprScale(240, -441, -23.5, 0, 0, 0, 0.05, 0.05, 0.05)
            self.geyserModel.reparentTo(sceneNode)
            self.geyserModel.hide()

            geyserWaterNode = self.geyserModel.attachNewNode('waterNode')
            geyserWaterNode.setScale(0.1)

            geyserSplashNode = SequenceNode('splashNode')

            self.geyserModel.findAllMatches('**/Splash*').reparentTo(NodePath(geyserSplashNode))
            self.geyserModel.find('**/spout').reparentTo(geyserWaterNode)

            geyserSplashNode.loop(0)
            geyserSplashNode.setFrameRate(12)
            geyserWaterNode.attachNewNode(geyserSplashNode)

            self.sceneSeq = Sequence(Wait(2),
                                     Func(self.trainModel.show),
                                     Func(self.geyserModel.show),
                                     LerpScaleInterval(self.geyserModel, 0.5, 4, blendType='easeOut'),
                                     Func(self.trainTunnel.show),
                                     Parallel(
                                     LerpScaleInterval(geyserWaterNode, 0.5, 1, blendType='easeOut'),
                                     LerpScaleInterval(self.trainTunnel, 0.5, (0.1, 8, 10), blendType='easeOut')
                                     ),
                                     LerpPosInterval(self.trainModel, 1, (210, -441, -23.5)),
                                     LerpPosHprInterval(self.trainModel, 1, (50, -432, 203), blendType='easeOut', hpr=(0, -60, -60)),
                                     Parallel(
                                     LerpScaleInterval(geyserWaterNode, 0.5, 0.05, blendType='easeIn'),
                                     LerpScaleInterval(self.trainTunnel, 0.5, (0.1, 0.05, 0.05), blendType='easeIn')
                                     ),
                                     Func(self.trainTunnel.hide),
                                     LerpScaleInterval(self.geyserModel, 0.5, 0.05, blendType='easeIn'),
                                     Func(self.geyserModel.hide),
                                     Func(self.trainModel.setPosHpr, 470, -441, -23.5, 0, 0, 0))

            self.sceneSeq.loop()

        elif zoneId == ToontownGlobals.CashbotLobby:
            if base.config.GetBool('want-qa-regression', 0):
                self.notify.info('QA-REGRESSION: COGHQ: Visit CashbotLobby')
            self.geom = loader.loadModel(self.cogHQLobbyModelPath)
        else:
            self.notify.warning('loadPlaceGeom: unclassified zone %s' % zoneId)
        CogHQLoader.CogHQLoader.loadPlaceGeom(self, zoneId)

    def unload(self):
        CogHQLoader.CogHQLoader.unload(self)
        Toon.unloadCashbotHQAnims()

    def enterMintInterior(self, requestStatus):
        self.placeClass = MintInterior.MintInterior
        self.mintId = requestStatus['mintId']
        self.enterPlace(requestStatus)

    def exitMintInterior(self):
        self.exitPlace()
        self.placeClass = None
        del self.mintId
        return

    def getExteriorPlaceClass(self):
        return CashbotHQExterior.CashbotHQExterior

    def getBossPlaceClass(self):
        return CashbotHQBossBattle.CashbotHQBossBattle

