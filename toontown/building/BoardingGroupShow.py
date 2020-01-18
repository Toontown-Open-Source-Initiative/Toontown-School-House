from panda3d.core import *
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals
from direct.task.Task import Task
from direct.interval.IntervalGlobal import *
from toontown.toonbase import TTLocalizer
from toontown.effects import DustCloud
TRACK_TYPE_TELEPORT = 1
TRACK_TYPE_POOF = 2

class BoardingGroupShow:
    notify = DirectNotifyGlobal.directNotify.newCategory('BoardingGroupShow')
    thresholdRunDistance = 25.0

    def __init__(self, toon):
        self.toon = toon
        self.avId = self.toon.doId
        self.dustCloudIval = None
        return

    def cleanup(self):
        if localAvatar.doId == self.avId:
            self.__stopTimer()
            self.clock.removeNode()

    def startTimer(self):
        self.clockNode = TextNode('elevatorClock')
        self.clockNode.setFont(ToontownGlobals.getSignFont())
        self.clockNode.setAlign(TextNode.ACenter)
        self.clockNode.setTextColor(0.5, 0.5, 0.5, 1)
        self.clockNode.setText(str(int(self.countdownDuration)))
        self.clock = aspect2d.attachNewNode(self.clockNode)
        self.clock.setPos(0, 0, -0.6)
        self.clock.setScale(0.15, 0.15, 0.15)
        self.__countdown(self.countdownDuration, self.__boardingTimerExpired)

    def __countdown(self, duration, callback):
        self.countdownTask = Task(self.__timerTask)
        self.countdownTask.duration = duration
        self.countdownTask.callback = callback
        taskMgr.remove(self.uniqueName(self.avId))
        return taskMgr.add(self.countdownTask, self.uniqueName(self.avId))

    def __timerTask(self, task):
        countdownTime = int(task.duration - task.time)
        timeStr = self.timeWarningText + str(countdownTime)
        if self.clockNode.getText() != timeStr:
            self.clockNode.setText(timeStr)
        if task.time >= task.duration:
            if task.callback:
                task.callback()
            return Task.done
        else:
            return Task.cont

    def __boardingTimerExpired(self):
        self.notify.debug('__boardingTimerExpired')
        self.clock.removeNode()

    def __stopTimer(self):
        if self.countdownTask:
            self.countdownTask.callback = None
            taskMgr.remove(self.countdownTask)
        return

    def uniqueName(self, avId):
        uniqueName = 'boardingTimerTask-' + str(avId)
        return uniqueName

    def getBoardingTrack(self, offset, wantToonRotation):
        self.timeWarningText = TTLocalizer.BoardingTimeWarning
        self.countdownDuration = 6
        trackType = TRACK_TYPE_TELEPORT
        boardingTrack = Sequence()
        if self.toon:
            if self.avId == localAvatar.doId:
                boardingTrack.append(Func(self.startTimer))
            if self.toon.isDisguised:
                boardingTrack.append(self.__getPoofTeleportTrack(offset, wantToonRotation))
                trackType = TRACK_TYPE_POOF
            else:
                boardingTrack.append(self.__getTeleportTrack(offset, wantToonRotation))
        boardingTrack.append(Func(self.cleanup))
        return boardingTrack, trackType

    def __getTeleportTrack(self, offset, wantToonRotation):
        teleportTrack = Sequence()
        if self.toon:
            if wantToonRotation:
                teleportTrack.append(Func(self.toon.headsUp, offset))
            teleportTrack.append(Func(self.toon.setAnimState, 'TeleportOut'))
            teleportTrack.append(Wait(3.5))
            teleportTrack.append(Func(self.toon.setPos, Point3(offset)))
            teleportTrack.append(Func(self.toon.setAnimState, 'TeleportIn'))
            teleportTrack.append(Wait(1))
        return teleportTrack

    def __getPoofTeleportTrack(self, offset, wantToonRotation):
        teleportTrack = Sequence()
        if wantToonRotation:
            teleportTrack.append(Func(self.toon.headsUp, offset))

        def getDustCloudPos():
            toonPos = self.toon.getPos(render)
            return Point3(toonPos.getX(), toonPos.getY(), toonPos.getZ() + 3)

        def cleanupDustCloudIval():
            if self.dustCloudIval:
                self.dustCloudIval.finish()
                self.dustCloudIval = None
            return

        def getDustCloudIval():
            cleanupDustCloudIval()
            dustCloud = DustCloud.DustCloud(fBillboard=0, wantSound=1)
            dustCloud.setBillboardAxis(2.0)
            dustCloud.setZ(3)
            dustCloud.setScale(0.4)
            dustCloud.createTrack()
            self.dustCloudIval = Sequence(Func(dustCloud.reparentTo, render), Func(dustCloud.setPos, getDustCloudPos()),
                                          dustCloud.track, Func(dustCloud.detachNode), Func(dustCloud.destroy),
                                          name='dustCloadIval')
            self.dustCloudIval.start()

        if self.toon:
            teleportTrack.append(Func(self.toon.setAnimState, 'neutral'))
            teleportTrack.append(Wait(0.5))
            teleportTrack.append(Func(getDustCloudIval))
            teleportTrack.append(Wait(0.25))
            teleportTrack.append(Func(self.toon.hide))
            teleportTrack.append(Wait(1.5))
            teleportTrack.append(Func(self.toon.setPos, Point3(offset)))
            teleportTrack.append(Func(getDustCloudIval))
            teleportTrack.append(Wait(0.25))
            teleportTrack.append(Func(self.toon.show))
            teleportTrack.append(Wait(0.5))
            teleportTrack.append(Func(cleanupDustCloudIval))
        return teleportTrack

    def getGoButtonShow(self, destName):
        self.destName = destName
        self.timeWarningText = TTLocalizer.BoardingGoShow % self.destName
        self.countdownDuration = 4
        goButtonShow = Sequence()
        if self.toon:
            if self.avId == localAvatar.doId:
                goButtonShow.append(Func(self.startTimer))
            goButtonShow.append(self.__getTeleportOutTrack())
            goButtonShow.append(Wait(3))
        goButtonShow.append(Func(self.cleanup))
        return goButtonShow

    def __getTeleportOutTrack(self):
        teleportOutTrack = Sequence()
        if self.toon and not self.toon.isDisguised:
            teleportOutTrack.append(Func(self.toon.b_setAnimState, 'TeleportOut'))
        return teleportOutTrack

    def getGoButtonPreShow(self):
        self.timeWarningText = TTLocalizer.BoardingGoPreShow
        self.countdownDuration = 4
        goButtonPreShow = Sequence()
        if self.toon:
            if self.avId == localAvatar.doId:
                goButtonPreShow.append(Func(self.startTimer))
                goButtonPreShow.append(Wait(3))
        goButtonPreShow.append(Func(self.cleanup))
        return goButtonPreShow
