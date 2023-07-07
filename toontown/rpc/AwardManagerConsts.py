# from enum import Enum

GiveAwardErrors = Enum('Success, WrongGender, NotRewardable, FullMailbox, FullAwardMailbox, AlreadyInMailbox, AlreadyInGiftQueue, '
                       'AlreadyInOrderedQueue, AlreadyInCloset, AlreadyInTrunk, AlreadyBeingWorn, AlreadyInAwardMailbox, '
                       'AlreadyInThirtyMinuteQueue, AlreadyInMyPhrases, AlreadyKnowDoodleTraining, AlreadyStartedGarden, AlreadyOwnFishingRod, '
                       'GardenSkillTooLow, NoGardenStarted, AlreadyRented, GenericAlreadyHaveError, UnknownError, UnknownToon, NonToon, '
                       )

GiveAwardErrorStrings = {
    GiveAwardErrors.Success: "success",
    GiveAwardErrors.WrongGender: "wrong gender",  # 1
    GiveAwardErrors.NotRewardable: "item is not rewardable",  # 2
    GiveAwardErrors.FullMailbox: "mailbox is full",  # 3
    GiveAwardErrors.FullAwardMailbox: "award mailbox is full",  # 4
    GiveAwardErrors.AlreadyInMailbox: "award already in mailbox.",  # 5
    GiveAwardErrors.AlreadyInGiftQueue: "award already in gift queue.",  # 6
    GiveAwardErrors.AlreadyInOrderedQueue: "award already in ordered queue.",  # 7
    GiveAwardErrors.AlreadyInCloset: "award already in closet.",  # 8
    GiveAwardErrors.AlreadyInTrunk: "award already in trunk.",  # 9
    GiveAwardErrors.AlreadyBeingWorn: "award already being worn.",  # 10
    GiveAwardErrors.AlreadyInAwardMailbox: "award already in award mailbox",  # 11
    GiveAwardErrors.AlreadyInThirtyMinuteQueue: "award already in 30 minute queue",  # 12
    GiveAwardErrors.AlreadyInMyPhrases: "speed chat award already in my phrases",  # 13
    GiveAwardErrors.AlreadyKnowDoodleTraining: "doodle training award already known",  # 14
    GiveAwardErrors.AlreadyStartedGarden: "garden already started",  # 15
    GiveAwardErrors.AlreadyOwnFishingRod: "fishing rod award already owned",  # 16
    GiveAwardErrors.GardenSkillTooLow: "unable to give award due to garden skill too low",  # 17
    GiveAwardErrors.NoGardenStarted: 'unable to give award due to no garden started',  # 18
    GiveAwardErrors.AlreadyRented: "award is already rented",  # 19
    GiveAwardErrors.GenericAlreadyHaveError: "generic-already-have error",  # 20
    GiveAwardErrors.UnknownError: "unknown error",  # 21
    GiveAwardErrors.UnknownToon: "toon not in database",  # 22
    GiveAwardErrors.NonToon: "this is not a toon",  # 23
}

assert len(GiveAwardErrorStrings) == len(GiveAwardErrors)
