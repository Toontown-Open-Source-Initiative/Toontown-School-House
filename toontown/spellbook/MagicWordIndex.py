import collections, types

from direct.distributed.ClockDelta import *
from direct.showbase.InputStateGlobal import inputState
from direct.interval.IntervalGlobal import *

from libotp import NametagGroup, WhisperPopup

from otp.otpbase import OTPLocalizer
from otp.otpbase import OTPGlobals

from toontown.battle import SuitBattleGlobals
from toontown.char import CharDNA
from toontown.coghq import CogDisguiseGlobals
from toontown.effects import FireworkShows
from toontown.estate import GardenGlobals
from toontown.fishing import FishGlobals
from toontown.golf import GolfGlobals
from toontown.hood import ZoneUtil
from toontown.parties import PartyGlobals
from toontown.quest import Quests
from toontown.racing.KartDNA import *
from toontown.racing import RaceGlobals
from toontown.shtiker import CogPageGlobals
from toontown.toon import NPCToons
from toontown.suit import SuitDNA
from toontown.toon import Experience
from toontown.toon import ToonDNA
from toontown.toonbase import ToontownBattleGlobals
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer

import MagicWordConfig
import time
import random
import json

magicWordIndex = collections.OrderedDict()

def getMagicWord(name):
    magicWord = globals().get(name)
    if not magicWord:
        magicWord = MagicWord()
    return magicWord

class MagicWord:
    # Whether this Magic word should be considered "hidden". This impacts if it is shown on the Magic Word page.
    hidden = False

    # Whether this Magic Word is an administrative command or not.
    # Administrative commands will be allowed on "Legit" servers.
    # Only these commands can be used on caged Toons.
    administrative = False

    # List of names that will also invoke this word - a setHP magic word might have "hp", for example.
    # A Magic Word will always be callable with its class name, so you don't have to put that in the aliases.
    aliases = None

    # Description of the Magic Word for use in the Shtikerbook.
    desc = "A simple Magic Word."

    # Default example with for commands with no arguments set.
    example = ""

    # The minimum access level required to use this Magic Word. By default, USER.
    accessLevel = 'USER'

    # A restriction on the Magic Word which sets what kind or set of Distributed Objects it can be used on. By default, AFFECT_EVERYONE.
    affectRange = [MagicWordConfig.AFFECT_SINGLE, MagicWordConfig.AFFECT_OTHER, MagicWordConfig.AFFECT_BOTH]

    # Where the magic word will be executed -- EXEC_LOC_CLIENT or EXEC_LOC_SERVER.
    execLocation = MagicWordConfig.EXEC_LOC_INVALID

    # List of all arguments for this word, with the format [(type, isRequired), (type, isRequired)...]
    # If the parameter is not required, you must provide a default argument: (type, False, default).
    arguments = None

    def __init__(self, air=None, cr=None, invokerId=None, targets=None, args=None):
        self.air = air
        self.cr = cr
        self.invokerId = invokerId
        self.targets = targets
        self.args = args
        if self.__class__.__name__ != "MagicWord": # If not the base class,
            self.aliases = self.aliases if self.aliases is not None else [] # if we use [] by default, it might get overwritten
            self.aliases.insert(0, self.__class__.__name__)  # add the class name to the alias list,
            self.aliases = map(lambda x: x.lower(), self.aliases)  # make all the aliases lowercase,
            self.arguments = self.arguments if self.arguments is not None else []

            if len(self.arguments) > 0:
                for arg in self.arguments:
                    argInfo = ""
                    if not arg[MagicWordConfig.ARGUMENT_REQUIRED]:
                        argInfo += "(DF:{0})".format(arg[MagicWordConfig.ARGUMENT_DEFAULT])
                    self.example += "[{0}{1}] ".format(arg[MagicWordConfig.ARGUMENT_NAME], argInfo)

            self.__register() # and register the magic word.

    def __register(self):

        for wordName in self.aliases:
            magicWordIndex[wordName] = {
                'classname': self.__class__.__name__, # This class
                'hidden': self.hidden,
                'administrative': self.administrative,
                'aliases': self.aliases,
                'desc': self.desc,
                'example': self.example,
                'execLocation': self.execLocation,
                'access': self.accessLevel,
                'affectRange': self.affectRange,
                'args': self.arguments
            }

    def executeWord(self):
        executedWord = None
        for avId in self.targets:
            invoker = None
            toon = None
            if self.air:
                invoker = self.air.doId2do.get(self.invokerId)
                toon = self.air.doId2do.get(avId)
            elif self.cr:
                invoker = self.cr.doId2do.get(self.invokerId)
                toon = self.cr.doId2do.get(avId)
            if not self.validateTarget(toon):
                if hasattr(toon, "getName"):
                    return "{} is not a valid target!".format(toon.getName())
                else:
                    return "{} is not a valid target!".format(avId)
            if toon.getLocked() and not self.administrative:
                return "{} is currently locked. You can only use administrative commands on them.".format(avId)

            if self.execLocation == MagicWordConfig.EXEC_LOC_CLIENT:
                self.args = json.loads(self.args)

            executedWord = self.handleWord(invoker, avId, toon, *self.args)
        if executedWord:
            return executedWord

    def validateTarget(self, target):
        if self.air:
            from toontown.toon.DistributedToonAI import DistributedToonAI
            return isinstance(target, DistributedToonAI)
        elif self.cr:
            from toontown.toon.DistributedToon import DistributedToon
            return isinstance(target, DistributedToon)
        return False

    def handleWord(self, invoker, avId, toon, *args):
        NotImplemented

# When creating new Magic Words, please try to use a consistent naming etiquette. Here are some rules we should follow:

# Restock - If a word gives you an item that you can consistently obtain and use (for example, a cog summon), but you cannot specify the amount you recieve, we give this command the prefix of "Restock"
# Unlock - If a word gives you an item that you can only ever obtain once (for example, pet trick phrases or emotes), we give this command the prefix of "Unlock"
# Set - If a word gives you an item that you can consistently obtain and use, or if it is a value on your toon (for example, a pinkslip, unite, or laff point value), and you can specify the amount you recieve, we give this command the prefix of "Set"
# Transform - If a word transforms you into something, we give this command the prefix of "Transform"
# Toggle - If a word toggles something on or off, we give this command the prefix of "Toggle"

class SetHP(MagicWord):
    aliases = ["hp", "setlaff", "laff"]
    desc = "Sets the target's current laff."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("hp", int, True)]

    def handleWord(self, invoker, avId, toon, *args):
        hp = args[0]

        if not -1 <= hp <= toon.getMaxHp():
            return "Can't set {0}'s laff to {1}! Specify a value between -1 and {0}'s max laff ({2}).".format(toon.getName(), hp, toon.getMaxHp())

        toon.b_setHp(hp)
        return "{}'s laff has been set to {}.".format(toon.getName(), hp)


class SetMaxHP(MagicWord):
    aliases = ["maxhp", "setmaxlaff", "maxlaff"]
    desc = "Sets the target's max laff."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("maxhp", int, True)]

    def handleWord(self, invoker, avId, toon, *args):
        maxhp = args[0]

        if not 15 <= maxhp <= 137:
            return "Can't set {}'s max laff to {}! Specify a value between 15 and 137.".format(toon.getName(), maxhp)

        toon.b_setMaxHp(maxhp)
        toon.toonUp(maxhp)
        return "{}'s max laff has been set to {}.".format(toon.getName(), maxhp)


class ToggleOobe(MagicWord):
    aliases = ["oobe"]
    desc = "Toggles the out of body experience mode, which lets you move the camera freely."
    execLocation = MagicWordConfig.EXEC_LOC_CLIENT

    def handleWord(self, invoker, avId, toon, *args):
        base.oobe()
        return "Oobe mode has been toggled."


class ToggleRun(MagicWord):
    aliases = ["run"]
    desc = "Toggles run mode, which gives you a faster running speed."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER

    def handleWord(self, invoker, avId, toon, *args):
        toon.d_setRun()
        return "Run mode has been toggled."


class SetSpeed(MagicWord):
    aliases = ["speed"]
    desc = "Sets your running speed."
    execLocation = MagicWordConfig.EXEC_LOC_CLIENT
    arguments = [("speed", float, False, OTPGlobals.ToonForwardSpeed)]

    def handleWord(self, invoker, avId, toon, *args):
        speed = args[0]

        if not 1.0 <= speed <= 1000.0:
            return "Can't set speed to {}! Specify a value between 1 and 1000.".format(toon.getName())

        if speed == OTPGlobals.ToonForwardSpeed:
            base.localAvatar.currentSpeed = OTPGlobals.ToonForwardSpeed
            base.localAvatar.currentReverseSpeed = OTPGlobals.ToonReverseSpeed
            base.localAvatar.controlManager.setSpeeds(OTPGlobals.ToonForwardSpeed, OTPGlobals.ToonJumpForce,
                                                      OTPGlobals.ToonReverseSpeed, OTPGlobals.ToonRotateSpeed)
            return "Your speed has been set to the default ({}).".format(OTPGlobals.ToonForwardSpeed)
        else:
            reverseSpeed = speed / 3
            base.localAvatar.currentSpeed = speed
            base.localAvatar.currentReverseSpeed = reverseSpeed
            base.localAvatar.controlManager.setSpeeds(speed, OTPGlobals.ToonJumpForce, reverseSpeed,
                                                      OTPGlobals.ToonRotateSpeed)
            return "Your speed has been set to {}.".format(speed)


class MaxToon(MagicWord):
    aliases = ["max", "idkfa"]
    desc = "Maxes out the target's stats. You can provide a gag track to exclude from the target's unlocked tracks."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("missingTrack", str, False, '')]

    def handleWord(self, invoker, avId, toon, *args):
        missingTrack = args[0]

        gagTracks = [1, 1, 1, 1, 1, 1, 1]
        if missingTrack != '':
            try:
                index = ('toonup', 'trap', 'lure', 'sound', 'throw',
                         'squirt', 'drop').index(missingTrack)
            except:
                return 'Missing Gag track is invalid!'
            gagTracks[index] = 0
        toon.b_setTrackAccess(gagTracks)
        toon.b_setMaxCarry(ToontownGlobals.MaxCarryLimit)

        experience = Experience.Experience(toon.getExperience(), toon)
        for i, track in enumerate(toon.getTrackAccess()):
            if track:
                experience.experience[i] = (
                        Experience.MaxSkill - Experience.UberSkill)
        toon.b_setExperience(experience.makeNetString())

        toon.inventory.zeroInv()
        toon.inventory.maxOutInv(filterUberGags=0, filterPaidGags=0)
        toon.b_setInventory(toon.inventory.makeNetString())

        toon.b_setMaxMoney(Quests.RewardDict[707][1])
        toon.b_setMoney(toon.getMaxMoney())
        toon.b_setBankMoney(ToontownGlobals.DefaultMaxBankMoney)

        toon.b_setMaxHp(ToontownGlobals.MaxHpLimit)
        laff = toon.getMaxHp() - toon.getHp()
        if laff < 15:
            laff = 15
        toon.toonUp(laff)

        toon.b_setHoodsVisited(ToontownGlobals.Hoods)
        toon.b_setTeleportAccess(ToontownGlobals.HoodsForTeleportAll)

        toon.b_setCogParts([
            CogDisguiseGlobals.PartsPerSuitBitmasks[0],
            CogDisguiseGlobals.PartsPerSuitBitmasks[1],
            CogDisguiseGlobals.PartsPerSuitBitmasks[2],
            CogDisguiseGlobals.PartsPerSuitBitmasks[3],
        ])
        toon.b_setCogLevels([ToontownGlobals.MaxCogSuitLevel] * 4 + [0])
        toon.b_setCogTypes([7] * 4 + [0])

        toon.b_setCogCount(list(CogPageGlobals.COG_QUOTAS[1]) * 4)
        cogStatus = [CogPageGlobals.COG_COMPLETE2] * SuitDNA.suitsPerDept
        toon.b_setCogStatus(cogStatus * 4)
        toon.b_setCogRadar([1] * 4)
        toon.b_setBuildingRadar([1] * 4)

        for id in toon.getQuests():
            toon.removeQuest(id)
        toon.b_setQuestCarryLimit(ToontownGlobals.MaxQuestCarryLimit)
        toon.b_setRewardHistory(Quests.COG_NATION_TIER, toon.getRewardHistory()[1])

        allFish = TTLocalizer.FishSpeciesNames
        fishLists = [[], [], []]
        for genus in allFish.keys():
            for species in xrange(len(allFish[genus])):
                fishLists[0].append(genus)
                fishLists[1].append(species)
                fishLists[2].append(FishGlobals.getRandomWeight(genus, species))
        toon.b_setFishCollection(*fishLists)
        toon.b_setFishingRod(FishGlobals.MaxRodId)
        toon.b_setFishingTrophies(FishGlobals.TrophyDict.keys())

        if not toon.hasKart() and simbase.wantKarts:
            toon.b_setKartBodyType(KartDict.keys()[1])
        toon.b_setTickets(RaceGlobals.MaxTickets)
        maxTrophies = RaceGlobals.NumTrophies + RaceGlobals.NumCups
        toon.b_setKartingTrophies(range(1, maxTrophies + 1))
        toon.b_setTickets(99999)

        toon.b_setGolfHistory([600] * (GolfGlobals.MaxHistoryIndex * 2 + 2))

        return "Maxed out {}'s stats.".format(toon.getName())


class UnlockEmotes(MagicWord):
    aliases = ["emotes"]
    desc = "Unlock all of the target's emotes."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER

    def handleWord(self, invoker, avId, toon, *args):
        emoteAccess = list(toon.getEmoteAccess())

        # Old version of command made emote access list shorter. Let's fix that.
        if len(emoteAccess) < len(OTPLocalizer.EmoteFuncDict):
            emoteAccess = [0] * len(OTPLocalizer.EmoteFuncDict)

        for emoteId in OTPLocalizer.EmoteFuncDict.values():
            if emoteId > 25 or emoteId in [17, 18, 19]:
                continue
            emoteAccess[emoteId] = 1

        toon.b_setEmoteAccess(emoteAccess)
        return "Unlocked all of {}'s emotes.".format(toon.getName())


class SetBeans(MagicWord):
    aliases = ["beans", "setjellybeans", "jellybeans", "setmoney", "money"]
    desc = "Sets the target's jellybean count."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("beans", int, True)]

    def handleWord(self, invoker, avId, toon, *args):
        beans = args[0]

        if not 0 <= beans <= toon.getMaxMoney():
            return "Can't set {0}'s jellybean count to {1}! Specify a value between 0 and {0}'s jellybean jar size ({2}).".format(toon.getName(), beans, toon.getMaxMoney())

        toon.b_setMoney(beans)
        return "{}'s jellybean count has been set to {}.".format(toon.getName(), beans)


class SetMaxBeans(MagicWord):
    aliases = ["maxbeans", "setmaxjellybeans", "maxjellybeans", "setmaxmoney", "maxMoney"]
    desc = "Sets the target's jellybean jar size."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("maxBeans", int, True)]

    def handleWord(self, invoker, avId, toon, *args):
        maxBeans = args[0]

        if not 0 <= maxBeans <= ToontownGlobals.MaxJarMoney:
            return "Can't set {}'s jellybean jar size to {}! Specify a value between 0 and 9999.".format(toon.getName(), maxBeans)

        toon.b_setMaxMoney(maxBeans)
        return "{}'s jellybean jar size has been set to {}.".format(toon.getName(), maxBeans)

########################################################################################################################
class SetEmblems(MagicWord):
    aliases = ["emblems"]
    desc = "Gives the target a specified amount of silver and gold emblems, respectively."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("silver", int, True), ("gold", int, True)]

    def handleWord(self, invoker, avId, toon, *args):
        emblems = (args[0], args[1])
        toon.addEmblems(emblems)
        return "Gave {} {} silver and {} gold emblems!".format(toon.getName(), *emblems)

