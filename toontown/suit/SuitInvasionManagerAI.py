from direct.directnotify import DirectNotifyGlobal

from toontown.toonbase import ToontownGlobals


class SuitInvasionManagerAI:
    notify = DirectNotifyGlobal.directNotify.newCategory('SuitInvasionManagerAI')

    def __init__(self, air):
        self.air = air
        self.invadingCog = (None, 0)
        self.numSuits = 0
        self.suits = 0
        self.invading = False

    def setInvadingCog(self, suitName, skeleton):
        self.invadingCog = (suitName, skeleton)

    def getInvadingCog(self):
        self.suits += 1
        self._checkInvasionStatus()
        return self.invadingCog

    def getInvading(self):
        return self.invading

    def _spGetOut(self):
        for suitPlanner in self.air.suitPlanners.values():
            suitPlanner.flySuits()

    def _checkInvasionStatus(self):
        if self.suits >= self.numSuits:
            self.stopInvasion()

    def stopInvasion(self, task=None):
        if not self.getInvading():
            return

        self.air.newsManager.d_setInvasionStatus(ToontownGlobals.SuitInvasionEnd, self.invadingCog[0], self.numSuits,
                                                 self.invadingCog[1])
        if task:
            task.remove()
        else:
            taskMgr.remove('invasion-timeout')

        self.setInvadingCog(None, 0)
        self.numSuits = 0
        self.suits = 0
        self.invading = False
        self._spGetOut()

    def startInvasion(self, cogType, numCogs, skeleton):
        if self.getInvading():
            return False

        self.numSuits = numCogs
        self.setInvadingCog(cogType, skeleton)
        self.invading = True
        self.air.newsManager.d_setInvasionStatus(ToontownGlobals.SuitInvasionBegin, self.invadingCog[0], self.numSuits,
                                                 self.invadingCog[1])
        self._spGetOut()
        timePerSuit = config.GetFloat('invasion-time-per-suit', 1.2)
        taskMgr.doMethodLater(self.numSuits * timePerSuit, self.stopInvasion, 'invasion-timeout')
        return True
