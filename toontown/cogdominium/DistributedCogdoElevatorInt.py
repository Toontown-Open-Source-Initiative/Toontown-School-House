from toontown.building.DistributedElevatorInt import DistributedElevatorInt

class DistributedCogdoElevatorInt(DistributedElevatorInt):

    def setupElevator(self):
        DistributedElevatorInt.setupElevator(self)
        self.elevatorSphereNodePath.setY(-1.0)
        self.elevatorSphereNodePath.setZ(1.5)

    def _getDoorsClosedInfo(self):
        return ('cogdoInterior', 'cogdoInterior')
