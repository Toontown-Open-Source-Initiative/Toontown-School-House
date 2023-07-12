from toontown.parties import PartyGlobals
from toontown.parties.DistributedPartyCatchActivityAI import DistributedPartyCatchActivityAI


class DistributedPartyWinterCatchActivityAI(DistributedPartyCatchActivityAI):
    """ Reskinned catch activity for winter party holiday. """

    def __init__(self, air, partyDoId, x, y, h):
        DistributedPartyCatchActivityAI.__init__(self,
                                                 air,
                                                 partyDoId,
                                                 x,
                                                 y,
                                                 h,
                                                 activityId=PartyGlobals.ActivityIds.PartyWinterCatch
                                                 )
