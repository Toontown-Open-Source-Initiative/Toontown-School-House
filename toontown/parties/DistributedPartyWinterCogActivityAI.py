from direct.directnotify import DirectNotifyGlobal

from toontown.parties.DistributedPartyCogActivityAI import DistributedPartyCogActivityAI
import PartyGlobals


class DistributedPartyWinterCogActivityAI(DistributedPartyCogActivityAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedPartyWinterCogActivityAI")

    def __init__(self, air, partyDoId, x, y, h):
        DistributedPartyCogActivityAI.__init__(self,
                                               air,
                                               partyDoId,
                                               x,
                                               y,
                                               h,
                                               PartyGlobals.ActivityIds.PartyWinterTrampoline
                                               )
