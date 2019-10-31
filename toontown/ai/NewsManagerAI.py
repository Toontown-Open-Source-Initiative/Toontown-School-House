import datetime
import time

from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

from toontown.toonbase import ToontownGlobals


class NewsManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('NewsManagerAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.weeklyCalendarHolidays = []
        self.yearlyCalendarHolidays = []
        self.oncelyCalendarHolidays = []
        self.relativelyCalendarHolidays = []
        self.multipleStartHolidays = []

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)

        # Setup our weekly calendar holidays.
        self.setupWeeklyCalendarHolidays()

        # Setup our yearly calendar holidays.
        self.setupYearlyCalendarHolidays()

        # Setup our holiday manager.
        self.air.holidayManager.setup()

        # Setup our weekly calendar holiday task.
        taskMgr.add(self.__weeklyCalendarHolidayTask, self.uniqueName('weekly-calendar-holiday-task'))

        # Handle avatars entering the district.
        self.accept('avatarEntered', self.handleAvatarEntered)

    def delete(self):
        DistributedObjectAI.delete(self)
        taskMgr.remove(self.uniqueName('silly-saturday-task'))
        taskMgr.remove(self.uniqueName('start-silly-saturday-bingo'))
        taskMgr.remove(self.uniqueName('start-silly-saturday-circuit'))
        taskMgr.remove(self.uniqueName('start-weekly-calendar-holiday'))

    def handleAvatarEntered(self, av):
        if self.air.suitInvasionManager.getInvading():
            self.sendUpdateToAvatarId(av.getDoId(), 'setInvasionStatus', [ToontownGlobals.SuitInvasionBulletin,
                                                                          self.air.suitInvasionManager.invadingCog[0],
                                                                          self.air.suitInvasionManager.numSuits,
                                                                          self.air.suitInvasionManager.invadingCog[1]])

        if self.air.holidayManager.isHolidayRunning(ToontownGlobals.SILLY_SATURDAY_BINGO) or \
                self.air.holidayManager.isHolidayRunning(ToontownGlobals.SILLY_SATURDAY_CIRCUIT) or \
                self.air.holidayManager.isHolidayRunning(ToontownGlobals.SILLY_SATURDAY_TROLLEY) or \
                self.air.holidayManager.isHolidayRunning(ToontownGlobals.ROAMING_TRIALER_WEEKEND):
            self.sendUpdateToAvatarId(av.getDoId(), 'holidayNotify', [])

    def setupWeeklyCalendarHolidays(self):
        # Get our current list of weekly calendar holidays.
        weeklyCalendarHolidays = self.getWeeklyCalendarHolidays()[:]

        # These are the weekly events that run consistently each week.
        weeklyEvents = [
            # [holidayId, weekday]
            [ToontownGlobals.CIRCUIT_RACING, 0],  # Grand Prix Mondays
            [ToontownGlobals.FISH_BINGO_NIGHT, 2],  # Fish Bingo Wednesdays
            [ToontownGlobals.SILLY_SATURDAY_BINGO, 5]  # Silly Saturdays
        ]

        # If an event from weeklyEvents doesn't already exist in weeklyCalendarHolidays, add it.
        for weeklyEvent in weeklyEvents:
            if weeklyEvent not in weeklyCalendarHolidays:
                weeklyCalendarHolidays.append(weeklyEvent)

        self.b_setWeeklyCalendarHolidays(weeklyCalendarHolidays)

    def setupYearlyCalendarHolidays(self):
        # Get our current list of yearly calendar holidays.
        yearlyCalendarHolidays = self.getYearlyCalendarHolidays()[:]

        # These are the yearly events that run consistently each year.
        yearlyEvents = [
            # [holidayId, [startMonth, startDay, startHour, startMinute], [endMonth, endDay, endHour, endMinute]]
            [ToontownGlobals.VALENTINES_DAY, [2, 9, 0, 0], [2, 16, 23, 59]],
            [ToontownGlobals.IDES_OF_MARCH, [3, 14, 0, 0], [3, 20, 23, 59]],
            [ToontownGlobals.APRIL_FOOLS_COSTUMES, [3, 29, 0, 0], [4, 11, 23, 59]],
            [ToontownGlobals.JULY4_FIREWORKS, [6, 30, 0, 0], [7, 15, 23, 59]],
            [ToontownGlobals.HALLOWEEN_PROPS, [10, 25, 0, 0], [11, 1, 23, 59]],
            [ToontownGlobals.TRICK_OR_TREAT, [10, 25, 0, 0], [11, 1, 23, 59]],
            [ToontownGlobals.BLACK_CAT_DAY, [10, 31, 0, 0], [10, 31, 23, 59]],
            [ToontownGlobals.WINTER_DECORATIONS, [12, 14, 0, 0], [1, 4, 23, 59]],
            [ToontownGlobals.WINTER_CAROLING, [12, 16, 0, 0], [1, 4, 23, 59]],
            [ToontownGlobals.NEWYEARS_FIREWORKS, [12, 31, 0, 0], [1, 6, 23, 59]]
        ]

        # If an event from yearlyEvents doesn't already exist in yearlyCalendarHolidays, add it.
        for yearlyEvent in yearlyEvents:
            if yearlyEvent not in yearlyCalendarHolidays:
                yearlyCalendarHolidays.append(yearlyEvent)

        self.b_setYearlyCalendarHolidays(yearlyCalendarHolidays)

    def __weeklyCalendarHolidayTask(self, task):
        # If needed, these will hold the holiday IDs for holidays that we want to start and/or end.
        holidaysToStart = []
        holidaysToEnd = []

        # Get our current list of weekly calendar holidays.
        weeklyCalendarHolidays = self.getWeeklyCalendarHolidays()[:]

        # Get our current day of the week.
        currentWeekday = self.air.toontownTimeManager.getCurServerDateTime().now(
            tz=self.air.toontownTimeManager.serverTimeZone).weekday()

        # We will now loop through all of our weekly calendar holidays.
        for weeklyCalendarHoliday in weeklyCalendarHolidays:
            # If this particular holiday is Silly Saturday, perform some special logic.
            if weeklyCalendarHoliday[0] == ToontownGlobals.SILLY_SATURDAY_BINGO:
                # Check if the current day of the week matches the desired day of the week.
                if currentWeekday == weeklyCalendarHoliday[1]:
                    # It does, so let's get the current hour.
                    currentHour = self.air.toontownTimeManager.getCurServerDateTime().now(
                        tz=self.air.toontownTimeManager.serverTimeZone).hour

                    # Silly Saturday events rotate every two hours. Fish Bingo starts first at midnight for two hours,
                    # then Grand Prix, then the cycle repeats until the end of Saturday. Let's see if we should run
                    # Fish Bingo.
                    if not ((currentHour // 2) % 12) % 2:
                        # It's time for Fish Bingo! Let's see if it's already running.
                        if not self.air.holidayManager.isHolidayRunning(ToontownGlobals.SILLY_SATURDAY_BINGO):
                            # Looks like Fish Bingo isn't currently running! Now let's check to see if the Grand Prix
                            # is currently running or not.
                            if self.air.holidayManager.isHolidayRunning(ToontownGlobals.SILLY_SATURDAY_CIRCUIT):
                                # The Grand Prix is currently running. In that case, we want to end the Grand Prix,
                                # then wait 5 seconds before starting Fish Bingo.
                                self.air.holidayManager.endHoliday(ToontownGlobals.SILLY_SATURDAY_CIRCUIT)
                                taskMgr.doMethodLater(5, self.air.holidayManager.startHoliday,
                                                      self.uniqueName('start-silly-saturday-bingo'),
                                                      extraArgs=[ToontownGlobals.SILLY_SATURDAY_BINGO], appendTask=True)
                            else:
                                # The Grand Prix is currently not running. In that case, we can just go ahead and
                                # start Fish Bingo.
                                self.air.holidayManager.startHoliday(ToontownGlobals.SILLY_SATURDAY_BINGO)
                    else:
                        # It's time for the Grand Prix! Let's see if it's already running.
                        if not self.air.holidayManager.isHolidayRunning(ToontownGlobals.SILLY_SATURDAY_CIRCUIT):
                            # Looks like the Grand Prix isn't currently running! Now let's check to see if
                            # Fish Bingo is currently running or not.
                            if self.air.holidayManager.isHolidayRunning(ToontownGlobals.SILLY_SATURDAY_BINGO):
                                # Fish Bingo is currently running. In that case, we want to end Fish Bingo, then wait
                                # 5 seconds before starting the Grand Prix.
                                self.air.holidayManager.endHoliday(ToontownGlobals.SILLY_SATURDAY_BINGO)
                                taskMgr.doMethodLater(5, self.air.holidayManager.startHoliday,
                                                      self.uniqueName('start-silly-saturday-circuit'),
                                                      extraArgs=[ToontownGlobals.SILLY_SATURDAY_CIRCUIT],
                                                      appendTask=True)
                            else:
                                # Fish Bingo is currently not running. In that case, we can just go ahead and start
                                # the Grand Prix.
                                self.air.holidayManager.startHoliday(ToontownGlobals.SILLY_SATURDAY_CIRCUIT)

                    # Get the current epoch relative to the server's time zone.
                    currentEpoch = time.mktime(datetime.datetime.now(
                        tz=self.air.toontownTimeManager.serverTimeZone).timetuple()) + datetime.datetime.now(
                        tz=self.air.toontownTimeManager.serverTimeZone).microsecond * 1e-6

                    # We want this task to run again at the top of each hour.
                    task.delayTime = 3600.0 - (currentEpoch % 3600.0)
                    return task.again
                else:
                    # It does not, so we want to end any Silly Saturday holidays if they are still running.
                    # Let's check if Fish Bingo is currently running.
                    if self.air.holidayManager.isHolidayRunning(ToontownGlobals.SILLY_SATURDAY_BINGO):
                        # It is, so we will now end Fish Bingo.
                        self.air.holidayManager.endHoliday(ToontownGlobals.SILLY_SATURDAY_BINGO)

                    # Now let's check if the Grand Prix is currently running.
                    if self.air.holidayManager.isHolidayRunning(ToontownGlobals.SILLY_SATURDAY_CIRCUIT):
                        # It is, so we will now end the Grand Prix.
                        self.air.holidayManager.endHoliday(ToontownGlobals.SILLY_SATURDAY_CIRCUIT)
            else:
                # We've landed on a holiday other than Silly Saturday! These are a lot more straightforward.
                # Check if the current day of the week matches the desired day of the week.
                if currentWeekday == weeklyCalendarHoliday[1]:
                    # It does, so let's check if this holiday is currently running or not.
                    if not self.air.holidayManager.isHolidayRunning(weeklyCalendarHoliday[0]):
                        # It is not, so we will add it to holidaysToStart.
                        holidaysToStart.append(weeklyCalendarHoliday[0])
                else:
                    # It does not, so we want to end the holiday, so let's check if it's currently running or not.
                    if self.air.holidayManager.isHolidayRunning(weeklyCalendarHoliday[0]):
                        # It is, so we will add it to holidaysToEnd.
                        holidaysToEnd.append(weeklyCalendarHoliday[0])

        # We will now loop through all of our holidays that we want to end.
        for holidayToEnd in holidaysToEnd:
            # Let's check if this holiday is currently running or not.
            if self.air.holidayManager.isHolidayRunning(holidayToEnd):
                # It is, so let's end it.
                self.air.holidayManager.endHoliday(holidayToEnd)

        # We will now loop through all of our holidays that we want to start.
        for holidayToStart in holidaysToStart:
            # Let's check if this holiday is currently running or not.
            if not self.air.holidayManager.isHolidayRunning(holidayToStart):
                # It is not, so let's check if holidaysToEnd is not empty. If it isn't, then that means we just ended
                # one or more holidays. If this is the case, we want to delay the new holidays starting by 5 seconds.
                if holidaysToEnd:
                    # holidaysToEnd is not empty, so delay the holidays starting by 5 seconds.
                    taskMgr.doMethodLater(5, self.air.holidayManager.startHoliday,
                                          self.uniqueName('start-weekly-calendar-holiday'), extraArgs=[holidayToStart],
                                          appendTask=True)
                else:
                    # holidaysToEnd is empty, so we can just start the new holidays right away.
                    self.air.holidayManager.startHoliday(holidayToStart)

        # We want this task to run again at midnight. We'll calculate the seconds until midnight, then
        # delay the task from running again until then.
        tomorrow = self.air.toontownTimeManager.getCurServerDateTime().now(
            tz=self.air.toontownTimeManager.serverTimeZone) + datetime.timedelta(1)
        midnight = datetime.datetime(year=tomorrow.year, month=tomorrow.month, day=tomorrow.day, hour=0, minute=0,
                                     second=0, tzinfo=self.air.toontownTimeManager.serverTimeZone)
        secondsUntilMidnight = (midnight - self.air.toontownTimeManager.getCurServerDateTime().now(
            tz=self.air.toontownTimeManager.serverTimeZone)).seconds
        task.delayTime = secondsUntilMidnight
        return task.again

    def setWeeklyCalendarHolidays(self, weeklyCalendarHolidays):
        self.weeklyCalendarHolidays = weeklyCalendarHolidays

    def d_setWeeklyCalendarHolidays(self, weeklyCalendarHolidays):
        self.sendUpdate('setWeeklyCalendarHolidays', [weeklyCalendarHolidays])

    def b_setWeeklyCalendarHolidays(self, weeklyCalendarHolidays):
        self.setWeeklyCalendarHolidays(weeklyCalendarHolidays)
        self.d_setWeeklyCalendarHolidays(weeklyCalendarHolidays)

    def getWeeklyCalendarHolidays(self):
        return self.weeklyCalendarHolidays

    def setYearlyCalendarHolidays(self, yearlyCalendarHolidays):
        self.yearlyCalendarHolidays = yearlyCalendarHolidays

    def d_setYearlyCalendarHolidays(self, yearlyCalendarHolidays):
        self.sendUpdate('setYearlyCalendarHolidays', [yearlyCalendarHolidays])

    def b_setYearlyCalendarHolidays(self, yearlyCalendarHolidays):
        self.setYearlyCalendarHolidays(yearlyCalendarHolidays)
        self.d_setYearlyCalendarHolidays(yearlyCalendarHolidays)

    def getYearlyCalendarHolidays(self):
        return self.yearlyCalendarHolidays

    def setOncelyCalendarHolidays(self, oncelyCalendarHolidays):
        self.oncelyCalendarHolidays = oncelyCalendarHolidays

    def d_setOncelyCalendarHolidays(self, oncelyCalendarHolidays):
        self.sendUpdate('setOncelyCalendarHolidays', [oncelyCalendarHolidays])

    def b_setOncelyCalendarHolidays(self, oncelyCalendarHolidays):
        self.setOncelyCalendarHolidays(oncelyCalendarHolidays)
        self.d_setOncelyCalendarHolidays(oncelyCalendarHolidays)

    def getOncelyCalendarHolidays(self):
        return self.oncelyCalendarHolidays

    def setRelativelyCalendarHolidays(self, relativelyCalendarHolidays):
        self.relativelyCalendarHolidays = relativelyCalendarHolidays

    def d_setRelativelyCalendarHolidays(self, relativelyCalendarHolidays):
        self.sendUpdate('setRelativelyCalendarHolidays', [relativelyCalendarHolidays])

    def b_setRelativelyCalendarHolidays(self, relativelyCalendarHolidays):
        self.setRelativelyCalendarHolidays(relativelyCalendarHolidays)
        self.d_setRelativelyCalendarHolidays(relativelyCalendarHolidays)

    def getRelativelyCalendarHolidays(self):
        return self.relativelyCalendarHolidays

    def setMultipleStartHolidays(self, multipleStartHolidays):
        self.multipleStartHolidays = multipleStartHolidays

    def d_setMultipleStartHolidays(self, multipleStartHolidays):
        self.sendUpdate('setMultipleStartHolidays', [multipleStartHolidays])

    def b_setMultipleStartHolidays(self, multipleStartHolidays):
        self.setMultipleStartHolidays(multipleStartHolidays)
        self.d_setMultipleStartHolidays(multipleStartHolidays)

    def getMultipleStartHolidays(self):
        return self.multipleStartHolidays

    def d_setInvasionStatus(self, msgType, cogType, numRemaining, skeleton):
        self.sendUpdate('setInvasionStatus', [msgType, cogType, numRemaining, skeleton])

    def d_setHolidayIdList(self, holidayIdList):
        self.sendUpdate('setHolidayIdList', [holidayIdList])

    def d_setBingoStart(self):
        self.sendUpdate('setBingoStart')

    def d_setBingoEnd(self):
        self.sendUpdate('setBingoEnd')

    def d_setCircuitRaceStart(self):
        self.sendUpdate('setCircuitRaceStart')

    def d_setCircuitRaceEnd(self):
        self.sendUpdate('setCircuitRaceEnd')
