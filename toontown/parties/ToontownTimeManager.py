import time
from datetime import datetime, timedelta, tzinfo
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import TTLocalizer


class ToontownTimeZone(tzinfo):
    """
    A simple implementation of US/Pacific time (UTC-08:00) that is only able to calculate
    correct DST for dates post-2006, which is perfectly acceptable for our use case.
    """
    offset = -8
    dstBegin = datetime(1, 3, 8, 2)  # DST begins on the second Sunday of March.
    dstEnd = datetime(1, 11, 1, 1)  # DST ends on the first Sunday of November.
    names = ('PST', 'PDT')

    @staticmethod
    def forwardToSunday(dt):
        daysToGo = 6 - dt.weekday()
        if daysToGo:
            dt += timedelta(daysToGo)

        return dt

    def dst(self, dt):
        # Determine if DST is active for the dt.
        beginning = self.forwardToSunday(self.dstBegin.replace(year=dt.year))
        ending = self.forwardToSunday(self.dstEnd.replace(year=dt.year))
        if beginning <= dt.replace(tzinfo=None) < ending:
            return timedelta(hours=1)
        else:
            return timedelta(0)

    def utcoffset(self, dt):
        offset = timedelta(hours=self.offset)
        offset += self.dst(dt)
        return offset

    def tzname(self, dt):
        standardName, dstName = self.names
        if self.dst(dt):
            return dstName
        else:
            return standardName


class UTC(tzinfo):
    """
    A very simple UTC implementation.
    """

    def utcoffset(self, dt):
        return timedelta(0)

    def tzname(self, dt):
        return 'UTC'

    def dst(self, dt):
        return timedelta(0)


class ToontownTimeManager:
    notify = DirectNotifyGlobal.directNotify.newCategory('ToontownTimeManager')
    ClockFormat = '%I:%M:%S %p'
    formatStr = '%Y-%m-%d %H:%M:%S'

    def __init__(self, serverTimeUponLogin = 0, clientTimeUponLogin = 0, globalClockRealTimeUponLogin = 0):
        try:
            self.serverTimeZoneString = base.config.GetString('server-timezone', TTLocalizer.TimeZone)
        except:
            try:
                self.serverTimeZoneString = simbase.config.GetString('server-timezone', TTLocalizer.TimeZone)
            except:
                notify.error('ToontownTimeManager does not have access to base or simbase.')

        if self.serverTimeZoneString == 'US/Pacific':
            self.serverTimeZone = ToontownTimeZone()
        else:
            self.notify.error('Time Zone %s is not supported.' % self.serverTimeZoneString)

        self.updateLoginTimes(serverTimeUponLogin, clientTimeUponLogin, globalClockRealTimeUponLogin)
        self.debugSecondsAdded = 0

    def updateLoginTimes(self, serverTimeUponLogin, clientTimeUponLogin, globalClockRealTimeUponLogin):
        self.serverTimeUponLogin = serverTimeUponLogin
        self.clientTimeUponLogin = clientTimeUponLogin
        self.globalClockRealTimeUponLogin = globalClockRealTimeUponLogin
        self.serverDateTime = datetime.fromtimestamp(self.serverTimeUponLogin, self.serverTimeZone)

    def getCurServerDateTime(self):
        secondsPassed = globalClock.getRealTime() - self.globalClockRealTimeUponLogin + self.debugSecondsAdded
        curDateTime = (self.serverDateTime + timedelta(seconds=secondsPassed)).astimezone(self.serverTimeZone)
        return curDateTime

    def getRelativeServerDateTime(self, timeOffset):
        secondsPassed = globalClock.getRealTime() - self.globalClockRealTimeUponLogin + self.debugSecondsAdded
        secondsPassed += timeOffset
        curDateTime = (self.serverDateTime + timedelta(seconds=secondsPassed)).astimezone(self.serverTimeZone)
        return curDateTime

    def getCurServerDateTimeForComparison(self):
        secondsPassed = globalClock.getRealTime() - self.globalClockRealTimeUponLogin + self.debugSecondsAdded
        curDateTime = self.serverDateTime + timedelta(seconds=secondsPassed)
        curDateTime = curDateTime.replace(tzinfo=self.serverTimeZone)
        return curDateTime

    def getCurServerTimeStr(self):
        curDateTime = self.getCurServerDateTime()
        result = curDateTime.strftime(self.ClockFormat)
        if result[0] == '0':
            result = result[1:]
        return result

    def setDebugSecondsAdded(self, moreSeconds):
        self.debugSecondsAdded = moreSeconds

    def debugTest(self):
        startTime = datetime.today()
        serverTzInfo = self.serverTimeZone
        startTime = startTime.replace(tzinfo=serverTzInfo)
        self.notify.info('startTime = %s' % startTime)
        serverTime = self.getCurServerDateTime()
        self.notify.info('serverTime = %s' % serverTime)
        result = startTime <= serverTime
        self.notify.info('start < serverTime %s' % result)
        startTime1MinAgo = startTime + timedelta(minutes=-1)
        self.notify.info('startTime1MinAgo = %s' % startTime1MinAgo)
        result2 = startTime1MinAgo <= serverTime
        self.notify.info('startTime1MinAgo < serverTime %s' % result2)
        serverTimeForComparison = self.getCurServerDateTimeForComparison()
        self.notify.info('serverTimeForComparison = %s' % serverTimeForComparison)
        result3 = startTime1MinAgo <= serverTimeForComparison
        self.notify.info('startTime1MinAgo < serverTimeForComparison %s' % result3)

    def convertStrToToontownTime(self, dateStr):
        curDateTime = self.getCurServerDateTime()
        try:
            curDateTime = datetime.fromtimestamp(time.mktime(time.strptime(dateStr, self.formatStr)), self.serverTimeZone)
        except:
            self.notify.warning('error parsing date string=%s' % dateStr)

        result = curDateTime
        return result

    def convertUtcStrToToontownTime(self, dateStr):
        curDateTime = self.getCurServerDateTime()
        try:
            timeTuple = time.strptime(dateStr, self.formatStr)
            utcDateTime = datetime(timeTuple[0], timeTuple[1], timeTuple[2], timeTuple[3], timeTuple[4], timeTuple[5], timeTuple[6], UTC())
            curDateTime = utcDateTime.astimezone(self.serverTimeZone)
        except:
            self.notify.warning('error parsing date string=%s' % dateStr)

        result = curDateTime
        return result
