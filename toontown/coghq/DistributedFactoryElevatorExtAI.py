from toontown.building import DistributedElevatorExtAI


class DistributedFactoryElevatorExtAI(DistributedElevatorExtAI.DistributedElevatorExtAI):

    def __init__(self, air, bldg, factoryId, entranceId, antiShuffle = 0, minLaff = 0):
        DistributedElevatorExtAI.DistributedElevatorExtAI.__init__(self, air, bldg, antiShuffle=antiShuffle, minLaff=minLaff)
        self.factoryId = factoryId
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

            factoryZone = self.bldg.createFactory(self.factoryId, self.entranceId, players)
            for seatIndex in xrange(len(self.seats)):
                avId = self.seats[seatIndex]
                if avId:
                    self.sendUpdateToAvatarId(avId, 'setFactoryInteriorZone', [factoryZone])
                    self.clearFullNow(seatIndex)

        else:
            self.notify.warning('The elevator left, but was empty.')
        self.fsm.request('closed')
        return

    def enterClosed(self):
        DistributedElevatorExtAI.DistributedElevatorExtAI.enterClosed(self)
        self.fsm.request('opening')
