from direct.directnotify import DirectNotifyGlobal
import HoodDataAI
from toontown.toonbase import ToontownGlobals
from toontown.coghq import DistributedLawOfficeElevatorExtAI
from toontown.coghq import DistributedCogHQDoorAI
from toontown.building import DoorTypes
from toontown.coghq import LobbyManagerAI
from toontown.suit import DistributedLawbotBossAI
from toontown.building import DistributedCJElevatorAI
from toontown.building import FADoorCodes


class LawbotHQDataAI(HoodDataAI.HoodDataAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('LawbotHQDataAI')

    def __init__(self, air, zoneId=None):
        self.notify.debug('__init__: zoneId:%s' % zoneId)
        hoodId = ToontownGlobals.LawbotHQ
        if zoneId == None:
            zoneId = hoodId
        HoodDataAI.HoodDataAI.__init__(self, air, zoneId, hoodId)
        return

    def startup(self):
        HoodDataAI.HoodDataAI.startup(self)

        def makeOfficeElevator(index, antiShuffle=0, minLaff=0):
            destZone = (ToontownGlobals.LawbotStageIntA, ToontownGlobals.LawbotStageIntB, ToontownGlobals.LawbotStageIntC, ToontownGlobals.LawbotStageIntD)[index]
            elev = DistributedLawOfficeElevatorExtAI.DistributedLawOfficeElevatorExtAI(self.air, self.air.lawMgr, destZone, index, antiShuffle=antiShuffle, minLaff=minLaff)
            elev.generateWithRequired(ToontownGlobals.LawbotOfficeExt)
            self.addDistObj(elev)

        mins = ToontownGlobals.FactoryLaffMinimums[2]
        for i in range(len(mins)):
            makeOfficeElevator(i, 0, mins[i])

        self.lobbyMgr = LobbyManagerAI.LobbyManagerAI(self.air, DistributedLawbotBossAI.DistributedLawbotBossAI)
        self.lobbyMgr.generateWithRequired(ToontownGlobals.LawbotLobby)
        self.addDistObj(self.lobbyMgr)
        self.lobbyElevator = DistributedCJElevatorAI.DistributedCJElevatorAI(self.air, self.lobbyMgr, ToontownGlobals.LawbotLobby, antiShuffle=1)
        self.lobbyElevator.generateWithRequired(ToontownGlobals.LawbotLobby)
        self.addDistObj(self.lobbyElevator)

        def makeDoor(destinationZone, intDoorIndex, extDoorIndex, lock=0):
            intDoor = DistributedCogHQDoorAI.DistributedCogHQDoorAI(self.air, 0, DoorTypes.INT_COGHQ, self.canonicalHoodId, doorIndex=intDoorIndex, lockValue=lock)
            intDoor.zoneId = destinationZone
            extDoor = DistributedCogHQDoorAI.DistributedCogHQDoorAI(self.air, 0, DoorTypes.EXT_COGHQ, destinationZone, doorIndex=extDoorIndex, lockValue=lock)
            extDoor.setOtherDoor(intDoor)
            intDoor.setOtherDoor(extDoor)
            intDoor.generateWithRequired(destinationZone)
            intDoor.sendUpdate('setDoorIndex', [intDoor.getDoorIndex()])
            self.addDistObj(intDoor)
            extDoor.generateWithRequired(self.canonicalHoodId)
            extDoor.sendUpdate('setDoorIndex', [extDoor.getDoorIndex()])
            self.addDistObj(extDoor)

        makeDoor(ToontownGlobals.LawbotLobby, 0, 1, FADoorCodes.LB_DISGUISE_INCOMPLETE)
        makeDoor(ToontownGlobals.LawbotOfficeExt, 0, 0)