class ToggleImmortal(MagicWord):
    aliases = ["immortal"]
    desc = "Makes the target immortal."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER

    def handleWord(self, invoker, avId, toon, *args):
        toon.b_setImmortalMode(not toon.getImmortalMode())
        return "{} is {} immortal!".format(toon.getName(), "now" if toon.getImmortalMode() else "no longer")


class ToggleUnlimitedGags(MagicWord):
    aliases = ["unlimitedgags"]
    desc = "Toggles unlimited gags for the target."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER

    def handleWord(self, invoker, avId, toon, *args):
        inventory = toon.inventory
        inventory.NPCMaxOutInv(targetTrack=-1, maxLevelIndex=6)
        invoker.b_setInventory(inventory.makeNetString())
        toon.b_setUnlimitedGags(not toon.getUnlimitedGags())
        return "{} {} has unlimited gags!".format(toon.getName(), "now" if toon.getUnlimitedGags() else "no longer")

class ToggleInstaKill(MagicWord):
    aliases = ["instakill"]
    desc = "Toggles the ability for the target to instantly kill Cogs with any amount of damage."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER

    def handleWord(self, invoker, avId, toon, *args):
        toon.b_setInstaKill(not toon.getInstaKill())
        return "{} can {} insta-kill Cogs!".format(toon.getName(), "now" if toon.getInstaKill() else "no longer")


class SkipMovie(MagicWord):
    desc = "Skips the current round of animations in a Cog battle."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER

    def handleWord(self, invoker, avId, toon, *args):
        battleId = toon.getBattleId()
        if not battleId:
            return "You cannot skip a movie if you are not currently in battle!"
        battle = self.air.doId2do.get(battleId)
        if not battle:
            return "{} is not a valid battle!".format(battleId)
        battle._DistributedBattleBaseAI__movieDone()
        return "Successfully skipped Battle movie!"


class ToggleGod(MagicWord):
    aliases = ["god"]
    desc = "Toggles running, immortality, unlimited gags and the ability to instantly kill Cogs with any amount of damage for the target."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER

    def handleWord(self, invoker, avId, toon, *args):
        isGod = not toon.getImmortalMode()
        toon.d_setRun()
        toon.b_setImmortalMode(isGod)
        toon.b_setUnlimitedGags(isGod)
        toon.b_setInstaKill(isGod)
        return "God mode {} for {}!".format("enabled" if isGod else "disabled", toon.getName())


class ToggleCollisionsOff(MagicWord):
    aliases = ['collisionsoff', 'noclip']
    desc = "Disables collisions for the target."
    execLocation = MagicWordConfig.EXEC_LOC_CLIENT

    def handleWord(self, invoker, avId, toon, *args):
        toon.collisionsOff()
        return "Collisions are now off for {}".format(toon.getName())

class ToggleCollisionsOn(MagicWord):
    aliases = ['collisionson', 'clip', 'yesclip']
    desc = "Enables collisions for the target."
    execLocation = MagicWordConfig.EXEC_LOC_CLIENT

    def handleWord(self, invoker, avId, toon, *args):
        toon.collisionsOn()
        return "Collisions are now on for {}".format(toon.getName())


class UnlockGlobalTP(MagicWord):
    aliases = ["alltp"]
    desc = "Allows the target to teleport anywhere."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER

    def handleWord(self, invoker, avId, toon, *args):
        hoodsVisited = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000]
        toon.b_setHoodsVisited(hoodsVisited)
        toon.b_setTeleportAccess(hoodsVisited)
        return "{} can now teleport anywhere!".format(toon.getName())


class Help(MagicWord):
    administrative = True
    desc = "Tells you to come here for more info... but you're already here!"
    execLocation = MagicWordConfig.EXEC_LOC_CLIENT

    def handleWord(self, invoker, avId, toon, *args):
        try:
            # make sure this is running on client
            settings = base.settings
        except NameError:
            # someone made this a server MW, so default to '~'
            mw_prefix = MagicWordConfig.PREFIX_ALLOWED[0]
        else:
            # we're actually client; get the actual prefix, or '~' if invalid
            idx = settings.getInt('game', 'magic-word-activator', 0)
            idx = idx if 0 <= idx < len(MagicWordConfig.PREFIX_ALLOWED) else 0
            mw_prefix = MagicWordConfig.PREFIX_ALLOWED[idx]
        return "Refer to your Shticker Book for a list of all commands! Some may require a higher access level. Clicking a Toon's nametag and then using 2 '{}' characters will run a command on them.".format(mw_prefix)


class ToggleSleeping(MagicWord):
    aliases = ["sleep", "sleeping"]
    desc = "Enables or disables sleeping for your current session. This does not affect other Toons."
    execLocation = MagicWordConfig.EXEC_LOC_CLIENT

    def handleWord(self, invoker, avId, toon, *args):
        if not base.localAvatar.neverSleep:
            base.localAvatar.disableSleeping()
            return "Sleeping has been deactivated for the current session."
        else:
            base.localAvatar.enableSleeping()
            return "Sleeping has been activated for the current session."


class ToggleRainbow(MagicWord):
    aliases = ["rainbow"]
    desc = "Makes everything rainbow for the target."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER

    def handleWord(self, invoker, avId, toon, *args):
        toon.d_generateRainbow()
        return "Rainbows toggled for {0}.".format(toon.getName())


class Teleport(MagicWord):
    aliases = ["tp"]
    desc = "Teleports the target to a specified location."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("hood", str, False, '')]

    def handleWord(self, invoker, avId, toon, *args):
        hood = args[0]

        if not hood:
            toon.d_doTeleport('GUI')
            return "Teleport GUI opened!"

        try:
            request = ToontownGlobals.hood2Id[hood.upper()]
        except:
            return "Invalid location!"

        hoodId = request[0]

        if hoodId in (ToontownGlobals.ToontownOutskirts, ToontownGlobals.ToontownCentralBeta, ToontownGlobals.DaisyGardensBeta) and not toon.getUnlocks()[0]:
            return "You don't know how to get to that location yet!"

        toon.d_doTeleport(hood)
        return "Teleporting {0} to {1}!".format(toon.getName(), ToontownGlobals.hoodNameMap[hoodId][-1])


class SetScale(MagicWord):
    aliases = ["scale"]
    desc = "Adjusts the scale of the target. Calling this with no arguments will set your scale to 1."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("scale", float, False, 1.0)]

    def handleWord(self, invoker, avId, toon, *args):
        scale = args[0]
        if not 0.1 <= scale <= 5:
            return "That scale is out of range! It must be between 0.1 and 5."
        toon.d_setToonScale(scale)
        return "Set {}'s scale to {}!".format(toon.getName(), scale)


class SpawnProp(MagicWord):
    aliases = ["prop"]
    desc = "Spawn a prop at the target's current location."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("name", str, False, ''), ("scale", float, False, 1.0)]

    def handleWord(self, invoker, avId, toon, *args):
        propName = args[0]
        scale = args[1]

        # Try to get the generator from the toon's current zone.
        propGenerator = self.air.propGenerators.get(toon.zoneId)
        if not propGenerator:
            # It's not there... Maybe this toon is on the street?
            propGenerator = self.air.propGenerators.get(ZoneUtil.getBranchZone(toon.zoneId))
            if not propGenerator:
                # Hmm... Oh well.
                return "Sorry, you can't spawn props in this location."

        if not propName:
            propGenerator.d_openNewPropWindow()
            return "Prop generator opened!"

        valid = 0
        for prop in ToontownGlobals.PropNames:
            propLower = prop.lower()
            propStripped = propLower.replace(" ", "")
            if propName == propLower or propName == propStripped:
                valid = 1
                propName = prop
                break

        if not valid:
            return "Invalid prop name!"

        if propName not in ToontownGlobals.PropNames:
            return "Invalid prop name!"

        if not 0.1 <= scale <= 5:
            return "That scale is out of range! It must be between 0.1 and 5."

        x, y, z = toon.getPos()
        h, p, r = toon.getHpr()

        propGenerator.d_spawnProp(propName, x, y, z, h, p, r, scale, scale, scale)
        return "Spawned a prop at {}'s location.".format(toon.getName())

class SetLoop(MagicWord):
    aliases = ['Loop']
    desc = "Causes the target to loop an animation."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("animName", str, True), ("start", int, False, -1), ("end", int, False, -1), ("part", str, False, '')]

    def handleWord(self, invoker, avId, toon, *args):
        start = args[1]
        end = args[2]

        if not -1 <= start <= 1000:
            return "Start frame out of range!"

        if not -1 <= end <= 1000:
            return "End frame out of range!"

        toon.d_setLoop(args[0], args[1], args[2], args[3])
        return "Looping animation for {}".format(toon.getName())

class SetPingPong(MagicWord):
    aliases = ['PingPong']
    desc = "Causes the target to go back and forth between two frames of an animation. By default, these are the start and end frames."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("animName", str, True), ("start", int, False, -1), ("end", int, False, -1), ("part", str, False, '')]

    def handleWord(self, invoker, avId, toon, *args):
        start = args[1]
        end = args[2]

        if not -1 <= start <= 1000:
            return "Start frame out of range!"

        if not -1 <= end <= 1000:
            return "End frame out of range!"

        toon.d_setPingPong(args[0], args[1], args[2], args[3])
        return "{} is now going back and forth between 2 frames of an animation.".format(toon.getName())

class SetPose(MagicWord):
    aliases = ['pose']
    desc = "Causes the target to pose using a given frame of a given animation."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("animName", str, True), ("frame", int, True), ("part", str, False, '')]

    def handleWord(self, invoker, avId, toon, *args):
        frame = args[1]

        if not 0 <= frame <= 1000:
            return "Frame out of range!"

        toon.d_setPose(args[0], args[1], args[2])
        return "{} is now posing.".format(toon.getName())


class UnlockTrackAccess(MagicWord):
    aliases = ["trackaccess"]
    desc = "Set the type of gags a toon has."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("wantTrack", int, True)]*7

    def handleWord(self, invoker, avId, toon, *args):
        # args = toonup, trap, lure, sound, throw, squirt, drop
        if len(args) == 7:
            toon.b_setTrackAccess(list(args))
        else:
            return "Invalid amount of arguments! There must be 7..."
        return "Tracks set for {}".format(toon.getName())
        


class UnlockTracks(MagicWord):
    aliases = ["tracks"]
    desc = "Grants all the gag tracks, with the option of leaving one out."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("leftOutTrack", str, False, '')]

    def handleWord(self, invoker, avId, toon, *args):
        leftOutTrack = args[0]

        tracks = [("toonup", 1), ("trap", 1), ("lure", 1), ("sound", 1), ("throw", 1), ("squirt", 1), ("drop", 1)]
        tracks = collections.OrderedDict(tracks)
        if leftOutTrack in tracks.keys():
            tracks[leftOutTrack] = 0

        toon.b_setTrackAccess(tracks.values())
        if leftOutTrack:
            msg = "Set your gag tracks, %sless Toon!" % (leftOutTrack)
        else:
            msg = "Set your gag tracks, Toon!"

        return msg


class Catalog(MagicWord):
    desc = "Gives the toon a new catalog."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER

    def handleWord(self, invoker, avId, toon, *args):
        simbase.air.catalogManager.deliverCatalogFor(toon)
        return 'New catalog is arriving for {}'.format(toon.getName())

class GetAccId(MagicWord):
    administrative = True
    aliases = ["accId", "accountId"]
    desc = "Get the accountId from the target player."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    accessLevel = "MODERATOR"

    def handleWord(self, invoker, avId, toon, *args):
        accountId = toon.DISLid
        return "%s has the accountId of %d" % (toon.getName(), accountId)


class GetAvId(MagicWord):
    administrative = True
    aliases = ["avId", "avatarId"]
    desc = "Get the avId from the target player."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    accessLevel = "MODERATOR"

    def handleWord(self, invoker, avId, toon, *args):
        return "%s has the avId of %d" % (toon.getName(), toon.getDoId())


class System(MagicWord):
    administrative = True
    aliases = ["sys", "sysmsg", "systemmessage"]
    desc = "Broadcasts a message to the server."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("message", str, True)]
    accessLevel = "MODERATOR"

    def handleWord(self, invoker, avId, toon, *args):
        from otp.avatar.DistributedPlayerAI import DistributedPlayerAI
        message = args[0]
        for doId, do in simbase.air.doId2do.items():
            if isinstance(do, DistributedPlayerAI):
                if str(doId)[0] != str(simbase.air.districtId)[0]:
                    if do.getAccessLevel() >= 400:
                        do.d_setSystemMessage(0, str(invoker.getName()) + " (" + str(invoker.getDoId()) + "): " + message, WhisperPopup.WTMagicWord)
                    else:
                        do.d_setSystemMessage(0, message, WhisperPopup.WTMagicWord)
        return "System message sent"

class SetGravity(MagicWord):
    aliases = ["gravity"]
    desc = "Set your gravity value."
    execLocation = MagicWordConfig.EXEC_LOC_CLIENT
    arguments = [("gravity", float, False, ToontownGlobals.GravityValue * 2.0), ("override", bool, False, False)]

    def handleWord(self, invoker, avId, toon, *args):
        gravityValue = args[0]
        overrideWarning = args[1]

        if not base.localAvatar:
            return "Your Toon does not exist!"

        if gravityValue < 1 and not overrideWarning:
            return "A value lower than 1 may crash your client."

        base.localAvatar.controlManager.currentControls.setGravity(gravityValue)
        if gravityValue == ToontownGlobals.GravityValue * 2.0:
            return "Gravity returned to normal."
        elif gravityValue == ToontownGlobals.GravityValue * 0.75:
            return "April fools gravity enabled!"
        return 'Gravity value set.'

class GetPos(MagicWord):
    desc = "Get the current position of your toon."
    execLocation = MagicWordConfig.EXEC_LOC_CLIENT

    def handleWord(self, invoker, avId, toon, *args):
        if not base.localAvatar:
            return "Your Toon does not exist!"
        return str(base.localAvatar.getPos())


class SetPos(MagicWord):
    desc = "Set the current position of your Toon."
    execLocation = MagicWordConfig.EXEC_LOC_CLIENT
    arguments = [("x", float, True), ("y", float, True), ("z", float, True)]

    def handleWord(self, invoker, avId, toon, *args):
        toonX = args[0]
        toonY = args[1]
        toonZ = args[2]
        if not base.localAvatar:
            return "Your Toon does not exist!"
        for arg in args:
            if not -2500 <= arg <= 2500:
                return "This position is too far out!"
        base.localAvatar.setPos(toonX, toonY, toonZ)
        return 'Position set.'


class GetH(MagicWord):
    desc = "Returns the rotation value of your Toon."
    execLocation = MagicWordConfig.EXEC_LOC_CLIENT

    def handleWord(self, invoker, avId, toon, *args):
        if not base.localAvatar:
            return "No Toon found!"
        return str(base.localAvatar.getH())


class SetH(MagicWord):
    desc = "Set the rotation value of your Toon."
    execLocation = MagicWordConfig.EXEC_LOC_CLIENT
    arguments = [("h", int, True), ("part", str, False, '')]

    def handleWord(self, invoker, avId, toon, *args):
        toonH = args[0]

        if not base.localAvatar:
            return "No Toon found!"

        part = args[1].lower()

        if part in ('head', 'torso', 'legs'):
            for lod in toon.getLODNames():
                base.localAvatar.getPart(part, lod).setH(toonH)

        base.localAvatar.setH(toonH)
        return "Rotation value set"

