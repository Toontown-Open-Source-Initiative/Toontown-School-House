import CogHood
from panda3d.core import *
from toontown.toonbase import ToontownGlobals
from toontown.coghq import SellbotCogHQLoader
from direct.task.Task import Task
from direct.fsm import State
from toontown.safezone import PublicWalk
from direct.fsm import ClassicFSM, State

class SellbotHQ(CogHood.CogHood):
    waterLevel = -1

    def __init__(self, parentFSM, doneEvent, dnaStore, hoodId):
        CogHood.CogHood.__init__(self, parentFSM, doneEvent, dnaStore, hoodId)
        self.id = ToontownGlobals.SellbotHQ
        self.cogHQLoaderClass = SellbotCogHQLoader.SellbotCogHQLoader
        self.storageDNAFile = None
        self.skyFile = 'phase_9/models/cogHQ/cog_sky'
        self.titleColor = (0.5, 0.5, 0.5, 1.0)
        self.cameraSubmerged = 0
        self.toonSubmerged = 0
        self.underwaterFogColor = Vec4(30/255, 0, 105/255, 1.0)
        self.whiteFogColor = Vec4(0.8, 0.8, 0.8, 1.0)
#        ground = self.geom.find('**/polySurface81')
#        self.activityFsm = ClassicFSM.ClassicFSM('Activity', [State.State('off', self.enterOff, self.exitOff)
#        self.activityFsm.enterInitialState()
        return

    def load(self):
        CogHood.CogHood.load(self)
        self.sky.setScale(2.0)
        self.walkDoneEvent = 'walkDone'
        self.parentFSM.getStateNamed('SellbotHQ').addChild(self.fsm)
        self.walkStateData = PublicWalk.PublicWalk(self.fsm, self.walkDoneEvent)
        self.walkStateData.load()
        self.fog = Fog('SBHQFog')

    def unload(self):
        self.parentFSM.getStateNamed('SellbotHQ').removeChild(self.fsm)
        del self.cogHQLoaderClass
        CogHood.CogHood.unload(self)

    def enter(self, *args):
        CogHood.CogHood.enter(self, *args)
        localAvatar.setCameraFov(ToontownGlobals.CogHQCameraFov)
        base.camLens.setNearFar(ToontownGlobals.CogHQCameraNear, ToontownGlobals.CogHQCameraFar)

    def exit(self):
        localAvatar.setCameraFov(ToontownGlobals.DefaultCameraFov)
        base.camLens.setNearFar(ToontownGlobals.DefaultCameraNear, ToontownGlobals.DefaultCameraFar)
        CogHood.CogHood.exit(self)
        taskMgr.remove('sbhq-check-toon-underwater')
        taskMgr.remove('sbhq-check-cam-underwater')

    def enterStart(self):
        self.cameraSubmerged = 0
        self.toonSubmerged = 0
        taskMgr.add(self.__checkToonUnderwater, 'sbhq-check-toon-underwater')
        taskMgr.add(self.__checkCameraUnderwater, 'sbhq-check-cam-underwater')


    def __checkCameraUnderwater(self, task):
        if camera.getZ(render) < self.waterLevel:
            self.__submergeCamera()
        else:
            self.__emergeCamera()
        return Task.cont

    def __checkToonUnderwater(self, task):
        if base.localAvatar.getZ() < self.waterLevel:
            self.__submergeToon()
        else:
            self.__emergeToon()
        return Task.cont

    def __submergeCamera(self):
        if self.cameraSubmerged == 1:
            return
#        self.ground.setColorScale(66/255, 46/255, 146/255, 1.0)
        self.groundTint = 1
        self.loader.hood.setUnderwaterFog()
        self.walkStateData.fsm.request('swimming', [self.loader.swimSound])
        base.playSfx(self.loader.underwaterSound, looping=1, volume=0.8)
        self.cameraSubmerged = 1
        self.walkStateData.setSwimSoundAudible(1)

    def __emergeCamera(self):
#        self.ground.clearColorScale()
        if self.cameraSubmerged == 0:
            return
        self.loader.hood.setNoFog()
#        self.loader.hood.setNoFog()
        self.walkStateData.fsm.request('walking')
        self.loader.underwaterSound.stop()
        self.cameraSubmerged = 0
        self.groundTint = 0
        self.walkStateData.setSwimSoundAudible(0)

    def __submergeToon(self):
        if self.toonSubmerged == 1:
            return
        base.playSfx(self.loader.submergeSound)
        if base.config.GetBool('disable-flying-glitch') == 0:
#            self.fsm.request('walk')
            return
#        self.walkStateData.fsm.request('swimming', [self.loader.swimSound])
        pos = base.localAvatar.getPos(render)
        base.localAvatar.d_playSplashEffect(pos[0], pos[1], self.waterLevel)
#        base.localAvatar.b_setAnimState('swim', 1.0)
        self.toonSubmerged = 1

    def __emergeToon(self):
        if self.toonSubmerged == 0:
            return
#        self.walkStateData.fsm.request('walking')
        self.toonSubmerged = 0

    def setUnderwaterFog(self):
        if base.wantFog:
            self.fog.setColor(self.underwaterFogColor)
            self.fog.setLinearRange(0.1, 60)
            render.setFog(self.fog)
            self.sky.setFog(self.fog)

    def setNoFog(self):
        if base.wantFog:
            render.clearFog()
            self.sky.clearFog()

'''
    def enterOff(self):
        return None

    def exitOff(self):
        return None'''
