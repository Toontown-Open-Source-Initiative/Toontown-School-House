from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectUD import DistributedObjectUD

class SettingsMgrUD(DistributedObjectUD):
    notify = DirectNotifyGlobal.directNotify.newCategory("SettingsMgrUD")

    def requestAllChangedSettings(self):
        pass

    def settingChange(self, todo0, todo1):
        pass

