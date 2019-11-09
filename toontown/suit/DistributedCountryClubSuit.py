from toontown.suit import DistributedMintSuit
from direct.directnotify import DirectNotifyGlobal

class DistributedCountryClubSuit(DistributedMintSuit.DistributedMintSuit):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedCountryClubSuit')