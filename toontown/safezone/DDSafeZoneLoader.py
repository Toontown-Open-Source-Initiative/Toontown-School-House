from panda3d.core import *
import SafeZoneLoader
import DDPlayground
from direct.fsm import State
from toontown.char import CharDNA
from toontown.char import Char
from toontown.toonbase import ToontownGlobals
from direct.actor import Actor
from direct.interval.IntervalGlobal import *


class DDSafeZoneLoader(SafeZoneLoader.SafeZoneLoader):

    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.playgroundClass = DDPlayground.DDPlayground
        self.musicFile = 'phase_6/audio/bgm/DD_nbrhood.ogg'
        self.activityMusicFile = 'phase_6/audio/bgm/DD_SZ_activity.ogg'
        self.dnaFile = 'phase_6/dna/donalds_dock_sz.dna'
        self.safeZoneStorageDNAFile = 'phase_6/dna/storage_DD_sz.dna'

    def load(self):
        SafeZoneLoader.SafeZoneLoader.load(self)
        self.seagullSound = base.loader.loadSfx('phase_6/audio/sfx/SZ_DD_Seagull.ogg')
        self.underwaterSound = base.loader.loadSfx('phase_4/audio/sfx/AV_ambient_water.ogg')
        self.swimSound = base.loader.loadSfx('phase_4/audio/sfx/AV_swim_single_stroke.ogg')
        self.submergeSound = base.loader.loadSfx('phase_5.5/audio/sfx/AV_jump_in_water.ogg')
        water = self.geom.find('**/water')
        water.setTransparency(1)
        water.setColor(1, 1, 1, 0.8)
        self.boat = self.geom.find('**/donalds_boat')
        if self.boat.isEmpty():
            self.notify.error('Boat not found')
        else:
            wheel = self.boat.find('**/wheel')
            if wheel.isEmpty():
                self.notify.warning('Wheel not found')
            else:
                wheel.hide()
            self.boat.stash()
        self.dockSound = base.loader.loadSfx('phase_6/audio/sfx/SZ_DD_dockcreak.ogg')
        self.foghornSound = base.loader.loadSfx('phase_5/audio/sfx/SZ_DD_foghorn.ogg')
        self.bellSound = base.loader.loadSfx('phase_6/audio/sfx/SZ_DD_shipbell.ogg')
        self.waterSound = base.loader.loadSfx('phase_6/audio/sfx/SZ_DD_waterlap.ogg')


        clownFishModel = loader.loadModel("phase_4/models/char/clownFish-zero.bam")
        clownFishModel.reparentTo(render)
        self.clownFish = Actor.Actor(clownFishModel, copy=0)
        self.clownFish.reparentTo(render)
        self.clownFish.setPos(-11.403, -48.344, -9.308)
        self.clownFish.setScale(0.4)
        self.clownFish.setHpr(255, 0, 0)
        self.clownFish.loadAnims({'anim': 'phase_4/models/char/clownFish-swim.bam'})
        self.clownFish.loop('anim')

        clownFishModel2 = loader.loadModel("phase_4/models/char/clownFish-zero.bam")
        clownFishModel2.reparentTo(render)
        self.clownFish2 = Actor.Actor(clownFishModel2, copy=0)
        self.clownFish2.reparentTo(render)
        self.clownFish2.setPos(-10.403, -48.344, -8.308)
        self.clownFish2.setScale(0.4)
        self.clownFish2.setHpr(255, 0, 0)
        self.clownFish2.loadAnims({'anim': 'phase_4/models/char/clownFish-swim.bam'})
        self.clownFish2.loop('anim')
        #below checks number  of frames of an animation
        #numFrames = self.clownFish2.getNumFrames('anim')

        self.clownFish1Move = Sequence(
            LerpPosInterval(self.clownFish, 6, (-74.021, -32.160, -9.308)),
            LerpPosInterval(self.clownFish, 6, (-62.701, 16.049, -9.308)),
            LerpPosInterval(self.clownFish, 6, (-22.759, 54.937, -9.308)),
            LerpPosInterval(self.clownFish, 4, (9.270, 37.066, -9.308)),
            LerpPosInterval(self.clownFish, 6, (-2.356, -37.253, -9.308)),
            LerpPosInterval(self.clownFish, 1, (-11.403, -48.344, -9.308)),
        )

        self.clownFish1Rotate = Sequence(
            Wait(4),
            LerpHprInterval(self.clownFish, 2, (165, 0, 0)),
            Wait(4),
            LerpHprInterval(self.clownFish, 2, (140, 0, 0)),
            Wait(4),
            LerpHprInterval(self.clownFish, 2, (68, 0, 0)),
            Wait(3),
            LerpHprInterval(self.clownFish, 1, (-22, 0, 0)),
            Wait(4),
            LerpHprInterval(self.clownFish, 2, (-65, 0, 0)),
            LerpHprInterval(self.clownFish, 1, (-105, 0, 0))
        )

        self.clownFish2Move = Sequence(
            LerpPosInterval(self.clownFish2, 6, (-73.021, -32.160, -8.308)),
            LerpPosInterval(self.clownFish2, 6, (-61.021, 16.049, -8.308)),
            LerpPosInterval(self.clownFish2, 6, (-21.759, 54.937, -8.308)),
            LerpPosInterval(self.clownFish2, 6, (10.270, 38.066, -8.308)),
            LerpPosInterval(self.clownFish2, 6, (-1.356, -36.253, -8.308)),
            LerpPosInterval(self.clownFish2, 1.5, (-10.403, -48.344, -8.308))
        )

        self.clownFish1Move.loop()
        self.clownFish1Rotate.loop()
        #self.clownFish2Move.loop()

    def unload(self):
        SafeZoneLoader.SafeZoneLoader.unload(self)
        del self.seagullSound
        del self.underwaterSound
        del self.swimSound
        del self.dockSound
        del self.foghornSound
        del self.bellSound
        del self.waterSound
        del self.submergeSound
        del self.boat

        self.clownFish.removeNode()
        self.clownFish2.removeNode()
        del self.clownFish
        del self.clownFish2


    def enter(self, requestStatus):
        SafeZoneLoader.SafeZoneLoader.enter(self, requestStatus)

    def exit(self):
        SafeZoneLoader.SafeZoneLoader.exit(self)
