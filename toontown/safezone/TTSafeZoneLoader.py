from toontown.safezone import SafeZoneLoader
from toontown.safezone import TTPlayground
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import *


class TTSafeZoneLoader(SafeZoneLoader.SafeZoneLoader):
    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.crate23 = loader.loadModel('phase_9/models/cogHQ/woodCrateB')
        self.crate22 = loader.loadModel('phase_9/models/cogHQ/woodCrateB')
        self.crate21 = loader.loadModel('phase_9/models/cogHQ/woodCrateB')
        self.crate20 = loader.loadModel('phase_9/models/cogHQ/woodCrateB')
        self.crate19 = loader.loadModel('phase_9/models/cogHQ/woodCrateB')
        self.crate18 = loader.loadModel('phase_9/models/cogHQ/woodCrateB')
        self.crate17 = loader.loadModel('phase_9/models/cogHQ/woodCrateB')
        self.crate16 = loader.loadModel('phase_9/models/cogHQ/woodCrateB')
        self.crate15 = loader.loadModel('phase_9/models/cogHQ/woodCrateB')
        self.crate14 = loader.loadModel('phase_9/models/cogHQ/woodCrateB')
        self.crate13 = loader.loadModel('phase_9/models/cogHQ/woodCrateB')
        self.crate12 = loader.loadModel('phase_9/models/cogHQ/woodCrateB')
        self.crate11 = loader.loadModel('phase_9/models/cogHQ/woodCrateB')
        self.crate10 = loader.loadModel('phase_9/models/cogHQ/woodCrateB')
        self.crate9 = loader.loadModel('phase_9/models/cogHQ/woodCrateB')
        self.crate8 = loader.loadModel('phase_9/models/cogHQ/woodCrateB')
        self.crate7 = loader.loadModel('phase_9/models/cogHQ/woodCrateB')
        self.crate6 = loader.loadModel('phase_9/models/cogHQ/woodCrateB')
        self.crate5 = loader.loadModel('phase_9/models/cogHQ/woodCrateB')
        self.crate4 = loader.loadModel('phase_9/models/cogHQ/woodCrateB')
        self.crate3 = loader.loadModel('phase_9/models/cogHQ/woodCrateB')
        self.crate2 = loader.loadModel('phase_9/models/cogHQ/woodCrateB')
        self.crate1 = loader.loadModel('phase_9/models/cogHQ/woodCrateB')
        self.interval = Sequence(
            Parallel(LerpPosInterval(self.crate17, 8, (87, 16, 30)),
                     LerpPosInterval(self.crate17, 8, (87, 16, 15)),
                     LerpPosInterval(self.crate17, 8, (87, 16, 30)),
                     LerpPosInterval(self.crate18, 8, (87, 8, 15)),
                     LerpPosInterval(self.crate18, 8, (87, 8, 30)),
                     LerpPosInterval(self.crate18, 8, (87, 8, 15)),
                     LerpPosInterval(self.crate19, 8, (87, 0, 30)),
                     LerpPosInterval(self.crate19, 8, (87, 0, 15)),
                     LerpPosInterval(self.crate19, 8, (87, 0, 30)),
                     LerpPosInterval(self.crate20, 8, (87, -8, 15)),
                     LerpPosInterval(self.crate20, 8, (87, -8, 30)),
                     LerpPosInterval(self.crate20, 8, (87, -8, 15)),
                     LerpPosInterval(self.crate21, 8, (87, -16, 15)),
                     LerpPosInterval(self.crate21, 8, (87, -16, 30)),
                     LerpPosInterval(self.crate21, 8, (87, -16, 15)),
                     LerpPosInterval(self.crate22, 8, (87, -24, 30)),
                     LerpPosInterval(self.crate22, 8, (87, -24, 15)),
                     LerpPosInterval(self.crate22, 8, (87, -24, 30)),
                     ),
        )
        self.interval.loop()
        self.birdSound = map(base.loadSfx, ['phase_4/audio/sfx/SZ_TC_bird1.ogg',
                                            'phase_4/audio/sfx/SZ_TC_bird2.ogg',
                                            'phase_4/audio/sfx/SZ_TC_bird3.ogg'])
        self.playgroundClass = TTPlayground.TTPlayground
        self.musicFile = 'phase_4/audio/bgm/TC_nbrhood.ogg'
        self.activityMusicFile = 'phase_3.5/audio/bgm/TC_SZ_activity.ogg'
        self.dnaFile = 'phase_4/dna/toontown_central_sz.pdna'
        self.safeZoneStorageDNAFile = 'phase_4/dna/storage_TT_sz.pdna'

    def load(self):
        SafeZoneLoader.SafeZoneLoader.load(self)
        bank = self.geom.find('**/*toon_landmark_TT_bank_DNARoot')
        loonylabs = self.geom.find('**/library/square_drop_shadow')
        doortrigger = bank.find('**/door_trigger*')
        doortrigger.setY(doortrigger.getY() - 1.5)
        loonylabs.find('**/building_front').setY(0.3)
        loonylabs.find('**/front_entrance_flag').setY(0.1)

        self.crate1.setPosHprScale(114, 125, 2.525, -925, 0, 0, 0.7, 1, 1)
        self.crate1.reparentTo(self.geom)
        self.crate2.setPosHprScale(109, 118, 4, -597, 0, 0, 0.7, 1, 1)
        self.crate2.reparentTo(self.geom)
        self.crate3.setPosHprScale(98, 111, 6, -607, 0, 0, 0.7, 1, 1)
        self.crate3.reparentTo(self.geom)
        self.crate4.setPosHprScale(87, 107, 8, -629, 0, 0, 0.7, 1, 1)
        self.crate4.reparentTo(self.geom)
        self.crate5.setPosHprScale(75, 107, 8, -629, 0, 0, 0.7, 1, 1)
        self.crate5.reparentTo(self.geom)
        self.crate6.setPosHprScale(64, 108, 10, -234, 0, 0, 0.7, 1, 1)
        self.crate6.reparentTo(self.geom)
        self.crate7.setPosHprScale(53, 99, 12, -193, 0, 0, 0.7, 1, 1)
        self.crate7.reparentTo(self.geom)
        self.crate8.setPosHprScale(52, 88, 14, 141, 0, 0, 0.7, 1, 1)
        self.crate8.reparentTo(self.geom)
        self.crate9.setPosHprScale(42, 76, 16, -180, 0, 0, 0.7, 1, 1)
        self.crate9.reparentTo(self.geom)
        self.crate10.setPosHprScale(41, 60, 18, -154, 0, 0, 0.7, 1, 1)
        self.crate10.reparentTo(self.geom)
        self.crate11.setPosHprScale(46, 49, 20, -166, 0, 0, 0.7, 1, 1)
        self.crate11.reparentTo(self.geom)
        self.crate12.setPosHprScale(49, 34, 22, -132, 0, 0, 0.7, 1, 1)
        self.crate12.reparentTo(self.geom)
        self.crate13.setPosHprScale(62, 28, 18, -75, 0, 0, 0.7, 1, 1)
        self.crate13.reparentTo(self.geom)
        self.crate14.setPosHprScale(70, 31, 22, -91, 0, 0, 0.7, 1, 1)
        self.crate14.reparentTo(self.geom)
        self.crate15.setPosHprScale(79, 27, 22, -91, 45, 0, 0.7, 1, 1)
        self.crate15.reparentTo(self.geom)
        self.crate16.setPosHprScale(82, 27, 20, -91, 0, 0, 0.7, 1, 1)
        self.crate16.reparentTo(self.geom)
        self.crate17.setPos(87, 16, 30)
        self.crate17.reparentTo(self.geom)
        self.crate18.setPos(87, 8, 15)
        self.crate18.reparentTo(self.geom)
        self.crate19.setPos(87, 0, 30)
        self.crate19.reparentTo(self.geom)
        self.crate20.setPos(87, -8, 15)
        self.crate20.reparentTo(self.geom)
        self.crate21.setPos(87, -16, 30)
        self.crate21.reparentTo(self.geom)
        self.crate22.setPos(87, -24, 15)
        self.crate22.reparentTo(self.geom)
        self.crate23.setPosHprScale(87, -35, 27, -90, 0, 0, 0.7, 1, 1)
        self.crate23.reparentTo(self.geom)

    def unload(self):
        SafeZoneLoader.SafeZoneLoader.unload(self)
        del self.birdSound
        del self.crate1
        del self.crate2
        del self.crate3
        del self.crate4
        del self.crate5
        del self.crate6
        del self.crate7
        del self.crate8
        del self.crate9
        del self.crate10
        del self.crate11
        del self.crate12
        del self.crate13
        del self.crate14
        del self.crate15
        del self.crate16
        del self.crate17
        del self.crate18
        del self.crate19
        del self.crate20
        del self.crate21
        del self.crate22
        del self.crate23
