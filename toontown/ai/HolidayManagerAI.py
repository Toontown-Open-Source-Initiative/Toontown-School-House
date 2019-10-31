from direct.directnotify import DirectNotifyGlobal

from toontown.toonbase import ToontownGlobals


class HolidayManagerAI:
    notify = DirectNotifyGlobal.directNotify.newCategory('HolidayManagerAI')

    def __init__(self, air):
        self.air = air
        self.currentHolidays = {}

    def setup(self):
        holidays = config.GetString('active-holidays', '')
        if holidays != '':
            for holiday in holidays.split(', '):
                holidayId = int(holiday)
                if holidayId not in self.currentHolidays:
                    self.currentHolidays[holidayId] = True

        if self.currentHolidays:
            self.air.newsManager.d_setHolidayIdList(self.currentHolidays.keys())

    def isHolidayRunning(self, holidayId):
        return holidayId in self.currentHolidays

    def isMoreXpHolidayRunning(self):
        if ToontownGlobals.MORE_XP_HOLIDAY in self.currentHolidays:
            return True

        return False

    def getCurPhase(self, holidayId):
        # TODO: Figure out how this works.
        return 1

    def startHoliday(self, holidayId, task=None):
        if holidayId not in self.currentHolidays:
            self.currentHolidays[holidayId] = True
            self.air.newsManager.d_setHolidayIdList(self.currentHolidays.keys())
            if holidayId == ToontownGlobals.SILLY_SATURDAY_BINGO:
                self.air.newsManager.d_setBingoStart()
            elif holidayId == ToontownGlobals.SILLY_SATURDAY_CIRCUIT:
                self.air.newsManager.d_setCircuitRaceStart()

        if task:
            return task.done

    def endHoliday(self, holidayId):
        if holidayId in self.currentHolidays:
            del self.currentHolidays[holidayId]
            self.air.newsManager.d_setHolidayIdList(self.currentHolidays.keys())
            if holidayId == ToontownGlobals.SILLY_SATURDAY_BINGO:
                self.air.newsManager.d_setBingoEnd()
            elif holidayId == ToontownGlobals.SILLY_SATURDAY_CIRCUIT:
                self.air.newsManager.d_setCircuitRaceEnd()
