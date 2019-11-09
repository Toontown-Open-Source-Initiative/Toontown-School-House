from ElevatorConstants import *
SuitBuildingInfo = (((1, 1), (1, 3), (4, 4), (8, 10), (1,)), # 1 Story Building
 ((1, 2), (2, 4), (5, 5), (8, 10), (1, 1.2)), # Buildings
 ((1, 3), (3, 5), (6, 6), (8, 10), (1, 1.3, 1.6)), # Buildings
 ((2, 3), (4, 6), (7, 7), (8, 10), (1, 1.4, 1.8)), # Buildings
 ((2, 4), (5, 7), (8, 8), (8, 10), (1, 1.6, 1.8, 2)), # Buildings
 ((3, 4), (6, 8), (9, 9), (10, 12), (1, 1.6, 2, 2.4)), # Buildings
 ((3, 5), (7, 9),(10, 10), (10, 14), (1, 1.6, 1.8, 2.2, 2.4)), # Buildings
 ((4, 5), (8, 10), (11, 11), (12, 16), (1, 1.8, 2.4, 3, 3.2)), # Buildings
 ((5, 5), (9, 11), (12, 12), (14, 20), (1.4, 1.8, 2.6, 3.4, 4, 4.8)), # Buildings
 ((1, 1), (5, 12), (12, 12), (67, 67), (1, 1, 1, 1, 1)), # VP Cogs
 ((1, 1), (8, 12), (12, 12), (100, 100), (1, 1, 1, 1, 1)), # VP Skelecogs (round 2)
 ((1, 1), (5, 13), (13, 13), (150, 150), (1, 1, 1, 1, 1)), # CFO Cogs
 ((1, 1), (8, 13), (13, 13), (200, 200), (1, 1, 1, 1, 1)), # CFO Skelecogs
 ((1, 1), (5, 16), (16, 16), (300, 300), (1, 1, 1, 1, 1)), # CJ Cogs
 ((1, 1), (5, 18), (18, 18), (290, 290), (1, 1, 1, 1, 1)), # CEO Cogs
 ((1, 1), (1, 5), (5, 5), (33, 33), (1, 1, 1, 1, 1)), # Storm Sellbot VP Round 1
 ((1, 1), (4, 7), (5, 5), (50, 50), (1, 1, 1, 1, 1)), # Storm Sellbot VP Round 2
 ((1, 1), (11, 12), (12, 12), (206, 206), (1, 1, 1, 1, 1)), # CEO Diner Cogs (Only uses level range and revives flag, cogs are decided based on tables served)
 ((1, 1), (5, 16), (16, 16), (160, 160), (1, 1, 1, 1, 1)), # CJ Skelecogs
 ((1, 1), (5, 18), (16, 16), (160, 160), (1, 1, 1, 1, 1))) # CEO Skelecogs (unimplemented)
SUIT_BLDG_INFO_FLOORS = 0
SUIT_BLDG_INFO_SUIT_LVLS = 1
SUIT_BLDG_INFO_BOSS_LVLS = 2
SUIT_BLDG_INFO_LVL_POOL = 3
SUIT_BLDG_INFO_LVL_POOL_MULTS = 4
SUIT_BLDG_INFO_REVIVES = 5
VICTORY_RUN_TIME = ElevatorData[ELEVATOR_NORMAL]['openTime'] + TOON_VICTORY_EXIT_TIME
TO_TOON_BLDG_TIME = 8
VICTORY_SEQUENCE_TIME = VICTORY_RUN_TIME + TO_TOON_BLDG_TIME
CLEAR_OUT_TOON_BLDG_TIME = 4
TO_SUIT_BLDG_TIME = 8
