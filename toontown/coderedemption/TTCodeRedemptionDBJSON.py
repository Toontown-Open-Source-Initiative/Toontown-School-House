from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.showbase.DirectObject import DirectObject

from direct.fsm.FSM import FSM
from direct.fsm.StatePush import StateVar, FunctionCall

from direct.task import Task

from toontown.coderedemption.TTCodeDict import TTCodeDict
from toontown.coderedemption import TTCodeRedemptionConsts
from toontown.coderedemption import TTCodeRedemptionDBConsts

from direct.showbase.Job import Job

import os
import json
import datetime
import random


from otp.ai.AIBaseGlobal import *


class TryAgainLater(Exception):
    def __init__(self, exception, file):
        self._exception = exception
        self._file = file

    def getJSONException(self):
        return self._exception

    def __str__(self):
        return 'problem using JSON file  %s, try again later (%s)' % (self._file, self.exception)


class TTCodeRedemptionDBTester(Job):
    notify = directNotify.newCategory('TTCodeRedemptionDBTester')

    class TestRewarder:
        def _giveReward(self, avId, rewardTypeId, rewardItemId, callback):
            callback(0)

    def __init__(self, db):
        self._db = db
        Job.__init__(self, 'TTCodeRedemptionDBTester-%s' % serialNum())

    def getRandomSamples(self, callback, numSamples):
        samples = []
        for i in range(numSamples):
            samples.append(int(random.random() * ((1 << 32)-1)))
        callback(samples)

    @classmethod
    def isLotNameValid(cls, lotName):
        # make sure a user doesn't create a lot that matches the test lot naming convention
        return (TTCodeRedemptionDBConsts.TestLotName not in lotName)

    @classmethod
    def cleanup(cls, db):
        # remove any leftover data from previous tests
        db._testing = True
        lotNames = db.getLotNames()
        for lotName in lotNames:
            if TTCodeRedemptionDBConsts.TestLotName in lotName:
                db.deleteLot(lotName)
        db._testing = False

    def _handleRedeemResult(self, result, awardMgrResult):
        self._redeemResult.append(result)
        self._redeemResult.append(awardMgrResult)

    def _getUnusedLotName(self):
        lotNames = self._db.getLotNames()
        while 1:
            lotName = '%s%s' % (TTCodeRedemptionDBConsts.TestLotName, int(random.random() * ((1 << 32)-1)))
            if lotName not in lotNames:
                break
        return lotName

    def _getUnusedManualCode(self):
        while 1:
            code = ''
            length = random.randrange(4, 16)
            manualCharIndex = random.randrange(length)
            for i in range(length):
                if i == manualCharIndex:
                    charSet = TTCodeDict.ManualOnlyCharacters
                else:
                    charSet = TTCodeDict.ManualCharacters
                char = random.choice(charSet)
                if char in TTCodeDict.IgnoredManualCharacters:
                    i -= 1
                code = code + char
            if not self._db.codeExists(code):
                break
        return code

    def _getUnusedUtf8ManualCode(self):
        chars = '\u65e5\u672c\u8a9e'
        code = str('')
        while 1:
            code += random.choice(chars)
            if not self._db.codeExists(code):
                break
        return code

    def run(self):
        self.notify.info('testing started')

        retryStartT = None
        retryDelay = 5

        while 1:
            try:
                db = self._db
                db._testing = True

                lotName = self._getUnusedLotName()

                # make sure there are at least one manual and one auto lot throughout the tests
                phLots = []
                phLots.append(self._getUnusedLotName())
                for i in self._db.createLot(self.getRandomSamples, phLots[-1], 1, 0, 0):
                    db._testing = False
                    yield None
                    db._testing = True
                phLots.append(self._getUnusedLotName())
                code = self._getUnusedManualCode()
                self._db.createManualLot(phLots[-1], code, 0, 0)
                db._testing = False
                yield None
                db._testing = True

                # lot creation
                NumCodes = 3
                RewardType = 0
                RewardItemId = 0
                ExpirationDate = '9999-04-01'
                for i in self._db.createLot(self.getRandomSamples, lotName, NumCodes, RewardType, RewardItemId, ExpirationDate):
                    db._testing = False
                    yield None
                    db._testing = True

                lotNames = self._db.getLotNames()
                if lotName not in lotNames:
                    self.notify.error('could not create code redemption lot \'%s\'' % lotName)
                db._testing = False
                yield None
                db._testing = True

                autoLotNames = self._db.getAutoLotNames()
                if lotName not in autoLotNames:
                    self.notify.error('auto lot \'%s\' not found in getAutoLotNames()' % lotName)
                db._testing = False
                yield None
                db._testing = True

                manualLotNames = self._db.getManualLotNames()
                if lotName in manualLotNames:
                    self.notify.error('auto lot \'%s\' found in getAutoLotNames()' % lotName)
                db._testing = False
                yield None
                db._testing = True

                # get codes in lot
                codes = self._db.getCodesInLot(lotName)
                if len(codes) != NumCodes:
                    self.notify.error('incorrect number of codes from getCodesInLot (%s)' % len(codes))
                db._testing = False
                yield None
                db._testing = True

                # code existance query
                exists = self._db.codeExists(codes[0])
                if not exists:
                    self.notify.error('codeExists returned false for code %s' % codes[0])
                db._testing = False
                yield None
                db._testing = True

                # number of redemptions (not yet redeemed)
                redemptions = self._db.getRedemptions(codes[0])
                if redemptions != 0:
                    self.notify.error('incorrect number of redemptions (%s) for not-yet-redeemed code %s' % (redemptions, codes[0], ))
                db._testing = False
                yield None
                db._testing = True

                # get lot name from code
                ln = self._db.getLotNameFromCode(codes[0])
                if ln != lotName:
                    self.notify.error('incorrect lot name (%s) from code (%s)' % (ln, codes[0]))
                db._testing = False
                yield None
                db._testing = True

                # get reward from code
                rt, rid = self._db.getRewardFromCode(codes[0])
                if rt != RewardType or rid != RewardItemId:
                    self.notify.error('incorrect reward (%s, %s) from code %s' % (rt, rid))
                db._testing = False
                yield None
                db._testing = True

                # redeem code
                self._redeemResult = []
                self._db.redeemCode(codes[0], TTCodeRedemptionDBConsts.FakeAvId, self.TestRewarder(), self._handleRedeemResult)
                if self._redeemResult[0] or self._redeemResult[1]:
                    self.notify.error('error redeeming code %s for fake avatar %s: %s' % (codes[0], TTCodeRedemptionDBConsts.FakeAvId, self._redeemResult))
                db._testing = False
                yield None
                db._testing = True

                # number of redemptions (redeemed)
                redemptions = self._db.getRedemptions(codes[0])
                if redemptions != 1:
                    self.notify.error('incorrect number of redemptions (%s) for already-redeemed code %s' % (redemptions, codes[0], ))
                db._testing = False
                yield None
                db._testing = True

                # redeem code that has already been redeemed
                self._redeemResult = []
                self._db.redeemCode(codes[0], TTCodeRedemptionDBConsts.FakeAvId, self.TestRewarder(), self._handleRedeemResult)
                if self._redeemResult[0] != TTCodeRedemptionConsts.RedeemErrors.CodeAlreadyRedeemed:
                    self.notify.error('able to redeem code %s twice' % (codes[0]))
                db._testing = False
                yield None
                db._testing = True

                # number of redemptions (redeemed)
                redemptions = self._db.getRedemptions(codes[0])
                if redemptions != 1:
                    self.notify.error('incorrect number of redemptions (%s) for already-redeemed code %s' % (redemptions, codes[0], ))
                db._testing = False
                yield None
                db._testing = True

                # lookup codes redeemed by avId
                c = self._db.lookupCodesRedeemedByAvId(TTCodeRedemptionDBConsts.FakeAvId)
                if len(c) != 1:
                    self.notify.error('lookupCodesRedeemedByAvId returned wrong number of codes: %s' % c)
                if c[0] != codes[0]:
                    self.notify.error('lookupCodesRedeemedByAvId returned wrong code: %s' % c[0])
                db._testing = False
                yield None
                db._testing = True

                # get code details
                details = self._db.getCodeDetails(codes[0])
                if details[TTCodeRedemptionDBConsts.CodeFieldName] != codes[0]:
                    self.notify.error('incorrect %s (%s) returned by getCodeDetails(%s)' % (TTCodeRedemptionDBConsts.CodeFieldName, details[TTCodeRedemptionDBConsts.CodeFieldName], codes[0]))
                if details[TTCodeRedemptionDBConsts.AvatarIdFieldName] != TTCodeRedemptionDBConsts.FakeAvId:
                    self.notify.error('incorrect %s (%s) returned by getCodeDetails(%s)' % (TTCodeRedemptionDBConsts.AvatarIdFieldName, details[TTCodeRedemptionDBConsts.AvatarIdFieldName], codes[0]))
                if details[TTCodeRedemptionDBConsts.RewardTypeFieldName] != RewardType:
                    self.notify.error('incorrect %s (%s) returned by getCodeDetails(%s)' % (TTCodeRedemptionDBConsts.RewardTypeFieldName, details[TTCodeRedemptionDBConsts.RewardTypeFieldName], codes[0]))
                if details[TTCodeRedemptionDBConsts.RewardItemIdFieldName] != RewardItemId:
                    self.notify.error('incorrect %s (%s) returned by getCodeDetails(%s)' % (TTCodeRedemptionDBConsts.RewardItemIdFieldName, details[TTCodeRedemptionDBConsts.RewardItemIdFieldName], codes[0]))
                db._testing = False
                yield None
                db._testing = True

                # get expiration date
                exp = self._db.getExpiration(lotName)
                if exp != ExpirationDate:
                    self.notify.error('incorrect expiration date: %s' % exp)
                db._testing = False
                yield None
                db._testing = True

                # change expiration date
                y = 1111
                m = 4
                d = 1
                NewExp = '%s-%02d-%02d' % (y, m, d)
                assert datetime.datetime.fromtimestamp(time.time()) > datetime.datetime(y, m, d)

                # make sure it doesn't change the expiration date of all lots
                controlLotName = self._getUnusedLotName()
                controlCode = self._getUnusedManualCode()
                controlExp = '%s-%02d-%02d' % (y, m, d+1)
                self._db.createManualLot(controlLotName, controlCode, RewardType, RewardItemId, expirationDate=controlExp)
                db._testing = False
                yield None
                db._testing = True

                self._db.setExpiration(lotName, NewExp)
                db._testing = False
                yield None
                db._testing = True

                exp = self._db.getExpiration(lotName)
                if (exp != NewExp):
                    self.notify.error('could not change expiration date for lot %s' % lotName)
                db._testing = False
                yield None
                db._testing = True

                cExp = self._db.getExpiration(controlLotName)
                if (cExp != controlExp):
                    self.notify.error('setExpiration changed control lot expiration!')
                db._testing = False
                yield None
                db._testing = True

                self._db.deleteLot(controlLotName)
                db._testing = False
                yield None
                db._testing = True

                # redeem code that is expired
                self._redeemResult = []
                self._db.redeemCode(codes[1], TTCodeRedemptionDBConsts.FakeAvId, self.TestRewarder(), self._handleRedeemResult)
                if self._redeemResult[0] != TTCodeRedemptionConsts.RedeemErrors.CodeIsExpired:
                    self.notify.error('expired code %s was not flagged upon redeem' % (codes[1]))
                db._testing = False
                yield None
                db._testing = True

                # lot deletion
                self._db.deleteLot(lotName)
                db._testing = False
                yield None
                db._testing = True

                codes = (self._getUnusedManualCode(), self._getUnusedUtf8ManualCode())

                for code in codes:
                    # manual code lot
                    lotName = self._getUnusedLotName()
                    self.notify.info('manual code: %s' % (code))
                    self._db.createManualLot(lotName, code, RewardType, RewardItemId)
                    if not self._db.lotExists(lotName):
                        self.notify.error('could not create manual lot %s' % lotName)
                    if not self._db.codeExists(code):
                        self.notify.error('could not create manual code %s' % code)
                    db._testing = False
                    yield None
                    db._testing = True

                    autoLotNames = self._db.getAutoLotNames()
                    if lotName in autoLotNames:
                        self.notify.error('manual lot \'%s\' found in getAutoLotNames()' % lotName)
                    db._testing = False
                    yield None
                    db._testing = True

                    manualLotNames = self._db.getManualLotNames()
                    if lotName not in manualLotNames:
                        self.notify.error('manual lot \'%s\' not found in getAutoLotNames()' % lotName)
                    db._testing = False
                    yield None
                    db._testing = True

                    # number of redemptions (not-yet-redeemed)
                    redemptions = self._db.getRedemptions(code)
                    if redemptions != 0:
                        self.notify.error('incorrect number of redemptions (%s) for not-yet-redeemed code %s' % (redemptions, code, ))
                    db._testing = False
                    yield None
                    db._testing = True

                    # redeem manually-created code
                    self._redeemResult = []
                    self._db.redeemCode(code, TTCodeRedemptionDBConsts.FakeAvId, self.TestRewarder(), self._handleRedeemResult)
                    if self._redeemResult[0] or self._redeemResult[1]:
                        self.notify.error('error redeeming code %s for fake avatar %s: %s' % (code, TTCodeRedemptionDBConsts.FakeAvId, self._redeemResult))
                    db._testing = False
                    yield None
                    db._testing = True

                    # number of redemptions (not-yet-redeemed)
                    self._db.commitOutstandingRedemptions()
                    redemptions = self._db.getRedemptions(code)
                    if redemptions != 1:
                        self.notify.error('incorrect number of redemptions (%s) for redeemed code %s' % (redemptions, code, ))
                    db._testing = False
                    yield None
                    db._testing = True

                    # redeem manually-created code again
                    self._redeemResult = []
                    self._db.redeemCode(code, TTCodeRedemptionDBConsts.FakeAvId, self.TestRewarder(), self._handleRedeemResult)
                    if self._redeemResult[0] or self._redeemResult[1]:
                        self.notify.error('error redeeming code %s again for fake avatar %s: %s' % (code, TTCodeRedemptionDBConsts.FakeAvId, self._redeemResult))
                    db._testing = False
                    yield None
                    db._testing = True

                    # number of redemptions (not-yet-redeemed)
                    self._db.commitOutstandingRedemptions()
                    redemptions = self._db.getRedemptions(code)
                    if redemptions != 2:
                        self.notify.error('incorrect number of redemptions (%s) for twice-redeemed code %s' % (redemptions, code, ))
                    db._testing = False
                    yield None
                    db._testing = True

                    self._db.deleteLot(lotName)
                    db._testing = False
                    yield None
                    db._testing = True

                    lotNames = self._db.getLotNames()
                    if lotName in lotNames:
                        self.notify.error('could not delete code redemption lot \'%s\'' % lotName)
                    db._testing = False
                    yield None
                    db._testing = True

                # remove placeholder lots
                for lotName in phLots:
                    self._db.deleteLot(lotName)
                    db._testing = False
                    yield None
                    db._testing = True

                break
            except TryAgainLater as e:
                self.notify.warning('caught TryAgainLater exception during self-test, retrying')
                retryStartT = globalClock.getRealTime()
                while globalClock.getRealTime() < (retryStartT + retryDelay):
                    yield None
                retryDelay *= 2

        self.notify.info('testing done')
        db._testing = False
        yield Job.Done


