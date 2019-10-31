from direct.directnotify import DirectNotifyGlobal

from toontown.estate.DistributedStatuaryAI import DistributedStatuaryAI


class DistributedChangingStatuaryAI(DistributedStatuaryAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedChangingStatuaryAI')
