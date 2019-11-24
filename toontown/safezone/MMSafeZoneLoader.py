from panda3d.core import *
import SafeZoneLoader
import MMPlayground
from toontown.toonbase import ToontownGlobals


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
        # BlueEyes
        self.blueEyes = loader.loadModel('phase_6/models/extras/bams/BlueEyesWhiteDragon')
        self.blueEyes.reparentTo(render)
        self.blueEyes.setPos(62.999, -21.119, -13.475)
        # self.blueEyes.setHPR(x, x, x) <-Get Real Value

    # Star Wars
        self.bb8 = loader.loadModel('phase_6/models/extras/bams/BB8')
        self.bb8.reparentTo(render)
        self.blueEyes.setPos(0, 0, 0)
    def unload(self):
        SafeZoneLoader.SafeZoneLoader.unload(self)
        del self.piano
        self.blueEyes.removeNode()
        del self.blueEyes
        self.bb8.removeNode()
        del self.bb8