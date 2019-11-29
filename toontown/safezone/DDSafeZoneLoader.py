from panda3d.core import *
import SafeZoneLoader
import DDPlayground
from direct.fsm import State
from toontown.char import CharDNA
from toontown.char import Char
from toontown.toonbase import ToontownGlobals
from direct.actor import Actor


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
        self.clownFish.setScale(0.5)
        self.clownFish.loadAnims({'anim': 'phase_4/models/char/clownFish-swim.bam'})
        self.clownFish.loop('anim')

        #clownFishModel2 = loader.loadModel("phase_4/models/char/clownFish-zero.bam")
        #clownFishModel2.reparentTo(render)
        #clownFish2 = Actor.Actor(clownFishModel2, copy=0)
        #clownFish2.reparentTo(render)
        #clownFish2.setPos(-11.403, -48.344, -6.308)
        #clownFish2.setScale(0.5)
        #clownFish2.loadAnims({'anim': 'phase_4/models/char/clownFish-swim.bam'})
        #clownFish2.loop('anim')

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

    def enter(self, requestStatus):
        SafeZoneLoader.SafeZoneLoader.enter(self, requestStatus)

    def exit(self):
        SafeZoneLoader.SafeZoneLoader.exit(self)
