from direct.fsm.StatePush import StateVar
from otp.level.EntityStateVarSet import EntityStateVarSet
from toontown.cogdominium.CogdoEntityTypes import CogdoCraneGameSettings, CogdoCraneCogSettings
from toontown.toonbase import ToontownGlobals

Settings = EntityStateVarSet(CogdoCraneGameSettings)
CogSettings = EntityStateVarSet(CogdoCraneCogSettings)
Cutoff = 75.0
MusicFiles = {'normal': 'phase_9/audio/bgm/CHQ_FACT_bg.ogg',
              'end': 'phase_7/audio/bgm/encntr_toon_winning_indoor.ogg',
              'waiting': 'phase_7/audio/bgm/encntr_toon_winning_indoor.ogg',
              'invul': 'phase_9/audio/bgm/encntr_toon_winning.ogg',
              'timeRunningOut': 'phase_7/audio/bgm/encntr_suit_winning_indoor.ogg'}
SfxFiles = {'getMemo': 'phase_4/audio/sfx/MG_maze_pickup.ogg',
            'popupHelpText': 'phase_3/audio/sfx/GUI_balloon_popup.ogg',
            'lose': 'phase_4/audio/sfx/MG_lose.ogg',
            'win': 'phase_4/audio/sfx/MG_win.ogg',
            'cogDialogue': 'phase_3.5/audio/dial/COG_VO_statement.ogg',
            'toonDialogue': 'phase_3.5/audio/dial/AV_dog_long.ogg'}
GameDuration = 180
CranePosHprs = [(13.4 - 36.874, -136.6 + 113.682, 6, -45, 0, 0),
                (13.4 - 36.874, -91.4 + 113.682, 6, -135, 0, 0),
                (58.6 - 36.874, -91.4 + 113.682, 6, 135, 0, 0),
                (58.6 - 36.874, -136.6 + 113.682, 6, 45, 0, 0)]
MoneyBagPosHprs = [[10, 10, 6, 0, 0, 0],
                   [-10, 10, 6, 0, 0, 0],
                   [10, -10, 6, 0, 0, 0],
                   [-10, -10, 6, 0, 0, 0]]
IntroDurationSeconds = 24.0
MoneyBagsRespawnRate = 15.0
FinishDurationSeconds = 10.0
MoneyBagsJoinHeight = 70
SpotlightObstacleWait = 36
SpotlightStomperDamage = {
    ToontownGlobals.ToontownCentral: 5,
    ToontownGlobals.DonaldsDock: 10,
    ToontownGlobals.DaisyGardens: 15,
    ToontownGlobals.MinniesMelodyland: 18,
    ToontownGlobals.TheBrrrgh: 22,
    ToontownGlobals.DonaldsDreamland: 28,
}