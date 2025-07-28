from direct.showbase.PythonUtil import Enum, SingletonError
from toontown.ai.HolidayInfoDaily import *
from toontown.ai.HolidayInfoWeekly import *
from toontown.ai.HolidayInfoMonthly import *
from toontown.ai.HolidayInfoYearly import *
from toontown.effects import FireworkManagerAI
from toontown.fishing import BingoNightHolidayAI
from toontown.suit import HolidaySuitInvasionManagerAI
from toontown.ai import BlackCatHolidayMgrAI
from toontown.toonbase import ToontownGlobals
from toontown.racing import RaceManagerAI
Month = Enum('JANUARY, FEBRUARY, MARCH, APRIL, \
              MAY, JUNE, JULY, AUGUST, SEPTEMBER, \
              OCTOBER, NOVEMBER, DECEMBER', 1)

Day = Enum('MONDAY, TUESDAY, WEDNESDAY, THURSDAY, \
            FRIDAY, SATURDAY, SUNDAY')

Holidays = {
    ToontownGlobals.NEWYEARS_FIREWORKS : HolidayInfo_Yearly(
    FireworkManagerAI.FireworkManagerAI,
    [ (Month.DECEMBER, 31, 0o7, 0, 0),
      (Month.DECEMBER, 31, 22, 30, 0) ]
    ),

    ToontownGlobals.BLOODSUCKER_INVASION : HolidayInfo_Yearly(
    HolidaySuitInvasionManagerAI.HolidaySuitInvasionManagerAI,
    [ (Month.JANUARY, 8, 4, 0, 0),
      (Month.JANUARY, 8, 8, 0, 0) ]
    ),

    ToontownGlobals.MOVER_SHAKER_INVASION : HolidayInfo_Yearly(
    HolidaySuitInvasionManagerAI.HolidaySuitInvasionManagerAI,
    # February 15, 05:00 - February 15, 10:00
    [ (Month.FEBRUARY, 15, 5, 0, 0),
      (Month.FEBRUARY, 15, 10, 0, 0) ]
    ),

    ToontownGlobals.HEAD_HUNTER_INVASION : HolidayInfo_Yearly(
    HolidaySuitInvasionManagerAI.HolidaySuitInvasionManagerAI,
    [ (Month.MARCH, 19, 10, 0, 0),
      (Month.MARCH, 19, 13, 0, 0) ]
    ),

    ToontownGlobals.BLACK_CAT_DAY: HolidayInfo_Yearly(
    BlackCatHolidayMgrAI.BlackCatHolidayMgrAI,
    [
      (Month.FEBRUARY, 13, 20, 0, 1),
      (Month.FEBRUARY, 14, 19, 59, 59),
      (Month.MARCH, 13, 21, 0, 1),
      (Month.MARCH, 14, 20, 59, 59),
      (Month.JUNE, 13, 19, 0, 1),
      (Month.JUNE, 14, 18, 59, 59),
      (Month.AUGUST, 13, 21, 0, 1),
      (Month.AUGUST, 14, 20, 59, 59),
      (Month.OCTOBER, 13, 21, 0, 1),
      (Month.OCTOBER, 14, 20, 59, 59),
      (Month.OCTOBER, 30, 20, 0, 1),
      (Month.OCTOBER, 31, 20, 59, 59),
      (Month.DECEMBER, 13, 20, 0, 1),
      (Month.DECEMBER, 14, 19, 59, 59),
      ]
    ),

    ToontownGlobals.THE_MINGLER_INVASION : HolidayInfo_Yearly(
    HolidaySuitInvasionManagerAI.HolidaySuitInvasionManagerAI,
    [ (Month.APRIL, 3, 14, 0, 0),
      (Month.APRIL, 3, 19, 0, 0) ]
    ),

    ToontownGlobals.MONEY_BAGS_INVASION : HolidayInfo_Yearly(
    HolidaySuitInvasionManagerAI.HolidaySuitInvasionManagerAI,
    # PDT: May 12, 10:00 - May 12, 13:00
    [ (Month.MAY, 12, 10, 0, 0),
      (Month.MAY, 12, 13, 0, 0) ]
    ),

    ToontownGlobals.VALENTINES_FIREWORKS : HolidayInfo_Yearly(
    FireworkManagerAI.FireworkManagerAI,
    [ (Month.JUNE, 12, 20, 0, 0),
      (Month.JUNE, 13, 19, 30, 0) ]
    ),

    ToontownGlobals.TELEMARKETER_INVASION : HolidayInfo_Yearly(
    HolidaySuitInvasionManagerAI.HolidaySuitInvasionManagerAI,
    # PDT: July 9, 09:00 - July 9 14:00
    [ (Month.JULY, 9, 9, 0, 0),
      (Month.JULY, 9, 14, 0, 0) ]
    ),

    ToontownGlobals.BOTTOMFEEDER_INVASION : HolidayInfo_Yearly(
    HolidaySuitInvasionManagerAI.HolidaySuitInvasionManagerAI,
    # PDT: August 24, 06:00 - August 24, 11:00
    [ (Month.AUGUST, 24, 6, 0, 0),
      (Month.AUGUST, 24, 11, 0, 0) ]
    ),

    ToontownGlobals.AMBULANCE_CHASER_INVASION : HolidayInfo_Yearly(
    HolidaySuitInvasionManagerAI.HolidaySuitInvasionManagerAI,
    # PDT: September 8, 07:00 - September 8, 10:00
    [ (Month.SEPTEMBER, 8, 7, 0, 0),
      (Month.SEPTEMBER, 8, 10, 0, 0) ]
    ),

    ToontownGlobals.THE_BIG_CHEESE_INVASION : HolidayInfo_Yearly(
    HolidaySuitInvasionManagerAI.HolidaySuitInvasionManagerAI,
    # PDT: October 26, 07:00 - October 26, 12:00
    [ (Month.OCTOBER, 26, 7, 0, 0),
      (Month.OCTOBER, 26, 12, 0, 0) ]
    ),

    ToontownGlobals.NUMBER_CRUNCHER_INVASION : HolidayInfo_Yearly(
    HolidaySuitInvasionManagerAI.HolidaySuitInvasionManagerAI,
    # PST: November 17, 09:00 - November 17, 14:00
    [ (Month.NOVEMBER, 17, 9, 0, 0),
      (Month.NOVEMBER, 17, 14, 0, 0) ]
    ),

    ToontownGlobals.YESMAN_INVASION : HolidayInfo_Yearly(
    HolidaySuitInvasionManagerAI.HolidaySuitInvasionManagerAI,
    # PST: December 20, 08:00 - November 17, 13:00
    [ (Month.DECEMBER, 20, 8, 0, 0),
      (Month.DECEMBER, 20, 13, 0, 0) ]
    ),

    ToontownGlobals.WINTER_DECORATIONS : HolidayInfo_Yearly(
    None, # No class defined, we just want the news manager to be called
    # PST: December 6, 12:00 - December 25, 09:00
    [ (Month.DECEMBER, 6, 12, 0, 0),
      (Month.DECEMBER, 25, 9, 0, 0) ]
    ),

    ToontownGlobals.FISH_BINGO_NIGHT: HolidayInfo_Weekly(
    BingoNightHolidayAI.BingoNightHolidayAI,
    # Fish Bingo Night - runs twice a week
    [
    # Time1: 11am PST to 3pm PST on Wednesdays
      (Day.WEDNESDAY, 11, 0, 0),
      (Day.WEDNESDAY, 15, 0, 0),
    # Time2: 11am PST to 3pm PST on Saturdays
      (Day.SATURDAY, 11, 0, 0),
      (Day.SATURDAY, 15, 0, 0) ]
    ),

    ToontownGlobals.KART_RECORD_DAILY_RESET: HolidayInfo_Daily(
     RaceManagerAI.KartRecordDailyResetter,
     [(0, 24, 1),
      (0, 24, 30),
     ]
    ),
    ToontownGlobals.KART_RECORD_WEEKLY_RESET: HolidayInfo_Weekly(
     RaceManagerAI.KartRecordWeeklyResetter,
     [(Day.MONDAY, 0, 25, 1),
      (Day.MONDAY, 0, 25, 30),
     ]
    ),
    ToontownGlobals.CIRCUIT_RACING: HolidayInfo_Weekly(
     RaceManagerAI.CircuitRaceHolidayMgr,
     [(Day.SUNDAY, 0, 0, 1),
      (Day.SUNDAY, 23, 59, 59),
      (Day.MONDAY, 0, 0, 1),
      (Day.MONDAY, 23, 59, 59),
     ]
    )

}
