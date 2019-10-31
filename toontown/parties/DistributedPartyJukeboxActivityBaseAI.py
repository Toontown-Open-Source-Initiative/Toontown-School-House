from direct.directnotify import DirectNotifyGlobal
from toontown.parties.DistributedPartyActivityAI import DistributedPartyActivityAI

class DistributedPartyJukeboxActivityBaseAI(DistributedPartyActivityAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedPartyJukeboxActivityBaseAI")

    def setNextSong(self, todo0):
        pass

    def setSongPlaying(self, todo0, todo1):
        pass

    def queuedSongsRequest(self):
        pass

    def queuedSongsResponse(self, todo0, todo1):
        pass

    def setSongInQueue(self, todo0):
        pass

    def moveHostSongToTopRequest(self):
        pass

    def moveHostSongToTop(self):
        pass

