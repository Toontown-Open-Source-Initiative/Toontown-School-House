from panda3d.core import *
from toontown.toonbase import ToontownGlobals
import Playground
import random
from toontown.launcher import DownloadForceAcknowledge
from direct.task.Task import Task
from toontown.hood import ZoneUtil

class TTPlayground(Playground.Playground):

    def __init__(self, loader, parentFSM, doneEvent):
        Playground.Playground.__init__(self, loader, parentFSM, doneEvent)

    def load(self):
        Playground.Playground.load(self)
        self.foodkart = loader.loadModel("phase_6/models/golf/golf_cart3")
        self.foodkart.reparentTo(render)
        self.foodkart.setPosHpr(-93.961, -88.638, 10.525, 0, 0, 45)

        self.cupcake1 = loader.loadModel("phase_6/models/golf/picnic_cupcake")
        self.cupcake1.reparentTo(render)
        self.cupcake1.setPosHpr(-87.961, -80.638, 9.525, 0, 0, 45)
        self.cupcake1.setScale(5)
        self.cupcake2 = loader.loadModel("phase_6/models/golf/picnic_cupcake")
        self.cupcake2.reparentTo(render)
        self.cupcake2.setPosHpr(-92.961, -80.638, 10.250, 0, 0, 135)
        self.cupcake2.setScale(5)
        self.cupcake3 = loader.loadModel("phase_6/models/golf/picnic_cupcake")
        self.cupcake3.reparentTo(render)
        self.cupcake3.setPosHpr(-93, -77, 1.850, 0, 0, 165)
        self.cupcake3.setScale(5)

        self.choccake = loader.loadModel("phase_6/models/golf/picnic_chocolate_cake")
        self.choccake.reparentTo(render)
        self.choccake.setPosHpr(-73.374, -76.127, 2, 0, 0, 180)
        self.choccake.setScale(5)

        self.sandwich1 = loader.loadModel("phase_6/models/golf/picnic_sandwich")
        self.sandwich1.reparentTo(render)
        self.sandwich1.setPos(-88, -79.266, 0.650)
        self.sandwich1.setScale(5)
        self.sandwich2 = loader.loadModel("phase_6/models/golf/picnic_sandwich")
        self.sandwich2.reparentTo(render)
        self.sandwich2.setPos(-85.513, -79.266, 0.650)
        self.sandwich2.setScale(5)
        self.sandwich3 = loader.loadModel("phase_6/models/golf/picnic_sandwich")
        self.sandwich3.reparentTo(render)
        self.sandwich3.setPos(-86.756, -79.266, 1.225)
        self.sandwich3.setScale(5)

        self.basket = loader.loadModel("phase_6/models/golf/picnic_basket")
        self.basket.reparentTo(render)
        self.basket.setPosHpr(-73.400, -82.848, 3.525, 0, 0, 145)
        self.basket.setScale(5)


    def unload(self):
        Playground.Playground.unload(self)

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
