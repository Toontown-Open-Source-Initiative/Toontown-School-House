from direct.directnotify import DirectNotifyGlobal
from toontown.ai.DistributedPhaseEventMgrAI import DistributedPhaseEventMgrAI

class DistributedMailboxZeroMgrAI(DistributedPhaseEventMgrAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedMailboxZeroMgrAI")

