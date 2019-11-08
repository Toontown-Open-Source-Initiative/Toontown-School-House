from panda3d.core import *
from direct.interval.IntervalGlobal import *
import ToonHood
from toontown.town import FFTownLoader
from toontown.safezone import FFSafeZoneLoader
from toontown.toonbase.ToontownGlobals import *
import SkyUtil
from direct.directnotify import DirectNotifyGlobal

class FFHood(ToonHood.ToonHood):
    notify = DirectNotifyGlobal.directNotify.newCategory('FFHood')

    def __init__(self,parentFSM,doneEvent,dnaStore,hoodId):
        ToonHood.ToonHood.__init__(self, parentFSM, doneEvent, dnaStore, hoodId)
        self.id = FunnyFarm
        self.townLoaderClass = FFTownLoader.FFTownLoader
        self.safeZoneLoaderClass = FFSafeZoneLoader.FFSafeZoneLoader
        self.storageDnaFile = 'phase_6/dna/storage_FF.dna'
        self.holidayStorageDNADict = {WINTER_DECORATIONS: ['phase_6/dna/winter_storage_FF.dna', 'phase_6/dna/winter_storage_FF_sz.dna'],
         WACKY_WINTER_DECORATIONS: ['phase_6/dna/winter_storage_FF.dna', 'phase_6/dna/winter_storage_FF_sz.dna'],
         HALLOWEEN_PROPS: ['phase_6/dna/halloween_props_storage_FF.dna', 'phase_6/dna/halloween_props_storage_FF_sz.dna'],
         SPOOKY_PROPS: ['phase_6/dna/halloween_props_storage_FF.dna', 'phase_6/dna/halloween_props_storage_FF_sz.dna']}
        self.skyFile = 'phase_3.5/models/props/TT_sky'
        self.spookySkyFile = 'phase_3.5/models/props/BR_sky'
        self.titleColor = (1.0, 0.5, 0.4, 1.0)
    
    def load(self):
        ToonHood.ToonHood.load()
        self.parentFSM.getStateNamed('FFHood').addChild(self.fsm)
  
    def unload(self):
        self.parentFSM.getStateNamed('FFHood').removeChild(self.fsm)
        ToonHood.ToonHood.unload()

    def enter(self, *args):
        ToonHood.ToonHood.enter(self,*args)
    
    def exit(self):
        ToonHood.ToonHood.exit(self)
    
    def skyTrack(self,task):
        return SkyUtil.cloudSkyTrack(task)
    
    def startSky(self):
        self.sky.setTransparency(TransparencyAttrib.MDual,1)
        if not self.sky.getTag('sky') == 'Regular':
            self.endSpookySky()
        SkyUtil.startCloudSky

    def startSpookySky(self):
        pass     #TODO
