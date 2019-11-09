from otp.ai.AIBaseGlobal import *
from direct.directnotify import DirectNotifyGlobal
import random
from toontown.suit import SuitDNA
import CogDisguiseGlobals

class CogSuitManagerAI:
    notify = DirectNotifyGlobal.directNotify.newCategory('CogSuitManagerAI')

    def __init__(self, air):
        self.air = air
