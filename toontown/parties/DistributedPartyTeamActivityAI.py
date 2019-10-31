from direct.directnotify import DirectNotifyGlobal
from toontown.parties.DistributedPartyActivityAI import DistributedPartyActivityAI

class DistributedPartyTeamActivityAI(DistributedPartyActivityAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedPartyTeamActivityAI")

    def toonJoinRequest(self, todo0):
        pass

    def toonExitRequest(self, todo0):
        pass

    def toonSwitchTeamRequest(self):
        pass

    def setPlayersPerTeam(self, todo0, todo1):
        pass

    def setDuration(self, todo0):
        pass

    def setCanSwitchTeams(self, todo0):
        pass

    def setState(self, todo0, todo1, todo2):
        pass

    def setToonsPlaying(self, todo0, todo1):
        pass

    def setAdvantage(self, todo0):
        pass

    def switchTeamRequestDenied(self, todo0):
        pass