# class GetNumFrames(MagicWord):
#     desc = "Returns the number of frames in a given Toon animation."
#     execLocation = MagicWordConfig.EXEC_LOC_CLIENT
#     arguments = [("anim", str, True), ("part", str, False, 'head')]
#
#     def handleWord(self, invoker, avId, toon, *args):
#         anim = args[0]
#         part = args[1]
#         if not base.localAvatar:
#             return 'No Toon found!'
#         return "There are {0} frames in the {1} animation.".format(str(base.localAvatar.getNumFrames(anim, part)), anim)


class SetTrueFriend(MagicWord):
    aliases = ["tf", 'TrueFriend']
    desc = "Automatically add a Toon as a true friend."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("avIdShort", int, True)]

    def handleWord(self, invoker, avId, toon, *args):
        avIdShort = args[0]
        avIdFull = 400000000 - (300000000 - avIdShort)
        av = simbase.air.doId2do.get(avIdFull)
        if not av:
            return "avId not found/online!"
        if int(str(avIdFull)[:2]) >= 40: # AI
            return "%s is an NPC!" % av.getName()
        if invoker == av:
            return "Cannot true friend yourself!"

        invoker.extendFriendsList(av.getDoId(), 1)
        av.extendFriendsList(invoker.getDoId(), 1)

        invoker.d_setFriendsList(invoker.getFriendsList())
        av.d_setFriendsList(av.getFriendsList())
        return "You are now true friends with {}".format(av.getName())


class ToggleOobeCull(MagicWord):
    aliases = ["oobecull"]
    desc = "Toggle 'out of body experience' view, with culling debugging."
    execLocation = MagicWordConfig.EXEC_LOC_CLIENT

    def handleWord(self, invoker, avId, toon, *args):
        base.oobeCull()
        return 'Toggled "out of body experience" view'


class ToggleWire(MagicWord):
    aliases = ["wire", "wireframe"]
    desc = "Toggle wireframe view."
    execLocation = MagicWordConfig.EXEC_LOC_CLIENT

    def handleWord(self, invoker, avId, toon, *args):
        base.toggleWireframe()
        return "Toggled wireframe"


class ToggleTextures(MagicWord):
    aliases = ["textures"]
    desc = "Toggle textures."
    execLocation = MagicWordConfig.EXEC_LOC_CLIENT

    def handleWord(self, invoker, avId, toon, *args):
        base.toggleTexture()
        return 'Toggled textures'


class ToggleFPS(MagicWord):
    aliases = ["fps", "showfps"]
    desc = "Toggle frame rate meter."
    execLocation = MagicWordConfig.EXEC_LOC_CLIENT

    def handleWord(self, invoker, avId, toon, *args):
        base.setFrameRateMeter(not base.frameRateMeter)
        return 'Toggled frame rate meter'

class GetAccess(MagicWord):
    desc = "Get the access level of a target."
    execLocation = MagicWordConfig.EXEC_LOC_CLIENT
    accessLevel = "MODERATOR"

    def handleWord(self, invoker, avId, toon, *args):
        return "Access level: " + str(toon.getAccessLevel())


class ToggleAspect2D(MagicWord):
    aliases = ["a2d", 'Aspect2D']
    desc = "Toggles Aspect2d."
    execLocation = MagicWordConfig.EXEC_LOC_CLIENT

    def handleWord(self, invoker, avId, toon, *args):
        if aspect2d.isHidden():
            aspect2d.show()
        else:
            aspect2d.hide()
        return "Toggled aspect2D"
        


class Ban(MagicWord):
    administrative = True
    desc = "Bans the target."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("duration", int, False, 0), ("reason", str, False, "Not specified.")]
    accessLevel = "MODERATOR"
    affectRange = [MagicWordConfig.AFFECT_OTHER]

    def handleWord(self, invoker, avId, toon, *args):
        from toontown.toon.DistributedToonAI import DistributedToonAI
        reason = args[1]
        duration = args[0]

        if duration:
            if not 10 <= duration <= 30000:
                return "Can't ban {0}'s with duration {1}! Specify a value between 10 and 30000.".format(toon.getName(), duration)

        if toon.getDoId() not in simbase.air.doId2do.keys() or invoker.getDoId() not in simbase.air.doId2do.keys():
            simbase.air.writeServerEvent('suspicious', issue="Invalid invoker: %s and target: %s when trying to ban them." % (invoker.getDoId(), toon.getDoId()))
            return "Failed to ban the target!"

        if not isinstance(toon, DistributedToonAI) and not isinstance(invoker, DistributedToonAI):
            return "You can only ban a Toon."
        else:
            toon.sendSetBan(reason=reason, target=toon, invoker=invoker, duration=duration)
            return "Banned %s!" % toon.getName()


class BanId(MagicWord):
    desc = "Bans the target based on their Toon ID."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("id", int, True), ("duration", int, False, 0), ("reason", str, False, "Not specified.")]
    accessLevel = "MODERATOR"

    def handleWord(self, invoker, avId, toon, *args):
        from toontown.toon.DistributedToonAI import DistributedToonAI
        id = args[0]
        reason = args[2]
        duration = args[1]

        toon = self.air.doId2do.get(id)
        if not toon:
            return "Invalid Toon ID specified, or the Toon is offline!"

        if duration:
            if not 10 <= duration <= 30000:
                return "Can't ban {0}'s with duration {1}! Specify a value between 10 and 30000.".format(toon.getName(), duration)

        if toon.getDoId() not in simbase.air.doId2do.keys() or invoker.getDoId() not in simbase.air.doId2do.keys():
            simbase.air.writeServerEvent('suspicious', issue="Invalid invoker: %s and target: %s when trying to ban them." % (invoker.getDoId(), toon.getDoId()))
            return "Failed to ban the target!"

        if not isinstance(toon, DistributedToonAI) and not isinstance(invoker, DistributedToonAI):
            return "You can only ban a Toon."
        else:
            toon.sendSetBan(reason=reason, target=toon, invoker=invoker, duration=duration)
            return "Banned %s!" % toon.getName()


class Kick(MagicWord):
    administrative = True
    desc = "Kicks the target."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("reason", str, False, "Not specified.")]
    accessLevel = "MODERATOR"
    affectRange = [MagicWordConfig.AFFECT_OTHER]

    def handleWord(self, invoker, avId, toon, *args):
        from toontown.toon.DistributedToonAI import DistributedToonAI
        reason = args[0]

        if toon.getDoId() not in simbase.air.doId2do.keys() or invoker.getDoId() not in simbase.air.doId2do.keys():
            simbase.air.writeServerEvent('suspicious',
                                        issue="Invalid invoker: %s and target: %s when trying to kick them." % (
                                            invoker.getDoId(), toon.getDoId()))
            return "Failed to kick avatar!"

        # Verify that we're a toon.
        if not isinstance(toon, DistributedToonAI) and not isinstance(invoker, DistributedToonAI):
            return "You can only kick an avatar."
        else:
            if toon.getDoId() == invoker.getDoId():
                return "You can\'t kick yourself, %s" % toon.getName()
            else:
                toon.sendSetKick(reason=reason, target=toon, invoker=invoker, silent=3)
                return "Kicked %s!" % toon.getName()


class GetInvasionStatus(MagicWord):
    aliases = ['InvasionStatus']
    desc = "Returns the number of cogs remaining in an invasion."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER

    def handleWord(self, invoker, avId, toon, *args):
        invasionMgr = simbase.air.suitInvasionManager

        if not invasionMgr.getInvading():
            return "There is no invasion in progress!"

        invadingCog = invasionMgr.getInvadingCog()
        simbase.air.newsManager.sendUpdateToAvatarId(invoker.getDoId(), 'setInvasionStatus', [
            ToontownGlobals.SuitInvasionUpdate, invadingCog[0], invasionMgr.numSuits, invadingCog[1]])


class RevealMap(MagicWord):
    desc = "Reveals map in the Sellbot Field Office maze game."
    execLocation = MagicWordConfig.EXEC_LOC_CLIENT

    def handleWord(self, invoker, avId, toon, *args):
        mazeGame = None
        from toontown.cogdominium.DistCogdoMazeGame import DistCogdoMazeGame
        for do in base.cr.doId2do.values():
            if isinstance(do, DistCogdoMazeGame):
                if invoker.doId in do.getToonIds():
                    mazeGame = do
                    break

        if mazeGame:
            mazeGame.game.guiMgr.mazeMapGui.showExit()
            mazeGame.game.guiMgr.mazeMapGui.revealAll()
            return "Map revealed!"

        return "You are not in a Maze Game!"

class EndMaze(MagicWord):
    desc = "Ends the maze game in a Sellbot Field Office."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER

    def handleWord(self, invoker, avId, toon, *args):
        mazeGame = None
        from toontown.cogdominium.DistCogdoMazeGameAI import DistCogdoMazeGameAI
        for do in simbase.air.doId2do.values():
            if isinstance(do, DistCogdoMazeGameAI):
                if invoker.doId in do.getToonIds():
                    mazeGame = do
                    break

        if mazeGame:
            mazeGame.openDoor()
            return "Completed Maze Game"

        return "You are not in a Maze Game!"


class SpawnBuilding(MagicWord):
    aliases = ["building", "spawnbldg", "bldg"]
    desc = "Spawns a Cog Building with the given suit index."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("suitName", str, True)]

    def handleWord(self, invoker, avId, toon, *args):
        suitName = args[0]

        try:
            suitIndex = SuitDNA.suitHeadTypes.index(suitName)
        except:
            return "Invalid Cog specified.".format(suitName)

        if suitName in SuitDNA.extraSuits.keys():
            return "Custom Cogs cannot take over buildings."

        returnCode = invoker.doBuildingTakeover(suitIndex)
        if returnCode[0] == 'success':
            return "Successfully spawned building with Cog '{0}'!".format(suitName)
        return "Couldn't spawn building with Cog '{0}'.".format(suitName)


class SpawnFO(MagicWord):
    aliases = ["fo", "spawncogdo", "cogdo"]
    desc = "Spawns a Field Office with the given type and difficulty."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("type", str, True), ("difficulty", int, False, 0)]

    def handleWord(self, invoker, avId, toon, *args):
        from toontown.building import SuitBuildingGlobals
        track = args[0]
        difficulty = args[1]

        tracks = ['s', 'l']
        if track not in tracks:
            return "Invalid Field Office type! Supported types are 's' and 'l'"
        if not 0 <= difficulty < len(SuitBuildingGlobals.SuitBuildingInfo):
            return "Difficulty out of bounds!"

        try:
            building = invoker.findClosestDoor()
        except KeyError:
            return "You\'re not on a street!"
        if building is None:
            return "Unable to spawn a %s Field Office with a difficulty of %d." % (ToontownGlobals.Dept2Dept.get(track), difficulty)

        building.cogdoTakeOver(track, difficulty, 2)
        return "Successfully spawned a %s Field Office with a difficulty of %d!" % (ToontownGlobals.Dept2Dept.get(track), difficulty)


class SetCEIndex(MagicWord):
    aliases = ["setce", "ce", "cheesyeffect"]
    desc = "Set Cheesy Effect of the target."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("index", int, True), ("zoneId", int, False, 0), ("duration", int, False, 0)]

    def handleWord(self, invoker, avId, toon, *args):
        """Set Cheesy Effect of the target."""
        index = args[0]
        zoneId = args[1]
        duration = args[2]

        if not 0 <= index <= 17:
            return "Invalid value %s specified for Cheesy Effect." % index
        if index == 17 and (not hasattr(self.air, 'holidayManager') or not self.air.holidayManager.isHolidayRunning(ToontownGlobals.APRIL_FOOLS)):
            return "Invalid value %s specified for Cheesy Effect." % index
        if zoneId != 0 and not 100 < zoneId < ToontownGlobals.DynamicZonesBegin:
            return "Invalid zoneId specified."
        toon.b_setCheesyEffect(index, zoneId, time.time() + duration)
        return "Cheesy effect set for {}".format(toon.getName())

class SetFishingRod(MagicWord):
    aliases = ["rod", "setrod"]
    desc = "Set target's fishing rod value."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("rodVal", int, True)]

    def handleWord(self, invoker, avId, toon, *args):
        rodVal = args[0]
        if not 0 <= rodVal <= 4:
            return "Rod value must be between 0 and 4."
        toon.b_setFishingRod(rodVal)
        return "Rod changed to " + str(rodVal)


class SetFishingBucket(MagicWord):
    aliases = ["fishbucket", "bucket", "maxtank"]
    desc = "Set target's max fish tank value."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("tankVal", int, True)]

    def handleWord(self, invoker, avId, toon, *args):
        tankVal = args[0]
        if not 20 <= tankVal <= 99:
            return "Max fish tank value must be between 20 and 99"
        toon.b_setMaxFishTank(tankVal)
        return "Max size of fish tank changed to " + str(tankVal)


class SetPlayRate(MagicWord):
    aliases = ["playrate"]
    desc = "Set target's play rate."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("playRate", float, False, 1.0)]

    def handleWord(self, invoker, avId, toon, *args):
        rate = args[0]
        toon.d_setAnimPlayRate(rate)
        if rate == 1:
            return "Set playrate to normal!"

        return 'Set play rate to {}'.format(rate)


class SetName(MagicWord):
    aliases = ["name"]
    desc = "Set target's name."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("name", str, True)]

    def handleWord(self, invoker, avId, toon, *args):
        nameStr = args[0]
        oldName = toon.getName()

        if not nameStr:
            return "Cannot change %s's name to nothing!" % oldName
        elif ":" in nameStr:
            return "Cannot change %s's name to %s. Invalid characters specified." % (oldName, nameStr)

        toon.b_setName(nameStr)
        return "Changed %s's name to %s!" % (oldName, nameStr)


class SetHat(MagicWord):
    aliases = ["hat"]
    desc = "Set hat of target toon."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("id", int, True), ("textureId", int, False, 0)]

    def handleWord(self, invoker, avId, toon, *args):
        hatId = args[0]
        hatTex = args[1]

        if hatId == 58:
            return "Invalid hat specified."
        if not 0 <= hatId <= 60:
            return "Invalid hat specified."
        if not 0 <= hatTex <= 40:
            return "Invalid hat texture specified."
        toon.b_setHat(hatId, hatTex, 0)
        return "{}'s hat has been set to {} with texture {}".format(toon.getName(),hatId,hatText)


class SetGlasses(MagicWord):
    aliases = ["glasses"]
    desc = "Set glasses of target toon."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("id", int, True), ("textureId", int, False, 0)]

    def handleWord(self, invoker, avId, toon, *args):
        glassesId = args[0]
        glassesTex = args[1]

        if not 0 <= glassesId <= 24:
            return "Invalid glasses specified."
        if not 0 <= glassesTex <= 25:
            return "Invalid glasses texture specified."
        toon.b_setGlasses(glassesId, glassesTex, 0)
        return "{}'s Glasses have been set to {} with texture {}".format(toon.getName(), glassesId, glassesTex)


class SetBackpack(MagicWord):
    aliases = ["backpack"]
    desc = "Set backpack of target toon."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("id", int, True), ("textureId", int, False, 0)]

    def handleWord(self, invoker, avId, toon, *args):
        bpId = args[0]
        bpTex = args[1]

        if not 0 <= bpId <= 26:
            return "Invalid backpack specified."
        if not 0 <= bpTex <= 22:
            return "Invalid backpack texture specified."
        toon.b_setBackpack(bpId, bpTex, 0)
        return "{}'s backpack has been set to {} with texture {}".format(toon.getName(), bpId, bpTex)

