from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

from toontown.fishing import FishGlobals


class DistributedFishingSpotAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedFishingSpotAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.pondDoId = 0
        self.posHpr = [0, 0, 0, 0, 0, 0]
        self.avId = None
        self.lastFish = [None, None, None]
        self.cast = False

    def generate(self):
        DistributedObjectAI.generate(self)
        pond = self.air.doId2do.get(self.pondDoId)
        if pond:
            pond.addSpot(self)

    def setPondDoId(self, pondDoId):
        self.pondDoId = pondDoId

    def d_setPondDoId(self, pondDoId):
        self.sendUpdate('setPondDoId', [pondDoId])

    def b_setPondDoId(self, pondDoId):
        self.setPondDoId(pondDoId)
        self.d_setPondDoId(pondDoId)

    def getPondDoId(self):
        return self.pondDoId

    def setPosHpr(self, x, y, z, h, p, r):
        self.posHpr = [x, y, z, h, p, r]

    def d_setPosHpr(self, x, y, z, h, p, r):
        self.sendUpdate('setPosHpr', [x, y, z, h, p, r])

    def b_setPosHpr(self, x, y, z, h, p, r):
        self.setPosHpr(x, y, z, h, p, r)
        self.d_setPosHpr(x, y, z, h, p, r)

    def getPosHpr(self):
        return self.posHpr

    def requestEnter(self):
        avId = self.air.getAvatarIdFromSender()
        if not avId:
            return

        if self.avId is not None:
            if self.avId == avId:
                self.air.writeServerEvent('suspicious', avId, 'Toon requested to enter a fishing spot twice!')

            self.sendUpdateToAvatarId(avId, 'rejectEnter', [])
            return

        event = self.air.getAvatarExitEvent(avId)
        self.acceptOnce(event, self.__handleUnexpectedExit)
        self.b_setOccupied(avId)
        self.d_setMovie(FishGlobals.EnterMovie, 0, 0, 0, 0, 0, 0)
        taskMgr.remove('cancel-animation-%d' % self.doId)
        taskMgr.doMethodLater(2, self.d_setMovie, 'cancel-animation-%d' % self.doId,
                              [FishGlobals.NoMovie, 0, 0, 0, 0, 0, 0])
        taskMgr.remove('time-out-%d' % self.doId)
        taskMgr.doMethodLater(FishGlobals.CastTimeout + 2.5, self.removeFromFishingSpotWithAnim,
                              'time-out-%d' % self.doId)
        self.lastFish = [None, None, None]
        self.cast = False

    def requestExit(self):
        avId = self.air.getAvatarIdFromSender()
        if not avId:
            return

        if self.avId != avId:
            self.air.writeServerEvent('suspicious', avId, 'Toon requested to exit a fishing spot they\'re not on!')
            return

        event = self.air.getAvatarExitEvent(avId)
        self.ignore(event)
        self.removeFromFishingSpotWithAnim()

    def setOccupied(self, avId):
        self.avId = avId

    def d_setOccupied(self, avId):
        self.sendUpdate('setOccupied', [avId])

    def b_setOccupied(self, avId):
        self.setOccupied(avId)
        self.d_setOccupied(avId)

    def doCast(self, p, h):
        avId = self.air.getAvatarIdFromSender()
        if not avId:
            return

        if self.avId != avId:
            self.air.writeServerEvent('suspicious', avId, 'Toon tried to cast from a fishing spot they\'re not on!')
            return

        av = self.air.doId2do.get(avId)
        if not av:
            self.air.writeServerEvent('suspicious', avId, 'Toon tried to cast, but they don\'t exist on this shard!')
            return

        money = av.getMoney()
        cost = FishGlobals.getCastCost(av.getFishingRod())
        if money < cost:
            self.air.writeServerEvent('suspicious', avId, 'Toon tried to cast without enough jellybeans!')
            return

        if len(av.fishTank) >= av.getMaxFishTank():
            self.air.writeServerEvent('suspicious', avId, 'Toon tried to cast with too many fish!')
            return

        av.takeMoney(cost, False)
        self.d_setMovie(FishGlobals.CastMovie, 0, 0, 0, 0, p, h)
        taskMgr.remove('cancel-animation-%d' % self.doId)
        taskMgr.doMethodLater(2, self.d_setMovie, 'cancel-animation-%d' % self.doId,
                              [FishGlobals.NoMovie, 0, 0, 0, 0, 0, 0])
        taskMgr.remove('time-out-%d' % self.doId)
        taskMgr.doMethodLater(FishGlobals.CastTimeout, self.removeFromFishingSpotWithAnim, 'time-out-%d' % self.doId)
        self.cast = True

    def sellFish(self):
        pass  # TODO

    def __handleUnexpectedExit(self):
        self.removeFromFishingSpot()

    def removeFromFishingSpot(self, task=None):
        taskMgr.remove('time-out-%d' % self.doId)
        self.d_setMovie(FishGlobals.NoMovie, 0, 0, 0, 0, 0, 0)
        self.d_setOccupied(0)
        self.avId = None
        if task:
            return task.done

    def d_setMovie(self, mode, code, genus, species, weight, p, h):
        self.sendUpdate('setMovie', [mode, code, genus, species, weight, p, h])

    def removeFromFishingSpotWithAnim(self, task=None):
        taskMgr.remove('cancel-animation-%d' % self.doId)
        self.d_setMovie(FishGlobals.ExitMovie, 0, 0, 0, 0, 0, 0)
        taskMgr.doMethodLater(1.5, self.removeFromFishingSpot, 'remove-%d' % self.doId)
        if task:
            return task.done

    def considerReward(self, target):
        if not self.cast:
            self.air.writeServerEvent('suspicious', self.avId, 'Toon tried to fish without casting!')
            return

        av = self.air.doId2do.get(self.avId)
        if not av:
            return

        pond = self.air.doId2do.get(self.pondDoId)
        if not pond:
            return

        area = pond.getArea()
        catch = self.air.fishManager.generateCatch(av, area)
        self.lastFish = catch
        self.d_setMovie(FishGlobals.PullInMovie, catch[0], catch[1], catch[2], catch[3], 0, 0)
        self.cast = False
