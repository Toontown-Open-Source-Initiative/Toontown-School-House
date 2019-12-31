from toontown.building import DistributedElevatorExtAI


class DistributedLawOfficeElevatorExtAI(DistributedElevatorExtAI.DistributedElevatorExtAI):

    def __init__(self, air, bldg, lawOfficeId, entranceId, antiShuffle = 0, minLaff = 0):
        DistributedElevatorExtAI.DistributedElevatorExtAI.__init__(self, air, bldg, antiShuffle=antiShuffle, minLaff=minLaff)
        self.lawOfficeId = lawOfficeId
        self.entranceId = entranceId

    def getEntranceId(self):
        return self.entranceId

    def elevatorClosed(self):
        numPlayers = self.countFullSeats()
        if numPlayers > 0:
            players = []
            for i in self.seats:
                if i not in [None, 0]:
                    players.append(i)

            lawOfficeZone = self.bldg.createLawOffice(self.lawOfficeId, self.entranceId, players)
            for seatIndex in xrange(len(self.seats)):
                avId = self.seats[seatIndex]
                if avId:
                    self.sendUpdateToAvatarId(avId, 'setLawOfficeInteriorZone', [lawOfficeZone])
                    self.clearFullNow(seatIndex)

        else:
            self.notify.warning('The elevator left, but was empty.')
        self.fsm.request('closed')
        return

    def enterClosed(self):
        DistributedElevatorExtAI.DistributedElevatorExtAI.enterClosed(self)
        self.fsm.request('opening')