class SetShoes(MagicWord):
    aliases = ["shoes"]
    desc = "Set shoes of target toon."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("id", int, True), ("textureId", int, False, 0)]

    def handleWord(self, invoker, avId, toon, *args):
        shoesId = args[0]
        shoesTex = args[1]

        if not 0 <= shoesId <= 3:
            return "Invalid shoe type specified."
        if (shoesTex == 54 and not __debug__) or not 0 <= shoesTex <= 54:
            return "Invalid shoe specified."
        toon.b_setShoes(shoesId, shoesTex, 0)
        return "{}'s shoes have been set to {} with texture {}".format(toon.getName(), shoesId, shoesTex)

class ClearAccessories(MagicWord):
    aliases = ["removeallaccessories", "removeaccessories"]
    desc = "Clear's all the accessories of the target."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER

    def handleWord(self, invoker, avId, toon, *args):
        toon.b_setHat(0, 0, 0)
        toon.b_setGlasses(0, 0, 0)
        toon.b_setBackpack(0, 0, 0)
        toon.b_setShoes(0, 0, 0)
        return "Cleared the target's accessories."


class SetInventory(MagicWord):
    aliases = ["inventory"]
    desc = "Modify gag inventory. Can reset (clear) inventory or restock."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("command", str, True), ("level", int, False, 5), ("track", int, False, -1)]

    def handleWord(self, invoker, avId, toon, *args):
        type = args[0]
        level = args[1]
        track = args[2]

        inventory = toon.inventory
        if type in ('reset', 'clear'):
            maxLevelIndex = level or 5
            if not 0 <= maxLevelIndex < len(ToontownBattleGlobals.Levels[0]):
                return "Invalid max level index: {0}".format(maxLevelIndex)
            targetTrack = -1 or track
            if not -1 <= targetTrack < len(ToontownBattleGlobals.Tracks):
                return "Invalid target track index: {0}".format(targetTrack)
            for track in xrange(0, len(ToontownBattleGlobals.Tracks)):
                if (targetTrack == -1) or (track == targetTrack):
                    inventory.inventory[track][:maxLevelIndex + 1] = [0] * (maxLevelIndex + 1)
            toon.b_setInventory(inventory.makeNetString())
            if targetTrack == -1:
                return "Inventory cleared."
            else:
                return "Inventory cleared for target track index: {0}".format(targetTrack)
        elif type == "restock":
            maxLevelIndex = level or 5
            if not 0 <= maxLevelIndex < len(ToontownBattleGlobals.Levels[0]):
                return "Invalid max level index: {0}".format(maxLevelIndex)
            targetTrack = -1 or track
            if not -1 <= targetTrack < len(ToontownBattleGlobals.Tracks):
                return "Invalid target track index: {0}".format(targetTrack)
            if (targetTrack != -1) and (not toon.hasTrackAccess(targetTrack)):
                return "The target Toon doesn't have target track index: {0}".format(targetTrack)
            inventory.NPCMaxOutInv(targetTrack=targetTrack, maxLevelIndex=maxLevelIndex)
            toon.b_setInventory(inventory.makeNetString())
            if targetTrack == -1:
                return "Inventory restocked."
            else:
                return "Inventory restocked for target track index: {0}".format(targetTrack)
        else:
            try:
                targetTrack = int(type)
            except:
                return "Invalid first argument."
            if not toon.hasTrackAccess(targetTrack):
                return "The target Toon doesn't have target track index: {0}".format(targetTrack)
            maxLevelIndex = level or 6
            if not 0 <= maxLevelIndex < len(ToontownBattleGlobals.Levels[0]):
                return "Invalid max level index: {0}".format(maxLevelIndex)
            for _ in xrange(track):
                inventory.addItem(targetTrack, maxLevelIndex)
                toon.b_setInventory(inventory.makeNetString())
            return "Restored {0} Gags to: {1}, {2}".format(track, targetTrack, maxLevelIndex)


class ToggleGM(MagicWord):
    desc = "Toggle the target's GM icon."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER

    def handleWord(self, invoker, avId, toon, *args):
        access = invoker.getAccessLevel()
        if invoker.isGM():
            invoker.b_setGM(0)
            return "You have disabled your GM icon."
        else:
            if access >= 800:
                invoker.b_setGM(5)
            elif access >= 700:
                invoker.b_setGM(6)
            elif access >=600:
                invoker.b_setGM(8)
                invoker.b_setGM(7)
                invoker.b_setGM(4)
            elif access >= 500:
                invoker.b_setGM(3)
            elif access >= 400:
                invoker.b_setGM(2)
            elif access >= 200:
                invoker.b_setGM(1)
            return "You have enabled your GM icon."


class ToggleGhost(MagicWord):
    aliases = ["ghost"]
    desc = "Set toon to invisible."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    accessLevel = 'MODERATOR'

    def handleWord(self, invoker, avId, toon, *args):
        if invoker.ghostMode == 0:
            invoker.b_setGhostMode(2)
            return "Going ghost!"
        else:
            invoker.b_setGhostMode(0)
            return "Back to normal!"


class SetGM(MagicWord):
    aliases = ["gmicon", "gm"]
    desc = "Set the target's GM Icon."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("id", int, True), ("name", bool, False, False)]
    accessLevel = 'MODERATOR'

    def handleWord(self, invoker, avId, toon, *args):
        gmId = args[0]
        name = args[1]

        #if gmId == 1:
        #    return 'This GM is reserved for the Toon Council. Use ~setGM 2 instead.'

        if not 0 <= gmId <= 8:
            return "Invalid GM Icon specified."

        accessLevel = toon.getAccessLevel()
        if gmId > 3 and accessLevel < 600:
            return "Your access level is too low to use this GM icon."
        else:
            if (accessLevel < 400 and gmId > 2) or (accessLevel < 500 and gmId > 3):
                return "Your access level is too low to use this GM icon."

        if toon.isGM() and gmId != 0:
            toon.b_setGM(0, name)
        elif toon.isGM and gmId == 0:
            toon.b_setGM(0, True)

        toon.b_setGM(gmId, name)

        if __debug__:
            pass
        else:
            toon.d_requestVerifyGM()

        return "You have set %s to GM type %s" % (toon.getName(), gmId)


class SetTickets(MagicWord):
    aliases = ["tickets"]
    desc = "Set the target's racing ticket's value."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("val", int, True)]

    def handleWord(self, invoker, avId, toon, *args):
        tixVal = args[0]
        if not 0 <= tixVal <= 99999:
            return "Ticket value out of range (0-99999)"
        toon.b_setTickets(tixVal)
        return "%s's tickets were set to %s." % (toon.getName(), tixVal)


class TransformCog(MagicWord):
    aliases = ["setcogindex", "cogindex"]
    desc = "Set the target's cog index."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("department", int, False, -1), ("cogType", int, False, 0)]

    def handleWord(self, invoker, avId, toon, *args):
        deptIndex = args[0]
        cogType = args[1]

        if (not -1 <= deptIndex <= 3) and (not 50 <= deptIndex <= 52):
            return "The cog department index must be between 0 and 3!"

        if (not -1 <= deptIndex <= 3) and cogType == 9:
            return "You cannot put Custom Cogs in a Rental Suit."

        toon.b_setCogIndex(deptIndex, cogType, 2)
        return "Transofrmed {} to {} {}".format(toon.getName(), deptIndex, cogType)


class SetDNA(MagicWord):
    aliases = ["dna"]
    desc = "Set a specific part of DNA for the target Toon."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("part", str, True), ("val", str, False, 0)]

    def handleWord(self, invoker, avId, toon, *args):
        part = args[0]
        value = args[1]

        # This is where the fun begins, woo!

        dna = ToonDNA.ToonDNA()
        dna.makeFromNetString(toon.getDNAString())

        part = part.lower()

        def isValidColor(colorIndex):
            if not 0 <= colorIndex <= len(ToonDNA.allColorsList) - 1:
                return False
            return True

        # Body Part Colors
        colorInt = -1
        if value.title() in ToonDNA.colorToInt.keys():
            colorInt = ToonDNA.colorToInt[value.title()]
        try:
            colorInt = int(value)
        except:
            pass

        if part == 'headcolor':
            value = value.title()
            if value not in ToonDNA.colorToInt.keys() and not isValidColor(colorInt):
                return "DNA: Invalid color specified for head."
            dna.headColor = colorInt

        elif part == 'armcolor':
            value = value.title()
            if value not in ToonDNA.colorToInt.keys() and not isValidColor(colorInt):
                return "DNA: Invalid color specified for arms."
            dna.armColor = colorInt

        elif part == 'legcolor':
            value = value.title()
            if value not in ToonDNA.colorToInt.keys() and not isValidColor(colorInt):
                return "DNA: Invalid color specified for legs."
            dna.legColor = colorInt

        elif part == 'color':
            value = value.title()
            if value not in ToonDNA.colorToInt.keys() and not isValidColor(colorInt):
                return "DNA: Invalid color specified for toon."
            dna.headColor = colorInt
            dna.armColor = colorInt
            dna.legColor = colorInt

        elif part == 'gloves':
            value = value.title()
            if value not in ToonDNA.colorToInt.keys() and not isValidColor(colorInt):
                return "DNA: Color index out of range."
            dna.gloveColor = colorInt

        # Body Sizes, Species & Gender (y u want to change gender pls)
        elif part == 'gender':
            if value.lower() == 'male' or value.lower() == 'm' or value == '0':
                dna.gender = 'm'
            elif value.lower() == 'female' or value.lower() == 'f' or value == '1':
                dna.gender = 'f'
            else:
                return "DNA: Invalid gender. Stick to 'male' or 'female'."

        elif part == 'species':
            species = ['dog', 'cat', 'horse', 'mouse', 'rabbit', 'duck', 'monkey', 'bear', 'pig', 'gyro', 'scrooge']
            if value.lower() not in species:
                return "DNA: Invalid head type specified."
            species = dict(map(None, species, ToonDNA.toonSpeciesTypes))
            headSize = dna.head[1:3]
            if value in ['gyro', 'scrooge']:
                headSize = 'ss'
            elif value == 'mouse':
                if headSize in ['sl', 'll']:
                    headSize = 'ls'
            dna.head = (species.get(value) + headSize)

        elif part == 'headsize':
            sizes = ['ls', 'ss', 'sl', 'll']
            species = dna.head[0]
            try:
                value = int(value)
            except ValueError:
                return "Invalid type of value!"
            print species
            if species in ['i', 'o']:
                return "DNA: Cannot change the head size of this species."
            elif species == 'm':
                if not 0 <= value <= 1:
                    return "DNA: Invalid head size index."
            else:
                if not 0 <= value <= 3:
                    return "DNA: Invalid head size index."
            if species == 'g':
                value == 2
            elif species == 'o':
                value == 3
            elif species == 'i':
                value == 1
            dna.head = (species + sizes[value])

        elif part == 'torso':
            try:
                value = int(value)
            except ValueError:
                return "Invalid type of value!"
            if dna.gender == 'm':
                if not 0 <= value <= 2:
                    return "DNA: Male torso index out of range (0-2)."
            elif dna.gender == 'f':
                if not 3 <= value <= 8:
                    return "DNA: Female torso index out of range (3-8)."
                if 6 <= value <= 8:
                    value = value - 6
            else:
                return "DNA: Unable to determine gender. Aborting DNA change."
            dna.torso = ToonDNA.toonTorsoTypes[value]

        elif part == 'legs':
            try:
                value = int(value)
            except ValueError:
                return "Invalid type of value!"
            if not 0 <= value <= 2:
                return "DNA: Legs index out of range."
            dna.legs = ToonDNA.toonLegTypes[value]

        # Clothing.
        elif part == 'toptex':
            if len(dna.torso) == 1:
                return 'What clothing?'
            try:
                value = int(value)
            except ValueError:
                return "Invalid type of value!"
            if value == 160 and not __debug__:
                return 'Invalid top texture index.'
            elif not 0 <= value <= len(ToonDNA.Shirts):
                return 'Top texture index out of range (0-{0}).'.format(
                    len(ToonDNA.Shirts))
            dna.topTex = value

        elif part == 'toptexcolor':
            if len(dna.torso) == 1:
                return 'What clothing?'
            try:
                value = int(value)
            except ValueError:
                return "Invalid type of value!"
            if not 0 <= value <= len(ToonDNA.ClothesColors):
                return 'Top texture color index out of range(0-{0}).'.format(
                    len(ToonDNA.ClothesColors))
            dna.topTexColor = value

        elif part == 'sleevetex':
            if len(dna.torso) == 1:
                return 'What clothing?'
            try:
                value = int(value)
            except ValueError:
                return "Invalid type of value!"
            if value == 149 and not __debug__:
                return 'Invalid sleeve texture index.'
            elif not 0 <= value <= len(ToonDNA.Sleeves):
                return 'Sleeve texture index out of range(0-{0}).'.format(
                    len(ToonDNA.Sleeves))
            dna.sleeveTex = value

        elif part == 'sleevetexcolor':
            if len(dna.torso) == 1:
                return 'What clothing?'
            try:
                value = int(value)
            except ValueError:
                return "Invalid type of value!"
            if not 0 <= value <= len(ToonDNA.ClothesColors):
                return 'Sleeve texture color index out of range(0-{0}).'.format(
                    len(ToonDNA.ClothesColors))
            dna.sleeveTexColor = value

        elif part == 'bottex':
            if len(dna.torso) == 1:
                return 'What clothing?'
            try:
                value = int(value)
            except ValueError:
                return "Invalid type of value!"
            if dna.gender not in ('m', 'f'):
                return 'Unknown gender.'
            if dna.gender == 'm':
                if value == 67 and not __debug__:
                    return 'Invalid bottom texture index.'
                bottoms = ToonDNA.BoyShorts
            else:
                bottoms = ToonDNA.GirlBottoms
            if not 0 <= value <= len(bottoms):
                return 'Bottom texture index out of range (0-{0}).'.format(
                    len(bottoms))
            dna.botTex = value

        elif part == 'bottexcolor':
            if len(dna.torso) == 1:
                return 'What clothing?'
            try:
                value = int(value)
            except ValueError:
                return "Invalid type of value!"
            if not 0 <= value <= len(ToonDNA.ClothesColors):
                return 'Bottom texture color index out of range(0-{0}).'.format(
                    len(ToonDNA.ClothesColors))
            dna.botTexColor = value

        else:
            return "DNA: Invalid part specified."

        toon.b_setDNAString(dna.makeNetString())
        return "Completed DNA change successfully."


class GrowFlowers(MagicWord):
    desc = "Grow a target's flowers."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER

    def handleWord(self, invoker, avId, toon, *args):
        estate = toon.air.estateMgr._lookupEstate(toon)

        if not estate:
            return "Estate not found!"

        house = estate.getAvHouse(avId)
        garden = house.gardenManager.gardens.get(toon.doId)
        if not garden:
            return "Garden not found!"

        now = int(time.time())
        i = 0
        for flower in garden.flowers:
            flower.b_setWaterLevel(5)
            flower.b_setGrowthLevel(2)
            flower.update()
            i += 1

        return "%d flowers grown." % i


class PickAllFlowers(MagicWord):
    aliases = ["pickflowers"]
    desc = "Picks all of the target's flowers."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER

    def handleWord(self, invoker, avId, toon, *args):
        estate = toon.air.estateMgr._lookupEstate(toon)

        if not estate:
            return "Estate not found!"

        house = estate.getAvHouse(avId)
        garden = house.gardenManager.gardens.get(toon.doId)
        if not garden:
            return "Garden not found!"

        i = 0
        for flower in garden.flowers.copy():
            if flower.getGrowthLevel() >= flower.growthThresholds[2]:
                flower.removeItem(1)
                i += 1

        return "%d flowers picked." % i


