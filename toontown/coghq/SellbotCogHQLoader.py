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
from direct.interval.IntervalGlobal import *
from direct.gui.DirectButton import DirectButton
from direct.gui.DirectLabel import DirectLabel
from direct.gui.DirectFrame import DirectFrame

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
        self.interval = None
        return

    def load(self, zoneId):
        CogHQLoader.CogHQLoader.load(self, zoneId)
        Toon.loadSellbotHQAnims()

    def unloadPlaceGeom(self):
        if self.geom:
            self.geom.removeNode()
            self.geom = None

        if self.VPSequenceLabel:
            self.VPSequenceLabel.destroy()
            self.VPSequenceLabel = None

        if self.VPSequenceButton:
            self.VPSequenceButton.destroy()
            self.VPSequenceButton = None

        if self.showHollyLabel:
            self.showHollyLabel.destroy()
            self.showHollyLabel = None

        if self.showHollyButton:
            self.showHollyButton.destroy()
            self.showHollyButton = None

        if self.hideHollyLabel:
            self.hideHollyLabel.destroy()
            self.hideHollyLabel = None

        if self.hideHollyButton:
            self.hideHollyButton.destroy()
            self.hideHollyButton = None

        if self.frameExample:
            self.frameExample.destroy()
            self.frameExample = None

        if self.VPSequenceGui:
            self.VPSequenceGui.removeNode()
            self.VPSequenceGui = None

        if self.showHollysGui:
            self.showHollysGui.removeNode()
            self.showHollysGui = None

        if self.hideHollysGui:
            self.hideHollysGui.removeNode()
            self.hideHollysGui = None

        if self.frameExampleGui:
            self.frameExampleGui.removeNode()
            self.frameExampleGui = None

        if self.interval:
            self.interval.finish()
            del self.interval

        if self.VPHead:
            self.VPHead.removeNode()
            self.VPHead = None

        if self.VPTorso:
            self.VPTorso.removeNode()
            self.VPTorso = None

        if self.VPTank:
            self.VPTank.removeNode()
            self.VPTank = None

        if self.VPTreads:
            self.VPTreads.removeNode()
            self.VPTreads = None

        if self.CreamPie1:
            self.CreamPie1.removeNode()
            self.CreamPie1 = None

        if self.CreamPie2:
            self.CreamPie2.removeNode()
            self.CreamPie2 = None

        if self.CreamPie3:
            self.CreamPie3.removeNode()
            self.CreamPie3 = None

        if self.CreamPie4:
            self.CreamPie4.removeNode()
            self.CreamPie4 = None

        if self.CreamPie5:
            self.CreamPie5.removeNode()
            self.CreamPie5 = None

        if self.CreamPie6:
            self.CreamPie6.removeNode()
            self.CreamPie6 = None

        if self.GoonGuard1:
            self.GoonGuard1.removeNode()
            self.GoonGuard1 = None

        if self.GoonGuard2:
            self.GoonGuard2.removeNode()
            self.GoonGuard2 = None

        if self.GoonGuard3:
            self.GoonGuard3.removeNode()
            self.GoonGuard3 = None

        if self.HollyHead1:
            self.HollyHead1.removeNode()
            self.HollyHead1 = None

        if self.HollyHead2:
            self.HollyHead2.removeNode()
            self.HollyHead2 = None

        if self.HollyHead3:
            self.HollyHead3.removeNode()
            self.HollyHead3 = None

        if self.HollyHead4:
            self.HollyHead4.removeNode()
            self.HollyHead4 = None

        if self.HollySuit1:
            self.HollySuit1.cleanup()
            self.HollySuit1.removeNode()
            self.HollySuit1 = None

        if self.HollySuit2:
            self.HollySuit2.cleanup()
            self.HollySuit2.removeNode()
            self.HollySuit2 = None

        if self.HollySuit3:
            self.HollySuit3.cleanup()
            self.HollySuit3.removeNode()
            self.HollySuit3 = None

        if self.HollySuit4:
            self.HollySuit4.cleanup()
            self.HollySuit4.removeNode()
            self.HollySuit4 = None

        if self.VPSequence:
            self.VPSequence.finish()
            self.VPSequence = None
        self.ignoreAll()

        CogHQLoader.CogHQLoader.unloadPlaceGeom(self)
        return

    def sequencePlayer(self):
        if self.VPSequence.isPlaying():
            self.VPSequence.pause()
        else:
            self.VPSequence.resume()

    def hideHolly(self):
        self.HollySuit1.hide()
        self.HollyHead1.hide()
        self.HollySuit2.hide()
        self.HollyHead2.hide()
        self.HollySuit3.hide()
        self.HollyHead3.hide()
        self.HollySuit4.hide()
        self.HollyHead4.hide()

    def showHolly(self):
        self.HollySuit1.show()
        self.HollyHead1.show()
        self.HollySuit2.show()
        self.HollyHead2.show()
        self.HollySuit3.show()
        self.HollyHead3.show()
        self.HollySuit4.show()
        self.HollyHead4.show()

    def loadPlaceGeom(self, zoneId):
        self.notify.info('loadPlaceGeom: %s' % zoneId)
        zoneId = zoneId - zoneId % 100
        if zoneId == ToontownGlobals.SellbotHQ:

            self.geom = loader.loadModel(self.cogHQExteriorModelPath)

            self.VPFall = loader.loadSfx('phase_9/audio/sfx/CHQ_VP_big_death.ogg')
            CreamPie = render.attachNewNode('CreamPie')
            self.CreamPie1 = loader.loadModel('phase_3.5/models/props/tart')
            self.CreamPie1.reparentTo(CreamPie)
            self.CreamPie1.setPosHpr(2.171, 34.561, 400, -1616.669, -500, 0)
            self.CreamPie1.setScale(2)
            self.CreamPie2 = loader.loadModel('phase_3.5/models/props/tart')
            self.CreamPie2.reparentTo(CreamPie)
            self.CreamPie2.setPosHpr(2.171, 34.561, 400, -1616.669, -500, 0)
            self.CreamPie2.setScale(2)
            self.CreamPie3 = loader.loadModel('phase_3.5/models/props/tart')
            self.CreamPie3.reparentTo(CreamPie)
            self.CreamPie3.setPosHpr(2.171, 34.561, 400, -1616.669, -500, 0)
            self.CreamPie3.setScale(2)
            self.CreamPie4 = loader.loadModel('phase_3.5/models/props/tart')
            self.CreamPie4.reparentTo(CreamPie)
            self.CreamPie4.setPosHpr(2.171, 34.561, 400, -1616.669, -500, 0)
            self.CreamPie4.setScale(2)
            self.CreamPie5 = loader.loadModel('phase_3.5/models/props/tart')
            self.CreamPie5.reparentTo(CreamPie)
            self.CreamPie5.setPosHpr(2.171, 34.561, 400, -1616.669, -500, 0)
            self.CreamPie5.setScale(2)
            self.CreamPie6 = loader.loadModel('phase_3.5/models/props/tart')
            self.CreamPie6.reparentTo(CreamPie)
            self.CreamPie6.setPosHpr(2.171, 34.561, 400, -1616.669, -500, 0)
            self.CreamPie6.setScale(2)
            self.VPHead = loader.loadModel('phase_9/models/char/sellbotBoss-head-zero')
            self.VPTorso = loader.loadModel('phase_9/models/char/sellbotBoss-torso-zero')
            self.VPTank = loader.loadModel('phase_9/models/char/bossCog-legs-zero')
            self.VPTreads = loader.loadModel('phase_9/models/char/bossCog-treads')
            self.VPTank.reparentTo(self.geom)
            VPTreads = self.VPTank.find('**/joint_axle')
            self.VPTreads.reparentTo(VPTreads)
            VPPelvis = self.VPTank.find('**/joint_legs')
            self.VPTorso.reparentTo(VPPelvis)
            VPNeck = self.VPTorso.find('**/joint34')
            self.VPHead.reparentTo(VPNeck)
            self.VPTank.setPosHpr(0.239, -179.500, 400, -543.251, -450, 0)

            self.VPSequenceGui = loader.loadModel('phase_3/models/gui/pick_a_toon_gui')
            quitHover = self.VPSequenceGui.find('**/QuitBtn_RLVR')
            self.VPSequenceButton = DirectButton(parent=aspect2d,
                                                 relief=None,
                                                 scale=1.05,
                                                 pos=(-1.253333, 0, 0.0903),
                                                 image=quitHover,
                                                 image_scale=1.5,
                                                 text='Toggle VP Sequence',
                                                 text_font=ToontownGlobals.getSignFont(),
                                                 text_fg=(0.977, 0.816, 0.133, 1),
                                                 text_pos=(0, 0),
                                                 text_scale=0.045,
                                                 command=self.sequencePlayer)

            self.VPSequenceLabel = DirectLabel(parent=aspect2d,
                                               relief=None,
                                               scale=0.05,
                                               pos=(-1.253333, 0, 0.193),
                                               text='Click this to toggle the VP Sequence to Play/Pause',
                                               text_font=ToontownGlobals.getSuitFont())

            self.showHollysGui = loader.loadModel('phase_3/models/gui/pick_a_toon_gui')
            quitHover2 = self.showHollysGui.find('**/QuitBtn_RLVR')
            self.showHollyButton = DirectButton(parent = aspect2d,
                                                relief = None,
                                                scale = 1.05,
                                                pos = (-1.253333,0, -0.2),
                                                image = quitHover2,
                                                image_scale = 1.5,
                                                text = 'Show Hollywoods',
                                                text_font = ToontownGlobals.getSignFont(),
                                                text_fg = (0.977, 0.816, 0.133, 1),
                                                text_pos = (0,0),
                                                text_scale = 0.045,
                                                command = self.showHolly)

            self.showHollyLabel = DirectLabel(parent = aspect2d,
                                              relief = None,
                                              scale = 0.05,
                                              pos = (-1.253333, 0, -0.1),
                                              text = 'Click this to show the Hollywood Actors',
                                              text_font = ToontownGlobals.getSuitFont())

            self.hideHollysGui = loader.loadModel('phase_3/models/gui/pick_a_toon_gui')
            quitHover3 = self.hideHollysGui.find('**/QuitBtn_RLVR')
            self.hideHollyButton = DirectButton(parent=aspect2d,
                                                relief=None,
                                                scale=1.05,
                                                pos=(1.253333, 0, 0.0903),
                                                image=quitHover3,
                                                image_scale=1.5,
                                                text='Hide Hollywoods',
                                                text_font=ToontownGlobals.getSignFont(),
                                                text_fg=(0.977, 0.816, 0.133, 1),
                                                text_pos=(0, 0),
                                                text_scale=0.045,
                                                command=self.hideHolly)

            self.hideHollyLabel = DirectLabel(parent=aspect2d,
                                              relief=None,
                                              scale=0.05,
                                              pos=(1.253333, 0, 0.193),
                                              text='Click this to Hide the Hollywood Actors',
                                              text_font=ToontownGlobals.getSuitFont())

            self.frameExampleGui = loader.loadModel('phase_3/models/gui/pick_a_toon_gui')
            quitHover4 = self.frameExampleGui.find('**/QuitBtn_RLVR')
            self.frameExample = DirectFrame(parent = aspect2d,
                                            relief = None,
                                            scale = 1.05,
                                            pos = (1.253333,0, -0.2),
                                            image = quitHover4,
                                            image_scale = 1.5,
                                            text = 'This is a Frame',
                                            text_font = ToontownGlobals.getSignFont(),
                                            text_fg = (0.977, 0.816, 0.133, 1),
                                            text_pos = (0, 0),
                                            text_scale = 0.045)

            self.VPSequence = Sequence(
                LerpPosInterval(self.VPTank, 0, (0.239, -179.500, 400), (-543.251, -450, 0)),
                Func(base.playSfx, self.VPFall),
                Wait(2.0),
                LerpPosHprInterval(self.VPTank, 2.5, (0.386, -179.500, -19.594), (-543.251, -450, 0)),
                Func(CreamPie.show),
                Parallel(
                    LerpPosHprScaleInterval(self.CreamPie1, 3.0, (22.110, -105.404, 0.287), (184.137, -500, 0), 2),
                    LerpPosHprScaleInterval(self.CreamPie2, 3.0, (-27.597, -126.047, 0.287), (188.899, -500, 0), 2),
                    LerpPosHprScaleInterval(self.CreamPie3, 3.0, (23.303, -183.232, -19.594), (157.797, -500, 0), 2),
                    LerpPosHprScaleInterval(self.CreamPie4, 3.0, (-22.105, -227.833, -9.226), (220.122, -500, 0), 2),
                    LerpPosHprScaleInterval(self.CreamPie5, 3.0, (28.365, -188.265, -19.594), (539.826, -500, 0), 2),
                    LerpPosHprScaleInterval(self.CreamPie6, 3.0, (0.689, -188.070, -19.594), (1612.135, -500, 0), 2)

                ),
                Wait(2.0),
                Func(CreamPie.hide),
                Wait(2.0),
                LerpPosHprInterval(self.VPTank, 5.0, (0.386, -188.850, -19.594), (-543.251, 0, 0)),
                Wait(5.0),
                LerpPosHprInterval(self.VPTank, 5.0, (-1.734, -125.109, 0.287), (-9.13, 0, 0)),
                Wait(5.0)
            )
            self.VPSequence.loop()

            self.accept('p', self.sequencePlayer)

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

            self.HollyHead1 = loader.loadModel('phase_4/models/char/suitA-heads').find('**/yesman')
            self.HollyHead2 = loader.loadModel('phase_4/models/char/suitA-heads').find('**/yesman')
            self.HollyHead3 = loader.loadModel('phase_4/models/char/suitA-heads').find('**/yesman')
            self.HollyHead4 = loader.loadModel('phase_4/models/char/suitA-heads').find('**/yesman')

            self.HollySuit1 = Actor('phase_3.5/models/char/SuitA-mod',
                                    {'suitA-squirt-large': 'phase_5/models/char/suitA-squirt-large'})
            self.HollySuit1.reparentTo(self.geom)
            self.HollySuit1.SellBlazer1 = loader.loadTexture('phase_3.5/maps/s_blazer.jpg')
            self.SellBlazer1 = self.HollySuit1.find('**/torso').setTexture(self.HollySuit1.SellBlazer1, 1)
            self.HollySuit1.SellLeg1 = loader.loadTexture('phase_3.5/maps/s_leg.jpg')
            self.SellLeg1 = self.HollySuit1.find('**/legs').setTexture(self.HollySuit1.SellLeg1, 1)
            self.HollySuit1.SellSleeve1 = loader.loadTexture('phase_3.5/maps/s_sleeve.jpg')
            self.SellSleeve1 = self.HollySuit1.find('**/arms').setTexture(self.HollySuit1.SellSleeve1, 1)
            self.SellHands1 = self.HollySuit1.find('**/hands')
            self.SellHands1.setColorScale(0.95, 0.75, 0.95, 1.0)
            HollyNeck1 = self.HollySuit1.find('**/joint_head')
            self.HollyHead1.reparentTo(HollyNeck1)
            self.HollySuit1.setPosHpr(-1.614, -194.110, -19.594, -27.220, 0, 0)
            self.HollySuit1.loop('suitA-squirt-large', restart = 0, fromFrame = 20, toFrame = 60)

            self.HollySuit2 = Actor('phase_3.5/models/char/SuitA-mod',
                                    {'suitA-squirt-large': 'phase_5/models/char/suitA-squirt-large'})
            self.HollySuit2.reparentTo(self.geom)
            self.HollySuit2.SellBlazer2 = loader.loadTexture('phase_3.5/maps/s_blazer.jpg')
            self.SellBlazer2 = self.HollySuit2.find('**/torso').setTexture(self.HollySuit2.SellBlazer2, 1)
            self.HollySuit2.SellLeg2 = loader.loadTexture('phase_3.5/maps/s_leg.jpg')
            self.SellLeg2 = self.HollySuit2.find('**/legs').setTexture(self.HollySuit2.SellLeg2, 1)
            self.HollySuit2.SellSleeve2 = loader.loadTexture('phase_3.5/maps/s_sleeve.jpg')
            self.SellSleeve2 = self.HollySuit2.find('**/arms').setTexture(self.HollySuit2.SellSleeve2, 1)
            self.SellHands2 = self.HollySuit2.find('**/hands')
            self.SellHands2.setColorScale(0.95, 0.75, 0.95, 1.0)
            HollyNeck2 = self.HollySuit2.find('**/joint_head')
            self.HollyHead2.reparentTo(HollyNeck2)
            self.HollySuit2.setPosHpr(-0.229, -194.023, -19.594, -4.022, 0, 0)
            self.HollySuit2.loop('suitA-squirt-large', restart = 0, fromFrame = 20, toFrame = 60)

            self.HollySuit3 = Actor('phase_3.5/models/char/SuitA-mod',
                                    {'suitA-squirt-large': 'phase_5/models/char/suitA-squirt-large'})
            self.HollySuit3.reparentTo(self.geom)
            self.HollySuit3.SellBlazer3 = loader.loadTexture('phase_3.5/maps/s_blazer.jpg')
            self.SellBlazer3 = self.HollySuit3.find('**/torso').setTexture(self.HollySuit3.SellBlazer3, 1)
            self.HollySuit3.SellLeg3 = loader.loadTexture('phase_3.5/maps/s_leg.jpg')
            self.SellLeg3 = self.HollySuit3.find('**/legs').setTexture(self.HollySuit3.SellLeg3, 1)
            self.HollySuit3.SellSleeve3 = loader.loadTexture('phase_3.5/maps/s_sleeve.jpg')
            self.SellSleeve3 = self.HollySuit3.find('**/arms').setTexture(self.HollySuit3.SellSleeve3, 1)
            self.SellHands3 = self.HollySuit3.find('**/hands')
            self.SellHands3.setColorScale(0.95, 0.75, 0.95, 1.0)
            HollyNeck3 = self.HollySuit3.find('**/joint_head')
            self.HollyHead3.reparentTo(HollyNeck3)
            self.HollySuit3.setPosHpr(1.892, -194.297, -19.594, 15.977, 0, 0)
            self.HollySuit3.loop('suitA-squirt-large', restart = 0, fromFrame = 20, toFrame = 60)

            self.HollySuit4 = Actor('phase_3.5/models/char/SuitA-mod',
                                    {'suitA-squirt-large': 'phase_5/models/char/suitA-squirt-large'})
            self.HollySuit4.reparentTo(self.geom)
            self.HollySuit4.SellBlazer4 = loader.loadTexture('phase_3.5/maps/s_blazer.jpg')
            self.SellBlazer4 = self.HollySuit4.find('**/torso').setTexture(self.HollySuit4.SellBlazer4, 1)
            self.HollySuit4.SellLeg4 = loader.loadTexture('phase_3.5/maps/s_leg.jpg')
            self.SellLeg4 = self.HollySuit4.find('**/legs').setTexture(self.HollySuit4.SellLeg4, 1)
            self.HollySuit4.SellSleeve4 = loader.loadTexture('phase_3.5/maps/s_sleeve.jpg')
            self.SellSleeve4 = self.HollySuit4.find('**/arms').setTexture(self.HollySuit4.SellSleeve4, 1)
            self.SellHands4 = self.HollySuit4.find('**/hands')
            self.SellHands4.setColorScale(0.95, 0.75, 0.95, 1.0)
            HollyNeck4 = self.HollySuit4.find('**/joint_head')
            self.HollyHead4.reparentTo(HollyNeck4)
            self.HollySuit4.setPosHpr(3.398, -194.494, -19.594, 36.625, 0, 0)
            self.HollySuit4.loop('suitA-squirt-large', restart = 0, fromFrame = 20, toFrame = 60)

            self.accept('h', self.hideHolly)
            self.accept('s', self.showHolly)

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
