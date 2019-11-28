from panda3d.core import Point3, PlaneNode
from direct.showbase.ShowBase import Plane
from direct.showbase.RandomNumGen import RandomNumGen
from direct.interval.MetaInterval import Sequence, Parallel
from direct.interval.FunctionInterval import Func, Wait
from toontown.toonbase import TTLocalizer
from toontown.toon import Toon, ToonHead, ToonDNA
from toontown.suit import Suit, SuitDNA
import CogdoCraneGameConsts as GameConsts
from CogdoUtil import CogdoGameMovie
import CogdoUtil

class CogdoCraneGameIntro(CogdoGameMovie):

    def __init__(self, rng):
        CogdoGameMovie.__init__(self)
        self._rng = RandomNumGen(rng)

    def _getRandomLine(self, lineList):
        return CogdoUtil.getRandomDialogueLine(lineList, self._rng)

    def displayLine(self, who, text):
        self._dialogueLabel.node().setText(text)
        self._dialogueLabel.setPos(0.32, 0, -0.724)
        if who == 'toon':
            self.toonHead.reparentTo(aspect2d)
            self.cogHead.reparentTo(hidden)
            self._toonDialogueSfx.play()
            self.toonHead.setClipPlane(self.clipPlane)
        else:
            self.toonHead.reparentTo(hidden)
            self.cogHead.reparentTo(aspect2d)
            self._cogDialogueSfx.play()
            self.cogHead.setClipPlane(self.clipPlane)

    def makeSuit(self, suitType):
        suit = Suit.Suit()
        dna = SuitDNA.SuitDNA()
        dna.newSuit(suitType)
        suit.setStyle(dna)
        suit.isDisguised = 1
        suit.generateSuit()
        suit.setScale(1, 1, 2)
        suit.setPos(0, 0, -4.4)
        suit.reparentTo(self.toonHead)
        for part in suit.getHeadParts():
            part.hide()

    def load(self):
        CogdoGameMovie.load(self)
        self.toonDNA = ToonDNA.ToonDNA()
        self.toonDNA.newToonFromProperties('dss', 'ss', 'm', 'm', 2, 0, 2, 2, 1, 8, 1, 8, 1, 14)
        self.toonHead = Toon.Toon()
        self.toonHead.setDNA(self.toonDNA)
        self.makeSuit('sc')
        self.toonHead.getGeomNode().setDepthWrite(1)
        self.toonHead.getGeomNode().setDepthTest(1)
        self.toonHead.loop('neutral')
        self.toonHead.setPosHprScale(-0.73, 0, -1.27, 180, 0, 0, 0.18, 0.18, 0.18)
        self.toonHead.reparentTo(hidden)
        self.toonHead.startBlink()
        self.cogHead = Suit.Suit()
        self.cogDNA = SuitDNA.SuitDNA()
        self.cogDNA.newSuit('mb')
        self.cogHead.setDNA(self.cogDNA)
        self.cogHead.getGeomNode().setDepthWrite(1)
        self.cogHead.getGeomNode().setDepthTest(1)
        self.cogHead.loop('neutral')
        self.cogHead.setPosHprScale(-0.74, 0, -1.49, 180, 0, 0, 0.12, 0.14, 0.14)
        self.cogHead.reparentTo(hidden)
        self.clipPlane = self.toonHead.attachNewNode(PlaneNode('clip'))
        self.clipPlane.node().setPlane(Plane(0, 0, 1, 0))
        self.clipPlane.setPos(0, 0, 2.45)
        audioMgr = base.cogdoGameAudioMgr
        self._cogDialogueSfx = audioMgr.createSfx('cogDialogue')
        self._toonDialogueSfx = audioMgr.createSfx('toonDialogue')

        def start():
            camera.wrtReparentTo(render)
            self._startUpdateTask()

        def end():
            self._stopUpdateTask()

        introDuration = GameConsts.IntroDurationSeconds
        dialogue = TTLocalizer.CogdoCraneIntroMovieDialogue
        waitDur = introDuration / len(dialogue)
        flyDur = introDuration - waitDur * 0.5
        cameraIval = Parallel()
        self._ival = Sequence(Func(start), Parallel(cameraIval,
                                                    Sequence(Func(self.displayLine, 'cog',
                                                                  self._getRandomLine(dialogue[0])),
                                                             Wait(waitDur), Func(self.displayLine, 'toon',
                                                                                 self._getRandomLine(dialogue[1])),
                                                             Wait(waitDur), Func(self.displayLine, 'cog',
                                                                                 self._getRandomLine(dialogue[2])),
                                                             Wait(waitDur))),
                              Func(end))

    def _updateTask(self, task):
        dt = globalClock.getDt()
        return task.cont

    def unload(self):
        CogdoGameMovie.unload(self)
        del self._cogDialogueSfx
        del self._toonDialogueSfx
        self.toonHead.stopBlink()
        self.toonHead.stop()
        self.toonHead.removeNode()
        self.toonHead.delete()
        del self.toonHead
        self.cogHead.stop()
        self.cogHead.removeNode()
        self.cogHead.delete()
        del self.cogHead
        self._exit = None
        return


class CogdoCraneGameFinish(CogdoGameMovie):

    def __init__(self, players):
        CogdoGameMovie.__init__(self)
        self._players = players

    def load(self):
        CogdoGameMovie.load(self)

        exitDur = 1.0
        showExitIval = Sequence(Func(camera.wrtReparentTo, render), camera.hprInterval(exitDur, Point3(0, -45, 0), blendType='easeInOut'))

        self._ival = Sequence(showExitIval, Wait(GameConsts.FinishDurationSeconds - exitDur - 1.0), Func(base.transitions.irisOut), Wait(1.0))

    def unload(self):
        CogdoGameMovie.unload(self)