class GrowTrees(MagicWord):
    desc = "Grows the target's trees."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("track", str, True), ("index", int, True), ("amount", int, False, 21)]

    def handleWord(self, invoker, avId, toon, *args):
        track = args[0]
        index = args[1]
        grown = args[2]

        estate = toon.air.estateMgr._lookupEstate(toon)

        if not estate:
            return "Estate not found!"

        house = estate.getAvHouse(avId)
        garden = house.gardenManager.gardens.get(toon.doId)
        if not garden:
            return "Garden not found!"

        try:
            trackIndex = ('toonup', 'trap', 'lure', 'sound', 'throw',
                     'squirt', 'drop').index(track)
        except ValueError:
            # Backwards compatibility
            try:
                trackIndex = int(track)
            except ValueError:
                return 'Gag track is invalid.'

        if trackIndex > 6:
            return 'Gag track is invalid.'

        tree = garden.getTree(trackIndex, index)
        if not tree:
            return "Tree not found!"

        result = tree.doGrow(grown)
        return '%d trees grown.' % result


class PickTrees(MagicWord):
    desc = "Picks the target's trees."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("track", str, True), ("index", int, True)]

    def handleWord(self, invoker, avId, toon, *args):
        track = args[0]
        index = args[1]
        estate = toon.air.estateMgr._lookupEstate(toon)

        if not estate:
            return "Estate not found!"

        house = estate.getAvHouse(avId)
        garden = house.gardenManager.gardens.get(toon.doId)
        if not garden:
            return "Garden not found!"

        try:
            trackIndex = ('toonup', 'trap', 'lure', 'sound', 'throw',
                     'squirt', 'drop').index(track)
        except ValueError:
            # Backwards compatibility
            try:
                trackIndex = int(track)
            except ValueError:
                return 'Gag track is invalid.'

        if trackIndex > 6:
            return 'Gag track is invalid.'

        tree = garden.getTree(trackIndex, index)
        if not tree:
            return "Tree not found!"

        tree.calculate(0, tree.lastCheck)
        tree.sendUpdate('setFruiting', [tree.getFruiting()])
        return "Trees picked."


class FlowerAll(MagicWord):
    desc = "Flowers the target's flowers."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("species", int, False, 49), ("variety", int, False, 0)]

    def handleWord(self, invoker, avId, toon, *args):
        species = args[0]
        variety = args[1]


        estate = toon.air.estateMgr._lookupEstate(toon)
        if not estate:
            return "Estate not found!"

        house = estate.getAvHouse(avId)
        garden = house.gardenManager.gardens.get(toon.doId)
        if not garden:
            return "Garden not found!"

        from toontown.estate.DistributedGardenPlotAI import DistributedGardenPlotAI
        i = 0
        for obj in garden.objects.copy():
            if isinstance(obj, DistributedGardenPlotAI):
                if obj.plotType != GardenGlobals.FLOWER_TYPE:
                    continue

                if not obj.plantFlower(species, variety, 1):
                    return "Error on plot %d!" % i

                i += 1

        return "%d flowers planted." % i


class RestockFlowerSpecials(MagicWord):
    desc = "Give special flowers."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER

    def handleWord(self, invoker, avId, toon, *args):
        toon.gardenSpecials = []
        for x in (100, 101, 102, 103, 105, 106, 107, 108, 109, 130, 131, 135):
            toon.addGardenItem(x, 99)
        return "Special flowers restocked."

class MaxDoodle(MagicWord):
    desc = "Maxes the target's doodle."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER

    def handleWord(self, invoker, avId, toon, *args):
        petId = invoker.getPetId()
        pet = simbase.air.doId2do.get(petId)
        if not pet:
            return "You must be at your estate and own a doodle to use this magic word!"

        pet.b_setTrickAptitudes([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
        return "Maxed your doodle!"


class LeaveRace(MagicWord):
    desc = "Leave the current race you are in."
    execLocation = MagicWordConfig.EXEC_LOC_CLIENT

    def handleWord(self, invoker, avId, toon, *args):
        messenger.send('leaveRace')

        return "You're done!!"


class SkipCFO(MagicWord):
    desc = "Skips to the indicated round of the CFO."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("round", str, False, "next")]
    accessLevel = "MODERATOR"

    def handleWord(self, invoker, avId, toon, *args):
        battle = args[0]

        from toontown.suit.DistributedCashbotBossAI import DistributedCashbotBossAI
        boss = None
        for do in simbase.air.doId2do.values():
            if isinstance(do, DistributedCashbotBossAI):
                if invoker.doId in do.involvedToons:
                    boss = do
                    break
        if not boss:
            return "You aren't in a CFO!"

        battle = battle.lower()

        if battle == 'two':
            if boss.state in ('PrepareBattleThree', 'BattleThree'):
                return "You can not return to previous rounds!"
            else:
                boss.exitIntroduction()
                boss.b_setState('PrepareBattleThree')
                return "Skipping to last round..."

        if battle == 'next':
            if boss.state in ('PrepareBattleOne', 'BattleOne'):
                boss.exitIntroduction()
                boss.b_setState('PrepareBattleThree')
                return "Skipping current round..."
            elif boss.state in ('PrepareBattleThree', 'BattleThree'):
                boss.exitIntroduction()
                boss.b_setState('Victory')
                return "Skipping final round..."


class HitBoss(MagicWord):
    desc = "Hits the boss cog if you're in a boss."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("damage", int, False, 1)]
    accessLevel = "MODERATOR"

    def handleWord(self, invoker, avId, toon, *args):
        dmg = args[0]

        if dmg < 1:
            return "Damage must be at least 1."

        from toontown.suit.DistributedBossCogAI import DistributedBossCogAI
        boss = None
        for do in simbase.air.doId2do.values():
            if isinstance(do, DistributedBossCogAI):
                if invoker.doId in do.involvedToons:
                    boss = do
                    break

        if not boss:
            return "You aren't in a boss battle!"

        boss.magicWordHit(dmg, invoker.doId)
        return "Hit boss for {0} damage.".format(dmg)


class DisableGoons(MagicWord):
    desc = "Stuns all of the goons in an area."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    accessLevel = "MODERATOR"

    def handleWord(self, invoker, avId, toon, *args):
        from toontown.suit.DistributedGoonAI import DistributedGoonAI
        for goon in simbase.air.doFindAllInstances(DistributedGoonAI):
            goon.requestStunned(0)
        return "Disabled all Goons!"

class ResetCFOObjects(MagicWord):
    desc = "Resets the state of cranes and safes in the CFO."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    accessLevel = "MODERATOR"

    def handleWord(self, invoker, avId, toon, *args):
        from toontown.suit.DistributedCashbotBossAI import DistributedCashbotBossAI
        boss = None
        for do in simbase.air.doId2do.values():
            if isinstance(do, DistributedCashbotBossAI):
                if invoker.doId in do.involvedToons:
                    boss = do
                    break
        if not boss:
            return "You aren't in a CFO!"

        if boss.state == 'BattleThree':
            boss.magicWordReset()
            return "Reset cranes and safes!"

        return 'You must be in the crane round!'


class DestroyCFOGoons(MagicWord):
    desc = "Stuns all of the goons in a CFO."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER

    def handleWord(self, invoker, avId, toon, *args):
        from toontown.suit.DistributedCashbotBossAI import DistributedCashbotBossAI
        boss = None
        for do in simbase.air.doId2do.values():
            if isinstance(do, DistributedCashbotBossAI):
                if invoker.doId in do.involvedToons:
                    boss = do
                    break
        if not boss:
            return "You aren't in a CFO!"

        if boss.state == 'BattleThree':
            boss.magicWordResetGoons()
            return "Destroyed all Goons!"

        return 'You must be in the crane round!'


class SkipCJ(MagicWord):
    desc = "Skips to the indicated round of the CJ."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("round", str, False, "next")]
    accessLevel = "MODERATOR"

    def handleWord(self, invoker, avId, toon, *args):
        battle = args[0]
        from toontown.suit.DistributedLawbotBossAI import DistributedLawbotBossAI
        boss = None
        for do in simbase.air.doId2do.values():
            if isinstance(do, DistributedLawbotBossAI):
                if invoker.doId in do.involvedToons:
                    boss = do
                    break
        if not boss:
            return "You aren't in a CJ!"

        battle = battle.lower()

        if battle == 'two':
            if boss.state in ('RollToBattleTwo', 'PrepareBattleTwo', 'BattleTwo', 'PrepareBattleThree', 'BattleThree'):
                return "You can not return to previous rounds!"
            else:
                boss.exitIntroduction()
                boss.b_setState('RollToBattleTwo')
                return "Skipping to second round..."

        if battle == 'three':
            if boss.state in ('PrepareBattleThree', 'BattleThree'):
                return "You can not return to previous rounds!"
            else:
                boss.exitIntroduction()
                boss.b_setState('PrepareBattleThree')
                return "Skipping to final round..."

        if battle == 'next':
            if boss.state in ('PrepareBattleOne', 'BattleOne'):
                boss.exitIntroduction()
                boss.b_setState('RollToBattleTwo')
                return "Skipping current round..."
            elif boss.state in ('RollToBattleTwo', 'PrepareBattleTwo', 'BattleTwo'):
                boss.exitIntroduction()
                boss.b_setState('PrepareBattleThree')
                return "Skipping current round..."
            elif boss.state in ('PrepareBattleThree', 'BattleThree'):
                boss.exitIntroduction()
                boss.enterNearVictory()
                boss.b_setState('Victory')
                return "Skipping final round..."


class FillJury(MagicWord):
    desc = "Fills all of the chairs in the CJ's Jury Round."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    accessLevel = "MODERATOR"

    def handleWord(self, invoker, avId, toon, *args):
        boss = None
        from toontown.suit.DistributedLawbotBossAI import DistributedLawbotBossAI
        for do in simbase.air.doId2do.values():
            if isinstance(do, DistributedLawbotBossAI):
                if invoker.doId in do.involvedToons:
                    boss = do
                    break
        if not boss:
            return "You aren't in a CJ!"
        if not boss.state == 'BattleTwo':
            return "You aren't in the cannon round."
        for i in xrange(len(boss.chairs)):
            boss.chairs[i].b_setToonJurorIndex(0)
            boss.chairs[i].requestToonJuror()
        return "Filled chairs."


class SkipVP(MagicWord):
    desc = "Skips to the indicated round of the VP."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("round", str, False, "next")]
    accessLevel = "MODERATOR"

    def handleWord(self, invoker, avId, toon, *args):
        battle = args[0]
        from toontown.suit.DistributedSellbotBossAI import DistributedSellbotBossAI
        boss = None
        for do in simbase.air.doId2do.values():
            if isinstance(do, DistributedSellbotBossAI):
                if invoker.doId in do.involvedToons:
                    boss = do
                    break
        if not boss:
            return "You aren't in a VP!"

        battle = battle.lower()

        if battle == 'three':
            if boss.state in ('PrepareBattleThree', 'BattleThree'):
                return "You can not return to previous rounds!"
            else:
                boss.exitIntroduction()
                boss.b_setState('PrepareBattleThree')
                return "Skipping to final round..."

        if battle == 'next':
            if boss.state in ('PrepareBattleOne', 'BattleOne'):
                boss.exitIntroduction()
                boss.b_setState('PrepareBattleThree')
                return "Skipping current round..."
            elif boss.state in ('PrepareBattleThree', 'BattleThree'):
                boss.exitIntroduction()
                boss.b_setState('Victory')
                return "Skipping final round..."


class StunVP(MagicWord):
    desc = "Stuns the VP in the final round of his battle."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    accessLevel = "MODERATOR"

    def handleWord(self, invoker, avId, toon, *args):
        from toontown.suit.DistributedSellbotBossAI import DistributedSellbotBossAI
        boss = None
        for do in simbase.air.doId2do.values():
            if isinstance(do, DistributedSellbotBossAI):
                if invoker.doId in do.involvedToons:
                    boss = do
                    break
        if not boss:
            return "You aren't in a VP!"
        currState = boss.getCurrentOrNextState()
        if currState != 'BattleThree':
            return "You aren't in the final round of a VP!"
        boss.b_setAttackCode(ToontownGlobals.BossCogDizzyNow)
        boss.b_setBossDamage(boss.getBossDamage(), 0, 0)


class SkipCEO(MagicWord):
    desc = "Skips to the indicated round of the CEO."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("round", str, False, "next")]
    accessLevel = "MODERATOR"

    def handleWord(self, invoker, avId, toon, *args):
        battle = args[0]
        from toontown.suit.DistributedBossbotBossAI import DistributedBossbotBossAI
        boss = None
        for do in simbase.air.doId2do.values():
            if isinstance(do, DistributedBossbotBossAI):
                if invoker.doId in do.involvedToons:
                    boss = do
                    break
        if not boss:
            return "You aren't in a CEO!"

        battle = battle.lower()

        if battle == 'two':
            if boss.state in ('PrepareBattleFour', 'BattleFour', 'PrepareBattleThree', 'BattleThree', 'PrepareBattleTwo', 'BattleTwo'):
                return "You can not return to previous rounds!"
            else:
                boss.exitIntroduction()
                boss.b_setState('PrepareBattleTwo')
                return "Skipping to second round..."

        if battle == 'three':
            if boss.state in ('PrepareBattleFour', 'BattleFour', 'PrepareBattleThree', 'BattleThree'):
                return "You can not return to previous rounds!"
            else:
                boss.exitIntroduction()
                boss.b_setState('PrepareBattleThree')
                return "Skipping to third round..."

        if battle == 'four':
            if boss.state in ('PrepareBattleFour', 'BattleFour'):
                return "You can not return to previous rounds!"
            else:
                boss.exitIntroduction()
                boss.b_setState('PrepareBattleFour')
                return "Skipping to last round..."

        if battle == 'next':
            if boss.state in ('PrepareBattleOne', 'BattleOne'):
                boss.exitIntroduction()
                boss.b_setState('PrepareBattleTwo')
                return "Skipping current round..."
            elif boss.state in ('PrepareBattleTwo', 'BattleTwo'):
                boss.exitIntroduction()
                boss.b_setState('PrepareBattleThree')
                return "Skipping current round..."
            elif boss.state in ('PrepareBattleThree', 'BattleThree'):
                boss.exitIntroduction()
                boss.b_setState('PrepareBattleFour')
                return "Skipping current round..."
            elif boss.state in ('PrepareBattleFour', 'BattleFour'):
                boss.exitIntroduction()
                boss.b_setState('Victory')
                return "Skipping final round..."


class FeedDiners(MagicWord):
    desc = "Feed the diners in the CEO battle."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER

    def handleWord(self, invoker, avId, toon, *args):
        boss = None
        from toontown.suit.DistributedBossbotBossAI import DistributedBossbotBossAI
        for do in simbase.air.doId2do.values():
            if isinstance(do, DistributedBossbotBossAI):
                if invoker.doId in do.involvedToons:
                    boss = do
                    break
        if not boss:
            return "You aren't in a CEO!"

        if boss.state != 'BattleTwo':
            return "You aren't in the waiter round!"

        for table in boss.tables:
            for chairIndex in table.dinerInfo.keys():
                dinerStatus = table.getDinerStatus(chairIndex)
                if dinerStatus in (table.HUNGRY, table.ANGRY):
                    table.foodServed(chairIndex)

        return "All diners have been fed!"


class AbortGame(MagicWord):
    aliases = ["abortminigame", "leaveminigame"]
    desc = "Abort any minigame you are currently in."
    execLocation = MagicWordConfig.EXEC_LOC_CLIENT

    def handleWord(self, invoker, avId, toon, *args):
        messenger.send('minigameAbort')


