from toontown.building import ElevatorConstants
from toontown.building import DistributedElevatorFloorAI
from direct.directnotify import DirectNotifyGlobal


class DistributedClubElevatorAI(DistributedElevatorFloorAI.DistributedElevatorFloorAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedElevatorFloorAI')
    DoBlockedRoomCheck = simbase.config.GetBool('elevator-blocked-rooms-check', 1)

    def __init__(self, air, lawOfficeId, bldg, avIds, markerId=None, numSeats=4, antiShuffle=0, minLaff=0):
        DistributedElevatorFloorAI.DistributedElevatorFloorAI.__init__(self, air, lawOfficeId, bldg, avIds, markerId, numSeats, antiShuffle, minLaff)
        self.type = ElevatorConstants.ELEVATOR_COUNTRY_CLUB

    def checkBoard(self, av):
        if av.hp < self.minLaff:
            return ElevatorConstants.REJECT_MINLAFF
        if self.DoBlockedRoomCheck and self.bldg:
            if hasattr(self.bldg, 'blockedRooms'):
                if self.bldg.blockedRooms:
                    return ElevatorConstants.REJECT_BLOCKED_ROOM
        return 0
