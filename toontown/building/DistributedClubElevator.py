from panda3d.core import *
from direct.distributed.ClockDelta import *
from direct.interval.IntervalGlobal import *
from toontown.building import ElevatorConstants
from toontown.building import DistributedElevatorFloor
from toontown.toonbase import ToontownGlobals
from direct.directnotify import DirectNotifyGlobal
from toontown.distributed import DelayDelete
from direct.showbase import PythonUtil


class DistributedClubElevator(DistributedElevatorFloor.DistributedElevatorFloor):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedClubElevator')
    JumpOutOffsets = ((3, 5, 0),
     (1.5, 4, 0),
     (-1.5, 4, 0),
     (-3, 4, 0))

    def __init__(self, cr):
        DistributedElevatorFloor.DistributedElevatorFloor.__init__(self, cr)
        self.type = ElevatorConstants.ELEVATOR_COUNTRY_CLUB
        self.kartModelPath = 'phase_12/models/bossbotHQ/Coggolf_cart3.bam'
        self.leftDoor = None
        self.rightDoor = None
        self.__toonTracks = {}
        return

    def setupElevator(self):
        collisionRadius = ElevatorConstants.ElevatorData[self.type]['collRadius']
        self.elevatorSphere = CollisionSphere(0, 0, 0, collisionRadius)
        self.elevatorSphere.setTangible(1)
        self.elevatorSphereNode = CollisionNode(self.uniqueName('elevatorSphere'))
        self.elevatorSphereNode.setIntoCollideMask(ToontownGlobals.WallBitmask)
        self.elevatorSphereNode.addSolid(self.elevatorSphere)
        self.elevatorSphereNodePath = self.getElevatorModel().attachNewNode(self.elevatorSphereNode)
        self.elevatorSphereNodePath.hide()
        self.elevatorSphereNodePath.reparentTo(self.getElevatorModel())
        self.elevatorSphereNodePath.stash()
        self.boardedAvIds = {}
        self.finishSetup()

    def generate(self):
        DistributedElevatorFloor.DistributedElevatorFloor.generate(self)
        self.loader = self.cr.playGame.hood.loader
        self.elevatorModel = render.attachNewNode('golfKartNode')
        self.kart = loader.loadModel(self.kartModelPath)
        self.kart.setPos(0, 0, 0)
        self.kart.setScale(1)
        self.kart.reparentTo(self.elevatorModel)
        self.wheels = self.kart.findAllMatches('**/wheelNode*')
        self.numWheels = self.wheels.getNumPaths()
        self.setPosHpr(0, 0, 0, 0, 0, 0)

    def announceGenerate(self):
        DistributedElevatorFloor.DistributedElevatorFloor.announceGenerate(self)
        if self.latch:
            self.notify.info('Setting latch in announce generate')
            self.setLatch(self.latch)
        angle = self.startingHpr[0]
        angle -= 90
        radAngle = deg2Rad(angle)
        unitVec = Vec3(math.cos(radAngle), math.sin(radAngle), 0)
        unitVec *= 45.0
        self.endPos = self.startingPos + unitVec
        self.endPos.setZ(0.5)
        dist = Vec3(self.endPos - self.enteringPos).length()
        wheelAngle = dist / (4.8 * 1.4 * math.pi) * 360
        self.kartEnterAnimateInterval = Parallel(LerpHprInterval(self.wheels[0], 5.0, Vec3(self.wheels[0].getH(), wheelAngle, self.wheels[0].getR())), LerpHprInterval(self.wheels[1], 5.0, Vec3(self.wheels[1].getH(), wheelAngle, self.wheels[1].getR())), LerpHprInterval(self.wheels[2], 5.0, Vec3(self.wheels[2].getH(), wheelAngle, self.wheels[2].getR())), LerpHprInterval(self.wheels[3], 5.0, Vec3(self.wheels[3].getH(), wheelAngle, self.wheels[3].getR())), name='CogKartAnimate')
        trolleyExitTrack1 = Parallel(LerpPosInterval(self.elevatorModel, 5.0, self.endPos), self.kartEnterAnimateInterval, name='CogKartExitTrack')
        self.trolleyExitTrack = Sequence(trolleyExitTrack1)
        self.trolleyEnterTrack = Sequence(LerpPosInterval(self.elevatorModel, 5.0, self.startingPos, startPos=self.enteringPos))
        self.closeDoors = Sequence(self.trolleyExitTrack, Func(self.onDoorCloseFinish))
        self.openDoors = Sequence(self.trolleyEnterTrack)
        self.setPos(0, 0, 0)

    def disable(self):
        self.clearToonTracks()
        DistributedElevatorFloor.DistributedElevatorFloor.disable(self)

    def forceDoorsOpen(self):
        pass

    def forceDoorsClosed(self):
        pass

    def getElevatorModel(self):
        return self.elevatorModel

    def setPosHpr(self, x, y, z, h, p, r):
        self.startingPos = Vec3(x, y, z)
        self.enteringPos = Vec3(x, y, z - 10)
        self.startingHpr = Vec3(h, 0, 0)
        self.elevatorModel.setPosHpr(x, y, z, h, 0, 0)

    def fillSlot(self, index, avId):
        self.notify.debug('%s.fillSlot(%s, %s, ...)' % (self.doId, index, avId))
        request = self.toonRequests.get(index)
        if request:
            self.cr.relatedObjectMgr.abortRequest(request)
            del self.toonRequests[index]
        if avId == 0:
            pass
        elif avId not in self.cr.doId2do:
            func = PythonUtil.Functor(self.gotToon, index, avId)
            self.toonRequests[index] = self.cr.relatedObjectMgr.requestObjects([avId], allCallback=func)
        elif not self.isSetup:
            self.deferredSlots.append((index, avId))
        else:
            if avId == base.localAvatar.getDoId():
                self.localToonOnBoard = 1
                elevator = self.getPlaceElevator()
                elevator.fsm.request('boarding', [self.getElevatorModel()])
                elevator.fsm.request('boarded')
            toon = self.cr.doId2do[avId]
            toon.stopSmooth()
            toon.wrtReparentTo(self.elevatorModel)
            jumpTrack = self.generateToonJumpTrack(toon, index)
            track = Sequence(jumpTrack, Func(toon.setAnimState, 'Sit', 1.0), Func(self.clearToonTrack, avId), name=toon.uniqueName('fillElevator'), autoPause=1)
            track.delayDelete = DelayDelete.DelayDelete(toon, 'fillSlot')
            self.storeToonTrack(avId, track)
            track.start()
            self.boardedAvIds[avId] = None
        return

    def generateToonJumpTrack(self, av, seatIndex):
        av.pose('sit', 47)
        hipOffset = av.getHipsParts()[2].getPos(av)

        def getToonJumpTrack(av, seatIndex):

            def getJumpDest(av=av):
                dest = Point3(0, 0, 0)
                if hasattr(self, 'elevatorModel') and self.elevatorModel:
                    dest = Vec3(self.elevatorModel.getPos(av.getParent()))
                    seatNode = self.elevatorModel.find('**/seat' + str(seatIndex + 1))
                    dest += seatNode.getPos(self.elevatorModel)
                    dest -= hipOffset
                    if seatIndex < 2:
                        dest.setY(dest.getY() + 2 * hipOffset.getY())
                    dest.setZ(dest.getZ() + 0.1)
                else:
                    self.notify.warning('getJumpDestinvalid golfKart, returning (0,0,0)')
                return dest

            def getJumpHpr(av=av):
                hpr = Point3(0, 0, 0)
                if hasattr(self, 'elevatorModel') and self.elevatorModel:
                    hpr = self.elevatorModel.getHpr(av.getParent())
                    if seatIndex < 2:
                        hpr.setX(hpr.getX() + 180)
                    else:
                        hpr.setX(hpr.getX())
                    angle = PythonUtil.fitDestAngle2Src(av.getH(), hpr.getX())
                    hpr.setX(angle)
                else:
                    self.notify.warning('getJumpHpr invalid golfKart, returning (0,0,0)')
                return hpr

            toonJumpTrack = Parallel(ActorInterval(av, 'jump'), Sequence(Wait(0.43), Parallel(LerpHprInterval(av, hpr=getJumpHpr, duration=0.9), ProjectileInterval(av, endPos=getJumpDest, duration=0.9))))
            return toonJumpTrack

        def getToonSitTrack(av):
            toonSitTrack = Sequence(ActorInterval(av, 'sit-start'), Func(av.loop, 'sit'))
            return toonSitTrack

        toonJumpTrack = getToonJumpTrack(av, seatIndex)
        toonSitTrack = getToonSitTrack(av)
        jumpTrack = Sequence(Parallel(toonJumpTrack, Sequence(Wait(1), toonSitTrack)), Func(av.wrtReparentTo, self.golfKart))
        return jumpTrack

    def emptySlot(self, index, avId, bailFlag, timestamp):
        if avId == 0:
            pass
        elif not self.isSetup:
            newSlots = []
            for slot in self.deferredSlots:
                if slot[0] != index:
                    newSlots.append(slot)

            self.deferredSlots = newSlots
        elif avId in self.cr.doId2do:
            if bailFlag == 1 and hasattr(self, 'clockNode'):
                if timestamp < self.countdownTime and timestamp >= 0:
                    self.countdown(self.countdownTime - timestamp)
                else:
                    self.countdown(self.countdownTime)
            toon = self.cr.doId2do[avId]
            toon.stopSmooth()
            jumpOutTrack = self.generateToonReverseJumpTrack(toon, index)
            track = Sequence(jumpOutTrack, Func(self.clearToonTrack, avId), Func(self.notifyToonOffElevator, toon), name=toon.uniqueName('emptyElevator'), autoPause=1)
            track.delayDelete = DelayDelete.DelayDelete(toon, 'ClubElevator.emptySlot')
            self.storeToonTrack(avId, track)
            track.start()
            if avId == base.localAvatar.getDoId():
                messenger.send('exitElevator')
            if avId in self.boardedAvIds:
                del self.boardedAvIds[avId]
        else:
            self.notify.warning('toon: ' + str(avId) + " doesn't exist, and" + ' cannot exit the elevator!')

    def generateToonReverseJumpTrack(self, av, seatIndex):
        self.notify.debug('av.getH() = %s' % av.getH())

        def getToonJumpTrack(av, destNode):

            def getJumpDest(av = av, node = destNode):
                dest = node.getPos(av.getParent())
                dest += Vec3(*self.JumpOutOffsets[seatIndex])
                return dest

            toonJumpTrack = Parallel(ActorInterval(av, 'jump'), Sequence(Wait(0.1), Parallel(ProjectileInterval(av, endPos=getJumpDest, duration=0.9))))
            return toonJumpTrack

        toonJumpTrack = getToonJumpTrack(av, self.elevatorModel)
        jumpTrack = Sequence(toonJumpTrack, Func(av.loop, 'neutral'), Func(av.wrtReparentTo, render))
        return jumpTrack

    def startCountdownClock(self, countdownTime, ts):
        DistributedElevatorFloor.DistributedElevatorFloor.startCountdownClock(self, countdownTime, ts)
        self.clock.setH(self.clock.getH() + 180)

    def storeToonTrack(self, avId, track):
        self.clearToonTrack(avId)
        self.__toonTracks[avId] = track

    def clearToonTrack(self, avId):
        oldTrack = self.__toonTracks.get(avId)
        if oldTrack:
            oldTrack.pause()
            if self.__toonTracks.get(avId):
                DelayDelete.cleanupDelayDeletes(self.__toonTracks[avId])
                del self.__toonTracks[avId]

    def clearToonTracks(self):
        keyList = []
        for key in self.__toonTracks:
            keyList.append(key)

        for key in keyList:
            if key in self.__toonTracks:
                self.clearToonTrack(key)
