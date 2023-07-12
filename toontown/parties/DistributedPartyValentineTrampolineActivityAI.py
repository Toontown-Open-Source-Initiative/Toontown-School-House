# -------------------------------------------------------------------------------
# Contact: Mark Wojtowicz
# Created: June 2010
# -------------------------------------------------------------------------------

from toontown.parties import PartyGlobals
from toontown.parties.DistributedPartyTrampolineActivityAI import DistributedPartyTrampolineActivityAI


class DistributedPartyValentineTrampolineActivityAI(DistributedPartyTrampolineActivityAI):
    """ Reskinned trampoline for valentoon party holiday. """

    def __init__(self, air, partyDoId, x, y, h):
        DistributedPartyTrampolineActivityAI.__init__(self,
                                                      air,
                                                      partyDoId,
                                                      x,
                                                      y,
                                                      h,
                                                      activityId=PartyGlobals.ActivityIds.PartyValentineTrampoline
                                                      )