class RequestGame(MagicWord):
    aliases = ["reqgame", "requestminigame", "reqminigame"]
    desc = "Request a minigame"
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("name", str, False, "remove"), ("keep", bool, False, False), ("diff", int, False, 0), ("zoneId", int, False, ToontownGlobals.ToontownCentral)]

    def handleWord(self, invoker, avId, toon, *args):
        minigameName = args[0]
        minigameKeep = args[1]
        minigameDiff = args[2]
        minigameZone = args[3]
        from toontown.minigame import MinigameCreatorAI
        if minigameName == 'remove':
            if invoker.doId in MinigameCreatorAI.RequestMinigame:
                del MinigameCreatorAI.RequestMinigame[invoker.doId]
                return "Deleted minigame request."
            else:
                return "You had no minigame requests!"
        elif minigameName not in ToontownGlobals.MinigameNames:
            return "Invalid minigame name!"
        elif minigameZone not in ToontownGlobals.HoodsWithMinigames:
            return "Invalid playground!"
        else:
            MinigameCreatorAI.RequestMinigame[invoker.doId] = ToontownGlobals.MinigameNames[minigameName], minigameKeep, minigameDiff, minigameZone
            return "Your request for the " + minigameName + " minigame was added."


class SpawnCog(MagicWord):
    aliases = ["cog"]
    desc = "Spawns a cog with the defined level"
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("suit", str, True), ("level", int, False, 1), ("specialSuit", int, False, 0)]

    def handleWord(self, invoker, avId, toon, *args):
        name = args[0]
        level = args[1]
        specialSuit = args[2]
        zoneId = invoker.getLocation()[1]
        if name not in SuitDNA.suitHeadTypes:
            return "Suit %s is not a valid suit!" % name
        if level not in ToontownGlobals.SuitLevels:
            return "Invalid Cog Level."
        level = ToontownGlobals.SuitLevels.index(level) + 1

        sp = simbase.air.suitPlanners.get(zoneId - (zoneId % 100))
        if not sp:
            return "Unable to spawn %s in current zone." % name
        pointmap = sp.streetPointList
        sp.createNewSuit([], pointmap, suitName=name, suitLevel=level, specialSuit=specialSuit)
        return "Spawned %s in current zone." % name


class SpawnInvasion(MagicWord):
    aliases = ["invasion"]
    desc = "Spawn an invasion on the current AI if one doesn't exist."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("command", str, True), ("suit", str, False, "f"), ("amount", int, False, 1000),
                 ("skelecog", bool, False, False)]

    def handleWord(self, invoker, avId, toon, *args):
        cmd = args[0]
        name = args[1]
        num = args[2]
        skeleton = args[3]

        if not 10 <= num <= 25000:
            return "Can't the invasion amount to {}! Specify a value between 10 and 25,000.".format(num)

        invMgr = simbase.air.suitInvasionManager
        if cmd == 'start':
            if invMgr.getInvading():
                return "There is already an invasion on the current AI!"
            if not name in SuitDNA.suitHeadTypes:
                return "This cog does not exist!"
            invMgr.startInvasion(name, num, skeleton)
        elif cmd == 'stop':
            if not invMgr.getInvading():
                return "There is no invasion on the current AI!"
            #elif invMgr.undergoingMegaInvasion:
            #    return "The current invasion is a mega invasion, you must stop the holiday to stop the invasion."
            invMgr.stopInvasion()
        else:
            return "You didn't enter a valid command! Commands are ~invasion start or stop."


class SetTrophyScore(MagicWord):
    aliases = ["trophyscore"]
    desc = "Set the trophy score of target."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("val", int, True)]

    def handleWord(self, invoker, avId, toon, *args):
        amt = args[0]

        if not 0 <= amt <= 255:
            return "The amount must be between 0 and 255!"
        simbase.air.trophyMgr.addTrophy(toon.doId, toon.name, amt, True)
        return "{}'s trophy score is now {}".format(toon.getName(), amt)


class GivePies(MagicWord):
    aliases = ["pies"]
    desc = "Gives the target pies to throw."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("type", int, True), ("amount", int, False, -1)]

    def handleWord(self, invoker, avId, toon, *args):
        pieType = args[0]
        numPies = args[1]
        if pieType == -1:
            toon.b_setNumPies(0)
            return "Removed %s's pies." % toon.getName()
        if not 0 <= pieType <= 7:
            return "You can only specify between pie types 0 and 7."
        if numPies == -1:
            toon.b_setPieType(pieType)
            toon.b_setNumPies(ToontownGlobals.FullPies)
            return "Gave %s an infinite amount of pies" % toon.getName()
        if not 0 <= numPies <= 99:
            return "You can only specify between 0 and 99 pies."
        toon.b_setPieType(pieType)
        toon.b_setNumPies(numPies)
        return "Gave {} an {} of {} pies".format(toon.getName(), numPies, pieType)


#class GiveProps(MagicWord):
#    desc = "Give target Y number of X pies."
#    execLocation = MagicWordConfig.EXEC_LOC_SERVER
#    arguments = [("type", int, True), ("amount", int, False, -1)]

#    def handleWord(self, invoker, avId, toon, *args):
#        pieType = args[0]
#        numPies = args[1]
#        if pieType == -1:
#            toon.b_setNumPies(0)
#            return "Removed %s's props." % toon.getName()
#        if not 0 <= pieType <= 7:
#            return "You can only specify between pie types 0 and 7."
#        if numPies == -1:
#            toon.b_setPieType(pieType)
#            toon.b_setNumPies(ToontownGlobals.FullPies)
#            return "Gave %s an infinite amount of props" % toon.getName()
#        if not 0 <= numPies <= 99:
#            return "You can only specify between -1 and 99 props."
#        toon.b_setPieType(pieType)
#        toon.b_setNumPies(numPies)


class SetQP(MagicWord):
    aliases = ["qp", "questprogress"]
    desc = "Get and set the targets quest progress."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("id", int, False, 0), ("progress", int, False, 0)]

    def handleWord(self, invoker, avId, toon, *args):
        questId = args[0]
        progress = args[1]
        questIds = ""
        for index in range(len(toon.quests)):
            questIds += "{0} ".format(toon.quests[index][0])
            if toon.quests[index][0] == questId:
                toon.quests[index][4] = progress
        toon.b_setQuests(toon.quests)
        return questIds


class SetUnites(MagicWord):
    aliases = ["unites", "restockunites"]
    desc = "Restocks the target's unites. The default amount is 999."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("amount", int, False, 999)]

    def handleWord(self, invoker, avId, toon, *args):
        amt = args[0]
        if not 1 <= amt <= 999:
            return "Unite amount must be between 0 and 999!"
        toon.restockAllResistanceMessages(amt)
        return "Restocked " + str(amt) + " unites successfully!"


class UnlockTricks(MagicWord):
    aliases = ["tricks"]
    desc = "Unlock all the target's pet trick phrases."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER

    def handleWord(self, invoker, avId, toon, *args):
        invoker.b_setPetTrickPhrases(range(7))
        return "Unlocked pet tricks!"


class RestockSummons(MagicWord):
    desc = "Restock all of the target's CJ summons."
    aliases = ["summons"]
    execLocation = MagicWordConfig.EXEC_LOC_SERVER

    def handleWord(self, invoker, avId, toon, *args):
        # Make sure we have every cog in our Cog Page.
        cogCount = []
        for deptIndex in xrange(5):
            for cogIndex in xrange(9):
                cogCount.append(CogPageGlobals.COG_QUOTAS[1][cogIndex] if cogIndex != 8 else 0)
        invoker.b_setCogCount(cogCount)
        invoker.b_setCogStatus(([CogPageGlobals.COG_COMPLETE2] * 8 + [0]) * 5)
        invoker.restockAllCogSummons()
        return "Restocked all cog summons successfully!"


class SetPinkSlips(MagicWord):
    aliases = ["pinkslips", "setfires", "fires"]
    desc = "Sets the target's pink slips. The default amount is 255."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("amount", int, False, 255)]

    def handleWord(self, invoker, avId, toon, *args):
        amt = args[0]
        plural = 's'
        if not 0 <= amt <= 255:
            return "The amount must be between 0 and 255!"
        if amt == 1:
            plural = ''
        toon.b_setPinkSlips(amt)
        return "Restocked {0} pink slip{1} successfully!".format(amt, plural)


class SetQuestTier(MagicWord):
    aliases = ['QuestTier']
    desc = "Sets the target's quest tier to specified value."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("tier", int, True)]

    def handleWord(self, invoker, avId, toon, *args):
        tier = args[0]

        if not 0 <= tier <= 255:
            return "Can't set {}'s quest tier to {}! Specify a value between 0 and 255.".format(toon.getName(), tier)

        toon.b_setQuests([])
        toon.b_setRewardHistory(tier, [])
        return "Set %s's quest tier to %d." % (toon.getName(), tier)


class SetExp(MagicWord):
    aliases = ["exp"]
    desc = "Sets the target's experience for the specified gag track. The default amount is 0."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("track", str, True), ("amount", int, False, 0)]

    def handleWord(self, invoker, avId, toon, *args):
        track = args[0]
        amt = args[1]

        tracks = ['toon-up', 'trap', 'lure', 'sound', 'throw', 'squirt', 'drop']
        maxed = ['max', 'maxxed']

        if track not in tracks + maxed:
            return "Invalid gag track specified!"

        if not 0 <= amt <= 10000:
            return "Can't set {0}'s jellybean count to {1}! Specify a value between 0 and 10,000.".format(toon.getName(), amt)

        if track in maxed:
            for track in tracks:
                toon.experience.setExp(track, 10000)
            toon.b_setExperience(toon.experience.makeNetString())
            return "Maxed all of {}'s gag tracks.".format(toon.getName())
        else:
            trackIndex = TTLocalizer.BattleGlobalTracks.index(track)
            toon.experience.setExp(trackIndex, amt)
            toon.b_setExperience(toon.experience.makeNetString())
            return "Set %s exp to %d successfully." % (track, amt)


class SetTrackBonus(MagicWord):
    aliases = ["trackbonus"]
    desc = "Sets the invoker's track bonus level."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("track", int, True)]

    def handleWord(self, invoker, avId, toon, *args):
        track = args[0]

        trackLength = ToontownBattleGlobals.UBER_GAG_LEVEL_INDEX
        numTracks = ToontownBattleGlobals.NUM_GAG_TRACKS
        gagAccess = invoker.getTrackAccess()

        trackBonusLevel = [-1] * numTracks
        if track == 8:
            bonusAccess = lambda x: trackLength if x > 0 else x
            trackBonusLevel = list(map(bonusAccess, gagAccess))
        elif 0 <= track < numTracks:
            if gagAccess[track]:
                trackBonusLevel[track] = trackLength
            else:
                return "You don\'t have that track!"
        else:
            return "Invalid track!"

        invoker.b_setTrackBonusLevel(trackBonusLevel)
        return "Track bonus set!"


class SetCogSuit(MagicWord):
    aliases = ["cogsuit"]
    desc = "Set disguise type and level."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("corp", str, True), ("type", str, True), ("level", int, True)]

    def handleWord(self, invoker, avId, toon, *args):
        corp = args[0]
        type = args[1]
        level = args[2]
        corps = ['bossbot', 'lawbot', 'cashbot', 'sellbot']
        corp = corp.lower()
        if corp not in corps:
            return "Invalid cog corp. specified."
        corpIndex = corps.index(corp)

        if type == "nosuit":
            # They want to reset their suit entirely.
            parts = toon.getCogParts()
            parts[corpIndex] = 0
            toon.b_setCogParts(parts)
            types = toon.getCogTypes()
            types[corpIndex] = 0
            toon.b_setCogTypes(types)
            levels = toon.getCogLevels()
            levels[corpIndex] = 0
            toon.b_setCogLevels(levels)
            merits = toon.getCogMerits()
            merits[corpIndex] = 0
            toon.b_setCogMerits(merits)
            return "Reset %s disguise and removed all earned parts." % corp.capitalize()

        # Get the cog type from the specified short-hand value.
        types = SuitDNA.suitHeadTypes[8 * corpIndex:(8 * corpIndex) + 8]
        if type not in types:
            return "Invalid cog type specified.."
        typeIndex = types.index(type)

        # Make sure they gave a level that is in range.
        if typeIndex == 7:
            # The final suit can go up to Level 50.
            levelRange = range(8, 51)  # Last digit is exclusive.
        else:
            levelRange = range((typeIndex + 1), (typeIndex + 6))
        if level not in levelRange:
            return "Invalid level specified for %s disguise %s." % (
                corp.capitalize(), SuitBattleGlobals.SuitAttributes[type]['name'])

        # Reset their merits to 0.
        merits = toon.getCogMerits()
        merits[corpIndex] = 0
        toon.b_setCogMerits(merits)

        # Ensure they have all the parts.
        parts = toon.getCogParts()
        parts[corpIndex] = CogDisguiseGlobals.PartsPerSuitBitmasks[corpIndex]
        toon.b_setCogParts(parts)

        # Find out if they need laff boosts or laff points removed.
        for levelBoost in [14, 19, 29, 39, 49]:
            if level <= levelBoost and not levelBoost > toon.getCogLevels()[corpIndex]:
                if toon.getMaxHp() <= 15:
                    continue
                toon.b_setMaxHp(toon.getMaxHp() - 1)
            elif level > levelBoost and not levelBoost <= toon.getCogLevels()[corpIndex]:
                if toon.getMaxHp() >= 137:
                    continue
                toon.b_setMaxHp(toon.getMaxHp() + 1)
        # Lets be nice and give them a toonup or make them suffer.
        if toon.getHp() > toon.getMaxHp():
            toon.takeDamage(toon.getHp() - toon.getMaxHp())
        else:
            toon.toonUp(toon.getMaxHp() - toon.getHp())

        # Set their type and level that they specified.
        types = toon.getCogTypes()
        types[corpIndex] = typeIndex
        toon.b_setCogTypes(types)
        levels = toon.getCogLevels()
        levels[corpIndex] = level - 1  # -1 because it starts at 0
        toon.b_setCogLevels(levels)

        return "Set {0} disguise to {1} Level {2}.".format(
            corp.capitalize(), SuitBattleGlobals.SuitAttributes[type]['name'], level)


class SetMerits(MagicWord):
    aliases = ["merits"]
    desc = "Sets your merits to the value specified."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("corp", str, True), ("amount", int, True)]

    def handleWord(self, invoker, avId, toon, *args):
        corp = args[0]
        amount = args[1]
        corps = ['bossbot', 'lawbot', 'cashbot', 'sellbot']
        corpsMerits = ['stock options', 'jury notices', 'cogbucks', 'merits']
        if corp not in corps:
            return "Invalid cog corp. specified."
        corpIndex = corps.index(corp)

        merits = invoker.getCogMerits()
        merits[corpIndex] = amount
        invoker.b_setCogMerits(merits)
        return "Set {0} to {1}.".format(corpsMerits[corpIndex], amount)


class Fanfare(MagicWord):
    desc = "Gives the target a fanfare, because why not?"
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    accessLevel = 'MODERATOR'

    def handleWord(self, invoker, avId, toon, *args):
        toon.d_generateFanfare()
        return "much congratulations. many trumpets. wow. (Fanfare given to {}.)".format(toon.getName())


class SetPouch(MagicWord):
    aliases = ["pouch", "setgagpouch", "gagpouch", "setmaxgags"]
    desc = "Sets your max gag pouch limit."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    affectRange = MagicWordConfig.AFFECT_SINGLE
    arguments = [("amount", int, True)]

    def handleWord(self, invoker, avId, toon, *args):
        amt = args[0]

        if not 1 <= amt <= 255:
            return "Can't set {0}'s pouch size to {1}! Specify a value between 1 and 255.".format(toon.getName(), amt)

        invoker.b_setMaxCarry(amt)
        return "Set your pouch size to {}.".format(amt)


