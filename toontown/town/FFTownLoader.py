import TownLoader
import FFStreet
from toontown.suit import Suit

class FFTownLoader(TownLoader.TownLoader):

    def __init__(self,hood,parentFSM,doneEvent):
        TownLoader.TownLoader.__init__(self,hood,parentFSM,doneEvent)
        self.streetClass = FFStreet.FFStreet
        self.musicFile = 'phase_6/audio/bgm/FF_SZ.ogg'
        self.activityMusicFile = 'phase_6/audio/bgm/FF_SZ_activity.ogg'
        self.townStorageDNAFile = 'phase_6/dna/storage_FF_town.dna'

    def load(self,zoneId):
        TownLoader.TownLoader.load(self,zoneId)
        Suit.loadSuits(3)
        dnaFile = 'phase_6/dna/funny_farm_' + str(self.canonicalBranchZone) + ".dna"
        self.createHood(dnaFile)
    
    def unload(self):
        Suit.unloadSuits(3)
        TownLoader.TownLoader.unload(self)