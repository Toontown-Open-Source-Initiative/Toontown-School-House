from toontown.cogdominium.CogdoCraneGameGlobals import CranePosHprs, SpotlightStomperDamage
from direct.interval.IntervalGlobal import Sequence, Func, Wait, Parallel, SoundInterval
from direct.distributed.DistributedObject import DistributedObject
from direct.showutil.BuildGeometry import addCircleGeom
from toontown.hood.ZoneUtil import getCanonicalHoodId
from direct.directnotify import DirectNotifyGlobal
from panda3d.core import Vec4

class DistCogdoCraneObstacle(DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistCogdoCraneObstacle')

    def __init__(self, cr):
        DistributedObject.__init__(self, cr)
        self.audioMgr = base.cogdoGameAudioMgr
        self.stomperSfx = self.audioMgr.createSfx('stomperSfx')
        self.caughtSfx = self.audioMgr.createSfx('caughtSfx')
        self.cycleSfx = self.audioMgr.createSfx('cycleSfx')
        self.loadSpotlightModel()
        self.realSequence = None

    def loadSpotlightModel(self):
        self.spotlightModel = loader.loadModel('phase_5/models/cogdominium/tt_m_ara_ccg_spotlight')
        self.spotlightModel.reparentTo(hidden)
        self.spotlightModel.setScale(2, 2, 6)

        self.spotlightCircle = addCircleGeom(self.spotlightModel, 50, 3, Vec4(1.0, 1.0, 1.0, 1.0))
        self.spotlightCircle[0].setTransparency(1)
        self.spotlightCircle[0].setAlphaScale(0.50)

        self.stomperModel = loader.loadModel('phase_9/models/cogHQ/square_stomper')
        self.stomperModel.reparentTo(hidden)
        self.stomperModel.find('**/head').setP(-90)
        self.stomperModel.find('**/head').setScale(5)
        self.stomperModel.find('**/shaft').setScale(1, 12, 1)

        self.stomperShadow = loader.loadModel('phase_3/models/props/square_drop_shadow')
        self.stomperShadow.reparentTo(hidden)
        self.stomperShadow.setScale(0.6)
        self.stomperShadow.setAlphaScale(0.8)
        self.stomperShadow.setColorScale(1.0, 1.0, 1.0, 0)
        self.stomperShadow.setBin('transparent', 0)
        self.stomperShadow.setTransparency(1)
        self.accept('entercollUpFloor', self.handleToonSquished)

    def determineBasePoint(self, point):
        x, y, z, h, p, r = CranePosHprs[point]
        self.stomperModel.setPos(x, y, 100)
        self.stomperShadow.setPos(x, y, 7)
        self.stomperModel.reparentTo(render)
        self.stomperShadow.reparentTo(render)

        self.spotlightModel.setColorScale(1.0, 1.0, 1.0, 1.0)
        self.spotlightCircle[0].setColorScale(1.0, 1.0, 1.0, 0.6)

        spotlightLoop = Sequence()

        def createSpotlightModelPosHprFuncIval(index):
            return Sequence(Func(self.spotlightModel.setPosHpr, *CranePosHprs[index]))

        for i in range(8):
            time = 0.15
            if i > 4:
                time += 0.025 * i
            seq = Sequence()
            for j in range(4):
                seq.append(Parallel(SoundInterval(self.cycleSfx.getAudioSound(), node=self.spotlightModel, duration=time),
                                    createSpotlightModelPosHprFuncIval(j)))
            spotlightLoop.append(seq)

        self.realSequence = Sequence(
            Func(self.spotlightModel.reparentTo, render),
            spotlightLoop,
            Parallel(
                Func(self.spotlightModel.setPos, x, y, z),
                Func(self.spotlightCircle[0].setColorScale, Vec4(1.0, 0, 0, 0.6)),
                self.spotlightCircle[0].scaleInterval(0.2, (1.2, 1.2, 1.2)),
                self.spotlightCircle[0].scaleInterval(0.2, (1.0, 1.0, 1.0)),
                Func(self.caughtSfx.play, source=self.spotlightModel),
            ),
            Wait(1.0),
            Parallel(
                self.spotlightCircle[0].colorScaleInterval(1.0, Vec4(1.0, 1.0, 1.0, 0.0)),
                self.spotlightModel.colorScaleInterval(1.0, Vec4(1.0, 1.0, 1.0, 0.0)),
            ),
            Parallel(
                self.stomperShadow.colorScaleInterval(0.2, Vec4(1.0, 1.0, 1.0, 1.0)),
                self.stomperModel.posInterval(0.2, (x, y, z)),
                Func(self.stomperSfx.play, source=self.stomperShadow),
                self.stomperShadow.scaleInterval(0.2, (2.0, 2.0, 2.0)),
            ),
            Parallel(
                self.stomperModel.posInterval(3.0, (x, y, 100)),
                self.stomperShadow.colorInterval(3.0, (1.0, 1.0, 1.0, 0.0)),
                self.stomperShadow.scaleInterval(3.0, (0.6, 0.6, 0.6)),
            )
        )
        self.realSequence.start()

    def handleToonSquished(self, entry):
        base.localAvatar.b_squish(SpotlightStomperDamage[getCanonicalHoodId(base.localAvatar.getZoneId())])
        self.sendUpdate('requestFreeCrane', [])

    def delete(self):
        self.ignore('entercollUpFloor')
        self.spotlightModel.removeNode()
        del self.spotlightModel
        self.spotlightCircle[0].removeNode()
        del self.spotlightCircle
        self.stomperModel.removeNode()
        del self.stomperModel
        self.stomperShadow.removeNode()
        del self.stomperShadow
        if self.realSequence:
            self.realSequence.finish()