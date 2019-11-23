from panda3d.core import *
import Playground
from direct.task.Task import Task
import random
from direct.fsm import ClassicFSM, State
from direct.actor import Actor
from toontown.toonbase import ToontownGlobals
from direct.directnotify import DirectNotifyGlobal
from toontown.hood import Place
from direct.interval.IntervalGlobal import *

class DDPlayground(Playground.Playground):
    notify = DirectNotifyGlobal.directNotify.newCategory('DDPlayground')

    def __init__(self, loader, parentFSM, doneEvent):
        Playground.Playground.__init__(self, loader, parentFSM, doneEvent)
        self.cameraSubmerged = -1
        self.toonSubmerged = -1
        self.activityFsm = ClassicFSM.ClassicFSM('Activity', [State.State('off', self.enterOff, self.exitOff, ['OnBoat']), State.State('OnBoat', self.enterOnBoat, self.exitOnBoat, ['off'])], 'off', 'off')
        self.activityFsm.enterInitialState()

    def load(self):
        Playground.Playground.load(self)
        sadsound = base.loader.loadSfx('phase_5/audio/sfx/ENC_Lose.ogg')
        crysound = base.loader.loadSfx('phase_4/audio/sfx/avatar_emotion_very_sad_1.ogg')
        self.toontanic = loader.loadModel('phase_5/models/props/ship')
        self.toontanic.reparentTo(render)
        self.toontanic.setPos(0,0,0)

        self.piano = loader.loadModel('phase_6/models/props/piano') # Loads our Piano
        self.piano.reparentTo(render)                               # Makes our Piano a child node of Render
        self.piano.setPos(0,0,30)                                   # Sets our x,y,z coordinates of our Piano

        self.piano.setHpr(90,45,0)                                  # Rotates the Piano degrees in x direction (x,y,z)
        self.piano.setColorScale(0,1,0,1)                           # Makes the piano green (R,G,B,T)  T= transparency

        self.apple = loader.loadModel('phase_4/models/minigames/apple') # Loads our Apple
        self.apple.reparentTo(self.piano)                               # Makes our Apple a child node of Piano
        self.apple.setScale(8)                                          # Sets our Apple's scale to 8

        self.interval = Sequence(
            Wait(3.0),
            LerpPosInterval(self.toontanic, 7.2, (0,-60,0)),
            Wait(0.5),
            LerpHprInterval(self.toontanic, 1.0, (0,90, 0)),
            Wait(1.0),
            Parallel(
                LerpPosInterval(self.toontanic, 4.0, (0, -60, -30)),
                Func(crysound.play)
            ),
            Wait(0.3),
            Func(sadsound.play),
            Wait(3.0),
            Func(self.toontanic.setHpr, 0, 0, 0)
        )
        self.interval.loop()

    def unload(self):
        self.piano.removenode()
        del self.piano

        self.toontanic.removenode()
        del self.toontanic

        del self.activityFsm
        Playground.Playground.unload(self)

    def enter(self, requestStatus):
        self.nextSeagullTime = 0
        taskMgr.add(self.__seagulls, 'dd-seagulls')
        self.loader.hood.setWhiteFog()
        Playground.Playground.enter(self, requestStatus)

    def exit(self):
        Playground.Playground.exit(self)
        taskMgr.remove('dd-check-toon-underwater')
        taskMgr.remove('dd-check-cam-underwater')
        taskMgr.remove('dd-seagulls')
        self.loader.hood.setNoFog()

    def enterStart(self):
        self.cameraSubmerged = 0
        self.toonSubmerged = 0
        taskMgr.add(self.__checkToonUnderwater, 'dd-check-toon-underwater')
        taskMgr.add(self.__checkCameraUnderwater, 'dd-check-cam-underwater')

    def enterDoorOut(self):
        taskMgr.remove('dd-check-toon-underwater')

    def exitDoorOut(self):
        pass

    def enterDoorIn(self, requestStatus):
        Playground.Playground.enterDoorIn(self, requestStatus)
        taskMgr.add(self.__checkToonUnderwater, 'dd-check-toon-underwater')

    def __checkCameraUnderwater(self, task):
        if camera.getZ(render) < 1.0:
            self.__submergeCamera()
        else:
            self.__emergeCamera()
        return Task.cont

    def __checkToonUnderwater(self, task):
        if base.localAvatar.getZ() < -2.3314585:
            self.__submergeToon()
        else:
            self.__emergeToon()
        return Task.cont

    def __submergeCamera(self):
        if self.cameraSubmerged == 1:
            return
        self.loader.hood.setUnderwaterFog()
        base.playSfx(self.loader.underwaterSound, looping=1, volume=0.8)
        self.loader.seagullSound.stop()
        taskMgr.remove('dd-seagulls')
        self.cameraSubmerged = 1
        self.walkStateData.setSwimSoundAudible(1)

    def __emergeCamera(self):
        if self.cameraSubmerged == 0:
            return
        self.loader.hood.setWhiteFog()
        self.loader.underwaterSound.stop()
        self.nextSeagullTime = random.random() * 8.0
        taskMgr.add(self.__seagulls, 'dd-seagulls')
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
        base.localAvatar.d_playSplashEffect(pos[0], pos[1], 1.675)
        self.toonSubmerged = 1

    def __emergeToon(self):
        if self.toonSubmerged == 0:
            return
        self.walkStateData.fsm.request('walking')
        self.toonSubmerged = 0

    def __seagulls(self, task):
        if task.time < self.nextSeagullTime:
            return Task.cont
        base.playSfx(self.loader.seagullSound)
        self.nextSeagullTime = task.time + random.random() * 4.0 + 8.0
        return Task.cont

    def enterTeleportIn(self, requestStatus):
        self.toonSubmerged = -1
        taskMgr.remove('dd-check-toon-underwater')
        Playground.Playground.enterTeleportIn(self, requestStatus)

    def teleportInDone(self):
        self.toonSubmerged = -1
        taskMgr.add(self.__checkToonUnderwater, 'dd-check-toon-underwater')
        Playground.Playground.teleportInDone(self)

    def enterOff(self):
        return None

    def exitOff(self):
        return None

    def enterOnBoat(self):
        base.localAvatar.b_setParent(ToontownGlobals.SPDonaldsBoat)
        base.playSfx(self.loader.waterSound, looping=1)

    def exitOnBoat(self):
        base.localAvatar.b_setParent(ToontownGlobals.SPRender)
        self.loader.waterSound.stop()