class SetNametagStyle(MagicWord):
    aliases = ["setnametag", "nametag", "nametagstyle"]
    desc = "Sets the style of the target's nametag to the specified ID."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("style", str, True)]

    def handleWord(self, invoker, avId, toon, *args):
        styleName = args[0]

        nametag_list = list(TTLocalizer.NametagFontNames)
        for index, item in enumerate(nametag_list):
            nametag_list[index] = item.lower()
        styleName = styleName.lower()

        if styleName in nametag_list:
            index = nametag_list.index(styleName)
        elif styleName == "basic":
            index = 100
        else:
            return "Invalid nametag name entered."

        toon.b_setNametagStyle(index)
        return "Set {}'s nametag style successfully.".format(toon.getName())


class SetNametagType(MagicWord):
    aliases = ["nametagtype", "lacker"]
    desc = "Set the style of the target's nametag to the specified ID."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("type", int, False, 0)]

    def handleWord(self, invoker, avId, toon, *args):
        type = args[0]

        nametagTypeList = [(0, NametagGroup.CCNormal), (1, NametagGroup.CCNonPlayer), (3, NametagGroup.CCSuit)]
        for nametag in nametagTypeList:
            if type == nametag[0]:
                toon.b_setNametagType(nametag[0])
                return "Changed {}'s nametag type successfully.".format(toon.getName())

        return "Invalid nametag type specified!"


class UnlockPhrase(MagicWord):
    aliases = ["phrase", "addphrase"]
    desc = "Unlocks a new phrase and adds it to target's list of 'My Phrases'."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("id", int, True)]

    def handleWord(self, invoker, avId, toon, *args):
        phraseId = args[0]

        strings = OTPLocalizer.CustomSCStrings
        scId = int(phraseId)*10
        id = None
        if scId in strings.iterkeys():
            id = scId

        if id:
            if toon.customMessages.count(id) != 0:
                return "{} already has this custom phrase!".format(toon.getName())
            if len(toon.customMessages) >= ToontownGlobals.MaxCustomMessages:
                toon.customMessages = toon.customMessages[1:]
            toon.customMessages.append(id)
            toon.d_setCustomMessages(toon.customMessages)
            return "Added phrase id {0} to {1}'s list.".format(id, toon.getName())

        return "Invalid phrase id! Could not set."


class SetSos(MagicWord):
    aliases = ["sos", "givesos"]
    desc = "Sets your SOS cards. The default is 1 Flippy card."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    affectRange = MagicWordConfig.AFFECT_SINGLE
    arguments = [("name", str, False, 'Flippy'), ("amount", int, False, 1)]

    def handleWord(self, invoker, avId, toon, *args):
        name = args[0]
        amt = args[1]

        if not 0 <= amt <= 100:
            return "The amount must be between 0 and 100!"

        npcId, npcName = NPCToons.loadCards(cardInfo=json.loads(simbase.air.moddingManager.getCards()), name=name)
        if not npcId:
            return "The {0} SOS card was not found!".format(name)

        if (amt == 0) and (npcId in invoker.NPCFriendsDict):
            del invoker.NPCFriendsDict[npcId]
        else:
            invoker.NPCFriendsDict[npcId] = amt
        invoker.d_setNPCFriendsDict(toon.NPCFriendsDict)
        return "Restocked {0} {1} SOS cards successfully!".format(amt, npcName)


class FreeBldg(MagicWord):
    aliases = ["freecogbldg", "freecogbuilding", "freebuilding"]
    desc = "Closest cog building to you gets freed."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER

    def handleWord(self, invoker, avId, toon, *args):

        returnCode = invoker.doBuildingFree()
        if returnCode[0] == 'success':
            return "Successfully took back building!"
        elif returnCode[0] == 'busy':
            return "Toons are currently taking back the building!"
        return "Could not free building."


class MaxGarden(MagicWord):
    desc = "Maxes your garden."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER

    def handleWord(self, invoker, avId, toon, *args):
        invoker.b_setShovel(3)
        invoker.b_setWateringCan(3)
        invoker.b_setShovelSkill(639)
        invoker.b_setWateringCanSkill(999)
        invoker.b_setGardenTrophies(GardenGlobals.TrophyDict.keys())


class ToggleInstantDelivery(MagicWord):
    aliases = ["fastdelivery", "togglefastdelivery", "toggleinstadelivery", "instantdelivery", "instadelivery"]
    desc = "Toggles instant delivery of all cattlelog items to your house."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    affectRange = MagicWordConfig.AFFECT_SINGLE

    def handleWord(self, invoker, avId, toon, *args):
        invoker.instantDelivery = not invoker.instantDelivery
        for item in toon.onOrder:
            item.deliveryDate = int(time.time() / 60)  # Deliver all the packages that they already ordered, too.
        return "Instant Delivery has been turned {0}.".format('on' if invoker.instantDelivery else 'off')


class TPose(MagicWord):
    aliases = ["settpose", "forcetpose"]
    desc = "Forces T-Pose on yourself."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    affectRange = MagicWordConfig.AFFECT_SINGLE

    def handleWord(self, invoker, avId, toon, *args):
        toon.d_setTPose()
        return "Forced yourself into a T-Pose."


class Nudify(MagicWord):
    aliases = ["setnudify", "setnudity", "nudity"]
    desc = "Makes yourself nude."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    affectRange = [MagicWordConfig.AFFECT_SINGLE]

    def handleWord(self, invoker, avId, toon, *args):
        dna = ToonDNA.ToonDNA()
        dna.makeFromNetString(toon.getDNAString())

        if len(dna.torso) == 1:
            return "There isn\'t a skeleton under {}.  Use ~dna torso to put clothes back on the target.".format(toon.getName())
        else:
            dna.torso = dna.getTorsoSize()[0]
            toon.b_setDNAString(dna.makeNetString())
            return "{} is now a naked toon!".format(toon.getName())


class SetMuzzle(MagicWord):
    aliases = ["muzzle"]
    desc = "Sets the target's muzzle to the specified type."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("id", int, False, 0)]

    def handleWord(self, invoker, avId, toon, *args):
        type = args[0]
        if not 0 <= type <= 5:
            return "The muzzle type must be between 0 and 5!"

        toon.b_setMuzzle(type)
        if type == 0:
            return "Returned muzzle to normal for {}!".format(toon.getName())
        return "Set muzzle to type {0} for {1}".format(type, toon.getName())


class SetEyes(MagicWord):
    aliases = ["eyes"]
    desc = "Sets the target's eyes to the specified type."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("id", int, False, 0)]

    def handleWord(self, invoker, avId, toon, *args):
        type = args[0]
        if not 0 <= type <= 3:
            return "The eye type must be between 0 and 3!"

        toon.b_setEyes(type)
        if type == 0:
            return "Returned eyes to normal for {}!".format(toon.getName())
        return "Set eyes to type {0} for {1}".format(type, toon.getName())


class InfoWarrior(MagicWord):
    hidden = True
    aliases = ["gayfrog"]
    desc = "There's A War On For Your Mind."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    accessLevel = 'TTOFF_DEVELOPER'

    def handleWord(self, invoker, avId, toon, *args):
        toon.d_generateBrowserEasterEgg(0)
        return "There's A War On For Your Mind"


class FakeNews(MagicWord):
    hidden = True
    desc = "FAKE NEWS!"
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    accessLevel = 'TTOFF_DEVELOPER'

    def handleWord(self, invoker, avId, toon, *args):
        toon.d_generateBrowserEasterEgg(1)
        return "I'VE GOT POWER, I'M A SATAN! I'M GONNA SUCK YOU DRY AND TORTURE YOU TO DEATH!"


class Weeb(MagicWord):
    aliases = ["toggleweeb", "japandialog", "togglejapandialog"]
    hidden = True
    desc = "NO ANIME! (Toggles Japanese dialog for the target.)"
    execLocation = MagicWordConfig.EXEC_LOC_CLIENT
    accessLevel = 'USER'

    def handleWord(self, invoker, avId, toon, *args):
        if base.japanDialog:
            base.japanDialog = 0
            base.settings.updateSetting('game', 'japan-dialog', False)
            return "Arigato gozaimasu! (Toggled Japanese dialog to off for {})".format(toon.getName())
        else:
            base.japanDialog = 1
            base.settings.updateSetting('game', 'japan-dialog', True)
            return "Arigato gozaimasu! (Toggled Japanese dialog to on for {})".format(toon.getName())


class PlaySound(MagicWord):
    aliases = ["sound", "playsfx", "sfx"]
    desc = "Plays a sound given by its name on the specified toon."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("name", str, True), ("loop", int, False, 0)]

    def handleWord(self, invoker, avId, toon, *args):
        sound = args[0]
        loop = args[1]
        toon.d_playSound(sound, loop)
        return "Attempting to play %s on %s." % (sound, toon.getName())


class Trolley(MagicWord):
    aliases = ["dingding", "littlecat"]
    desc = "Creates a trolley that falls from the sky on the specified target."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    accessLevel = 'MODERATOR'

    def handleWord(self, invoker, avId, toon, *args):
        toon.d_generateTrolley()
        return "Ding Ding! Trolley spawned for {}".format(toon.getName())


class SetTaskCarryLimit(MagicWord):
    aliases = ["taskcarrylimit", "settaskcarry", "taskcarry", "setcarry"]
    desc = "Set the amount of tasks you can carry."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("limit", int, False, 1)]

    def handleWord(self, invoker, avId, toon, *args):
        amt = args[0]
        plural = 's'

        if not 1 <= amt <= 4:
            return "The amount must be between 1 and 4!"
        if amt == 1:
            plural = ''
        invoker.b_setQuestCarryLimit(amt)
        return "You can now carry {0} task{1}!".format(amt, plural)


class ToggleAlwaysHitCogs(MagicWord):
    aliases = ["alwayshitcogs", "hitcogs", "setalwayshitcogs"]
    desc = "Toggles always hitting cogs. When enabled, you will have 100% accuracy at all times."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER

    def handleWord(self, invoker, avId, toon, *args):
        if not invoker:
            return

        if not invoker.getAlwaysHitSuits():
            invoker.setAlwaysHitSuits(True)
        else:
            invoker.setAlwaysHitSuits(False)

        return "Toggled always hitting Cogs".format('ON' if toon.getAlwaysHitSuits() else 'OFF')


class ToggleFireworks(MagicWord):
    aliases = ["fireworks", "startfireworks", "beginfireworks"]
    desc = "Start a fireworks show."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("showName(summer/july4, newyears, party, combo)", str, False, "july4")]
    accessLevel = "MODERATOR"

    def handleWord(self, invoker, avId, toon, *args):
        showName = args[0]
        if showName in ('summer', 'july4'):
            showType = ToontownGlobals.JULY4_FIREWORKS
        elif showName == 'newyears':
            showType = ToontownGlobals.NEWYEARS_FIREWORKS
        elif showName == 'party':
            showType = PartyGlobals.FireworkShows.Summer
        elif showName == 'combo':
            showType = ToontownGlobals.COMBO_FIREWORKS
        else:
            return 'Improper firework type specified. Refer to magic words page for acceptable types.'
        fireworkMgr = simbase.air.fireworkManager
        if fireworkMgr.isShowRunning():
            return 'A firework show is already running.  Please wait before starting another.'
        fireworkMgr.startShow(showType)
        return 'Started fireworks in all playgrounds!'


class Snap(MagicWord):
    aliases = ["thanos", "thanossnap"]
    desc = "Perfectly balanced. As all things should be."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    accessLevel = 'MODERATOR'

    def handleWord(self, invoker, avId, toon, *args):
        from otp.avatar.DistributedPlayerAI import DistributedPlayerAI
        for do in simbase.air.doId2do.values():
            if isinstance(do, DistributedPlayerAI) and do.isPlayerControlled():
                if random.random() < 0.5:
                    do.d_generateSnapEffect()
        return "I am inevitable."


class Green(MagicWord):
    aliases = ["gosad", "maketoongosad"]
    desc = "Greens the targeted Toon with the specified character."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("character", str, False, 'f')]

    def handleWord(self, invoker, avId, toon, *args):
        character = args[0]
        hqOfficers = []
        type = 0
        toonId = 0
        if character not in SuitDNA.suitHeadTypes:
            for npcId, npcName in TTLocalizer.NPCToonNames.items():
                if character.lower() == 'hq officer':
                    if npcName.lower() != 'hq officer':
                        continue
                    hqOfficers.append(npcId)
                elif character.lower() == npcName.lower():
                    if character.lower() != 'kong':
                        toonId = npcId
                        type = 1
                        break
            if hqOfficers:
                toonId = random.choice(hqOfficers)
                type = 1
            elif character == 'toon':
                toonId = 2
                type = 1
            elif character == 'panda':
                type = 2
            elif character not in [TTLocalizer.SellbotP.lower(), TTLocalizer.CashbotP.lower(), TTLocalizer.LawbotP.lower(), TTLocalizer.BossbotP.lower()] and type != 1:
                return "Invalid character name! Target could not be greened"
        if type == 1:
            toon.d_generateGreenEffect(character, toonId)
            if toonId == 2 and toon.getTransformationsIndex(ToontownGlobals.TransformationCog) != -1:
                landingDuration = 10.0
            else:
                landingDuration = 5.5
            seq = Sequence(Wait(landingDuration), Func(toon.b_setHp, -1))
        elif type == 2:
            toon.d_generateGreenEffect(character, 0)
            seq = Sequence(Func(toon.b_setHp, -1))
        else:
            toon.d_generateGreenEffect(character, 0)
            seq = Sequence(Wait(10.0), Func(toon.b_setHp, -1))
        seq.start()
        return "Time for {} to make a new Toon!".format(toon.getName())


class EndFlying(MagicWord):
    aliases = ["endflyinggame", "setendflying", "setendflyinggame"]
    desc = "Ends the flying game in a Lawbot Field Office."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER

    def handleWord(self, invoker, avId, toon, *args):
        from toontown.cogdominium.DistCogdoFlyingGameAI import DistCogdoFlyingGameAI
        flyingGame = None
        for do in simbase.air.doId2do.values():
            if isinstance(do, DistCogdoFlyingGameAI):
                if invoker.doId in do.getToonIds():
                    flyingGame = do
                    break

        if flyingGame:
            flyingGame._handleGameFinished()
            return "Completed the flying game."
        else:
            return "You are not in a flying game! Could not complete."


class Ping(MagicWord):
    desc = "Pong!"
    execLocation = MagicWordConfig.EXEC_LOC_SERVER

    def handleWord(self, invoker, avId, toon, *args):
        return "Pong!"


class GardenGame(MagicWord):
    aliases = ["gardendrop"]
    desc = "Start the garden drop mini-game."
    execLocation = MagicWordConfig.EXEC_LOC_CLIENT

    def handleWord(self, invoker, avId, toon, *args):
        from toontown.estate import GardenDropGame
        base.localAvatar.game = GardenDropGame.GardenDropGame()
        return "Started the garden drop mini-game."


class WinGame(MagicWord):
    aliases = ["winminigame"]
    desc = "Win the trolley game you are in."
    execLocation = MagicWordConfig.EXEC_LOC_CLIENT

    def handleWord(self, invoker, avId, toon, *args):
        messenger.send("minigameVictory")
        return "Trolley game won."


class LeftHandProp(MagicWord):
    aliases = ["lefthand", "proplefthand"]
    desc = "Attaches a prop to the target's left hand."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("prop", str, False, '')]

    def handleWord(self, invoker, avId, toon, *args):
        propName = args[0]

        if not propName:
            toon.d_setLeftHand(propName)
            return "Cleared the target's right hand."

        valid = 0
        for prop in ToontownGlobals.PropNames:
            propLower = prop.lower()
            propStripped = propLower.replace(" ", "")
            if propName == propLower or propName == propStripped:
                valid = 1
                propName = prop
                break

        if not valid:
            return "Invalid prop name!"

        if propName not in ToontownGlobals.PropNames:
            return "Invalid prop name!"

        toon.d_setLeftHand(propName)

        return "Prop attached to target's left hand."


