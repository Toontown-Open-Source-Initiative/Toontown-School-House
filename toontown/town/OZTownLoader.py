import TownLoader
import OZStreet
from toontown.suit import Suit

class OZTownLoader(TownLoader.TownLoader):

    def __init__(self, hood, parentFSM, doneEvent):
        TownLoader.TownLoader.__init__(self,hood,parentFSM,doneEvent)
        self.streetClass = OZStreet.OZStreet
        self.musicFile = 'phase_6/audio/bgm/OZ_SZ.ogg'
        self.activityMusicFile = 'phase_3.5/audio/bgm/TC_SZ_activity.ogg'
        self.townStorageDNAFile = 'phase_6/dna/storage_OZ_town.dna'

    def load(self,zoneId):
        TownLoader.TownLoader.load(self,zoneId)
        Suit.loadSuits(3)
        dnaFile = 'phase_6/dna/outdoor_zone_' + str(self.canonicalBranchZone) + '.dna'
        self.createHood(dnaFile)

    def unload(self):
        Suit.unloadSuits(3)
        TownLoader.TownLoader.unload(self)