class NotFound:
    pass


class InfoCache:
    NotFound = NotFound

    def __init__(self):
        self._cache = {}

    def clear(self):
        self._cache = {}

    def cacheInfo(self, key, info):
        self._cache[key] = info

    def hasInfo(self, key):
        return key in self._cache

    def getInfo(self, key):
        return self._cache.get(key, NotFound)


class TTCodeRedemptionDB(DirectObject):
    notify = directNotify.newCategory('TTCodeRedemptionDB')

    TryAgainLater = TryAgainLater

    RewardTypeFieldName = 'reward_type'
    RewardItemIdFieldName = 'reward_item_id'

    DoSelfTest = ConfigVariableBool('code-redemption-self-test', False).getValue()

    # optimization that reads in all codes and maps them to their lot
    # if the code set gets too large this might use up too much RAM
    # you can disable the optimization by turning this config off
    CacheAllCodes = ConfigVariableBool('code-redemption-cache-all-codes', True).getValue()

    class LotFilter:
        All = 'All Codes'
        Redeemable = 'Redeemable Codes'
        NonRedeemable = 'Non-Redeemable Codes'
        Redeemed = 'Redeemed Codes'
        Expired = 'Expired Codes'

    def __init__(self, air):
        self.air = air

        self.filePath = ConfigVariableString('code-redemption-data-folder', 'data/code_redemption/').getValue()
        self.lotsFileName = ConfigVariableString('code-redemption-lots-file', 'lots').getValue()
        self.codeSpaceFileName = ConfigVariableString('code-redemption-code-space-file', 'code_space').getValue()
        self.codeSetFileName = ConfigVariableString('code-redemption-code-set-file', 'code_set_%s').getValue()

        # lot name cache
        self._code2lotNameCache = InfoCache()
        self._lotName2manualCache = InfoCache()
        self._code2rewardCache = InfoCache()
        self.doMethodLater(5 * 60, self._cacheClearTask, uniqueName('clearLotNameCache'))

        self._manualCode2outstandingRedemptions = {}
        self.doMethodLater(1 * 60, self._updateRedemptionsTask, uniqueName('updateRedemptions'))

        self._code2lotName = {}

        # set to true while doing internal tests
        self._testing = False
        self._initializedSV = StateVar(False)
        self._startTime = globalClock.getRealTime()
        self._doingCleanup = False
        self._dbInitRetryTimeout = 5
        self._doInitialCleanup()

        self._refreshCode2lotName()
        self._repairOldCodeLots()

    def _doInitialCleanup(self, task=None):
        if not self._initializedSV.get():
            self._doCleanup()

        if not self._initializedSV.get():
            self.doMethodLater(self._dbInitRetryTimeout, self._doInitialCleanup,
                               uniqueName('codeRedemptionInitialCleanup'))

            self._dbInitRetryTimeout *= 2
            self.notify.warning('could not initialize MySQL db, trying again later...')
        return Task.done

    def _doCleanup(self):
        if self._doingCleanup:
            return

        self._doingCleanup = True

        if not self._initializedSV.get():
            try:
                TTCodeRedemptionDBTester.cleanup(self)
            except TryAgainLater as e:
                pass
            else:
                self._initializedSV.set(True)

        self._doingCleanup = False

    def _randFuncCallback(self, randList, randSamplesOnOrder, samples):
        randSamplesOnOrder[0] -= len(samples)
        randList.extend(samples)

    def _refreshCode2lotName(self):
        if not self.CacheAllCodes:
            return

        # update the dict of code -> lotName for all codes
        self._code2lotName = {}
        lotNames = self.getLotNames()

        for lotName in lotNames:
            codes = self.getCodesInLot(lotName)

            for code in codes:
                self._code2lotName[code] = lotName

    @staticmethod
    def _getExpirationString(expiration):
        """
        formats expiration date for JSON
        """
        return '%s 23:59:59' % str(expiration)

    @staticmethod
    def _getNowString():
        nowStr = str(datetime.datetime.fromtimestamp(time.time()))
        # leave off the fractional seconds
        if '.' in nowStr:
            nowStr = nowStr[:nowStr.index('.')]
        return nowStr

    def createManualLot(self, name, code, rewardType, rewardItemId, expirationDate=None):
        self.notify.info('creating manual code lot \'%s\', code=%s' % (name, (code), ))
        self._doCleanup()

        code = TTCodeDict.getFromReadableCode(code)

        if self.lotExists(name):
            self.notify.error('tried to create lot %s that already exists' % name)

        if self.codeExists(code):
            self.notify.error('tried to create code %s that already exists' % (code))

        # First load lots file
        lotsFile = self.getFileName(self.lotsFileName)
        lotsData = self.loadLotsFile(lotsFile)

        lotId = lotsData[TTCodeRedemptionDBConsts.NextLotIdFieldName]

        lot = {
            TTCodeRedemptionDBConsts.LotIdFieldName: lotId,
            TTCodeRedemptionDBConsts.NameFieldName: name,
            TTCodeRedemptionDBConsts.ManualFieldName: 'T',
            TTCodeRedemptionDBConsts.RewardTypeFieldName: rewardType,
            TTCodeRedemptionDBConsts.RewardItemIdFieldName: rewardItemId,
            TTCodeRedemptionDBConsts.SizeFieldName: 1,
            TTCodeRedemptionDBConsts.CreationFieldName: self._getNowString()
        }

        if expirationDate:
            lot[TTCodeRedemptionDBConsts.ExpirationFieldName] = self._getExpirationString(expirationDate)
        else:
            lot[TTCodeRedemptionDBConsts.ExpirationFieldName] = ''

        lotsData[TTCodeRedemptionDBConsts.LotsFieldName].append(lot)

        lotsData[TTCodeRedemptionDBConsts.NextLotIdFieldName] = lotId + 1

        # Then load Code Set file
        codeSetFile = self.getFileName(self.codeSetFileName % (name))
        codeSetData = self.loadCodeSetFile(codeSetFile)

        codeSet = {
            TTCodeRedemptionDBConsts.CodeFieldName: code,
            TTCodeRedemptionDBConsts.LotIdFieldName: lotId,
            TTCodeRedemptionDBConsts.RedemptionsFieldName: 0
        }

        codeSetData.append(codeSet)

        self.saveFile(lotsFile, lotsData)
        self.saveFile(codeSetFile, codeSetData)

        self._refreshCode2lotName()

        self.notify.info('done')

    def createLot(self, randFunc, name, numCodes, rewardType, rewardItemId, expirationDate=None):
        """
        generator, yields None while working, yields True when finished
        randFunc must take a callback and a number of random samples, and must call the callback
        with a list of random 32-bit values of length equal to that specified in the call to randFunc
        the random values must be truly random and non-repeatable (see NonRepeatableRandomSource)
        """
        self.notify.info('creating code lot \'%s\', %s codes' % (name, numCodes, ))
        self._doCleanup()

        if self.lotExists(name):
            self.notify.error('tried to create lot %s that already exists' % name)

        randSampleRequestSize = ConfigVariableInt('code-redemption-rand-request-size', 50).getValue()
        randSampleRequestThreshold = 2 * randSampleRequestSize
        randSamples = []
        randSamplesOnOrder = [0, ]

        requestSize = min(numCodes, randSampleRequestSize)
        randSamplesOnOrder[0] += requestSize
        randFunc(Functor(self._randFuncCallback, randSamples, randSamplesOnOrder), requestSize)

        # First load code space file
        codeSpaceFile = self.getFileName(self.codeSpaceFileName)
        codeSpaceData = self.loadCodeSpaceFile(codeSpaceFile)

        codeLength = codeSpaceData[TTCodeRedemptionDBConsts.CodeLengthFieldName]
        nextCodeValue = codeSpaceData[TTCodeRedemptionDBConsts.NextCodeValueFieldName]

        startSerialNum = nextCodeValue

        # Second load lots file
        lotsFile = self.getFileName(self.lotsFileName)
        lotsData = self.loadLotsFile(lotsFile)

        lotId = lotsData[TTCodeRedemptionDBConsts.NextLotIdFieldName]

        lot = {
            TTCodeRedemptionDBConsts.LotIdFieldName: lotId,
            TTCodeRedemptionDBConsts.NameFieldName: name,
            TTCodeRedemptionDBConsts.ManualFieldName: 'F',
            TTCodeRedemptionDBConsts.RewardTypeFieldName: rewardType,
            TTCodeRedemptionDBConsts.RewardItemIdFieldName: rewardItemId,
            TTCodeRedemptionDBConsts.SizeFieldName: numCodes,
            TTCodeRedemptionDBConsts.CreationFieldName: self._getNowString()
        }

        if expirationDate:
            lot[TTCodeRedemptionDBConsts.ExpirationFieldName] = self._getExpirationString(expirationDate)
        else:
            lot[TTCodeRedemptionDBConsts.ExpirationFieldName] = ''

        lotsData[TTCodeRedemptionDBConsts.LotsFieldName].append(lot)

        lotsData[TTCodeRedemptionDBConsts.NextLotIdFieldName] = lotId + 1

        # Then load Code Set file
        codeSetFile = self.getFileName(self.codeSetFileName % (name))
        codeSetData = self.loadCodeSetFile(codeSetFile)

        codesLeft = numCodes
        curSerialNum = startSerialNum
        numCodeValues = TTCodeDict.getNumUsableValuesInCodeSpace(codeLength)
        n = 0
        while codesLeft:
            numCodesRequested = (len(randSamples) + randSamplesOnOrder[0])
            if numCodesRequested < codesLeft:
                if numCodesRequested < randSampleRequestThreshold:
                    requestSize = min(codesLeft, randSampleRequestSize)
                    randSamplesOnOrder[0] += requestSize
                    randFunc(Functor(self._randFuncCallback, randSamples, randSamplesOnOrder), requestSize)

            if len(randSamples) == 0:
                yield None
                continue

            # r in [0,1) but truly random (non-repeatable)
            r = randSamples.pop(0) / float(1 << 32)
            assert 0. <= r < 1.
            # this produces the 1 in N chance of guessing a correct code
            # each code is given a chunk of code space, of size N, and the actual value of the
            # code is chosen from that section of code space using a true random source
            # that means there's no way to guess a valid code based on observation of other codes
            randScatter = int(r * TTCodeDict.BruteForceFactor)
            assert 0 <= randScatter < TTCodeDict.BruteForceFactor
            value = (curSerialNum * TTCodeDict.BruteForceFactor) + randScatter
            obfValue = TTCodeDict.getObfuscatedCodeValue(value, codeLength)
            code = TTCodeDict.getCodeFromValue(obfValue, codeLength)

            codeSet = {
                TTCodeRedemptionDBConsts.CodeFieldName: code,
                TTCodeRedemptionDBConsts.LotIdFieldName: lotId,
                TTCodeRedemptionDBConsts.RedemptionsFieldName: 0
            }

            codeSetData.append(codeSet)

            codesLeft -= 1
            curSerialNum += 1
            if curSerialNum >= numCodeValues:
                curSerialNum = 0
                codeLength += 1
                numCodeValues = TTCodeDict.getNumUsableValuesInCodeSpace(codeLength)

            n = n + 1
            if (n % 100) == 0:
                yield None

        codeSpaceData[TTCodeRedemptionDBConsts.CodeLengthFieldName] = codeLength
        codeSpaceData[TTCodeRedemptionDBConsts.NextCodeValueFieldName] = curSerialNum

        self.saveFile(codeSpaceFile, codeSpaceData)
        self.saveFile(lotsFile, lotsData)
        self.saveFile(codeSetFile, codeSetData)

        self._refreshCode2lotName()

        self.notify.info('done')
        yield True

    def deleteLot(self, lotName):
        self.notify.info('deleting code lot \'%s\'' % (lotName, ))
        self._doCleanup()

        self._clearCaches()

        self.deleteFile(self.getFileName(self.codeSetFileName % (lotName)))

        lotsFile = self.getFileName(self.lotsFileName)
        lotsData = self.loadLotsFile(lotsFile)

        oldLots = lotsData.copy()
        lotsData[TTCodeRedemptionDBConsts.LotsFieldName] = []

        for lot in oldLots[TTCodeRedemptionDBConsts.LotsFieldName]:
            if lot[TTCodeRedemptionDBConsts.NameFieldName] != lotName:
                lotsData[TTCodeRedemptionDBConsts.LotsFieldName].append(lot)

        self.saveFile(lotsFile, lotsData)

        self._refreshCode2lotName()

    def getLotNames(self):
        assert self.notify.debugCall()
        self._doCleanup()
        lotNames = []

        lotsData = self.loadLotsFile(self.getFileName(self.lotsFileName))

        for lot in lotsData[TTCodeRedemptionDBConsts.LotsFieldName]:
            lotName = lot[TTCodeRedemptionDBConsts.NameFieldName]
            if not self._testing:
                if TTCodeRedemptionDBConsts.TestLotName in lotName:
                    continue
            lotNames.append(lotName)

        return lotNames

    def getAutoLotNames(self):
        """
        returns names of all code lots that were automatically generated
        """
        assert self.notify.debugCall()
        self._doCleanup()

        autoLotNames = []

        lotsData = self.loadLotsFile(self.getFileName(self.lotsFileName))

        for lot in lotsData[TTCodeRedemptionDBConsts.LotsFieldName]:
            if lot[TTCodeRedemptionDBConsts.ManualFieldName] == 'F':
                lotName = lot[TTCodeRedemptionDBConsts.NameFieldName]

                if not self._testing:
                    if TTCodeRedemptionDBConsts.TestLotName in lotName:
                        continue

                autoLotNames.append(lotName)

        return autoLotNames

    def getManualLotNames(self):
        """
        returns names of all code lots that were manually generated
        """
        assert self.notify.debugCall()
        self._doCleanup()

        manualLotNames = []

        lotsData = self.loadLotsFile(self.getFileName(self.lotsFileName))

        for lot in lotsData[TTCodeRedemptionDBConsts.LotsFieldName]:
            if lot[TTCodeRedemptionDBConsts.ManualFieldName] == 'T':
                lotName = lot[TTCodeRedemptionDBConsts.NameFieldName]

                if not self._testing:
                    if TTCodeRedemptionDBConsts.TestLotName in lotName:
                        continue

                manualLotNames.append(lotName)

        return manualLotNames

    def getExpirationLotNames(self):
        """
        returns names of all code lots that have expiration dates
        """
        assert self.notify.debugCall()
        self._doCleanup()

        lotNames = []

        lotsData = self.loadLotsFile(self.getFileName(self.lotsFileName))

        for lot in lotsData[TTCodeRedemptionDBConsts.LotsFieldName]:
            if lot[TTCodeRedemptionDBConsts.ExpirationFieldName] != '':
                lotName = lot[TTCodeRedemptionDBConsts.NameFieldName]

                if not self._testing:
                    if TTCodeRedemptionDBConsts.TestLotName in lotName:
                        continue

                lotNames.append(lotName)

        return lotNames

    def getCodesInLot(self, lotName, justCode=True, filter=None):
        # if justCode, returns list of codes
        # if not justCode, returns list of dict of field->value
        assert self.notify.debugCall()
        self._doCleanup()

        if filter is None:
            filter = self.LotFilter.All

        lotsData = self.loadLotsFile(self.getFileName(self.lotsFileName))
        codeSetData = self.loadCodeSetFile(self.getFileName(self.codeSetFileName % (lotName)))

        currentLot = ()

        for lot in lotsData[TTCodeRedemptionDBConsts.LotsFieldName]:
            if lot[TTCodeRedemptionDBConsts.NameFieldName] == lotName:
                currentLot = lot

        if currentLot == ():
            return ()

        if justCode:
            codes = []

            for codeSet in codeSetData:
                code = str(codeSet[TTCodeRedemptionDBConsts.CodeFieldName])
                codes.append(code)

            result = codes
        else:
            for codeSet in codeSetData:
                codeSet[TTCodeRedemptionDBConsts.CodeFieldName] = str(codeSet[TTCodeRedemptionDBConsts.CodeFieldName])
                codeSet[TTCodeRedemptionDBConsts.AvatarIdFieldName] = codeSet[TTCodeRedemptionDBConsts.AvatarIdFieldName] if TTCodeRedemptionDBConsts.AvatarIdFieldName in codeSet else None
                codeSet[TTCodeRedemptionDBConsts.NameFieldName] = currentLot[TTCodeRedemptionDBConsts.NameFieldName]
                codeSet[TTCodeRedemptionDBConsts.ManualFieldName] = currentLot[TTCodeRedemptionDBConsts.ManualFieldName]
                codeSet[TTCodeRedemptionDBConsts.RewardTypeFieldName] = currentLot[TTCodeRedemptionDBConsts.RewardTypeFieldName]
                codeSet[TTCodeRedemptionDBConsts.RewardItemIdFieldName] = currentLot[TTCodeRedemptionDBConsts.RewardItemIdFieldName]
                codeSet[TTCodeRedemptionDBConsts.SizeFieldName] = currentLot[TTCodeRedemptionDBConsts.SizeFieldName]
                codeSet[TTCodeRedemptionDBConsts.CreationFieldName] = currentLot[TTCodeRedemptionDBConsts.CreationFieldName]
                codeSet[TTCodeRedemptionDBConsts.ExpirationFieldName] = currentLot[TTCodeRedemptionDBConsts.ExpirationFieldName] if TTCodeRedemptionDBConsts.ExpirationFieldName in currentLot else None

            result = codeSetData

        if filter == self.LotFilter.Redeemable:
            oldResults = list(result)
            result = []

            for code in oldResults:
                if ((code[TTCodeRedemptionDBConsts.ManualFieldName] == 'T' or code[TTCodeRedemptionDBConsts.RedemptionsFieldName] == 0) and ((code[TTCodeRedemptionDBConsts.ExpirationFieldName] == None) or (datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') <= code[TTCodeRedemptionDBConsts.ExpirationFieldName]))):
                    result.append(code)
        elif filter == self.LotFilter.NonRedeemable:
            oldResults = list(result)
            result = []

            for code in oldResults:
                if ((code[TTCodeRedemptionDBConsts.ManualFieldName] == 'F' and code[TTCodeRedemptionDBConsts.RedemptionsFieldName] > 0) or ((code[TTCodeRedemptionDBConsts.ExpirationFieldName] != None) and (datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') > code[TTCodeRedemptionDBConsts.ExpirationFieldName]))):
                    result.append(code)
        elif filter == self.LotFilter.Redeemed:
            oldResults = result
            result = []

            for code in oldResults:
                if (code[TTCodeRedemptionDBConsts.RedemptionsFieldName] > 0):
                    result.append(code)
        elif filter == self.LotFilter.Expired:
            oldResults = list(result)
            result = []

            for code in oldResults:
                if (code[TTCodeRedemptionDBConsts.ExpirationFieldName] != None) and (datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') > code[TTCodeRedemptionDBConsts.ExpirationFieldName]):
                    result.append(code)

        return result

    def _clearCaches(self):
        self._code2lotNameCache.clear()
        self._lotName2manualCache.clear()
        self._code2rewardCache.clear()

    def _cacheClearTask(self, task):
        self._clearCaches()
        return Task.again

    def commitOutstandingRedemptions(self):
        if len(self._manualCode2outstandingRedemptions):
            self.notify.info('committing cached manual code redemption counts to DB')

        for key in self._manualCode2outstandingRedemptions.keys():
            code, lotName = key
            count = self._manualCode2outstandingRedemptions[key]
            self._updateRedemptionCount(code, True, None, lotName, count)

        self._manualCode2outstandingRedemptions = {}

    def _updateRedemptionsTask(self, task):
        try:
            self.commitOutstandingRedemptions()
        except TryAgainLater as e:
            pass
        return Task.again

    def getLotNameFromCode(self, code):
        assert self.notify.debugCall()

        code = TTCodeDict.getFromReadableCode(code)
        assert TTCodeDict.isLegalCode(code)

        if self.CacheAllCodes:
            return self._code2lotName.get(code, None)

        cachedLotName = self._code2lotNameCache.getInfo(code)
        if cachedLotName is not self._code2lotNameCache.NotFound:
            return cachedLotName

        assert self.notify.debug('lotNameFromCode CACHE MISS (%s)' % (code))

        self._doCleanup()

        lotNames = self.getLotNames()
        result = None

        for lotName in lotNames:
            codeSetData = self.loadCodeSetFile(self.getFileName(self.codeSetFileName % (lotName)))

            for codeSet in codeSetData:
                if codeSet[TTCodeRedemptionDBConsts.CodeFieldName] == code:
                    result = lotName
                    break

        if result is not None:
            self._code2lotNameCache.cacheInfo(code, result)

        return result

    def getRewardFromCode(self, code):
        assert self.notify.debugCall()

        code = TTCodeDict.getFromReadableCode(code)
        assert TTCodeDict.isLegalCode(code)

        lotName = self.getLotNameFromCode(code)
        assert lotName is not None

        cachedReward = self._code2rewardCache.getInfo(code)
        if cachedReward is not self._code2rewardCache.NotFound:
            return cachedReward

        assert self.notify.debug('reward from code CACHE MISS (%s)' % (code))

        self._doCleanup()

        lotsData = self.loadLotsFile(self.getFileName(self.lotsFileName))

        codeSetData = self.loadCodeSetFile(self.getFileName(self.codeSetFileName % (lotName)))

        lotId = -1
        rows = []

        for codeSet in codeSetData:
            if codeSet[TTCodeRedemptionDBConsts.CodeFieldName] == code:
                lotId = codeSet[TTCodeRedemptionDBConsts.LotIdFieldName]
                break

        for lot in lotsData[TTCodeRedemptionDBConsts.LotsFieldName]:
            if lot[TTCodeRedemptionDBConsts.LotIdFieldName] == lotId:
                rows.append(lot)

        assert len(rows) == 1
        reward = (int(rows[0][TTCodeRedemptionDBConsts.RewardTypeFieldName]), int(rows[0][TTCodeRedemptionDBConsts.RewardItemIdFieldName]))

        self._code2rewardCache.cacheInfo(code, reward)

        return reward

    def lotExists(self, lotName):
        return lotName in self.getLotNames()

    def codeExists(self, code):
        return self.getLotNameFromCode(code) != None

    def getRedemptions(self, code):
        assert self.notify.debugCall()

        self._doCleanup()

        code = TTCodeDict.getFromReadableCode(code)

        lotName = self.getLotNameFromCode(code)

        if lotName is None:
            self.notify.error('getRedemptions: could not find code %s' % (code))

        codeSetData = self.loadCodeSetFile(self.getFileName(self.codeSetFileName % (lotName)))

        for codeSet in codeSetData:
            if codeSet[TTCodeRedemptionDBConsts.CodeFieldName] == code:
                return codeSet[TTCodeRedemptionDBConsts.RedemptionsFieldName]

        return 0

    def redeemCode(self, code, avId, rewarder, callback):
        assert self.notify.debugCall()

        self._doCleanup()
        # callback takes a RedeemError
        # 'code' can come from a client, treat with care
        origCode = code
        code = TTCodeDict.getFromReadableCode(code)
        assert TTCodeDict.isLegalCode(code)

        lotName = self.getLotNameFromCode(code)
        if lotName is None:
            self.air.writeServerEvent('invalidCodeRedemption', avId, '%s' % ((origCode), ))
            callback(TTCodeRedemptionConsts.RedeemErrors.CodeDoesntExist, 0)
            return

        lotsData = self.loadLotsFile(self.getFileName(self.lotsFileName))
        codeSetData = self.loadCodeSetFile(self.getFileName(self.codeSetFileName % (lotName)))

        cachedManual = self._lotName2manualCache.getInfo(lotName)
        if cachedManual is not self._lotName2manualCache.NotFound:
            manualCode = cachedManual
        else:
            assert self.notify.debug('manualFromCode CACHE MISS (%s)' % (code))
            rows = []

            for lot in lotsData[TTCodeRedemptionDBConsts.LotsFieldName]:
                if lot[TTCodeRedemptionDBConsts.NameFieldName] == lotName:
                    rows.append(lot)

            assert len(rows) == 1

            manualCode = (rows[0][TTCodeRedemptionDBConsts.ManualFieldName] == 'T')

            self._lotName2manualCache.cacheInfo(lotName, manualCode)

        if not manualCode:
            rows = []

            for codeSet in codeSetData:
                if codeSet[TTCodeRedemptionDBConsts.CodeFieldName] == code:
                    codeSet = codeSet
                    break

            for lot in lotsData[TTCodeRedemptionDBConsts.LotsFieldName]:
                if lot[TTCodeRedemptionDBConsts.LotIdFieldName] == codeSet[TTCodeRedemptionDBConsts.LotIdFieldName] and (lot[TTCodeRedemptionDBConsts.ExpirationFieldName] == '' or datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') <= lot[TTCodeRedemptionDBConsts.ExpirationFieldName]):
                    rows.append(codeSet)

            assert len(rows) <= 1

        if not manualCode:
            if len(rows) == 0:
                # code is expired
                callback(TTCodeRedemptionConsts.RedeemErrors.CodeIsExpired, 0)
                return

            redemptions = rows[0][TTCodeRedemptionDBConsts.RedemptionsFieldName]

            if redemptions > 0:
                callback(TTCodeRedemptionConsts.RedeemErrors.CodeAlreadyRedeemed, 0)
                return

        rewardTypeId, rewardItemId = self.getRewardFromCode(code)

        rewarder._giveReward(avId, rewardTypeId, rewardItemId, Functor(
            self._handleRewardResult, code, manualCode, avId, lotName, rewardTypeId, rewardItemId,
            callback))

    def _updateRedemptionCount(self, code, manualCode, avId, lotName, count):
        assert self.notify.debugCall()

        codeSetFile = self.getFileName(self.codeSetFileName % (lotName))
        codeSetData = self.loadCodeSetFile(codeSetFile)

        for codeSet in codeSetData:
            if codeSet[TTCodeRedemptionDBConsts.CodeFieldName] == code:
                codeSet[TTCodeRedemptionDBConsts.RedemptionsFieldName] = codeSet[TTCodeRedemptionDBConsts.RedemptionsFieldName] + count

                if not manualCode:
                    codeSet[TTCodeRedemptionDBConsts.AvatarIdFieldName] = avId

        self.saveFile(codeSetFile, codeSetData)

    def _handleRewardResult(self, code, manualCode, avId, lotName, rewardTypeId, rewardItemId, callback, result):
        assert self.notify.debugCall()
        self._doCleanup()

        assert TTCodeDict.isLegalCode(code)

        awardMgrResult = result

        if awardMgrResult:
            callback(TTCodeRedemptionConsts.RedeemErrors.AwardCouldntBeGiven, awardMgrResult)
            return

        if manualCode:
            # queue up redemption count for manual code and write every N minutes
            key = (code, lotName)
            self._manualCode2outstandingRedemptions.setdefault(key, 0)
            self._manualCode2outstandingRedemptions[key] += 1
        else:
            self._updateRedemptionCount(code, manualCode, avId, lotName, 1)

        if not self._testing:
            self.air.writeServerEvent('codeRedeemed', avId, '%s|%s|%s|%s' % (
                (choice(manualCode, code, TTCodeDict.getReadableCode(code))),
                lotName, rewardTypeId, rewardItemId, ))

        callback(TTCodeRedemptionConsts.RedeemErrors.Success, awardMgrResult)

    def lookupCodesRedeemedByAvId(self, avId):
        assert self.notify.debugCall()

        self._doCleanup()

        codes = []

        # manual lots don't record redeemer avIds since they are single-code-multi-toon
        for lotName in self.getAutoLotNames():
            codeSetData = self.loadCodeSetFile(self.getFileName(self.codeSetFileName % (lotName)))

            for codeSet in codeSetData:
                if codeSet.get(TTCodeRedemptionDBConsts.AvatarIdFieldName):
                    if codeSet[TTCodeRedemptionDBConsts.AvatarIdFieldName] == avId:
                        code = str(codeSet[TTCodeRedemptionDBConsts.CodeFieldName])
                        codes.append(code)

        return codes

    def getExpiration(self, lotName):
        assert self.notify.debugCall()

        self._doCleanup()

        lotsData = self.loadLotsFile(self.getFileName(self.lotsFileName))
        expiration = ''

        for lot in lotsData[TTCodeRedemptionDBConsts.LotsFieldName]:
            if lot[TTCodeRedemptionDBConsts.NameFieldName] == lotName:
                expiration = str(datetime.datetime.strptime(lot[TTCodeRedemptionDBConsts.ExpirationFieldName], '%Y-%m-%d %H:%M:%S').date())

        return expiration

    def setExpiration(self, lotName, expiration):
        assert self.notify.debugCall()

        self._doCleanup()

        lotsFile = self.getFileName(self.lotsFileName)
        lotsData = self.loadLotsFile(lotsFile)

        for lot in lotsData[TTCodeRedemptionDBConsts.LotsFieldName]:
            if lot[TTCodeRedemptionDBConsts.NameFieldName] == lotName:
                lot[TTCodeRedemptionDBConsts.ExpirationFieldName] = self._getExpirationString(expiration)

        self.saveFile(lotsFile, lotsData)

    def getCodeDetails(self, code):
        assert self.notify.debugCall()

        self._doCleanup()

        lotsData = self.loadLotsFile(self.getFileName(self.lotsFileName))

        for lotName in self.getLotNames():
            codeSetData = self.loadCodeSetFile(self.getFileName(self.codeSetFileName % (lotName)))

            for codeSet in codeSetData:
                if codeSet[TTCodeRedemptionDBConsts.CodeFieldName] == TTCodeDict.getFromReadableCode(code):
                    codeSet[TTCodeRedemptionDBConsts.CodeFieldName] = str(codeSet[TTCodeRedemptionDBConsts.CodeFieldName])
                    codeSet[TTCodeRedemptionDBConsts.RewardTypeFieldName] = 0
                    codeSet[TTCodeRedemptionDBConsts.RewardItemIdFieldName] = 0

                    for lot in lotsData[TTCodeRedemptionDBConsts.LotsFieldName]:
                        if lot[TTCodeRedemptionDBConsts.LotIdFieldName] == codeSet[TTCodeRedemptionDBConsts.LotIdFieldName]:
                            codeSet[TTCodeRedemptionDBConsts.RewardTypeFieldName] = lot[TTCodeRedemptionDBConsts.RewardTypeFieldName]
                            codeSet[TTCodeRedemptionDBConsts.RewardItemIdFieldName] = lot[TTCodeRedemptionDBConsts.RewardItemIdFieldName]

                    return codeSet
        self.notify.error('code \'%s\' not found' % (code))

    if __debug__:
        def runTests(self):
            self._doRunTests(self._initializedSV.get())
            self._runTestsFC = FunctionCall(self._doRunTests, self._initializedSV)

        def _doRunTests(self, initialized):
            if initialized and self.DoSelfTest:
                jobMgr.add(TTCodeRedemptionDBTester(self))

    # Custom for JSONs
    def loadLotsFile(self, fileName):
        data = {TTCodeRedemptionDBConsts.LotsFieldName: [], TTCodeRedemptionDBConsts.NextLotIdFieldName: 0}

        try:
            with open(self.filePath + fileName, 'r') as f:
                data = json.load(f)

            fileExists = True
        except:
            fileExists = False

        if not fileExists:
            # Use self.update() to setup initial db:
            self.saveFile(fileName, data)

        return data

    def loadCodeSpaceFile(self, fileName):
        data = {TTCodeRedemptionDBConsts.CodeLengthFieldName: 4, TTCodeRedemptionDBConsts.NextCodeValueFieldName: 0}

        try:
            with open(self.filePath + fileName, 'r') as f:
                data = json.load(f)

            fileExists = True
        except:
            fileExists = False

        if not fileExists:
            # Use self.update() to setup initial db:
            self.saveFile(fileName, data)

        return data

    def loadCodeSetFile(self, fileName):
        data = []

        try:
            with open(self.filePath + fileName, 'r') as f:
                data = json.load(f)

            fileExists = True
        except:
            fileExists = False

        return data

    def saveFile(self, fileName, jsonData):
        if not os.path.exists(self.filePath):
            os.makedirs(self.filePath)

        with open(self.filePath + fileName, 'w+') as f:
            json.dump(jsonData, f, indent=4)

    def deleteFile(self, fileName):
        if os.path.exists(self.filePath + fileName):
            os.remove(self.filePath + fileName)

    def getFileName(self, fileName):
        return '%s.json' % (fileName)

    def _repairOldCodeLots(self):
        lotsFile = self.getFileName(self.lotsFileName)
        lotsData = self.loadLotsFile(lotsFile)

        oldLots = lotsData.copy()
        lotsData[TTCodeRedemptionDBConsts.LotsFieldName] = []

        for lot in oldLots[TTCodeRedemptionDBConsts.LotsFieldName]:
            if lot[TTCodeRedemptionDBConsts.ManualFieldName] == True:
                lot[TTCodeRedemptionDBConsts.ManualFieldName] = 'T'
                lotsData[TTCodeRedemptionDBConsts.LotsFieldName].append(lot)
            elif lot[TTCodeRedemptionDBConsts.ManualFieldName] == False:
                lot[TTCodeRedemptionDBConsts.ManualFieldName] = 'F'
                lotsData[TTCodeRedemptionDBConsts.LotsFieldName].append(lot)
            else:
                lotsData[TTCodeRedemptionDBConsts.LotsFieldName].append(lot)

        for lotName in self.getLotNames():
            codeSetFile = self.getFileName(self.codeSetFileName % (lotName))
            codeSetData = self.loadCodeSetFile(codeSetFile)

            for codeSet in codeSetData:
                if TTCodeRedemptionDBConsts.OldAvatarIdFieldName in codeSet.keys():
                    codeSet[TTCodeRedemptionDBConsts.AvatarIdFieldName] = codeSet[TTCodeRedemptionDBConsts.OldAvatarIdFieldName]
                    del codeSet[TTCodeRedemptionDBConsts.OldAvatarIdFieldName]

            self.saveFile(codeSetFile, codeSetData)

        self.saveFile(lotsFile, lotsData)
