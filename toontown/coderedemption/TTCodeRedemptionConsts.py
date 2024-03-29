from panda3d.core import *

RedeemErrors = Enum('Success, CodeDoesntExist, CodeIsExpired, CodeAlreadyRedeemed, AwardCouldntBeGiven, TooManyAttempts, SystemUnavailable, ')

# for ~code response
RedeemErrorStrings = {
    RedeemErrors.Success: 'Success',
    RedeemErrors.CodeDoesntExist: 'Invalid code',
    RedeemErrors.CodeIsExpired: 'Code is expired',
    RedeemErrors.CodeAlreadyRedeemed: 'Code has already been redeemed',
    RedeemErrors.AwardCouldntBeGiven: 'Award could not be given',
    RedeemErrors.TooManyAttempts: 'Too many attempts, code ignored',
    RedeemErrors.SystemUnavailable: 'Code redemption is currently unavailable',
}

assert len(RedeemErrorStrings) == len(RedeemErrors)

MaxCustomCodeLen = ConfigVariableInt('tt-max-custom-code-len', 16).getValue()
