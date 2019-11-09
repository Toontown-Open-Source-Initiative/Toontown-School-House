from panda3d.core import *
import SafeZoneLoader
import FFPlayground
import random
from toontown.launcher import DownloadForceAcknowledge

class FFSafeZoneLoader(SafeZoneLoader.SafeZoneLoader):

    def __init__(self,hood,parentFSM,doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(self,hood,parentFSM,doneEvent)
        self.playgroundClass = FFPlayground.FFPlayground
        self.musicFile = 'phase_6/audio/bgm/FF_nbrhood.mp3'
        self.activityMusicFile = 'phase_6/audio/bgm/FF_SZ_activity.mp3'
        self.dnaFile = 'phase_6/dna/funny_farm_sz.dna'
        self.safeZoneStorageDNAFile = 'phase_6/dna/storage_FF_sz.dna'
    
   