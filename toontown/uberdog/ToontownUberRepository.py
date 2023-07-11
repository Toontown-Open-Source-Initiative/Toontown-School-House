import time

from direct.directnotify import DirectNotifyGlobal

from otp.distributed.DistributedDirectoryAI import DistributedDirectoryAI
from otp.distributed.OtpDoGlobals import *

from toontown.distributed.ToontownInternalRepository import ToontownInternalRepository
from toontown.parties.ToontownTimeManager import ToontownTimeManager

if config.GetBool('want-rpc-server', False):
    from otp.rpc.RPCServer import RPCServer
    from toontown.rpc.ToontownRPCHandler import ToontownRPCHandler


class ToontownUberRepository(ToontownInternalRepository):
    notify = DirectNotifyGlobal.directNotify.newCategory('ToontownUberRepository')

    def __init__(self, baseChannel, serverId):
        ToontownInternalRepository.__init__(self, baseChannel, serverId, dcSuffix='UD')
        self.gameServicesManager = None
        self.ttoffFriendsManager = None
        self.chatManager = None
        self.deliveryManager = None

    def handleConnected(self):
        ToontownInternalRepository.handleConnected(self)

        rootObj = DistributedDirectoryAI(self)
        rootObj.generateWithRequiredAndId(self.getGameDoId(), 0, 0)

        # Create our local objects.
        self.notify.info('Creating local objects...')
        self.createLocals()

        # Create our global objects.
        self.notify.info('Creating global objects...')
        self.createGlobals()

        if config.GetBool('want-rpc-server', False):
            self.rpcserver = RPCServer(ToontownRPCHandler(self))

        self.notify.info('Done.')

    def createLocals(self):
        """
        Creates "local" objects.
        """
        self.toontownTimeManager = ToontownTimeManager(serverTimeUponLogin=int(time.time()), globalClockRealTimeUponLogin=globalClock.getRealTime())

    def createGlobals(self):
        self.gameServicesManager = self.generateGlobalObject(OTP_DO_ID_TOONTOWN_GAME_SERVICES_MANAGER,
                                                             'TTGameServicesManager')
        self.ttoffFriendsManager = self.generateGlobalObject(OTP_DO_ID_TTOFF_FRIENDS_MANAGER, 'TTOffFriendsManager')
        self.chatManager = self.generateGlobalObject(OTP_DO_ID_CHAT_MANAGER, 'TTOffChatManager')
        self.deliveryManager = self.generateGlobalObject(OTP_DO_ID_TOONTOWN_DELIVERY_MANAGER,
                                                         'DistributedDeliveryManager')
        self.codeRedemptionManager = self.generateGlobalObject(OTP_DO_ID_TOONTOWN_CODE_REDEMPTION_MANAGER,
                                                               'TTCodeRedemptionMgr')
        self.awardManager = self.generateGlobalObject(OTP_DO_ID_TOONTOWN_AWARD_MANAGER,
                                                      'AwardManager')
        self.randomSourceManager = self.generateGlobalObject(OTP_DO_ID_TOONTOWN_NON_REPEATABLE_RANDOM_SOURCE,
                                                             'NonRepeatableRandomSource')
        self.partyManager = self.generateGlobalObject(OTP_DO_ID_TOONTOWN_PARTY_MANAGER,
                                                      "DistributedPartyManager")
