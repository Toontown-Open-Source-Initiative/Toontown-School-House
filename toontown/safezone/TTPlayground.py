from panda3d.core import *
from toontown.toonbase import ToontownGlobals
import Playground
import random
from toontown.launcher import DownloadForceAcknowledge
from direct.task.Task import Task
from toontown.hood import ZoneUtil
from toontown.toon import NPCToons

class TTPlayground(Playground.Playground):

    def __init__(self, loader, parentFSM, doneEvent):
        Playground.Playground.__init__(self, loader, parentFSM, doneEvent)

    def load(self):
        Playground.Playground.load(self)
        render.setColorScale(0.5,0.5,0.5,1)
        self.bldg = loader.loadModel('phase_4/models/modules/suit_landmark_corp')
        self.bldg.reparentTo(render)
        self.bldg.setPos(150,96,2.525)
        self.bldg.setHpr(-100,0,0)

        self.shopOwnerNpc = NPCToons.createLocalNPC(2001)
        self.shopOwnerNpc.addActive()
        self.shopOwnerNpc.reparentTo(render)
        self.shopOwnerNpc.setPos(130,83,2.525)
        self.shopOwnerNpc.setHpr(-100,0,0)
        self.shopOwnerNpc.loop('bored')

        self.shopOwnerNpcc = NPCToons.createLocalNPC(20000)
        self.shopOwnerNpcc.addActive()
        self.shopOwnerNpcc.reparentTo(render)
        self.shopOwnerNpcc.setPos(130,87,2.525)
        self.shopOwnerNpcc.setHpr(-100,0,0)
        self.shopOwnerNpcc.loop('shrug')

    def unload(self):
        render.setColorScale(1,1,1,1)
        self.bldg.removeNode()
        del self.bldg
        Playground.Playground.unload(self)
        if self.shopOwnerNpc:
            self.shopOwnerNpc.removeActive()
            self.shopOwnerNpc.delete()
            self.shopOwnerNpc = None
        if  self.shopOwnerNpcc:
            self.shopOwnerNpcc.removeActive()
            self.shopOwnerNpcc.delete()
            self.shopOwnerNpcc = None

    def enter(self, requestStatus):
        Playground.Playground.enter(self, requestStatus)

    def exit(self):
        Playground.Playground.exit(self)

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
