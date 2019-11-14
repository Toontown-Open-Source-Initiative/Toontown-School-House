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
        self.bottle = loader.loadModel ('phase_3.5/models/props/bottle')
        self.bottle.reparentTo (render)
        self.bottle.setPos (-72,  -80,  0.525)

        self.bottle.setHpr (2,  0,  60)
        self.bottle = loader.loadModel ('phase_3.5/models/props/bottle')
        self.bottle.reparentTo (render)
        self.bottle.setPos (-72,  -79,  0.5)

        self.bottle.setHpr (2,  0,  60)
        self.bottle = loader.loadModel ('phase_3.5/models/props/bottle')
        self.bottle.reparentTo (render)
        self.bottle.setPos (-72,  -78,  0.5)

        self.bottle.setHpr (2,  20,  60)
        self.bottle = loader.loadModel ('phase_3.5/models/props/bottle')
        self.bottle.reparentTo (render)
        self.bottle.setPos (-75,  -77,  0.5)

        self.bottle.setHpr (2,  0,  60)
        self.bottle = loader.loadModel ('phase_3.5/models/props/bottle')
        self.bottle.reparentTo (render)
        self.bottle.setPos (-74,  -77,  0.5)

        self.bottle.setHpr (2,  0,  60)
        self.bottle = loader.loadModel ('phase_3.5/models/props/bottle')
        self.bottle.reparentTo (render)
        self.bottle.setPos (-73,  -77,  0.5)

        self.bottle.setHpr (2,  0,  60)

        self.button = loader.loadModel ('phase_3.5/models/props/button')
        self.button.reparentTo (render)
        self.button.setPos (-74.2389,  -87.5,  0.525)

        self.button.setHpr (20,  20,  20)

        self.ship = loader.loadModel ("phase_5/models/props/ship")
        self.ship.reparentTo (render)
        self.ship.setPos (-44,  -82,  0.52)

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
