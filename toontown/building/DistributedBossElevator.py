from panda3d.core import *
from ElevatorUtils import *
import DistributedElevator
import DistributedElevatorExt
from toontown.toonbase import TTLocalizer


class DistributedBossElevator(DistributedElevatorExt.DistributedElevatorExt):

    def __init__(self, cr):
        DistributedElevatorExt.DistributedElevatorExt.__init__(self, cr)
        self.elevatorPoints = BigElevatorPoints
        self.openSfx = base.loader.loadSfx('phase_9/audio/sfx/CHQ_FACT_door_open_sliding.ogg')
        self.finalOpenSfx = base.loader.loadSfx('phase_9/audio/sfx/CHQ_FACT_door_open_final.ogg')
        self.closeSfx = base.loader.loadSfx('phase_9/audio/sfx/CHQ_FACT_door_open_sliding.ogg')
        self.finalCloseSfx = base.loader.loadSfx('phase_9/audio/sfx/CHQ_FACT_door_open_final.ogg')
        self.type = ELEVATOR_VP
        self.countdownTime = ElevatorData[self.type]['countdown']

    def disable(self):
        DistributedElevator.DistributedElevator.disable(self)

    def generate(self):
        DistributedElevatorExt.DistributedElevatorExt.generate(self)

    def delete(self):
        self.elevatorModel.removeNode()
        del self.elevatorModel
        DistributedElevatorExt.DistributedElevatorExt.delete(self)

    def setupElevator(self):
        self.elevatorModel = loader.loadModel('phase_9/models/cogHQ/cogHQ_elevator')
        icon = self.elevatorModel.find('**/big_frame/')
        icon.hide()
        self.leftDoor = self.elevatorModel.find('**/left-door')
        self.rightDoor = self.elevatorModel.find('**/right-door')
        geom = base.cr.playGame.hood.loader.geom
        locator = geom.find('**/elevator_locator')
        self.elevatorModel.reparentTo(locator)
        self.elevatorModel.setH(180)
        DistributedElevator.DistributedElevator.setupElevator(self)

    def getElevatorModel(self):
        return self.elevatorModel

    def gotBldg(self, buildingList):
        return DistributedElevator.DistributedElevator.gotBldg(self, buildingList)

    def getZoneId(self):
        return 0

    def __doorsClosed(self, zoneId):
        pass

    def setBossOfficeZone(self, zoneId):
        if self.localToonOnBoard:
            hoodId = self.cr.playGame.hood.hoodId
            doneStatus = {'loader': 'cogHQLoader',
             'where': 'cogHQBossBattle',
             'how': 'movie',
             'zoneId': zoneId,
             'hoodId': hoodId}
            self.cr.playGame.getPlace().elevator.signalDone(doneStatus)
