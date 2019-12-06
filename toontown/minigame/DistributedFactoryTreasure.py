from toontown.safezone import DistributedTreasure
from toontown.toonbase import ToontownGlobals
from toontown.battle import BattleProps
import random


class DistributedFactoryTreasure(DistributedTreasure.DistributedTreasure):

    def __init__(self, cr):
        DistributedTreasure.DistributedTreasure.__init__(self, cr)
        self.modelPath = BattleProps.globalPropPool.getProp(random.choice(ToontownGlobals.FactoryGameTreasureModels))
        self.grabSoundPath = 'phase_4/audio/sfx/SZ_DD_treasure.ogg'
        self.accept('minigameOffstage', self.handleMinigameOffstage)

    def handleEnterSphere(self, collEntry):
        self.d_requestGrab()
        return None

    def handleMinigameOffstage(self):
        self.nodePath.reparentTo(hidden)

    def loadModel(self, modelPath, modelFindString = None):
        self.grabSound = base.loader.loadSfx(self.grabSoundPath)
        self.rejectSound = base.loader.loadSfx(self.rejectSoundPath)
        if self.nodePath == None:
            self.makeNodePath()
        else:
            self.treasure.getChildren().detach()
        model = self.modelPath
        if modelFindString != None:
            model = model.find('**/' + modelFindString)
        model.instanceTo(self.treasure)
        return

