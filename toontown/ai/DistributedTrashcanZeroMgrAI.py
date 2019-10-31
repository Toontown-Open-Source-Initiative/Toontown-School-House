from direct.directnotify import DirectNotifyGlobal
from toontown.ai.DistributedPhaseEventMgrAI import DistributedPhaseEventMgrAI

class DistributedTrashcanZeroMgrAI(DistributedPhaseEventMgrAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedTrashcanZeroMgrAI")

