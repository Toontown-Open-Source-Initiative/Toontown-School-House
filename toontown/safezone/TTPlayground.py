from panda3d.core import *
from toontown.toonbase import ToontownGlobals
import Playground
import random
from toontown.launcher import DownloadForceAcknowledge
from direct.task.Task import Task
from toontown.hood import ZoneUtil
from direct.interval.IntervalGlobal import *

class TTPlayground(Playground.Playground):

    def __init__(self, loader, parentFSM, doneEvent):
        Playground.Playground.__init__(self, loader, parentFSM, doneEvent)
        self.interval = None

    def load(self):
        Playground.Playground.load(self)
        self.foodkart = loader.loadModel("phase_6/models/golf/golf_cart3")
        self.foodkart.reparentTo(render)
        self.foodkart.setPos(0, 0, 50)

        propNode = self.foodkart.attachNewNode('prop')
        propNode.hide()

        self.cupcake1 = loader.loadModel("phase_6/models/golf/picnic_cupcake")
        self.cupcake1.reparentTo(propNode)
        self.cupcake1.setScale(5)
        self.cupcake2 = loader.loadModel("phase_6/models/golf/picnic_cupcake")
        self.cupcake2.reparentTo(propNode)
        self.cupcake2.setScale(5)
        self.cupcake3 = loader.loadModel("phase_6/models/golf/picnic_cupcake")
        self.cupcake3.reparentTo(propNode)
        self.cupcake3.setScale(5)

        self.choccake = loader.loadModel("phase_6/models/golf/picnic_chocolate_cake")
        self.choccake.reparentTo(propNode)
        self.choccake.setScale(5)

        self.sandwich1 = loader.loadModel("phase_6/models/golf/picnic_sandwich")
        self.sandwich1.reparentTo(propNode)
        self.sandwich1.setScale(5)
        self.sandwich2 = loader.loadModel("phase_6/models/golf/picnic_sandwich")
        self.sandwich2.reparentTo(propNode)
        self.sandwich2.setScale(5)
        self.sandwich3 = loader.loadModel("phase_6/models/golf/picnic_sandwich")
        self.sandwich3.reparentTo(propNode)
        self.sandwich3.setScale(5)

        self.basket = loader.loadModel("phase_6/models/golf/picnic_basket")
        self.basket.reparentTo(propNode)
        self.basket.setScale(5)

        self.interval = Sequence(
            LerpPosInterval(self.foodkart, 3.5, (-93.961, -88.638, 10.525)),
            Func(propNode.show),
            Func(self.cupcake1.wrtReparentTo, render),
            Func(self.cupcake2.wrtReparentTo, render),
            Func(self.cupcake3.wrtReparentTo, render),
            Func(self.choccake.wrtReparentTo, render),
            Func(self.sandwich1.wrtReparentTo, render),
            Func(self.sandwich2.wrtReparentTo, render),
            Func(self.sandwich3.wrtReparentTo, render),
            Func(self.basket.wrtReparentTo, render),
            Parallel(
                LerpPosHprInterval(self.cupcake1, 1.0, (-87.961, -80.638, 9.525), (0, 0, 45)),
                LerpPosHprInterval(self.cupcake2, 1.0, (-92.961, -80.638, 10.250), (0, 0, 135)),
                LerpPosHprInterval(self.cupcake3, 1.0, (-93, -77, 1.850), (0, 0, 165)),
                LerpPosHprInterval(self.choccake, 1.0, (-73.374, -76.127, 2), (0, 0, 180)),
                LerpPosInterval(self.sandwich1, 1.0, (-88, -79.266, 0.650)),
                LerpPosInterval(self.sandwich2, 1.0, (-85.513, -79.266, 0.650)),
                LerpPosInterval(self.sandwich3, 1.0, (-86.756, -79.266, 1.225)),
                LerpPosHprInterval(self.basket, 1.0, (-73.400, -82.848, 3.525), (0, 0, 145))
            ),
            Wait(5.0),
            Func(self.foodkart.setPos, 0, 0, 200),
            Func(propNode.hide),
            Func(self.cupcake1.reparentTo, propNode),
            Func(self.cupcake2.reparentTo, propNode),
            Func(self.cupcake3.reparentTo, propNode),
            Func(self.choccake.reparentTo, propNode),
            Func(self.sandwich1.reparentTo, propNode),
            Func(self.sandwich2.reparentTo, propNode),
            Func(self.sandwich3.reparentTo, propNode),
            Func(self.basket.reparentTo, propNode),
            Func(self.cupcake1.setPos, 0, 0, 0),
            Func(self.cupcake2.setPos, 0, 0, 0),
            Func(self.cupcake3.setPos, 0, 0, 0),
            Func(self.choccake.setPos, 0, 0, 0),
            Func(self.sandwich1.setPos, 0, 0, 0),
            Func(self.sandwich2.setPos, 0, 0, 0),
            Func(self.sandwich3.setPos, 0, 0, 0),
            Func(self.basket.setPos, 0, 0, 0),
        )
        self.interval.loop()

        self.stuffHidden = False
        self.accept('h', self.hideStuff)

    def hideStuff(self):
        self.stuffHidden = not self.stuffHidden

        if self.stuffHidden:
            self.foodkart.hide()
            self.cupcake1.hide()
            self.cupcake2.hide()
            self.cupcake3.hide()
            self.sandwich1.hide()
            self.sandwich2.hide()
            self.sandwich3.hide()
            self.choccake.hide()
            self.basket.hide()
        else:
            self.foodkart.show()
            self.cupcake1.show()
            self.cupcake2.show()
            self.cupcake3.show()
            self.sandwich1.show()
            self.sandwich2.show()
            self.sandwich3.show()
            self.choccake.show()
            self.basket.show()

    def unload(self):
        Playground.Playground.unload(self)

        if self.interval:
            self.interval.finish()
            del self.interval

    def enter(self, requestStatus):
        Playground.Playground.enter(self, requestStatus)
        taskMgr.doMethodLater(1, self.__birds, 'TT-birds')

    def exit(self):
        Playground.Playground.exit(self)
        taskMgr.remove('TT-birds')

    def __birds(self, task):
        base.playSfx(random.choice(self.loader.birdSound))
        t = random.random() * 20.0 + 1
        taskMgr.doMethodLater(t, self.__birds, 'TT-birds')
        return Task.done

    def doRequestLeave(self, requestStatus):
        self.fsm.request('trialerFA', [requestStatus])

    def enterDFA(self, requestStatus):
        doneEvent = 'dfaDoneEvent'
        self.accept(doneEvent, self.enterDFACallback, [requestStatus])
        self.dfa = DownloadForceAcknowledge.DownloadForceAcknowledge(doneEvent)
        hood = ZoneUtil.getCanonicalZoneId(requestStatus['hoodId'])
        if hood == ToontownGlobals.MyEstate:
            self.dfa.enter(base.cr.hoodMgr.getPhaseFromHood(ToontownGlobals.MyEstate))
        elif hood == ToontownGlobals.GoofySpeedway:
            self.dfa.enter(base.cr.hoodMgr.getPhaseFromHood(ToontownGlobals.GoofySpeedway))
        elif hood == ToontownGlobals.PartyHood:
            self.dfa.enter(base.cr.hoodMgr.getPhaseFromHood(ToontownGlobals.PartyHood))
        else:
            self.dfa.enter(5)

    def showPaths(self):
        from toontown.classicchars import CCharPaths
        from toontown.toonbase import TTLocalizer
        self.showPathPoints(CCharPaths.getPaths(TTLocalizer.Mickey))
