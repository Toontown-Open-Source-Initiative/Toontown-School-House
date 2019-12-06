from panda3d.core import *
from panda3d.direct import *
from toontown.safezone import DistributedTreasure
from direct.distributed import DistributedObject
from toontown.toonbase import ToontownGlobals
import FactoryGameGlobals
from toontown.battle import BattleProps
import random
from direct.interval.IntervalGlobal import *


class DistributedFactoryTreasure(DistributedTreasure.DistributedTreasure):

    def __init__(self, cr):
        DistributedTreasure.DistributedTreasure.__init__(self, cr)
        self.modelPath = BattleProps.globalPropPool.getProp(random.choice(FactoryGameGlobals.FactoryGameTreasureModels))
        self.radius = self.modelPath.getBounds().getRadius()
        self.grabSoundPath = 'phase_4/audio/sfx/SZ_DD_treasure.ogg'
        self.animateTrack = None
        self.zOffset = 1.25
        self.modelScaler = BattleProps.globalPropPool.getProp(FactoryGameGlobals.FactoryGameModelForScale)
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

    def handleGrab(self, avId):
        self.collNodePath.stash()
        self.avId = avId
        if avId in self.cr.doId2do:
            av = self.cr.doId2do[avId]
            self.av = av
        else:
            self.nodePath.detachNode()
            return
        if self.playSoundForRemoteToons or self.avId == base.localAvatar.getDoId():
            base.playSfx(self.grabSound, node=self.nodePath)
        if not self.fly:
            self.nodePath.detachNode()
            return
        self.nodePath.wrtReparentTo(av)
        if self.treasureFlyTrack:
            self.treasureFlyTrack.finish()
            self.treasureFlyTrack = None
        if self.animateTrack:
            self.animateTrack.finish()
            self.animateTrack = None
        avatarGoneName = self.av.uniqueName('disable')
        self.accept(avatarGoneName, self.handleUnexpectedExit)
        flytime = 1.0
        track = Sequence(LerpPosInterval(self.nodePath, flytime, pos=Point3(0, 0, 3), startPos=self.nodePath.getPos(), blendType='easeInOut'), Func(self.nodePath.detachNode), Func(self.ignore, avatarGoneName))
        if self.shadow:
            self.treasureFlyTrack = Sequence(HideInterval(self.dropShadow), track, ShowInterval(self.dropShadow), name=self.uniqueName('treasureFlyTrack'))
        else:
            self.treasureFlyTrack = Sequence(track, name=self.uniqueName('treasureFlyTrack'))
        self.treasureFlyTrack.start()
        return

    def setPosition(self, x, y, z):
        if not self.nodePath:
            self.makeNodePath()
        self.nodePath.reparentTo(self.getParentNodePath())
        self.nodePath.setPos(x, y, z)
        self.treasure.setPos(0, 0, self.zOffset)
        self.collNodePath.unstash()
        self.__makeAnimation()

    def __makeAnimation(self):
        self.__scaleModel()
        spinTrack = LerpHprInterval(self.treasure, 8, (0, 0, 0), (360, 0, 0))
        startPos = self.treasure.getPos()
        endPos = startPos + Point3(0, 0, 1)
        floatTrack = Sequence(LerpPosInterval(self.treasure, 4, endPos, startPos=startPos, blendType='easeInOut'), LerpPosInterval(self.treasure, 4, startPos, endPos, blendType='easeInOut'))
        self.animateTrack = Parallel(spinTrack, floatTrack)
        self.animateTrack.loop()

    def __scaleModel(self):
        bounds = self.modelScaler.getBounds()
        radius = bounds.getRadius()
        self.treasure.setScale(radius / self.radius)
        self.modelScaler.detachNode()
        self.modelScaler = None
        del self.modelScaler

    def delete(self):
        if self.treasureFlyTrack:
            self.treasureFlyTrack.finish()
            self.treasureFlyTrack = None
        if self.animateTrack:
            self.animateTrack.finish()
            self.animateTrack = None
        DistributedObject.DistributedObject.delete(self)
        self.nodePath.removeNode()
        return

