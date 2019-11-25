from direct.directnotify import DirectNotifyGlobal
import HoodDataAI
from toontown.toonbase import ToontownGlobals
from toontown.coghq import DistributedMintElevatorExtAI
from toontown.coghq import DistributedCogHQDoorAI
from toontown.building import DoorTypes
from toontown.coghq import LobbyManagerAI
from toontown.building import DistributedCFOElevatorAI
from toontown.suit import DistributedCashbotBossAI
from toontown.building import DistributedCAOElevatorAI
from toontown.suit import DistributedCashbotBossHardmodeAI
from toontown.building import FADoorCodes
from toontown.building import DistributedBoardingPartyAI

class CashbotHQDataAI(HoodDataAI.HoodDataAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('CashbotHqDataAI')

    def __init__(self, air, zoneId=None):
        hoodId = ToontownGlobals.CashbotHQ
        if zoneId == None:
            zoneId = hoodId
        HoodDataAI.HoodDataAI.__init__(self, air, zoneId, hoodId)
        return

    def startup(self):
        HoodDataAI.HoodDataAI.startup(self)
        mins = ToontownGlobals.FactoryLaffMinimums[1]
        self.testElev0 = DistributedMintElevatorExtAI.DistributedMintElevatorExtAI(self.air, self.air.mintMgr, ToontownGlobals.CashbotMintIntA, antiShuffle=0, minLaff=mins[0])
        self.testElev0.generateWithRequired(ToontownGlobals.CashbotHQ)
        self.addDistObj(self.testElev0)
        self.testElev1 = DistributedMintElevatorExtAI.DistributedMintElevatorExtAI(self.air, self.air.mintMgr, ToontownGlobals.CashbotMintIntB, antiShuffle=0, minLaff=mins[1])
        self.testElev1.generateWithRequired(ToontownGlobals.CashbotHQ)
        self.addDistObj(self.testElev1)
        self.testElev2 = DistributedMintElevatorExtAI.DistributedMintElevatorExtAI(self.air, self.air.mintMgr, ToontownGlobals.CashbotMintIntC, antiShuffle=0, minLaff=mins[2])
        self.testElev2.generateWithRequired(ToontownGlobals.CashbotHQ)
        self.addDistObj(self.testElev2)
        self.lobbyMgr = LobbyManagerAI.LobbyManagerAI(self.air, DistributedCashbotBossAI.DistributedCashbotBossAI)
        self.lobbyMgr.generateWithRequired(ToontownGlobals.CashbotLobby)
        self.addDistObj(self.lobbyMgr)
        self.lobbyMgrHardmode = LobbyManagerAI.LobbyManagerAI(self.air, DistributedCashbotBossHardmodeAI.DistributedCashbotBossHardmodeAI)
        self.lobbyMgrHardmode.generateWithRequired(ToontownGlobals.CashbotLobbyHardmode)
        self.addDistObj(self.lobbyMgrHardmode)
        self.lobbyElevator = DistributedCFOElevatorAI.DistributedCFOElevatorAI(self.air, self.lobbyMgr, ToontownGlobals.CashbotLobby, antiShuffle=1)
        self.lobbyElevator.generateWithRequired(ToontownGlobals.CashbotLobby)
        self.addDistObj(self.lobbyElevator)
        self.lobbyElevatorHardmode = DistributedCAOElevatorAI.DistributedCAOElevatorAI(self.air, self.lobbyMgrHardmode, ToontownGlobals.CashbotLobbyHardmode, antiShuffle=1)
        self.lobbyElevatorHardmode.generateWithRequired(ToontownGlobals.CashbotLobbyHardmode)
        self.addDistObj(self.lobbyElevatorHardmode)
        if simbase.config.GetBool('want-boarding-groups', 1):
            self.boardingParty = DistributedBoardingPartyAI.DistributedBoardingPartyAI(self.air, [self.lobbyElevator.doId], 8)
            self.boardingParty.generateWithRequired(ToontownGlobals.CashbotLobby)
        destinationZone = ToontownGlobals.CashbotLobby
        extDoor0 = DistributedCogHQDoorAI.DistributedCogHQDoorAI(self.air, 0, DoorTypes.EXT_COGHQ, destinationZone, doorIndex=0, lockValue=FADoorCodes.CB_DISGUISE_INCOMPLETE)
        extDoor1 = DistributedCogHQDoorAI.DistributedCogHQDoorAI(self.air, 0, DoorTypes.INT_COGHQ, ToontownGlobals.CashbotLobbyHardmode, doorIndex=0)
        extDoorList = [
         extDoor0, extDoor1]
        intDoor0 = DistributedCogHQDoorAI.DistributedCogHQDoorAI(self.air, 0, DoorTypes.INT_COGHQ, ToontownGlobals.CashbotHQ, doorIndex=0)
        intDoor0.setOtherDoor(extDoor0)
        intDoor0.zoneId = ToontownGlobals.CashbotLobby
        intDoor1 = DistributedCogHQDoorAI.DistributedCogHQDoorAI(self.air, 0, DoorTypes.INT_COGHQ, destinationZone, doorIndex=0)
        mintIdList = [
         self.testElev0.doId, self.testElev1.doId, self.testElev2.doId]
        if simbase.config.GetBool('want-boarding-groups', 1):
            self.mintBoardingParty = DistributedBoardingPartyAI.DistributedBoardingPartyAI(self.air, mintIdList, 4)
            self.mintBoardingParty.generateWithRequired(self.zoneId)
        extDoor0.setOtherDoor(intDoor0)
        extDoor0.zoneId = ToontownGlobals.CashbotHQ
        extDoor0.generateWithRequired(ToontownGlobals.CashbotHQ)
        extDoor0.sendUpdate('setDoorIndex', [extDoor0.getDoorIndex()])
        self.addDistObj(extDoor0)

        extDoor1.setOtherDoor(intDoor1)
        extDoor1.zoneId = ToontownGlobals.CashbotLobby
        extDoor1.generateWithRequired(ToontownGlobals.CashbotLobby)
        extDoor1.sendUpdate('setDoorIndex', [extDoor1.getDoorIndex()])
        self.addDistObj(extDoor1)

        intDoor0.generateWithRequired(ToontownGlobals.CashbotLobby)
        intDoor0.sendUpdate('setDoorIndex', [intDoor0.getDoorIndex()])
        intDoor1.generateWithRequired((ToontownGlobals.CashbotLobbyHardmode))
        intDoor1.sendUpdate('setDoorIndex', [intDoor1.getDoorIndex()])
        self.addDistObj(intDoor0)
        self.addDistObj(intDoor1)
