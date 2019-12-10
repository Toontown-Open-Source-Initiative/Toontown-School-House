from panda3d.core import *
import SafeZoneLoader
import MMPlayground
from toontown.toonbase import ToontownGlobals
from direct.interval.IntervalGlobal import *


class MMSafeZoneLoader(SafeZoneLoader.SafeZoneLoader):

    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.playgroundClass = MMPlayground.MMPlayground
        self.musicFile = 'phase_6/audio/bgm/MM_nbrhood.ogg'
        self.activityMusicFile = 'phase_6/audio/bgm/MM_SZ_activity.ogg'
        self.dnaFile = 'phase_6/dna/minnies_melody_land_sz.dna'
        self.safeZoneStorageDNAFile = 'phase_6/dna/storage_MM_sz.dna'

    def load(self):
        print 'loading MM safezone'
        SafeZoneLoader.SafeZoneLoader.load(self)
        self.piano = self.geom.find('**/center_icon')
        if self.piano.isEmpty():
            self.notify.error('Piano not found')
        else:
            hq = self.geom.find('**/*toon_landmark_hqMM_DNARoot')
            hq.wrtReparentTo(self.piano)

        # Yugioh
        #self.blueEyes = loader.loadModel('phase_6/models/extras/bams/BlueEyesWhiteDragon')
        #self.blueEyes.reparentTo(render)
        #self.blueEyes.setPos(62.999, -21.119, 40)

        #self.sequence = Sequence(
        #    LerpPosInterval(self.blueEyes, 2.5, (62.999, -21.119, 60)),
        #    Wait(0.25),
        #    LerpPosInterval(self.blueEyes, 2.5, (62.999, -21.119, 40))
        #)
        #self.sequence.loop()
    # Star Wars
        #self.bb8 = loader.loadModel('phase_6/models/extras/bams/BB8')
        #self.bb8.reparentTo(render)
        #self.bb8.setPos(64.199, -98.559, -14.481)
        #self.bb8.setScale(0.25)
        #self.bb8.setHpr(-349.820, 0, 0)

        #self.bb8Move = Sequence(
        #    LerpPosInterval(self.bb8, 5, (-19.337, -98.489, -14.485)),
        #    Wait(0.7),
        #    LerpPosInterval(self.bb8, 5, (-48.061, -38.341, -14.649)),
        #    Wait(0.7),
        #    LerpPosInterval(self.bb8, 5, (-58.508, 19.285, -14.489)),
        #    Wait(0.7),
        #    LerpPosInterval(self.bb8, 5, (-19.175, 58.556, -14.484)),
        #    Wait(0.7),
        #    LerpPosInterval(self.bb8, 5, (64.301, 58.495, -14.481)),
        #    Wait(0.7),
        #    LerpPosInterval(self.bb8, 5, (51.671, -13.673, -14.593)),
        #    Wait(0.7),
        #    LerpPosInterval(self.bb8, 5, (64.199, -98.559, -14.481))
        #)
        #self.bb8Move.loop()

    def unload(self):
        SafeZoneLoader.SafeZoneLoader.unload(self)
        del self.piano
        #self.blueEyes.removeNode()
        #del self.blueEyes
        #self.bb8.removeNode()
        #del self.bb8