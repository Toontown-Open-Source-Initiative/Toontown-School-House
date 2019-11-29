from direct.directnotify.DirectNotifyGlobal import directNotify

from toontown.cogdominium.DistCogdoGame import DistCogdoGame
from toontown.cogdominium import CogdoCraneGameGlobals as Globals
from toontown.toonbase import TTLocalizer as TTL

from CogdoCraneGame import CogdoCraneGame


class DistCogdoCraneGame(DistCogdoGame):
    notify = directNotify.newCategory('DistCogdoCraneGame')

    def __init__(self, cr):
        DistCogdoGame.__init__(self, cr)
        self.game = CogdoCraneGame(self)
        self.cranes = {}
        self.moneyBags = {}

    def getTitle(self):
        return TTL.CogdoCraneGameTitle

    def getInstructions(self):
        return TTL.CogdoCraneGameInstructions

    def announceGenerate(self):
        DistCogdoGame.announceGenerate(self)

    def disable(self):
        DistCogdoGame.disable(self)
        return

    def enterLoaded(self):
        DistCogdoGame.enterLoaded(self)
        self.game.load()

    def exitLoaded(self):
        self.ignoreAll()
        self.game.unload()
        DistCogdoGame.exitLoaded(self)

    def toCraneMode(self):
        if self.cr:
            place = self.cr.playGame.getPlace()
            if place and hasattr(place, 'fsm'):
                place.setState('crane')

    def enterVisible(self):
        DistCogdoGame.enterVisible(self)
        self.game.geomRoot.reparentTo(render)

    def placeEntranceElev(self, elev):
        self.game.placeEntranceElevator(elev)

    def enterIntro(self):
        DistCogdoGame.enterIntro(self, Globals.IntroDurationSeconds)
        self.game.startIntro()

    def exitIntro(self):
        DistCogdoGame.exitIntro(self)
        self.game.endIntro()
        self.stashEntranceElevator()

    def enterGame(self):
        DistCogdoGame.enterGame(self)
        self.game.start()

    def exitGame(self):
        DistCogdoGame.exitGame(self)
        self.game.exit()

    def enterFinish(self):
        return
