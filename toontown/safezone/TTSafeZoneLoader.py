from panda3d.core import *
import SafeZoneLoader
import TTPlayground
import random
from toontown.launcher import DownloadForceAcknowledge

class TTSafeZoneLoader(SafeZoneLoader.SafeZoneLoader):

    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.playgroundClass = TTPlayground.TTPlayground
        self.musicFile = 'phase_4/audio/bgm/TC_nbrhood.ogg'
        self.activityMusicFile = 'phase_3.5/audio/bgm/TC_SZ_activity.ogg'
        self.dnaFile = 'phase_4/dna/toontown_central_sz.dna'
        self.safeZoneStorageDNAFile = 'phase_4/dna/storage_TT_sz.dna'

    def load(self):
        SafeZoneLoader.SafeZoneLoader.load(self)
        self.elevator = loader.loadModel('phase_4/models/modules/elevator')
        self.elevator.reparentTo(render)
        self.elevator.setPos(144,81.8,2.525)
        self.elevator.setHpr(-100, 0, 0)
        self.leftDoor = self.elevator.find('**/left-door')
        self.leftDoor.setPos(3.5, 0, 0)
        self.rightDoor = self.elevator.find('**/right-door')
        self.rightDoor.setPos(-3.5, 0, 0)
        self.birdSound = map(base.loader.loadSfx,['phase_4/audio/sfx/SZ_TC_bird1.ogg','phase_4/audio/sfx/SZ_TC_bird2.ogg','phase_4/audio/sfx/SZ_TC_bird3.ogg'])

    def unload(self):
        del self.birdSound
        self.elevator.removeNode()
        del self.elevator
        SafeZoneLoader.SafeZoneLoader.unload(self)

    def enter(self, requestStatus):
        SafeZoneLoader.SafeZoneLoader.enter(self, requestStatus)

    def exit(self):
        SafeZoneLoader.SafeZoneLoader.exit(self)
