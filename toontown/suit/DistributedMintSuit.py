from toontown.suit import DistributedFactorySuit
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import TTLocalizer

class DistributedMintSuit(DistributedFactorySuit.DistributedFactorySuit):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedMintSuit')

    def renameBoss(self):
        if self.getSkeleRevives() > 0:
            nameInfo = TTLocalizer.SuitBaseNameWithLevel % {'name': TTLocalizer.Supervisor,
             'dept': self.getStyleDept(),
             'level': '%s%s%s' % (self.getActualLevel(), TTLocalizer.SkeleRevivePostFix, ' X')}
            self.setDisplayName(nameInfo + '.X')
            self.setDisplayName(nameInfo)
        else:
            nameInfo = TTLocalizer.SuitBaseNameWithLevel % {'name': TTLocalizer.Supervisor,
             'dept': self.getStyleDept(),
             'level': str(self.getActualLevel())}
            self.setName(TTLocalizer.Supervisor)
            self.setDisplayName(nameInfo + '.X')