class RightHandProp(MagicWord):
    aliases = ["righthand", "proprighthand"]
    desc = "Attaches a prop to the target's right hand."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("prop", str, False, '')]

    def handleWord(self, invoker, avId, toon, *args):
        propName = args[0]

        if not propName:
            toon.d_setRightHand(propName)
            return "Cleared the target's right hand."

        valid = 0
        for prop in ToontownGlobals.PropNames:
            propLower = prop.lower()
            propStripped = propLower.replace(" ", "")
            if propName == propLower or propName == propStripped:
                valid = 1
                propName = prop
                break

        if not valid:
            return "Invalid prop name!"

        if propName not in ToontownGlobals.PropNames:
            return "Invalid prop name!"

        toon.d_setRightHand(propName)

        return "Prop attached to target's right hand."


class BothHandsProp(MagicWord):
    aliases = ["bothhands", "propbothhands"]
    desc = "Attaches a prop to both of the target's hands."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("prop", str, False, '')]

    def handleWord(self, invoker, avId, toon, *args):
        propName = args[0]

        if not propName:
            toon.d_setLeftHand(propName)
            toon.d_setRightHand(propName)
            return "Cleared both of the target's hands."

        valid = 0
        for prop in ToontownGlobals.PropNames:
            propLower = prop.lower()
            propStripped = propLower.replace(" ", "")
            if propName == propLower or propName == propStripped:
                valid = 1
                propName = prop
                break

        if not valid:
            return "Invalid prop name!"

        if propName not in ToontownGlobals.PropNames:
            return "Invalid prop name!"

        toon.d_setLeftHand(propName)
        toon.d_setRightHand(propName)

        return "Prop attached to both of the target's hands."


class SetHouse(MagicWord):
    aliases = ["house"]
    desc = "Sets the house of the target."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("type", int, False, 0)]

    def handleWord(self, invoker, avId, toon, *args):
        type = args[0]

        if not 0 <= type <= 5:
            return "Invalid house type!"

        if toon.getHouseId() in simbase.air.doId2do:
            house = simbase.air.doId2do.get(toon.getHouseId())
            if house is None:
                return "House not generated! Target must visit their estate to generate their house."
            house.b_setHouseType(type)
            return "{0}'s House type set to {1}.".format(toon.getName(), type)
        return "House not generated! Go to your estate to generate your house."


class GetZone(MagicWord):
    aliases = ["getzoneid", "zoneid"]
    desc = "Returns the target's zone ID."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER

    def handleWord(self, invoker, avId, toon, *args):
        return "{}'s zone ID is {}.".format(toon.getName(), str(toon.zoneId))


class Oboe(MagicWord):
    aliases = ["playoboe", "oboesfx", "sfxoboe", "oboesound", "playoboesfx", "playoboesound"]
    desc = "Plays an oboe sound effect on the target's client."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    accessLevel = 'MODERATOR'

    def handleWord(self, invoker, avId, toon, *args):
        toon.d_generateOboeEffect()
        return "Played oboe sound effect for {}".format(toon.getName())


class ToggleCage(MagicWord):
    administrative = True
    aliases = ["cage", "setcage", "tooncage"]
    desc = "Toggles a lock-down on the target Toon."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    affectRange = [MagicWordConfig.AFFECT_OTHER]

    def handleWord(self, invoker, avId, toon, *args):
        if invoker == toon:
            return "You cannot toggle a Cage on yourself!"

        toon.b_setImmortalMode(1)
        toon.b_setLocked(not toon.getLocked())
        toon.d_generateCage()
        return "Cage has been toggled for {}.".format(toon.getName())


class ToggleMute(MagicWord):
    aliases = ["setmute", "mutetoon", "toonmute"]
    administrative = True
    desc = "Toggles a mute on the target Toon. Optionally, you can provide a time (in minutes) the Toon is muted for."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("time", int, False, 0)]
    affectRange = [MagicWordConfig.AFFECT_OTHER]

    def handleWord(self, invoker, avId, toon, *args):
        timed = args[0]

        if invoker == toon:
            return "You cannot toggle Mute on yourself!"

        if 0 > timed or timed > 1440:
            return "Mute time must be between 1 and 1440 seconds."

        if toon.getMuted() and timed:
            return "You cannot time a mute on a Toon that is already muted!"

        toon.b_setMuted(not toon.getMuted(), timed)
        return "Mute has been toggled for {}.".format(toon.getName())


class TransformDisneyCharacter(MagicWord):
    aliases = ["transformdisney", "transformchar", "setdisneyindex", "setcharindex", "disney", "char", "setchar"]
    desc = "Transforms the target into a Disney character."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("id", int, False, -1)]

    def handleWord(self, invoker, avId, toon, *args):
        index = args[0]

        if not -1 <= index <= 17:
            return "Invalid character ID specified. Could not transform {} into a Disney character.".format(toon.getName())

        toon.b_setCharIndex(index, 2)
        if index != -1:
            return 'Transformed {0} into {1}'.format(toon.getName(), TTLocalizer.charName2Id[index])
        else:
            return 'Transformed {} back into a Toon!'.format(toon.getName())


class TransformDoodle(MagicWord):
    aliases = ["setdoodleindex", "doodleindex", "doodle", "setdoodle"]
    desc = "Transforms the target into their Doodle."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER

    def handleWord(self, invoker, avId, toon, *args):
        index = toon.getDoodleIndex()
        if index == -1:
            index = 0
        elif index == 0:
            index = -1

        toon.b_setDoodleIndex(index, 2)
        if index != -1:
            return 'Transformed {} into a Doodle!'.format(toon.getName())
        else:
            return 'Transformed {} back into a Toon!'.format(toon.getName())


class TransformGoon(MagicWord):
    aliases = ["setgoonindex", "goonindex", "goon", "setgoon"]
    desc = "Transforms the target into a Goon."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("id", int, False, -1)]

    def handleWord(self, invoker, avId, toon, *args):
        index = args[0]

        if not -1 <= index <= 1:
            return "Invalid Goon ID specified. Could not transform {} into a goon".format(toon.getName())

        toon.b_setGoonIndex(index, 2)
        if index != -1:
            return 'Transformed {} into a Goon!'.format(toon.getName())
        else:
            return 'Transformed {} back into a Toon!'.format(toon.getName())


class TransformProp(MagicWord):
    aliases = ["setpropindex", "setprop"]
    desc = "Transforms the target into a Prop."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("propName", str, False, '')]

    def handleWord(self, invoker, avId, toon, *args):
        propName = args[0]

        valid = 0
        for prop in ToontownGlobals.PropNames:
            prop = prop.lower()
            propStripped = prop.replace(" ", "")
            if propName == prop or propName == propStripped:
                valid = 1
                break

        if propName != '':
            if not valid:
                return "Invalid prop name! Could not transform {} into a prop.".format(toon.getName())
            retMsg = 'Transformed {} into a Prop!'.format(toon.getName())
        else:
            retMsg = 'Transformed {} back into a Toon!'.format(toon.getName())
        toon.b_setPropIndex(propName, 2)
        return retMsg


class TransformBoss(MagicWord):
    aliases = ["setbossindex", "bossindex", "boss", "setboss"]
    desc = "Transforms the target into a Cog Boss."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("id", int, False, -1)]

    def handleWord(self, invoker, avId, toon, *args):
        index = args[0]

        if not -1 <= index <= 3:
            return "Invalid Cog Boss ID specified. {} could not be transformed.".format(toon.getName())

        toon.b_setBossIndex(index, 2)
        if index != -1:
            return 'Transformed {} into a Cog Boss!'.format(toon.getName())
        else:
            return 'Transformed {} back into a Toon!'.format(toon.getName())


class SetAccessLevel(MagicWord):
    administrative = True
    aliases = ["accesslevel", "access", "setaccess"]
    desc = "Sets the target's access level."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("rank", int, False, 100)]
    affectRange = [MagicWordConfig.AFFECT_OTHER]

    def handleWord(self, invoker, avId, toon, *args):
        rank = args[0]

        if not -100 <= rank <= 800:
            return "Can't set {0}'s speed to {1}! Specify a value between -100 and 800.".format(toon.getName(), rank)

        if invoker.getAccessLevel() == rank:
            return "You cannot set the target to your own Access Level!"

        rank = OTPGlobals.AccessLevelInt2Name.get(rank)
        toon.b_setAccessLevel(rank)
        return "Set {0}'s Access Level to {1}.".format(toon.getName(), rank)


class StartMaintenance(MagicWord):
    administrative = True
    aliases = ["update", "maintenance", "startupdate", "updatestart", "maintenancestart"]
    desc = "Sends a maintenance warning to the players."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("time", int, False, 300), ("type", int, False, 0)]
    accessLevel = "MODERATOR"

    def handleWord(self, invoker, avId, toon, *args):
        time = args[0]
        type = args[1]

        if not 60 <= time <= 600:
            return "Can't announce maintenance with a time of {}! Specify a value between 60 and 600 seconds.".format(time)

        if type not in [0, 1]:
            return "Could not announce maintenance with a type of {}! Specify a value between 0 and 1.".format(time)

        if type:
            reasonType = TTLocalizer.ServerShutdownUpdate
        else:
            reasonType = TTLocalizer.ServerShutdownMaintenance

        reason = TTLocalizer.ServerShutdownMessage % reasonType
        simbase.air.announceMaintenance(reason, reasonType, time)
        return "Announcing {0} with a time of {1} seconds and a reason of {2}".format(reasonType, time, reason)


class SetTurbo(MagicWord):
    aliases = ["setturbomode", "turbomode", "kartturbo", "turbokart"]
    desc = "Sets your kart to TURBO mode!"
    execLocation = MagicWordConfig.EXEC_LOC_CLIENT

    def handleWord(self, invoker, avId, toon, *args):
        if not base.localAvatar.kart:
            return "You aren't in a Kart! Kart could not be set to TURBO mode."

        base.localAvatar.kart.startTurbo()
        return "Kart set to TURBO mode!"


class StartHoliday(MagicWord):
    aliases = ["holiday", "setholidaystart", "setstartholiday", "holidaystart"]
    administrative = True
    desc = "Starts the specified holiday on the server."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("holidayId", int, True)]
    accessLevel = "MODERATOR"

    def handleWord(self, invoker, avId, toon, *args):
        holidayId = args[0]

        if not hasattr(self.air, 'holidayManager'):
            return 'Holiday manager isn\'t generated in this AI.  Holiday not started.'
        if self.air.holidayManager.isHolidayRunning(holidayId):
            return 'Holiday {} is already running!'.format(holidayId)

        self.air.holidayManager.startHoliday(holidayId)
        return 'Holiday {} has started!'.format(holidayId)


class EndHoliday(MagicWord):
    aliases = ["setholidayend", "setendholiday", "holidayend"]
    administrative = True
    desc = "Ends the specified holiday currently running on the server."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER
    arguments = [("holidayId", int, True)]
    accessLevel = "MODERATOR"

    def handleWord(self, invoker, avId, toon, *args):
        holidayId = args[0]

        if not hasattr(self.air, 'holidayManager'):
            return 'Holiday manager isn\'t generated in this AI.  Holiday not ended.'
        if not self.air.holidayManager.isHolidayRunning(holidayId):
            return 'Holiday {} isn\'t currently active!'.format(holidayId)

        self.air.holidayManager.endHoliday(holidayId)
        return 'Holiday {} has been ended.'.format(holidayId)


class ToggleRougesGallery(MagicWord):
    aliases = ["roguesgallery", "togglerogues", "rogues", "togglegallery", "gallery"]
    desc = "Toggles the Rogues Gallery page in your Shtickerbook."
    execLocation = MagicWordConfig.EXEC_LOC_CLIENT

    def handleWord(self, invoker, avId, toon, *args):
        if base.localAvatar.roguesPage:
            return "Rogues Gallery already loaded."

        if base.localAvatar.cogRadar != [1, 1, 1, 1]:
            return "You must finish your Cog Radar before toggling the Rogues Gallery."

        base.localAvatar.addRoguesPage()
        return "Loaded the Rogues Gallery."


class PrintChildren(MagicWord):
    aliases = ["children", "getchildren"]
    desc = "Prints all of render's children to the client log."
    execLocation = MagicWordConfig.EXEC_LOC_CLIENT
    arguments = [("type", int, False, 0), ("mode", int, False, 0)]

    def handleWord(self, invoker, avId, toon, *args):
        type = args[0]
        mode = args[1]

        if not type:
            node = render
        else:
            node = render2d

        if not mode:
            print node.getChildren()
        elif mode == 2:
            for child in node.getChildren():
                for secondaryChild in child.getChildren():
                    print secondaryChild.getChildren()
        elif mode == 3:
            for child in node.getChildren():
                for secondaryChild in child.getChildren():
                    for thirdChild in secondaryChild.getChildren():
                        print thirdChild.getChildren()
        elif mode == 4:
            for child in node.getChildren():
                for secondaryChild in child.getChildren():
                    for thirdChild in secondaryChild.getChildren():
                        for fourthChild in thirdChild.getChildren():
                            print fourthChild.getChildren()
        elif mode == 5:
            for child in node.getChildren():
                for secondaryChild in child.getChildren():
                    for thirdChild in secondaryChild.getChildren():
                        for fourthChild in thirdChild.getChildren():
                            for fifthChild in fourthChild.getChildren():
                                print fifthChild.getChildren()
        else:
            for child in node.getChildren():
                print child.getChildren()
        return "Printed children of render to the client log file."


class StartParty(MagicWord):
    aliases = ["party", "planparty", "hostparty"]
    desc = "Starts a predefined party, free of charge."
    execLocation = MagicWordConfig.EXEC_LOC_SERVER

    def handleWord(self, invoker, avId, toon, *args):
        if not invoker.canPlanParty():
            return "You're already hosting a party!  You can only host one at a time."

        # Get ASAP time.
        from datetime import timedelta
        curServerTime = simbase.air.toontownTimeManager.getCurServerDateTime()
        startTime = curServerTime
        startTime = startTime.replace(startTime.year, startTime.month, startTime.day, startTime.hour, startTime.minute, second=0, microsecond=0)
        minute = curServerTime.minute
        remainder = minute % PartyGlobals.PartyPlannerAsapMinuteRounding
        if remainder:
            startTime += timedelta(minutes=PartyGlobals.PartyPlannerAsapMinuteRounding - remainder)
        else:
            startTime += timedelta(minutes=PartyGlobals.PartyPlannerAsapMinuteRounding)
        endTime = startTime + timedelta(hours=PartyGlobals.DefaultPartyDuration)

        isPrivate = 0
        inviteTheme = PartyGlobals.InviteTheme.GenericMale
        activities = [(1, 7, 14, 12), (1, 8, 14, 12), (1, 9, 14, 12), (1, 10, 14, 12), (5, 9, 11, 0), (2, 4, 10, 6), (10, 15, 7, 18), (6, 3, 7, 6), (7, 8, 7, 0), (3, 5, 4, 6), (8, 9, 3, 12), (9, 12, 2, 18)]
        decorations = []

        invitees = []
        for friend in invoker.friendsList:
            invitees.append(friend[0])

        simbase.air.partyManager.addPartyRequest(invoker.doId, startTime.strftime('%Y-%m-%d %H:%M:%S'),
                                                 endTime.strftime('%Y-%m-%d %H:%M:%S'), isPrivate, inviteTheme,
                                                 activities, decorations, invitees, free=True)
        return "Party requested."



# Instantiate all classes defined here to register them.
# A bit hacky, but better than the old system
for item in globals().values():
    if isinstance(item, types.ClassType) and issubclass(item, MagicWord):
        i = item()
