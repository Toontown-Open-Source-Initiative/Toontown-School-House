from toontown.parties.DistributedPartyCogActivity import DistributedPartyCogActivity


class DistributedPartyWinterCogActivity(DistributedPartyCogActivity):
    """ Reskinned cog pie arena for winter holiday parties. """

    def __init__(self, cr):
        DistributedPartyCogActivity.__init__(self, cr, "phase_13/models/parties/tt_m_ara_pty_cogPieArenaWinter")
