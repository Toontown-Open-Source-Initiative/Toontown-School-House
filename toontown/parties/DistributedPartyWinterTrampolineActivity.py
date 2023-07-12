# -------------------------------------------------------------------------------
# Contact: Mark Wojtowicz
# Created: June 2010
# -------------------------------------------------------------------------------

from toontown.parties import PartyGlobals
from toontown.parties.DistributedPartyTrampolineActivity import DistributedPartyTrampolineActivity


class DistributedPartyWinterTrampolineActivity(DistributedPartyTrampolineActivity):
    """ Reskinned trampoline for winter holiday parties. """

    def __init__(self, cr, doJellyBeans=True, doTricks=False, texture=None):
        self.notify.debug("Intializing.")
        DistributedPartyTrampolineActivity.__init__(self,
                                                    cr,
                                                    doJellyBeans,
                                                    doTricks,
                                                    "phase_13/maps/tt_t_ara_pty_trampolineWinter.jpg",
                                                    activityId=PartyGlobals.ActivityIds.PartyWinterTrampoline
                                                    )