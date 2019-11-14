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
        
        self.houseB     = loader.loadModel("phase_5.5/models/estate/houseB")
        self.houseB.reparentTo(render)
        self.houseB.setPos(138, 80, 2.5)
        self.houseB.setHpr(180, 0, 0)
        
        self.houseBDoor = loader.loadModel("phase_3.5/models/modules/doors_practical.bam").find("**/door_double_round_ur")
        self.houseBDoor.reparentTo(self.houseB.find("**/door_origin"))
        self.houseBDoor.setHpr(90, 0, 0)
        self.houseBDoor.setScale(0.8)
        self.houseBDoor.setColorScale(0.88, 0.45, 0.38, 1)
        
        # prop "HouseBGroup_DNARoot" [
        #  code [ "HouseBGroup" ]
        #  pos [ 138 80 2.5 ]
        #  nhpr [ 180 0 0 ]
        #  door [
        #   code [ "door_double_round_ur" ]
        #   color [ 0.88 0.45 0.38 1 ]
        #  ]
        # ]
        
        # place_model "phase_5.5/models/estate/houseB" [
	    #     store_node [ "prop" "HouseBGroup" ]

    def unload(self):
        Playground.Playground.unload(self)
        
        self.houseB.removeNode()
        self.houseBDoor.removeNode()
        del self.houseB
        del self.houseBDoor

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
