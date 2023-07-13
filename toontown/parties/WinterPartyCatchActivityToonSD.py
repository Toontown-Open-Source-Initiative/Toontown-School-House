#-------------------------------------------------------------------------------
# Contact:
# Created: 2010
#-------------------------------------------------------------------------------

from . import PartyCatchActivityToonSD

from panda3d.core import Vec4

from direct.directnotify import DirectNotifyGlobal
from direct.interval.IntervalGlobal import Sequence, Parallel, Wait, Func
from direct.interval.IntervalGlobal import LerpColorScaleInterval
from direct.interval.IntervalGlobal import WaitInterval, ActorInterval, FunctionInterval
from direct.fsm import ClassicFSM, State


class WinterPartyCatchActivityToonSD(PartyCatchActivityToonSD.PartyCatchActivityToonSD):
    """ WinterPartyCatchActivityToonSD catching activity char anim statedata """
    notify = DirectNotifyGlobal.directNotify.newCategory("PartyCatchActivityToonSD")

    def __init__(self, avId, activity):
        WinterPartyCatchActivityToonSD.notify.debug("init : avId = %s, activity = %s " % (avId, activity))
        PartyCatchActivityToonSD.PartyCatchActivityToonSD.__init__(self, avId, activity)

    def enterEatFruit(self, fruitModel, handNode):
        """ fruit model is placed under handNode in this state;
        this function takes ownership of the fruit model """
        self.notify.debug('enterEatFruit')
        if self.isLocal:
            self.activity.orthoWalk.start()
        self.setAnimState('CatchEating', 1.0)

        self.fruitModel = fruitModel
        # make sure the scale stays the same wrt render
        renderScale = fruitModel.getScale(render)
        fruitModel.reparentTo(handNode)
        fruitModel.setScale(render, renderScale)
        fruitModel.setTransparency(1)

        duration = self.toon.getDuration('catch-eatneutral')
        self.eatIval = Sequence(
            Parallel(WaitInterval(duration),
                     # toon eats the fruit halfway through animation
                     Sequence(LerpScaleInterval(fruitModel, duration/2.,
                                                #fruitModel.getScale()*.5,
                                                #blendType='easeInOut'),
                                                Vec4(1.0, 1.0, 1.0, 0.0)))),
            Func(self.fsm.request, "normal"),
            name=self.toon.uniqueName('eatingIval')
        )
        self.eatIval.start()

    def exitEatFruit(self):
        # if we were to 'finish' the ival, we could run into trouble with
        # nested 'request' calls
        self.eatIval.pause()
        del self.eatIval

        self.fruitModel.reparentTo(hidden)
        self.fruitModel.removeNode()
        del self.fruitModel

        self.setAnimState('off', 1.)
        if self.isLocal:
            self.activity.orthoWalk.stop()
