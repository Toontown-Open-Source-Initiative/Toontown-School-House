from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD
from direct.directnotify.DirectNotifyGlobal import directNotify

from panda3d.core import *

from otp.distributed import OtpDoGlobals

if ConfigVariableBool('want-code-redemption-mysql', False).getValue():
    from toontown.coderedemption.TTCodeRedemptionDBMYSQL import TTCodeRedemptionDB
else:
    from toontown.coderedemption.TTCodeRedemptionDB import TTCodeRedemptionDB
from toontown.coderedemption.TTCodeDict import TTCodeDict
from toontown.coderedemption import TTCodeRedemptionConsts
from toontown.coderedemption import TTCodeRedemptionSpamDetector
from toontown.coderedemption.TTCodeRedemptionMgrRPC import TTCodeRedemptionMgrRPC

import traceback


class TTCodeRedemptionMgrUD(DistributedObjectGlobalUD):
    notify = directNotify.newCategory('TTCodeRedemptionMgrUD')

    Disabled = ConfigVariableBool('disable-code-redemption', False).getValue()

    if __dev__:
        TestRedemptionSpamAvIdMin = 6
        TestRedemptionSpamAvIdMax = 9999999
        TestRedemptions = (
            # non-ascii
            ('\xff', (TTCodeRedemptionConsts.RedeemErrors.CodeDoesntExist, 0)),
            # invalid characters
            ('.', (TTCodeRedemptionConsts.RedeemErrors.CodeDoesntExist, 0)),
        )
        DisabledTestRedemptions = (
            ('HWF', (TTCodeRedemptionConsts.RedeemErrors.SystemUnavailable, 0)),
            (',', (TTCodeRedemptionConsts.RedeemErrors.SystemUnavailable, 0)),
        )
        # spam detection
        TestSpamRedemptions = (([('!!!', (TTCodeRedemptionConsts.RedeemErrors.CodeDoesntExist, 0)), ] * TTCodeRedemptionSpamDetector.Settings.DetectThreshold) +
                               [('!!!', (TTCodeRedemptionConsts.RedeemErrors.TooManyAttempts, 0)), ]
                               )

    def __init__(self, air):
        DistributedObjectGlobalUD.__init__(self, air)

        self._rewardSerialNumGen = SerialNumGen()
        self._rewardContextTable = {}

        self._redeemContextGen = SerialNumGen()
        self._redeemContext2session = {}

        if ConfigVariableBool('want-code-redemption-mysql', False).getValue():
            self.dbHost = ConfigVariableString("tt-code-db-host", 'localhost').getValue()
            self.dbPort = ConfigVariableInt("tt-code-db-port", 3306).getValue()

            self.dbUser = ConfigVariableString("tt-code-db-user", 'toontown_code_redemption').getValue()
            self.dbPassword = ConfigVariableString("tt-code-db-password", 'change_me').getValue()
            self.dbName = ConfigVariableString("tt-code-db-name", 'tt_code_redemption').getValue()

            self._db = TTCodeRedemptionDB(self.air, self.dbHost, self.dbPort, self.dbUser, self.dbPassword, self.dbName)
        else:
            self._db = TTCodeRedemptionDB(self.air)

        if __debug__:
            self._db.runTests()

        self._randSampleContext2callback = {}
        self._randSampleContextGen = SerialMaskedGen((1 << 32)-1)

        self._spamDetector = TTCodeRedemptionSpamDetector.TTCodeRedemptionSpamDetector()
        self._wantSpamDetect = ConfigVariableBool('want-code-redemption-spam-detect', True).getValue()

        self.rpcManager = TTCodeRedemptionMgrRPC(self.air, self._db)

        if __dev__:
            self._testAvId = random.randrange(self.TestRedemptionSpamAvIdMin, self.TestRedemptionSpamAvIdMax)
            self._avId2table = {self._testAvId: self.TestRedemptions,
                                }
            self._disabledAvId2table = {self._testAvId: self.DisabledTestRedemptions,
                                        }
            if self._wantSpamDetect:
                self._spamAvId = random.randrange(self.TestRedemptionSpamAvIdMin, self.TestRedemptionSpamAvIdMax)
                self._avId2table[self._spamAvId] = self.TestSpamRedemptions

    if __dev__:
        def _sendTestRedemptions(self):
            assert self.notify.debugCall()
            for avId in self._avId2table.keys():
                redemptions = self._avId2table[avId]
                for i in range(len(redemptions)):
                    redemption = redemptions[i]
                    code, results = redemption
                    self.redeemCodeAiToUd(0, 0, i, code, avId, self._resolveTestRedemption)

        def _sendDisabledTestRedemptions(self):
            saved = TTCodeRedemptionMgrUD.Disabled
            TTCodeRedemptionMgrUD.Disabled = True
            for avId in self._disabledAvId2table.keys():
                redemptions = self._disabledAvId2table[avId]
                for i in range(len(redemptions)):
                    redemption = redemptions[i]
                    code, results = redemption
                    self.redeemCodeAiToUd(0, 0, i, code, avId, self._resolveDisabledTestRedemption)
            TTCodeRedemptionMgrUD.Disabled = saved

        def _resolveTestRedemption(self, serial, context, avId, result, awardMgrResult):
            if avId in self._avId2table:
                redemptions = self._avId2table.get(avId)
                redemption = redemptions[context]
                code, results = redemption
                assert result == results[0]
                assert awardMgrResult == results[1]

        def _resolveDisabledTestRedemption(self, serial, context, avId, result, awardMgrResult):
            if avId in self._disabledAvId2table:
                redemptions = self._disabledAvId2table.get(avId)
                redemption = redemptions[context]
                code, results = redemption
                assert result == results[0]
                assert awardMgrResult == results[1]

    def announceGenerate(self):
        assert self.notify.debugCall()

        DistributedObjectGlobalUD.announceGenerate(self)

        if __dev__ and TTCodeRedemptionDB.DoSelfTest:
            if not self.Disabled:
                self._sendTestRedemptions()
            self._sendDisabledTestRedemptions()

    def _requestRandomSamples(self, callback, numSamples):
        assert self.notify.debugCall()
        context = self._randSampleContextGen.next()
        self._randSampleContext2callback[context] = callback
        self.air.dispatchUpdateToGlobalDoId("NonRepeatableRandomSourceUD", "getRandomSamples",
                                            OtpDoGlobals.OTP_DO_ID_TOONTOWN_NON_REPEATABLE_RANDOM_SOURCE,
                                            [self.doId, 'TTCodeRedemptionMgr', context, numSamples])

    def getRandomSamplesReply(self, context, samples):
        assert self.notify.debugCall()
        callback = self._randSampleContext2callback.pop(context)
        callback(samples)

    def _codeHasInvalidChars(self, code):
        return not TTCodeDict.isLegalCode(code)

    def redeemCodeAiToUd(self, serial, rmDoId, context, code, senderId, callback=None):
        assert self.notify.debugCall()
        avId = senderId

        # context is supplied by the client and there are no invalid values for it
        # code comes from the client and could be any string

        try:
            result = None

            if self.Disabled:
                result = TTCodeRedemptionConsts.RedeemErrors.SystemUnavailable
            else:
                while 1:
                    try:
                        code = str(code)
                    except UnicodeDecodeError as e:
                        # code is not utf-8-able
                        self.air.writeServerEvent('suspicious', avId, 'non-utf-8 code redemption: %s' % repr(code))
                        result = TTCodeRedemptionConsts.RedeemErrors.CodeDoesntExist
                        break

                    if self._codeHasInvalidChars(code):
                        # code has non-letter/digit/dash characters
                        result = TTCodeRedemptionConsts.RedeemErrors.CodeDoesntExist
                        break

                    break

                if (result or (not self._db.codeExists(code))):
                    # check to make sure this avatar isn't submitting incorrect codes too often
                    self._spamDetector.codeSubmitted(senderId)

                if self._wantSpamDetect and self._spamDetector.avIsBlocked(senderId):
                    self.air.writeServerEvent('suspicious', avId,
                                              'too many invalid code redemption attempts, '
                                              'submission rejected: %s' % (code))
                    result = TTCodeRedemptionConsts.RedeemErrors.TooManyAttempts

            if result is not None:
                awardMgrResult = 0
                self._handleRedeemCodeAiToUdResult(callback, serial, rmDoId, context, avId, result, awardMgrResult)
            else:
                """
                'code' came from a client and therefore should be considered to be any potential string
                (apart from any checks that have already been done), in particular strings intended
                to cause trouble
                """
                self._db.redeemCode(code, avId, self, Functor(
                    self._handleRedeemCodeAiToUdResult, callback, serial, rmDoId, context, avId, ))

        except TTCodeRedemptionDB.TryAgainLater as e:
            self._warnTryAgainLater(e)
        except:
            traceback.print_exc()

    def _handleRedeemCodeAiToUdResult(self, callback, serial, rmDoId, context, avId, result, awardMgrResult):
        assert self.notify.debugCall()
        if callback:
            callback(serial, context, avId, result, awardMgrResult)
        else:
            self.air.sendUpdateToDoId('TTCodeRedemptionMgr',
                                      'redeemCodeResultUdToAi',
                                      rmDoId,
                                      [serial, context, avId, result, awardMgrResult]
                                      )

    def redeemCode(self, code, avId, callback):
        assert self.notify.debugCall()
        # callback takes TTCodeRedemptionConsts.RedeemErrors value
        return self._db.redeemCode(code, avId, self, callback)

    def _giveReward(self, avId, rewardType, rewardItemId, callback):
        assert self.notify.debugCall()
        # callback takes result
        context = self._rewardSerialNumGen.next()
        self._rewardContextTable[context] = callback
        self.air.dispatchUpdateToGlobalDoId(
            "AwardManagerUD", "giveAwardToToon",
            OtpDoGlobals.OTP_DO_ID_TOONTOWN_AWARD_MANAGER,
            [context, self.doId, "TTCodeRedemptionMgrUD", avId, rewardType, rewardItemId, ])

    def giveAwardToToonResult(self, context, result):
        assert self.notify.debugCall()

        callback = self._rewardContextTable.pop(context)
        try:
            callback(result)
        except TTCodeRedemptionDB.TryAgainLater as e:
            self._warnTryAgainLater(e)

    def _warnTryAgainLater(self, exception):
        # if we catch a TryAgainLater, drop this code submission on the floor. The AI
        # will resubmit the code shortly
        self.notify.warning('%s' % exception)
        self.notify.warning('caught TryAgainLater exception from TTCodeRedemptionDB. Dropping request')
