from panda3d.core import *
from toontown.toonbase import ToontownGlobals
import Playground
from toontown.launcher import DownloadForceAcknowledge
from toontown.building import Elevator
from toontown.toontowngui import TTDialog
from toontown.toonbase import TTLocalizer
from toontown.racing import RaceGlobals
from direct.fsm import State
from toontown.safezone import PicnicBasket
from toontown.safezone import GolfKart
from direct.task.Task import Task

class OZPlayground(Playground.Playground):
    waterLevel = -0.53

    def __init__(self, loader, parentFSM, doneEvent):
        Playground.Playground.__init__(self, loader, parentFSM, doneEvent)
        self.parentFSM = parentFSM
        self.picnicBasketBlockDoneEvent = 'picnicBasketBlockDone'
        self.cameraSubmerged = -1
        self.toonSubmerged = -1
        self.fsm.addState(State.State('picnicBasketBlock', self.enterPicnicBasketBlock, self.exitPicnicBasketBlock, ['walk']))
        state = self.fsm.getStateNamed('walk')
        state.addTransition('picnicBasketBlock')
        self.picnicBasketDoneEvent = 'picnicBasketDone'

    def load(self):
        Playground.Playground.load(self)
        self.mole = loader.loadModel('phase_12/models/bossbotHQ/mole_cog')
        self.mole.reparentTo(render)
        self.mole.setPos(-47.677, -146.560, -2)
        self.mole.setHpr(-176.020, 0, 0)
        self.mole.setScale(3.45)

        self.moleHole = loader.loadModel('phase_12/models/bossbotHQ/mole_hole')
        self.moleHole.reparentTo(self.mole)
        self.mole.setPos(-47.677, -146.560, 0)

        self.leftMoney = loader.loadModel('phase_10/models/cashbotHQ/MoneyStackPallet')
        self.leftMoney.reparentTo(render)
        self.leftMoney.setPos(-39.105, -125, 0)
        self.leftMoney.setHpr(180, 0, 0)
        self.leftMoney.setScale(0.5)

        self.rightMoney = loader.loadModel('phase_10/models/cashbotHQ/MoneyStackPallet')
        self.rightMoney.reparentTo(render)
        self.rightMoney.setPos(-55.725, -125, 0)
        self.rightMoney.setHpr(180, 0, 0)
        self.rightMoney.setScale(0.5)

        self.leftGavel = loader.loadModel('phase_11/models/lawbotHQ/LB_gavel')
        self.leftGavel.reparentTo(render)
        self.leftGavel.setPos(-40, -133, 0)
        self.leftGavel.setHpr(90, -65, 0)

        self.rightGavel = loader.loadModel('phase_11/models/lawbotHQ/LB_gavel')
        self.rightGavel.reparentTo(render)
        self.rightGavel.setPos(-55, -133, 0)
        self.rightGavel.setHpr(-90, -25, 0)

        self.cogWheel = loader.loadModel('phase_9/models/char/gearProp')
        self.cogWheel.reparentTo(render)
        self.cogWheel.setPos(-48, -136, 25)
        self.cogWheel.setHpr(0, 90, 0)


    def unload(self):
        Playground.Playground.unload(self)
        self.mole.removeNode()
        del self.mole
        self.moleHole.removeNode()
        del self.moleHole
        self.leftMoney.removeNode()
        del self.leftMoney
        self.rightMoney.removeNode()
        del self.rightMoney
        self.leftGavel.removeNode()
        del self.leftGavel
        self.rightGavel.removeNode()
        del self.rightGavel
        self.cogWheel.removeNode()
        del self.cogWheel

    def enter(self, requestStatus):
        Playground.Playground.enter(self, requestStatus)

    def exit(self):
        Playground.Playground.exit(self)
        taskMgr.remove('oz-check-toon-underwater')
        taskMgr.remove('oz-check-cam-underwater')
        self.loader.hood.setNoFog()

    def doRequestLeave(self, requestStatus):
        self.fsm.request('trialerFA', [requestStatus])

    def enterDFA(self, requestStatus):
        doneEvent = 'dfaDoneEvent'
        self.accept(doneEvent, self.enterDFACallback, [requestStatus])
        self.dfa = DownloadForceAcknowledge.DownloadForceAcknowledge(doneEvent)
        if requestStatus['hoodId'] == ToontownGlobals.MyEstate:
            self.dfa.enter(base.cr.hoodMgr.getPhaseFromHood(ToontownGlobals.MyEstate))
        else:
            self.dfa.enter(5)

    def enterStart(self):
        self.cameraSubmerged = 0
        self.toonSubmerged = 0
        taskMgr.add(self.__checkToonUnderwater, 'oz-check-toon-underwater')
        taskMgr.add(self.__checkCameraUnderwater, 'oz-check-cam-underwater')

    def __checkCameraUnderwater(self, task):
        if camera.getZ(render) < self.waterLevel:
            self.__submergeCamera()
        else:
            self.__emergeCamera()
        return Task.cont

    def __checkToonUnderwater(self, task):
        if base.localAvatar.getZ() < -4.0:
            self.__submergeToon()
        else:
            self.__emergeToon()
        return Task.cont

    def __submergeCamera(self):
        if self.cameraSubmerged == 1:
            return
        self.loader.hood.setUnderwaterFog()
        base.playSfx(self.loader.underwaterSound, looping=1, volume=0.8)
        self.cameraSubmerged = 1
        self.walkStateData.setSwimSoundAudible(1)

    def __emergeCamera(self):
        if self.cameraSubmerged == 0:
            return
        self.loader.hood.setNoFog()
        self.loader.underwaterSound.stop()
        self.cameraSubmerged = 0
        self.walkStateData.setSwimSoundAudible(0)

    def __submergeToon(self):
        if self.toonSubmerged == 1:
            return
        base.playSfx(self.loader.submergeSound)
        if base.config.GetBool('disable-flying-glitch') == 0:
            self.fsm.request('walk')
        self.walkStateData.fsm.request('swimming', [self.loader.swimSound])
        pos = base.localAvatar.getPos(render)
        base.localAvatar.d_playSplashEffect(pos[0], pos[1], self.waterLevel)
        self.toonSubmerged = 1

    def __emergeToon(self):
        if self.toonSubmerged == 0:
            return
        self.walkStateData.fsm.request('walking')
        self.toonSubmerged = 0

    def enterTeleportIn(self, requestStatus):
        reason = requestStatus.get('reason')
        if reason == RaceGlobals.Exit_Barrier:
            requestStatus['nextState'] = 'popup'
            self.dialog = TTDialog.TTDialog(text=TTLocalizer.KartRace_RaceTimeout, command=self.__cleanupDialog, style=TTDialog.Acknowledge)
        elif reason == RaceGlobals.Exit_Slow:
            requestStatus['nextState'] = 'popup'
            self.dialog = TTDialog.TTDialog(text=TTLocalizer.KartRace_RacerTooSlow, command=self.__cleanupDialog, style=TTDialog.Acknowledge)
        elif reason == RaceGlobals.Exit_BarrierNoRefund:
            requestStatus['nextState'] = 'popup'
            self.dialog = TTDialog.TTDialog(text=TTLocalizer.KartRace_RaceTimeoutNoRefund, command=self.__cleanupDialog, style=TTDialog.Acknowledge)
        self.toonSubmerged = -1
        taskMgr.remove('oz-check-toon-underwater')
        Playground.Playground.enterTeleportIn(self, requestStatus)

    def teleportInDone(self):
        self.toonSubmerged = -1
        taskMgr.add(self.__checkToonUnderwater, 'oz-check-toon-underwater')
        Playground.Playground.teleportInDone(self)

    def __cleanupDialog(self, value):
        if self.dialog:
            self.dialog.cleanup()
            self.dialog = None
        if hasattr(self, 'fsm'):
            self.fsm.request('walk', [1])
        return

    def enterPicnicBasketBlock(self, picnicBasket):
        base.localAvatar.laffMeter.start()
        base.localAvatar.b_setAnimState('off', 1)
        base.localAvatar.cantLeaveGame = 1
        self.accept(self.picnicBasketDoneEvent, self.handlePicnicBasketDone)
        self.trolley = PicnicBasket.PicnicBasket(self, self.fsm, self.picnicBasketDoneEvent, picnicBasket.getDoId(), picnicBasket.seatNumber)
        self.trolley.load()
        self.trolley.enter()

    def exitPicnicBasketBlock(self):
        base.localAvatar.laffMeter.stop()
        base.localAvatar.cantLeaveGame = 0
        self.ignore(self.trolleyDoneEvent)
        self.trolley.unload()
        self.trolley.exit()
        del self.trolley

    def detectedPicnicTableSphereCollision(self, picnicBasket):
        self.fsm.request('picnicBasketBlock', [picnicBasket])

    def handleStartingBlockDone(self, doneStatus):
        self.notify.debug('handling StartingBlock done event')
        where = doneStatus['where']
        if where == 'reject':
            self.fsm.request('walk')
        elif where == 'exit':
            self.fsm.request('walk')
        elif where == 'racetrack':
            self.doneStatus = doneStatus
            messenger.send(self.doneEvent)
        else:
            self.notify.error('Unknown mode: ' + where + ' in handleStartingBlockDone')

    def handlePicnicBasketDone(self, doneStatus):
        self.notify.debug('handling picnic basket done event')
        mode = doneStatus['mode']
        if mode == 'reject':
            self.fsm.request('walk')
        elif mode == 'exit':
            self.fsm.request('walk')
        else:
            self.notify.error('Unknown mode: ' + mode + ' in handlePicnicBasketDone')

    def showPaths(self):
        from toontown.classicchars import CCharPaths
        from toontown.toonbase import TTLocalizer
        self.showPathPoints(CCharPaths.getPaths(TTLocalizer.Chip))
