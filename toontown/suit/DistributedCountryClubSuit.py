from toontown.suit import DistributedMintSuit
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import TTLocalizer

class DistributedCountryClubSuit(DistributedMintSuit.DistributedMintSuit):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedCountryClubSuit')

    def renameBoss(self):
        if self.getSkeleRevives() > 0:
            nameInfo = TTLocalizer.SuitBaseNameWithLevel % {'name': TTLocalizer.ClubPresident,
             'dept': self.getStyleDept(),
             'level': '%s%s' % (self.getActualLevel(), TTLocalizer.SkeleRevivePostFix)}
            self.setName(TTLocalizer.ClubPresident)
            self.setDisplayName(nameInfo)
        else:
            nameInfo = TTLocalizer.SuitBaseNameWithLevel % {'name': TTLocalizer.ClubPresident,
             'dept': self.getStyleDept(),
             'level': self.getActualLevel()}
            self.setName(TTLocalizer.ClubPresident)
            self.setDisplayName(nameInfo)