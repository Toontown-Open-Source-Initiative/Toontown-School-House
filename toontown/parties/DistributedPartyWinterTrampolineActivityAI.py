
from toontown.parties import PartyGlobals
from toontown.parties.DistributedPartyTrampolineActivityAI import DistributedPartyTrampolineActivityAI


class DistributedPartyWinterTrampolineActivityAI(DistributedPartyTrampolineActivityAI):
    """ Reskinned trampoline for winter holiday parties. """

    def __init__(self, air, partyDoId, x, y, h):
        DistributedPartyTrampolineActivityAI.__init__(self,
                                                      air,
                                                      partyDoId,
                                                      x,
                                                      y,
                                                      h,
                                                      activityId=PartyGlobals.ActivityIds.PartyWinterTrampoline
                                                      )
