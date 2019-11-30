from direct.interval.IntervalGlobal import *
from direct.task.TaskManagerGlobal import *
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import TTLocalizer
import DistributedBossCog
from direct.task.Task import Task
import DistributedCashbotBossGoon
import DistributedCashbotBossHardmodeGoon
import GoonGlobals
import SuitDNA
from toontown.toon import Toon
from toontown.toon import ToonDNA
from direct.fsm import FSM
from toontown.toonbase import ToontownGlobals
from otp.otpbase import OTPGlobals
from toontown.building import ElevatorUtils
from toontown.building import ElevatorConstants
from toontown.battle import MovieToonVictory
from toontown.battle import RewardPanel
from toontown.distributed import DelayDelete
from toontown.chat import ResistanceChat
from toontown.coghq import CogDisguiseGlobals
from panda3d.core import *
from panda3d.physics import *
from panda3d.direct import *
from libotp import *
import random
import math
OneBossCog = None
TTL = TTLocalizer

class DistributedCashbotBossHardmode(DistributedBossCog.DistributedBossCog, FSM.FSM):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedCashbotBossHardmode')
    numFakeGoons = 3
    numCogGoons = 2

    def __init__(self, cr):
        DistributedBossCog.DistributedBossCog.__init__(self, cr)
        FSM.FSM.__init__(self, 'DistributedCashbotBossHardmode')
        self.resistanceToon = None
        self.resistanceToonOnstage = 0
        self.resistanceToonTwo = None
        self.resistanceToonTwoOnstage = 0
        self.cranes = {}
        self.safes = {}
        self.goons = []
        self.bossMaxDamage = ToontownGlobals.CashbotBossHardmodeMaxDamage
        self.elevatorType = ElevatorConstants.ELEVATOR_CFO
        base.boss = self
        return

    def announceGenerate(self):
        DistributedBossCog.DistributedBossCog.announceGenerate(self)
        self.setName(TTLocalizer.CashbotBossName)
        nameInfo = TTLocalizer.BossCogHardmodeNameWithDept % {'name': self._name,
         'dept': SuitDNA.getDeptFullname(self.style.dept),
         'mark': TTLocalizer.BossCogHardmodePostFix}
        self.setDisplayName(nameInfo)
        target = CollisionSphere(2, 0, 0, 3)
        targetNode = CollisionNode('headTarget')
        targetNode.addSolid(target)
        targetNode.setCollideMask(ToontownGlobals.PieBitmask)
        self.headTarget = self.neck.attachNewNode(targetNode)
        shield = CollisionSphere(0, 0, 0.8, 7)
        shieldNode = CollisionNode('shield')
        shieldNode.addSolid(shield)
        shieldNode.setCollideMask(ToontownGlobals.PieBitmask)
        shieldNodePath = self.pelvis.attachNewNode(shieldNode)
        self.heldObject = None
        self.bossDamage = 0
        self.loadEnvironment()
        self.__makeResistanceToon()
        self.__makeResistanceToonTwo()
        self.physicsMgr = PhysicsManager()
        integrator = LinearEulerIntegrator()
        self.physicsMgr.attachLinearIntegrator(integrator)
        fn = ForceNode('gravity')
        self.fnp = self.geom.attachNewNode(fn)
        gravity = LinearVectorForce(0, 0, -32)
        fn.addForce(gravity)
        self.physicsMgr.addLinearForce(gravity)
        localAvatar.chatMgr.chatInputSpeedChat.addCAOMenu()
        global OneBossCog
        if OneBossCog != None:
            self.notify.warning('Multiple BossCogs visible.')
        OneBossCog = self
        return

    def disable(self):
        global OneBossCog
        DistributedBossCog.DistributedBossCog.disable(self)
        self.demand('Off')
        self.unloadEnvironment()
        self.__cleanupResistanceToon()
        self.fnp.removeNode()
        self.physicsMgr.clearLinearForces()
        self.battleThreeMusic.stop()
        self.epilogueMusic.stop()
        localAvatar.chatMgr.chatInputSpeedChat.removeCAOMenu()
        if OneBossCog == self:
            OneBossCog = None
        return

    def __makeResistanceToon(self):
        if self.resistanceToon:
            return
        npc = Toon.Toon()
        npc.setName(TTLocalizer.ResistanceToonName)
        npc.setPickable(0)
        npc.setPlayerType(NametagGroup.CCNonPlayer)
        dna = ToonDNA.ToonDNA()
        dna.newToonRandom(11237, 'f', 1)
        dna.head = 'pls'
        npc.setDNAString(dna.makeNetString())
        npc.animFSM.request('neutral')
        self.resistanceToon = npc
        self.resistanceToon.setPosHpr(*ToontownGlobals.CashbotRTBattleOneStartPosHpr)
        state = random.getstate()
        random.seed(self.doId)
        self.resistanceToon.suitType = SuitDNA.getRandomSuitByDept('m')
        random.setstate(state)
        self.fakeGoons = []
        self.cogGoons = []
        for i in xrange(self.numFakeGoons):
            goon = DistributedCashbotBossGoon.DistributedCashbotBossGoon(base.cr)
            goon.doId = -1 - i
            goon.setBossCogId(self.doId)
            goon.generate()
            goon.announceGenerate()
            goon.hat.setColorScale(GoonGlobals.PG_COLORS[0])
            goon.setScale(2)
            goon.setAttackRadius(7)
            goon.setHFov(90)
            goon.scaleRadar()
            self.fakeGoons.append(goon)
        for i in xrange(self.numCogGoons):
            goon = DistributedCashbotBossGoon.DistributedCashbotBossGoon(base.cr)
            goon.doId = -10 - i
            goon.setBossCogId(self.doId)
            goon.generate()
            goon.announceGenerate()
            goon.hat.setColorScale(GoonGlobals.PG_COLORS[0])
            goon.setScale(3.5)
            goon.setAttackRadius(7)
            goon.setHFov(90)
            goon.scaleRadar()
            self.cogGoons.append(goon)

        self.__hideFakeGoons()
        self.__hideCogGoons()

    def __cleanupResistanceToon(self):
        self.__hideResistanceToon()
        if self.resistanceToon:
            self.resistanceToon.removeActive()
            self.resistanceToon.delete()
            self.resistanceToon = None
            for i in xrange(self.numFakeGoons):
                self.fakeGoons[i].disable()
                self.fakeGoons[i].delete()
                self.fakeGoons[i] = None
            for i in xrange(self.numCogGoons):
                self.cogGoons[i].disable()
                self.cogGoons[i].delete()
                self.cogGoons[i] = None

        return

    def __showResistanceToon(self, withSuit):
        if not self.resistanceToonOnstage:
            self.resistanceToon.addActive()
            self.resistanceToon.reparentTo(self.geom)
            self.resistanceToonOnstage = 1
        if withSuit:
            suit = self.resistanceToon.suitType
            self.resistanceToon.putOnSuit(suit, False)
        else:
            self.resistanceToon.takeOffSuit()

    def __hideResistanceToon(self):
        if self.resistanceToonOnstage:
            self.resistanceToon.removeActive()
            self.resistanceToon.detachNode()
            self.resistanceToonOnstage = 0

    def __makeResistanceToonTwo(self):
        if self.resistanceToonTwo:
            return
        npc = Toon.Toon()
        npc.setName(TTLocalizer.ResistanceToonTwoName)
        npc.setPickable(0)
        npc.setPlayerType(NametagGroup.CCNonPlayer)
        dna = ToonDNA.ToonDNA()
        dna.newToonFromProperties('dss', 'ss', 'm', 'm', 2, 0, 2, 2, 1, 8, 1, 8, 1, 14)
        npc.setDNAString(dna.makeNetString())
        npc.animFSM.request('neutral')
        self.resistanceToonTwo = npc
        self.resistanceToonTwo.setPosHpr(*ToontownGlobals.CashbotRTTwoBattleTwoStartPosHpr)

    def __cleanupResistanceToonTwo(self):
        self.__hideResistanceToonTwo()
        if self.resistanceToonTwo:
            self.resistanceToonTwo.removeActive()
            self.resistanceToonTwo.delete()
            self.resistanceToonTwo = None
        return

    def __showResistanceToonTwo(self):
        if not self.resistanceToonTwoOnstage:
            self.resistanceToonTwo.addActive()
            self.resistanceToonTwo.reparentTo(self.geom)
            self.resistanceToonTwoOnstage = 1

    def __hideResistanceToonTwo(self):
        if self.resistanceToonTwoOnstage:
            self.resistanceToonTwo.removeActive()
            self.resistanceToonTwo.detachNode()
            self.resistanceToonTwoOnstage = 0

    def __hideFakeGoons(self):
        if self.fakeGoons:
            for goon in self.fakeGoons:
                goon.request('Off')

    def __showFakeGoons(self, state):
        print self.fakeGoons
        if self.fakeGoons:
            for goon in self.fakeGoons:
                goon.request(state)

    def __hideCogGoons(self):
        if self.cogGoons:
            for goon in self.cogGoons:
                goon.request('Off')

    def __showCogGoons(self, state):
        print self.cogGoons
        if self.cogGoons:
            for goon in self.cogGoons:
                goon.request(state)

    def loadEnvironment(self):
        DistributedBossCog.DistributedBossCog.loadEnvironment(self)
        self.midVault = loader.loadModel('phase_10/models/cogHQ/MidVault.bam')
        self.endVault = loader.loadModel('phase_10/models/cogHQ/EndVault.bam')
        self.lightning = loader.loadModel('phase_10/models/cogHQ/CBLightning.bam')
        self.magnet = loader.loadModel('phase_10/models/cogHQ/CBMagnet.bam')
        self.craneArm = loader.loadModel('phase_10/models/cogHQ/CBCraneArm.bam')
        self.controls = loader.loadModel('phase_10/models/cogHQ/CBCraneControls.bam')
        self.stick = loader.loadModel('phase_10/models/cogHQ/CBCraneStick.bam')
        self.safe = loader.loadModel('phase_10/models/cogHQ/CBSafe.bam')
        self.eyes = loader.loadModel('phase_10/models/cogHQ/CashBotBossEyes.bam')
        self.cableTex = self.craneArm.findTexture('MagnetControl')
        self.eyes.setPosHprScale(4.5, 0, -2.5, 90, 90, 0, 0.4, 0.4, 0.4)
        self.eyes.reparentTo(self.neck)
        self.eyes.hide()
        self.midVault.setPos(0, -222, -70.7)
        self.endVault.setPos(84, -201, -6)
        self.geom = NodePath('geom')
        self.midVault.reparentTo(self.geom)
        self.endVault.reparentTo(self.geom)
        self.endVault.findAllMatches('**/MagnetArms').detach()
        self.endVault.findAllMatches('**/Safes').detach()
        self.endVault.findAllMatches('**/MagnetControlsAll').detach()
        cn = self.endVault.find('**/wallsCollision').node()
        cn.setIntoCollideMask(OTPGlobals.WallBitmask | ToontownGlobals.PieBitmask | BitMask32.lowerOn(3) << 21)
        self.door1 = self.midVault.find('**/SlidingDoor1/')
        self.door2 = self.midVault.find('**/SlidingDoor/')
        self.door3 = self.endVault.find('**/SlidingDoor/')
        elevatorModel = loader.loadModel('phase_10/models/cogHQ/CFOElevator')
        elevatorOrigin = self.midVault.find('**/elevator_origin')
        elevatorOrigin.setScale(1)
        elevatorModel.reparentTo(elevatorOrigin)
        leftDoor = elevatorModel.find('**/left_door')
        leftDoor.setName('left-door')
        rightDoor = elevatorModel.find('**/right_door')
        rightDoor.setName('right-door')
        self.setupElevator(elevatorOrigin)
        ElevatorUtils.closeDoors(leftDoor, rightDoor, ElevatorConstants.ELEVATOR_CFO)
        walls = self.endVault.find('**/RollUpFrameCillison')
        walls.detachNode()
        self.evWalls = self.replaceCollisionPolysWithPlanes(walls)
        self.evWalls.reparentTo(self.endVault)
        self.evWalls.stash()
        floor = self.endVault.find('**/EndVaultFloorCollision')
        floor.detachNode()
        self.evFloor = self.replaceCollisionPolysWithPlanes(floor)
        self.evFloor.reparentTo(self.endVault)
        self.evFloor.setName('floor')
        plane = CollisionPlane(Plane(Vec3(0, 0, 1), Point3(0, 0, -50)))
        planeNode = CollisionNode('dropPlane')
        planeNode.addSolid(plane)
        planeNode.setCollideMask(ToontownGlobals.PieBitmask)
        self.geom.attachNewNode(planeNode)
        self.geom.reparentTo(render)

    def unloadEnvironment(self):
        DistributedBossCog.DistributedBossCog.unloadEnvironment(self)
        self.geom.removeNode()

    def replaceCollisionPolysWithPlanes(self, model):
        newCollisionNode = CollisionNode('collisions')
        newCollideMask = BitMask32(0)
        planes = []
        collList = model.findAllMatches('**/+CollisionNode')
        if not collList:
            collList = [model]
        for cnp in collList:
            cn = cnp.node()
            if not isinstance(cn, CollisionNode):
                self.notify.warning('Not a collision node: %s' % repr(cnp))
                break
            newCollideMask = newCollideMask | cn.getIntoCollideMask()
            for i in xrange(cn.getNumSolids()):
                solid = cn.getSolid(i)
                if isinstance(solid, CollisionPolygon):
                    plane = Plane(solid.getPlane())
                    planes.append(plane)
                else:
                    self.notify.warning('Unexpected collision solid: %s' % repr(solid))
                    newCollisionNode.addSolid(plane)

        newCollisionNode.setIntoCollideMask(newCollideMask)
        threshold = 0.1
        planes.sort(lambda p1, p2: p1.compareTo(p2, threshold))
        lastPlane = None
        for plane in planes:
            if lastPlane == None or plane.compareTo(lastPlane, threshold) != 0:
                cp = CollisionPlane(plane)
                newCollisionNode.addSolid(cp)
                lastPlane = plane

        return NodePath(newCollisionNode)

    def __makeGoonMovieForIntro(self):
        goonTrack = Parallel()
        goon = self.fakeGoons[0]
        goonTrack.append(Sequence(
            goon.posHprInterval(0, Point3(111, -287, 0), VBase3(165, 0, 0)),
            goon.posHprInterval(9, Point3(101, -323, 0), VBase3(165, 0, 0)),
            goon.hprInterval(1, VBase3(345, 0, 0)),
            goon.posHprInterval(9, Point3(111, -287, 0), VBase3(345, 0, 0)),
            goon.hprInterval(1, VBase3(165, 0, 0)),
            goon.posHprInterval(9.5, Point3(104, -316, 0), VBase3(165, 0, 0))))
        goon = self.fakeGoons[1]
        goonTrack.append(Sequence(
            goon.posHprInterval(0, Point3(119, -315, 0), VBase3(357, 0, 0)),
            goon.posHprInterval(9, Point3(121, -280, 0), VBase3(357, 0, 0)),
            goon.hprInterval(1, VBase3(177, 0, 0)),
            goon.posHprInterval(9, Point3(119, -315, 0), VBase3(177, 0, 0)),
            goon.hprInterval(1, VBase3(357, 0, 0)),
            goon.posHprInterval(9, Point3(121, -280, 0), VBase3(357, 0, 0))))
        goon = self.fakeGoons[2]
        goonTrack.append(Sequence(
            goon.posHprInterval(0, Point3(102, -320, 0), VBase3(231, 0, 0)),
            goon.posHprInterval(9, Point3(127, -337, 0), VBase3(231, 0, 0)),
            goon.hprInterval(1, VBase3(51, 0, 0)),
            goon.posHprInterval(9, Point3(102, -320, 0), VBase3(51, 0, 0)),
            goon.hprInterval(1, VBase3(231, 0, 0)),
            goon.posHprInterval(9, Point3(127, -337, 0), VBase3(231, 0, 0))))
        return Sequence(Func(self.__showFakeGoons, 'Walk'), goonTrack, Func(self.__hideFakeGoons))

    def __makeCogGoonMovieForIntro(self):
        goonTrack = Parallel()
        goon = self.cogGoons[0]
        goonTrack.append(Sequence(
            goon.posHprInterval(0, Point3(ToontownGlobals.CashbotBossHardmodeCogGoonOffstagePosHpr[0], ToontownGlobals.CashbotBossHardmodeCogGoonOffstagePosHpr[1], ToontownGlobals.CashbotBossHardmodeCogGoonOffstagePosHpr[2]), VBase3(180, 0, 0)),
            goon.posHprInterval(8, Point3(ToontownGlobals.CashbotBossHardmodeCogGoonOffstage2PosHpr[0], ToontownGlobals.CashbotBossHardmodeCogGoonOffstage2PosHpr[1], ToontownGlobals.CashbotBossHardmodeCogGoonOffstage2PosHpr[2]), VBase3(180, 0, 0))
        ))

        return Sequence(Func(self.__showCogGoons, 'Walk'), goonTrack, Func(self.__hideCogGoons))

    def makeIntroductionMovie(self, delayDeletes):
        for toonId in self.involvedToons:
            toon = self.cr.doId2do.get(toonId)
            if toon:
                delayDeletes.append(DelayDelete.DelayDelete(toon, 'CashbotBoss.makeIntroductionMovie'))

        rtTrack = Sequence()
        startPos = Point3(ToontownGlobals.CashbotBossOffstagePosHpr[0], ToontownGlobals.CashbotBossOffstagePosHpr[1], ToontownGlobals.CashbotBossOffstagePosHpr[2])
        battlePos = Point3(ToontownGlobals.CashbotBossBattleOnePosHpr[0], ToontownGlobals.CashbotBossBattleOnePosHpr[1], ToontownGlobals.CashbotBossBattleOnePosHpr[2])
        battleHpr = VBase3(ToontownGlobals.CashbotBossBattleOnePosHpr[3], ToontownGlobals.CashbotBossBattleOnePosHpr[4], ToontownGlobals.CashbotBossBattleOnePosHpr[5])
        bossTrack = Sequence()
        bossTrack.append(Func(self.reparentTo, render))
        bossTrack.append(Func(self.getGeomNode().setH, 180))
        bossTrack.append(Func(self.pelvis.setHpr, self.pelvisForwardHpr))
        bossTrack.append(Func(self.loop, 'Ff_neutral'))
        bossTrack.append(Wait(4))
        track, hpr = self.rollBossToPoint(startPos, None, battlePos, None, 0)
        bossTrack.append(track)
        track, hpr = self.rollBossToPoint(battlePos, hpr, battlePos, battleHpr, 0)
        bossTrack.append(track)
        bossTrack.append(Func(self.getGeomNode().setH, 0))
        bossTrack.append(Func(self.pelvis.setHpr, self.pelvisReversedHpr))
        goonTrack = self.__makeGoonMovieForIntro()
        cogGoonTrack = self.__makeCogGoonMovieForIntro()
        attackToons = TTL.CashbotBossCogHardmodeAttack
        rToon = self.resistanceToon
        rToon.setPosHpr(*ToontownGlobals.CashbotRTBattleOneStartPosHpr)
        rToonTrack = Sequence()
        rToonTrack.append(Wait(1))
        rToonTrack.append(Func(rToon.setChatAbsolute, TTL.ResistanceToonHardmodeGottaGo, CFSpeech))
        rToonTrack.append(Func(rToon.suit.loop, 'walk'))
        rToonTrack.append(rToon.hprInterval(1, VBase3(180, 0, 0)))
        rToonTrack.append(Parallel(Sequence(Wait(4),
                                            self.door2.posInterval(3, VBase3(0, 0, 0))),
                                   Sequence(rToon.posInterval(5, Point3(ToontownGlobals.CashbotBossHardmodeCogGoonOffstage2PosHpr[0], ToontownGlobals.CashbotBossHardmodeCogGoonOffstage2PosHpr[1], ToontownGlobals.CashbotBossHardmodeCogGoonOffstage2PosHpr[2])),
                                           )))
        track = Sequence(
            Func(camera.setPosHpr, 82, -219, 5, 267, 0, 0),
            Func(rToon.setChatAbsolute, TTL.ResistanceToonWelcome, CFSpeech),
            Wait(3),
            Sequence(goonTrack, duration=0),
            Parallel(
                camera.posHprInterval(4, Point3(108, -244, 4), VBase3(211.5, 0, 0), blendType='easeInOut'),
                Sequence(
                    Func(rToon.suit.setPlayRate, 1.4, 'walk'),
                    Func(rToon.suit.loop, 'walk'),
                    Parallel(
                        rToon.hprInterval(1, VBase3(180, 0, 0)),
                        rToon.posInterval(3, VBase3(120, -255, 0)),
                        Sequence(
                            Wait(2),
                            Func(rToon.clearChat))),
                        Func(rToon.suit.loop, 'neutral'),
                        Parallel(self.door2.posInterval(3, VBase3(0, 0, 30)),
                                 Sequence(Wait(1),
                                          Func(rToon.suit.loop, 'walk'),
                                          Parallel(rToon.hprInterval(1.5, VBase3(0, 0, 0)),
                                          Sequence(Wait(0.6),
                                                   Func(rToon.setChatAbsolute, TTL.ResistanceToonHardmodeTooLate, CFSpeech)))),
                                 Sequence(Wait(2.5),
                                          Func(rToon.suit.loop, 'neutral')),
                                 Func(camera.reparentTo, render)
                                 ))),
                        Parallel(camera.posHprInterval(3, Point3(61.1, -228.8, 10.2), VBase3(270, 0, 0), blendType='easeInOut'),
                                 self.door1.posInterval(3, VBase3(0, 0, 30))),
                        Parallel(
                            Sequence(cogGoonTrack, duration=0),
                            rToonTrack,
                            bossTrack,
                            Sequence(
                                Wait(7),
                                Func(rToon.clearChat),
                                self.door1.posInterval(3, VBase3(0, 0, 0)))),
                            Func(self.setChatAbsolute, TTL.CashbotBossHardmodeDiscoverToons1, CFSpeech),
                            camera.posHprInterval(1.5, Point3(93.3, -230, 0.7), VBase3(267.1, 39.7, 8.3)),
                            Wait(2),
                            Func(self.clearChat),
                            Func(self.setChatAbsolute, TTL.CashbotBossHardmodeDiscoverToons2, CFSpeech),
                            Wait(4),
                            Func(self.clearChat),
                            self.loseCogSuits(self.toonsA + self.toonsB, render, (113, -228, 10, 90, 0, 0)),
                            Wait(0.5),
                            Sequence(
                                self.toonNormalEyes(self.involvedToons),
                                Func(camera.setPosHpr, 93.3, -230, 0.7, -92.9, 39.7, 8.3),
                                Func(self.setChatAbsolute, TTL.CashbotBossHardmodeDiscoverToons3, CFSpeech),
                                Wait(4),
                                Func(self.clearChat),
                                Func(self.setChatAbsolute, TTL.CashbotBossHardmodeDiscoverToons4, CFSpeech),
                                Wait(4),
                                Func(self.clearChat),
                                Func(self.setChatAbsolute, TTL.CashbotBossHardmodeDiscoverToons5, CFSpeech),
                                Wait(4),
                                Func(self.clearChat),
                                Parallel(Func(self.setChatAbsolute, attackToons, CFSpeech),
                                     LerpColorScaleInterval(render, 2, (0.65, 1.0, 0.8, 1.0))),
                                Wait(2),
                                Func(self.clearChat)))
        return Sequence(Func(camera.reparentTo, render), track)

    def __makeGoonMovieForBattleThree(self):
        goonPosHprs = [[Point3(111, -287, 0),
          VBase3(165, 0, 0),
          Point3(101, -323, 0),
          VBase3(165, 0, 0)], [Point3(119, -315, 0),
          VBase3(357, 0, 0),
          Point3(121, -280, 0),
          VBase3(357, 0, 0)], [Point3(102, -320, 0),
          VBase3(231, 0, 0),
          Point3(127, -337, 0),
          VBase3(231, 0, 0)]]
        mainGoon = self.fakeGoons[0]
        goonLoop = Parallel()
        print self.fakeGoons
        for i in xrange(1, self.numFakeGoons):
            goon = self.fakeGoons[i]
            goonLoop.append(Sequence(goon.posHprInterval(8, goonPosHprs[i][0], goonPosHprs[i][1]), goon.posHprInterval(8, goonPosHprs[i][2], goonPosHprs[i][3])))

        goonTrack = Sequence(Func(self.__showFakeGoons, 'Walk'), Func(mainGoon.request, 'Stunned'), Func(goonLoop.loop), Wait(20))
        return goonTrack

    def makePrepareBattleTwoMovie(self, delayDeletes, crane, safe):
        for toonId in self.involvedToons:
            toon = self.cr.doId2do.get(toonId)
            if toon:
                delayDeletes.append(DelayDelete.DelayDelete(toon, 'CashbotBoss.makeRollToBattleTwoMovie'))

        startPos = Point3(ToontownGlobals.CashbotBossBattleOnePosHpr[0], ToontownGlobals.CashbotBossBattleOnePosHpr[1],
                          ToontownGlobals.CashbotBossBattleOnePosHpr[2])
        midPos = Point3(ToontownGlobals.CashbotBossHardmodeBattleTwoMidPosHpr[0], ToontownGlobals.CashbotBossHardmodeBattleTwoMidPosHpr[1],
                          ToontownGlobals.CashbotBossHardmodeBattleTwoMidPosHpr[2])
        battlePos = Point3(ToontownGlobals.CashbotBossBattleThreePosHpr[0],
                           ToontownGlobals.CashbotBossBattleThreePosHpr[1],
                           ToontownGlobals.CashbotBossBattleThreePosHpr[2])
        startHpr = Point3(ToontownGlobals.CashbotBossBattleOnePosHpr[3], ToontownGlobals.CashbotBossBattleOnePosHpr[4],
                          ToontownGlobals.CashbotBossBattleOnePosHpr[5])
        battleHpr = VBase3(ToontownGlobals.CashbotBossBattleThreePosHpr[3],
                           ToontownGlobals.CashbotBossBattleThreePosHpr[4],
                           ToontownGlobals.CashbotBossBattleThreePosHpr[5])
        finalHpr = VBase3(135, 0, 0)
        battleANodePos = self.battleANode.getPos()
        battleBNodePos = self.battleBNode.getPos()
        battleANodeHpr = self.battleANode.getHpr()
        battleBNodeHpr = self.battleBNode.getHpr()
        bossTrack = Sequence()
        bossTrack.append(Func(self.reparentTo, render))
        bossTrack.append(Func(self.getGeomNode().setH, 180))
        bossTrack.append(Func(self.pelvis.setHpr, self.pelvisForwardHpr))
        bossTrack.append(Func(self.loop, 'Ff_neutral'))
        track, hpr = self.rollBossToPoint(startPos, startHpr, startPos, battleHpr, 0)
        bossTrack.append(track)
        track, hpr = self.rollBossToPoint(startPos, None, midPos, None, 0)
        bossTrack.append(track)
        rToon = self.resistanceToon
        rToon.setPosHpr(93.935, -341.065, 0, -45, 0, 0)
        goon = self.cogGoons[0]
        walkTime = 3
        turnTime = 0.3
        goonFinalPos = (140, ToontownGlobals.CashbotBattleTwoGoonChasePosHpr[4][1], ToontownGlobals.CashbotBattleTwoGoonChasePosHpr[4][2])
        goonFinalHpr = (ToontownGlobals.CashbotBattleTwoGoonChasePosHpr[4][3], ToontownGlobals.CashbotBattleTwoGoonChasePosHpr[4][4], ToontownGlobals.CashbotBattleTwoGoonChasePosHpr[4][5])
        rToonForParallel = Sequence(rToon.posInterval(walkTime, (ToontownGlobals.CashbotBattleTwoGoonChasePosHpr[1][0], ToontownGlobals.CashbotBattleTwoGoonChasePosHpr[1][1], ToontownGlobals.CashbotBattleTwoGoonChasePosHpr[1][2])),
                         rToon.hprInterval(turnTime, (ToontownGlobals.CashbotBattleTwoGoonChasePosHpr[2][3], 0, 0)),
                         rToon.posInterval(walkTime, (ToontownGlobals.CashbotBattleTwoGoonChasePosHpr[2][0], ToontownGlobals.CashbotBattleTwoGoonChasePosHpr[2][1], ToontownGlobals.CashbotBattleTwoGoonChasePosHpr[2][2])),
                         rToon.hprInterval(turnTime, (ToontownGlobals.CashbotBattleTwoGoonChasePosHpr[3][3], 0, 0)),
                         rToon.posInterval(walkTime, (ToontownGlobals.CashbotBattleTwoGoonChasePosHpr[3][0], ToontownGlobals.CashbotBattleTwoGoonChasePosHpr[3][1], ToontownGlobals.CashbotBattleTwoGoonChasePosHpr[3][2])),
                         rToon.hprInterval(turnTime, (ToontownGlobals.CashbotBattleTwoGoonChasePosHpr[4][3], 0, 0)),
                         rToon.posInterval(walkTime, (ToontownGlobals.CashbotBattleTwoGoonChasePosHpr[4][0], ToontownGlobals.CashbotBattleTwoGoonChasePosHpr[4][1], ToontownGlobals.CashbotBattleTwoGoonChasePosHpr[4][2])),
                         Func(rToon.animFSM.request, 'FallDown'),
                         rToon.posInterval(0.5, (ToontownGlobals.CashbotBattleTwoGoonChasePosHpr[5][0], ToontownGlobals.CashbotBattleTwoGoonChasePosHpr[5][1], ToontownGlobals.CashbotBattleTwoGoonChasePosHpr[5][2])),
                         Wait(1.5),
                         Func(rToon.animFSM.request, 'walk'),
                         rToon.hprInterval(1.5, (ToontownGlobals.CashbotBattleTwoGoonChasePosHpr[2][3], 0, 0)),
                         Func(rToon.animFSM.request, 'cringe'),
                         Wait(2),
                         Func(rToon.enterDied),
                         Wait(5))
        bossRollMidMovie = Sequence()
        track, hpr = self.rollBossToPoint(midPos, None, battlePos, None, 0)
        bossRollMidMovie.append(track)
        track, hpr = self.rollBossToPoint(battlePos, battleHpr, battlePos, finalHpr, 0)
        bossRollMidMovie.append(track)
        goonForParallel = Sequence(Wait(2.5),
                         goon.posInterval(walkTime, (ToontownGlobals.CashbotBattleTwoGoonChasePosHpr[1][0], ToontownGlobals.CashbotBattleTwoGoonChasePosHpr[1][1], ToontownGlobals.CashbotBattleTwoGoonChasePosHpr[1][2])),
                         goon.hprInterval(turnTime, (ToontownGlobals.CashbotBattleTwoGoonChasePosHpr[2][3], 0, 0)),
                         goon.posInterval(walkTime, (ToontownGlobals.CashbotBattleTwoGoonChasePosHpr[2][0], ToontownGlobals.CashbotBattleTwoGoonChasePosHpr[2][1], ToontownGlobals.CashbotBattleTwoGoonChasePosHpr[2][2])),
                         goon.hprInterval(turnTime, (ToontownGlobals.CashbotBattleTwoGoonChasePosHpr[3][3], 0, 0)),
                         goon.posInterval(walkTime, (ToontownGlobals.CashbotBattleTwoGoonChasePosHpr[3][0], ToontownGlobals.CashbotBattleTwoGoonChasePosHpr[3][1], ToontownGlobals.CashbotBattleTwoGoonChasePosHpr[3][2])),
                         goon.hprInterval(turnTime, (ToontownGlobals.CashbotBattleTwoGoonChasePosHpr[4][3], 0, 0)),
                         goon.posInterval(walkTime + 1, (goonFinalPos[0], goonFinalPos[1], goonFinalPos[2])),
                         Func(goon.request, 'Battle'),
                         Wait(9),
                         Func(camera.reparentTo, self),
                         Func(camera.setPosHpr, 0, 25, 25.4, 180, 0, 0),
                         Parallel(
                             Sequence(
                                 Wait(1.5),
                                 Func(self.setChatAbsolute, TTL.CashbotBossHardmodeGoons1, CFSpeech),
                                 Wait(4),
                                 Func(self.clearChat),
                                 Func(self.setChatAbsolute, TTL.CashbotBossHardmodeGoons2, CFSpeech)),

                             bossRollMidMovie),
                         Wait(1),
                         Func(goon.request, 'Stand'),
                         Func(self.clearChat),
                         Parallel(camera.posInterval(1, (0, 25, 26.7), blendType='easeInOut'),
                                  Func(self.setChatAbsolute, TTL.CashbotBossHardmodeGoons3, CFSpeech)),
                         Wait(4),
                         Func(self.clearChat),
                         Func(camera.reparentTo, self.geom),
                         Func(camera.setPosHpr, Point3(ToontownGlobals.CashbotBossBattleThreePosHpr[0] + 5, ToontownGlobals.CashbotBossBattleThreePosHpr[1] + 20, ToontownGlobals.CashbotBossBattleThreePosHpr[2] + 25), VBase3(210, -30, 0)),
                         Wait(0.5),
                         LerpColorScaleInterval(goon.radar, 1, (0, 1, 0, 1), blendType='easeIn'),
                         Func(goon.request, 'Walk'),
                         goon.hprInterval(1, (ToontownGlobals.CashbotBossHardmodeBattleTwoGoonMidwayPosHpr[3], 0, 0)),
                         Parallel(
                             Sequence(
                                 goon.posInterval(2, (ToontownGlobals.CashbotBossHardmodeBattleTwoGoonMidwayPosHpr[0], ToontownGlobals.CashbotBossHardmodeBattleTwoGoonMidwayPosHpr[1], ToontownGlobals.CashbotBossHardmodeBattleTwoGoonMidwayPosHpr[2])),
                                 goon.hprInterval(0.6, (ToontownGlobals.CashbotBossHardmodeBattleTwoGoonPosHpr[3], 0, 0)),
                                 goon.posInterval(2, (ToontownGlobals.CashbotBossHardmodeBattleTwoGoonPosHpr[0], ToontownGlobals.CashbotBossHardmodeBattleTwoGoonPosHpr[1], ToontownGlobals.CashbotBossHardmodeBattleTwoGoonPosHpr[2])),
                                 goon.hprInterval(1, (-50, 0, 0))),
                             camera.posHprInterval(3.5, Point3(ToontownGlobals.CashbotBossBattleThreePosHpr[0] - 20, ToontownGlobals.CashbotBossBattleThreePosHpr[1] + 32, ToontownGlobals.CashbotBossBattleThreePosHpr[2] + 45), (210, -55, 0), blendType='easeInOut')),

                         Func(goon.request, 'Stand'),
                         Wait(1.2),
                         Func(camera.reparentTo, self),
                         Func(camera.setPosHpr, 0, 25, 24.6, 180, 0, 0),
                         Func(self.setChatAbsolute, TTL.CashbotBossHardmodeGoons4, CFSpeech),
                         Wait(4),
                         Func(self.clearChat),
                         Parallel(camera.posInterval(1, (0, 25, 26.7), blendType='easeInOut'),
                                  Func(self.setChatAbsolute, TTL.CashbotBossHardmodeGoons5, CFSpeech)),
                         Wait(4),
                         Func(self.clearChat),
                                   Parallel(camera.posInterval(1, (0, 25, 24.6), blendType='easeInOut'),
                                            Func(self.setChatAbsolute, TTL.CashbotBossHardmodeGoons6, CFSpeech)),
                         Wait(4),
                         Func(self.clearChat),
                         Parallel(
                            self.door3.posInterval(3, VBase3(0, 0, 0)),
                             Sequence(Func(self.setChatAbsolute, TTL.CashbotBossHardmodeGoons7, CFSpeech),
                             Wait(4),
                             Func(self.clearChat))))
        goonChaseTrack = Sequence(
            Func(rToon.animFSM.request, 'run'),
            Func(goon.request, 'Walk'),
            Func(rToon.setPosHpr, *ToontownGlobals.CashbotBattleTwoGoonChasePosHpr[0]),
            Func(goon.setPosHpr, *ToontownGlobals.CashbotBattleTwoGoonChasePosHpr[0]),
            Parallel(
                rToonForParallel,
                goonForParallel
        ))
        track = Sequence(
            Func(self.__hideToons),
            Parallel(
                self.door2.posInterval(4.5, VBase3(0, 0, 30)),
                self.door3.posInterval(4.5, VBase3(0, 0, 30)),
                bossTrack,
                goonChaseTrack,
                Sequence(Wait(5),
                         Func(camera.wrtReparentTo, self.geom),
                         camera.posHprInterval(5, Point3(ToontownGlobals.CashbotBossBattleThreePosHpr[0] + 5, ToontownGlobals.CashbotBossBattleThreePosHpr[1] + 20, ToontownGlobals.CashbotBossBattleThreePosHpr[2] + 25), VBase3(210, -30, 0), blendType='easeOut'))),
            Func(self.getGeomNode().setH, 0),
            Func(self.__showToons))
        return Sequence(Func(camera.reparentTo, self), Func(camera.setPosHpr, 0, -27, 25, 0, -18, 0), track, name=self.uniqueName('BattleTwo'))

    def makePrepareBattleThreeMovie(self, delayDeletes, crane, safe):
        for toonId in self.involvedToons:
            toon = self.cr.doId2do.get(toonId)
            if toon:
                delayDeletes.append(DelayDelete.DelayDelete(toon, 'CashbotBoss.makePrepareBattleThreeMovie'))

        rToon = self.resistanceToon
        rToon.setPosHpr(93.935, -341.065, 0, -45, 0, 0)
        goon = self.fakeGoons[0]
        crane = self.cranes[0]
        track = Sequence(
            Func(self.__hideToons),
            Func(crane.request, 'Movie'),
            Func(crane.accomodateToon, rToon),
            Func(goon.request, 'Stunned'),
            Func(goon.setPosHpr, 104, -316, 0, 165, 0, 0),
            Func(rToon.loop, 'leverNeutral'),
            Func(camera.reparentTo, self.geom),
            Func(camera.setPosHpr, 105, -326, 5, 136.3, 0, 0),
            Func(rToon.setChatAbsolute, TTL.ResistanceToonWatchThis, CFSpeech),
            Wait(2),
            Func(rToon.clearChat),
            Func(camera.setPosHpr, 105, -326, 20, -45.3, 11, 0),
            Func(self.setChatAbsolute, TTL.CashbotBossGetAwayFromThat, CFSpeech),
            Wait(2),
            Func(self.clearChat),
            camera.posHprInterval(1.5, Point3(105, -326, 5), Point3(136.3, 0, 0), blendType='easeInOut'),
            Func(rToon.setChatAbsolute, TTL.ResistanceToonCraneInstructions1, CFSpeech),
            Wait(4),
            Func(rToon.setChatAbsolute, TTL.ResistanceToonCraneInstructions2, CFSpeech),
            Wait(4),
            Func(rToon.setChatAbsolute, TTL.ResistanceToonCraneInstructions3, CFSpeech),
            Wait(4),
            Func(rToon.setChatAbsolute, TTL.ResistanceToonCraneInstructions4, CFSpeech),
            Wait(4),
            Func(rToon.clearChat),
            Func(camera.setPosHpr, 102, -323.6, 0.9, -10.6, 14, 0),
            Func(goon.request, 'Recovery'),
            Wait(2),
            Func(camera.setPosHpr, 95.4, -332.6, 4.2, 167.1, -13.2, 0),
            Func(rToon.setChatAbsolute, TTL.ResistanceToonGetaway, CFSpeech),
            Func(rToon.animFSM.request, 'jump'),
            Wait(1.8),
            Func(rToon.clearChat),
            Func(camera.setPosHpr, 109.1, -300.7, 13.9, -15.6, -13.6, 0),
            Func(rToon.animFSM.request, 'run'),
            Func(goon.request, 'Walk'),
            Parallel(
                self.door3.posInterval(3, VBase3(0, 0, 0)),
                rToon.posHprInterval(3, Point3(136, -212.9, 0), VBase3(-14, 0, 0), startPos=Point3(110.8, -292.7, 0), startHpr=VBase3(-14, 0, 0)),
                goon.posHprInterval(3, Point3(125.2, -243.5, 0), VBase3(-14, 0, 0), startPos=Point3(104.8, -309.5, 0), startHpr=VBase3(-14, 0, 0))),
            Func(self.__hideFakeGoons),
            Func(crane.request, 'Free'),
            Func(self.getGeomNode().setH, 0),
            self.moveToonsToBattleThreePos(self.involvedToons),
            Func(self.__showToons),
            Func(self.__hideCogGoons))
        return Sequence(Func(camera.reparentTo, self), Func(camera.setPosHpr, 0, -27, 25, 0, -18, 0), track)

    def moveToonsToBattleThreePos(self, toons):
        track = Parallel()
        for i in xrange(len(toons)):
            toon = base.cr.doId2do.get(toons[i])
            if toon:
                posHpr = ToontownGlobals.CashbotToonsBattleThreeStartPosHpr[i]
                pos = Point3(*posHpr[0:3])
                hpr = VBase3(*posHpr[3:6])
                track.append(toon.posHprInterval(0.2, pos, hpr))

        return track

    def makeBossFleeMovie(self):
        hadEnough = TTLocalizer.CashbotBossHadEnough
        outtaHere = TTLocalizer.CashbotBossOuttaHere
        loco = loader.loadModel('phase_10/models/cogHQ/CashBotLocomotive')
        car1 = loader.loadModel('phase_10/models/cogHQ/CashBotBoxCar')
        car2 = loader.loadModel('phase_10/models/cogHQ/CashBotTankCar')
        trainPassingSfx = base.loader.loadSfx('phase_10/audio/sfx/CBHQ_TRAIN_pass.ogg')
        boomSfx = loader.loadSfx('phase_3.5/audio/sfx/ENC_cogfall_apart.ogg')
        rollThroughDoor = self.rollBossToPoint(fromPos=Point3(120, -280, 0), fromHpr=None, toPos=Point3(120, -250, 0), toHpr=None, reverse=0)
        rollTrack = Sequence(Func(self.getGeomNode().setH, 180), rollThroughDoor[0], Func(self.getGeomNode().setH, 0))
        g = 80.0 / 300.0
        trainTrack = Track(
            (0 * g, loco.posInterval(0.5, Point3(0, -242, 0), startPos=Point3(150, -242, 0))),
            (1 * g, car2.posInterval(0.5, Point3(0, -242, 0), startPos=Point3(150, -242, 0))),
            (2 * g, car1.posInterval(0.5, Point3(0, -242, 0), startPos=Point3(150, -242, 0))),
            (3 * g, car2.posInterval(0.5, Point3(0, -242, 0), startPos=Point3(150, -242, 0))),
            (4 * g, car1.posInterval(0.5, Point3(0, -242, 0), startPos=Point3(150, -242, 0))),
            (5 * g, car2.posInterval(0.5, Point3(0, -242, 0), startPos=Point3(150, -242, 0))),
            (6 * g, car1.posInterval(0.5, Point3(0, -242, 0), startPos=Point3(150, -242, 0))),
            (7 * g, car2.posInterval(0.5, Point3(0, -242, 0), startPos=Point3(150, -242, 0))),
            (8 * g, car1.posInterval(0.5, Point3(0, -242, 0), startPos=Point3(150, -242, 0))),
            (9 * g, car2.posInterval(0.5, Point3(0, -242, 0), startPos=Point3(150, -242, 0))),
            (10 * g, car1.posInterval(0.5, Point3(0, -242, 0), startPos=Point3(150, -242, 0))),
            (11 * g, car2.posInterval(0.5, Point3(0, -242, 0), startPos=Point3(150, -242, 0))),
            (12 * g, car1.posInterval(0.5, Point3(0, -242, 0), startPos=Point3(150, -242, 0))),
            (13 * g, car2.posInterval(0.5, Point3(0, -242, 0), startPos=Point3(150, -242, 0))),
            (14 * g, car1.posInterval(0.5, Point3(0, -242, 0), startPos=Point3(150, -242, 0))))
        bossTrack = Track(
            (0.0, Sequence(
                Func(camera.reparentTo, render),
                Func(camera.setPosHpr, 105, -280, 20, -158, -3, 0),
                Func(self.reparentTo, render),
                Func(self.show),
                Func(self.clearChat),
                Func(self.setPosHpr, *ToontownGlobals.CashbotBossBattleThreePosHpr),
                Func(self.reverseHead),
                ActorInterval(self, 'Fb_firstHit'),
                ActorInterval(self, 'Fb_down2Up'))),
            (1.0, Func(self.setChatAbsolute, hadEnough, CFSpeech)),
            (5.5, Parallel(
                Func(camera.setPosHpr, 100, -315, 16, -20, 0, 0),
                Func(self.hideBattleThreeObjects),
                Func(self.forwardHead),
                Func(self.loop, 'Ff_neutral'),
                rollTrack,
                self.door3.posInterval(2.5, Point3(0, 0, 25), startPos=Point3(0, 0, 18)))),
            (5.5, Func(self.setChatAbsolute, outtaHere, CFSpeech)),
            (5.5, SoundInterval(trainPassingSfx)),
            (8.1, Func(self.clearChat)),
            (9.4, Sequence(
                Func(loco.reparentTo, render),
                Func(car1.reparentTo, render),
                Func(car2.reparentTo, render),
                trainTrack,
                Func(loco.detachNode),
                Func(car1.detachNode),
                Func(car2.detachNode),
                Wait(2))),
            (9.5, SoundInterval(boomSfx)),
            (9.5, Sequence(
                self.posInterval(0.4, Point3(0, -250, 0)),
                Func(self.stash))))
        return bossTrack

    def grabObject(self, obj):
        obj.wrtReparentTo(self.neck)
        obj.hideShadows()
        obj.stashCollisions()
        if obj.lerpInterval:
            obj.lerpInterval.finish()
        obj.lerpInterval = Parallel(obj.posInterval(ToontownGlobals.CashbotBossToMagnetTime, Point3(-1, 0, 0.2)), obj.quatInterval(ToontownGlobals.CashbotBossToMagnetTime, VBase3(0, -90, 90)), Sequence(Wait(ToontownGlobals.CashbotBossToMagnetTime), ShowInterval(self.eyes)), obj.toMagnetSoundInterval)
        obj.lerpInterval.start()
        self.heldObject = obj

    def dropObject(self, obj):
        if obj.lerpInterval:
            obj.lerpInterval.finish()
            obj.lerpInterval = None
        obj = self.heldObject
        obj.wrtReparentTo(render)
        obj.setHpr(obj.getH(), 0, 0)
        self.eyes.hide()
        obj.showShadows()
        obj.unstashCollisions()
        self.heldObject = None
        return

    def setBossDamage(self, bossDamage):
        if bossDamage > self.bossDamage:
            delta = bossDamage - self.bossDamage
            self.flashRed()
            self.doAnimate('hit', now=1)
            self.showHpText(-delta, scale=5)
        self.bossDamage = bossDamage
        self.updateHealthBar()
        self.bossHealthBar.update(self.bossMaxDamage - bossDamage, self.bossMaxDamage)

    def setRewardId(self, rewardId):
        self.rewardId = rewardId

    def d_applyReward(self):
        self.sendUpdate('applyReward', [])

    def stunAllGoons(self):
        for goon in self.goons:
            if goon.state == 'Walk' or goon.state == 'Battle':
                goon.demand('Stunned')
                goon.sendUpdate('requestStunned', [0])

    def destroyAllGoons(self):
        for goon in self.goons:
            if goon.state != 'Off' and not goon.isDead:
                goon.b_destroyGoon()

    def deactivateCranes(self):
        for crane in self.cranes.values():
            crane.demand('Free')

    def hideBattleThreeObjects(self):
        for goon in self.goons:
            goon.demand('Off')

        for safe in self.safes.values():
            safe.demand('Off')

        for crane in self.cranes.values():
            crane.demand('Off')

    def __doPhysics(self, task):
        dt = globalClock.getDt()
        self.physicsMgr.doPhysics(dt)
        return Task.cont

    def __hideToons(self):
        for toonId in self.involvedToons:
            toon = self.cr.doId2do.get(toonId)
            if toon:
                toon.hide()

    def __showToons(self):
        for toonId in self.involvedToons:
            toon = self.cr.doId2do.get(toonId)
            if toon:
                toon.show()

    def __arrangeToonsAroundResistanceToon(self, num):
        radius = 7
        numToons = len(self.involvedToons)
        center = (numToons - 1) / 2.0
        for i in xrange(numToons):
            toon = self.cr.doId2do.get(self.involvedToons[i])
            if toon:
                angle = 90 - 15 * (i - center)
                radians = angle * math.pi / 180.0
                x = math.cos(radians) * radius
                y = math.sin(radians) * radius
                if num == 1:
                    toon.setPos(self.resistanceToon, x, y, 0)
                    toon.headsUp(self.resistanceToon)
                elif num == 2:
                    toon.setPos(self.resistanceToonTwo, x, y, 0)
                    toon.headsUp(self.resistanceToonTwo)
                toon.loop('neutral')
                toon.show()

    def __talkAboutPromotion(self, speech):
        if self.prevCogSuitLevel < ToontownGlobals.MaxCogSuitLevel:
            newCogSuitLevel = localAvatar.getCogLevels()[CogDisguiseGlobals.dept2deptIndex(self.style.dept)]
            if newCogSuitLevel == ToontownGlobals.MaxCogSuitLevel:
                speech += TTLocalizer.ResistanceToonLastPromotion % (ToontownGlobals.MaxCogSuitLevel + 1)
            if newCogSuitLevel in ToontownGlobals.CogSuitHPLevels:
                speech += TTLocalizer.ResistanceToonHPBoost
        else:
            speech += TTLocalizer.ResistanceToonMaxed % (ToontownGlobals.MaxCogSuitLevel + 1)
        return speech

    def enterOff(self):
        DistributedBossCog.DistributedBossCog.enterOff(self)
        if self.resistanceToon:
            self.resistanceToon.clearChat()
        if self.resistanceToonTwo:
            self.resistanceToonTwo.clearChat()

    def enterWaitForToons(self):
        DistributedBossCog.DistributedBossCog.enterWaitForToons(self)
        self.detachNode()
        self.geom.hide()
        self.resistanceToon.removeActive()

    def exitWaitForToons(self):
        DistributedBossCog.DistributedBossCog.exitWaitForToons(self)
        self.geom.show()
        self.resistanceToon.addActive()

    def enterElevator(self):
        DistributedBossCog.DistributedBossCog.enterElevator(self)
        self.detachNode()
        self.resistanceToon.removeActive()
        self.endVault.stash()
        self.midVault.unstash()
        self.__showResistanceToon(True)

    def exitElevator(self):
        DistributedBossCog.DistributedBossCog.exitElevator(self)
        self.resistanceToon.addActive()

    def enterIntroduction(self):
        self.detachNode()
        self.stopAnimate()
        self.endVault.unstash()
        self.evWalls.stash()
        self.midVault.unstash()
        self.__showResistanceToon(True)
        self.__hideResistanceToonTwo()
        base.playMusic(self.stingMusic, looping=1, volume=0.9)
        DistributedBossCog.DistributedBossCog.enterIntroduction(self)

    def exitIntroduction(self):
        DistributedBossCog.DistributedBossCog.exitIntroduction(self)
        self.stingMusic.stop()

    def enterBattleOne(self):
        DistributedBossCog.DistributedBossCog.enterBattleOne(self)
        self.reparentTo(render)
        self.setPosHpr(*ToontownGlobals.CashbotBossBattleOnePosHpr)
        self.show()
        self.pelvis.setHpr(self.pelvisReversedHpr)
        self.doAnimate()
        self.endVault.stash()
        self.midVault.unstash()
        self.__hideResistanceToon()

    def exitBattleOne(self):
        DistributedBossCog.DistributedBossCog.exitBattleOne(self)

    def enterRollToBattleTwo(self):
        self.__onToPrepareBattleTwo(0)

    def exitRollToBattleTwo(self):
        self.battleOneMusic.stop()

    def __onToPrepareBattleTwo(self, elapsed):
        self.doneBarrier('RollToBattleTwo')

    def enterPrepareBattleTwo(self):
        self.controlToons()
        NametagGlobals.setMasterArrowsOn(0)
        delayDeletes = []
        self.midVault.unstash()
        self.endVault.unstash()
        self.movieCrane = self.cranes[0]
        self.movieSafe = self.safes[1]
        self.movieCrane.request('Movie')
        intervalName = 'PrepareBattleTwoMovie'
        seq = Sequence(self.makePrepareBattleTwoMovie(delayDeletes, self.movieCrane, self.movieSafe),
                       Func(self.__beginBattleTwo), name=intervalName)
        seq.start()
        self.__showResistanceToon(False)
        self.storeInterval(seq, intervalName)

    def exitPrepareBattleTwo(self):
        self.cleanupIntervals()

    def enterBattleTwo(self):
        self.reparentTo(render)
        self.show()
        self.setPosHpr(*ToontownGlobals.CashbotBossHardmodeBattleTwoBossPosHpr)
        self.endVault.unstash()
        self.midVault.stash()
        self.releaseToons()
        self.toonsToBattlePosition(self.toonsA, self.battleANode)
        self.toonsToBattlePosition(self.toonsB, self.battleBNode)
        self.doAnimate()
        self.__hideResistanceToon()
        self.__hideResistanceToonTwo()
        base.playMusic(self.battleThreeMusic, looping=1, volume=0.9)

    def exitBattleTwo(self):
        self.battleThreeMusic.stop()
        self.cleanupBattles()

    def __beginBattleTwo(self):
        intervalName = 'PrepareBattleTwoMovie'
        self.clearInterval(intervalName)
        self.doneBarrier('PrepareBattleTwo')

    def enterPrepareBattleThree(self):
        self.controlToons()
        NametagGlobals.setMasterArrowsOn(0)
        intervalName = 'PrepareBattleThreeMovie'
        delayDeletes = []
        self.movieCrane = self.cranes[0]
        self.movieSafe = self.safes[1]
        self.movieCrane.request('Movie')
        seq = Sequence(self.makePrepareBattleThreeMovie(delayDeletes, self.movieCrane, self.movieSafe), Func(self.__beginBattleThree), name=intervalName)
        seq.delayDeletes = delayDeletes
        seq.start()
        self.storeInterval(seq, intervalName)
        self.endVault.unstash()
        self.evWalls.stash()
        self.midVault.unstash()
        taskMgr.add(self.__doPhysics, self.uniqueName('physics'), priority=25)

    def __beginBattleThree(self):
        intervalName = 'PrepareBattleThreeMovie'
        self.clearInterval(intervalName)
        self.doneBarrier('PrepareBattleThree')

    def exitPrepareBattleThree(self):
        intervalName = 'PrepareBattleThreeMovie'
        self.clearInterval(intervalName)
        self.unstickToons()
        self.releaseToons()
        if self.newState == 'BattleThree':
            self.movieCrane.request('Free')
            self.movieSafe.request('Initial')
        NametagGlobals.setMasterArrowsOn(1)
        ElevatorUtils.closeDoors(self.leftDoor, self.rightDoor, ElevatorConstants.ELEVATOR_CFO)
        taskMgr.remove(self.uniqueName('physics'))

    def enterBattleThree(self):
        DistributedBossCog.DistributedBossCog.enterBattleThree(self)
        self.clearChat()
        self.resistanceToon.clearChat()
        self.reparentTo(render)
        self.setPosHpr(*ToontownGlobals.CashbotBossBattleThreePosHpr)
        self.happy = 1
        self.raised = 1
        self.forward = 1
        self.doAnimate()
        self.endVault.unstash()
        self.evWalls.unstash()
        self.midVault.stash()
        self.__hideResistanceToon()
        self.__hideResistanceToonTwo()
        localAvatar.setCameraFov(ToontownGlobals.BossBattleCameraFov)
        self.generateHealthBar()
        self.updateHealthBar()
        base.playMusic(self.battleThreeMusic, looping=1, volume=0.9)
        taskMgr.add(self.__doPhysics, self.uniqueName('physics'), priority=25)
        self.bossHealthBar.initialize(self.bossMaxDamage - self.bossDamage, self.bossMaxDamage)

    def exitBattleThree(self):
        DistributedBossCog.DistributedBossCog.exitBattleThree(self)
        bossDoneEventName = self.uniqueName('DestroyedBoss')
        self.ignore(bossDoneEventName)
        self.stopAnimate()
        self.cleanupAttacks()
        self.setDizzy(0)
        self.removeHealthBar()
        localAvatar.setCameraFov(ToontownGlobals.CogHQCameraFov)
        if self.newState != 'Victory':
            self.battleThreeMusic.stop()
        taskMgr.remove(self.uniqueName('physics'))

    def enterVictory(self):
        self.cleanupIntervals()
        self.reparentTo(render)
        self.setPosHpr(*ToontownGlobals.CashbotBossBattleThreePosHpr)
        self.stopAnimate()
        self.endVault.unstash()
        self.evWalls.unstash()
        self.midVault.unstash()
        self.__hideResistanceToon()
        self.__hideResistanceToonTwo()
        self.__hideToons()
        self.clearChat()
        self.resistanceToon.clearChat()
        self.deactivateCranes()
        if self.cranes:
            self.cranes[1].demand('Off')
        self.releaseToons(finalBattle=1)
        if self.hasLocalToon():
            self.toMovieMode()
        intervalName = 'VictoryMovie'
        seq = Sequence(self.makeBossFleeMovie(), Func(self.__continueVictory), name=intervalName)
        seq.start()
        self.storeInterval(seq, intervalName)
        self.bossHealthBar.deinitialize()
        if self.oldState != 'BattleThree':
            base.playMusic(self.battleThreeMusic, looping=1, volume=0.9)

    def __continueVictory(self):
        self.doneBarrier('Victory')

    def exitVictory(self):
        self.cleanupIntervals()
        if self.newState != 'Reward':
            if self.hasLocalToon():
                self.toWalkMode()
        self.__showToons()
        self.door3.setPos(0, 0, 0)
        if self.newState != 'Reward':
            self.battleThreeMusic.stop()

    def enterReward(self):
        self.cleanupIntervals()
        self.clearChat()
        self.resistanceToon.clearChat()
        self.stash()
        self.stopAnimate()
        self.controlToons()
        panelName = self.uniqueName('reward')
        self.rewardPanel = RewardPanel.RewardPanel(panelName)
        victory, camVictory, skipper = MovieToonVictory.doToonVictory(1, self.involvedToons, self.toonRewardIds, self.toonRewardDicts, self.deathList, self.rewardPanel, allowGroupShot=0, uberList=self.uberList, noSkip=True)
        ival = Sequence(Parallel(victory, camVictory), Func(self.__doneReward))
        intervalName = 'RewardMovie'
        delayDeletes = []
        for toonId in self.involvedToons:
            toon = self.cr.doId2do.get(toonId)
            if toon:
                delayDeletes.append(DelayDelete.DelayDelete(toon, 'CashbotBoss.enterReward'))

        ival.delayDeletes = delayDeletes
        ival.start()
        self.storeInterval(ival, intervalName)
        if self.oldState != 'Victory':
            base.playMusic(self.battleThreeMusic, looping=1, volume=0.9)

    def __doneReward(self):
        self.doneBarrier('Reward')
        self.toWalkMode()

    def exitReward(self):
        intervalName = 'RewardMovie'
        self.clearInterval(intervalName)
        if self.newState != 'Epilogue':
            self.releaseToons()
        self.unstash()
        self.rewardPanel.destroy()
        del self.rewardPanel
        self.battleThreeMusic.stop()

    def enterEpilogue(self):
        self.cleanupIntervals()
        self.clearChat()
        self.resistanceToon.clearChat()
        self.resistanceToonTwo.clearChat()
        self.stash()
        self.stopAnimate()
        self.controlToons()
        self.__showResistanceToonTwo()
        self.resistanceToonTwo.setPosHpr(*ToontownGlobals.CashbotBossBattleThreePosHpr)
        self.resistanceToonTwo.loop('neutral')
        self.__arrangeToonsAroundResistanceToon(2)
        camera.reparentTo(render)
        camera.setPos(self.resistanceToonTwo, -9, 12, 6)
        camera.lookAt(self.resistanceToonTwo, 0, 0, 3)
        self.revertColorIval = Sequence(LerpColorScaleInterval(render, 2, (1.0, 1.0, 1.0, 1.0)))
        self.revertColorIval.start()
        intervalName = 'EpilogueMovie'
        text = ResistanceChat.getChatText(self.rewardId)
        menuIndex, itemIndex = ResistanceChat.decodeId(self.rewardId)
        value = ResistanceChat.getItemValue(self.rewardId)
        if menuIndex == ResistanceChat.RESISTANCE_TOONUP:
            if value == -1:
                instructions = TTLocalizer.ResistanceToonToonupAllInstructions
            else:
                instructions = TTLocalizer.ResistanceToonToonupInstructions % value
        elif menuIndex == ResistanceChat.RESISTANCE_MONEY:
            if value == -1:
                instructions = TTLocalizer.ResistanceToonMoneyAllInstructions
            else:
                instructions = TTLocalizer.ResistanceToonMoneyInstructions % value
        elif menuIndex == ResistanceChat.RESISTANCE_RESTOCK:
            if value == -1:
                instructions = TTLocalizer.ResistanceToonRestockAllInstructions
            else:
                trackName = TTLocalizer.BattleGlobalTracks[value]
                instructions = TTLocalizer.ResistanceToonRestockInstructions % trackName
        speech = TTLocalizer.ResistanceToonCongratulations % (text, instructions)
        speech = self.__talkAboutPromotion(speech)
        self.resistanceToonTwo.setLocalPageChat(speech, 0)
        self.accept('nextChatPage', self.__epilogueChatNext)
        self.accept('doneChatPage', self.__epilogueChatDone)
        base.playMusic(self.epilogueMusic, looping=1, volume=0.9)

    def __epilogueChatNext(self, pageNumber, elapsed):
        if pageNumber == 1:
            toon = self.resistanceToonTwo
            playRate = 0.75
            track = Sequence(ActorInterval(toon, 'victory', playRate=playRate, startFrame=0, endFrame=9), ActorInterval(toon, 'victory', playRate=playRate, startFrame=9, endFrame=0), Func(self.resistanceToon.loop, 'neutral'))
            intervalName = 'EpilogueMovieToonAnim'
            self.storeInterval(track, intervalName)
            track.start()
        elif pageNumber == 3:
            self.d_applyReward()
            ResistanceChat.doEffect(self.rewardId, self.resistanceToonTwo, self.involvedToons)

    def __epilogueChatDone(self, elapsed):
        self.resistanceToonTwo.setChatAbsolute(TTLocalizer.CagedToonGoodbye, CFSpeech)
        self.ignore('nextChatPage')
        self.ignore('doneChatPage')
        intervalName = 'EpilogueMovieToonAnim'
        self.clearInterval(intervalName)
        track = Parallel(Sequence(ActorInterval(self.resistanceToonTwo, 'wave'), Func(self.resistanceToonTwo.loop, 'neutral')), Sequence(Wait(0.5), Func(self.localToonToSafeZone)))
        self.storeInterval(track, intervalName)
        track.start()

    def exitEpilogue(self):
        self.clearInterval('EpilogueMovieToonAnim')
        self.unstash()
        self.epilogueMusic.stop()
        self.revertColorIval.finish()

    def enterFrolic(self):
        DistributedBossCog.DistributedBossCog.enterFrolic(self)
        self.setPosHpr(*ToontownGlobals.CashbotBossBattleOnePosHpr)
        self.releaseToons()
        if self.hasLocalToon():
            self.toWalkMode()
        self.door3.setZ(25)
        self.door2.setZ(25)
        self.endVault.unstash()
        self.evWalls.stash()
        self.midVault.unstash()
        self.__hideResistanceToon()
        self.__hideResistanceToonTwo()

    def exitFrolic(self):
        self.door3.setZ(0)
        self.door2.setZ(0)
