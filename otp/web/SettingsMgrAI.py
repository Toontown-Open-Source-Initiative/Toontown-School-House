from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class SettingsMgrAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("SettingsMgrAI")

    def requestAllChangedSettings(self):
        pass

    def settingChange(self, todo0, todo1):
        pass

