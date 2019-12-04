from panda3d.core import *
from direct.task.TaskManagerGlobal import *
from direct.distributed.ClockDelta import *
from direct.interval.IntervalGlobal import *
import GoonGlobals
from direct.task.Task import Task
from toontown.toonbase import ToontownGlobals
from otp.otpbase import OTPGlobals
from toontown.coghq import DistributedCashbotBossObjectAI
import DistributedCashbotBossGoonAI
from direct.showbase import PythonUtil
import DistributedGoonAI
import math
import random


class DistributedCashbotBossHardmodeGoonAI(DistributedCashbotBossGoonAI.DistributedCashbotBossGoonAI):

    def __init__(self, air, boss):
        DistributedCashbotBossGoonAI.DistributedCashbotBossGoonAI.__init__(self, air, boss)
        self.wantPickup = 0

    def enterGrabbed(self, avId, craneId):
        if not self.wantPickup:
            DistributedCashbotBossObjectAI.DistributedCashbotBossObjectAI.enterDropped(self, avId, craneId)
        DistributedCashbotBossObjectAI.DistributedCashbotBossObjectAI.enterGrabbed(self, avId, craneId)
        taskMgr.remove(self.taskName('recovery'))
        taskMgr.remove(self.taskName('resumeWalk'))

    def enterCogGoon(self):
        self.avId = 0
        self.craneId = 0
        h = -50
        dist = 4
        pos = (ToontownGlobals.CashbotBossHardmodeBattleThreeGoonLoopPosHpr[0], ToontownGlobals.CashbotBossHardmodeBattleThreeGoonLoopPosHpr[1], ToontownGlobals.CashbotBossHardmodeBattleThreeGoonLoopPosHpr[2])
        walkTime = dist / self.velocity
        self.setPosHpr(pos[0], pos[1], pos[2], h, 0, 0)
        self.d_setPosHpr(pos[0], pos[1], pos[2], h, 0, 0)
        self.target = self.boss.scene.getRelativePoint(self, Point3(0, dist, 0))
        self.departureTime = globalClock.getFrameTime()
        self.arrivalTime = self.departureTime + walkTime
        self.d_setTarget(self.target[0], self.target[1], h, globalClockDelta.localToNetworkTime(self.arrivalTime))
        self.__startWalk()
        self.d_setObjectState('a', 0, 0)
        taskMgr.doMethodLater(walkTime, self.__recoverWalk, self.uniqueName('recoverWalk'))

    def exitCogGoon(self):
        self.__stopWalk()
        taskMgr.remove(self.uniqueName('recoverWalk'))

    def requestInitial(self):
        avId = self.air.getAvatarIdFromSender()
        if avId == self.avId:
            self.demand('Initial')

    def enterInitial(self):
        self.toInitialPos()

    def exitInitial(self):
        pass

    def toInitialPos(self):
        self.demand('CogGoon')

    def requestBattle(self, pauseTime):
        avId = self.air.getAvatarIdFromSender()
        avatar = self.air.doId2do.get(avId)
        if avatar:
            self.boss.damageToon(avatar, self.strength)
        DistributedGoonAI.DistributedGoonAI.requestBattle(self, pauseTime)

    def sendMovie(self, type, avId=0, pauseTime=0):
        if type == GoonGlobals.GOON_MOVIE_WALK:
            self.demand('Walk')
        elif type == GoonGlobals.GOON_MOVIE_BATTLE:
            self.demand('Battle')
        elif type == GoonGlobals.GOON_MOVIE_STUNNED:
            self.demand('Stunned')
        elif type == GoonGlobals.GOON_MOVIE_RECOVERY:
            self.demand('Recovery')
        else:
            self.notify.warning('Ignoring movie type %s' % type)

    def __chooseTarget(self, extraDelay=0):
        direction = self.__chooseDirection()
        if direction == None:
            self.target = None
            self.arrivalTime = None
            self.b_destroyGoon()
            return
        heading, dist = direction
        dist = min(dist, self.legLength)
        targetH = PythonUtil.reduceAngle(self.getH() + heading)
        origH = self.getH()
        h = PythonUtil.fitDestAngle2Src(origH, targetH)
        delta = abs(h - origH)
        turnTime = delta / (self.velocity * 5)
        walkTime = dist / self.velocity
        self.setH(targetH)
        self.target = self.boss.scene.getRelativePoint(self, Point3(0, dist, 0))
        self.departureTime = globalClock.getFrameTime()
        self.arrivalTime = self.departureTime + turnTime + walkTime + extraDelay
        self.d_setTarget(self.target[0], self.target[1], h, globalClockDelta.localToNetworkTime(self.arrivalTime))
        return

    def __chooseDirection(self):
        self.tubeNode.setIntoCollideMask(self.offMask)
        self.cTrav.traverse(self.boss.scene)
        self.tubeNode.setIntoCollideMask(self.onMask)
        entries = {}
        self.cQueue.sortEntries()
        for i in xrange(self.cQueue.getNumEntries() - 1, -1, -1):
            entry = self.cQueue.getEntry(i)
            dist = Vec3(entry.getSurfacePoint(self)).length()
            if dist < 1.2:
                dist = 0
            entries[entry.getFrom()] = dist

        netScore = 0
        scoreTable = []
        for i in xrange(len(self.directionTable)):
            heading, weight = self.directionTable[i]
            seg = self.feelers[i]
            dist = entries.get(seg, self.feelerLength)
            score = dist * weight
            netScore += score
            scoreTable.append(score)

        if netScore == 0:
            self.notify.info('Could not find a path for %s' % self.doId)
            return None
        s = random.uniform(0, netScore)
        for i in xrange(len(self.directionTable)):
            s -= scoreTable[i]
            if s <= 0:
                heading, weight = self.directionTable[i]
                seg = self.feelers[i]
                dist = entries.get(seg, self.feelerLength)
                return (heading, dist)

        self.notify.warning('Fell off end of weighted table.')
        return (0, self.legLength)

    def __startWalk(self):
        if self.arrivalTime == None:
            return
        now = globalClock.getFrameTime()
        availableTime = self.arrivalTime - now
        if availableTime > 0:
            point = self.getRelativePoint(self.boss.scene, self.target)
            self.tube.setPointB(point)
            self.node().resetPrevTransform()
            taskMgr.doMethodLater(availableTime, self.__reachedTarget, self.uniqueName('reachedTarget'))
            self.isWalking = 1
        else:
            self.__reachedTarget(None)
        return

    def __stopWalk(self, pauseTime=None):
        if self.isWalking:
            taskMgr.remove(self.uniqueName('reachedTarget'))
            if pauseTime == None:
                now = globalClock.getFrameTime()
                t = (now - self.departureTime) / (self.arrivalTime - self.departureTime)
            else:
                t = pauseTime / (self.arrivalTime - self.departureTime)
            t = min(t, 1.0)
            pos = self.getPos()
            self.setPos(pos + (self.target - pos) * t)
            self.tube.setPointB(0, 0, 0)
            self.isWalking = 0
        return

    def __reachedTarget(self, task):
        self.__stopWalk()
        self.__chooseTarget()
        self.__startWalk()

    def __recoverWalk(self, task):
        self.demand('Walk')
        return Task.done

    def doFree(self, task):
        DistributedCashbotBossObjectAI.DistributedCashbotBossObjectAI.doFree(self, task)
        self.demand('Walk')
        return Task.done

    def requestStunned(self, pauseTime):
        avId = self.air.getAvatarIdFromSender()
        if simbase.air.doId2do.get(avId) is not self:
            if avId not in self.boss.involvedToons:
                return
        if self.state == 'Stunned' or self.state == 'Grabbed':
            return
        self.__stopWalk(pauseTime)
        self.boss.makeTreasure(self, guaranteed=1)
        DistributedGoonAI.DistributedGoonAI.requestStunned(self, pauseTime)

    def hitBoss(self, impact):
        avId = self.air.getAvatarIdFromSender()
        self.validate(avId, impact <= 1.0, 'invalid hitBoss impact %s' % impact)
        if avId not in self.boss.involvedToons:
            return
        if self.state == 'Dropped' or self.state == 'Grabbed':
            if not self.boss.heldObject:
                damage = int(impact * 25 * self.scale)
                self.boss.recordHit(max(damage, 2))
        self.b_destroyGoon()

    def d_setTarget(self, x, y, h, arrivalTime):
        self.sendUpdate('setTarget', [x,
                                      y,
                                      h,
                                      arrivalTime])

    def d_destroyGoon(self):
        self.sendUpdate('destroyGoon')

    def b_destroyGoon(self):
        self.d_destroyGoon()
        self.destroyGoon()

    def destroyGoon(self):
        self.requestStunned(6)

    def enterOff(self):
        self.tubeNodePath.stash()
        self.feelerNodePath.stash()

    def exitOff(self):
        self.tubeNodePath.unstash()
        self.feelerNodePath.unstash()

    def enterWalk(self):
        self.avId = 0
        self.craneId = 0
        self.__chooseTarget()
        self.__startWalk()
        self.d_setObjectState('W', 0, 0)

    def exitWalk(self):
        self.__stopWalk()

    def enterEmergeA(self):
        self.avId = 0
        self.craneId = 0
        h = 0
        dist = 15
        pos = self.boss.getPos()
        walkTime = dist / self.velocity
        self.setPosHpr(pos[0], pos[1], pos[2], h, 0, 0)
        self.d_setPosHpr(pos[0], pos[1], pos[2], h, 0, 0)
        self.target = self.boss.scene.getRelativePoint(self, Point3(0, dist, 0))
        self.departureTime = globalClock.getFrameTime()
        self.arrivalTime = self.departureTime + walkTime
        self.d_setTarget(self.target[0], self.target[1], h, globalClockDelta.localToNetworkTime(self.arrivalTime))
        self.__startWalk()
        self.d_setObjectState('a', 0, 0)
        taskMgr.doMethodLater(walkTime, self.__recoverWalk, self.uniqueName('recoverWalk'))

    def exitEmergeA(self):
        self.__stopWalk()
        taskMgr.remove(self.uniqueName('recoverWalk'))

    def enterEmergeB(self):
        self.avId = 0
        self.craneId = 0
        h = 180
        dist = 15
        pos = self.boss.getPos()
        walkTime = dist / self.velocity
        self.setPosHpr(pos[0], pos[1], pos[2], h, 0, 0)
        self.d_setPosHpr(pos[0], pos[1], pos[2], h, 0, 0)
        self.target = self.boss.scene.getRelativePoint(self, Point3(0, dist, 0))
        self.departureTime = globalClock.getFrameTime()
        self.arrivalTime = self.departureTime + walkTime
        self.d_setTarget(self.target[0], self.target[1], h, globalClockDelta.localToNetworkTime(self.arrivalTime))
        self.__startWalk()
        self.d_setObjectState('b', 0, 0)
        taskMgr.doMethodLater(walkTime, self.__recoverWalk, self.uniqueName('recoverWalk'))

    def exitEmergeB(self):
        self.__stopWalk()
        taskMgr.remove(self.uniqueName('recoverWalk'))

    def enterBattle(self):
        self.d_setObjectState('B', 0, 0)

    def exitBattle(self):
        taskMgr.remove(self.taskName('resumeWalk'))

    def enterStunned(self):
        self.d_setObjectState('S', 0, 0)

    def exitStunned(self):
        taskMgr.remove(self.taskName('recovery'))

    def enterRecovery(self):
        self.d_setObjectState('R', 0, 0)
        taskMgr.doMethodLater(2.0, self.__recoverWalk, self.uniqueName('recoverWalk'))

    def exitRecovery(self):
        self.__stopWalk()
        taskMgr.remove(self.uniqueName('recoverWalk'))
