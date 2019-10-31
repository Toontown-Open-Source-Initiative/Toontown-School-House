import time

from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

from toontown.catalog.CatalogGenerator import CatalogGenerator
from toontown.toonbase import ToontownGlobals


class CatalogManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('CatalogManagerAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.catalogGenerator = CatalogGenerator()

    def startCatalog(self):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)
        if not av:
            return

        self.deliverCatalogFor(av)

    def deliverCatalogFor(self, av):
        previousWeek, previousTime = av.getCatalogSchedule()
        mailboxContents = av.mailboxNotify
        currentTime = time.time()
        if previousTime:
            elapsedWeeks = int((time.time() - previousTime * 60) // 604800)
            if elapsedWeeks < 1:
                currentTime = previousTime * 60
            else:
                currentTime = previousTime * 60 + elapsedWeeks * 604800

        nextWeek = currentTime + 604800
        currentWeek = previousWeek + 1
        monthlyCatalog = self.catalogGenerator.generateMonthlyCatalog(av, currentTime / 60)
        weeklyCatalog = self.catalogGenerator.generateWeeklyCatalog(av, currentWeek, monthlyCatalog)
        backlogCatalog = self.catalogGenerator.generateBackCatalog(av, currentWeek, previousWeek, weeklyCatalog)
        av.b_setCatalogSchedule(currentWeek, nextWeek / 60)
        av.b_setCatalog(monthlyCatalog, weeklyCatalog, backlogCatalog)
        av.b_setCatalogNotify(ToontownGlobals.NewItems, mailboxContents)
