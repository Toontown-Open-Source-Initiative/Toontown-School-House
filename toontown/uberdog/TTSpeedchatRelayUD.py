from direct.directnotify import DirectNotifyGlobal
from otp.uberdog.SpeedchatRelayUD import SpeedchatRelayUD

class TTSpeedchatRelayUD(SpeedchatRelayUD):
    notify = DirectNotifyGlobal.directNotify.newCategory("TTSpeedchatRelayUD")

