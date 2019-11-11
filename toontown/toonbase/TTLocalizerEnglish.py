# coding=utf-8
from toontown.toonbase.TTLocalizerEnglishProperty import *
from toontown.catalog import CatalogAccessoryItemGlobals
from otp.otpbase import OTPLocalizer as OL
OL.SpeedChatStaticText = OL.SpeedChatStaticTextToontown.copy()
for key in OL.SpeedChatStaticTextCommon.iterkeys():
    OL.SpeedChatStaticText[key] = OL.SpeedChatStaticTextCommon[key]

commitmantst = 'kptmptest - removable'
InterfaceFont = 'phase_3/models/fonts/ImpressBT.ttf'
ToonFont = 'phase_3/models/fonts/ImpressBT.ttf'
SuitFont = 'phase_3/models/fonts/vtRemingtonPortable.ttf'
SignFont = 'phase_3/models/fonts/MickeyFont'
MinnieFont = 'phase_3/models/fonts/MinnieFont'
FancyFont = 'phase_3/models/fonts/Comedy'
NametagFonts = ('phase_3/models/fonts/AnimGothic',
 'phase_3/models/fonts/Aftershock',
 'phase_3/models/fonts/JiggeryPokery',
 'phase_3/models/fonts/Ironwork',
 'phase_3/models/fonts/HastyPudding',
 'phase_3/models/fonts/Comedy',
 'phase_3/models/fonts/Humanist',
 'phase_3/models/fonts/Portago',
 'phase_3/models/fonts/Musicals',
 'phase_3/models/fonts/Scurlock',
 'phase_3/models/fonts/Danger',
 'phase_3/models/fonts/Alie',
 'phase_3/models/fonts/OysterBar',
 'phase_3/models/fonts/RedDogSaloon')
NametagFontNames = ('Member',
 'Shivering',
 'Wonky',
 'Fancy',
 'Silly',
 'Zany',
 'Practical',
 'Nautical',
 'Whimsical',
 'Spooky',
 'Action',
 'Poetic',
 'Boardwalk',
 'Western')
NametagLabel = ' Nametag'
UnpaidNameTag = 'Basic'
GM_NAMES = ('TOON COUNCIL',
 'TOON TROOPER',
 'RESISTANCE RANGER',
 'GC')
BuildingNametagFont = 'phase_3/models/fonts/MickeyFont'
BuildingNametagShadow = None
ProductPrefix = 'TT'
Mickey = 'Mickey'
VampireMickey = 'VampireMickey'
Minnie = 'Minnie'
WitchMinnie = 'WitchMinnie'
Donald = 'Donald'
DonaldDock = 'DonaldDock'
FrankenDonald = 'FrankenDonald'
Daisy = 'Daisy'
SockHopDaisy = 'SockHopDaisy'
Goofy = 'Dingo'
SuperGoofy = 'SuperGoofy'
Pluto = 'Pluto'
WesternPluto = 'WesternPluto'
Flippy = 'Flippy'
Chip = 'Tic'
Dale = 'Tac'
JailbirdDale = 'JailbirdDale'
PoliceChip = 'PoliceChip'
lTheBrrrgh = 'Le Glagla'
lDaisyGardens = 'Le Jardin de Daisy'
lDonaldsDock = 'Quais Donald'
lDonaldsDreamland = 'Le Pays des R\xc3\xaaves de Donald'
lMinniesMelodyland = 'Le Pays Musical de Minnie'
lToontownCentral = 'Toontown Centre'
lToonHQ = 'QG des Toons'
lSellbotHQ = 'QG Vendibot'
lGoofySpeedway = 'Circuit Dingo'
lOutdoorZone = 'For\xc3\xaat de glands de Tic et Tac'
lGolfZone = 'Minigolf de Tic et Tac'
lPartyHood = 'Party Grounds'
GlobalStreetNames = {20000: ('vers la', 'sur la', 'terrasse du Tourbillon'),
    1000: ('vers le', 'sur le', 'Terrain de jeux'),
    1100: ('vers le', 'sur le', 'Boulevard de la Bernache'),
    1200: ('vers la', 'sur la', 'Rue des R\xc3\xa9cifs'),
    1300: ("vers l'", "sur l'", 'All\xc3\xa9e des Mar\xc3\xa9es'),
    2000: ('vers le', 'sur le', 'Terrain de jeux'),
    2100: ('vers la', 'sur la', 'Rue B\xc3\xa9ta'),
    2200: ("vers l'", "sur l'", 'Avenue des Fondus'),
    2300: ('vers la', 'sur la', 'Place des Blagues'),
    3000: ('vers le', 'sur le', 'Terrain de jeux'),
    3100: ('vers le', 'sur le', 'Chemin du Marin'),
    3200: ('vers la', 'sur la', 'Rue de la Neige fondue'),
    3300: ('vers la', 'sur la', 'Place Polaire'),
    4000: ('vers le', 'sur le', 'Terrain de jeux'),
    4100: ("vers l'", "sur l'", 'Avenue du Contralto'),
    4200: ('vers le', 'sur le', 'Boulevard du Baryton'),
    4300: ('vers la', 'sur la', 'Terrasse des T\xc3\xa9nors'),
    5000: ('vers le', 'sur le', 'Terrain de jeux'),
    5100: ('vers la', 'sur la', 'Rue des Ormes'),
    5200: ('vers la', 'sur la', 'Rue des \xc3\x89rables'),
    5300: ('vers la', 'sur la', 'Rue du Ch\xc3\xaane'),
    6000: ('to the', 'in the', 'Playground'),
    8000: ('to the', 'in the', 'Playground'),
    9000: ('vers le', 'sur le', 'Terrain de jeux'),
    9100: ('vers le', 'sur le', 'Boulevard de la Berceuse'),
    9200: ('', '', 'Place de la Couette'),
    10000: ('vers le', 'au', 'QG Chefbot'),
    10100: ('vers le', 'dans le', 'hall du QG des Chefbots'),
    10200: ('to the', 'in the', 'The Clubhouse'),
    10500: ('to the', 'in the', 'The Front Three'),
    10600: ('to the', 'in the', 'The Middle Six'),
    10700: ('to the', 'in the', 'The Back Nine'),
    11000: ('vers la', 'sur la', 'cour du QG Vendibot'),
    11100: ('vers le', 'dans le', 'hall du QG Vendibot'),
    11200: ("vers l'", "\xc3\xa0 l'", 'usine Vendibot'),
    11500: ("vers l'", "\xc3\xa0 l'", 'usine Vendibot'),
    12000: ('vers le', 'au', 'QG Caissbot'),
    12100: ('vers le', 'dans le', 'hall du QG Caissbot'),
    12500: ('', '', 'Fabrique \xc3\xa0 Sous Caissbot'),
    12600: ('', '', 'Fabrique \xc3\xa0 Euros Caissbot'),
    12700: ('', '', 'Fabrique \xc3\xa0 Lingots Caissbot'),
    13000: ('vers le', 'au', 'QG Loibot'),
    13100: ('vers le', 'dans le', 'hall du QG Loibot'),
    13200: ('vers le', 'au', 'hall du bureau du Procureur'),
    13300: ('vers le', 'au', 'bureau Loibot A'),
    13400: ('vers le', 'au', 'bureau Loibot B'),
    13500: ('vers le', 'au', 'bureau Loibot C'),
    13600: ('vers le', 'au', 'bureau Loibot D')}
DonaldsDock = ('vers les', 'sur les', 'Quais Donald')
ToontownCentral = ('vers', '\xc3\xa0', 'Toontown centre')
TheBrrrgh = ('vers', 'dans', 'le Glagla')
MinniesMelodyland = ('vers le', 'au', 'Pays musical de Minnie')
DaisyGardens = ('vers les', 'au', 'Jardins de Daisy')
ConstructionZone = ('vers la', 'dans la', 'Zone de construction')
FunnyFarm = ('vers la', 'dans la', 'Ferme farfelue')
GoofySpeedway = ('vers le', 'au', 'Circuit Dingo')
DonaldsDreamland = ('vers le', 'au', 'Pays des r\xc3\xaaves de Donald')
BossbotHQ = ('vers le', 'dans le', 'QG des Chefbots')
SellbotHQ = ('vers le', 'dans le', 'QG Vendibot')
CashbotHQ = ('vers le', 'dans le', 'QG Caissbot')
LawbotHQ = ('vers le', 'dans le', 'QG Loibot')
Tutorial = ('vers les', 'aux', 'Travaux pratiques')
MyEstate = ('vers', 'dans', 'ta maison')
WelcomeValley = ('vers la', 'dans la', 'Bienvenue')
GolfZone = ('to', 'in', lGolfZone)
PartyHood = ('to the', 'in the', lPartyHood)
Factory = 'Usine'
Headquarters = 'Quartiers g\xc3\xa9n\xc3\xa9raux'
SellbotFrontEntrance = 'Entr\xc3\xa9e principale'
SellbotSideEntrance = 'Entr\xc3\xa9e lat\xc3\xa9rale'
Office = 'Officier'
FactoryNames = {0: "Maquette d'usine",
 11500: 'Usine des Cogs Vendibots',
 13300: 'Bureau des Cogs Loibot'}
FactoryTypeLeg = 'Jambe'
FactoryTypeArm = 'Bras'
FactoryTypeTorso = 'Torse'
MintFloorTitle = '\xc3\x89tage %s'
lCancel = 'Annuler'
lClose = 'Fermer'
lOK = 'OK'
lNext = 'Suivant'
lQuit = 'Quitter'
lYes = 'Oui'
lNo = 'Non'
sleep_auto_reply = '%s is sleeping right now.'
sleep_auto_reply_retro = '%s is sleeping right now'
lHQOfficerF = 'Officier QG'
lHQOfficerM = 'Officier QG'
MickeyMouse = 'Mickey Mouse'
AIStartDefaultDistrict = 'Idioville'
Cog = 'Cog'
Cogs = 'Cogs'
ACog = 'un Cog'
TheCogs = 'les Cogs'
ASkeleton = 'a Skelecog'
Skeleton = 'Skelecog'
SkeletonP = 'Skelecogs'
Av2Cog = 'a Version 2.0 Cog'
v2Cog = 'Version 2.0 Cog'
v2CogP = 'Version 2.0 Cogs'
ASkeleton = 'un Skelecog'
Foreman = "Contrema\xc3\xaetre de l'usine"
ForemanP = "Contrema\xc3\xaetres de l'usine"
AForeman = "un contrema\xc3\xaetre de l'usine"
CogVP = 'Vice-\nPr\xc3\xa9sident ' + Cog
CogVPs = 'Vice-\nPr\xc3\xa9sidents Cogs'
ACogVP = 'Un Vice-\nPr\xc3\xa9sident ' + Cog
Supervisor = 'Superviseur de la Fabrique \xc3\xa0 Sous'
SupervisorP = 'Superviseurs de la Fabrique \xc3\xa0 Sous'
ASupervisor = 'un Superviseur de la Fabrique \xc3\xa0 Sous'
CogCFO = Cog + ' Vice-\nPr\xc3\xa9sident'
CogCFOs = 'Vice-\nPr\xc3\xa9sidents Cog'
ACogCFO = ACog + ' C.F.O.'
TheFish = 'les poissons'
AFish = 'un poisson'
Level = 'niveau'
QuestsCompleteString = 'Termin\xc3\xa9'
QuestsNotChosenString = 'Non choisi'
Period = '.'
Laff = 'Rigolpoints'
QuestInLocationString = ' %(inPhrase)s %(location)s'
QuestsDefaultGreeting = ('Bonjour, _avName_!',
'Oh\xc3\xa9, _avName_!',
'Coucou, _avName_!',
'Eh, _avName_!',
'Bienvenue, _avName_!',
'Salut, _avName_!',
'Comment \xc3\xa7a va, _avName_?',
'Quoi de neuf, _avName_?')
QuestsDefaultIncomplete = ('Comment est-ce que ce d\xc3\xa9fi se pr\xc3\xa9sente, _avName_?',
'On dirait que tu as encore du travail \xc3\xa0 faire pour ce d\xc3\xa9fi!',
'Continue \xc3\xa0 bien travailler, _avName_!',
'Essaie de finir ce d\xc3\xa9fi. Je sais que tu peux le faire!',
'Essaie de terminer ce d\xc3\xa9fi, nous comptons sur toi!',
'Continue \xc3\xa0 travailler sur ce d\xc3\xa9fitoon!')
QuestsDefaultIncompleteProgress = ("Tu es au bon endroit, mais tu dois d'abord finir ton d\xc3\xa9fitoon.",
'Quand tu auras termin\xc3\xa9 ton d\xc3\xa9fitoon, reviens ici.',
'Reviens quand tu auras termin\xc3\xa9 ton d\xc3\xa9fitoon.')
QuestsDefaultIncompleteWrongNPC = ('Joli travail pour ce d\xc3\xa9fitoon. Tu devrais aller voir _toNpcName_._where_',
'On dirait que tu as presque fini ton d\xc3\xa9fitoon. Va voir _toNpcName_._where_.',
'Va voir _toNpcName_ pour finir ton d\xc3\xa9fitoon._where_')
QuestsDefaultComplete = ('Bon travail! Voil\xc3\xa0 ta r\xc3\xa9compense...',
'Super boulot, _avName_! Prends cette r\xc3\xa9compense...',
'Excellent boulot, _avName_! Voil\xc3\xa0 ta r\xc3\xa9compense...')
QuestsDefaultLeaving = ('Salut!', 'Au revoir!', 'Bon vent, _avName_!', '\xc3\x80 plus, _avName_!', 'Bonne chance!',
                        'Amuse-toi bien \xc3\xa0 Toontown!', '\xc3\x80 plus tard!')
QuestsDefaultReject = ('Bonjour.', "Puis-je t'aider ?", 'Comment \xc3\xa7a va?', 'Bien le bonjour.',
                       'Je suis un peu occup\xc3\xa9 l\xc3\xa0, _avName_.', 'Oui?', 'Salut, _avName_!',
                       'Bienvenue, _avName_!', 'H\xc3\xa9, _avName_! Comment \xc3\xa7a va?',
                       'Sais-tu que tu peux ouvrir ton journal de bord en appuyant sur la touche F8?',
                       "Tu peux utiliser ta carte pour te t\xc3\xa9l\xc3\xa9porter jusqu'au terrain de jeux!",
                       'Tu peux devenir ami(e) avec les autres joueurs en cliquant sur eux.',
                       'Tu peux en savoir plus sur un  ' + Cog + ' en cliquant sur lui.',
                       'Trouve des tr\xc3\xa9sors sur les terrains de jeux pour remplir ton rigolm\xc3\xa8tre.',
                       'Les immeubles ' + Cog + " sont dangereux! N'y va pas tout seul!",
                       'Lorsque tu perds un combat, les ' + Cogs + ' prennent tous tes gags.',
                       'Pour avoir plus de gags, joue aux jeux du tramway!',
                       'Tu peux accumuler des rigolpoints en effectuant des d\xc3\xa9fitoons.',
                       'Chaque d\xc3\xa9fitoon te vaudra une r\xc3\xa9compense.',
                       "Certaines r\xc3\xa9compenses te permettent d'avoir plus de gags.",
                       'Si tu gagnes un combat, ton d\xc3\xa9fitoon est cr\xc3\xa9dit\xc3\xa9 pour chaque ' + Cog + ' vaincu.',
                       'Si tu regagnes un b\xc3\xa2timent ' + Cog + ", retourne \xc3\xa0 l'int\xc3\xa9rieur pour recevoir un remerciement sp\xc3\xa9cial de la part de son propri\xc3\xa9taire!",
                       'Si tu appuies sur la touche "page pr\xc3\xa9c\xc3\xa9dente", tu peux regarder vers le haut!',
                       "Si tu appuies sur la touche de tabulation, tu peux voir diff\xc3\xa9rents points de vue de ce qui t'entoure!",
                       "Pour montrer \xc3\xa0 tes amis ce que tu penses, entre un '.' avant ta pens\xc3\xa9e.",
                       'Si un ' + Cog + " est assomm\xc3\xa9, il lui est plus difficile d'\xc3\xa9viter les objets qui tombent.",
                       'Chaque type de b\xc3\xa2timent ' + Cog + ' a un aspect diff\xc3\xa9rent.',
                       "Tu obtiens plus de r\xc3\xa9compenses d'habilet\xc3\xa9 si tu vaincs des " + Cogs + ' aux plus hauts \xc3\xa9tages des b\xc3\xa2timents.')
QuestsDefaultTierNotDone = (
"Bonjour, _avName_! Tu dois terminer tes d\xc3\xa9fitoons commenc\xc3\xa9s avant d'en obtenir un autre.",
'Salut! Tu dois terminer les d\xc3\xa9fitoons sur lesquels tu es en train de travailler pour en obtenir un nouveau.',
'Oh\xc3\xa9, _avName_! Pour que je puisse te donner un autre d\xc3\xa9fitoon, tu dois finir ceux que tu as d\xc3\xa9j\xc3\xa0.')
QuestsDefaultQuest = None
QuestsDefaultVisitQuestDialog = (
"J'ai entendu dire que _toNpcName_ te cherchait._where_", 'Arr\xc3\xaate-toi voir _toNpcName_ quand tu pourras._where_',
'Va donc voir _toNpcName_ la prochaine fois que tu passes par l\xc3\xa0-bas._where_',
'Si tu peux, arr\xc3\xaate-toi dire bonjour \xc3\xa0 _toNpcName_._where_',
'_toNpcName_ va te donner ton prochain d\xc3\xa9fitoon._where_')
QuestsLocationArticle = ''

def getLocalNum(num):
    return str(num)


QuestsItemNameAndNum = '%(num)s %(name)s'
QuestsCogQuestProgress = '%(progress)s sur %(numCogs)s sont vaincus'
QuestsCogQuestHeadline = 'RECHERCHE'
QuestsCogQuestSCStringS = 'Je dois vaincre %(cogName)s%(cogLoc)s'
QuestsCogQuestSCStringP = 'Je dois vaincre quelques %(cogName)s%(cogLoc)s'
QuestsCogQuestDefeat = 'Tu dois vaincre %s'
QuestsCogQuestDefeatDesc = '%(numCogs)s %(cogName)s'
QuestsCogNewNewbieQuestObjective = 'Aide un nouveau Toon \xc3\xa0 vaincre %s'
QuestsCogNewNewbieQuestCaption = 'Aide un nouveau Toon qui a %d rigolpoints ou moins'
QuestsCogOldNewbieQuestObjective = 'Aide un Toon avec %(laffPoints)d rigolpoints ou moins \xc3\xa0 vaincre %(objective)s'
QuestsCogOldNewbieQuestCaption = 'Aide un Toon avec %d rigolpoints ou moins'
QuestsCogNewbieQuestAux = 'Tu dois\nvaincre:'
QuestsNewbieQuestHeadline = 'APPRENTI'
QuestsCogTrackQuestProgress = '%(progress)s sur %(numCogs)s sont vaincus'
QuestsCogTrackQuestHeadline = 'RECHERCHE'
QuestsCogTrackQuestSCStringS = 'Je dois vaincre %(cogText)s%(cogLoc)s'
QuestsCogTrackQuestSCStringP = 'Je dois vaincre quelques %(cogText)s%(cogLoc)s.'
QuestsCogTrackQuestDefeat = 'Tu dois vaincre %s'
QuestsCogTrackDefeatDesc = '%(numCogs)s %(trackName)s'
QuestsCogLevelQuestProgress = '%(progress)s sur %(numCogs)s sont vaincus'
QuestsCogLevelQuestHeadline = 'RECHERCHE'
QuestsCogLevelQuestDefeat = 'Tu dois vaincre %s'
QuestsCogLevelQuestDesc = 'un Cog de niveau %(level)s+'
QuestsCogLevelQuestDescC = '%(count)s Cogs de niveau %(level)s+'
QuestsCogLevelQuestDescI = 'des Cogs de niveau %(level)s+'
QuestsCogLevelQuestSCString = 'Je dois vaincre %(objective)s%(location)s.'
QuestsBuildingQuestFloorNumbers = ('',
'deux+',
'trois+',
'quatre+',
'cinq+')
QuestsBuildingQuestBuilding = 'B\xc3\xa2timent'
QuestsBuildingQuestBuildings = 'B\xc3\xa2timents'
QuestsBuildingQuestHeadline = 'VAINCRE'
QuestsBuildingQuestProgressString = '%(progress)s sur %(num)s sont vaincus'
QuestsBuildingQuestString = 'Tu dois vaincre %s'
QuestsBuildingQuestSCString = 'Je dois vaincre %(objective)s%(location)s.'
QuestsBuildingQuestDesc = 'un b\xc3\xa2timent %(type)s'
QuestsBuildingQuestDescF = 'un b\xc3\xa2timent %(type)s de %(floors)s \xc3\xa9tages'
QuestsBuildingQuestDescC = '%(count)s b\xc3\xa2timents %(type)s '
QuestsBuildingQuestDescCF = '%(count)s b\xc3\xa2timents %(type)s de %(floors)s \xc3\xa9tages'
QuestsBuildingQuestDescI = 'des b\xc3\xa2timents %(type)s'
QuestsBuildingQuestDescIF = 'des b\xc3\xa2timents %(type)s de %(floors)s \xc3\xa9tages'
QuestFactoryQuestFactory = 'Usine'
QuestsFactoryQuestFactories = 'Usines'
QuestsFactoryQuestHeadline = 'VAINCRE'
QuestsFactoryQuestProgressString = '%(progress)s sur%(num)s sont vaincus'
QuestsFactoryQuestString = 'Tu dois vaincre %s'
QuestsFactoryQuestSCString = 'Je dois vaincre %(objective)s%(location)s.'
QuestsFactoryQuestDesc = 'une usine %(type)s'
QuestsFactoryQuestDescC = '%(count)s usines %(type)s'
QuestsFactoryQuestDescI = 'des usines %(type)s'
QuestMintQuestMint = 'Fabrique \xc3\xa0 Sous'
QuestsMintQuestMints = 'Fabriques \xc3\xa0 Sous'
QuestsMintQuestHeadline = 'VAINCRE'
QuestsMintQuestProgressString = '%(progress)s de %(num)s vaincus'
QuestsMintQuestString = 'Vaincre %s'
QuestsMintQuestSCString = 'Je dois vaincre %(objective)s%(location)s.'
QuestsMintQuestDesc = 'une Fabrique \xc3\xa0 Sous Cog'
QuestsMintQuestDescC = '%(count)s Fabriques \xc3\xa0 Sous Cog'
QuestsMintQuestDescI = 'des Fabriques \xc3\xa0 Sous Cog'
QuestsRescueQuestProgress = '%(progress)s sur %(numToons)s sont sauv\xc3\xa9s'
QuestsRescueQuestHeadline = 'SAUVER'
QuestsRescueQuestSCStringS = 'Je dois sauver un Toon%(toonLoc)s.'
QuestsRescueQuestSCStringP = 'Je dois sauver des Toons%(toonLoc)s.'
QuestsRescueQuestRescue = 'Tu dois sauver %s'
QuestsRescueQuestRescueDesc = '%(numToons)s Toons'
QuestsRescueQuestToonS = 'un Toon'
QuestsRescueQuestToonP = 'Toons'
QuestsRescueQuestAux = 'Tu dois sauver:'
QuestsRescueNewNewbieQuestObjective = 'Aide un nouveau Toon \xc3\xa0 sauver %s'
QuestsRescueOldNewbieQuestObjective = 'Aide un Toon avec %(laffPoints)d rigolpoints ou moins \xc3\xa0 vaincre %(objective)s'
QuestCogPartQuestCogPart = 'Pi\xc3\xa8ce de costume de Cog'
QuestsCogPartQuestFactories = 'Usines'
QuestsCogPartQuestHeadline = 'R\xc3\x89CUP\xc3\x89RER'
QuestsCogPartQuestProgressString = '%(progress)s sur %(num)s sont r\xc3\xa9cup\xc3\xa9r\xc3\xa9s'
QuestsCogPartQuestString = 'R\xc3\xa9cup\xc3\xa9rer %s'
QuestsCogPartQuestSCString = 'Je dois r\xc3\xa9cup\xc3\xa9rer %(objective)s%(location)s.'
QuestsCogPartQuestAux = 'Tu dois r\xc3\xa9cup\xc3\xa9rer:'
QuestsCogPartQuestDesc = 'une pi\xc3\xa8ce de costume de Cog'
QuestsCogPartQuestDescC = '%(count)s pi\xc3\xa8ces de costume de Cog'
QuestsCogPartQuestDescI = 'des pi\xc3\xa8ces de costume de Cog'
QuestsCogPartNewNewbieQuestObjective = 'Aide un nouveau Toon \xc3\xa0 r\xc3\xa9cup\xc3\xa9rer %s'
QuestsCogPartOldNewbieQuestObjective = 'Aide un Toon avec %(laffPoints)d rigolpoints ou moins \xc3\xa0 vaincre %(objective)s'
QuestsDeliverGagQuestProgress = '%(progress)s sur %(numGags)s sont livr\xc3\xa9s'
QuestsDeliverGagQuestHeadline = 'LIVRER'
QuestsDeliverGagQuestToSCStringS = 'Je dois livrer %(gagName)s.'
QuestsDeliverGagQuestToSCStringP = 'Je dois livrer des %(gagName)s.'
QuestsDeliverGagQuestSCString = 'Je dois faire une livraison.'
QuestsDeliverGagQuestString = 'Tu dois livrer %s'
QuestsDeliverGagQuestStringLong = 'Tu dois livrer %s \xc3\xa0 _toNpcName_.'
QuestsDeliverGagQuestInstructions = 'Tu pourras acheter ce gag \xc3\xa0 la Boutique \xc3\xa0 gags une fois que tu en auras gagn\xc3\xa9 le droit.'
QuestsDeliverItemQuestProgress = ''
QuestsDeliverItemQuestHeadline = 'LIVRER'
QuestsDeliverItemQuestSCString = 'Je dois livrer %(article)s%(itemName)s.'
QuestsDeliverItemQuestString = 'Tu dois livrer %s'
QuestsDeliverItemQuestStringLong = 'Tu dois livrer %s \xc3\xa0 _toNpcName_.'
QuestsVisitQuestProgress = ''
QuestsVisitQuestHeadline = 'VISITER'
QuestsVisitQuestStringShort = 'Tu dois rendre visite'
QuestsVisitQuestStringLong = 'Rends visite \xc3\xa0 _toNpcName_'
QuestsVisitQuestSeeSCString = 'Je dois voir %s.'
QuestsRecoverItemQuestProgress = '%(progress)s sur %(numItems)s sont repris'
QuestsRecoverItemQuestHeadline = 'REPRENDRE'
QuestsRecoverItemQuestSeeHQSCString = 'Je dois voir un officier du QG.'
QuestsRecoverItemQuestReturnToHQSCString = 'Je dois rendre %s \xc3\xa0 un officier du QG.'
QuestsRecoverItemQuestReturnToSCString = 'Je dois rendre %(item)s \xc3\xa0 %(npcName)s.'
QuestsRecoverItemQuestGoToHQSCString = 'Je dois aller \xc3\xa0 un QG des Toons.'
QuestsRecoverItemQuestGoToPlaygroundSCString = 'Je dois aller au terrain de jeux de %s.'
QuestsRecoverItemQuestGoToStreetSCString = 'Je dois aller %(to)s %(street)s dans %(hood)s.'
QuestsRecoverItemQuestVisitBuildingSCString = 'Je dois rendre visite \xc3\xa0 %s%s.'
QuestsRecoverItemQuestWhereIsBuildingSCString = 'O\xc3\xb9 est %s%s?'
QuestsRecoverItemQuestRecoverFromSCString = 'Je dois reprendre %(item)s \xc3\xa0 %(holder)s%(loc)s.'
QuestsRecoverItemQuestString = 'Reprendre %(item)s \xc3\xa0 %(holder)s'
QuestsRecoverItemQuestHolderString = '%(level)s %(holder)d+ %(cogs)s'
QuestsTrackChoiceQuestHeadline = 'CHOISIR'
QuestsTrackChoiceQuestSCString = 'Je dois choisir entre %(trackA)s et %(trackB)s.'
QuestsTrackChoiceQuestMaybeSCString = 'Je devrais peut-\xc3\xaatre choisir %s.'
QuestsTrackChoiceQuestString = 'Choisis entre %(trackA)s et %(trackB)s.'
QuestsFriendQuestHeadline = 'AMI'
QuestsFriendQuestSCString = 'Je dois trouver un(e) ami(e).'
QuestsFriendQuestString = 'Trouve un(e) ami(e).'
QuestsMailboxQuestHeadline = 'COURRIER'
QuestsMailboxQuestSCString = 'Je dois v\xc3\xa9rifier mon courrier.'
QuestsMailboxQuestString = 'V\xc3\xa9rifie ton courrier.'
QuestsPhoneQuestHeadline = 'CLARABELLE'
QuestsPhoneQuestSCString = 'Je dois appeler Clarabelle.'
QuestsPhoneQuestString = 'Appelle Clarabelle.'
QuestsFriendNewbieQuestString = ' Trouve %d contacts de %d rigolpoints ou moins'
QuestsFriendNewbieQuestProgress = '%(progress)s sur %(numFriends)s sont trouv\xc3\xa9s.'
QuestsFriendNewbieQuestObjective = 'Deviens ami(e) avec %d nouveaux Toons.'
QuestsTrolleyQuestHeadline = 'TRAMWAY'
QuestsTrolleyQuestSCString = 'Je dois faire un tour de tramway.'
QuestsTrolleyQuestString = 'Fais un tour de tramway.'
QuestsTrolleyQuestStringShort = 'Prends le tramway.'
QuestsMinigameNewbieQuestString = '%d Mini jeux'
QuestsMinigameNewbieQuestProgress = '%(progress)s sur %(numMinigames)s ont \xc3\xa9t\xc3\xa9 jou\xc3\xa9s.'
QuestsMinigameNewbieQuestObjective = 'Jouer \xc3\xa0 %d mini jeux avec de nouveaux Toons'
QuestsMinigameNewbieQuestSCString = 'Je dois jouer aux mini jeux avec de nouveaux Toons.'
QuestsMinigameNewbieQuestCaption = 'Aide un nouveau Toon qui a %d rigolpoints ou moins.'
QuestsMinigameNewbieQuestAux = 'Tu dois jouer:'
QuestsMaxHpReward = 'Ta rigo-limite a \xc3\xa9t\xc3\xa9 augment\xc3\xa9e de %s.'
QuestsMaxHpRewardPoster = 'R\xc3\xa9compense: Rigol-augmentation de %s point(s)'
QuestsMoneyRewardSingular = 'Tu obtiens 1 bonbon.'
QuestsMoneyRewardPlural = 'Tu obtiens %s bonbons.'
QuestsMoneyRewardPosterSingular = 'R\xc3\xa9compense: 1 bonbon'
QuestsMoneyRewardPosterPlural = 'R\xc3\xa9compense: %s bonbons'
QuestsMaxMoneyRewardSingular = 'Tu peux maintenant avoir 1 bonbon.'
QuestsMaxMoneyRewardPlural = 'Tu peux maintenant avoir %s bonbons.'
QuestsMaxMoneyRewardPosterSingular = 'R\xc3\xa9compense: Tu as 1 bonbon.'
QuestsMaxMoneyRewardPosterPlural = 'R\xc3\xa9compense: Tu as %s bonbons.'
QuestsMaxGagCarryReward = 'Tu as un %(name)s. Tu peux maintenant avoir %(num)s gags.'
QuestsMaxGagCarryRewardPoster = 'R\xc3\xa9compense: (%(num)s) %(name)s'
QuestsMaxQuestCarryReward = ' Tu peux maintenant avoir %s d\xc3\xa9fitoons.'
QuestsMaxQuestCarryRewardPoster = 'R\xc3\xa9compense: Tu as %s d\xc3\xa9fitoons'
QuestsTeleportReward = 'Tu peux maintenant acc\xc3\xa9der par t\xc3\xa9l\xc3\xa9portation \xc3\xa0 %s.'
QuestsTeleportRewardPoster = 'R\xc3\xa9compense: Acc\xc3\xa8s par t\xc3\xa9l\xc3\xa9portation \xc3\xa0 %s'
QuestsTrackTrainingReward = 'Tu peux maintenant t\'entra\xc3\xaener pour les gags "%s".'
QuestsTrackTrainingRewardPoster = 'R\xc3\xa9compense: Entra\xc3\xaenement aux gags'
QuestsTrackProgressReward = "Tu as maintenant l'image %(frameNum)s de l'animation de la s\xc3\xa9rie %(trackName)s."
QuestsTrackProgressRewardPoster = 'R\xc3\xa9compense: image %(frameNum)s de l\'animation de la s\xc3\xa9rie "%(trackName)s"'
QuestsTrackCompleteReward = 'Tu peux maintenant avoir et utiliser des gags "%s".'
QuestsTrackCompleteRewardPoster = 'R\xc3\xa9compense: Entra\xc3\xaenement final aux s\xc3\xa9ries %s'
QuestsClothingTicketReward = 'Tu peux changer de v\xc3\xaatements.'
QuestsClothingTicketRewardPoster = "R\xc3\xa9compense: Ticket d'habillement"
TIPQuestsClothingTicketReward = 'You can change your shirt for a TIP shirt'
TIPQuestsClothingTicketRewardPoster = 'Reward: TIP Clothing Ticket'
QuestsCheesyEffectRewardPoster = 'R\xc3\xa9compense: %s'
QuestsCogSuitPartReward = 'Tu as maintenant une %(cogTrack)s %(part)s pi\xc3\xa8ce de costume de Cog.'
QuestsCogSuitPartRewardPoster = 'R\xc3\xa9compense: %(cogTrack)s %(part)s pi\xc3\xa8ce'
QuestsStreetLocationThisPlayground = 'sur ce terrain de jeux'
QuestsStreetLocationThisStreet = 'sur cette rue'
QuestsStreetLocationNamedPlayground = 'sur le terrain de jeux de %s'
QuestsStreetLocationNamedStreet = 'sur %(toStreetName)s dans %(toHoodName)s'
QuestsLocationString = '%(string)s%(location)s'
QuestsLocationBuilding = 'Le b\xc3\xa2timent de %s est appel\xc3\xa9'
QuestsLocationBuildingVerb = 'qui est'
QuestsLocationParagraph = '\x7 %(building)s "%(buildingName)s "...\x7...%(buildingVerb)s %(street)s.'
QuestsGenericFinishSCString = 'Je dois terminer un d\xc3\xa9fitoon.'
QuestsMediumPouch = 'Bourse moyenne'
QuestsLargePouch = 'Grande bourse'
QuestsSmallBag = 'Petit sac'
QuestsMediumBag = 'Sac moyen'
QuestsLargeBag = 'Grand sac'
QuestsSmallBackpack = 'Petit sac \xc3\xa0 dos'
QuestsMediumBackpack = 'Sac \xc3\xa0 dos moyen'
QuestsLargeBackpack = 'Grand sac \xc3\xa0 dos'
QuestsItemDict = {1: ['Paire de lunettes', 'Paires de lunettes', 'une'],
2: ['Cl\xc3\xa9', 'Cl\xc3\xa9s', 'une'],
3: ['Tableau', 'Tableaux', 'un'],
4: ['Livre', 'Livres',  'un'],
5: [
        "Sucre d'orge",
        "Sucres d'orge",
        'un'],
    6: [
        'Craie',
        'Craies',
        'une'],
    7: [
        'Recette',
        'Recettes',
        'une'],
    8: [
        'Note',
        'Notes',
        'une'],
    9: [
        'Machine \xc3\xa0 calculer',
        'Machines \xc3\xa0 calculer',
        'une'],
    10: [
        'Pneu de voiture de clown',
        'Pneus de voiture de clown',
        'un'],
    11: [
        'Pompe \xc3\xa0 air',
        'Pompes \xc3\xa0 air',
        'une'],
    12: [
        'Encre de seiche',
        'Encres de seiche',
        "de l'"],
    13: [
        'Paquet',
        'Paquets',
        'un '],
    14: [
        'Re\xc3\xa7u de poisson dor\xc3\xa9',
        'Re\xc3\xa7us de poissons dor\xc3\xa9s',
        'un '],
    15: [
        'Poisson dor\xc3\xa9',
        'Poissons dor\xc3\xa9s',
        'un '],
    16: [
        'Huile',
        'Huiles',
        "de l'"],
    17: [
        'Graisse',
        'Graisses',
        'de la '],
    18: [
        'Eau',
        'Eaux',
        "de l'"],
    19: [
        'Rapport de pignons',
        'Rapports de pignons',
        'un '],
    20: [
        'Brosse \xc3\xa0 Tableaux',
        'Brosses \xc3\xa0 Tableaux',
        'une '],
    1000: [
        "Ticket d'habillement",
        "Tickets d'habillement",
        'un '],
    2001: [
        'Chambre \xc3\xa0 air',
        'Chambres \xc3\xa0 air',
        'une '],
    2002: [
        'Ordonnance de monocle',
        'Ordonnances de monocles',
        'une '],
    2003: [
        'Monture de monocle',
        'Montures de monocles',
        'une '],
    2004: [
        'Monocle',
        'Monocles',
        'un '],
    2005: [
        'Grande perruque blanche',
        'Grandes perruques blanches',
        'une '],
    2006: [
        'Boisseau de lest',
        'Boisseaux de lest',
        'un '],
    2007: [
        '\xc3\x89quipement de Cog',
        '\xc3\x89quipements de Cog',
        'un '],
    2008: [
        'Carte marine',
        'Cartes marines',
        'une '],
    2009: [
        'Manille crado',
        'Manilles crados',
        'un '],
    2010: [
        'Manille propre',
        'Manilles propres',
        'un '],
    2011: [
        "Ressort d'horloge",
        "Ressorts d'horloge",
        'un '],
    2012: [
        'Contrepoids',
        'Contrepoids',
        'un '],
    4001: [
        'Inventaire de Tina',
        'Inventaires de Tina',
        ''],
    4002: [
        'Inventaire de Yuki',
        'Inventaires de Yuki',
        ''],
    4003: [
        "Formulaire d'inventaire",
        "Formulaires d'inventaire",
        'un '],
    4004: [
        'Inventaire de Fifi',
        'Inventaires de Fifi',
        ''],
    4005: [
        'Ticket de Jack B\xc3\xbbcheron',
        'Tickets de Jack B\xc3\xbbcheron',
        ''],
    4006: [
        'Ticket de Tabatha',
        'Tickets de Tabatha',
        ''],
    4007: [
        'Ticket de Barry',
        'Tickets de Barry',
        ''],
    4008: [
        'Castagnette ternie',
        'Castagnettes ternies',
        ''],
    4009: [
        'Encre de seiche bleue',
        'Encre de seiche bleue',
        "de l'"],
    4010: [
        'Castagnette brillante',
        'Castagnettes brillantes',
        'une '],
    4011: [
        'Paroles de L\xc3\xa9o',
        'Paroles de L\xc3\xa9o',
        ''],
    5001: [
        'Cravate en soie',
        'Cravates en soie',
        'une '],
    5002: [
        'Costume \xc3\xa0 rayures',
        'Costumes \xc3\xa0 rayures',
        'un '],
    5003: [
        'Paire de ciseaux',
        'Paires de ciseaux',
        'une '],
    5004: [
        'Carte postale',
        'Cartes postales',
        'une '],
    5005: [
        'Crayon',
        'Crayons',
        'un '],
    5006: [
        'Encrier',
        'Encriers',
        'un '],
    5007: [
        'Bloc-notes',
        'Blocs-notes',
        'un '],
    5008: [
        'Coffre de bureau',
        'Coffres de bureau',
        'un '],
    5009: [
        'Sac de graines pour oiseaux',
        'Sacs de graines pour oiseaux',
        'un '],
    5010: [
        'Pignon',
        'Pignons',
        'un '],
    5011: [
        'Salade',
        'Salades',
        'une '],
    5012: [
        'Cl\xc3\xa9 du jardin de Daisy',
        'Cl\xc3\xa9s du jardin de Daisy',
        'une '],
    5013: [
        'Plans du QG Vendibot',
        'Plans du QG Vendibot',
        'des '],
    5014: [
        'Note de service du QG Vendibot',
        'Notes de service du QG Vendibot',
        'une '],
    5015: [
        'Note de service du QG Vendibot',
        'Notes de service du QG Vendibot',
        'une '],
    5016: [
        'Note de service du QG Vendibot',
        'Notes de service du QG Vendibot',
        'une '],
    5017: [
        'Note de service du QG Vendibot',
        'Notes de service du QG Vendibot',
        'une '],
    3001: [
        'Ballon de foot',
        'Ballons de foot',
        'un '],
    3002: [
        'Luge',
        'Luges',
        'une '],
    3003: [
        'Gla\xc3\xa7on',
        'Gla\xc3\xa7ons',
        'un '],
    3004: [
        "Lettre d'amour",
        "Lettres d'amour",
        'une '],
    3005: [
        'Teckel',
        'Teckels',
        'un '],
    3006: [
        'Bague de fian\xc3\xa7ailles',
        'Bagues de fian\xc3\xa7ailles',
        'une '],
    3007: [
        'Moustaches de sardine',
        'Moustaches de sardines',
        'des '],
    3008: [
        'Potion calmante',
        'Potions calmantes',
        'une '],
    3009: [
        'Dent cass\xc3\xa9e',
        'Dents cass\xc3\xa9es',
        'une '],
    3010: [
        'Dent en or',
        'Dents en or',
        'une '],
    3011: [
        'Pain aux pommes de pin',
        'Pains aux pommes de pin',
        'un '],
    3012: [
        'Fromage grumeleux',
        'Fromages grumeleux',
        'du '],
    3013: [
        'Cuill\xc3\xa8re ordinaire',
        'Cuill\xc3\xa8res ordinaires',
        'une '],
    3014: [
        'Crapaud parlant',
        'Crapauds parlants',
        'un '],
    3015: [
        'C\xc3\xb4ne de glace',
        'C\xc3\xb4nes de glace',
        'un '],
    3016: [
        'Poudre \xc3\xa0 perruque',
        'Poudres \xc3\xa0 perruques',
        'de la '],
    3017: [
        'Canard en plastique',
        'Canards en plastique',
        'un '],
    3018: [
        'D\xc3\xa9s en peluche',
        'D\xc3\xa9s en peluche',
        'des '],
    3019: [
        'Micro',
        'Micros',
        'un '],
    3020: [
        'Clavier \xc3\xa9lectrique',
        'Claviers \xc3\xa9lectriques',
        'un '],
    3021: [
        'Chaussures \xc3\xa0 plate-forme',
        'Chaussures \xc3\xa0 plate-forme',
        'des '],
    3022: [
        'Caviar',
        'Caviar',
        'du '],
    3023: [
        'Poudre de maquillage',
        'Poudres de maquillage',
        'de la '],
    3024: [
        'Fil',
        'Fil',
        'du '],
    3025: [
        'Aiguille \xc3\xa0 tricoter',
        'Aiguilles \xc3\xa0 tricoter',
        'une '],
    3026: [
        'Alibi',
        'Alibis',
        'un '],
    3027: [
        'Thermom\xc3\xa8tre ext\xc3\xa9rieur',
        'Thermom\xc3\xa8tres ext\xc3\xa9rieurs',
        'un '],
    6001: [
        'Plans du QG Caissbot ',
        'Plans du QG Caissbot ',
        'des '],
    6002: [
        'Tige',
        'Tiges',
        'une '],
    6003: [
        'Courroie',
        'Courroies',
        'une '],
    6004: [
        'Tenaille',
        'Tenailles',
        'une '],
    6005: [
        'Lampe de lecture',
        'Lampes de lecture',
        'une '],
    6006: [
        'Cithare',
        'Cithares',
        'une '],
    6007: [
        'Surfaceuse',
        'Surfaceuses',
        'une '],
    6008: [
        'Coussin z\xc3\xa8bre',
        'Coussins z\xc3\xa8bre',
        'un '],
    6009: [
        'Zinnia',
        'Zinnias',
        'quelques '],
    6010: [
        'Disques de Zydeco',
        'Disques de Zydeco',
        'des '],
    6011: [
        'Courgette',
        'Courgettes',
        'une '],
    6012: [
        'Costume de zazou',
        'Costumes de zazou',
        'un '],
    7001: [
        'Lit ordinaire',
        'Lits ordinaires',
        'un '],
    7002: [
        'Lit fantaisie',
        'Lits fantaisie',
        'un '],
    7003: [
        'Dessus-de-lit bleu',
        'Dessus-de-lit bleus',
        'un '],
    7004: [
        'Dessus-de-lit motif cachemire',
        'Dessus-de-lit motif cachemire',
        'un '],
    7005: [
        'Oreillers',
        'Oreillers',
        'des '],
    7006: [
        'Oreillers durs',
        'Oreillers durs',
        'des '],
    7007: [
        'Pyjama',
        'Pyjamas',
        'un '],
    7008: [
        'Grenouill\xc3\xa8re',
        'Grenouill\xc3\xa8res',
        'une '],
    7009: [
        'Grenouill\xc3\xa8re puce',
        'Grenouill\xc3\xa8res puce',
        'une '],
    7010: [
        'Grenouill\xc3\xa8re fuchsia',
        'Grenouill\xc3\xa8res fuchsia',
        'une '],
    7011: [
        'Corail chou-fleur',
        'Coraux chou-fleur',
        'du '],
    7012: [
        'Algue gluante',
        'Algues gluantes',
        "de l'"],
    7013: [
        'Pilon',
        'Pilons',
        'un '],
    7014: [
        'Pot de cr\xc3\xa8me antirides',
        'Pots de cr\xc3\xa8me antirides',
        'un ']}
QuestsHQOfficerFillin = lHQOfficerM
QuestsHQWhereFillin = ''
QuestsHQBuildingNameFillin = lToonHQ
QuestsHQLocationNameFillin = "dans n'importe quel quartier"
QuestsTailorFillin = 'Tailleur'
QuestsTailorWhereFillin = ''
QuestsTailorBuildingNameFillin = 'Boutique de pr\xc3\xaat-\xc3\xa0-porter'
QuestsTailorLocationNameFillin = "dans n'importe quel quartier"
QuestsTailorQuestSCString = "J'ai besoin de voir un tailleur."
QuestMovieQuestChoiceCancel = "Reviens plus tard si tu as besoin d'un d\xc3\xa9fitoon! Salut!"
QuestMovieTrackChoiceCancel = 'Reviens quand tu es pr\xc3\xaat \xc3\xa0 te d\xc3\xa9cider!! Salut!'
QuestMovieQuestChoice = 'Choisis un d\xc3\xa9fitoon.'
QuestMovieTrackChoice = 'Pr\xc3\xaat \xc3\xa0 te d\xc3\xa9cider ? Choisis une s\xc3\xa9rie, ou reviens plus tard.'
GREETING = 0
QUEST = 1
INCOMPLETE = 2
INCOMPLETE_PROGRESS = 3
INCOMPLETE_WRONG_NPC = 4
COMPLETE = 5
LEAVING = 6
TheBrrrghTrackQuestDict = {
    GREETING: '',
    QUEST: "Maintenant tu es pr\xc3\xaat(e).\x7Sors et fais un tour avant de d\xc3\xa9cider quelle s\xc3\xa9rie tu voudras choisir.\x7Choisis bien, parce que c'est ta derni\xc3\xa8re s\xc3\xa9rie.\x7Quand tu auras d\xc3\xa9cid\xc3\xa9, reviens me voir.",
    INCOMPLETE_PROGRESS: 'Choisis bien.',
    INCOMPLETE_WRONG_NPC: 'Choisis bien.',
    COMPLETE: 'Choix tr\xc3\xa8s sage!',
    LEAVING: 'Bonne chance. Reviens me voir quand tu as ma\xc3\xaetris\xc3\xa9 ta nouvelle habilet\xc3\xa9.'}
QuestDialog_3225 = {
    QUEST: "Oh, merci pour ta visite, _avName_!\x7Les Cogs du quartier ont effray\xc3\xa9 mon livreur.\x7Je n'ai personne pour livrer cette salade \xc3\xa0 _toNpcName_!\x7Peux-tu le faire pour moi? Merci beaucoup!_where_"}
QuestDialog_2910 = {
    QUEST: 'D\xc3\xa9j\xc3\xa0 de retour ?\x7Super travail avec le ressort.\x7Le dernier article est un contrepoids.\x7Va donc voir _toNpcName_ et ram\xc3\xa8ne tout ce que tu peux._where_'}
QuestDialogDict = {
    160: {
        GREETING: '',
        QUEST: 'OK, maintenant je crois que nous sommes pr\xc3\xaats pour quelque chose de plus compliqu\xc3\xa9.\x7Tu dois vaincre 3 Chefbots.',
        INCOMPLETE_PROGRESS: 'Les ' + Cogs + ' sont dans les rues, dans les tunnels.',
        INCOMPLETE_WRONG_NPC: 'Bien, tu as battu ces Chefbots! Maintenant, va au quartier g\xc3\xa9n\xc3\xa9ral des Toons pour recevoir ta r\xc3\xa9compense!',
        COMPLETE: QuestsDefaultComplete,
        LEAVING: QuestsDefaultLeaving},
    161: {
        GREETING: '',
        QUEST: 'OK, maintenant je crois que nous sommes pr\xc3\xaats pour quelque chose de plus compliqu\xc3\xa9.\x7Tu dois vaincre 3 Loibots.',
        INCOMPLETE_PROGRESS: 'Les ' + Cogs + ' sont dans les rues, dans les tunnels.',
        INCOMPLETE_WRONG_NPC: 'Bien, tu as battu ces Loibots! Maintenant, va au quartier g\xc3\xa9n\xc3\xa9ral des Toons pour recevoir ta r\xc3\xa9compense!',
        COMPLETE: QuestsDefaultComplete,
        LEAVING: QuestsDefaultLeaving},
    162: {
        GREETING: '',
        QUEST: 'OK, maintenant je crois que nous sommes pr\xc3\xaats pour quelque chose de plus compliqu\xc3\xa9.\x7Tu dois vaincre 3 Caissbots.',
        INCOMPLETE_PROGRESS: 'Les ' + Cogs + ' sont dans les rues, dans les tunnels.',
        INCOMPLETE_WRONG_NPC: 'Bien, tu as battu ces Caissbots! Maintenant, va au quartier g\xc3\xa9n\xc3\xa9ral des Toons pour recevoir ta r\xc3\xa9compense!',
        COMPLETE: QuestsDefaultComplete,
        LEAVING: QuestsDefaultLeaving},
    163: {
        GREETING: '',
        QUEST: 'OK, maintenant je crois que nous sommes pr\xc3\xaats pour quelque chose de plus compliqu\xc3\xa9.\x7Tu dois vaincre 3 Vendibots.',
        INCOMPLETE_PROGRESS: 'Les ' + Cogs + ' sont dans les rues, dans les tunnels.',
        INCOMPLETE_WRONG_NPC: 'Bien, tu as battu ces Vendibots! Maintenant, va au quartier g\xc3\xa9n\xc3\xa9ral des Toons pour recevoir ta r\xc3\xa9compense!',
        COMPLETE: QuestsDefaultComplete,
        LEAVING: QuestsDefaultLeaving},
    164: {
        QUEST: "Il semble que tu as besoin de nouveaux gags.\x7Va voir Flippy, peut-\xc3\xaatre pourra-t-il t'aider._where_"},
    165: {
        QUEST: "Salut!\x7On dirait que tu as besoin de t'entra\xc3\xaener \xc3\xa0 utiliser tes gags.\x7Chaque fois que tu atteins un Cog avec l'un de tes gags, ton exp\xc3\xa9rience augmente.\x7Quand tu auras assez d'exp\xc3\xa9rience, tu pourras utiliser un gag encore meilleur.\x7Va t'entra\xc3\xaener \xc3\xa0 utiliser tes gags en battant 4 Cogs."},
    166: {
        QUEST: "Bien jou\xc3\xa9 pour avoir battu ces Cogs.\x7Tu sais, les Cogs sont de quatre sortes diff\xc3\xa9rentes.\x7Il y a les Loibots, les Caissbots, les Vendibots et les Chefbots.\x7Tu peux les distinguer par leurs couleurs et leurs \xc3\xa9tiquettes.\x7Pour t'entra\xc3\xaener va battre 4 Chefbots."},
    167: {
        QUEST: "Bien jou\xc3\xa9 pour avoir battu ces Cogs.\x7Tu sais, les Cogs sont de quatre sortes diff\xc3\xa9rentes.\x7Il y a les Loibots, les Caissbots, les Vendibots et les Chefbots.\x7Tu peux les distinguer par leurs couleurs et leurs \xc3\xa9tiquettes.\x7Pour t'entra\xc3\xaener va battre 4 Loibots."},
    168: {
        QUEST: "Bien jou\xc3\xa9 pour avoir battu ces Cogs.\x7Tu sais, les Cogs sont de quatre sortes diff\xc3\xa9rentes.\x7Il y a les Loibots, les Caissbots, les Vendibots et les Chefbots.\x7Tu peux les distinguer par leurs couleurs et leurs \xc3\xa9tiquettes.\x7Pour t'entra\xc3\xaener va battre 4 Vendibots."},
    169: {
        QUEST: "Bien jou\xc3\xa9 pour avoir battu ces Cogs.\x7Tu sais, les Cogs sont de quatre sortes diff\xc3\xa9rentes.\x7Il y a les Loibots, les Caissbots, les Vendibots et les Chefbots.\x7Tu peux les distinguer par leurs couleurs et leurs \xc3\xa9tiquettes.\x7Pour t'entra\xc3\xaener va battre 4 Caissbots."},
    170: {
        QUEST: "Bon travail, maintenant tu connais la diff\xc3\xa9rence entre les 4 sortes de Cogs.\x7Je crois que tu peux commencer \xc3\xa0 t'entra\xc3\xaener pour ta troisi\xc3\xa8me s\xc3\xa9rie de gags.\x7Va parler \xc3\xa0_toNpcName_ pour choisir ta prochaine s\xc3\xa9rie de gags - il peut te donner des conseils avis\xc3\xa9s._where_"},
    171: {
        QUEST: "Bon travail, maintenant tu connais la diff\xc3\xa9rence entre les 4 sortes de Cogs.\x7Je crois que tu peux commencer \xc3\xa0 t'entra\xc3\xaener pour ta troisi\xc3\xa8me s\xc3\xa9rie de gags.\x7Va parler \xc3\xa0_toNpcName_ pour choisir ta prochaine s\xc3\xa9rie de gags - il peut te donner des conseils avis\xc3\xa9s._where_"},
    172: {
        QUEST: "Bon travail, maintenant tu connais la diff\xc3\xa9rence entre les 4 sortes de Cogs.\x7Je crois que tu peux commencer \xc3\xa0 t'entra\xc3\xaener pour ta troisi\xc3\xa8me s\xc3\xa9rie de gags.\x7Va parler \xc3\xa0_toNpcName_ pour choisir ta prochaine s\xc3\xa9rie de gags - elle peut te donner des conseils avis\xc3\xa9s._where_"},
    175: {
        GREETING: '',
        QUEST: "Est-ce que tu savais que tu as une maison Toon \xc3\xa0 toi?\x7Clarabelle la vache s'occupe d'un catalogue par t\xc3\xa9l\xc3\xa9phone ou tu peux commander des meubles pour d\xc3\xa9corer ta maison.\x7Tu peux aussi y acheter des mots de Chat rapide, des v\xc3\xaatements et d'autres choses amusantes!\x7Je vais dire \xc3\xa0 Clarabelle de t'envoyer ton premier catalogue maintenant.\x7Tu recevras un catalogue avec les nouveaux articles chaque semaine!\x7Rentre a la maison et appelle Clarabelle avec ton t\xc3\xa9l\xc3\xa9phone.",
        INCOMPLETE_PROGRESS: 'Rentre \xc3\xa0 la maison et appelle Clarabelle avec ton t\xc3\xa9l\xc3\xa9phone.',
        COMPLETE: "J'esp\xc3\xa8re que tu t'amuses en commandant des choses chez Clarabelle!\x7Je viens tout juste de red\xc3\xa9corer ma maison. Elle est toontastique!\x7Continue \xc3\xa0 relever les d\xc3\xa9fitoons pour avoir plus de r\xc3\xa9compenses!",
        LEAVING: QuestsDefaultLeaving},
    400: {
        GREETING: '',
        QUEST: "Le lancer et l'\xc3\xa9claboussure sont super, mais tu auras besoin de plus de gags pour battre les Cogs de plus haut niveau.\x7Lorsque tu fais \xc3\xa9quipe avec d'autres Toons contre les Cogs, vous pouvez combiner vos attaques pour faire encore plus de d\xc3\xa9g\xc3\xa2ts.\x7Essayez diff\xc3\xa9rentes combinaisons de gags pour voir ce qui marche le mieux.\x7Pour ta prochaine s\xc3\xa9rie, choisis entre tapage et toonique.\x7Tapage est particulier parce que lorsqu'il frappe, il endommage tous les Cogs.\x7Toonique te permet de soigner les autres Toons lors d'un combat.\x7Lorsque tu es pr\xc3\xaat(e) \xc3\xa0 te d\xc3\xa9cider, reviens ici faire ton choix.",
        INCOMPLETE_PROGRESS: 'D\xc3\xa9j\xc3\xa0 de retour ? OK, quel est ton choix?',
        INCOMPLETE_WRONG_NPC: 'Pense bien \xc3\xa0 ta d\xc3\xa9cision avant de choisir.',
        COMPLETE: "Bonne d\xc3\xa9cision. Maintenant tu dois t'entra\xc3\xaener avant de pouvoir utiliser ces gags.\x7Tu dois effectuer une s\xc3\xa9rie de d\xc3\xa9fitoons pour t'entra\xc3\xaener.\x7Chaque d\xc3\xa9fi te donnera une seule image de ton animation d'attaque avec les gags.\x7Lorsque tu auras les 15 images, tu pourras faire le dernier d\xc3\xa9fi d'entra\xc3\xaenement qui te permettra d'utiliser tes nouveaux gags.\x7Tu peux suivre tes progr\xc3\xa8s dans ton journal de bord.",
        LEAVING: QuestsDefaultLeaving},
    1039: {
        QUEST: 'Va voir _toNpcName_ si tu veux parcourir la ville plus facilement._where_'},
    1040: {
        QUEST: 'Va voir _toNpcName_ si tu veux parcourir la ville plus facilement._where_'},
    1041: {
        QUEST: "Salut! Qu'est-ce qui t'am\xc3\xa8ne ?\x7Tout le monde utilise son trou portable pour voyager dans Toontown.\x7Tu peux te t\xc3\xa9l\xc3\xa9porter vers tes contacts en utilisant la liste d'contacts, ou vers n'importe quel quartier en utilisant la carte du journal de bord.\x7Bien entendu, tu dois d'abord gagner le droit de le faire!\x7Disons que je peux activer ton acc\xc3\xa8s \xc3\xa0 Toontown centre par t\xc3\xa9l\xc3\xa9portation si tu aides un de mes contacts.\x7On dirait que les Cogs font du d\xc3\xa9sordre sur l'avenue des Fondus. Va voir _toNpcName_._where_"},
    1042: {
        QUEST: "Salut! Qu'est-ce qui t'am\xc3\xa8ne ?\x7Tout le monde utilise son trou portable pour voyager dans Toontown.\x7Tu peux te t\xc3\xa9l\xc3\xa9porter vers tes contacts en utilisant la liste d'contacts, ou vers n'importe quel quartier en utilisant la carte du journal de bord.\x7Bien entendu, tu dois d'abord gagner le droit de le faire!\x7Disons que je peux activer ton acc\xc3\xa8s \xc3\xa0 Toontown centre par t\xc3\xa9l\xc3\xa9portation si tu aides un de mes contacts.\x7On dirait que les Cogs font du d\xc3\xa9sordre sur l'avenue des Fondus. Va voir _toNpcName_._where_"},
    1043: {
        QUEST: "Salut! Qu'est-ce qui t'am\xc3\xa8ne ?\x7Tout le monde utilise son trou portable pour voyager dans Toontown.\x7Tu peux te t\xc3\xa9l\xc3\xa9porter vers tes contacts en utilisant la liste d'contacts, ou vers n'importe quel quartier en utilisant la carte du journal de bord.\x7Bien entendu, tu dois d'abord gagner le droit de le faire!\x7Disons que je peux activer ton acc\xc3\xa8s \xc3\xa0 Toontown centre par t\xc3\xa9l\xc3\xa9portation si tu aides un de mes contacts.\x7On dirait que les Cogs font du d\xc3\xa9sordre sur l'avenue des Fondus. Va voir _toNpcName_._where_"},
    1044: {
        QUEST: "Oh, merci de passer par ici. J'ai vraiment besoin d'aide.\x7Comme tu peux voir, je n'ai pas de clients.\x7Mon livre de recettes secret est perdu et personne ne vient plus dans mon restaurant.\x7La derni\xc3\xa8re fois que je l'ai vu, c'\xc3\xa9tait avant que ces Cogs ne prennent mon b\xc3\xa2timent.\x7Est-ce que tu peux m'aider \xc3\xa0 retrouver quatre de mes c\xc3\xa9l\xc3\xa8bres recettes?",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Est-ce que tu as pu retrouver mes recettes?'},
    1045: {
        QUEST: "Merci beaucoup!\x7D'ici peu, j'aurai retrouv\xc3\xa9 toutes mes recettes et je pourrai rouvrir mon restaurant.\x7Oh, j'ai une petite note ici pour toi - quelque chose \xc3\xa0 propos de l'acc\xc3\xa8s par t\xc3\xa9l\xc3\xa9portation ?\x7C'est \xc3\xa9crit, merci d'avoir aid\xc3\xa9 mon ami et d'avoir livr\xc3\xa9 ceci au quartier g\xc3\xa9n\xc3\xa9ral des Toons. \x7Eh bien, merci vraiment - au revoir!",
        LEAVING: '',
        COMPLETE: "Ah oui, c'est \xc3\xa9crit que tu as \xc3\xa9t\xc3\xa9 d'une grande aide \xc3\xa0 de braves gens de l'avenue des Fondus.\x7Et que tu as besoin d'un acc\xc3\xa8s par t\xc3\xa9l\xc3\xa9portation \xc3\xa0 Toontown centre.\x7Bon, c'est comme si c'\xc3\xa9tait fait.\x7Maintenant tu peux revenir au terrain de jeux par t\xc3\xa9l\xc3\xa9portation depuis presque partout dans Toontown.\x7Ouvre simplement ta carte et clique sur Toontown centre."},
    1046: {
        QUEST: "Les Caissbots ont vraiment ennuy\xc3\xa9 la Caisse d'\xc3\xa9pargne Dr\xc3\xb4le d'argent.\x7Va donc y faire un tour et vois si tu peux faire quelque chose._where_"},
    1047: {
        QUEST: "Les Caissbots se sont introduits dans la banque et ont vol\xc3\xa9 nos machines.\x7S'il te pla\xc3\xaet, reprends 5 machines \xc3\xa0 calculer aux Caissbots.\x7Pour t'\xc3\xa9viter de faire des allers et retours, rapporte-les toutes en une seule fois.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Tu cherches encore des machines \xc3\xa0 calculer ?'},
    1048: {
        QUEST: 'Oh l\xc3\xa0 l\xc3\xa0! >Merci d\'avoir trouv\xc3\xa9 nos machines \xc3\xa0 calculer.\x7Hmm... Elles ont l\'air un peu ab\xc3\xaem\xc3\xa9es.\x7Dis donc, pourrais-tu les amener \xc3\xa0 _toNpcName_ \xc3\xa0 son magasin, "Machines \xc3\xa0 chatouilles", dans cette rue ?\x7Voir si elle peut les r\xc3\xa9parer.',
        LEAVING: ''},
    1049: {
        QUEST: "Qu'est-ce que c'est ? Des machines \xc3\xa0 calculer cass\xc3\xa9es?\x7Des Caissbots dis-tu?\x7Bon, regardons \xc3\xa7a...\x7Mouais, les pignons sont cass\xc3\xa9s, mais je n'en vends pas...\x7Tu sais ce qui pourrait marcher - des pignons de Cog, des gros, de gros Cogs...\x7Des pignons de Cog de niveau 3 devraient faire l'affaire. J'en aurai besoin de 2 pour chaque machine, donc 10 au total.\x7Rapporte-les moi tous ensemble et je ferai la r\xc3\xa9paration!",
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Souviens-toi, j'ai besoin de 10 pignons pour r\xc3\xa9parer les machines."},
    1053: {
        QUEST: "Ah oui, \xc3\xa7a devrait bien faire l'affaire.\x7Tout est r\xc3\xa9par\xc3\xa9 maintenant, gratuitement.\x7Rapporte-les \xc3\xa0 Dr\xc3\xb4le d'argent, et dis-leur bonjour de ma part.",
        LEAVING: '',
        COMPLETE: "Toutes les machines \xc3\xa0 calculer sont r\xc3\xa9par\xc3\xa9es?\x7Joli travail. Je crois bien que j'ai quelque chose par l\xc3\xa0 pour te r\xc3\xa9compenser..."},
    1054: {
        QUEST: "_toNpcName_ a besoin d'aide pour ses voitures de clown._where_"},
    1055: {
        QUEST: "Bon sang! Je n'arrive pas \xc3\xa0 trouver les pneus de cette voiture de clown!\x7Tu crois que tu pourrais m'aider ?\x7Je crois que Bob Fondu les a lanc\xc3\xa9s dans la mare du terrain de jeux de Toontown centre.\x7Si tu vas sur les pontons, de l\xc3\xa0 tu peux essayer de rep\xc3\xaacher les pneus.",
        GREETING: 'Youhouu!',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Tu as du mal \xc3\xa0 rep\xc3\xaacher les 4 pneus?'},
    1056: {
        QUEST: "Fanta-super-tastique! Maintenant je vais pouvoir remettre en marche cette vieille voiture de clown!\x7H\xc3\xa9, je croyais que j'avais une pompe par ici pour gonfler ces pneus...\x7C'est peut-\xc3\xaatre _toNpcName_ qui l'a emprunt\xc3\xa9e ?\x7Tu peux aller lui demander de me la rendre ?_where_",
        LEAVING: ''},
    1057: {
        QUEST: 'Salut!\x7Une pompe \xc3\xa0 pneus tu dis?\x7Je vais te dire - tu me nettoies les rues de quelques-uns de ces Cogs de haut niveau...\x7Et je te donne la pompe \xc3\xa0 pneus.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "C'est tout ce que tu peux faire ?"},
    1058: {
        QUEST: 'Bon travail - je savais que tu pouvais le faire.\x7Voil\xc3\xa0 la pompe. Je suis certain que_toNpcName_ sera content de la r\xc3\xa9cup\xc3\xa9rer.',
        LEAVING: '',
        GREETING: '',
        COMPLETE: "Youpiii! Maintenant \xc3\xa7a va marcher!\x7Et dis donc, merci de m'avoir aid\xc3\xa9.\x7Tiens, prends \xc3\xa7a."},
    1059: {
        QUEST: '_toNpcName_ est \xc3\xa0 court de fournitures. Tu peux peut-\xc3\xaatre lui donner un coup de main ?_where_'},
    1060: {
        QUEST: "Merci d'\xc3\xaatre pass\xc3\xa9 par ici!\x7Ces Cogs ont vol\xc3\xa9 mon encre je n'en ai presque plus.\x7 Pourrais-tu me p\xc3\xaacher de l'encre de seiche dans la mare ?\x7Tu n'as qu'\xc3\xa0 rester sur un ponton pr\xc3\xa8s de la mare pour p\xc3\xaacher.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: '{Tu as des probl\xc3\xa8mes pour p\xc3\xaacher ?'},
    1061: {
        QUEST: "Super - merci pour l'encre!\x7Tu sais quoi, et si tu nous d\xc3\xa9barrassais de quelques Gratte-papiers...\x7Je ne serais plus en panne d'encre aussi rapidement.\x7Tu dois vaincre 6 Gratte-papiers dans Toontown centre pour avoir ta r\xc3\xa9compense.",
        LEAVING: '',
        COMPLETE: 'Merci! Laisse-moi te r\xc3\xa9compenser pour ton aide.',
        INCOMPLETE_PROGRESS: "Je viens de voir encore d'autres Gratte-papiers."},
    1062: {
        QUEST: "Super - merci pour l'encre!\x7Tu sais quoi, et si tu nous d\xc3\xa9barrassais de quelques Pique-au-sang...\x7Je ne serais plus en panne d'encre aussi rapidement.\x7Tu dois vaincre 6 Pique-au-sang dans Toontown centre pour avoir ta r\xc3\xa9compense.",
        LEAVING: '',
        COMPLETE: 'Merci! Laisse-moi te r\xc3\xa9compenser pour ton aide.',
        INCOMPLETE_PROGRESS: "Je viens de voir encore d'autres Pique-au-sang."},
    900: {
        QUEST: "Je crois comprendre que_toNpcName_ a besoin d'aide avec un paquet._where_"},
    1063: {
        QUEST: "Salut, merci d'\xc3\xaatre l\xc3\xa0.\x7Un Cog a vol\xc3\xa9 un paquet tr\xc3\xa8s important juste sous mon nez.\x7Peux-tu le r\xc3\xa9cup\xc3\xa9rer ? Je crois que c'\xc3\xa9tait un Cog de niveau 3...\x7Donc, tu dois vaincre des Cogs de niveau 3 jusqu'\xc3\xa0 ce que tu retrouves mon paquet.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Tu n'as pas retrouv\xc3\xa9 le paquet, hein ?"},
    1067: {
        QUEST: "C'est \xc3\xa7a, tr\xc3\xa8s bien!\x7Oh, l'adresse est toute tach\xc3\xa9e...\x7Tout ce que j'arrive \xc3\xa0 lire, c'est Docteur... - le reste est brouill\xc3\xa9.\x7C'est peut-\xc3\xaatre pour_toNpcName_? Peux-tu lui porter ?_where_",
        LEAVING: ''},
    1068: {
        QUEST: "Je n'attendais pas de paquet. C'est peut-\xc3\xaatre pour le Dr E. Phorique ?\x7Mon assistant doit aller le voir aujourd'hui, je me charge de lui remettre.\x7En attendant, est-ce que tu voudrais bien d\xc3\xa9barrasser ma rue de quelques Cogs?\x7Tu dois vaincre 10 Cogs dans Toontown centre.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Mon assistant n'est pas encore revenu."},
    1069: {
        QUEST: "Le Dr. E. Phorique dit qu'il n'attendait pas de paquet non plus.\x7Malheureusement, un Caissbot l'a vol\xc3\xa9 \xc3\xa0 mon assistant alors qu'il revenait.\x7Pourrais-tu essayer de le r\xc3\xa9cup\xc3\xa9rer ?",
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Tu n'as pas retrouv\xc3\xa9 le paquet, hein ?"},
    1070: {
        QUEST: "Le Dr. E. Phorique dit qu'il n'attendait pas de paquet non plus.\x7Malheureusement, un Vendibot l'a vol\xc3\xa9 \xc3\xa0 mon assistant alors qu'il revenait.\x7Je suis d\xc3\xa9sol\xc3\xa9, mais il va falloir que tu retrouves ce Vendibot pour le r\xc3\xa9cup\xc3\xa9rer.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Tu n'as pas retrouv\xc3\xa9 le paquet, hein ?"},
    1071: {
        QUEST: "Le Dr. E. Phorique dit qu'il n'attendait pas de paquet non plus.\x7Malheureusement, un Chefbot l'a vol\xc3\xa9 \xc3\xa0 mon assistant alors qu'il revenait.\x7Pourrais-tu essayer de le r\xc3\xa9cup\xc3\xa9rer ?",
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Tu n'as pas retrouv\xc3\xa9 le paquet, hein ?"},
    1072: {
        QUEST: "Super - tu l'as retrouv\xc3\xa9!\x7Tu devrais peut-\xc3\xaatre essayer _toNpcName_, cela pourrait \xc3\xaatre pour lui._where_",
        LEAVING: ''},
    1073: {
        QUEST: "Oh, merci de m'avoir apport\xc3\xa9 mes paquets.\x7Juste une seconde, j'en attendais deux. Pourrais-tu v\xc3\xa9rifier avec _toNpcName_ voir s'il a l'autre ?",
        INCOMPLETE: 'Est-ce que tu as trouv\xc3\xa9 mon autre paquet ?',
        LEAVING: ''},
    1074: {
        QUEST: "Il a dit qu'il y avait un autre paquet ? Les Cogs l'ont peut-\xc3\xaatre aussi vol\xc3\xa9.\x7Tu dois vaincre des Cogs jusqu'\xc3\xa0 ce que tu trouves le second paquet.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Tu n'as pas retrouv\xc3\xa9 le paquet, hein ?"},
    1075: {
        QUEST: "Finalement je crois qu'il y avait un second paquet!\x7Va vite le porter \xc3\xa0 _toNpcName_ avec mes excuses.",
        COMPLETE: 'Eh, mon paquet est l\xc3\xa0!\x7Puisque tu es un Toon aussi serviable, cela devrait aider.',
        LEAVING: ''},
    1076: {
        QUEST: "Il y a un probl\xc3\xa8me au Ornithorynques 14 carats.\x7_toNpcName_ serait sans doute content d'avoir de l'aide._where_"},
    1077: {
        QUEST: "Merci d'\xc3\xaatre venu - les Cogs ont vol\xc3\xa9 tous mes poissons dor\xc3\xa9s.\x7Je crois que les Cogs veulent les vendre pour se faire de l'argent facilement.\x7Ces 5 poissons ont \xc3\xa9t\xc3\xa9 mes seuls compagnons dans cette petite boutique depuis tant d'ann\xc3\xa9es...\x7Si tu pouvais me les retrouver, je t'en serais vraiment reconnaissant.\x7Je suis certain qu'un des Cogs a mes poissons.\x7Tu dois vaincre des Cogs jusqu'\xc3\xa0 ce que tu trouves mes poissons dor\xc3\xa9s.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: "S'il te pla\xc3\xaet, ram\xc3\xa8ne-moi mes poissons."},
    1078: {
        QUEST: "Oh, tu as mes poissons!\x7Eh? Qu'est-ce que c'est que \xc3\xa7a?\x7Aah, ce sont bien les Cogs, apr\xc3\xa8s tout.\x7Je ne comprends rien \xc3\xa0 ce re\xc3\xa7u. Peux-tu l'emmener \xc3\xa0 _toNpcName_ voir s'il peut le lire ?_where_",
        INCOMPLETE: "Qu'est-ce que _toNpcName_ a dit \xc3\xa0 propos du re\xc3\xa7u?",
        LEAVING: ''},
    1079: {
        QUEST: "Mmm, laisse-moi voir ce re\xc3\xa7u.\x7...Ah oui, il dit qu'un poisson dor\xc3\xa9 a \xc3\xa9t\xc3\xa9 vendu \xc3\xa0 un Laquaistic.\x7\xc3\x87a n'a pas l'air de dire ce qui est arriv\xc3\xa9 aux 4 autres poissons.\x7Tu devrais peut-\xc3\xaatre essayer de trouver ce Laquaistic.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Je ne crois pas que je puisse t'aider \xc3\xa0 grand-chose d'autre.\x7Pourquoi n'essaies-tu pas de trouver ce poisson dor\xc3\xa9?"},
    1092: {
        QUEST: "Mmm, laisse-moi voir ce re\xc3\xa7u.\x7...Ah oui, il dit qu'un poisson dor\xc3\xa9 a \xc3\xa9t\xc3\xa9 vendu \xc3\xa0 un Gardoseille.\x7\xc3\x87a n'a pas l'air de dire ce qui est arriv\xc3\xa9 aux 4 autres poissons.\x7Tu devrais peut-\xc3\xaatre essayer de trouver ce Gardoseille.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Je ne crois pas que je puisse t'aider \xc3\xa0 grand-chose d'autre.\x7Pourquoi n'essaies-tu pas de trouver ce poisson dor\xc3\xa9?"},
    1080: {
        QUEST: "Oh, Dieu merci! Tu as trouv\xc3\xa9 Oscar - c'est mon pr\xc3\xa9f\xc3\xa9r\xc3\xa9.\x7Qu'est-ce que c'est, Oscar ? Hein, hein...ils ont quoi? ... Ils sont ?\x7Oscar dit que les 4 autres se sont \xc3\xa9chapp\xc3\xa9s dans la mare du terrain de jeux.\x7Peux-tu aller me les chercher ?\x7Tu n'as qu'\xc3\xa0 les p\xc3\xaacher dans la mare.",
        LEAVING: '',
        COMPLETE: 'Ahh, je suis si content! Avoir retrouv\xc3\xa9 mes petits camarades!\x7Tu m\xc3\xa9rites une belle r\xc3\xa9compense pour cela!',
        INCOMPLETE_PROGRESS: 'Tu as des probl\xc3\xa8mes pour trouver ces poissons?'},
    1081: {
        QUEST: "_toNpcName_ a l'air d'\xc3\xaatre dans une situation difficile. Elle serait s\xc3\xbbrement contente d'avoir de l'aide._where_"},
    1082: {
        QUEST: "J'ai renvers\xc3\xa9 de la colle \xc3\xa0 s\xc3\xa9chage rapide, et je suis coll\xc3\xa9e - compl\xc3\xa8tement coll\xc3\xa9e!\x7Si seuleument je trouvais une fa\xc3\xa7on de m'en sortir...\x7Cela me donne une id\xc3\xa9e, si tu veux bien.\x7Va vaincre quelques Vendibots et ram\xc3\xa8ne-moi de l'huile.",
        LEAVING: '',
        GREETING: '',
        INCOMPLETE_PROGRESS: "Peux-tu m'aider \xc3\xa0 me d\xc3\xa9coller ?"},
    1083: {
        QUEST: "Bon, l'huile a fait un peu d'effet, mais je ne peux toujours pas bouger.\x7Qu'est-ce qui pourrait bien m'aider ? C'est difficile \xc3\xa0 dire.\x7Cela me donne une id\xc3\xa9e on peut au moins essayer.\x7Va vaincre quelques Loibots et ram\xc3\xa8ne-moi de la graisse.",
        LEAVING: '',
        GREETING: '',
        INCOMPLETE_PROGRESS: "Peux-tu m'aider \xc3\xa0 me d\xc3\xa9coller ?"},
    1084: {
        QUEST: "Non, \xc3\xa7a n'a rien fait. Ce n'est vraiment pas dr\xc3\xb4le.\x7J'ai pourtant mis de la graisse partout.\x7\xc3\x87a me donne une id\xc3\xa9e, avant que j'oublie.\x7Va vaincre quelques Caissbots et rapporte de l'eau pour l'humecter.",
        LEAVING: '',
        GREETING: '',
        COMPLETE: 'Hourrah, je suis lib\xc3\xa9r\xc3\xa9e de cette colle rapide.\x7Comme r\xc3\xa9compense, je te donne ce cadeau.\x7Tu peux rire un peu plus longtemps lorsque tu es en train de te battre, et puis...\x7Oh, non! Je suis de nouveau coll\xc3\xa9e l\xc3\xa0!',
        INCOMPLETE_PROGRESS: "Peux-tu m'aider \xc3\xa0 me d\xc3\xa9coller ?"},
    1085: {
        QUEST: "_toNpcName_ est en train de faire des recherches sur les Cogs.\x7Va lui parler si tu veux l'aider._where_"},
    1086: {
        QUEST: "C'est cela, je fais une \xc3\xa9tude sur les Cogs.\x7Je veux savoir ce qui les fait tiquer.\x7Cela m'aiderait certainement si tu pouvais me trouver des pignons de Cogs.\x7Assure-toi qu'il s'agit de Cogs de niveau 2 au minimum, qu'ils soient assez gros pour \xc3\xaatre examin\xc3\xa9s.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Tu ne peux pas trouver assez de pignons?'},
    1089: {
        QUEST: "OK, regardons un peu \xc3\xa7a. Ce sont d'excellents sp\xc3\xa9cimens!\x7Mmmm...\x7OK, voil\xc3\xa0 mon rapport. Emm\xc3\xa8ne-le tout de suite au quartier g\xc3\xa9n\xc3\xa9ral des Toons.",
        INCOMPLETE: 'As-tu port\xc3\xa9 mon rapport au quartier g\xc3\xa9n\xc3\xa9ral?',
        COMPLETE: "Bon travail _avName_, on va s'occuper de \xc3\xa7a.",
        LEAVING: ''},
    1090: {
        QUEST: '_toNpcName_ a des informations importantes pour toi._where_'},
    1091: {
        QUEST: "J'ai entendu dire que le quartier g\xc3\xa9n\xc3\xa9ral des Toons travaille sur une sorte de d\xc3\xa9tecteur de Cogs.\x7Il te permettra de voir o\xc3\xb9 sont les Cogs afin de les rep\xc3\xa9rer plus facilement.\x7La page des Cogs dans ton journal de bord en est la cl\xc3\xa9.\x7En battant assez de Cogs, tu pourras te r\xc3\xa9gler sur leurs signaux et d\xc3\xa9tecter leur emplacement.\x7Continue \xc3\xa0 vaincre des Cogs, afin d'\xc3\xaatre pr\xc3\xaat.",
        COMPLETE: 'Bon travail! Tu pourras probablement utiliser ceci...',
        LEAVING: ''},
    401: {
        GREETING: '',
        QUEST: 'Tu peux maintenant choisir la prochaine s\xc3\xa9rie de gags que tu veux apprendre.\x7Prends ton temps pour te d\xc3\xa9cider, et reviens quand tu auras choisi.',
        INCOMPLETE_PROGRESS: 'Pense bien \xc3\xa0 ta d\xc3\xa9cision avant de choisir.',
        INCOMPLETE_WRONG_NPC: 'Pense bien \xc3\xa0 ta d\xc3\xa9cision avant de choisir.',
        COMPLETE: 'Une sage d\xc3\xa9cision...',
        LEAVING: QuestsDefaultLeaving},
    2201: {
        QUEST: 'Ces faux-jetons de Cogs font encore des leurs.\x7_toNpcName_ vient de signaler un autre objet disparu. Va voir si tu peux r\xc3\xa9gler cela._where_'},
    2202: {
        QUEST: "Salut, _avName_. Dieu merci, tu es l\xc3\xa0. Un Radino \xc3\xa0 l'air m\xc3\xa9chant \xc3\xa9tait l\xc3\xa0 \xc3\xa0 l'instant et il est parti avec une chambre \xc3\xa0 air.\x7Je crains qu'ils ne l'utilisent pour leurs sombres desseins.\x7S'il te pla\xc3\xaet, essaie de le retrouver et ram\xc3\xa8ne-la moi.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Est-ce que tu as retrouv\xc3\xa9 ma chambre \xc3\xa0 air ?',
        COMPLETE: 'Tu as trouv\xc3\xa9 ma chambre \xc3\xa0 air! Tu es vraiment tr\xc3\xa8s dou\xc3\xa9. Tiens, prends ta r\xc3\xa9compense...'},
    2203: {
        QUEST: 'Les Cogs sont en train de mettre la banque sens dessus dessous.\x7Va voir le Capitaine Carl et vois ce que tu peux faire._where_'},
    2204: {
        QUEST: "Bienvenue \xc3\xa0 bord, moussaillon.\x7Grrr! Ces fripons de Cogs ont cass\xc3\xa9 mon monocle et je n'arrive plus \xc3\xa0 compter la monnaie sans lui.\x7Garde les pieds sur terre et porte cette ordonnance au Dr. Queequeg puis rapporte m'en un nouveau._where_",
        GREETING: '',
        LEAVING: ''},
    2205: {
        QUEST: "Qu'est-ce que c'est ?\x7Oh, je voudrais bien pr\xc3\xa9parer cette ordonnance mais les Cogs ont chapard\xc3\xa9 mes r\xc3\xa9serves.\x7Si tu peux reprendre la monture \xc3\xa0 un Laquaistic je pourrai probablement t'aider.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'D\xc3\xa9sol\xc3\xa9. Pas de monture du Laquaistic, pas de monocle.'},
    2206: {
        QUEST: 'Excellent!\x7Une seconde...\x7Ton ordonnance est pr\xc3\xaate. Emm\xc3\xa8ne tout de suite ce monocle au Capitaine Carl._where_',
        GREETING: '',
        LEAVING: '',
        COMPLETE: 'Hisse et ho!\x7Tu vas finir par gagner du galon apr\xc3\xa8s tout.\x7Et voil\xc3\xa0.'},
    2207: {
        QUEST: 'Barbara Bernache a un Cog dans son magasin!\x7Il vaudrait mieux que tu y ailles tout de suite._where_'},
    2208: {
        QUEST: '\xc3\x87a alors! Tu viens de le rater, mon chou.\x7Il y avait un Frappedos ici. Il a pris ma grande perruque blanche.\x7Il a dit que c\'\xc3\xa9tait pour son chef et quelque chose \xc3\xa0 propos de "jurisprudence".\x7Si tu pouvais me la rapporter, je t\'en serais toujours reconnaissante.',
        LEAVING: '',
        GREETING: '',
        INCOMPLETE_PROGRESS: "Tu ne l'as toujours pas trouv\xc3\xa9?\x7Il est grand avec une t\xc3\xaate pointue.",
        COMPLETE: "Tu l'as trouv\xc3\xa9!?!?\x7Tu es vraiment un ange!\x7Tu as bien m\xc3\xa9rit\xc3\xa9 ceci..."},
    2209: {
        QUEST: "Ginette se pr\xc3\xa9pare pour un voyage important.\x7Va y faire un tour et vois ce que tu peux faire pour l'aider._where_"},
    2210: {
        QUEST: "Tu peux m'aider.\x7Le quartier g\xc3\xa9n\xc3\xa9ral des Toons m'a demand\xc3\xa9 de faire un voyage pour voir si je peux trouver d'o\xc3\xb9 viennent les Cogs.\x7J'aurais besoin de quelques affaires pour mon bateau mais je n'ai pas beaucoup de bonbons.\x7Va et ram\xc3\xa8ne-moi du lest de chez Ernest. Il faudra que tu lui rendes un service pour l'avoir._where_",
        GREETING: 'Salut, _avName_',
        LEAVING: ''},
    2211: {
        QUEST: "Comme \xc3\xa7a, Ginette veut du lest, n'est-ce pas?\x7Elle me doit encore de l'argent pour le dernier boisseau.\x7Je te le donnerai si tu peux faire partir cinq Microchefs de ma rue.",
        INCOMPLETE_PROGRESS: "Non, idiot! J'ai dit CINQ Microchefs...",
        GREETING: 'Que puis-je faire pour toi?',
        LEAVING: ''},
    2212: {
        QUEST: 'Un march\xc3\xa9 est un march\xc3\xa9.\x7Voil\xc3\xa0 ton lest pour cette pingre de Ginette._where_',
        GREETING: 'Eh bien, regarde ce qui arrive l\xc3\xa0...',
        LEAVING: ''},
    2213: {
        QUEST: "Excellent travail. Je savais qu'il serait raisonnable.\x7Ensuite il me faudra une carte marine de chez Art.\x7Je ne crois pas avoir beaucoup de cr\xc3\xa9dit l\xc3\xa0-bas non plus il faudra que tu t'arranges avec lui._where_",
        GREETING: '',
        LEAVING: ''},
    2214: {
        QUEST: "Oui, j'ai la carte marine que veut Ginette.\x7Et tu l'auras en \xc3\xa9change d'un petit travail.aJ'essaie de construire un astrolabe pour naviguer dans les \xc3\xa9toiles.aJ'aurais besoin de trois pignons de Cog pour le construire.\x7Reviens quand tu les auras trouv\xc3\xa9s.",
        INCOMPLETE_PROGRESS: 'Alors ils arrivent ces pignons de Cogs?',
        GREETING: 'Bienvenue!',
        LEAVING: 'Bonne chance!'},
    2215: {
        QUEST: "Ooh! Ces pignons feront tr\xc3\xa8s bien l'affaire.\x7Voil\xc3\xa0 la carte. Donne-la \xc3\xa0 Ginette avec mes compliments._where_",
        GREETING: '',
        LEAVING: '',
        COMPLETE: "Bon, on y est presque. Je suis pr\xc3\xaate \xc3\xa0 prendre la mer!\x7Je t'emm\xc3\xa8nerais avec moi si tu n'avais pas un teint si vert. Prends plut\xc3\xb4t ceci."},
    901: {
        QUEST: "Si tu es d'accord, Ahab a besoin d'aide, chez lui..._where_"},
    2902: {
        QUEST: "Tu es la nouvelle recrue ?\x7Bien, bien. Tu peux peut-\xc3\xaatre m'aider.\x7Je suis en train de construire un crabe g\xc3\xa9ant pr\xc3\xa9fabriqu\xc3\xa9 pour d\xc3\xa9router les Cogs.\x7Je pourrais quand m\xc3\xaame utiliser une manille. Va voir G\xc3\xa9rard et rapportes-en une, s'il te pla\xc3\xaet._where_"},
    2903: {
        QUEST: "Salut!\x7Oui, j'ai entendu parler du crabe g\xc3\xa9ant qu'Ahab est en train de fabriquer.\x7La meilleure manille que j'aie est un peu sale quand m\xc3\xaame.\x7Sois sympa, passe chez un blanchisseur avant de la d\xc3\xa9poser._where_",
        LEAVING: 'Merci!'},
    2904: {
        QUEST: 'Tu dois \xc3\xaatre la personne que G\xc3\xa9rard a envoy\xc3\xa9e.\x7Je crois que je peux faire \xc3\xa7a assez vite.\x7Juste une minute...\x7Et voil\xc3\xa0. Comme neuf!\x7Tu salueras Ahab de ma part._where_'},
    2905: {
        QUEST: "Ah, c'est exactement ce que je cherchais.\x7Pendant que tu es l\xc3\xa0, je vais aussi avoir besoin d'un tr\xc3\xa8s gros ressort d'horloge.\x7Va donc chez Crochet voir s'il en a un._where_"},
    2906: {
        QUEST: "Un gros ressort, hein ?\x7Je suis d\xc3\xa9sol\xc3\xa9 mais le plus gros ressort que j'aie est quand m\xc3\xaame plut\xc3\xb4t petit.\x7Je pourrais peut-\xc3\xaatre en fabriquer un avec des ressorts de g\xc3\xa2chette de pistolet \xc3\xa9clabousseur.\x7Apporte-moi trois de ces gags et je vais voir ce que je peux faire."},
    2907: {
        QUEST: 'Regardons \xc3\xa7a...\x7G\xc3\xa9nial. Vraiment g\xc3\xa9nial.\x7Quelquefois je me surprends moi-m\xc3\xaame.\x7Et voil\xc3\xa0 : un gros ressort pour Ahab!_where_',
        LEAVING: 'Bonne route!'},
    2911: {
        QUEST: 'Je serais tr\xc3\xa8s content de pouvoir aider, _avName_.\x7Malheureusement, les rues ne sont plus s\xc3\xbbres.\x7Va donc \xc3\xa9liminer quelques Cogs Caissbots et on pourra parler.',
        INCOMPLETE_PROGRESS: 'Je crois que tu peux rendre les rues encore plus s\xc3\xbbres.'},
    2916: {
        QUEST: "Oui, j'ai un contrepoids que je pourrais donner \xc3\xa0 Ahab.\x7Je crois que ce serait plus s\xc3\xbbr si tu pouvais vaincre deux Vendibots d'abord.",
        INCOMPLETE_PROGRESS: 'Pas encore. Tu dois vaincre plus de Vendibots.'},
    2921: {
        QUEST: "Hmmm, je pensais que je pourrais me d\xc3\xa9barrasser d'un poids.\x7Je me sentirais bien mieux s'il n'y avait pas autant de Cogs Chefbots \xc3\xa0 r\xc3\xb4der par ici.\x7Va donc en vaincre six et reviens me voir.",
        INCOMPLETE_PROGRESS: "Je crois qu'on n'est toujours pas en s\xc3\xa9curit\xc3\xa9..."},
    2925: {
        QUEST: "\xc3\x87a y est ?\x7Bon, je suppose qu'on est suffisamment en s\xc3\xa9curit\xc3\xa9 maintenant.\x7Voil\xc3\xa0 le contrepoids pour Ahab._where_"},
    2926: {
        QUEST: "Bon, c'est tout.\x7Voyons si \xc3\xa7a marche.\x7Hmmm, il y a un petit probl\xc3\xa8me.\x7Je n'ai plus de courant parce que ce b\xc3\xa2timent Cog bloque mon capteur solaire.\x7Peux-tu le reprendre pour moi?",
        INCOMPLETE_PROGRESS: 'Toujours pas de courant. O\xc3\xb9 en es-tu avec ce b\xc3\xa2timent ?',
        COMPLETE: 'Super! Tu es une sacr\xc3\xa9e terreur pour les Cogs! Tiens, prends ta r\xc3\xa9compense...'},
    3200: {
        QUEST: "Je viens d'avoir un appel de _toNpcName_.\x7Ce n'est pas son jour. Tu pourrais peut-\xc3\xaatre l'aider.!\x7Va y faire un tour et vois ce dont il a besoin._where_"},
    3201: {
        QUEST: "Oh, merci d'\xc3\xaatre l\xc3\xa0!\x7J'ai besoin de quelqu'un pour emporter cette nouvelle cravate en soie \xc3\xa0 _toNpcName_.\x7Est-ce que tu peux faire \xc3\xa7a pour moi?_where_"},
    3203: {
        QUEST: "Oh, \xc3\xa7a doit \xc3\xaatre la cravate que j'ai command\xc3\xa9e! Merci!\x7Elle va avec un costume \xc3\xa0 rayures que je viens de finir, juste l\xc3\xa0.\x7H\xc3\xa9, qu'est ce qui est arriv\xc3\xa9 \xc3\xa0 ce costume ?\x7Oh non! Les Cogs ont d\xc3\xbb voler mon nouveau costume!\x7Tu dois vaincre des Cogs jusqu'\xc3\xa0 ce que tu trouves mon costume, et que tu me le rapportes.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Tu n'as pas encore trouv\xc3\xa9 mon costume ? Je suis certain que les Cogs l'ont pris!",
        COMPLETE: "Youpii! Tu as trouv\xc3\xa9 mon nouveau costume!\x7Tu vois, je t'avais dit que les Cogs l'avaient! Voil\xc3\xa0 ta r\xc3\xa9compense..."},
    3204: {
        QUEST: "_toNpcName_ vient d'appeler pour signaler un vol.\x7Pourquoi n'irais-tu pas voir si tu peux arranger l'affaire ?_where_"},
    3205: {
        QUEST: "Bonjour, _avName_! Tu es l\xc3\xa0 pour m'aider ?\x7Je viens de chasser un Pique-au-sang de mon magasin. Houlala! C'\xc3\xa9tait effrayant.\x7Mais maintenant je ne trouve plus mes ciseaux! Je suis certain que ce Pique-au-sang les a pris.\x7Trouve-le, et ram\xc3\xa8ne-moi mes ciseaux.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Tu cherches encore mes ciseaux?',
        COMPLETE: 'Mes ciseaux! Merci beaucoup! Voil\xc3\xa0 ta r\xc3\xa9compense...'},
    3206: {
        QUEST: "On dirait que _toNpcName_ a des probl\xc3\xa8mes avec des Cogs.\x7Va voir si tu peux l'aider._where_"},
    3207: {
        QUEST: "Oh\xc3\xa9, _avName_! Merci d'\xc3\xaatre venu!\x7Une bande de Charabieurs est arriv\xc3\xa9e et a vol\xc3\xa9 une pile de cartes postales sur mon comptoir.\x7S'il te pla\xc3\xaet, sors vaincre tous ces Charabieurs et rapporte-moi mes cartes postales!",
        INCOMPLETE_PROGRESS: "Il n'y a pas assez de cartes postales! Continue de chercher!",
        COMPLETE: 'Oh, merci! Maintenant je vais pouvoir livrer le courrier \xc3\xa0 temps! Voil\xc3\xa0 ta r\xc3\xa9compense...'},
    3208: {
        QUEST: 'Nous avons eu des plaintes des r\xc3\xa9sidents r\xc3\xa9cemment \xc3\xa0 propos des Cassepieds.\x7Essaie de vaincre 10 Cassepieds pour aider tes camarades Toons du Jardin de Daisy.'},
    3209: {
        QUEST: "Merci d'avoir battu ces Cassepieds!\x7Mais maintenant ce sont les T\xc3\xa9l\xc3\xa9vendeurs qui sont incontr\xc3\xb4lables.\x7Va vaincre 10 T\xc3\xa9l\xc3\xa9vendeurs au Jardin de Daisy et reviens ici pour ta r\xc3\xa9compense."},
    3247: {
        QUEST: 'Nous avons eu des plaintes des r\xc3\xa9sidents r\xc3\xa9cemment \xc3\xa0 propos des Pique-au-sang.\x7Essaie de vaincre 20 Pique-au-sang pour aider tes camarades Toons du Jardin de Daisy.'},
    3210: {
        QUEST: "Oh non, la Fleur qui mouille, rue des \xc3\x89rables, n'a plus de fleurs!\x7Emm\xc3\xa8ne-leur dix de tes fleurs \xc3\xa0 \xc3\xa9clabousser pour les aider.\x7V\xc3\xa9rifie que tu as bien 10 fleurs \xc3\xa0 \xc3\xa9clabousser dans ton inventaire d'abord.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: "J'ai besoin de 10 fleurs \xc3\xa0 \xc3\xa9clabousser. Tu n'en as pas assez!"},
    3211: {
        QUEST: "Oh, merci beaucoup! Ces fleurs \xc3\xa0 \xc3\xa9clabousser vont nous tirer d'embarras.\x7Mais j'ai peur des Cogs qui sont dehors.\x7Peux-tu m'aider et vaincre quelques-uns de ces Cogs?\x7Reviens me voir apr\xc3\xa8s avoir vaincu 20 Cogs dans cette rue.",
        INCOMPLETE_PROGRESS: 'Il reste encore des Cogs \xc3\xa0 vaincre par ici! Continue!',
        COMPLETE: "Oh, merci! Cela m'aide beaucoup. Ta r\xc3\xa9compense est..."},
    3212: {
        QUEST: "_toNpcName_ a besoin d'aide pour chercher quelque chose qu'elle a perdu.\x7Va la voir et vois ce que tu peux faire._where_"},
    3213: {
        QUEST: "Salut, _avName_. Peux-tu m'aider ?\x7Je crois que j'ai \xc3\xa9gar\xc3\xa9 mon stylo. Je pense que les Cogs l'ont peut-\xc3\xaatre pris.\x7Va vaincre des Cogs pour retrouver le stylo qu'ils m'ont vol\xc3\xa9.",
        INCOMPLETE_PROGRESS: "Tu n'as pas encore trouv\xc3\xa9 mon stylo?"},
    3214: {
        QUEST: "Oui, c'est mon stylo! Merci beaucoup!\x7Mais apr\xc3\xa8s ton d\xc3\xa9part, j'ai r\xc3\xa9alis\xc3\xa9 que mon encrier manquait aussi.\x7Va vaincre des Cogs pour retrouver mon encrier.",
        INCOMPLETE_PROGRESS: 'Je cherche encore mon encrier!'},
    3215: {
        QUEST: "Super! Maintenant j'ai retrouv\xc3\xa9 mon stylo et mon encrier!\x7Mais tu ne devineras jamais!\x7Mon bloc-notes a disparu! Ils ont d\xc3\xbb le voler aussi!\x7Va vaincre des Cogs pour retrouver mon bloc-notes vol\xc3\xa9, puis reviens pour ta r\xc3\xa9compense.",
        INCOMPLETE_PROGRESS: 'Tu as des nouvelles de mon bloc-notes?'},
    3216: {
        QUEST: "C'est mon bloc-notes! Youpii! Ta r\xc3\xa9compense est...\x7H\xc3\xa9! Mais o\xc3\xb9 est-elle ?\x7J'avais ta r\xc3\xa9compense l\xc3\xa0, dans le coffre de mon bureau. Mais le coffre entier a disparu!\x7Incroyable! Ces Cogs ont vol\xc3\xa9 ta r\xc3\xa9compense!\x7Va vaincre des Cogs pour retrouver mon coffre.\x7Quand tu me le ram\xc3\xa8neras, je te donnerai ta r\xc3\xa9compense.",
        INCOMPLETE_PROGRESS: 'Continue de chercher ce coffre! Ta r\xc3\xa9compense est dedans!',
        COMPLETE: "Enfin! J'avais ton nouveau sac \xc3\xa0 gags dans ce coffre. Le voil\xc3\xa0..."},
    3217: {
        QUEST: 'Nous avons fait quelques \xc3\xa9tudes sur les m\xc3\xa9canismes des Vendibots.\x7Nous devons encore \xc3\xa9tudier certaines pi\xc3\xa8ces de plus pr\xc3\xa8s.\x7Apporte-nous un pignon de Cafteur.\x7Tu peux en attraper un quand le Cog explose.'},
    3218: {
        QUEST: "Bon travail! Maintenant, nous avons besoin d'un pignon de Passetout pour faire la comparaison.\x7Ces pignons sont plus difficiles \xc3\xa0 attraper, ne te d\xc3\xa9courage pas."},
    3219: {
        QUEST: "Super! Maintenant on n'a plus besoin que d'un pignon en plus.\x7Cette fois, il nous faut un pignon de Secousse-cousse.\x7Tu devras peut-\xc3\xaatre chercher \xc3\xa0 l'int\xc3\xa9rieur des b\xc3\xa2timents Vendibots pour trouver cette sorte de Cogs.\x7Quand tu en auras attrap\xc3\xa9 un, rapporte-le pour recevoir ta r\xc3\xa9compense."},
    3244: {
        QUEST: 'Nous avons fait quelques \xc3\xa9tudes sur les m\xc3\xa9canismes des Loibots.\x7Nous devons encore \xc3\xa9tudier certaines pi\xc3\xa8ces de plus pr\xc3\xa8s.\x7Apporte-nous un pignon de Charognard.\x7Tu peux en attraper un quand le Cog explose.'},
    3245: {
        QUEST: "Bon travail! Maintenant nous avons besoin d'un pignon de Frappedos pour faire la comparaison.\x7Ces pignons sont plus difficiles \xc3\xa0 attraper, ne te d\xc3\xa9courage pas."},
    3246: {
        QUEST: "Super! Encore un pignon et c'est bon.\x7Cette fois, il nous faut un pignon de Tournegris.\x7Quand tu en auras attrap\xc3\xa9 un, rapporte-le pour avoir ta r\xc3\xa9compense."},
    3220: {
        QUEST: "Je viens d'apprendre que _toNpcName_ te cherchait.\x7Pourquoi ne vas-tu pas voir ce qu'elle veut ?_where_"},
    3221: {
        QUEST: "Oh\xc3\xa9, _avName_! Et voil\xc3\xa0!\x7J'ai entendu dire que tu \xc3\xa9tais expert(e) en \xc3\xa9claboussures.\x7J'ai besoin de quelqu'un pour montrer l'exemple \xc3\xa0 tous les Toons du Jardin de Daisy.\x7Utilise tes attaques par \xc3\xa9claboussure pour vaincre un groupe de Cogs.\x7Encourage tes contacts \xc3\xa0 utiliser aussi les \xc3\xa9claboussures.\x7Lorque tu auras vaincu 20 Cogs, reviens ici pour ta r\xc3\xa9compense!"},
    3222: {
        QUEST: "C'est le moment de faire preuve de ta Toonma\xc3\xaetrise.\x7Si tu r\xc3\xa9ussis \xc3\xa0 reprendre un certain nombre de b\xc3\xa2timents aux Cogs, tu gagneras le droit \xc3\xa0 trois qu\xc3\xaates.\x7D'abord, tu dois prendre deux b\xc3\xa2timents aux Cogs.\x7N'h\xc3\xa9site pas \xc3\xa0 demander l'aide de tes contacts."},
    3223: {
        QUEST: 'Super travail pour ces b\xc3\xa2timents!\x7Maintenant tu dois prendre deux b\xc3\xa2timents de plus.\x7Ces immeubles doivent faire au moins deux \xc3\xa9tages.'},
    3224: {
        QUEST: 'Fantastique!\x7Maintenant tu dois prendre deux b\xc3\xa2timents de plus.\x7Ces immeubles doivent faire au moins trois \xc3\xa9tages.\x7Quand tu auras fini, reviens chercher ta r\xc3\xa9compense!',
        COMPLETE: "Tu as r\xc3\xa9ussi, _avName_!\x7Tu as fait preuve d'une excellente Toonma\xc3\xaetrise.",
        GREETING: ''},
    3225: {
        QUEST: "_toNpcName_ dit qu'elle a besoin d'aide.\x7Va voir si tu peux lui donner un coup de main ?_where_"},
    3235: {
        QUEST: "Oh, c'est la salade que j'ai command\xc3\xa9e!\x7Merci de me l'avoir apport\xc3\xa9e.\x7Tous ces Cogs ont d\xc3\xbb effrayer le livreur habituel de _toNpcName_ encore une fois.\x7Tu pourrais nous rendre service et vaincre quelques-uns des Cogs qui tra\xc3\xaenent par ici?\x7Va vaincre 10 Cogs dans le Jardin de Daisy et reviens voir _toNpcName_.",
        INCOMPLETE_PROGRESS: "Tu es en train de vaincre des Cogs pour moi?\x7C'est super!! Continue comme \xc3\xa7a!",
        COMPLETE: "Oh, merci beaucoup d'avoir vaincu ces Cogs!\x7Maintenant je vais peut-\xc3\xaatre pouvoir reprendre mon programme habituel de livraisons.\x7Ta r\xc3\xa9compense est...",
        INCOMPLETE_WRONG_NPC: 'Va raconter \xc3\xa0 _toNpcName_ tous les Cogs que tu as vaincus._where_'},
    3236: {
        QUEST: 'Il y a beaucoup trop de Loibots par ici.\x7Tu peux faire ta part de travail!\x7Va vaincre 3 b\xc3\xa2timents Loibot.'},
    3237: {
        QUEST: 'Super travail pour ces b\xc3\xa2timents Loibot!\x7Mais maintenant il y a beaucoup trop de Vendibots!\x7Va vaincre 3 b\xc3\xa2timents Vendibot, puis reviens chercher ta r\xc3\xa9compense.'},
    3238: {
        QUEST: 'Oh non! Un Cog Circulateur a vol\xc3\xa9 la cl\xc3\xa9 du Jardin de Daisy!\x7Va voir si tu peux la retrouver.\x7Souviens-toi que les Circulateurs ne se trouvent que dans les b\xc3\xa2timents Vendibot.'},
    3239: {
        QUEST: "Tu as bien trouv\xc3\xa9 une cl\xc3\xa9, mais ce n'est pas la bonne!\x7Nous avons besoin de la cl\xc3\xa9 du Jardin de Daisy.\x7Continue de chercher! Un Cog Circulateur l'a encore!"},
    3242: {
        QUEST: 'Oh non! Un Cog Avocageot a vol\xc3\xa9 la cl\xc3\xa9 du Jardin de Daisy!\x7Va voir si tu peux la retrouver.\x7Souviens-toi que les Avocageots ne se trouvent que dans les b\xc3\xa2timents Loibot.'},
    3243: {
        QUEST: "Tu as bien trouv\xc3\xa9 une cl\xc3\xa9, mais ce n'est pas la bonne!\x7Nous avons besoin de la cl\xc3\xa9 du Jardin de Daisy.\x7Continue de chercher! Un Cog Avocageot l'a encore!"},
    3240: {
        QUEST: "_toNpcName_ vient de me dire qu'un Avocageot lui a vol\xc3\xa9 un sac de graines pour oiseaux.\x7Va vaincre des Avocageots jusqu'\xc3\xa0 ce que tu retrouves les graines pour oiseaux de Piaf, et rapporte-les lui.\x7Les Avocageots ne se trouvent que dans les b\xc3\xa2timents Loibot._where_",
        COMPLETE: "Oh, merci beaucoup d'avoir retrouv\xc3\xa9 mes graines pour oiseaux!\x7Ta r\xc3\xa9compense est...",
        INCOMPLETE_WRONG_NPC: 'Bien, tu as retrouv\xc3\xa9 ces graines pour oiseaux!\x7Maintenant apporte-les \xc3\xa0 _toNpcName_._where_'},
    3241: {
        QUEST: 'Certains des b\xc3\xa2timents des Cogs deviennent beaucoup trop hauts.\x7Va voir si tu peux r\xc3\xa9duire de hauteur certains des immeubles les plus hauts.\x7Reprends 5 immeubles de 3 \xc3\xa9tages ou plus et reviens ici pour ta r\xc3\xa9compense.'},
    3250: {
        QUEST: "Lima, la d\xc3\xa9tective de la rue du Ch\xc3\xaane, a entendu parler d'un quartier g\xc3\xa9n\xc3\xa9ral Vendibot. \x7Va donc la voir et aide-la \xc3\xa0 enqu\xc3\xaater."},
    3251: {
        QUEST: "Il y a quelque chose de bizarre par ici.\x7Il y a tant de Vendibots!\x7J'ai entendu dire qu'ils ont install\xc3\xa9 leur propre quartier g\xc3\xa9n\xc3\xa9ral au bout de cette rue.\x7Va au bout de la rue voir ce qu'il en est.\x7Trouve des Cogs Vendibots dans leur quartier g\xc3\xa9n\xc3\xa9ral, vaincs-en 5 et reviens me le dire."},
    3252: {
        QUEST: "OK, annonce la couleur\x7Qu'est-ce que tu dis?\x7Ah, le quartier g\xc3\xa9n\xc3\xa9ral des Vendibots?? Oh non!!! Il faut faire quelque chose.\x7Nous devons le dire au Juge Ticot - il saura quoi faire.\x7Va le voir tout de suite et dis-lui ce que tu as trouv\xc3\xa9. Il est juste au bout de la rue."},
    3253: {
        QUEST: "Oui, puis-je t'aider ? Je suis tr\xc3\xa8s occup\xc3\xa9.\x7Hein ? Un quartier g\xc3\xa9n\xc3\xa9ral Cog?\x7Hein ? Sottises. \xc3\x87a n'est pas possible.\x7Tu dois te tromper. C'est grotesque.\x7Hein ? Ne discute pas avec moi.\x7Ok, alors ram\xc3\xa8ne des preuves.\x7Si les Vendibots sont vraiment en train de construire ce quartier g\xc3\xa9n\xc3\xa9ral Cog, les Cogs du quartier auront des plans sur eux.\x7Les Cogs adorent la paperasserie, tu le savais?\x7Va vaincre des Vendibots par l\xc3\xa0-bas jusqu'\xc3\xa0 ce que tu trouves des plans.\x7Rapporte-les moi, alors je te croirai peut-\xc3\xaatre."},
    3254: {
        QUEST: "Encore toi, hein ? Des plans? Tu les as?\x7Laisse-moi regarder \xc3\xa7a! Hmmm... Une usine ?\x7Ce doit \xc3\xaatre l\xc3\xa0 qu'ils fabriquent les Vendibots... Et qu'est-ce que c'est que \xc3\xa7a?\x7Oui, exactement ce que je pensais. Je le savais depuis le d\xc3\xa9part.\x7Ils sont en train de construire un quartier g\xc3\xa9n\xc3\xa9ral des Cogs Vendibots.\x7Ce n'est pas bon signe. Je dois passer quelques appels. Tr\xc3\xa8s occup\xc3\xa9. Au revoir!\x7Hein ? Oh oui, retourne ces plans \xc3\xa0 la d\xc3\xa9tective Lima.\x7Elle saura les lire mieux que quiconque.",
        COMPLETE: "Qu'a dit le Juge Ticot ?\x7On avait raison ? Oh non. Regardons ces plans.\x7Hmmm... On dirait que les Vendibots ont install\xc3\xa9 une usine avec l'outillage pour construire des Cogs.\x7\xc3\x87a a l'air tr\xc3\xa8s dangereux. N'y va pas tant que tu n'as pas plus de rigolpoints.\x7Quand tu auras plus de rigolpoints, nous en aurons beaucoup \xc3\xa0 apprendre sur le quartier g\xc3\xa9n\xc3\xa9ral des Vendibots.\x7Pour l'instant, bon travail, voil\xc3\xa0 ta r\xc3\xa9compense."},
    3255: {
        QUEST: "_toNpcName_ est en train d'enqu\xc3\xaater sur le quartier g\xc3\xa9n\xc3\xa9ral des Vendibots.\x7Va voir si tu peux donner un coup de main._where_"},
    3256: {
        QUEST: "_toNpcName_ est en train d'enqu\xc3\xaater sur le quartier g\xc3\xa9n\xc3\xa9ral des Vendibots.\x7Va voir si tu peux donner un coup de main._where_"},
    3257: {
        QUEST: "_toNpcName_ est en train d'enqu\xc3\xaater sur le quartier g\xc3\xa9n\xc3\xa9ral des Vendibots.\x7Va voir si tu peux lui donner un coup de main._where_"},
    3258: {
        QUEST: "Personne ne sait au juste ce que les Cogs sont en train de faire dans leur nouveau quartier g\xc3\xa9n\xc3\xa9ral.\x7J'ai besoin que tu nous ram\xc3\xa8nes des informations venant directement d'eux.\x7Si nous pouvons trouver quatre notes de service internes des Vendibots \xc3\xa0 l'int\xc3\xa9rieur de leur quartier g\xc3\xa9n\xc3\xa9ral, cela mettrait un peu les choses au clair.\x7Ram\xc3\xa8ne-moi la premi\xc3\xa8re note de service que tu pourras afin qu'on en sache un peu plus."},
    3259: {
        QUEST: 'Super! Voyons ce que dit cette note de service...\x7"\xc3\x80 l\'attention des Vendibots :\x7Je serai dans mon bureau tout en haut des Tours Vendibot pour faire monter en grade les Cogs. \x7Lorsque vous aurez gagn\xc3\xa9 suffisamment de m\xc3\xa9rites, montez me voir par l\'ascenseur du hall.\x7La pause est termin\xc3\xa9e - tout le monde au travail!"\x7Sign\xc3\xa9, Vice-Pr\xc3\xa9sident des Vendibots"\x7Aah.... Flippy sera content de voir \xc3\xa7a. Je lui envoie \xc3\xa7a tout de suite.\x7Va chercher une seconde note de service et rapporte-la moi.'},
    3260: {
        QUEST: 'Oh, bien, tu es de retour. Voyons ce que tu as trouv\xc3\xa9....\x7"\xc3\x80 l\'attention des Vendibots :\x7Les Tours Vendibot ont \xc3\xa9t\xc3\xa9 \xc3\xa9quip\xc3\xa9es d\'un nouveau syst\xc3\xa8me de s\xc3\xa9curit\xc3\xa9 pour emp\xc3\xaacher les Toons de p\xc3\xa9n\xc3\xa9trer \xc3\xa0 l\'int\xc3\xa9rieur.\x7Les Toons qui seront attrap\xc3\xa9s dans les Tours Vendibot seront retenus pour interrogatoire.\x7Veuillez en discuter dans le hall autour d\'un ap\xc3\xa9ritif.\x7Sign\xc3\xa9, Le Circulateur "\x7Tr\xc3\xa8s int\xc3\xa9ressant... Je communique l\'information imm\xc3\xa9diatement.\x7S\'il te pla\xc3\xaet, rapporte-moi une troisi\xc3\xa8me note de service.'},
    3261: {
        QUEST: 'Excellent travail, _avName_! Que dit cette note de service ?\x7"\xc3\x80 l\'attention des Vendibots :\x7Les Toons sont parvenus \xc3\xa0 trouver une fa\xc3\xa7on d\'infiltrer les Tours Vendibot.\x7Je vous appellerai ce soir pendant le d\xc3\xaener pour vous donner des d\xc3\xa9tails.\x7Sign\xc3\xa9, T\xc3\xa9l\xc3\xa9vendeur"\x7Hmmm... Je me demande comment les Toons se sont infiltr\xc3\xa9s....\x7Rapporte-moi une note de service suppl\xc3\xa9mentaire et je crois que nous aurons assez d\'informations pour l\'instant.',
        COMPLETE: 'Je savais que tu pouvais le faire! OK, voil\xc3\xa0 ce que dit la note de service....\x7"\xc3\x80 l\'attention des Vendibots :\x7J\'ai d\xc3\xa9je\xc3\xbbn\xc3\xa9 avec M. Hollywood hier.\x7Il dit que le Vice-Pr\xc3\xa9sident est tr\xc3\xa8s occup\xc3\xa9 en ce moment.\x7Il ne prendra de rendez-vous qu\'avec les Cogs qui m\xc3\xa9ritent une promotion.\x7J\'allais oublier, Passetout joue au golf avec moi dimanche.\x7Sign\xc3\xa9, Cafteur"\x7Bon... _avName_, voil\xc3\xa0 qui est bien utile.\x7Voil\xc3\xa0 ta r\xc3\xa9compense.'},
    3262: {
        QUEST: "_toNpcName_ a de nouvelles informations \xc3\xa0 propos de l'usine du quartier g\xc3\xa9n\xc3\xa9ral Vendibot.\x7Va donc voir ce que c'est._where_"},
    3263: {
        GREETING: 'Salut, mon pote!',
        QUEST: "Je suis Zucchini l'entra\xc3\xaeneur, mais tu peux simplement m'appeler Coach Z.\x7Je mets la gomme sur le squash et les \xc3\xa9tirements, si tu vois ce que je veux dire.\x7\xc3\x89coute, les Vendibots ont termin\xc3\xa9 une \xc3\xa9norme usine qui sort des Vendibots 24 heures sur 24.\x7Prends une \xc3\xa9quipe de potes Toons et va me r\xc3\xa9duire cette usine \xc3\xa0 n\xc3\xa9ant!\x7\xc3\x80 l'int\xc3\xa9rieur du quartier g\xc3\xa9n\xc3\xa9ral Vendibot, cherche le tunnel qui m\xc3\xa8ne \xc3\xa0 l'usine puis monte par l'ascenseur de l'usine.\x7V\xc3\xa9rifie que tu as fait le plein de gags, de rigolpoints et que tu as quelques Toons costauds comme guides.\x7Va vaincre le contrema\xc3\xaetre dans l'usine pour ralentir la progression des Vendibots.\x7Ce sera une vraie s\xc3\xa9ance d'entra\xc3\xaenement, si tu vois ce que je veux dire.",
        LEAVING: '\xc3\x80 plus, mon pote!',
        COMPLETE: 'H\xc3\xa9 mon pote, bon boulot pour cette usine!\x7On dirait que tu as trouv\xc3\xa9 un morceau de costume de Cog.\x7Il doit venir de la cha\xc3\xaene de fabrication des Cogs.\x7\xc3\x87a peut \xc3\xaatre pratique. Continue \xc3\xa0 en ramasser quand tu as du temps de libre.\x7Peut-\xc3\xaatre que si tu r\xc3\xa9cup\xc3\xa8res un costume de Cog complet, \xc3\xa7a pourrait \xc3\xaatre utile \xc3\xa0 quelque chose....'},
    4001: {
        GREETING: '',
        QUEST: 'Tu peux maintenant choisir la prochaine s\xc3\xa9rie de gags que tu veux apprendre.\x7Prends ton temps pour te d\xc3\xa9cider, et reviens quand tu auras choisi.',
        INCOMPLETE_PROGRESS: 'Pense bien \xc3\xa0 ta d\xc3\xa9cision avant de choisir.',
        INCOMPLETE_WRONG_NPC: 'Pense bien \xc3\xa0 ta d\xc3\xa9cision avant de choisir.',
        COMPLETE: 'Une sage d\xc3\xa9cision...',
        LEAVING: QuestsDefaultLeaving},
    4002: {
        GREETING: '',
        QUEST: 'Tu peux maintenant choisir la prochaine s\xc3\xa9rie de gags que tu veux apprendre.\x7Prends ton temps pour te d\xc3\xa9cider, et reviens quand tu auras choisi.',
        INCOMPLETE_PROGRESS: 'Pense bien \xc3\xa0 ta d\xc3\xa9cision avant de choisir.',
        INCOMPLETE_WRONG_NPC: 'Pense bien \xc3\xa0 ta d\xc3\xa9cision avant de choisir.',
        COMPLETE: 'Une sage d\xc3\xa9cision...',
        LEAVING: QuestsDefaultLeaving},
    4200: {
        QUEST: "Je parie que Tom aimerait de l'aide pour ses recherches._where_"},
    4201: {
        GREETING: 'Salut!',
        QUEST: "Je suis tr\xc3\xa8s emb\xc3\xaat\xc3\xa9 au sujet d'une vague de vols d'instruments.\x7Je fais une enqu\xc3\xaate parmi mes confr\xc3\xa8res commer\xc3\xa7ants.\x7Je vais peut-\xc3\xaatre pouvoir trouver une constante qui me permettra de r\xc3\xa9soudre ce cas.\x7Va voir Tina et demande-lui un inventaire des concertinas._where_"},
    4202: {
        QUEST: "Oui, j'ai parl\xc3\xa9 \xc3\xa0 Tom ce matin.\x7J'ai l'inventaire ici.\x7Tu vas lui apporter tout de suite, ok?_where_"},
    4203: {
        QUEST: 'Super! Et de un...\x7Maintenant va chercher celui de Yuki._where_'},
    4204: {
        QUEST: "Oh! L'inventaire!\x7J'avais compl\xc3\xa8tement oubli\xc3\xa9.\x7Je parie que je peux le faire le temps que tu aies vaincu 10 Cogs.\x7Repasse apr\xc3\xa8s \xc3\xa7a et je promets que ce sera pr\xc3\xaat.",
        INCOMPLETE_PROGRESS: "31, 32... OUPS!\x7Tu m'as fait perdre mon compte!",
        GREETING: ''},
    4205: {
        QUEST: "Ah, et voil\xc3\xa0.\x7Merci de m'avoir laiss\xc3\xa9 un peu de temps.\x7Emm\xc3\xa8ne \xc3\xa7a \xc3\xa0 Tom et dis-lui bonjour de ma part._where_"},
    4206: {
        QUEST: 'Hmm, tr\xc3\xa8s int\xc3\xa9ressant.\x7\xc3\x87a commence \xc3\xa0 ressembler \xc3\xa0 quelque chose.\x7OK, le dernier inventaire est celui de Fifi._where_'},
    4207: {
        QUEST: "Inventaire ?\x7Comment est-ce que je pourrais faire un inventaire sans formulaire ?\x7Va voir Cl\xc3\xa9ment de sol et demande-lui s'il en a un pour moi._where_",
        INCOMPLETE_PROGRESS: 'Alors, ce formulaire ?'},
    4208: {
        QUEST: "Ah \xc3\xa7a oui j'ai un formulaire d'inventaire!\x7Mais c'est pas gratuit, tu vois.\x7Je vais te dire. Je te le vends pour une tarte \xc3\xa0 la cr\xc3\xa8me enti\xc3\xa8re.",
        GREETING: 'Allez, mon petit!',
        LEAVING: 'Chouette...',
        INCOMPLETE_PROGRESS: "Une seule tranche c'est pas assez.\x7J'ai faim, mon petit! Je veux la tarte TOUTE ENTI\xc3\x88RE."},
    4209: {
        GREETING: '',
        QUEST: 'Mmmm...\x7Super bon!\x7Voil\xc3\xa0 ton formulaire pour Fifi._where_'},
    4210: {
        GREETING: '',
        QUEST: "Merci. \xc3\x87a va bien m'aider.\x7Voyons...violons: 2\x7\xc3\x87a y est! Et voil\xc3\xa0!",
        COMPLETE: 'Bon travail, _avName_!\x7Je suis s\xc3\xbbr de pouvoir attraper ces voleurs maintenant.\x7On va pouvoir creuser cette affaire!'},
    4211: {
        QUEST: 'Dis donc, le Dr Tefaispasdebile appelle toutes les cinq minutes. Tu pourrais aller voir quel est son probl\xc3\xa8me ?_where_'},
    4212: {
        QUEST: "Houlala! Je suis content que le quartier g\xc3\xa9n\xc3\xa9ral des Toons ait fini par envoyer quelqu'un.\x7\xc3\x87a fait des jours que je n'ai pas vu un client.\x7Ce sont ces satan\xc3\xa9s Gobechiffres qui sont partout.\x7Je crois qu'ils enseignent une mauvaise hygi\xc3\xa8ne buccale \xc3\xa0 nos r\xc3\xa9sidents.\x7Va donc en vaincre dix et nous verrons si les affaires reprennent.",
        INCOMPLETE_PROGRESS: 'Toujours pas de patients. Mais continue!'},
    4213: {
        QUEST: "Tu sais apr\xc3\xa8s tout peut-\xc3\xaatre que ce n'\xc3\xa9tait pas les Gobechiffres.\x7Peut-\xc3\xaatre que ce sont simplement les Caissbots en g\xc3\xa9n\xc3\xa9ral.\x7D\xc3\xa9barrasse-nous de vingt d'entre eux et j'esp\xc3\xa8re que quelqu'un viendra au moins pour un bilan de sant\xc3\xa9.",
        INCOMPLETE_PROGRESS: 'Je sais que vingt \xc3\xa7a fait beaucoup. Mais je suis certain que \xc3\xa7a va rapporter des tonnes.'},
    4214: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Je ne comprends rien du tout!\x7Toujours pas un SEUL client.\x7Peut-\xc3\xaatre qu'on devrait remonter jusqu'\xc3\xa0 la source.\x7Essaie de reprendre un b\xc3\xa2timent Cog Caissbot.\x7\xc3\x87a devrait faire l'affaire...",
        INCOMPLETE_PROGRESS: "Oh, s'il te pla\xc3\xaet! Juste un tout petit b\xc3\xa2timent...",
        COMPLETE: "Toujours personne.\x7Mais tu vois, maintenant que j'y pense.\x7Je n'avais pas non plus de clients avant l'invasion des Cogs!\x7Je te remercie quand m\xc3\xaame beaucoup pour ton aide.\x7Cela devrait te rendre service."},
    4215: {
        QUEST: "Anna a d\xc3\xa9sesp\xc3\xa9r\xc3\xa9ment besoin de quelqu'un pour l'aider.\x7Pourquoi ne vas-tu pas voir ce que tu peux faire ?_where_"},
    4216: {
        QUEST: "Merci d'\xc3\xaatre l\xc3\xa0 aussi vite!\x7On dirait que les Cogs sont partis avec les tickets de croisi\xc3\xa8re de plusieurs de mes clients.\x7Yuki a dit qu'elle avait vu un Passetout sortir d'ici avec des tickets plein les mains.\x7Va voir si tu peux retrouver le ticket pour l'Alaska de Jack B\xc3\xbbcheron.",
        INCOMPLETE_PROGRESS: "Ces Passetouts pourraient \xc3\xaatre n'importe o\xc3\xb9 maintenant..."},
    4217: {
        QUEST: "Oh, super. Tu l'as trouv\xc3\xa9!\x7Puisque je peux compter sur toi, va le porter \xc3\xa0 Jack pour moi, tu veux bien ?_where_"},
    4218: {
        QUEST: "Tralala!\x7Alaska, me voil\xc3\xa0!\x7Je ne peux plus supporter ces Cogs infernaux.\x7Dis donc, je crois qu'Anna a encore besoin de toi._where_"},
    4219: {
        QUEST: "Ouais, tu as devin\xc3\xa9.\x7J'aurais besoin que tu secoues ces satan\xc3\xa9s Passetouts pour r\xc3\xa9cup\xc3\xa9rer le ticket de Tabatha pour la f\xc3\xaate du Jazz.\x7Tu sais comment \xc3\xa7a marche...",
        INCOMPLETE_PROGRESS: "Il y en a d'autres qui r\xc3\xb4dent..."},
    4220: {
        QUEST: 'Adorable!\x7Tu peux lui emmener \xc3\xa7a pour moi aussi?_where_'},
    4221: {
        GREETING: '',
        LEAVING: 'Sois sympa...',
        QUEST: "Super, mon petit!\x7Maintenant je suis \xc3\xa0 la f\xc3\xaate, _avName_.\x7Avant de partir, tu ferais mieux d'aller voir Anna Banane encore une fois..._where_"},
    4222: {
        QUEST: "C'est la derni\xc3\xa8re fois, je te promets!\x7Maintenant tu vas chercher le ticket de Barry pour le concours de chant.",
        INCOMPLETE_PROGRESS: 'Allez, _avName_.\x7Barry compte sur toi.'},
    4223: {
        QUEST: '\xc3\x87a devrait redonner le sourire \xc3\xa0 Barry._where_'},
    4224: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Bonjour, Bonjour, BONJOUR!\x7Super!\x7Je suis s\xc3\xbbr que les gars et moi on a va ramasser le gros lot cette ann\xc3\xa9e.\x7Anna demande que tu repasses la voir pour r\xc3\xa9cup\xc3\xa9rer ta r\xc3\xa9compense._where_\x7Au revoir, au revoir, AU REVOIR!',
        COMPLETE: "Merci pour toute ton aide, _avName_.\x7Tu es vraiment un atout pour nous \xc3\xa0 Toontown.\x7En parlant d'atouts..."},
    902: {
        QUEST: "Va donc voir L\xc3\xa9o.\x7Il a besoin de quelqu'un pour porter un message._where_"},
    4903: {
        QUEST: "Pote!\x7Mes castagnettes sont toutes ternies et j'ai un grand spectacle ce soir. \x7Emporte-les donc \xc3\xa0 Carlos voir s'il peut me les faire reluire._where_"},
    4904: {
        QUEST: "Voui, y\xc3\xa9 crois que y\xc3\xa9 peux r\xc3\xa9luire \xc3\xa7a.\x7M\xc3\xa9 y\xc3\xa9 b\xc3\xa9zoin d'encre de seiche bleue.",
        GREETING: '\xc2\xa1Hol\xc3\xa0!',
        LEAVING: '\xc2\xa1Adi\xc3\xb3s!',
        INCOMPLETE_PROGRESS: 'Tou p\xc3\xa9 trrouver la seiche partout sour l\xc3\xa9 pontons de p\xc3\xaache.'},
    4905: {
        QUEST: "Voui! Souperr!\x7Ah\xc3\xb3ra y\xc3\xa9 b\xc3\xa9zoin d'un peu de temps pour r\xc3\xa9luire \xc3\xa7a.\x7Tou p\xc3\xa9 aller r\xc3\xa9coup\xc3\xa9rer un b\xc3\xa2timent de oun \xc3\xa9tage pendant qu\xc3\xa9 y\xc3\xa9 trravaille ?",
        GREETING: '\xc2\xa1Hol\xc3\xa0!',
        LEAVING: '\xc2\xa1Adi\xc3\xb3s!',
        INCOMPLETE_PROGRESS: 'Oun pitite minute...'},
    4906: {
        QUEST: 'Trr\xc3\xa8s bien!\x7Voil\xc3\xa0 les castagnettes pour L\xc3\xa9o._where_'},
    4907: {
        GREETING: '',
        QUEST: 'Super, mon petit!\x7Elles sont superbes!\x7Maintenant j\'ai besoin que tu me rapportes une copie des paroles de "Un No\xc3\xabl toon" de chez \xc3\x89lise._where_'},
    4908: {
        QUEST: "Hol\xc3\xa0 par ici!\x7Hmmm, je n'ai pas de copie de cette chanson.\x7Si tu me laisses un peu de temps je pourrai la retranscrire de m\xc3\xa9moire.\x7Pourquoi tu n'irais pas faire un tour et reprendre un b\xc3\xa2timent de deux \xc3\xa9tages pendant que j'\xc3\xa9cris?"},
    4909: {
        QUEST: 'Je suis d\xc3\xa9sol\xc3\xa9e.\x7Ma m\xc3\xa9moire est un peu floue.\x7Si tu vas reprendre un b\xc3\xa2timent de trois \xc3\xa9tages, je suis s\xc3\xbbre que ce sera fait quand tu reviendras...'},
    4910: {
        QUEST: "\xc3\x87a y est!\x7D\xc3\xa9sol\xc3\xa9e d'avoir mis si longtemps.\x7Rapporte-\xc3\xa7a \xc3\xa0 L\xc3\xa9o._where_",
        GREETING: '',
        COMPLETE: 'G\xc3\xa9nial, mon petit!\x7Mon concert va casser la baraque!\x7\xc3\x80 propos de casser, tu pourras utiliser \xc3\xa7a sur quelques Cogs...'},
    5247: {
        QUEST: "Le quartier est assez chaud...\x7Tu pourrais avoir besoin d'apprendre quelques nouveaux trucs.\x7_toNpcName_ m'a appris tout ce que je sais, il peut peut-\xc3\xaatre t'aider aussi._where_"},
    5248: {
        GREETING: 'Ahh, oui.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Tu as l'air d'avoir des difficult\xc3\xa9s avec cette mission.",
        QUEST: "Aah, bienvenue, nouvel apprenti.\x7Je sais tout ce qu'on peut savoir \xc3\xa0 propos du jeu de tartes.\x7Mais avant qu'on ne commence ton entra\xc3\xaenement, une petite d\xc3\xa9monstration s'impose.\x7Va donc faire un tour et vaincre dix des plus gros Cogs."},
    5249: {
        GREETING: 'Mmmmm.',
        QUEST: "Excellent!\x7Maintenant tu vas nous montrer ce que tu sais faire \xc3\xa0 la p\xc3\xaache.\x7J'ai fait tomber trois d\xc3\xa9s en peluche dans la mare hier.\x7Va-les p\xc3\xaacher et rapporte-les moi.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: "On dirait que tu n'es pas si habile avec la canne et le moulinet."},
    5250: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Aah! Ces d\xc3\xa9s auront l'air super, accroch\xc3\xa9s au r\xc3\xa9troviseur de ma bagnole!\x7Maintenant, montre-moi que tu peux distinguer tes ennemis les uns des autres.\x7Reviens quand tu auras repris deux des plus grands b\xc3\xa2timents Loibot.",
        INCOMPLETE_PROGRESS: 'Est-ce que tu as des difficult\xc3\xa9s avec ces b\xc3\xa2timents?'},
    5258: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Aah! Ces d\xc3\xa9s auront l'air super, accroch\xc3\xa9s au r\xc3\xa9troviseur de ma bagnole!\x7Maintenant, montre-moi que tu peux distinguer tes ennemis les uns des autres.\x7Reviens quand tu auras repris deux des plus grands b\xc3\xa2timents Chefbot.",
        INCOMPLETE_PROGRESS: 'Est-ce que tu as des difficult\xc3\xa9s avec ces b\xc3\xa2timents?'},
    5259: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Aah! Ces d\xc3\xa9s auront l'air super, accroch\xc3\xa9s au r\xc3\xa9troviseur de ma bagnole!\x7Maintenant, montre-moi que tu peux distinguer tes ennemis les uns des autres.\x7Reviens quand tu auras repris deux des plus grands b\xc3\xa2timents Caissbot.",
        INCOMPLETE_PROGRESS: 'Est-ce que tu as des difficult\xc3\xa9s avec ces b\xc3\xa2timents?'},
    5260: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Aah! Ces d\xc3\xa9s auront l'air super, accroch\xc3\xa9s au r\xc3\xa9troviseur de ma bagnole!\x7Maintenant, montre-moi que tu peux distinguer tes ennemis les uns des autres.\x7Reviens quand tu auras repris deux des plus grands b\xc3\xa2timents Vendibot.",
        INCOMPLETE_PROGRESS: 'Est-ce que tu as des difficult\xc3\xa9s avec ces b\xc3\xa2timents?'},
    5200: {
        QUEST: 'Ces faux-jetons de Cogs font encore des leurs.\x7_toNpcName_ vient de signaler un autre objet disparu. Va voir si tu peux r\xc3\xa9gler cela._where_'},
    5201: {
        GREETING: '',
        QUEST: "Salut, _avName_. Je sais que je devrais te remercier d'\xc3\xaatre venu.\x7Un groupe de ces Chasset\xc3\xaates est venu et a vol\xc3\xa9 mon ballon de foot.\x7Le chef m'a dit que je devais faire des \xc3\xa9conomies et me l'a arrach\xc3\xa9!\x7Peux-tu me rapporter mon ballon ?",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Est-ce que tu as retrouv\xc3\xa9 mon ballon de foot ?',
        COMPLETE: "Youpiii! Tu l'as trouv\xc3\xa9! Tiens, prends ta r\xc3\xa9compense..."},
    5261: {
        GREETING: '',
        QUEST: "Salut, _avName_. Je sais que je devrais te remercier d'\xc3\xaatre l\xc3\xa0.\x7Un groupe de ces Bifaces est venu et a vol\xc3\xa9 mon ballon de foot.\x7Le chef m'a dit que je devais faire des \xc3\xa9conomies et me l'a arrach\xc3\xa9!\x7Peux-tu me rapporter mon ballon ?",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Est-ce que tu as retrouv\xc3\xa9 mon ballon de foot ?',
        COMPLETE: "Youpiii! Tu l'as trouv\xc3\xa9! Tiens, prends ta r\xc3\xa9compense..."},
    5262: {
        GREETING: '',
        QUEST: "Salut, _avName_. Je sais que je devrais te remercier d'\xc3\xaatre l\xc3\xa0.\x7Un groupe de ces Sacasous est venu et a vol\xc3\xa9 mon ballon de foot.\x7Le chef m'a dit que je devais faire des \xc3\xa9conomies et me l'a arrach\xc3\xa9!\x7Peux-tu me rapporter mon ballon ?",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Est-ce que tu as retrouv\xc3\xa9 mon ballon de foot ?',
        COMPLETE: "Youpiii! Tu l'as trouv\xc3\xa9! Tiens, prends ta r\xc3\xa9compense..."},
    5263: {
        GREETING: '',
        QUEST: "Salut, _avName_. Je sais que je devrais te remercier d'\xc3\xaatre l\xc3\xa0.\x7Un groupe de ces Tournegris est venu et a vol\xc3\xa9 mon ballon de foot.\x7Le chef m'a dit que je devais faire des \xc3\xa9conomies et me l'a arrach\xc3\xa9!\x7Peux-tu me rapporter mon ballon ?",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Est-ce que tu as retrouv\xc3\xa9 mon ballon de foot ?',
        COMPLETE: "Youpiii! Tu l'as trouv\xc3\xa9! Tiens, prends ta r\xc3\xa9compense..."},
    5202: {
        QUEST: "Le Glagla a \xc3\xa9t\xc3\xa9 envahi par des Cogs parmi les plus robustes qu'on ait vus.\x7Tu auras probablement besoin d'emporter plus de gags l\xc3\xa0-bas.\x7J'ai entendu dire que _toNpcName_ pourrait te pr\xc3\xaater un grand sac pour emporter plus de gags._where_"},
    5203: {
        GREETING: 'Eh? Tu es dans mon \xc3\xa9quipe de luge ?',
        QUEST: "Qu'est-ce que c'est ? Tu veux un sac?\x7J'en avais un par l\xc3\xa0...peut-\xc3\xaatre qu'il est dans ma luge ?\x7Mais c'est que... Je n'ai pas vu ma luge depuis la grande course!\x7Peut-\xc3\xaatre qu'un de ces Cogs l'a prise ?",
        LEAVING: 'As-tu vu ma luge ?',
        INCOMPLETE_PROGRESS: "Rappelle-moi qui tu es? D\xc3\xa9sol\xc3\xa9, je suis un peu \xc3\xa9tourdi depuis l'accident."},
    5204: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Est-ce que c'est ma luge ? Je ne vois pas de sac par ici.\x7Je crois que Boris Tourne \xc3\xa9tait dans l'\xc3\xa9quipe...c'est peut-\xc3\xaatre lui qui l'a?_where_"},
    5205: {
        GREETING: 'Oooh, ma t\xc3\xaate!',
        LEAVING: '',
        QUEST: "Hein ? Ted qui? Un sac?\x7Ah, peut-\xc3\xaatre qu'il \xc3\xa9tait dans notre \xc3\xa9quipe ?\x7J'ai tellement mal \xc3\xa0 la t\xc3\xaate que je n'arrive plus \xc3\xa0 r\xc3\xa9fl\xc3\xa9chir.\x7Pourrais-tu aller me p\xc3\xaacher des gla\xc3\xa7ons dans la mare gel\xc3\xa9e pour ma t\xc3\xaate ?",
        INCOMPLETE_PROGRESS: 'A\xc3\xafe, ma t\xc3\xaate me fait mal! Tu as de la glace ?'},
    5206: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Aah, ma t\xc3\xaate va beaucoup mieux!\x7Alors tu cherches le sac de Ted, hein ?\x7Je crois qu'il a atterri sur la t\xc3\xaate de Sam Simiesque apr\xc3\xa8s l'accident._where_"},
    5207: {
        GREETING: 'H\xc3\xa9-ho!',
        LEAVING: '',
        QUEST: "Quoi c'est \xc3\xa7a un sac? Qui c'est \xc3\xa7a Bouris?\x7Moi avoir peur b\xc3\xa2timents! Toi battre b\xc3\xa2timents, moi te donner sac!",
        INCOMPLETE_PROGRESS: 'Encore b\xc3\xa2timents! Moi encore peur!',
        COMPLETE: "Ooooh! Moi t'aime!"},
    5208: {
        GREETING: '',
        LEAVING: 'Hein!',
        QUEST: "Ooooh! Moi t'aime!\x7Va Atelier de ski. Sac l\xc3\xa0-bas."},
    5209: {
        GREETING: 'Pote!',
        LEAVING: "'plus!",
        QUEST: 'Bon sang, ce Sam Simiesque est fou!\x7Si tu es aussi malade que Sam, je te donne ton sac.\x7Va d\xc3\xa9molir des Cogs pour ton sac, mon pote! Salut!',
        INCOMPLETE_PROGRESS: "Es-tu certain(e) d'\xc3\xaatre au point ? Va donc d\xc3\xa9molir plus de Cogs.",
        COMPLETE: "Ouah! T'es vachement chouette! C'est un sacr\xc3\xa9 tas de Cogs que tu as bousill\xc3\xa9s!\x7Voil\xc3\xa0 ton sac!"},
    5210: {
        QUEST: "_toNpcName_ aime quelqu'un du quartier en secret.\x7Si tu l'aides, elle pourrait te donner une belle r\xc3\xa9compense._where_"},
    5211: {
        GREETING: 'Bouhouhou.',
        QUEST: "J'ai pass\xc3\xa9 toute la nuit derni\xc3\xa8re \xc3\xa0 \xc3\xa9crire une lettre au chien que j'aime.\x7Mais avant que je puisse l'envoyer, un de ces m\xc3\xa9chants Cogs avec un bec me l'a d\xc3\xa9rob\xc3\xa9e.\x7Peux-tu me la rapporter ?",
        LEAVING: 'Bouhouhou.',
        INCOMPLETE_PROGRESS: "S'il te pla\xc3\xaet, retrouve ma lettre."},
    5264: {
        GREETING: 'Bouhouhou.',
        QUEST: "J'ai pass\xc3\xa9 toute la nuit derni\xc3\xa8re \xc3\xa0 \xc3\xa9crire une lettre au chien que j'aime.\x7Mais avant que je puisse l'envoyer, un de ces m\xc3\xa9chants Cogs avec un aileron me l'a d\xc3\xa9rob\xc3\xa9e.\x7Peux-tu me la rapporter ?",
        LEAVING: 'Bouhouhou.',
        INCOMPLETE_PROGRESS: "S'il te pla\xc3\xaet, retrouve ma lettre."},
    5265: {
        GREETING: 'Bouhouhou.',
        QUEST: "J'ai pass\xc3\xa9 toute la nuit derni\xc3\xa8re \xc3\xa0 \xc3\xa9crire une lettre au chien que j'aime.\x7Mais avant que je puisse l'envoyer, un de ces m\xc3\xa9chants Cogs Circulateurs me l'a d\xc3\xa9rob\xc3\xa9e.\x7Peux-tu me la rapporter ?",
        LEAVING: 'Bouhouhou.',
        INCOMPLETE_PROGRESS: "S'il te pla\xc3\xaet, retrouve ma lettre."},
    5266: {
        GREETING: 'Bouhouhou.',
        QUEST: "J'ai pass\xc3\xa9 toute la nuit derni\xc3\xa8re \xc3\xa0 \xc3\xa9crire une lettre au chien que j'aime.\x7Mais avant que je puisse l'envoyer, un de ces m\xc3\xa9chants Cogs Attactics me l'a d\xc3\xa9rob\xc3\xa9e.\x7Peux-tu me la rapporter ?",
        LEAVING: 'Bouhouhou.',
        INCOMPLETE_PROGRESS: "S'il te pla\xc3\xaet, retrouve ma lettre."},
    5212: {
        QUEST: "Oh, merci d'avoir retrouv\xc3\xa9 ma lettre!\x7S'il te pla\xc3\xaet, peux-tu la remettre au plus beau chien du quartier ?",
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Tu n'as pas remis ma lettre, n'est-ce pas?"},
    5213: {
        GREETING: 'Charm\xc3\xa9, certainement.',
        QUEST: "Je ne peux pas m'occuper de ta lettre, tu vois.\x7Tous mes chiots m'ont \xc3\xa9t\xc3\xa9 pris!\x7Si tu les ram\xc3\xa8nes, peut-\xc3\xaatre qu'on pourra parler.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Mes pauvres petits chiots!'},
    5214: {
        GREETING: '',
        LEAVING: 'Youhouuu!',
        QUEST: "Merci de m'avoir rapport\xc3\xa9 mes petits choux.\x7Regardons cette lettre maintenant...Mmmm, il semblerait que j'ai une autre admiratrice secr\xc3\xa8te.\x7Il est temps de rendre visite \xc3\xa0 mon cher ami Carl.\x7Tu l'aimeras beaucoup, c'est certain._where_"},
    5215: {
        GREETING: 'H\xc3\xa9, h\xc3\xa9...',
        LEAVING: 'Reviens, oui, oui.',
        INCOMPLETE_PROGRESS: "Il y en a encore des gros par ici. Reviens nous voir quand il n'y en aura plus.",
        QUEST: "Qui est-ce qui t'envoie ? On aime pas trop les b\xc3\xaacheurs, non...\x7Mais on aime encore moins les Cogs...\x7D\xc3\xa9barrasse-nous donc des gros et on t'aidera, oui on t'aidera."},
    5216: {
        QUEST: "On t'avait bien dit qu'on t'aiderait.\x7Tu peux emmener cette bague \xc3\xa0 la fille.",
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Tu as encore la bague ???',
        COMPLETE: "Oh, tu es un amour!!! Merci!!!\x7Oh, et j'ai quelque chose de sp\xc3\xa9cial pour toi aussi."},
    5217: {
        QUEST: "On dirait que _toNpcName_ pourrait avoir besoin d'aide._where_"},
    5218: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Je crois bien qu'il y a d'autres Circulateurs par ici.",
        QUEST: "\xc3\x80 l'aide!!! \xc3\x80 l'aide!!! Je n'en peux plus!\x7Ces Circulateurs me rendent dingue!!!"},
    5219: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Ce n'est pas possible qu'il n'y ait que \xc3\xa7a. Je viens d'en voir un!!!",
        QUEST: "Oh, merci, mais maintenant ce sont les Attactics!!!\x7Il faut que tu m'aides!!!"},
    5220: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Non, non, il y en avait un juste l\xc3\xa0!',
        QUEST: 'Je r\xc3\xa9alise maintenant que ce sont les Usuriers!!!\x7Je croyais que tu allais me sauver!!!'},
    5221: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Tu sais quoi, peut-\xc3\xaatre finalement que ce ne sont pas du tout les Cogs!!!\x7Pourrais-tu demander \xc3\xa0 Ga\xc3\xablle de me pr\xc3\xa9parer une potion calmante ? \xc3\x87a m'aiderait peut-\xc3\xaatre...._where_"},
    5222: {
        LEAVING: '',
        QUEST: "Oh, ce Harry, c'est quelqu'un!\x7Je vais concocter quelque chose qui le remettra sur pied!\x7Bon, on dirait que je n'ai plus de moustaches de sardine...\x7Sois un ange et cours \xc3\xa0 la mare m'en attraper.",
        INCOMPLETE_PROGRESS: 'Tu les as, ces moustaches de sardine ?'},
    5223: {
        QUEST: 'OK. Merci, mon ange.\x7Voil\xc3\xa0, maintenant porte \xc3\xa7a \xc3\xa0 Harry. \xc3\x87a devrait le calmer tout de suite.',
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Vas-y maintenant, emporte la potion \xc3\xa0 Harry.'},
    5224: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Tu vas attraper ces Avocageots pour moi, n'est-ce pas?",
        QUEST: "Oh merci mon Dieu tu es de retour!\x7Donne-moi la potion, vite!!!\x7Glou, glou, glou...\x7Berk, c'est d\xc3\xa9go\xc3\xbbtant!!\x7Mais tu sais quoi? Je me sens bien plus calme. Maintenant que j'ai les id\xc3\xa9es claires, je r\xc3\xa9alise que...\x7C'est les Avocageots qui me rendaient malade pendant tout ce temps!!!",
        COMPLETE: "Bon sang! Maintenant je peux me d\xc3\xa9tendre!\x7J'ai s\xc3\xbbrement quelque chose \xc3\xa0 te donner. Oh, prends \xc3\xa7a!"},
    5225: {
        QUEST: "Depuis l'incident avec le pain de navets, Phil \xc3\x89lectrique est furieux apr\xc3\xa8s _toNpcName_.\x7Tu pourrais peut-\xc3\xaatre aider Paul \xc3\xa0 les r\xc3\xa9concilier ?_where_"},
    5226: {
        QUEST: "Ouais, tu as sans doute entendu dire que Phil \xc3\x89lectrique est furieux contre moi...\x7J'essayais juste d'\xc3\xaatre gentil avec ce pain de navets.\x7Peut-\xc3\xaatre que tu pourrais le remettre de bonne humeur.\x7Phil a horreur de ces Cogs Caissbots, surtout leurs b\xc3\xa2timents.\x7Si tu reprends des b\xc3\xa2timents Caissbot, \xc3\xa7a pourrait aider.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Peut-\xc3\xaatre quelques b\xc3\xa2timents de plus?'},
    5227: {
        QUEST: "C'est formidable! Va dire \xc3\xa0 Phil ce que tu as fait._where_"},
    5228: {
        QUEST: "Oh il a fait \xc3\xa7a?\x7Ce Paul croit qu'il peut s'en tirer comme \xc3\xa7a, hein ?\x7Il m'a cass\xc3\xa9 ma dent, oui, avec son fichu pain de navets!\x7Peut-\xc3\xaatre que si tu amenais ma dent au Dr Marmotter, il pourrait la r\xc3\xa9parer.",
        GREETING: 'Mmmmrrphh.',
        LEAVING: 'Grrr, grrr.',
        INCOMPLETE_PROGRESS: 'Encore toi? Je pensais que tu allais faire r\xc3\xa9parer ma dent.'},
    5229: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Je suis encore en train de travailler sur la dent. \xc3\x87a va \xc3\xaatre un peu plus long.',
        QUEST: "Ah oui, cette dent est en mauvais \xc3\xa9tat, c'est s\xc3\xbbr.\x7Je peux peut-\xc3\xaatre faire quelque chose, mais \xc3\xa7a va mettre un moment.\x7Tu pourrais peut-\xc3\xaatre profiter de ce temps-l\xc3\xa0 pour d\xc3\xa9barrasser les rues de quelques Cogs Caissbots?\x7Ils effraient mes clients."},
    5267: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Je suis encore en train de travailler sur la dent. \xc3\x87a va \xc3\xaatre un peu plus long.',
        QUEST: "Ah oui, cette dent est en mauvais \xc3\xa9tat, c'est s\xc3\xbbr.\x7Je peux peut-\xc3\xaatre faire quelque chose, mais \xc3\xa7a va mettre un moment.\x7Tu pourrais peut-\xc3\xaatre profiter de ce temps-l\xc3\xa0 pour d\xc3\xa9barrasser les rues de quelques Cogs Vendibots?\x7Ils effraient mes clients."},
    5268: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Je suis encore en train de travailler sur la dent. \xc3\x87a va \xc3\xaatre un peu plus long.',
        QUEST: "Ah oui, cette dent est en mauvais \xc3\xa9tat, c'est s\xc3\xbbr.\x7Je peux peut-\xc3\xaatre faire quelque chose, mais \xc3\xa7a va mettre un moment.\x7Tu pourrais peut-\xc3\xaatre profiter de ce temps-l\xc3\xa0 pour d\xc3\xa9barrasser les rues de quelques Cogs Loibots?\x7Ils effraient mes clients."},
    5269: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Je suis encore en train de travailler sur la dent. \xc3\x87a va \xc3\xaatre un peu plus long.',
        QUEST: "Ah oui, cette dent est en mauvais \xc3\xa9tat, c'est s\xc3\xbbr.\x7Je peux peut-\xc3\xaatre faire quelque chose, mais \xc3\xa7a va mettre un moment.\x7Tu pourrais peut-\xc3\xaatre profiter de ce temps-l\xc3\xa0 pour d\xc3\xa9barrasser les rues de quelques Cogs Chefbots?\x7Ils effraient mes clients."},
    5230: {
        GREETING: '',
        QUEST: "Je suis content que tu sois revenu!\x7J'ai arr\xc3\xaat\xc3\xa9 d'essayer de r\xc3\xa9parer cette vieille dent, et j'ai fait une nouvelle dent en or pour Phil \xc3\xa0 la place.\x7Malheureusement un Pillard me l'a d\xc3\xa9rob\xc3\xa9e.\x7Tu peux peut-\xc3\xaatre le rattraper si tu cours.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Tu l'as retrouv\xc3\xa9e, cette dent ?"},
    5270: {
        GREETING: '',
        QUEST: "Je suis content que tu sois revenu(e)!\x7J'ai arr\xc3\xaat\xc3\xa9 d'essayer de r\xc3\xa9parer cette vieille dent, et j'ai fait une nouvelle dent en or pour Phil \xc3\xa0 la place.\x7Malheureusement un Gros Blochon me l'a d\xc3\xa9rob\xc3\xa9e.\x7Tu peux peut-\xc3\xaatre le rattraper si tu cours.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Tu l'as retrouv\xc3\xa9e, cette dent ?"},
    5271: {
        GREETING: '',
        QUEST: "Je suis content que tu sois revenu(e)!\x7J'ai arr\xc3\xaat\xc3\xa9 d'essayer de r\xc3\xa9parer cette vieille dent, et j'ai fait une nouvelle dent en or pour Phil \xc3\xa0 la place.\x7Malheureusement M. Hollywood me l'a d\xc3\xa9rob\xc3\xa9e.\x7Tu peux peut-\xc3\xaatre le rattraper si tu cours.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Tu l'as retrouv\xc3\xa9e, cette dent ?"},
    5272: {
        GREETING: '',
        QUEST: "Je suis content que tu sois revenu(e)!\x7J'ai arr\xc3\xaat\xc3\xa9 d'essayer de r\xc3\xa9parer cette vieille dent, et j'ai fait une nouvelle dent en or pour Phil \xc3\xa0 la place.\x7Malheureusement un Chouffleur me l'a d\xc3\xa9rob\xc3\xa9e.\x7Tu peux peut-\xc3\xaatre le rattraper si tu cours.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Tu l'as retrouv\xc3\xa9e, cette dent ?"},
    5231: {
        QUEST: 'Super, voil\xc3\xa0 la dent!\x7Pourquoi ne filerais-tu pas chez Phil pour lui porter ?',
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Je parie que Phil serait content de voir sa nouvelle dent.'},
    5232: {
        QUEST: "Oh, merci.\x7Mmmrrrphhhh\x7\xc3\x87a a l'air de quoi, hein ?\x7OK, tu peux dire \xc3\xa0 Paul que je lui pardonne.",
        LEAVING: '',
        GREETING: ''},
    5233: {
        QUEST: "Oh, bonne nouvelle.\x7Je savais bien que ce vieux Phil ne pourrait pas rester f\xc3\xa2ch\xc3\xa9 contre moi.\x7Pour prouver ma bonne volont\xc3\xa9, je lui ai fait cuire ce pain de pommes de pin.\x7Pourrais-tu lui porter, s'il te pla\xc3\xaet ?",
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Presse-toi donc. Le pain de pommes de pin est meilleur chaud.',
        COMPLETE: "Oh, qu'est-ce que c'est que \xc3\xa7a? Pour moi?\x7Gromp, gromp...\x7A\xc3\xaf\xc3\xaf\xc3\xafa\xc3\xaf\xc3\xafe! Ma dent! Ce Paul Poulemouill\xc3\xa9e!\x7Oh, apr\xc3\xa8s tout ce n'est pas ta faute. Voil\xc3\xa0, prends \xc3\xa7a pour ta peine."},
    903: {
        QUEST: 'Tu dois te pr\xc3\xa9parer \xc3\xa0 voir _toNpcName_ le vieillard du blizzard pour ton test final._where_'},
    5234: {
        GREETING: '',
        QUEST: 'Aha, te revoil\xc3\xa0.\x7Avant de commencer, nous devons manger.\x7Apporte-nous du fromage grumeleux pour notre bouillon.\x7Le fromage grumeleux ne se trouve que sur les Cogs Gros Blochons.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Nous avons encore besoin de fromage grumeleux.'},
    5278: {
        GREETING: '',
        QUEST: 'Aha, te revoil\xc3\xa0.\x7Avant de commencer, nous devons manger.\x7Apporte-nous du caviar pour notre bouillon.\x7Le caviar ne se trouve que dans les Cogs M. Hollywood.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Nous avons encore besoin de caviar.'},
    5235: {
        GREETING: '',
        QUEST: "Un homme ordinaire mange avec une cuill\xc3\xa8re ordinaire.\x7Un Cog a pris ma cuill\xc3\xa8re ordinaire, donc je ne peux tout simplement pas manger.\x7Ram\xc3\xa8ne-moi ma cuill\xc3\xa8re, je crois qu'un Pillard l'a prise.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: "J'ai tout simplement besoin de ma cuill\xc3\xa8re."},
    5279: {
        GREETING: '',
        QUEST: "Un homme ordinaire mange avec une cuill\xc3\xa8re ordinaire.\x7Un Cog a pris ma cuill\xc3\xa8re ordinaire, donc je ne peux tout simplement pas manger.\x7Ram\xc3\xa8ne-moi ma cuill\xc3\xa8re, je crois qu'un Chouffleur l'a prise.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: "J'ai tout simplement besoin de ma cuill\xc3\xa8re."},
    5236: {
        GREETING: '',
        QUEST: "Merci beaucoup.\x7Slurp, slurp...\x7Ahhh, maintenant tu dois attraper un crapaud parlant. Essaie d'en p\xc3\xaacher dans la mare.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'O\xc3\xb9 est ce crapaud parlant ?'},
    5237: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Tu n'as pas encore gagn\xc3\xa9 ton dessert.",
        QUEST: "Oh, c'est vraiment un crapaud parlant. Donne-le moi.\x7Qu'est-ce que tu dis, crapaud?\x7Couac.\x7Couac.\x7Le crapaud a parl\xc3\xa9. Nous avons besoin de dessert.\x7Rapporte-nous des c\xc3\xb4nes de glace de chez _toNpcName_.\x7Le crapaud aime la glace aux haricots rouges pour une raison inconnue._where_"},
    5238: {
        GREETING: '',
        QUEST: "Alors c'est le vieillard du blizzard qui t'envoie. Je dois dire qu'on vient de tomber en rupture de stock de c\xc3\xb4nes de glace aux haricots rouges.\x7Tu vois, un groupe de Cogs est venu et les a tous emport\xc3\xa9s.\x7Ils ont dit qu'ils \xc3\xa9taient pour M. Hollywood ou quelque chose comme \xc3\xa7a.\x7Je serais ravi si tu pouvais me les rapporter.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'As-tu d\xc3\xa9j\xc3\xa0 trouv\xc3\xa9 tous mes c\xc3\xb4nes de glace ?'},
    5280: {
        GREETING: '',
        QUEST: "Alors c'est le vieillard du blizzard qui t'envoie. Je dois dire qu'on vient de tomber en rupture de stock de c\xc3\xb4nes de glace aux haricots rouges.\x7Tu vois, un groupe de Cogs est venu et les a tous emport\xc3\xa9s.\x7Ils ont dit qu'ils \xc3\xa9taient pour le Gros Blochon ou quelque chose comme \xc3\xa7a.\x7Je serais ravi si tu pouvais me les rapporter.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'As-tu trouv\xc3\xa9 tous mes c\xc3\xb4nes de glace ?'},
    5239: {
        QUEST: "Merci de m'avoir rapport\xc3\xa9 mes c\xc3\xb4nes de glace!\x7En voil\xc3\xa0 un pour Allan Bic.",
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Tu ferais mieux de porter cette glace \xc3\xa0 Allan Bic avant qu'elle ne fonde."},
    5240: {
        GREETING: '',
        QUEST: "Tr\xc3\xa8s bien. Et voil\xc3\xa0 mon petit crapaud...\x7Slurp, slurp...\x7OK, maintenant nous sommes presque pr\xc3\xaats.\x7Si tu pouvais juste m'apporter de la poudre pour s\xc3\xa9cher mes mains.\x7Je pense que ces Cogs Chouffleurs ont quelquefois de la poudre dans leurs perruques.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'As-tu trouv\xc3\xa9 de la poudre ?'},
    5281: {
        GREETING: '',
        QUEST: "Tr\xc3\xa8s bien. Et voil\xc3\xa0 mon petit crapaud...\x7Slurp, slurp...\x7OK, maintenant nous sommes presque pr\xc3\xaats.\x7Si tu pouvais juste m'apporter de la poudre pour s\xc3\xa9cher mes mains.\x7Je crois que ces Cogs M. Hollywood ont quelquefois de la poudre pour se poudrer le nez.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'As-tu trouv\xc3\xa9 de la poudre ?'},
    5241: {
        QUEST: "OK.\x7Comme je l'ai d\xc3\xa9j\xc3\xa0 dit, pour bien lancer une tarte, tu ne dois pas la lancer avec la main...\x7...mais avec ton \xc3\xa2me.\x7Je ne sais pas ce que cela veut dire, alors je vais m'asseoir et r\xc3\xa9fl\xc3\xa9chir pendant que tu r\xc3\xa9cup\xc3\xa8res des b\xc3\xa2timents.\x7Reviens quand tu as termin\xc3\xa9 ton d\xc3\xa9fi.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Ton d\xc3\xa9fi n'est pas termin\xc3\xa9."},
    5242: {
        GREETING: '',
        QUEST: "Bien que je ne sache toujours pas de quoi je suis en train de parler, tu es vraiment quelqu'un de valeur.\x7Je te donne un dernier d\xc3\xa9fi...\x7Le crapaud parlant voudrait une petite amie.\x7Trouve un autre crapaud parlant. Le crapaud a parl\xc3\xa9.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'O\xc3\xb9 est cet autre crapaud parlant ?',
        COMPLETE: "Houlala! Je suis fatigu\xc3\xa9 par tous ces efforts. Je dois me reposer maintenant.\x7Tiens, prends ta r\xc3\xa9compense et va t'en."},
    5243: {
        QUEST: 'Pierre Lasueur commence \xc3\xa0 empester dans la rue.\x7Peux-tu essayer de le convaincre de prendre une douche par exemple ?_where_'},
    5244: {
        GREETING: '',
        QUEST: "Oui, je crois que je dois commencer \xc3\xa0 transpirer pas mal.\x7Mmmm, peut-\xc3\xaatre que si je pouvais r\xc3\xa9parer ce tuyau qui fuit dans ma douche...\x7Je crois qu'un pignon de l'un de ces tous petits Cogs ferait l'affaire.\x7Va trouver un pignon de Microchef et on va essayer.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'O\xc3\xb9 est ce pignon que tu \xc3\xa9tais parti chercher ?'},
    5245: {
        GREETING: '',
        QUEST: 'Ouaip, on dirait que \xc3\xa7a va.\x7Mais je me sens seul quand je prends ma douche...\x7Pourrais-tu aller me p\xc3\xaacher un canard en plastique pour me tenir compagnie ?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Alors ce canard?'},
    5246: {
        QUEST: "Le canard en plastique est g\xc3\xa9nial, mais...\x7Tous ces b\xc3\xa2timents tout autour me rendent nerveux.\x7Je me sentirais beaucoup plus d\xc3\xa9tendu s'il y avait moins de b\xc3\xa2timents.",
        LEAVING: '',
        COMPLETE: 'Ok, je vais prendre ma douche maintenant. Et voil\xc3\xa0 aussi quelque chose pour toi.',
        INCOMPLETE_PROGRESS: 'Je suis toujours emb\xc3\xaat\xc3\xa9 au sujet des b\xc3\xa2timents.'},
    5251: {
        QUEST: "S\xc3\xa9bastien Toutseul est cens\xc3\xa9 faire un concert ce soir.\x7J'ai entendu dire qu'il pourrait avoir des probl\xc3\xa8mes avec son mat\xc3\xa9riel._where_"},
    5252: {
        GREETING: '',
        QUEST: "Oh ouais! S\xc3\xbbr que j'aurais besoin d'aide.\x7Ces Cogs sont arriv\xc3\xa9s et ont piqu\xc3\xa9 tout mon mat\xc3\xa9riel pendant que je d\xc3\xa9chargeais la camionnette.\x7Tu pourrais me donner un coup de main pour retrouver mon micro?",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'H\xc3\xa9 mon pote, je ne peux pas chanter sans micro.'},
    5253: {
        GREETING: '',
        QUEST: "Ouais, c'est bien mon micro.\x7Merci de me l'avoir rapport\xc3\xa9, mais...\x7J'ai vraiment besoin de mon clavier pour chatouiller les touches.\x7Je crois qu'un de ces Attactics a pris mon clavier.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Alors, mon clavier ?'},
    5273: {
        GREETING: '',
        QUEST: "Ouais, c'est bien mon micro.\x7Merci de me l'avoir rapport\xc3\xa9, mais...\x7J'ai vraiment besoin de mon clavier pour chatouiller les touches.\x7Je crois qu'un de ces Circulateurs a pris mon clavier.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Alors, mon clavier ?'},
    5274: {
        GREETING: '',
        QUEST: "Ouais, c'est bien mon micro.\x7Merci de me l'avoir rapport\xc3\xa9, mais...\x7J'ai vraiment besoin de mon clavier pour chatouiller les touches.\x7Je crois qu'un de ces Usuriers a pris mon clavier.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Alors, mon clavier ?'},
    5275: {
        GREETING: '',
        QUEST: "Ouais, c'est bien mon micro.\x7Merci de me l'avoir rapport\xc3\xa9, mais...\x7J'ai vraiment besoin de mon clavier pour chatouiller les touches.\x7Je crois qu'un de ces Avocageots a pris mon clavier.",
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Alors, mon clavier ?'},
    5254: {
        GREETING: '',
        QUEST: "Tout va bien! Maintenant je peux travailler.\x7Si seulement ils n'avaient pas pris mes chaussures \xc3\xa0 plate-forme...\x7Je parie que mes chaussures sont s\xc3\xbbrement aux pieds d'un M Hollywood.",
        LEAVING: '',
        COMPLETE: "Tout va bien! Je suis pr\xc3\xaat maintenant.\x7Vous \xc3\xaates tous pr\xc3\xaats \xc3\xa0 mettre le feu dans le Glagla ce soir ?\x7Eh? O\xc3\xb9 sont-ils?\x7OK, prends \xc3\xa7a et ram\xc3\xa8ne-moi des fans, d'accord?",
        INCOMPLETE_PROGRESS: 'Je ne peux pas faire mon spectacle pieds nus, si?'},
    5282: {
        GREETING: '',
        QUEST: "Tout va bien! Maintenant je peux travailler.\x7Si seulement ils n'avaient pas pris mes chaussures \xc3\xa0 plate-forme...\x7Je parie que mes chaussures sont aux pieds d'un Gros Blochon.",
        LEAVING: '',
        COMPLETE: "Tout va bien! Je suis pr\xc3\xaat maintenant.\x7Vous \xc3\xaates tous pr\xc3\xaats \xc3\xa0 mettre le feu dans le Glagla ce soir ?\x7Eh? O\xc3\xb9 sont-ils?\x7OK, prends \xc3\xa7a et ram\xc3\xa8ne-moi des fans, d'accord?",
        INCOMPLETE_PROGRESS: 'Je ne peux pas faire mon spectacle pieds nus, si?'},
    5283: {
        GREETING: '',
        QUEST: "Tout va bien! Maintenant je peux travailler.\x7Si seulement ils n'avaient pas pris mes chaussures \xc3\xa0 plate-forme...\x7Je parie que mes chaussures sont aux pieds d'un Pillard.",
        LEAVING: '',
        COMPLETE: "Tout va bien! Je suis pr\xc3\xaat maintenant.\x7Vous \xc3\xaates tous pr\xc3\xaats \xc3\xa0 mettre le feu dans le Glagla ce soir ?\x7Eh? O\xc3\xb9 sont-ils?\x7OK, prends \xc3\xa7a et ram\xc3\xa8ne-moi des fans, d'accord?",
        INCOMPLETE_PROGRESS: 'Je ne peux pas faire mon spectacle pieds nus, si?'},
    5284: {
        GREETING: '',
        QUEST: "Tout va bien! Maintenant je peux travailler.\x7Si seulement ils n'avaient pas pris mes chaussures \xc3\xa0 plate-forme...\x7Je parie que mes chaussures sont aux pieds d'un Chouffleur.",
        LEAVING: '',
        COMPLETE: "Tout va bien! Je suis pr\xc3\xaat maintenant.\x7Vous \xc3\xaates tous pr\xc3\xaats \xc3\xa0 mettre le feu dans le Glagla ce soir ?\x7Eh? O\xc3\xb9 sont-ils?\x7OK, prends \xc3\xa7a et ram\xc3\xa8ne-moi des fans, d'accord?",
        INCOMPLETE_PROGRESS: 'Je ne peux pas faire mon spectacle pieds nus, si?'},
    5255: {
        QUEST: "On dirait que tu as besoin de plus de rigolpoints.\x7Peut-\xc3\xaatre que tu pourrais passer un march\xc3\xa9 avec _toNpcName_.\x7V\xc3\xa9rifie que c'est fait par \xc3\xa9crit..._where_"},
    5256: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Un march\xc3\xa9 est un march\xc3\xa9.',
        QUEST: "Alors comme \xc3\xa7a tu cherches des rigolpoints, hein ?\x7J'ai un march\xc3\xa9 pour toi!\x7Occupe-toi simplement de quelques Cogs Chefbots pour moi...\x7Et je te garantis que tu n'y perdras pas."},
    5276: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Un march\xc3\xa9 est un march\xc3\xa9.',
        QUEST: "Alors comme \xc3\xa7a tu cherches des rigolpoints, hein ?\x7J'ai un march\xc3\xa9 pour toi!\x7Occupe-toi simplement de quelques Cogs Loibots pour moi...\x7Et je te garantis que tu n'y perdras pas."},
    5257: {
        GREETING: '',
        LEAVING: '',
        COMPLETE: "OK, mais je suis s\xc3\xbbr de t'avoir dit de ramasser des Cogs Loibots.\x7Bon, si tu le dis, mais tu m'es redevable.",
        INCOMPLETE_PROGRESS: 'Je ne crois pas que tu aies fini.',
        QUEST: "Tu dis que c'est fait ? Tu as vaincu tous les Cogs?\x7Tu as d\xc3\xbb mal comprendre, notre march\xc3\xa9 portait sur des Cogs Vendibots.\x7Je suis certain de t'avoir dit de me vaincre des Cogs Vendibots."},
    5277: {
        GREETING: '',
        LEAVING: '',
        COMPLETE: "OK, mais je suis s\xc3\xbbr de t'avoir dit de ramasser des Cogs Loibots.\x7Bon, si tu le dis, mais tu m'es redevable.",
        INCOMPLETE_PROGRESS: 'Je ne crois pas que tu aies fini.',
        QUEST: "Tu dis que c'est fait ? Tu as vaincu tous les Cogs?\x7Tu as d\xc3\xbb mal comprendre, notre march\xc3\xa9 portait sur des Cogs Caissbots.\x7Je suis certain de t'avoir dit de me vaincre des Cogs Caissbots."},
    5301: {
        QUEST: "Je ne peux pas t'aider pour les rigolpoints, mais peut-\xc3\xaatre que _toNpcName_ pourra t'arranger.\x7Attention: il est un peu caract\xc3\xa9riel..._where_"},
    5302: {
        GREETING: '',
        LEAVING: '',
        COMPLETE: "Je t'ai dit quoi?!?!\x7Merci bien! Voil\xc3\xa0 ton rigolpoint!",
        INCOMPLETE_PROGRESS: "Salut!\x7Qu'est-ce que tu fais encore l\xc3\xa0?!",
        QUEST: "Un rigolpoint? Je ne crois pas!\x7Sans probl\xc3\xa8me, mais il va d'abord falloir que tu me d\xc3\xa9barrasses de quelques-uns de ces fichus Loibots."},
    5303: {
        QUEST: lTheBrrrgh + " est envahi de Cogs tr\xc3\xa8s dangereux.\x7Si j'\xc3\xa9tais toi, j'irais l\xc3\xa0-bas avec plus de gags.\x7J'ai entendu dire que _toNpcName_ peut te faire un grand sac si tu n'as pas peur de marcher._where_"},
    5304: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Il devrait y avoir plein de Loibots par l\xc3\xa0-bas.\x7Alors, vas-y!',
        QUEST: "Un sac plus grand?\x7Je pourrais s\xc3\xbbrement t'en coudre un en vitesse.\x7Mais je vais avoir besoin de fil.\x7Des Loibots m'ont vol\xc3\xa9 le mien hier matin."},
    5305: {
        GREETING: 'Coucou!',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Va donc chercher quelques Cogs de plus.\x7La couleur n'a pas encore pris.",
        QUEST: "En voil\xc3\xa0 du beau fil!\x7Bon, ce n'est pas ma couleur pr\xc3\xa9f\xc3\xa9r\xc3\xa9e.\x7\xc3\x89coute-moi bien...\x7Tu vas l\xc3\xa0-bas et tu bousilles quelques-uns des Cogs les plus costauds...\x7Et pendant ce temps-l\xc3\xa0, je vais teindre ton fil."},
    5306: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Ils doivent bien \xc3\xaatre quelque part par l\xc3\xa0...',
        QUEST: "Voil\xc3\xa0, le fil est teint. Mais nous avons un petit probl\xc3\xa8me.\x7Je n'arrive pas \xc3\xa0 trouver mes aiguilles \xc3\xa0 tricoter.\x7La derni\xc3\xa8re fois que je les ai vues, c'\xc3\xa9tait pr\xc3\xa8s de la mare."},
    5307: {
        GREETING: '',
        LEAVING: 'Merci beaucoup!',
        INCOMPLETE_PROGRESS: "Rome ne s'est pas tricot\xc3\xa9 en un jour!",
        QUEST: 'Ce sont bien mes aiguilles.\x7Pendant que je tricote, va faire un peu de nettoyage de Cogs dans ces grands b\xc3\xa2timents.',
        COMPLETE: 'Excellent travail!\x7Et en parlant de bon travail...\x7Voil\xc3\xa0 ton nouveau sac!'},
    5308: {
        GREETING: '',
        LEAVING: '',
        QUEST: "J'ai entendu dire que _toNpcName_ a des probl\xc3\xa8mes avec la justice.\x7Est-ce que tu pourrais aller le voir et lui demander?_where_"},
    5309: {
        GREETING: 'Je suis content de te voir...',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'D\xc3\xa9p\xc3\xaache-toi! La rue en est envahie!',
        QUEST: "Les Loibots ont vraiment pris le pouvoir dans le quartier.\x7J'ai bien peur qu'ils ne me tra\xc3\xaenent en justice.\x7Tu pourrais pas les faire d\xc3\xa9gager de cette rue?"},
    5310: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Je crois que je les entends qui viennent me chercher...',
        QUEST: 'Merci. Je me sens un peu mieux.\x7 Mais il y a autre chose...\x7Est-ce que tu pourrais passer chez _toNpcName_ pour me trouver un alibi?_where_'},
    5311: {
        GREETING: 'HOUAAA!!!',
        LEAVING: '',
        INCOMPLETE_PROGRESS: "Je ne peux pas l'aider si tu n'en trouves pas!",
        QUEST: "Un alibi?! G\xc3\xa9nial!\x7Tu n'en as pas une autre comme \xc3\xa7a?\x7Je parie qu'un Avocageot aurait..."},
    5312: {
        GREETING: 'Enfin!',
        LEAVING: '',
        INCOMPLETE_PROGRESS: '',
        COMPLETE: "Houlala! Je suis vraiment soulag\xc3\xa9 d'avoir \xc3\xa7a.\x7Voil\xc3\xa0 ta r\xc3\xa9compense...",
        QUEST: 'Super! Tu ferais mieux de rapporter \xc3\xa7a en vitesse \xc3\xa0 _toNpcName_!'},
    6201: {
        QUEST: "Ali Mentation a besoin d'aide. Peux-tu y faire un saut et lui donner un coup de main ?_where_"},
    6202: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Oh, un client! Super! Que puis-je faire pour toi?\x7Comment \xc3\xa7a, que peux-tu faire pour moi? OH! Tu n'es pas un client.\x7Je m'en souviens maintenant. Tu es l\xc3\xa0 pour m'aider avec ces affreux Cogs.\x7Eh bien, ton aide me sera certainement bien utile, m\xc3\xaame si tu n'es pas un client.\x7Si tu nettoies un peu les rues, je te r\xc3\xa9serve un petit quelque chose.",
        INCOMPLETE_PROGRESS: "Si tu ne veux pas d'\xc3\xa9lectricit\xc3\xa9, je ne peux rien faire pour toi tant que tu n'as pas vaincu ces Cogs.",
        COMPLETE: "Bon boulot avec ces Cogs, _avName_.\x7Tu es vraiment s\xc3\xbbr(e) que tu n'as pas besoin d'\xc3\xa9lectricit\xc3\xa9? \xc3\x87a pourrait t'\xc3\xaatre utile...\x7Non ? OK, comme tu voudras.\x7Quoi? Ah oui, je me souviens. Et voil\xc3\xa0. \xc3\x87a te sera s\xc3\xbbrement utile contre ces m\xc3\xa9chants Cogs.\x7Continue \xc3\xa0 bien travailler!"},
    6206: {
        QUEST: "Eh bien, _avName_, je n'ai rien pour toi pour le moment.\x7Attends! Je crois que Susan Sieste cherchait de l'aide. Pourquoi n'irais-tu pas la voir ?_where_"},
    6207: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Je ne serai jamais riche avec ces satan\xc3\xa9s Cogs qui ruinent mes affaires!\x7Il faut que tu m'aides, _avName_.\x7Nettoie quelques b\xc3\xa2timents Cog pour le bien de tout le voisinage et je te rendrai plus riche.",
        INCOMPLETE_PROGRESS: 'Pauvre de moi! Tu ne peux pas te d\xc3\xa9barrasser de ces b\xc3\xa2timents?',
        COMPLETE: "\xc3\x80 moi la fortune! Je vois \xc3\xa7a d'ici!\x7Je passerai tout mon temps \xc3\xa0 la p\xc3\xaache. Maintenant, laisse-moi t'enrichir un peu.\x7Et voil\xc3\xa0!"},
    6211: {
        QUEST: "H\xc3\xa9 _avName_! J'ai entendu dire que Linda Kapok te cherchait.\x7Tu devrais passer lui rendre visite._where_"},
    6212: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Bonjour! Waouh, ce que je suis contente de te voir!\x7J'ai pass\xc3\xa9 mon temps \xc3\xa0 r\xc3\xa9parer ce r\xc3\xa9pondeur pendant mon temps libre mais il me manque des pi\xc3\xa8ces.\x7J'ai besoin de trois tiges suppl\xc3\xa9mentaires et celles des Pince Menus ont l'air de bien marcher.\x7Pourrais-tu m'en trouver quelques-unes?",
        INCOMPLETE_PROGRESS: 'Toujours en train de chercher ces tiges?'},
    6213: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Oh, ces tiges iront tr\xc3\xa8s bien.\x7C'est dr\xc3\xb4le. J'\xc3\xa9tais s\xc3\xbbre d'avoir une courroie de rechange quelque part mais je n'arrive pas \xc3\xa0 la trouver.\x7Pourrais-tu m'en rapporter une de chez Sacasous, s'il te pla\xc3\xaet ? Merci!",
        INCOMPLETE: "Non, je ne peux pas t'aider avant d'avoir cette courroie."},
    6214: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Voil\xc3\xa0, c'est \xc3\xa7a. Maintenant \xc3\xa7a devrait marcher comme sur des roulettes.\x7O\xc3\xb9 sont pass\xc3\xa9es mes pinces? Je ne peux pas fixer \xc3\xa7a sans mes pinces.\x7Peut-\xc3\xaatre qu'une tenaille de Radino ferait l'affaire ?\x7Si tu vas m'en chercher une, je te donnerai un petit quelque chose qui t'aidera contre les Cogs.",
        INCOMPLETE_PROGRESS: 'Toujours pas de tenaille, hein ? Continue \xc3\xa0 chercher.',
        COMPLETE: "G\xc3\xa9nial! Maintenant il ne me reste plus qu'\xc3\xa0 fixer tout \xc3\xa7a.\x7\xc3\x87a a l'air de marcher maintenant. Me voil\xc3\xa0 de retour aux affaires!\x7Euh, sauf que nous n'avons pas de t\xc3\xa9l\xc3\xa9phone. Mais merci quand m\xc3\xaame de ton aide.\x7Je pense que \xc3\xa7a t'aidera contre les Cogs. Bonne chance!"},
    6221: {
        QUEST: "J'ai entendu dire que Rocco avait besoin d'aide. Va voir ce que tu peux faire pour lui._where_"},
    6222: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Yo! Tu tombes \xc3\xa0 pic. Moi, \xc3\xa7a va pas mieux.\x7Ouais, j'aurais besoin d'un coup de main avec ces Cogs. Ils sont tout le temps l\xc3\xa0, \xc3\xa0 essayer de me donner des le\xc3\xa7ons.\x7Si tu pouvais mettre hors d'\xc3\xa9tat de nuire certains de ces Chefbots, je f'rais en sorte que t'aies pas perdu ton temps.",
        INCOMPLETE_PROGRESS: "Eh, _avName_, qu'est-ce que tu fiches?\x7Faut qu'tu fasses la chasse \xc3\xa0 ces Chefbots. On a un accord, tu te rappelles?\x7Rocco tient toujours sa parole.",
        COMPLETE: "Yo, _avName_! Toi, t'es OK pour moi.\x7Ces Chefbots ils font moins les malins maintenant, pas vrai?\x7Eh voil\xc3\xa0! Un bon petit coup de boost. Maintenant, \xc3\xa9vite les ennuis, t'entends?"},
    6231: {
        QUEST: "Place de la couette, Plume a entendu des rumeurs \xc3\xa0 propos du quartier g\xc3\xa9n\xc3\xa9ral Caissbot.\x7Va y faire un tour et vois si tu peux l'aider._where_"},
    6232: {
        GREETING: '',
        LEAVING: '',
        QUEST: "J'ai entendu dire qu'il se passait de dr\xc3\xb4les de choses.\x7Bon, c'est peut-\xc3\xaatre un coup des puces mais il se passe quelque chose de toute fa\xc3\xa7on.\x7Tous ces Caissbots!\x7IJe pense qu'ils ont install\xc3\xa9 un nouveau quartier g\xc3\xa9n\xc3\xa9ral tout pr\xc3\xa8s de la Place de la Couette.\x7P.J. conna\xc3\xaet bien le coin.\x7Va voir _toNpcName_ _where_ Demande-lui s'il a entendu quelque chose.",
        INCOMPLETE_PROGRESS: "Tu n'as pas encore vu P.J.? Qu'est-ce qui t'en emp\xc3\xaache ?\x7Ah, ces satan\xc3\xa9es puces!"},
    6233: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Salut _avName_, o\xc3\xb9 vas-tu?\x7Un quartier g\xc3\xa9n\xc3\xa9ral Caissbot ?? Je n'ai rien vu.\x7Tu pourrais aller au bout de la place de la Couette et voir si c'est vrai?\x7Trouve quelques Caissbots dans leur quartier g\xc3\xa9n\xc3\xa9ral, bats-en quelques-uns et reviens me le dire.",
        INCOMPLETE_PROGRESS: "Pas encore trouv\xc3\xa9 le QG? Tu dois y aller, vaincre des Caissbots et voir ce qui s'y passe."},
    6234: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Quoi?! Il y a D\xc3\x89J\xc3\x80 un QG Caissbot ?\x7Tu ferais mieux d'aller tout de suite le dire \xc3\xa0 Plume!\x7Qui aurait pu deviner qu'il y aurait un QG Cog \xc3\xa0 deux pas de sa rue ?",
        INCOMPLETE_PROGRESS: "Qu'est-ce que Plume t'a dit ? Tu ne l'as pas encore vu?"},
    6235: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Je suis impatient de savoir ce que P.J. a dit.\x7Hmm... on a besoin de plus d'informations sur cette affaire de Cogs mais je dois me d\xc3\xa9barrasser de ces puces!\x7Je sais! TOI, tu peux essayer d'en savoir plus!\x7Va vaincre des Caissbots au QG jusqu'\xc3\xa0 ce que tu trouves des plans. Apr\xc3\xa8s, tu reviens me voir!",
        INCOMPLETE_PROGRESS: 'Toujours pas de plans? Continue \xc3\xa0 chercher les Cogs!\x7Ils doivent avoir des plans!',
        COMPLETE: "Tu as les plans?\x7G\xc3\xa9nial! Voyons voir ce qu'ils disent.\x7Je vois... Les Caissbots ont construit une Fabrique \xc3\xa0 Sous pour fabriquer des euros Cog.\x7\xc3\x87a doit \xc3\xaatre PLEIN de Caissbots. On devrait essayer d'en savoir plus.\x7Peut-\xc3\xaatre que si tu avais un d\xc3\xa9guisement... Hmmm... attends! Je crois que j'ai une pi\xc3\xa8ce de costume de Cog quelque part par l\xc3\xa0....\x7La voil\xc3\xa0! Prends-la en r\xc3\xa9compense de tes efforts! Merci encore de ton aide!"},
    6241: {
        QUEST: "La comtesse te cherchait partout! S'il te pla\xc3\xaet, va lui rendre visite, comme \xc3\xa7a elle arr\xc3\xaatera d'appeler._where_"},
    6242: {
        GREETING: '',
        LEAVING: '',
        QUEST: "_avName_, je compte sur toi pour m'aider!\x7Tu vois, ces Cogs font tellement de bruit que je ne peux tout simplement pas me concentrer.\x7Je n'arr\xc3\xaate pas de perdre le compte de mes moutons!\x7Si tu fais diminuer ce bruit, je t'aiderai aussi! Tu peux compter l\xc3\xa0-dessus!\x7Bon, o\xc3\xb9 en \xc3\xa9tais-je ? C'est \xc3\xa7a, cent trente-six, cent trente-sept...",
        INCOMPLETE_PROGRESS: "Quatre cent quarante-deux... quatre cent quarante-trois...\x7Quoi? Tu es d\xc3\xa9j\xc3\xa0 de retour ? Mais il y a toujours trop de bruit!\x7Ah non, j'ai encore perdu le compte.\x7 Un...deux...trois...",
        COMPLETE: "Cinq cent quatre-vingt-treize... cinq cent quatre-vingt-quatorze..\x7Hello! Ah, je savais que je pouvais compter sur toi! C'est beaucoup plus calme maintenant.\x7Et voil\xc3\xa0, pour tous ces Gobechiffres.\x7Le nombre ? Maintenant il faut que je recommence \xc3\xa0 compter depuis le d\xc3\xa9but! Un...deux...."},
    6251: {
        QUEST: 'Ce pauvre p\xc3\xa8re San a cass\xc3\xa9 son zipper et maintenant il ne peut plus livrer ses clients. Ton aide lui sera certainement utile._where_'},
    6252: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Oh, bonjour _avName_. Tu es l\xc3\xa0 pour m'aider \xc3\xa0 faire mes livraisons?\x7C'est g\xc3\xa9nial! Avec ce zipper cass\xc3\xa9, c'est difficile de se d\xc3\xa9placer.\x7Voyons voir... OK, \xc3\xa7a devrait \xc3\xaatre facile. Ron Chonneau a command\xc3\xa9 une cithare la semaine derni\xc3\xa8re.\x7Pourrais-tu la lui apporter ? _where_",
        INCOMPLETE_PROGRESS: 'Ah, salut! Tu as oubli\xc3\xa9 quelque chose ? Ron Chonneau attend sa cithare.'},
    6253: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Ma cithare! Enfin! Bon sang, je suis impatient d'en jouer.\x7Va dire au p\xc3\xa8re San que je le remercie, tu veux?",
        INCOMPLETE_PROGRESS: "Merci encore pour la cithare. Le p\xc3\xa8re San n'a pas d'autres livraisons pour toi?"},
    6254: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Quelle rapidit\xc3\xa9! Quelle est la prochaine livraison sur ma liste ?\x7Bon. Mike Mac a command\xc3\xa9 une surfaceuse. Quel dr\xc3\xb4le de type.\x7Tu peux la lui apporter, s'il te pla\xc3\xaet ?_where_",
        INCOMPLETE_PROGRESS: 'Cette surfaceuse est pour Mike Mac._where_'},
    6255: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Super! La surfaceuse que j'avais command\xc3\xa9e!\x7Maintenant, si seulement il n'y avait pas autant de Cogs dans les environs, je pourrais avoir le temps de m'en servir.\x7Sois sympa et occupe-toi de certains de ces Caissbots pour moi, tu veux?",
        INCOMPLETE_PROGRESS: "Ces Caissbots r\xc3\xa9sistent, hein ? Avec eux, pas facile d'essayer ma surfaceuse."},
    6256: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Excellent! Maintenant je peux essayer ma surfaceuse.\x7S'il te pla\xc3\xaet, dis au p\xc3\xa8re San que je viendrai la semaine prochaine passer ma prochaine commande.",
        INCOMPLETE_PROGRESS: "C'est tout ce dont j'ai besoin pour le moment. Est-ce que le p\xc3\xa8re San n'est pas en train de t'attendre ?"},
    6257: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Alors, est-ce que Mike Mac a \xc3\xa9t\xc3\xa9 content de sa surfaceuse ? G\xc3\xa9nial.\x7\xc3\x80 qui le tour ? Ah, Olivier Daure a command\xc3\xa9 un coussin z\xc3\xa8bre.\x7Le voil\xc3\xa0! Pourrais-tu faire un saut chez lui, s'il te pla\xc3\xaet ?_where_",
        INCOMPLETE_PROGRESS: "Je crois qu'Olivier Daure a besoin de ce coussin pour m\xc3\xa9diter."},
    6258: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Ah, mon coussin, enfin. Maintenant je peux m\xc3\xa9diter.\x7Comment se concentrer avec un tel vacarme ? Tous ces Cogs!\x7Comme tu es l\xc3\xa0, peut-\xc3\xaatre que tu pourrais t'occuper de certains de ces Cogs?\x7Apr\xc3\xa8s \xc3\xa7a je pourrai utiliser mon coussin en paix.",
        INCOMPLETE_PROGRESS: 'Il y a toujours tellement de bruit avec ces Cogs! Comment se concentrer ?'},
    6259: {
        GREETING: '',
        LEAVING: '',
        QUEST: "La paix et le calme, enfin. Merci, _avName_.\x7S'il te pla\xc3\xaet, va dire au p\xc3\xa8re San que je suis tr\xc3\xa8s content. OMMM....",
        INCOMPLETE_PROGRESS: "Le p\xc3\xa8re San t'as appel\xc3\xa9. Tu devrais aller voir ce qu'il veut."},
    6260: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Je suis heureux de voir qu'Olivier Daure est content de son coussin z\xc3\xa8bre.\x7Oh, ces zinnias viennent juste d'arriver pour Eva Sandor-Mir.\x7Comme tu as l'air d'\xc3\xaatre un livreur z\xc3\xa9l\xc3\xa9, peut-\xc3\xaatre que tu pourrais les lui apporter ?_where_",
        INCOMPLETE_PROGRESS: 'Ces zinnias vont faner si tu ne les livres pas rapidement.'},
    6261: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Quels jolis zinnias! Ca c'est s\xc3\xbbr, le p\xc3\xa8re San s'y conna\xc3\xaet en livraison.\x7Oh, eh bien, je suppose que c'est TOI qui fais les livraisons, _avName_. Tu remercieras le p\xc3\xa8re San pour moi!",
        INCOMPLETE_PROGRESS: "N'oublie pas de remercier le p\xc3\xa8re San pour les zinnias!"},
    6262: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Te voil\xc3\xa0 de retour, _avName_. Tu es sacr\xc3\xa9ment rapide.\x7Voyons... Quelle est la prochaine livraison sur ma liste ? Des disques de Zydeco pour Th\xc3\xa9r\xc3\xa8se Eveill\xc3\xa9._where_',
        INCOMPLETE_PROGRESS: 'Je suis s\xc3\xbbr que Th\xc3\xa9r\xc3\xa8se Eveill\xc3\xa9 attend ses disques de Zydeco.'},
    6263: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Des disques de Zydeco? Je ne me rappelle pas avoir command\xc3\xa9 de disques de Zydeco.\x7Oh, je parie que c'est Lou Laberceuse qui les a command\xc3\xa9s._where_",
        INCOMPLETE_PROGRESS: 'Non, ces disques de Zydeco sont pour Lou Laberceuse._where_'},
    6264: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Ah, enfin, mes disques de Zydeco! Je pensais que le p\xc3\xa8re San avait oubli\xc3\xa9.\x7Pourrais-tu lui apporter cette courgette ? Il trouvera bien quelqu'un qui en veut une. Merci!",
        INCOMPLETE_PROGRESS: "Oh, j'ai d\xc3\xa9j\xc3\xa0 plein de courgettes. Apporte-la au p\xc3\xa8re San."},
    6265: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Une courgette ? Hmm. Eh bien, je trouverai s\xc3\xbbrement quelqu'un qui en voudra.\x7OK, nous avons presque fini ma liste. Plus qu'une livraison \xc3\xa0 faire.\x7B\xc3\xa9b\xc3\xa9 MacDougal a command\xc3\xa9 un costume zazou._where_",
        INCOMPLETE_PROGRESS: 'Si tu ne livres pas ce costume zazou \xc3\xa0 B\xc3\xa9b\xc3\xa9 MacDougal,\x7 il va \xc3\xaatre tout froiss\xc3\xa9.'},
    6266: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Il \xc3\xa9tait une fois... oh! Tu n'es pas l\xc3\xa0 pour \xc3\xa9couter une histoire, hein ?\x7Tu es l\xc3\xa0 pour me livrer mon costume zazou? Super! Waouh, c'est quelque chose.\x7Eh, tu pourrais transmettre un message au p\xc3\xa8re San pour moi? J'aurais besoin de boutons de manchette en zircon pour aller avec le costume. Merci!",
        INCOMPLETE_PROGRESS: 'Tu as transmis mon message au p\xc3\xa8re San ?',
        COMPLETE: "Des boutons de manchette en zircon, hein ? Eh bien, je vais voir ce que je peux faire pour lui.\x7Bon, tu m'as \xc3\xa9t\xc3\xa9 d'une aide pr\xc3\xa9cieuse et je ne peux pas te laisser partir sans rien.\x7Voici un GROS coup de boost pour t'aider \xc3\xa0 zapper ces Cogs!"},
    6271: {
        QUEST: "Dave Bigleau a des probl\xc3\xa8mes et tu peux peut-\xc3\xaatre l'aider. Pourquoi ne pas passer \xc3\xa0 sa boutique ?_where_"},
    6272: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Quoi? Hein ? Oh, j'ai d\xc3\xbb m'endormir.\x7Tu sais, ces b\xc3\xa2timents Cog sont remplis de machines qui me donnent vraiment sommeil.\x7Je les entends ronronner toute la journ\xc3\xa9e et...\x7Hein ? Ah, ouais, d'accord. Si tu pouvais te d\xc3\xa9barrasser de certains de ces b\xc3\xa2timents Cog, je pourrais rester \xc3\xa9veill\xc3\xa9.",
        INCOMPLETE_PROGRESS: "Zzzzz...hein ? Oh, c'est toi, _avName_.\x7D\xc3\xa9j\xc3\xa0 de retour ? Je faisais juste une petite sieste.\x7Reviens quand tu en auras fini avec ces b\xc3\xa2timents.",
        COMPLETE: 'Quoi? Je me suis juste assoupi une minute.\x7Maintenant que ces b\xc3\xa2timents Cog ont disparu, je peux enfin me d\xc3\xa9tendre.\x7Merci de ton aide, _avName_.\x7A plus tard! Je crois que je vais faire un petit somme.'},
    6281: {
        QUEST: 'Va voir Teddy Blaireau. Il a un boulot pour toi._where_'},
    6282: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Qu'est-ce que tu dis? Non, je n'ai pas de goulot pour toi.\x7Oh, un boulot! Pourquoi ne pas l'avoir dit plus t\xc3\xb4t ? Il faudrait que tu parles plus fort.\x7Avec ces Cogs, ce n'est pas facile d'hiberner. Si tu ram\xc3\xa8nes un peu de calme au Pays des R\xc3\xaaves,\x7je te donnerai un petit quelque chose.",
        INCOMPLETE_PROGRESS: "Tu as vaincu les bogs? Quels bogs?\x7Oh, les Cogs! Pourquoi ne pas l'avoir dit plus t\xc3\xb4t ?\x7Hmm, il y a encore pas mal de bruit. Pourquoi ne pas en vaincre quelques autres?",
        COMPLETE: "Tu t'es bien amus\xc3\xa9? Hein ? Oh!\x7Tu as fini! Super. C'est sympa de ta part de donner un coup de main comme \xc3\xa7a.\x7J'ai trouv\xc3\xa9 \xc3\xa7a dans la pi\xc3\xa8ce du fond mais \xc3\xa7a ne m'est d'aucune utilit\xc3\xa9.\x7Peut-\xc3\xaatre que tu pourras en faire quelque chose. \xc3\x80 plus, _avName_!"},
    6291: {
        QUEST: "Les Cogs ont p\xc3\xa9n\xc3\xa9tr\xc3\xa9 dans la Banque du Doudou d'Or! Va voir Laurent Lauronpat et vois si tu peux l'aider."},
    6292: {
        QUEST: "Ah ces satan\xc3\xa9s Caissbots! Ils ont vol\xc3\xa9 mes lampes de lecture!\x7J'en ai besoin tout de suite. Tu peux aller les chercher ?\x7Si tu me rapportes mes lampes de lecture, je pourrai peut-\xc3\xaatre t'aider \xc3\xa0 rencontrer le Vice-Pr\xc3\xa9sident.\x7Fais vite!",
        INCOMPLETE_PROGRESS: 'Il me faut ces lampes. Continue de les chercher!',
        COMPLETE: 'Te voil\xc3\xa0 revenu! Et tu as mes lampes!\x7Je ne peux pas te remercier comme il le faudrait mais je peux te donner \xc3\xa7a.'},
    7201: {
        QUEST: "Nina Lamparo te cherchait, _avName_. Elle a besoin d'aide._where_"},
    7202: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Ah! Je suis si contente de te voir, _avName_. J'aurais bien besoin d'aide!\x7Ces fichus Cogs ont chass\xc3\xa9 les livreurs et je n'ai plus aucun lit en stock.\x7Peux-tu aller voir Am\xc3\xa9d\xc3\xa9 Brouilletoitoutseul et me rapporter un lit ?_where_",
        INCOMPLETE_PROGRESS: "Am\xc3\xa9d\xc3\xa9 n'avait pas de lit ? J'\xc3\xa9tais s\xc3\xbbre qu'il en avait un.",
        COMPLETE: ''},
    7203: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Un lit ? Bien s\xc3\xbbr, en voil\xc3\xa0 un de pr\xc3\xaat.\x7Apporte-le-lui pour boi, tu veux? Tu as compris? Pour \x7" BOIS "? Hi-hi!\x7Tr\xc3\xa8s dr\xc3\xb4le, non ? Eh bien, am\xc3\xa8ne-le quand m\xc3\xaame l\xc3\xa0-bas s\'il te pla\xc3\xaet.',
        INCOMPLETE_PROGRESS: 'Est-ce que le lit a plu \xc3\xa0 Nina?',
        COMPLETE: ''},
    7204: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Ce lit ne convient pas. Il est beaucoup trop ordinaire.\x7Va voir s'il a quelque chose de plus fantaisie, tu veux?\x7Je suis s\xc3\xbbre que \xc3\xa7a ne te prendra qu'une minute.",
        INCOMPLETE_PROGRESS: "Je suis s\xc3\xbbre qu'Am\xc3\xa9d\xc3\xa9 a un lit plus fantaisie.",
        COMPLETE: ''},
    7205: {
        GREETING: '',
        LEAVING: '',
        QUEST: "On n'est pas tomb\xc3\xa9 pile avec ce lit, hein ? J'en ai un ici qui devrait faire l'affaire.\x7Mais il y a un petit probl\xc3\xa8me - il faut d'abord l'assembler.\x7Pendant que je m'en charge avec mon marteau, pourrais-tu te d\xc3\xa9barrasser de certains des Cogs, l\xc3\xa0-dehors?\x7Ces affreux Cogs ruinent mon travail.\x7Reviens quand tu auras fini et le lit sera pr\xc3\xaat.",
        INCOMPLETE_PROGRESS: "Je n'ai pas tout \xc3\xa0 fait fini d'assembler le lit.\x7Quand tu en auras fini avec les Cogs, il sera pr\xc3\xaat.",
        COMPLETE: ''},
    7206: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Salut _avName_!\x7Tu as fait du sacr\xc3\xa9 bon boulot avec ces Cogs.\x7Le lit est pr\xc3\xaat. Pourrais-tu le livrer pour moi?\x7Maintenant que tous ces Cogs sont partis, les affaires vont reprendre!',
        INCOMPLETE_PROGRESS: 'Je pense que Nina attend la livraison de ce lit.',
        COMPLETE: "Quel joli lit!\x7Maintenant mes clients vont \xc3\xaatre contents. Merci, _avName_.\x7Tiens, ceci pourra peut-\xc3\xaatre t'\xc3\xaatre utile. Quelqu'un l'a laiss\xc3\xa9 ici."},
    7209: {
        QUEST: "Va voir Ros\xc3\xa9e de Lune. Elle a besoin d'aide._where_"},
    7210: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Oh! Comme je suis contente de te voir, _avName_. J'ai vraiment besoin d'aide!\x7Je n'ai pas eu mon compte de sommeil depuis bien longtemps. Tu vois, les Cogs m'ont vol\xc3\xa9 mon dessus-de-lit.\x7Tu pourrais faire un saut voir si Ed n'aurait rien dans les tons bleus?_where_",
        INCOMPLETE_PROGRESS: "Qu'est-ce qu'Ed a dit \xc3\xa0 propos de ce dessus-de-lit bleu?",
        COMPLETE: ''},
    7211: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Alors comme \xc3\xa7a, Ros\xc3\xa9e veut un dessus-de-lit, hein ?\x7De quelle couleur ? BLEU?!\x7Eh bien, je vais devoir le fabriquer sp\xc3\xa9cialement pour elle. Tout ce que j'ai, c'est du rouge.\x7Tu sais quoi? Si tu vas t'occuper de certains des Cogs l\xc3\xa0-dehors, je fabriquerai un dessus-de-lit bleu sp\xc3\xa9cialement pour elle.\x7Des dessus-de-lit bleus... et puis quoi encore ?",
        INCOMPLETE_PROGRESS: "Je travaille toujours sur ce dessus-de-lit bleu, _avName_. Continue de t'occuper de ces Cogs!",
        COMPLETE: ''},
    7212: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Content de te revoir. J'ai quelque chose pour toi!\x7Voil\xc3\xa0 le dessus-de-lit et il est bleu. Elle va l'adorer.",
        INCOMPLETE_PROGRESS: 'Est-ce que Ros\xc3\xa9e a aim\xc3\xa9 le dessus-de-lit ?',
        COMPLETE: ''},
    7213: {
        GREETING: '',
        LEAVING: '',
        QUEST: "C'est mon dessus-de-lit ? Non, \xc3\xa7a ne va pas.\x7C'est un tissu \xc3\x89COSSAIS! Qui pourrait dormir avec un motif aussi CRIARD?\x7Tu vas devoir le rapporter et m'en ramener un autre.\x7Je suis s\xc3\xbbre qu'il en a d'autres.",
        INCOMPLETE_PROGRESS: "Il est hors de question que j'accepte un dessus-de-lit \xc3\xa9cossais. Va voir ce qu'Ed peut faire.",
        COMPLETE: ''},
    7214: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Quoi? Elle n'aime pas l'\xc3\x89COSSAIS?\x7Hmm... Voyons ce que nous avons par ici.\x7\xc3\x87a va prendre un certain temps. Pourquoi tu n'irais pas t'occuper de quelques Cogs pendant que j'essaie de trouver autre chose ?\x7J'aurai trouv\xc3\xa9 quand tu reviendras.",
        INCOMPLETE_PROGRESS: 'Je suis toujours en train de chercher un autre dessus-de-lit. Comment \xc3\xa7a se passe avec les Cogs?',
        COMPLETE: ''},
    7215: {
        GREETING: '',
        LEAVING: '',
        QUEST: "H\xc3\xa9, bon travail avec ces Cogs!\x7Et voil\xc3\xa0, il est bleu et il n'est pas \xc3\xa9cossais.\x7Reste \xc3\xa0 esp\xc3\xa9rer qu'elle aime le cachemire.\x7Apporte ce dessus-de-lit \xc3\xa0 Ros\xc3\xa9e.",
        INCOMPLETE_PROGRESS: "C'est tout ce que j'ai pour toi pour l'instant.\x7S'il te pla\xc3\xaet, va apporter ce dessus-de-lit \xc3\xa0 Ros\xc3\xa9e.",
        COMPLETE: "Oh! Que c'est joli! Le cachemire me va vraiment bien.\x7Il est temps pour moi de prendre un peu de repos! \xc3\x80 plus tard, _avName_.\x7Quoi? Tu es encore l\xc3\xa0? Tu ne vois pas que j'essaie de dormir ?\x7Tiens, prends \xc3\xa7a et laisse-moi me reposer. Je dois \xc3\xaatre \xc3\xa0 faire peur!"},
    7218: {
        QUEST: "Daphn\xc3\xa9 Puis\xc3\xa9 aurait bien besoin d'un coup de main._where_"},
    7219: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Oh, _avName_, je suis contente de te voir! Les Cogs ont pris mes oreillers.\x7Pourrais-tu aller voir si Pierrot en a?_where_\x7Je suis s\xc3\xbbre qu'il peut m'aider.",
        INCOMPLETE_PROGRESS: 'Est-ce que Pierrot a des oreillers pour moi ?',
        COMPLETE: ''},
    7220: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Salut! Daphn\xc3\xa9 a besoin d'oreillers, hein ? Eh bien, tu as frapp\xc3\xa9 \xc3\xa0 la bonne porte, partenaire!\x7Il y a plus d'oreillers ici que d'\xc3\xa9pines sur un cactus.\x7Et voil\xc3\xa0, _avName_. Apporte-les \xc3\xa0 Daphn\xc3\xa9, avec mes compliments.\x7Toujours heureux de donner un coup de main \xc3\xa0 une demoiselle.",
        INCOMPLETE_PROGRESS: 'Ces oreillers sont-ils assez doux pour cette jeune dame ?',
        COMPLETE: ''},
    7221: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Tu as les oreillers! G\xc3\xa9nial!\x7Eh, attends une seconde! Ces oreillers sont affreusement mous.\x7Beaucoup trop mous pour moi. J'ai besoin d'oreillers plus durs.\x7Ram\xc3\xa8ne-les \xc3\xa0 Pierrot et vois ce qu'il a d'autre. Merci.",
        INCOMPLETE_PROGRESS: "Non! Trop mous. Demande d'autres oreillers \xc3\xa0 Pierrot.",
        COMPLETE: ''},
    7222: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Trop mous, hein ? Eh bien, laisse-moi voir ce que j'ai d'autre....\x7Hmm... Il me semblait que j'avais un bon paquet d'oreillers durs. O\xc3\xb9 sont-ils pass\xc3\xa9s?\x7Oh! Je me rappelle. Je pensais les renvoyer, donc ils sont \xc3\xa0 l'entrep\xc3\xb4t.\x7Pourquoi tu ne nettoierais pas quelques b\xc3\xa2timents Cog l\xc3\xa0-dehors pendant que je les sors de l'entrep\xc3\xb4t, partenaire ?",
        INCOMPLETE_PROGRESS: "Dur, dur les b\xc3\xa2timents Cog. C'est pas comme ces oreillers.\x7Continue \xc3\xa0 chercher.",
        COMPLETE: ''},
    7223: {
        GREETING: '',
        LEAVING: '',
        QUEST: "D\xc3\xa9j\xc3\xa0 de retour ? Eh bien, c'est parfait. Tu vois, j'ai trouv\xc3\xa9 les oreillers que Daphn\xc3\xa9 voulait.\x7Maintenant, va les lui apporter. Ils sont tellement durs qu'on s'y casserait les dents!",
        INCOMPLETE_PROGRESS: "Ouais, ces oreillers sont bien durs. J'esp\xc3\xa8re qu'ils plairont \xc3\xa0 Daphn\xc3\xa9.",
        COMPLETE: "Je savais bien que Pierrot aurait des oreillers plus durs.\x7Ah oui, ils sont parfaits. Bien durs, juste comme je les aime.\x7Tu aurais besoin de cette pi\xc3\xa8ce de costume de Cog? Tu n'as qu'\xc3\xa0 la prendre."},
    7226: {
        QUEST: 'Passe voir Sandie Marchand. Elle a perdu son pyjama._where_'},
    7227: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Je n'ai plus de pyjama! Je ne le trouve plus!\x7Qu'est-ce que je vais faire ? Oh! Je sais!\x7Va voir Big Mama. Elle aura s\xc3\xbbrement un pyjama pour moi._where_",
        INCOMPLETE_PROGRESS: 'Est-ce que Big Mama a un pyjama pour moi?',
        COMPLETE: ''},
    7228: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Te voil\xc3\xa0, petit Toon! Big Mama a les plus beaux pyjamas des Bahamas.\x7Oh, quelque chose pour Sandie Marchand, hein ? Bon, voyons voir ce que j'ai.\x7Voil\xc3\xa0 un petit quelque chose. Maintenant elle peut dormir en toute \xc3\xa9l\xc3\xa9gance!\x7Voudrais-tu courir le lui apporter pour moi? Je ne peux pas quitter la boutique pour l'instant.\x7Merci, _avName_. \xc3\x80 plus tard!",
        INCOMPLETE_PROGRESS: 'Tu dois apporter ce pyjama \xc3\xa0 Sandie._where_',
        COMPLETE: ''},
    7229: {
        GREETING: '',
        LEAVING: '',
        QUEST: "C'est Big Mama qui me l'envoie ? Oh...\x7Est-ce qu'elle n'a pas de pyjama avec des pieds?\x7Je porte toujours des pyjamas avec des pieds. Comme tout le monde, non ?\x7Ram\xc3\xa8ne celui-l\xc3\xa0 et demande-lui de m'en trouver un avec des pieds.",
        INCOMPLETE_PROGRESS: "Mon pyjama doit avoir des pieds. Va voir si Big Mama peut m'aider.",
        COMPLETE: ''},
    7230: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Des pieds? Laisse-moi r\xc3\xa9fl\xc3\xa9chir....\x7Attends un peu! J'ai ce qu'il te faut!\x7Ta-dam! Un pyjama avec des pieds. Une jolie grenouill\xc3\xa8re bleue avec des pieds. La meilleure de toutes les \xc3\xaeles.\x7S'il te pla\xc3\xaet, va-la-lui porter, tu veux? Merci!",
        INCOMPLETE_PROGRESS: 'Est-ce que Sandie a aim\xc3\xa9 la grenouill\xc3\xa8re bleue ?',
        COMPLETE: ''},
    7231: {
        GREETING: '',
        LEAVING: '',
        QUEST: "OK, elle a EFFECTIVEMENT des pieds, mais je ne peux pas porter une grenouill\xc3\xa8re bleue!\x7Demande \xc3\xa0 Big Mama si elle n'a pas une autre couleur.",
        INCOMPLETE_PROGRESS: "Je suis s\xc3\xbbre que Big Mama a une grenouill\xc3\xa8re d'une autre couleur.",
        COMPLETE: ''},
    7232: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Quel dommage. C'est la seule grenouill\xc3\xa8re que j'aie.\x7Oh, j'ai une id\xc3\xa9e. Va demander \xc3\xa0 Tartine. Elle aura peut-\xc3\xaatre des pyjamas avec des pieds._where_",
        INCOMPLETE_PROGRESS: "Non, ce sont les seuls pyjamas que j'aie. Va voir si Tartine en a._where_",
        COMPLETE: ''},
    7233: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Des pyjamas avec des pieds? Bien s\xc3\xbbr.\x7Qu'est-ce que tu veux dire, il est bleu? Elle n'aime pas le bleu?\x7Oh, alors l\xc3\xa0, c'est plus compliqu\xc3\xa9. Tiens, essaie \xc3\xa7a.\x7Il n'est pas bleu et il A des pieds.",
        INCOMPLETE_PROGRESS: "Moi j'adore la couleur puce, pas toi?\x7J'esp\xc3\xa8re que Sandie l'aimera....",
        COMPLETE: ''},
    7234: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Non, il n'est pas bleu mais personne avec mon teint ne peut porter de couleur puce.\x7Absolument impossible. Retourne l\xc3\xa0-bas et rapporte-le! Va voir ce que Tartine a d'autre.",
        INCOMPLETE_PROGRESS: "Tartine doit avoir d'autres pyjamas. La couleur puce, hors de question pour moi!",
        COMPLETE: ''},
    7235: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Pas de puce non plus. Hmm....\x7Par ma barbe, je sais que j'en ai d'autres.\x7Il va me falloir un moment pour les trouver. Faisons un march\xc3\xa9.\x7Je cherche d'autres grenouill\xc3\xa8res si tu te d\xc3\xa9barrasses de quelques b\xc3\xa2timents Cog. Ils sont vraiment g\xc3\xaanants.\x7La grenouill\xc3\xa8re sera pr\xc3\xaate quand tu reviendras, _avName_.",
        INCOMPLETE_PROGRESS: "Tu dois \xc3\xa9liminer d'autres b\xc3\xa2timents Cog pendant que je cherche d'autres grenouill\xc3\xa8res.",
        COMPLETE: ''},
    7236: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Tu as fait de l'excellent travail avec ces Cogs! Merci!\x7J'ai trouv\xc3\xa9 cette grenouill\xc3\xa8re pour Sandie, j'esp\xc3\xa8re que \xc3\xa7a lui plaira.\x7Apporte-la-lui. Merci.",
        INCOMPLETE_PROGRESS: 'Sandie attend sa grenouill\xc3\xa8re, _avName_.',
        COMPLETE: "Une grenouill\xc3\xa8re fuchsia! Parr-fait!\x7Ah, maintenant je suis parfaitement bien. Voyons voir....\x7Oh, je suppose que je devrais te donner quelque chose pour te remercier de ton aide.\x7Peut-\xc3\xaatre que ceci te sera utile. Quelqu'un l'a laiss\xc3\xa9 ici."},
    7239: {
        QUEST: "Va voir Emma Scara. Elle demande de l'aide._where_"},
    7240: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Ces satan\xc3\xa9s Cogs ont pris ma cr\xc3\xa8me antirides!\x7Mes clients DOIVENT absolument avoir de la cr\xc3\xa8me antirides quand je m'occupe d'eux.\x7Va voir Honor\xc3\xa9 et demande-lui s'il a toujours ma recette sp\xc3\xa9ciale en stock._where_",
        INCOMPLETE_PROGRESS: "Je refuse de m'occuper de quelqu'un qui n'a pas de cr\xc3\xa8me antirides.\x7Va voir si Honor\xc3\xa9 en a."},
    7241: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Oh, cette Emma n'est pas facile. Elle ne se contente pas de ma recette habituelle.\x7Ce qui veut dire que je vais avoir besoin de corail chou-fleur, mon ingr\xc3\xa9dient sp\xc3\xa9cial ultrasecret. Mais je n'en ai pas en stock.\x7Pourrais-tu aller m'en p\xc3\xaacher dans l'\xc3\xa9tang? D\xc3\xa8s que tu auras le corail, je pr\xc3\xa9parerai un m\xc3\xa9lange de cr\xc3\xa8me pour Emma.",
        INCOMPLETE_PROGRESS: "J'ai besoin de corail chou-fleur pour pr\xc3\xa9parer ma cr\xc3\xa8me antirides."},
    7242: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Waouh, quel beau corail chou-fleur!\x7Ok, voyons voir... Un peu de ceci et une petite gicl\xc3\xa9e de cela... Et maintenant, une cuiller\xc3\xa9e d'algues.\x7H\xc3\xa9, o\xc3\xb9 sont les algues? On dirait que je suis aussi \xc3\xa0 court d'algues.\x7Peux-tu faire un saut \xc3\xa0 l'\xc3\xa9tang et me ramasser une belle algue gluante ?",
        INCOMPLETE_PROGRESS: "Plus un brin d'algue gluante dans cette boutique.\x7Impossible de pr\xc3\xa9parer la cr\xc3\xa8me sans algue."},
    7243: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Oooh! Voil\xc3\xa0 une algue gluante \xc3\xa0 souhait, _avName_.\x7Maintenant, je vais juste \xc3\xa9craser quelques perles dans le mortier avec le pilon.\x7Hum, o\xc3\xb9 est mon pilon ? \xc3\x80 quoi sert un mortier sans un pilon ?\x7Je parie que ce fichu Usurier l'a pris quand il est venu ici!\x7Il faut que tu m'aides \xc3\xa0 le trouver! Il se dirigeait vers le QG Caissbot!",
        INCOMPLETE_PROGRESS: 'Je ne peux tout simplement pas \xc3\xa9craser mes perles sans un pilon.\x7Fichus Usuriers!'},
    7244: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Parfait! Tu as mon pilon!\x7Maintenant on va pouvoir travailler. \xc3\x89craser \xc3\xa7a... Touiller un peu et...\x7\xc3\x87a y est! Va dire \xc3\xa0 Emma que c'est de la bonne cr\xc3\xa8me, fra\xc3\xaechement pr\xc3\xa9par\xc3\xa9e.",
        INCOMPLETE_PROGRESS: "Tu devrais apporter cette cr\xc3\xa8me \xc3\xa0 Emma tant qu'elle est encore fra\xc3\xaeche.\x7C'est une cliente tr\xc3\xa8s difficile.",
        COMPLETE: "Honor\xc3\xa9 n'avait pas un pot de cr\xc3\xa8me antirides plus gros que \xc3\xa7a? Non ?\x7Eh bien, je suppose qu'il faudra simplement que j'en recommande quand je n'en aurai plus.\x7\xc3\x80 un de ces quatre, _avName_.\x7Quoi? Tu es toujours l\xc3\xa0? Tu ne vois pas que j'essaie de travailler ?\x7Tiens, prends \xc3\xa7a."},
    11000: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Si tu es int\xc3\xa9ress\xc3\xa9 par les pi\xc3\xa8ces de d\xc3\xa9guisement de Loibot, tu devrais aller voir _toNpcName_.\x7J'ai entendu dire qu'il a grand besoin d'aide pour ses recherches m\xc3\xa9t\xc3\xa9orologiques._where_"},
    11001: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Oui, oui. J'ai des pi\xc3\xa8ces de d\xc3\xa9guisement de Loibot.\x7Mais elles sont sans int\xc3\xa9r\xc3\xaat pour moi.\x7Mes recherches portent sur les fluctuations de la temp\xc3\xa9rature ambiante de Toontown.\x7J'\xc3\xa9changerais volontiers des pi\xc3\xa8ces de d\xc3\xa9guisement contre des sondes de temp\xc3\xa9rature Cog.\x7Tu peux commencer par aller voir %s." %
               GlobalStreetNames[2100][-1],
        INCOMPLETE_PROGRESS: 'Est-ce que tu as essay\xc3\xa9 de chercher sur %s?' % GlobalStreetNames[2100][-1],
        COMPLETE: "Ah, parfait!\x7C'est ce que je craignais...\x7Oh, oui! Voil\xc3\xa0 ta pi\xc3\xa8ce de d\xc3\xa9guisement."},
    11002: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Pour obtenir d'autres pi\xc3\xa8ces de d\xc3\xa9guisement de Loibot, tu devrais retourner voir _toNpcName_.\x7J'ai entendu dire qu'il avait besoin d'assistants de recherche._where_"},
    11003: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Plus de pi\xc3\xa8ces de d\xc3\xa9guisement de Loibot?\x7Bon, si tu insistes...\x7mais j'ai besoin d'une autre sonde de temp\xc3\xa9rature Cog.\x7Cette fois-ci, va sur %s." %
               GlobalStreetNames[2200][-1],
        INCOMPLETE_PROGRESS: 'Tu cherches bien sur %s ?' % GlobalStreetNames[2200][-1],
        COMPLETE: 'Merci!\x7Voil\xc3\xa0 ta pi\xc3\xa8ce de d\xc3\xa9guisement.'},
    11004: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Si tu as besoin de pi\xc3\xa8ces de d\xc3\xa9guisement Loibot suppl\xc3\xa9mentaires, tu devrais retourner voir _toNpcName_.\x7Apparemment, il a toujours besoin d'aide pour ses recherches m\xc3\xa9t\xc3\xa9orologiques._where_"},
    11005: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Tu sais te montrer utile!\x7Est-ce que tu peux aller jeter un oeil sur %s?' % GlobalStreetNames[2300][
            -1],
        INCOMPLETE_PROGRESS: ' Tu es bien en train de chercher sur %s ?' % GlobalStreetNames[2300][-1],
        COMPLETE: "Hmmm, je n'aime pas trop \xc3\xa7a...\x7mais voici ta pi\xc3\xa8ce de d\xc3\xa9guisement..."},
    11006: {
        GREETING: '',
        LEAVING: '',
        QUEST: ' Qui-tu-sais a besoin de relev\xc3\xa9s de temp\xc3\xa9rature suppl\xc3\xa9mentaires.\x7Passe le voir si tu veux une autre pi\xc3\xa8ce de d\xc3\xa9guisement._where_'},
    11007: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Encore toi?\x7Tu as vraiment envie de travailler...\x7La prochaine destination, c'est %s." %
               GlobalStreetNames[1100][-1],
        INCOMPLETE_PROGRESS: 'Est-ce que tu as essay\xc3\xa9 de chercher sur %s?' % GlobalStreetNames[1100][-1],
        COMPLETE: "Bon! On dirait que tu t'en sors plut\xc3\xb4t bien!\x7Ta pi\xc3\xa8ce de d\xc3\xa9guisement..."},
    11008: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Si tu as envie d'une autre pi\xc3\xa8ce de d\xc3\xa9guisement de Loibot..._where_"},
    11009: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Content de te trouver ici!\x7Maintenant, j'ai besoin de relev\xc3\xa9s sur %s." %
               GlobalStreetNames[1200][-1],
        INCOMPLETE_PROGRESS: 'Tu cherches bien sur %s ?' % GlobalStreetNames[1200][-1],
        COMPLETE: "Merci beaucoup!\x7Tu n'es probablement pas loin d'avoir tout ton d\xc3\xa9guisement..."},
    11010: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Je crois que _toNpcName_ a encore du travail pour toi._where_'},
    11011: {
        GREETING: '',
        LEAVING: '',
        QUEST: ' Content de te revoir, _avName_!\x7Est-ce que tu peux faire un relev\xc3\xa9 sur %s?' %
               GlobalStreetNames[1300][-1],
        INCOMPLETE_PROGRESS: 'Est-ce que tu as essay\xc3\xa9 de chercher sur %s?' % GlobalStreetNames[1300][-1],
        COMPLETE: "Super boulot!\x7Voici ta r\xc3\xa9compense. Tu l'as bien m\xc3\xa9rit\xc3\xa9e!"},
    11012: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Tu sais ce qu'il faut faire._where_"},
    11013: {
        GREETING: '',
        LEAVING: '',
        QUEST: '_avName_, mon ami!\x7Est-ce que tu pourrais aller \xc3\xa0 %s et me trouver une autre sonde de temp\xc3\xa9rature?' %
               GlobalStreetNames[5100][-1],
        INCOMPLETE_PROGRESS: 'Est-ce que tu es vraiment en train de chercher sur %s?' % GlobalStreetNames[5100][-1],
        COMPLETE: 'Excellent!\x7Gr\xc3\xa2ce \xc3\xa0 ton aide, mes recherches avancent tr\xc3\xa8s vite!\x7Voici ta r\xc3\xa9compense.'},
    11014: {
        GREETING: '',
        LEAVING: '',
        QUEST: '_toNpcName_ a parl\xc3\xa9 de toi.aOn dirait que tu as fait une sacr\xc3\xa9e impression!_where_'},
    11015: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Content de te revoir!\x7Je t'attendais.\x7Le prochain relev\xc3\xa9 dont j'ai besoin, c'est sur %s." %
               GlobalStreetNames[5200][-1],
        INCOMPLETE_PROGRESS: 'Tu cherches bien sur %s ?' % GlobalStreetNames[5200][-1],
        COMPLETE: 'Merci!\x7Voici ta r\xc3\xa9compense.'},
    11016: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Si tu as besoin de terminer ton d\xc3\xa9guisement de Loibot...\x7_toNpcName_ peut t'aider._where_"},
    11017: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Salut, jeune chercheur!\x7Nous avons encore besoin de relev\xc3\xa9s de %s.' % GlobalStreetNames[5300][
            -1],
        INCOMPLETE_PROGRESS: 'Est-ce que tu as essay\xc3\xa9 de chercher sur %s?' % GlobalStreetNames[5300][-1],
        COMPLETE: 'Excellent travail!\x7Voil\xc3\xa0 ton machin de Loibot...'},
    11018: {
        GREETING: '',
        LEAVING: '',
        QUEST: "_toNpcName_ a un autre travail pour toi.\x7Si tu n'en as pas assez de le voir..._where_"},
    11019: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Bon, tr\xc3\xa8s bien.\x7Tu te sens d'attaque pour aller chercher autre chose?\x7Cette fois-ci, essaie %s." %
               GlobalStreetNames[4100][-1],
        INCOMPLETE_PROGRESS: 'Tu es bien en train de chercher sur %s ?' % GlobalStreetNames[4100][-1],
        COMPLETE: 'Et un de plus!\x7Quelle efficacit\xc3\xa9!'},
    11020: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Tu es toujours \xc3\xa0 la recherche de pi\xc3\xa8ces de d\xc3\xa9guisement de Loibot?_where_'},
    11021: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Tu as sans doute d\xc3\xa9j\xc3\xa0 devin\xc3\xa9...\x7mais j'ai besoin de relev\xc3\xa9s de %s." %
               GlobalStreetNames[4200][-1],
        INCOMPLETE_PROGRESS: 'Tu cherches bien sur %s ?' % GlobalStreetNames[4200][-1],
        COMPLETE: 'On y est presque!\x7Et voil\xc3\xa0...'},
    11022: {
        GREETING: '',
        LEAVING: '',
        QUEST: "J'ai presque honte de le dire, mais..._where_"},
    11023: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Qu'est-ce que tu penses de %s? Est-ce que tu crois que tu pourrais aller chercher une sonde l\xc3\xa0-bas aussi?" %
               GlobalStreetNames[4300][-1],
        INCOMPLETE_PROGRESS: 'Est-ce que tu as essay\xc3\xa9 de chercher sur %s?' % GlobalStreetNames[4300][-1],
        COMPLETE: 'Encore du bon travail, _avName_'},
    11024: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Va voir le Professeur, si tu as encore besoin de pi\xc3\xa8ces de d\xc3\xa9guisement._where_'},
    11025: {
        GREETING: '',
        LEAVING: '',
        QUEST: "Je crois qu'on a encore besoin d'un relev\xc3\xa9 de %s." % GlobalStreetNames[9100][-1],
        INCOMPLETE_PROGRESS: 'Tu es bien en train de chercher sur %s ?' % GlobalStreetNames[9100][-1],
        COMPLETE: "Bon travail!\x7Je crois qu'on se rapproche..."},
    11026: {
        GREETING: '',
        LEAVING: '',
        QUEST: '_toNpcName_ a une derni\xc3\xa8re mission pour toi._where_'},
    11027: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'D\xc3\xa9j\xc3\xa0 de retour?\x7Le dernier relev\xc3\xa9 est sur %s.' % GlobalStreetNames[9200][-1],
        INCOMPLETE_PROGRESS: 'Tu cherches bien sur %s ?' % GlobalStreetNames[9200][-1],
        COMPLETE: "\xc3\x87a y est enfin!\x7Maintenant, tu vas pouvoir t'introduire dans le bureau du Procureur et ramasser des convocations du jury.\x7Bonne chance et merci pour ton aide!"}}
ChatGarblerDog = [
    'ouaf',
    'ouarf',
    'rrrgh']
ChatGarblerCat = [
    'miaou',
    'maaou']
ChatGarblerMouse = [
    'couic',
    'couiiic',
    'iiiiic']
ChatGarblerHorse = [
    'hihiii',
    'brrr']
ChatGarblerRabbit = [
    'ouic',
    'pouip',
    'plouik',
    'bouip']
ChatGarblerDuck = [
    'coin',
    'couac',
    'coiinc']
ChatGarblerMonkey = [
    'oh',
    'hou',
    'ah']
ChatGarblerBear = [
    'grrr',
    'grrr']
ChatGarblerPig = [
    'rrrrr',
    'ouing',
    'ouing']
ChatGarblerDefault = [
    'blabla']
Bossbot = 'Chefbot'
Lawbot = 'Loibot'
Cashbot = 'Caissbot'
Sellbot = 'Vendibot'
BossbotS = 'un Chefbot'
LawbotS = 'un Loibot'
CashbotS = 'un Caissbot'
SellbotS = 'un Vendibot'
BossbotP = 'des Chefbots'
LawbotP = 'des Loibots'
CashbotP = 'des Caissbots'
SellbotP = 'des Vendibots'
BossbotSkelS = 'un Chefbot Skelecog'
LawbotSkelS = 'un Loibot Skelecog'
CashbotSkelS = 'un Caissbot Skelecog'
SellbotSkelS = 'un Vendibot Skelecog'
BossbotSkelP = 'des Chefbots Skelecogs'
LawbotSkelP = 'des Loibots Skelecogs'
CashbotSkelP = 'des Caissbots Skelecogs'
SellbotSkelP = 'des Vendibots Skelecogs'
AvatarDetailPanelOK = lOK
AvatarDetailPanelCancel = lCancel
AvatarDetailPanelClose = lClose
AvatarDetailPanelLookup = 'Recherche de coordonn\xc3\xa9es pour %s.'
AvatarDetailPanelFailedLookup = "Impossible d'obtenir les coordonn\xc3\xa9es de %s."
AvatarDetailPanelOnline = 'District : %(district)s\nLieu : %(location)s'
AvatarDetailPanelOffline = 'District: hors-ligne\nLieu : hors-ligne'
AvatarDetailPanelPlayer = 'Joueur : %(player)s\nMonde : %(world)s'
AvatarDetailPanelPlayerShort = '%(player)s\nMonde : %(world)s\nLieu : %(location)s'
AvatarDetailPanelRealLife = 'Hors ligne'
AvatarDetailPanelOnlinePlayer = 'District : %(district)s\nLieu : %(location)s\nJoueur : %(player)s'
AvatarShowPlayer = 'Montrer joueur'
OfflineLocation = 'Hors ligne'
PlayerToonName = 'Toon : %(toonname)s'
PlayerShowToon = 'Montrer Toon'
PlayerPanelDetail = 'Informations joueur'
AvatarPanelFriends = 'Contacts'
AvatarPanelWhisper = 'Chuchoter'
AvatarPanelSecrets = 'Secrets'
AvatarPanelGoTo = 'Aller \xc3\xa0'
AvatarPanelPet = 'Montrer le Doudou'
AvatarPanelIgnore = 'Ignorer'
AvatarPanelCogLevel = 'Niveau: %s'
AvatarPanelCogDetailClose = lClose
AvatarPanelDetail = 'D\xc3\xa9tails du Toon'
PetPanelFeed = 'Nourrir'
PetPanelCall = 'Appeler'
PetPanelGoTo = 'Aller \xc3\xa0'
PetPanelOwner = 'Montrer le propri\xc3\xa9taire'
PetPanelDetail = "D\xc3\xa9tails de l'animalerie"
PetPanelScratch = 'Cajoler'
PetDetailPanelTitle = 'Apprentissage des tours'
PetTrickStrings = {
    0: 'Saute',
    1: 'Fais le beau',
    2: 'Fais le mort',
    3: 'Fais une roulade',
    4: 'Saute en arri\xc3\xa8re',
    5: 'Danse',
    6: 'Parle'}
PetMoodAdjectives = {
    'neutral': 'neutre',
    'hunger': 'affam\xc3\xa9',
    'boredom': "s'ennuie",
    'excitement': 'excit\xc3\xa9',
    'sadness': 'triste',
    'restlessness': 'agit\xc3\xa9',
    'playfulness': 'joueur',
    'loneliness': 'solitaire',
    'fatigue': 'fatigu\xc3\xa9',
    'confusion': 'perplexe',
    'anger': 'en col\xc3\xa8re',
    'surprise': 'surpris',
    'affection': 'affectueux'}
DialogQuestion = '?'
FriendsListLabel = 'Contacts'
TeleportPanelOK = lOK
TeleportPanelCancel = lCancel
TeleportPanelYes = lYes
TeleportPanelNo = lNo
TeleportPanelCheckAvailability = "Essaie d'aller \xc3\xa0 %s."
TeleportPanelNotAvailable = '%s est occup\xc3\xa9(e) en ce moment, ressaie plus tard.'
TeleportPanelIgnored = "%s t'ignore"
TeleportPanelNotOnline = "%s n'est pas en ligne en ce moment."
TeleportPanelWentAway = '%s est parti(e).'
TeleportPanelUnknownHood = "Tu ne sais pas aller jusqu'\xc3\xa0 %s!"
TeleportPanelUnavailableHood = '%s est occup\xc3\xa9(e) en ce moment, ressaie plus tard.'
TeleportPanelDenySelf = 'Tu ne peux pas aller te voir toi-m\xc3\xaame!'
TeleportPanelOtherShard = '%(avName)s est dans le district %(shardName)s, et tu es dans le district %(myShardName)s. Veux-tu aller \xc3\xa0 %(shardName)s?'
BattleBldgBossTaunt = 'Je suis le chef.'
FactoryBossTaunt = 'Je suis le contrema\xc3\xaetre.'
FactoryBossBattleTaunt = 'Je te pr\xc3\xa9sente le contrema\xc3\xaetre.'
MintBossTaunt = 'Je suis le Superviseur.'
MintBossBattleTaunt = 'Vous devez parler au Superviseur.'
StageBossTaunt = "Ma justice n'est pas aveugle"
StageBossBattleTaunt = 'Je suis au-dessus des lois'
ToonHealJokes = [
    [
        "Qu'est ce qui fait PIOU-PIOU?",
        'Un poussin de 500 kilos!'],
    [
        'Que dit un pneu qui va voir un m\xc3\xa9decin ?',
        'Docteur, je me sens crev\xc3\xa9.'],
    [
        'Pourquoi est-ce difficile pour un fant\xc3\xb4me de mentir ?',
        "Parce qu'il est cousu de fil blanc."],
    [
        "Vous connaissez l'histoire de la chaise ?",
        'Dommage, elle est pliante!'],
    [
        "Qu'est-ce qui est vert et qui monte et qui descend?",
        'Un petit pois dans un ascenseur!'],
    [
        "Quel est le comble de l'\xc3\xa9lectricien ?",
        'De ne pas \xc3\xaatre au courant.'],
    [
        'Que font deux chiens qui se rencontrent \xc3\xa0 Tokyo?',
        'Ils se jappent au nez.'],
    [
        'Quel est le futur de "je baille"?',
        'Je dors.'],
    [
        "Quel est l'animal le plus rapide ?",
        'Le pou car il est toujours en t\xc3\xaate!'],
    [
        "Quel animal n'a jamais soif?",
        'Le z\xc3\xa9bu, parce que quand z\xc3\xa9bu z\xc3\xa9 plus soif!'],
    [
        'Quel est le comble pour un myope ?',
        'De manger des lentilles.'],
    [
        'Pourquoi as-tu mis le journal dans le r\xc3\xa9frig\xc3\xa9rateur ?',
        'Pour avoir des nouvelles fra\xc3\xaeches!'],
    [
        "Qu'est-ce qui est gris et qui t'\xc3\xa9clabousse de confiture ?",
        'Une souris qui mange un beignet.'],
    [
        'Que demande un douanier \xc3\xa0 un cochon qui passe la fronti\xc3\xa8re ?',
        'Son passe-porc.'],
    [
        'Que dit un b\xc3\xa9b\xc3\xa9 souris \xc3\xa0 sa maman quand il voit passer une chauve-souris?',
        'Maman, un ange!'],
    [
        'Comment appelle-t-on un ascenseur au Japon ?',
        'En appuyant sur le bouton.'],
    [
        'Comment appelle-t-on un poisson pas encore n\xc3\xa9?',
        'Un poisson pan\xc3\xa9.'],
    [
        'Si tu fais tomber un chapeau blanc dans la mer rouge, comment ressort-il?',
        'Mouill\xc3\xa9.'],
    [
        'Que demande un chat qui entre dans une pharmacie ?',
        'Du sirop pour matou.'],
    [
        'Quel est le comble pour un jockey?',
        "D'\xc3\xaatre \xc3\xa0 cheval sur les principes."],
    [
        'Quelles sont les deux choses que tu ne peux pas prendre au petit-d\xc3\xa9jeuner ?',
        'Le d\xc3\xa9jeuner et le d\xc3\xaener.'],
    [
        "Qu'est ce qu'on donne \xc3\xa0 un \xc3\xa9l\xc3\xa9phant qui a de grands pieds?",
        'De grandes chaussures.'],
    [
        "Comment sait-on qu'un \xc3\xa9l\xc3\xa9phant est cach\xc3\xa9 dans le r\xc3\xa9frig\xc3\xa9rateur ?",
        'Aux empreintes de pattes dans le beurre.'],
    [
        'Quelle est la diff\xc3\xa9rence entre un instituteur et un thermom\xc3\xa8tre ?',
        'Aucune, on tremble toujours quand ils marquent z\xc3\xa9ro!'],
    [
        "Qu'est-ce qui est petit, carr\xc3\xa9 et vert ?",
        'Un petit carr\xc3\xa9 vert.'],
    [
        'Quel est le comble pour un \xc3\xa9l\xc3\xa9phant ?',
        "D'\xc3\xaatre sans d\xc3\xa9fense."],
    [
        'Que dit le 0 au 8?',
        'Tiens, tu as mis ta ceinture!'],
    [
        "Qu'est ce qu'il ne faut jamais faire devant un poisson-scie ?",
        'La planche!'],
    [
        'Pourquoi est-ce que certaines personnes travaillent la nuit ?',
        'Pour mettre leur travail \xc3\xa0 jour.'],
    [
        'Quel est le comble de la patience ?',
        'Trier des petits pois avec des gants de boxe.'],
    [
        "Qu'est ce qui voyage tout autour du monde en restant dans son coin ?",
        'Un timbre.'],
    [
        'Quel est le comble pour une souris?',
        'Avoir un chat dans la gorge.'],
    [
        'Quel est le comble pour un canard?',
        'En avoir marre!'],
    [
        'Quel est le comble pour un magicien ?',
        "Se nourrir d'illusions."],
    [
        'Quel est le comble de la cl\xc3\xa9?',
        'Se faire mettre \xc3\xa0 la porte.'],
    [
        'Quel est le comble pour un cordonnier ?',
        'Avoir les dents qui se d\xc3\xa9chaussent.'],
    [
        'De quelle couleur sont les petits pois?',
        'Les petits poissons rouges.'],
    [
        "Qu'est-ce qui baille et qui ne dort jamais?",
        'Une porte.'],
    [
        "Tu sais ce que c'est un canif?",
        "C'est un p'tit fien!"],
    [
        "Qu'est-ce qu'un chou au fond d'une baignoire ?",
        'Un choumarin!'],
    [
        "Quel est le comble pour le propri\xc3\xa9taire d'un champ de pommiers?",
        'Travailler pour des prunes!'],
    [
        "Qu'est-ce qui est aussi grand que l'Arc de Triomphe mais ne p\xc3\xa8se rien ?",
        'Son ombre.'],
    [
        "Comment s'appelle un boomerang qui ne revient pas?",
        'Un bout de bois.'],
    [
        'Pourquoi est-ce que les \xc3\xa9l\xc3\xa9phants se d\xc3\xa9placent en troupeau compact ?',
        "Parce que c'est celui du milieu qui a la radio."],
    [
        'De quelle couleur sont les parapluies quand il pleut ?',
        'Ils sont tout verts.'],
    [
        'Quel est le comble du torero?',
        'Que le taureau soit vache.'],
    [
        "Quel est l'animal le plus heureux?",
        'Le hibou, parce que sa femme est chouette.'],
    [
        'Que dit un vitrier \xc3\xa0 son fils?',
        'Tiens-toi \xc3\xa0 carreau si tu veux une glace.'],
    [
        'Comment appelle-t-on un chien sans pattes?',
        "On ne l'appelle pas, on va le chercher."],
    [
        "Qu'ont les girafes que n'ont pas les autres animaux?",
        'Des b\xc3\xa9b\xc3\xa9s girafes.'],
    [
        'Un chameau peut-il avoir 3 bosses?',
        "Oui, s'il se cogne la t\xc3\xaate contre le mur."],
    [
        'Pourquoi les musiciens aiment-ils prendre le train ?',
        'Parce que la voie fait r\xc3\xa9.'],
    [
        "Deux fourmis sont sur un \xc3\xa2ne, laquelle va doubler l'autre ?",
        "Aucune, il est interdit de doubler sur un dos d'\xc3\xa2ne."],
    [
        'Quelle est la note la plus basse ?',
        'Le sol.'],
    [
        'Pourquoi les trains \xc3\xa9lectriques vont-ils plus vite que les trains \xc3\xa0 vapeur ?',
        "Parce qu'ils ont arr\xc3\xaat\xc3\xa9 de fumer."],
    [
        "Qu'est ce qu'un arbuste dit \xc3\xa0 un g\xc3\xa9ranium?",
        "Esp\xc3\xa8ce d'empot\xc3\xa9!"],
    [
        'Que recommande la maman allumette \xc3\xa0 ses enfants?',
        'Surtout, ne vous grattez pas la t\xc3\xaate!'],
    [
        "Qu'est-ce qu'il y a \xc3\xa0 la fin de tout ?",
        'La lettre T.'],
    [
        "Pourquoi les poissons-chats s'ennuient-ils?",
        "Parce qu'il n'y a pas de poissons-souris."],
    [
        "Qu'est-ce que le vainqueur du marathon a perdu?",
        'Son souffle.'],
    [
        'Comment appelle-t-on un spectacle qui rend propre ?',
        'Un ballet.'],
    [
        'Qu\'est-ce qui fait 999 fois "Tic" et une fois "Toc"?',
        'Un mille-pattes avec une jambe de bois.'],
    [
        "Comment reconna\xc3\xaet-on un \xc3\xa9cureuil d'une fourchette ?",
        "En les mettant au pied d'un arbre, celui qui monte est l'\xc3\xa9cureuil."],
    [
        'Pourquoi les flamants roses l\xc3\xa8vent-ils une patte en dormant ?',
        "Parce qu'ils tomberaient s'ils levaient les deux."],
    [
        "Qu'est-ce qui est noir quand il est propre et blanc quand il est sale ?",
        'Un tableau noir!'],
    [
        "Qu'est-ce qui fait Oh, Oh, Oh?",
        'Le P\xc3\xa8re No\xc3\xabl qui marche en arri\xc3\xa8re.'],
    [
        "Qu'est-ce qui peut voyager jour et nuit sans quitter son lit ?",
        'La rivi\xc3\xa8re.'],
    [
        "Quel arbre n'aime pas la vitesse ?",
        'Le fr\xc3\xaane.'],
    [
        'Pourquoi est-ce que les dinosaures ont de longs cous?',
        'Parce que leurs pieds sentent mauvais.'],
    [
        "Qu'est-ce qui est jaune et qui court tr\xc3\xa8s vite ?",
        'Un citron press\xc3\xa9.'],
    [
        "Pourquoi est-ce que les \xc3\xa9l\xc3\xa9phants n'oublient jamais?",
        "Parce qu'on ne leur dit jamais rien."],
    [
        'Quel animal peut changer de t\xc3\xaate facilement ?',
        'Un pou.'],
    [
        "Qu'est-ce qu'un steak cach\xc3\xa9 derri\xc3\xa8re un arbre ?",
        'Un steak cach\xc3\xa9.'],
    [
        'Pourquoi est-ce que les serpents ne sont pas susceptibles?',
        "Parce qu'on ne peut pas leur casser les pieds."],
    [
        'Pourquoi dit-on que les boulangers travaillent rapidement ?',
        "Parce qu'ils travaillent en un \xc3\xa9clair."],
    [
        'Que dit un fant\xc3\xb4me quand il est ennuy\xc3\xa9?',
        'Je suis dans de beaux draps!'],
    [
        "Comment peut-on arr\xc3\xaater un \xc3\xa9l\xc3\xa9phant qui veut passer dans le chas d'une aiguille ?",
        'On fait un n\xc5\x93ud \xc3\xa0 sa queue.'],
    [
        'Pourquoi est-ce que les pompiers ont des bretelles rouges?',
        'Pour tenir leurs pantalons!'],
    [
        "Que prend un \xc3\xa9l\xc3\xa9phant lorsqu'il rentre dans un bar ?",
        'De la place!'],
    [
        'Savez-vous que votre chien aboie toute la nuit ?',
        '\xc3\x87a ne fait rien, il dort toute la journ\xc3\xa9e!'],
    [
        'Savez-vous que le v\xc3\xa9t\xc3\xa9rinaire a \xc3\xa9pous\xc3\xa9 la manucure ?',
        "Au bout d'un mois ils se battaient becs et ongles."],
    [
        'Tu sais que nous sommes sur terre pour travailler ?',
        'Bon, alors plus tard je serai marin.'],
    [
        'Quand je dis "il pleuvait", de quel temps s\'agit-il?',
        "D'un sale temps."],
    [
        '\xc3\x80 quoi reconna\xc3\xaet-on un motard heureux?',
        'Aux moustiques coll\xc3\xa9s sur ses dents.'],
    [
        'Son succ\xc3\xa8s lui est mont\xc3\xa9 \xc3\xa0 la t\xc3\xaate.',
        "C'est normal, c'est l\xc3\xa0 qu'il y avait le plus de place libre."],
    [
        "Qu'est-ce qui est gris, pousse de petits cris et fait 5 kilos?",
        'Une souris qui a besoin de se mettre au r\xc3\xa9gime.'],
    [
        'Que dit-on \xc3\xa0 un croque-mort qui rentre dans un caf\xc3\xa9?',
        '"Je vous sers une bi\xc3\xa8re ?"'],
    [
        "Connais-tu l'histoire du lit vertical?",
        "C'est une histoire \xc3\xa0 dormir debout."],
    [
        'Pourquoi est-ce que les \xc3\xa9l\xc3\xa9phants sont gros et gris?',
        "Parce que s'ils \xc3\xa9taient petits et jaunes ce seraient des canaris."],
    [
        'Combien co\xc3\xbbte cet aspirateur ?',
        '750 et des poussi\xc3\xa8res.'],
    [
        'Quel est le comble pour un juge gourmand?',
        'De manger des avocats.'],
    [
        'Pourquoi' + Donald + " regarde-t-il \xc3\xa0 droite et \xc3\xa0 gauche lorsqu'il rentre dans une pi\xc3\xa8ce ?",
        "Parce qu'il ne peut pas regarder des deux c\xc3\xb4t\xc3\xa9s \xc3\xa0 la fois."],
    [
        'Pourquoi est-ce que' + Goofy + ' emm\xc3\xa8ne son peigne chez le dentiste ?',
        "Parce qu'il a perdu toutes ses dents."],
    [
        'Quel bruit fait la fourmi?',
        'La fourmi cro-onde.'],
    [
        "Si les sorties \xc3\xa9taient surveill\xc3\xa9es, comment le voleur a-t-il pu s'\xc3\xa9chapper ?",
        "Par l'entr\xc3\xa9e!"],
    [
        'Que dit un haut-parleur \xc3\xa0 un autre haut-parleur ?',
        'Tu veux une baffle ?'],
    [
        'Pourquoi les l\xc3\xa9zards aiment-ils les vieux murs?',
        "Parce qu'ils ont des l\xc3\xa9zardes."],
    [
        'Pourquoi est-ce que les moutons ont des pelages en laine ?',
        "Parce qu'ils auraient l'air idiots avec des pelages en synth\xc3\xa9tique."],
    [
        'O\xc3\xb9 trouve-t-on le dimanche avant le jeudi?',
        'Dans le dictionnaire.'],
    [
        'Pourquoi est-ce que' + Pluto + ' a dormi avec une peau de banane ?',
        'Pour pouvoir se glisser hors de son lit le lendemain matin.'],
    [
        'Pourquoi est-ce que la souris portait des chaussons noirs?',
        'Parce que les blancs \xc3\xa9taient \xc3\xa0 la lessive.'],
    [
        'Quel est le point commun entre les fausses dents et les \xc3\xa9toiles?',
        'Elles sortent la nuit.'],
    [
        'Pourquoi est-ce que les chats aiment se faire photographier ?',
        'Parce qu\'on leur dit "souris!".'],
    [
        "Pourquoi est-ce que l'arch\xc3\xa9ologue a fait faillite ?",
        'Parce que sa carri\xc3\xa8re \xc3\xa9tait en ruine.'],
    [
        "Qui boit l'eau sans jamais l'avaler ?",
        "L'\xc3\xa9ponge."],
    [
        'Quelle est la couleur du virus de la grippe ?',
        'Gris p\xc3\xa2le.'],
    [
        'Pourquoi faut-il craindre le soleil?',
        "Parce que c'est le plus grand des astres."],
    [
        "Quel est le comble d'un avion ?",
        "C'est d'avoir un antivol."],
    [
        'Que dit la nappe \xc3\xa0 la table ?',
        'Ne crains rien, je te couvre.'],
    [
        'Que fait' + Goofy + " quand il tombe dans l'eau?",
        'PLOUF!'],
    [
        'Quel est le comble pour un crayon ?',
        'Se tailler pour avoir bonne mine.'],
    [
        'Que dit la grosse chemin\xc3\xa9e \xc3\xa0 la petite chemin\xc3\xa9e ?',
        'Tu es trop jeune pour fumer.'],
    [
        'Que dit le tapis au carrelage ?',
        "Ne t'inqui\xc3\xa8te pas, je te couvre."],
    [
        'Quelle est la diff\xc3\xa9rence entre le cancre et le premier de la classe ?',
        "Quand le cancre redouble, c'est rarement d'attention."],
    [
        "Qu'est-ce qui fait zzzb zzzb?",
        "Une gu\xc3\xaape qui vole \xc3\xa0 l'envers."],
    [
        "Comment appelle-t-on quelqu'un qui tue son beau-fr\xc3\xa8re ?",
        "Un insecticide, car il tue l'\xc3\xa9poux de sa s\xc5\x93ur."],
    [
        "Comment appelle-t-on un dinosaure qui n'est jamais en retard?",
        'Un promptosaure.'],
    [
        'On ne devrait pas dire "un chapitre".',
        'On devrait dire "un chat rigolo".'],
    [
        'On ne devrait pas dire "un perroquet".',
        'On devrait dire "mon papa est d\'accord".'],
    [
        'On ne devrait pas dire "bosser \xc3\xa0 la cha\xc3\xaene".',
        'On devrait dire "travailler \xc3\xa0 la t\xc3\xa9l\xc3\xa9".'],
    [
        'Pourquoi est-ce que le livre de maths \xc3\xa9tait malheureux?',
        "Parce qu'il avait trop de probl\xc3\xa8mes."],
    [
        'On ne devrait pas dire "un match interminable".',
        'On devrait dire "une rencontre de mauvais joueurs".'],
    [
        'On ne devrait pas dire "la ma\xc3\xaetresse d\'\xc3\xa9cole".',
        'On devrait dire "l\'institutrice prend l\'avion".'],
    [
        'Que voit-on quand deux mille-pattes se serrent la main ?',
        'Une fermeture-\xc3\xa9clair.'],
    [
        'Comment appelle-t-on un journal publi\xc3\xa9 au Sahara?',
        'Un hebdromadaire.'],
    [
        'Que doit planter un agriculteur frileux?',
        "Un champ d'ail."],
    [
        'Quel est le comble du chauve ?',
        'Avoir un cheveu sur la langue.'],
    [
        "Qu'est-ce que tu trouves si tu croises un \xc3\xa9l\xc3\xa9phant avec un corbeau?",
        'Des tas de poteaux t\xc3\xa9l\xc3\xa9phoniques cass\xc3\xa9s.'],
    [
        'Combien gagne un fakir ?',
        'Des clous!'],
    [
        "Quelle est la meilleure mani\xc3\xa8re d'\xc3\xa9conomiser l'eau?",
        'La diluer.'],
    [
        'Quelle diff\xc3\xa9rence y a-t-il entre un horloger et une girouette ?',
        "L'horloger vend des montres et la girouette montre le vent."],
    [
        'Pourquoi est-ce que les ordinateurs se grattent ?',
        "Parce qu'ils sont pleins de puces."],
    [
        "Qu'est-ce qui a un chapeau et pas de t\xc3\xaate, un pied mais pas de souliers?",
        'Un champignon.'],
    [
        'Pourquoi est-ce que le ciel est haut ?',
        'Pour \xc3\xa9viter que les oiseaux ne se cognent la t\xc3\xaate en volant.'],
    [
        "Qu'est ce qui est pire qu'une girafe qui a mal \xc3\xa0 la gorge ?",
        'Un mille-pattes avec des cors aux pieds.'],
    [
        "Qu'est-ce qui fait ABC...gloups...DEF...gloups?",
        "Quelqu'un qui mange de la soupe aux p\xc3\xa2tes alphabet."],
    [
        "Qu'est-ce qui est blanc et qui va vite ?",
        'Un frigo de course.'],
    [
        "Quel est le fruit que les poissons n'aiment pas?",
        'La p\xc3\xaache!'],
    [
        'Comment font les \xc3\xa9l\xc3\xa9phants pour traverser un \xc3\xa9tang?',
        'Ils sautent de n\xc3\xa9nuphar en n\xc3\xa9nuphar.'],
    [
        "Qu'est-ce qui est noir et blanc \xc3\xa0 pois rouges?",
        'Un Dalmatien qui a la rougeole.'],
    [
        "Qu'est-ce qu'un chalumeau?",
        'Un drolumadaire \xc3\xa0 2 bosses.'],
    [
        'Pourquoi les \xc3\xa9l\xc3\xa9phants sont-ils gris?',
        'Pour ne pas les confondre avec les fraises.'],
    [
        'Qu\'est-ce qui est gris, fait 100 kilos et appelle "Minou, Minou!"?',
        'Une souris de 100 kilos.'],
    [
        'Quel est le point commun entre un p\xc3\xa2tissier et un ciel orageux?',
        'Tous les deux font des \xc3\xa9clairs.'],
    [
        "Quel bruit font les esquimaux lorsqu'ils boivent ?",
        'Iglou, iglou, iglou'],
    [
        'Comment appelle-t-on une chauve-souris avec une perruque ?',
        'Une souris.'],
    [
        'Pourquoi les aiguilles sont-elles moins intelligentes que les \xc3\xa9pingles?',
        "Parce qu'elles n'ont pas de t\xc3\xaate."],
    [
        "Qu'est-ce qui a de la fourrure, miaule et chasse les souris sous l'eau?",
        'Un poisson-chat.'],
    [
        'Comment fait-on aboyer un chat ?',
        'Si on lui donne une tasse de lait il la boit.'],
    [
        "Qu'est-ce qui est vert \xc3\xa0 l'ext\xc3\xa9rieur et jaune \xc3\xa0 l'int\xc3\xa9rieur ?",
        'Une banane d\xc3\xa9guis\xc3\xa9e en concombre.'],
    [
        "Qu'est-ce qu'un ingrat ?",
        "Le contraire d'un g\xc3\xa9ant maigre."],
    [
        "Qu'est-ce qui p\xc3\xa8se 4 tonnes, a une trompe et est rouge vif?",
        'Un \xc3\xa9l\xc3\xa9phant qui a honte.'],
    [
        'Dans un virage \xc3\xa0 60 degr\xc3\xa9s \xc3\xa0 droite, quelle est la roue qui tourne le moins vite ?',
        'La roue de secours.'],
    [
        'Comment reconna\xc3\xaet-on un idiot dans un magasin de chaussures?',
        "C'est celui qui essaie les bo\xc3\xaetes."],
    [
        "Que dit-on d'un enfant qui ram\xc3\xa8ne le pain \xc3\xa0 la maison ?",
        "C'est le petit calepin."],
    [
        "Que dit la cacahu\xc3\xa8te \xc3\xa0 l'\xc3\xa9l\xc3\xa9phant ?",
        'Rien, les cacahu\xc3\xa8tes ne parlent pas.'],
    [
        "Que dit un \xc3\xa9l\xc3\xa9phant lorsqu'il se heurte \xc3\xa0 un autre \xc3\xa9l\xc3\xa9phant ?",
        "Le monde est petit, n'est-ce pas?"],
    [
        'Que dit la comptable \xc3\xa0 la machine \xc3\xa0 calculer ?',
        'Je compte sur toi.'],
    [
        'Que dit la puce \xc3\xa0 une autre puce ?',
        'On y va \xc3\xa0 pied ou on prend le chat ?'],
    [
        'Que dit la grande aiguille \xc3\xa0 la petite aiguille ?',
        'Attends une minute.'],
    [
        'Que dit une poule quand elle rencontre une autre poule ?',
        'Tu viens, on va prendre un ver ?'],
    [
        'Que dit le collant \xc3\xa0 la chaussure ?',
        '\xc3\x80 plus tard, je dois filer.'],
    [
        'Papa kangourou demande \xc3\xa0 sa fille qui rentre de l\'\xc3\xa9cole: "Alors, cet examen ?"',
        '"C\'est dans la poche, pas de probl\xc3\xa8me!"'],
    [
        'Quelle est la ville de France la plus f\xc3\xa9roce ?',
        'Lyon.'],
    [
        'Quelle est la ville de France la moins l\xc3\xa9g\xc3\xa8re ?',
        'Lourdes.'],
    [
        'Pourquoi porte-t-on des v\xc3\xaatements?',
        "Parce qu'ils ne peuvent pas marcher tout seuls."],
    [
        'Que dit une pomme de terre quand elle en voit une autre se faire \xc3\xa9craser dans la rue ?',
        '"Oh, pur\xc3\xa9e!"'],
    [
        "Que dit un petit fakir quand il arrive en retard \xc3\xa0 l'\xc3\xa9cole ?",
        '"Pardon ma\xc3\xaetresse, je me suis endormi sur le passage clout\xc3\xa9!"'],
    [
        "Que dit un marin-p\xc3\xaacheur s'il se dispute avec un autre marin-p\xc3\xaacheur ?",
        'Je ne veux pas que tu me parles sur ce thon!'],
    [
        'Pourquoi les cultivateurs disent-ils des gros mots \xc3\xa0 leurs tomates?',
        'Pour les faire rougir.'],
    [
        "Que disent deux vers de terre s'ils se rencontrent au milieu d'une pomme ?",
        '"Vous habitez dans le quartier ?"'],
    [
        "Qu'est-ce que se disent deux serpents qui se rencontrent ?",
        '"Quelle heure reptile ?"'],
    [
        'Pourquoi les mille-pattes ne peuvent-ils pas jouer au hockey?',
        "Le temps d'enfiler leurs patins, la partie est d\xc3\xa9j\xc3\xa0 termin\xc3\xa9e!"],
    [
        'Comment fait-on cuire un poisson dans un piano?',
        'On fait Do, R\xc3\xa9, La, Sol.'],
    [
        "Connaissez-vous l'histoire du chauffeur d'autobus?",
        "Moi non plus, j'\xc3\xa9tais \xc3\xa0 l'arri\xc3\xa8re!"],
    [
        'Crois-tu aux girafes?',
        "Non, c'est un cou mont\xc3\xa9."],
    [
        "Que dit un crocodile s'il rencontre un chien ?",
        'Salut, sac \xc3\xa0 puces!'],
    [
        'Que dit un chien quand il rencontre un crocodile ?',
        'Salut, sac \xc3\xa0 main!']]
MovieHealLaughterMisses = ('hmm', 'hou', 'ha', 'rhaa')
MovieHealLaughterHits1 = ('Ha ha ha', 'Hi hi', 'H\xc3\xa9 h\xc3\xa9', 'Ha ha')
MovieHealLaughterHits2 = ('OUARF OUARF OUARF!', 'HO HO HO!', 'HA HA HA!')
MovieSOSCallHelp = "%s \xc3\x80 L'AIDE!"
MovieSOSWhisperHelp = "%s a besoin d'aide pour un combat!"
MovieSOSObserverHelp = "\xc3\x80 L'AIDE!"
MovieNPCSOSGreeting = "Salut, %s! C'est un plaisir de pouvoir t'aider!"
MovieNPCSOSGoodbye = '\xc3\x80 plus tard!'
MovieNPCSOSToonsHit = 'Les Toons font toujours mouche!'
MovieNPCSOSCogsMiss = 'Les Cogs ratent toujours leurs cibles!'
MovieNPCSOSRestockGags = 'En train de faire le plein de gags %s!'
MovieNPCSOSHeal = 'Gu\xc3\xa9rison'
MovieNPCSOSTrap = 'Pi\xc3\xa9geage'
MovieNPCSOSLure = 'Leurre'
MovieNPCSOSSound = 'Tapage'
MovieNPCSOSThrow = 'Lancer'
MovieNPCSOSSquirt = '\xc3\x89claboussure'
MovieNPCSOSDrop = 'Chute'
MovieNPCSOSAll = 'Tout'
MoviePetSOSTrickFail = 'Soupir'
MoviePetSOSTrickSucceedBoy = 'Bon gar\xc3\xa7on!'
MoviePetSOSTrickSucceedGirl = 'Brave fifille!'
MovieSuitCancelled = 'ANNUL\xc3\x89\nANNUL\xc3\x89\nANNUL\xc3\x89'
RewardPanelToonTasks = 'D\xc3\xa9fitoons'
RewardPanelItems = 'Objets r\xc3\xa9cup\xc3\xa9r\xc3\xa9s'
RewardPanelMissedItems = 'Objets non r\xc3\xa9cup\xc3\xa9r\xc3\xa9s'
RewardPanelQuestLabel = 'Qu\xc3\xaate %s'
RewardPanelCongratsStrings = [
    'Ouais!',
    'Bravo!',
    'Ouah!',
    'Sympa!',
    'Atmosph\xc3\xa9rique!',
    'Toontastique!']
RewardPanelNewGag = 'Nouveau gag %(gagName)s pour %(avName)s!'
RewardPanelUberGag = '%(avName)s earned the %(gagName)s gag with %(exp)s experience points!'
RewardPanelEndTrack = 'Haa! %(avName)s a atteint la fin de la s\xc3\xa9rie de gags %(gagName)s!'
RewardPanelMeritsMaxed = 'Au maximum'
RewardPanelMeritBarLabels = [
    'Avis de licenciement',
    'Citations \xc3\xa0 compara\xc3\xaetre',
    'Euros Cog',
    'M\xc3\xa9rites']
RewardPanelMeritAlert = 'Pr\xc3\xaat pour la promotion!'
RewardPanelCogPart = 'Tu as gagn\xc3\xa9 un morceau de d\xc3\xa9guisement de Cog!'
RewardPanelPromotion = 'Pr\xc3\xa9parez pour la promotion %s voie!'
CheesyEffectDescriptions = [
    ('Toon normal', 'tu seras normal(e)'),
    ('Grosse t\xc3\xaate', 'tu auras une grosse t\xc3\xaate'),
    ('Petite t\xc3\xaate', 'tu auras une petite t\xc3\xaate'),
    ('Grosses jambes', 'tu auras de grosses jambes'),
    ('Petites jambes', 'tu auras de petites jambes'),
    ('Gros Toon', 'tu seras un peu plus gros(se)'),
    ('Petit Toon', 'tu seras un peu plus petit(e)'),
    ('\xc3\x80 plat', 'tu seras en deux dimensions'),
    ('Profil plat', 'tu seras en deux dimensions'),
    ('Transparent', 'tu seras transparent(e)'),
    ('Sans couleur', 'tu seras incolore'),
    ('Toon invisible', 'tu seras invisible')]
CheesyEffectIndefinite = "Jusqu'\xc3\xa0 ce que tu choisisses un autre effet, %(effectName)s%(whileIn)s."
CheesyEffectMinutes = 'Pendant les %(time)s prochaines minutes, %(effectName)s%(whileIn)s.'
CheesyEffectHours = 'Pendant les %(time)s prochaines heures, %(effectName)s%(whileIn)s.'
CheesyEffectDays = 'Pendant les %(time)s prochains jours, %(effectName)s%(whileIn)s.'
CheesyEffectWhileYouAreIn = ' pendant que tu es dans %s'
CheesyEffectExceptIn = ', except\xc3\xa9 dans %s'
SuitFlunky = 'Laquaistic'
SuitPencilPusher = 'Gratte-\npapier'
SuitYesman = 'B\xc3\xa9niouioui'
SuitMicromanager = 'Micro\x3chef'
SuitDownsizer = 'Touptisseur'
SuitHeadHunter = 'Chasset\xc3\xaate'
SuitCorporateRaider = 'Attactic'
SuitTheBigCheese = 'Gros Blochon'
SuitColdCaller = 'Cassepied'
SuitTelemarketer = 'T\xc3\xa9l\xc3\xa9\x3vendeur'
SuitNameDropper = 'Cafteur'
SuitGladHander = 'Passetout'
SuitMoverShaker = 'Secousse-\ncousse'
SuitTwoFace = 'Biface'
SuitTheMingler = 'Le Circulateur'
SuitMrHollywood = 'M. Hollywood'
SuitShortChange = 'Gardoseille'
SuitPennyPincher = 'Radino'
SuitTightwad = 'Grippesou'
SuitBeanCounter = 'Pince Menu'
SuitNumberCruncher = 'Gobechiffre'
SuitMoneyBags = 'Sacasous'
SuitLoanShark = 'Usurier'
SuitRobberBaron = 'Pillard'
SuitBottomFeeder = 'Volebas'
SuitBloodsucker = 'Pique-\nau-sang'
SuitDoubleTalker = 'Charabieur'
SuitAmbulanceChaser = 'Charognard'
SuitBackStabber = 'Frappedos'
SuitSpinDoctor = 'Tournegris'
SuitLegalEagle = 'Avocageot'
SuitBigWig = 'Chouffleur'
SuitFlunkyS = 'un Laquaistic'
SuitPencilPusherS = 'un Gratte-Papier'
SuitYesmanS = 'un B\xc3\xa9niouioui'
SuitMicromanagerS = 'un Microchef'
SuitDownsizerS = 'un Touptisseur'
SuitHeadHunterS = 'un Chasset\xc3\xaate'
SuitCorporateRaiderS = 'un Attactic'
SuitTheBigCheeseS = 'un Gros Blochon'
SuitColdCallerS = 'un Cassepied'
SuitTelemarketerS = 'un T\xc3\xa9l\xc3\xa9vendeur'
SuitNameDropperS = 'un Cafteur'
SuitGladHanderS = 'un Passetout'
SuitMoverShakerS = 'un Secousse-cousse'
SuitTwoFaceS = 'un Biface'
SuitTheMinglerS = 'un Circulateur'
SuitMrHollywoodS = 'un M. Hollywood'
SuitShortChangeS = 'un Gardoseille'
SuitPennyPincherS = 'un Radino'
SuitTightwadS = 'un Grippesou'
SuitBeanCounterS = 'un Pince-Menu'
SuitNumberCruncherS = 'un Gobechiffre'
SuitMoneyBagsS = 'un Sacasous'
SuitLoanSharkS = 'un Usurier'
SuitRobberBaronS = 'un Pillard'
SuitBottomFeederS = 'un Volebas'
SuitBloodsuckerS = 'un Pique-au-sang'
SuitDoubleTalkerS = 'un Charabieur'
SuitAmbulanceChaserS = 'un Charognard'
SuitBackStabberS = 'un Frappedos'
SuitSpinDoctorS = 'un Tournegris'
SuitLegalEagleS = 'un Avocageot'
SuitBigWigS = 'un Chouffleur'
SuitFlunkyP = 'Laquaistics'
SuitPencilPusherP = 'Gratte-Papiers'
SuitYesmanP = 'B\xc3\xa9niouiouis'
SuitMicromanagerP = 'Microchefs'
SuitDownsizerP = 'Touptisseurs'
SuitHeadHunterP = 'Chasset\xc3\xaates'
SuitCorporateRaiderP = 'Attactics'
SuitTheBigCheeseP = 'Gros Blochons'
SuitColdCallerP = 'Cassepieds'
SuitTelemarketerP = 'T\xc3\xa9l\xc3\xa9vendeurs'
SuitNameDropperP = 'Cafteurs'
SuitGladHanderP = 'Passetouts'
SuitMoverShakerP = 'Secousse-cousses'
SuitTwoFaceP = 'Bifaces'
SuitTheMinglerP = 'Les Circulateurs'
SuitMrHollywoodP = 'MM. Hollywood'
SuitShortChangeP = 'Gardoseilles'
SuitPennyPincherP = 'Radinos'
SuitTightwadP = 'Grippesous'
SuitBeanCounterP = 'Pince-Menus'
SuitNumberCruncherP = 'Gobechiffres'
SuitMoneyBagsP = 'Sacasous'
SuitLoanSharkP = 'Usuriers'
SuitRobberBaronP = 'Pillards'
SuitBottomFeederP = 'Volebas'
SuitBloodsuckerP = 'Pique-au-sang'
SuitDoubleTalkerP = 'Charabieurs'
SuitAmbulanceChaserP = 'Charognards'
SuitBackStabberP = 'Frappedos'
SuitSpinDoctorP = 'Tournegris'
SuitLegalEagleP = 'Avocageots'
SuitBigWigP = 'Chouffleurs'
SuitFaceOffDefaultTaunts = [
    'Bouh!']
SuitAttackDefaultTaunts = [
    'Prends \xc3\xa7a!',
    'Garde des notes l\xc3\xa0-dessus!']
SuitAttackNames = {
    'Audit': 'Audit!',
    'Bite': 'Morsure!',
    'BounceCheck': 'Ch\xc3\xa8que refus\xc3\xa9!',
    'BrainStorm': 'Remue-m\xc3\xa9ninges!',
    'BuzzWord': 'Mot \xc3\xa0 la mode!',
    'Calculate': '\xc3\x89valuation!',
    'Canned': 'En conserve!',
    'Chomp': 'Mastication!',
    'CigarSmoke': 'Fum\xc3\xa9e de cigare!',
    'ClipOnTie': 'Cravate toute faite!',
    'Crunch': '\xc3\x89crasement!',
    'Demotion': 'R\xc3\xa9trogradation!',
    'Downsize': 'Rapetissement!',
    'DoubleTalk': 'Charabia!',
    'EvictionNotice': "Ordre d'expulsion!",
    'EvilEye': 'Mauvais \xc5\x93il!',
    'Filibuster': 'Obstruction!',
    'FillWithLead': 'Plombage!',
    'FiveOClockShadow': 'Barbe naissante!',
    'FingerWag': 'Montr\xc3\xa9 du doigt!',
    'Fired': 'Liquid\xc3\xa9!',
    'FloodTheMarket': 'Invasion du march\xc3\xa9!',
    'FountainPen': 'Stylo-plume!',
    'FreezeAssets': 'Capital gel\xc3\xa9!',
    'Gavel': 'Adjug\xc3\xa9!',
    'GlowerPower': 'Regard furieux!',
    'GuiltTrip': 'Culpabilisation!',
    'HalfWindsor': 'N\xc5\x93ud de cravate!',
    'HangUp': 'Interruption!',
    'HeadShrink': 'R\xc3\xa9tr\xc3\xa9cissement de la t\xc3\xaate!',
    'HotAir': 'Air chaud!',
    'Jargon': 'Jargon!',
    'Legalese': 'Expression juridique!',
    'Liquidate': 'Liquidation!',
    'MarketCrash': 'Krach boursier!',
    'MumboJumbo': 'Baragouinage!',
    'ParadigmShift': 'Changement radical!',
    'PeckingOrder': 'Hi\xc3\xa9rarchie!',
    'PickPocket': 'Vol \xc3\xa0 la tire!',
    'PinkSlip': 'Avis de licenciement!',
    'PlayHardball': 'Grands moyens!',
    'PoundKey': 'Touche di\xc3\xa8se!',
    'PowerTie': 'Cravate ray\xc3\xa9e!',
    'PowerTrip': 'M\xc3\xa9galomanie!',
    'Quake': 'Tremblement!',
    'RazzleDazzle': 'Bringue!',
    'RedTape': 'Paperasserie!',
    'ReOrg': 'R\xc3\xa9organisation!',
    'RestrainingOrder': 'Injonction!',
    'Rolodex': 'Fichier rotatif!',
    'RubberStamp': 'Tampon!',
    'RubOut': 'Effacement!',
    'Sacked': 'Licenciement!',
    'SandTrap': 'Ensablement!',
    'Schmooze': 'Jacasserie!',
    'Shake': 'Secousse!',
    'Shred': 'D\xc3\xa9chiquetage!',
    'SongAndDance': 'Couplet habituel!',
    'Spin': 'Tournoiement!',
    'Synergy': 'Synergie!',
    'Tabulate': 'Tabulation!',
    'TeeOff': 'F\xc3\xa2cherie!',
    'ThrowBook': 'Maximum!',
    'Tremor': 'Fr\xc3\xa9missement!',
    'Watercooler': 'Boissons fra\xc3\xaeches!',
    'Withdrawal': 'Retrait!',
    'WriteOff': 'Pertes et profits!'}
SuitAttackTaunts = {
    'Audit': [
        "Je crois que ton bilan n'est pas \xc3\xa9quilibr\xc3\xa9.",
        'On dirait que tu es dans le rouge.',
        "Laisse-moi t'aider \xc3\xa0 faire ta comptabilit\xc3\xa9.",
        'Tes d\xc3\xa9bits sont beaucoup trop \xc3\xa9lev\xc3\xa9s.',
        'V\xc3\xa9rifions ton capital',
        'Tu vas avoir des dettes.',
        'Regardons de plus pr\xc3\xa8s ce que tu dois.',
        'Cela devrait mettre ton compte \xc3\xa0 sec.',
        'Il est temps que tu comptabilises tes d\xc3\xa9penses.',
        "J'ai trouv\xc3\xa9 une erreur dans ton bilan."],
    'Bite': [
        'Tu en veux une bouch\xc3\xa9e ?',
        "Essaye d'en mordre un morceau!",
        'Tu as les yeux plus gros que le ventre.',
        "Je mords plus que je n'aboie.",
        'Avale donc \xc3\xa7a!',
        'Attention, je pourrais mordre.',
        'Je ne fais pas que mordre quand je suis coinc\xc3\xa9.',
        "J'en veux juste une petite bouch\xc3\xa9e.",
        "Je n'ai rien aval\xc3\xa9 de la journ\xc3\xa9e.",
        "Je ne veux qu'un petit morceau. C'est trop demander ?"],
    'BounceCheck': [
        "Dommage, tu n'as pas d'humour.",
        'Tu as une \xc3\xa9ch\xc3\xa9ance de retard.',
        'Je crois que ce ch\xc3\xa8que est \xc3\xa0 toi.',
        "Tu m'es redevable.",
        'Je recouvre cette cr\xc3\xa9ance.',
        'Ce ch\xc3\xa8que ne va pas \xc3\xaatre un cadeau.',
        'Tu vas \xc3\xaatre factur\xc3\xa9 pour \xc3\xa7a.',
        'V\xc3\xa9rifie ce ch\xc3\xa8que.',
        '\xc3\x87a va te co\xc3\xbbter cher.',
        "J'aimerais bien encaisser \xc3\xa7a.",
        'Je vais simplement te renvoyer ton ch\xc3\xa8que.',
        'Voil\xc3\xa0 une facture sal\xc3\xa9e.',
        'Je d\xc3\xa9duis des frais de service.'],
    'BrainStorm': [
        'Je pr\xc3\xa9vois des perturbations.',
        "J'adore les casse-t\xc3\xaate.",
        "Je voudrais t'\xc3\xa9clairer.",
        "Qu'est-ce que tu penserais de la CHUTE de tes facult\xc3\xa9s?",
        'Que de m\xc3\xa9diocrit\xc3\xa9!',
        'Tu es pr\xc3\xaat(e) pour le grand d\xc3\xa9m\xc3\xa9nagement ?',
        "J'ai les neurones en feu.",
        '\xc3\x87a casse des briques.',
        "Rien de tel qu'un remue-m\xc3\xa9ninges."],
    'BuzzWord': [
        'Excuse-moi si je radote.',
        'Tu connais la derni\xc3\xa8re ?',
        'Tu peux piger \xc3\xa7a?',
        'Toonicoton!',
        'Laisse-moi en placer une.',
        'Je serai incontournablement clair.',
        'Tu as dit un mot de trop.',
        'Voyons si tu te situes en transversalit\xc3\xa9.',
        'Fais attention, \xc3\xa7a va \xc3\xaatre ringard.',
        "Je crois que tu vas faire de l'urticaire."],
    'Calculate': [
        'Le compte est bon!',
        'Tu comptais l\xc3\xa0-dessus?',
        'Ajoutes-en un peu, tu es en train de diminuer.',
        "Je peux t'aider \xc3\xa0 faire cette addition ?",
        'Tu as bien enregistr\xc3\xa9 toutes tes d\xc3\xa9penses?',
        "D'apr\xc3\xa8s mes calculs, tu n'en as plus pour longtemps.",
        'Voil\xc3\xa0 le total g\xc3\xa9n\xc3\xa9ral.',
        'Houl\xc3\xa0, ton addition est bien longue.',
        'Essaie de trafiquer ces chiffres!',
        Cogs + ' : 1 Toons: 0'],
    'Canned': [
        "Tu aimes quand c'est en bo\xc3\xaete ?",
        "Tu peux t'occuper des bo\xc3\xaetes?",
        'Celui-l\xc3\xa0 vient de sortir de sa bo\xc3\xaete!',
        'Tu as d\xc3\xa9j\xc3\xa0 \xc3\xa9t\xc3\xa9 attaqu\xc3\xa9 par des bo\xc3\xaetes de conserve ?',
        "J'aimerais te faire un cadeau qui se conserve!",
        'Tu es pr\xc3\xaat pour la mise en bo\xc3\xaete ?',
        'Tu crois que tu es bien conserv\xc3\xa9?',
        'Tu vas \xc3\xaatre emball\xc3\xa9!',
        "Je me fais du Toon \xc3\xa0 l'huile pour d\xc3\xaener!",
        "Tu n'es pas si mangeable que \xc3\xa7a en conserve."],
    'Chomp': [
        'Tu as une mine de papier m\xc3\xa2ch\xc3\xa9!',
        'Croc, croc, croc!',
        'On va pouvoir se mettre quelque chose sous la dent.',
        'Tu as besoin de grignoter quelque chose ?',
        'Tu pourrais grignoter \xc3\xa7a!',
        'Je vais te manger pour le d\xc3\xaener.',
        'Je me nourrirais bien de Toons!'],
    'ClipOnTie': [
        "Il faut s'habiller pour la r\xc3\xa9union.",
        'Tu ne peux PAS sortir sans ta cravate.',
        "C'est ce que portent les " + Cogs + ' les plus \xc3\xa9l\xc3\xa9gants.',
        'Essaie pour voir si la taille te va.',
        "Tu devrais mieux t'habiller pour r\xc3\xa9ussir.",
        'On ne sert que les clients portant une cravate.',
        "Tu as besoin d'aide pour enfiler \xc3\xa7a?",
        "Rien n'est plus flatteur qu'une belle cravate.",
        'Voyons si \xc3\xa7a te va.',
        '\xc3\x87a va te bouleverser.',
        "Il va falloir que tu t'habilles avant de SORTIR.",
        'Je crois que je vais te faire un n\xc5\x93ud de cravate.'],
    'Crunch': [
        'On dirait que tu es \xc3\xa9cras\xc3\xa9(e) par les \xc3\xa9v\xc3\xa9nements.',
        "C'est l'heure d'en \xc3\xa9craser!",
        'Je vais te donner quelque chose \xc3\xa0 pulv\xc3\xa9riser.',
        'Je vais broyer tout \xc3\xa7a.',
        "J'ai tout \xc3\xa9cras\xc3\xa9.",
        'Tu pr\xc3\xa9f\xc3\xa8res tendre ou croquant ?',
        "J'esp\xc3\xa8re que tu aimes les croque-monsieur.",
        'On dirait que tu es en train de te faire \xc3\xa9craser!',
        'Je vais te r\xc3\xa9duire en miettes.'],
    'Demotion': [
        "Tu descends sur l'\xc3\xa9chelle de la hi\xc3\xa9rarchie.",
        'Je te renvoie \xc3\xa0 trier le courrier.',
        'Il est temps de rendre tes galons.',
        'Tu descends, petit clown!',
        "On dirait qu'il y a un blocage.",
        'Tu progresses lentement.',
        'Tu es dans une voie sans issue.',
        "Tu n'iras nulle part dans l'imm\xc3\xa9diat.",
        'Tu ne vas nulle part.',
        "Cela sera port\xc3\xa9 sur ta fiche d'assiduit\xc3\xa9."],
    'Downsize': [
        'Redescends donc de l\xc3\xa0!',
        'Tu sais comment redescendre ?',
        'Revenons \xc3\xa0 nos affaires.',
        "Qu'est-ce qui ne va pas? Tu as l'air d'avoir le moral dans les chaussettes.",
        'Tu descends?',
        "Qu'est-ce qui te chiffonne ? Toi!",
        'Pourquoi est-ce que tu choisis des gens de ma taille ?',
        'Pourquoi es-tu si terre-\xc3\xa0-terre ?',
        'Est-ce que tu voudrais un mod\xc3\xa8le plus petit pour seulement dix cents de plus?',
        'Essaie pour voir si la taille te va!',
        'Ce mod\xc3\xa8le est disponible dans une plus petite taille.',
        "C'est une attaque \xc3\xa0 taille unique!"],
    'EvictionNotice': [
        "C'est l'heure de partir!",
        'Fais tes bagages, Toon.',
        "C'est le moment d'aller habiter ailleurs.",
        'Disons que ton bail est termin\xc3\xa9.',
        'Tu as un loyer de retard.',
        'Cela va \xc3\xaatre tr\xc3\xa8s d\xc3\xa9stabilisant.',
        "Tu vas \xc3\xaatre d\xc3\xa9racin\xc3\xa9 d'ici peu.",
        "Je vais t'envoyer sous les ponts.",
        "Tu n'es pas \xc3\xa0 ta place.",
        'Pr\xc3\xa9pare-toi \xc3\xa0 une d\xc3\xa9localisation.',
        "Tu vas subir un placement d'office."],
    'EvilEye': [
        'Je te donne le mauvais \xc5\x93il.',
        "Tu peux donner un coup d'\xc5\x93il \xc3\xa0 \xc3\xa7a pour moi?",
        "Attends. J'ai quelque chose dans l'\xc5\x93il.",
        "J'ai l'\xc5\x93il sur toi!",
        'Tu pourrais garder un \xc5\x93il sur \xc3\xa7a?',
        "J'ai vraiment l'\xc5\x93il pour voir ce qui cloche.",
        "Je vais te taper dans l'\xc5\x93il.",
        "J'ai le regard m\xc3\xa9chant!",
        "Tu vas te retrouver dans l'\xc5\x93il du cyclone!",
        'Je te regarde en roulant des yeux.'],
    'Filibuster': [
        'Est-ce que je dois te barrer la route ?',
        '\xc3\x87a va nous bloquer pendant un moment.',
        'Je pourrais rester coinc\xc3\xa9 l\xc3\xa0 toute la journ\xc3\xa9e.',
        "Je n'ai m\xc3\xaame pas besoin de respirer.",
        "J'avance et j'avance et j'avance.",
        "Je ne m'en fatigue jamais.",
        "On ne peut pas m'arr\xc3\xaater de parler.",
        'Tu peux te boucher les oreilles?',
        'Je crois que je vais te tenir la jambe.',
        'Je finis toujours par placer un mot.'],
    'FingerWag': [
        '\xc3\x87a fait mille fois que je te le r\xc3\xa9p\xc3\xa8te!',
        'Regarde bien l\xc3\xa0, Toon.',
        'Ne me fais pas rire.',
        "Ne m'oblige pas \xc3\xa0 y aller.",
        "J'en ai assez de r\xc3\xa9p\xc3\xa9ter la m\xc3\xaame chose.",
        "Je crois qu'on en a d\xc3\xa9j\xc3\xa0 parl\xc3\xa9.",
        "Tu n'as aucun respect pour nous les" + Cogs + '.',
        'Il est grand temps de faire attention.',
        'Blablablablabla.',
        "Ne m'oblige pas \xc3\xa0 mettre fin \xc3\xa0 cette r\xc3\xa9union.",
        'Est-ce que je vais devoir te s\xc3\xa9parer ?',
        'On est d\xc3\xa9j\xc3\xa0 pass\xc3\xa9s par l\xc3\xa0.'],
    'Fired': [
        "J'esp\xc3\xa8re que tu as apport\xc3\xa9 des rafra\xc3\xaechissements.",
        "On s'emb\xc3\xaate solide.",
        '\xc3\x87a va nous rafra\xc3\xaechir.',
        "J'esp\xc3\xa8re que tu as le sang froid.",
        "J'ai la gorge s\xc3\xa8che.",
        'Va donc nager un peu!',
        'Tu es d\xc3\xa9j\xc3\xa0 sur le d\xc3\xa9part.',
        'Encore un peu de sauce ?',
        'Tu peux dire "a\xc3\xafe"?',
        "J'esp\xc3\xa8re que tu sais nager.",
        'Tu es en phase de d\xc3\xa9shydratation ?',
        'Je vais te liquider!',
        'Tu vas finir en bouillie.',
        "Tu n'es qu'un feu de paille.",
        'Je me trouve fondant.',
        "Je suis d'une limpidit\xc3\xa9!",
        "Et on n'en parle plus !",
        'Un Toon \xc3\xa0 la mer !'],
    'FountainPen': [
        '\xc3\x87a va tacher.',
        'Mettons \xc3\xa7a par \xc3\xa9crit.',
        'Pr\xc3\xa9pare-toi \xc3\xa0 des ennuis ind\xc3\xa9l\xc3\xa9biles.',
        "Tu vas avoir besoin d'un bon nettoyage \xc3\xa0 sec.",
        'Tu devrais corriger.',
        'Ce stylo \xc3\xa9crit si bien.',
        'Voil\xc3\xa0, je prends mon crayon.',
        'Tu peux lire mon \xc3\xa9criture ?',
        "Et voil\xc3\xa0 la plume de l'apocalypse.",
        'Ta performance est entach\xc3\xa9e.',
        "Tu n'as pas envie de tout effacer ?"],
    'FreezeAssets': [
        'Ton capital est le mien.',
        'Tu ne sens pas un appel de fonds?',
        "J'esp\xc3\xa8re que tu n'as pas de projets.",
        'Cela devrait te mettre sur la paille.',
        "Le fond de l'air est frais.",
        "L'hiver va venir t\xc3\xb4t cette ann\xc3\xa9e.",
        'Tu as froid?',
        'Je vais geler mes projets.',
        'Tu vas trouver \xc3\xa7a froid.',
        'Tu vas avoir des engelures.',
        "J'esp\xc3\xa8re que tu aimes la viande froide.",
        'Je garde mon sang-froid.'],
    'GlowerPower': [
        'Tu me regardes?',
        "On me dit que j'ai une vue per\xc3\xa7ante.",
        "J'aime bien que tu sois \xc3\xa0 port\xc3\xa9e de mon regard.",
        "Tu n'aimes pas que je te regarde ?",
        'Voil\xc3\xa0, je te regarde.',
        "Tu ne trouves pas que j'ai un regard expressif?",
        'Mon regard est mon point fort.',
        "C'est le regard qui compte.",
        'Coucou, je te vois.',
        'Regarde-moi dans les yeux...',
        'Est-ce que tu voudrais voir ton avenir ?'],
    'GuiltTrip': [
        'Tu vas vraiment te sentir coupable!',
        'Tu te sens coupable!',
        "C'est enti\xc3\xa8rement de ta faute!",
        "C'est toujours ta faute.",
        'Tu te complais dans la culpabilit\xc3\xa9!',
        'Je ne te reparlerai plus jamais!',
        "Tu ferais mieux de t'excuser.",
        'Jamais je ne te pardonnerai!',
        'Tu veux bien te faire de la bile ?',
        'Rappelle-moi quand tu ne te sentiras plus coupable.',
        'Quand finiras-tu par te pardonner \xc3\xa0 toi-m\xc3\xaame ?'],
    'HalfWindsor': [
        "Tu ne t'es encore jamais fait cravater comme \xc3\xa7a!",
        'Essaye de ne pas trop faire de n\xc5\x93uds.',
        'Tu es dans une situation inextricable.',
        "Tu as de la chance, j'aurais pu faire un n\xc5\x93ud plus serr\xc3\xa9.",
        'Cette cravate est trop ch\xc3\xa8re pour toi.',
        "Je crois que tu n'as jamais m\xc3\xaame VU de n\xc5\x93ud de cravate!",
        'Cette cravate est trop ch\xc3\xa8re pour toi.',
        'Cette cravate serait g\xc3\xa2ch\xc3\xa9e, sur toi.',
        'Tu ne vaux m\xc3\xaame pas la moiti\xc3\xa9 du prix de cette cravate!'],
    'HangUp': [
        'Tu as \xc3\xa9t\xc3\xa9 d\xc3\xa9connect\xc3\xa9(e).',
        'Au revoir!',
        "C'est l'heure de mettre fin \xc3\xa0 notre conversation.",
        '...et ne me rappelle pas!',
        'Clic!',
        'La conversation est termin\xc3\xa9e.',
        'Je vais couper cette ligne.',
        'Je crois que nous allons \xc3\xaatre coup\xc3\xa9s.',
        'On dirait que la ligne est d\xc3\xa9fectueuse.',
        'Ton forfait est termin\xc3\xa9.',
        "J'esp\xc3\xa8re que tu m'entends clairement.",
        'Tu as fait le mauvais num\xc3\xa9ro.'],
    'HeadShrink': [
        'On dirait que tu as besoin de te faire soigner la t\xc3\xaate.',
        "Ch\xc3\xa9rie, j'ai r\xc3\xa9tr\xc3\xa9ci le Toon.",
        "J'esp\xc3\xa8re que \xc3\xa7a ne t'est pas mont\xc3\xa9 \xc3\xa0 la t\xc3\xaate.",
        'Tu r\xc3\xa9tr\xc3\xa9cis au lavage ?',
        'Je r\xc3\xa9tr\xc3\xa9cis donc je suis.',
        "Il n'y a pas de quoi perdre la t\xc3\xaate.",
        'O\xc3\xb9 as-tu la t\xc3\xaate ?',
        'Rel\xc3\xa8ve la t\xc3\xaate! Ou plut\xc3\xb4t, mets-la par terre.',
        "Les choses sont parfois plus grandes qu'elles ne paraissent.",
        'Les bons Toons se vendent par petits paquets.'],
    'HotAir': [
        'Nous avons de chaudes discussions.',
        'Tu subis une vague de chaleur.',
        "J'ai atteint mon point d'\xc3\xa9bullition.",
        'Cela pourrait te br\xc3\xbbler.',
        'Je d\xc3\xa9testerais te passer au gril, mais...',
        "N'oublie pas qu'il n'y a pas de fum\xc3\xa9e sans feu.",
        "Tu m'as l'air un peu grill\xc3\xa9(e).",
        "C'est encore un \xc3\xa9cran de fum\xc3\xa9e.",
        "C'est le moment de mettre de l'huile sur le feu.",
        "Allumons le feu de l'amiti\xc3\xa9.",
        "J'ai des remarques br\xc3\xbblantes \xc3\xa0 te faire.",
        'Air chaud!'],
    'Jargon': [
        'Quel non-sens.',
        'Regarde si tu peux trouver du sens \xc3\xa0 tout \xc3\xa7a.',
        "J'esp\xc3\xa8re que tu m'entends clairement.",
        'On dirait que je vais devoir \xc3\xa9lever la voix.',
        "J'ai vraiment mon mot \xc3\xa0 dire.",
        "J'ai mon franc-parler.",
        'Je vais pontifier sur ce sujet.',
        'Tu sais, les mots peuvent faire mal.',
        'Tu as compris ce que je voulais dire ?',
        'Des mots, rien que des mots.'],
    'Legalese': [
        "Tu dois cesser d'\xc3\xaatre et renoncer.",
        'Tu vas \xc3\xaatre d\xc3\xa9bout\xc3\xa9(e), l\xc3\xa9galement parlant.',
        'Tu es au courant des implications l\xc3\xa9gales?',
        "Tu n'es pas au-dessus des lois!",
        'Il devrait y avoir une loi contre toi.',
        "Il n'y a rien de post\xc3\xa9rieur aux faits!",
        "Toontown Online de Disney n'est pas l\xc3\xa9galement responsable des opinions exprim\xc3\xa9es dans cette attaque.",
        'Nous ne serons pas tenus responsables des dommages subis suite \xc3\xa0 cette attaque.',
        'Les r\xc3\xa9sultats de cette attaque peuvent diff\xc3\xa9rer.',
        "Cette attaque est nulle l\xc3\xa0 o\xc3\xb9 elle n'est pas autoris\xc3\xa9e.",
        'Tu ne rentres pas dans mon syst\xc3\xa8me l\xc3\xa9gislatif.',
        'Tu ne peux pas g\xc3\xa9rer les questions juridiques.'],
    'Liquidate': [
        "J'aime bien que les choses restent fluides.",
        'As-tu des probl\xc3\xa8mes de liquidit\xc3\xa9s?',
        'Je dois purger ton capital.',
        'Il est temps pour toi de suivre le flux mon\xc3\xa9taire.',
        "N'oublie pas que \xc3\xa7a glisse quand c'est mouill\xc3\xa9.",
        'Il y a des fuites dans ta comptabilit\xc3\xa9.',
        "Tu as l'air de perdre pied.",
        'Tout te tombe dessus.',
        'Je crois que tu vas subir une dilution.',
        'Tu es lessiv\xc3\xa9(e).'],
    'MarketCrash': [
        'Tu vas avoir un choc.',
        'Tu ne survivras pas au choc.',
        "C'est plus que la bourse ne peut en supporter.",
        "J'ai un traitement de choc pour toi!",
        'Maintenant je vais te faire un choc.',
        "Je m'attends \xc3\xa0 un choc boursier.",
        'On dirait que le march\xc3\xa9 est sur la pente descendante.',
        'Il vaudrait mieux que tu te retires du jeu!',
        'Vends! Vends! Vends!',
        'Est-ce que je dois mener la r\xc3\xa9cession ?',
        "Tout le monde s'enfuit, tu devrais peut-\xc3\xaatre en faire autant ?"],
    'MumboJumbo': [
        'Que ce soit parfaitement clair.',
        "C'est aussi simple que \xc3\xa7a.",
        "C'est comme cela que nous allons proc\xc3\xa9der.",
        "Laisse-moi te l'\xc3\xa9crire en grosses lettres.",
        "C'est du jargon technique.",
        "Ma parole est d'argent.",
        "J'en ai plein la bouche.",
        'On dit que je suis grandiloquent.',
        'Je vais interjeter \xc3\xa7a.',
        'Je crois que ce sont les mots ad\xc3\xa9quats.'],
    'ParadigmShift': [
        'Fais attention! Je suis plut\xc3\xb4t changeant.',
        'Pr\xc3\xa9pare-toi pour un changement radical!',
        'Voil\xc3\xa0 donc des substitutions int\xc3\xa9ressantes.',
        "Tu n'es pas \xc3\xa0 ta place.",
        "C'est ton tour de changer de place.",
        'Ton temps de pr\xc3\xa9sence est termin\xc3\xa9.',
        "Tu n'as encore jamais autant chang\xc3\xa9 dans ta vie.",
        'Voil\xc3\xa0 qui est radical!',
        'La lumi\xc3\xa8re est changeante!'],
    'PeckingOrder': [
        'Pauvre sous-fifre!',
        "Tu vas te retrouver le bec dans l'eau.",
        "Tu vas te retrouver en bas de l'\xc3\xa9chelle.",
        "Ce n'est pas une attaque de d\xc3\xa9butant.",
        'Tu es tout en bas de la hi\xc3\xa9rarchie.',
        'Je vaux bien plus cher que toi!',
        "La hi\xc3\xa9rarchie, il n'y a que \xc3\xa7a de vrai!",
        "Pourquoi est-ce que je ne trouve pas d'adversaire \xc3\xa0 ma taille ? Bof.",
        '\xc3\x80 moi le pouvoir!'],
    'PickPocket': [
        'Laisse-moi v\xc3\xa9rifier tes valeurs.',
        "Eh, c'est quoi par ici?",
        "C'est comme faucher les jouets d'un enfant.",
        "C'est du vol.",
        'Je te garde \xc3\xa7a.',
        'Ne l\xc3\xa2che pas mes mains des yeux.',
        'Mes mains sont plus rapides que tes yeux.',
        "Je n'ai rien dans la manche.",
        "La direction n'est pas responsable des objets perdus.",
        'Qui trouve garde.',
        'Tu ne le verras jamais revenir.',
        'Tout pour moi, rien pour toi.',
        '\xc3\x87a ne te g\xc3\xaane pas que \xc3\xa7a me g\xc3\xaane ?',
        "Tu n'en auras plus besoin..."],
    'PinkSlip': [
        "On n'a pas besoin de ton avis.",
        'Tu as peur de cette vague de licenciements?.',
        "Celui-l\xc3\xa0 va s\xc3\xbbrement \xc3\xaatre d'un avis contraire.",
        'Oh, tu as une licence de quoi?',
        'Fais attention, si tu veux mon avis!',
        "N'oublie pas que \xc3\xa7a glisse \xc3\xa0 mon avis.",
        'Je vais juste te renvoyer celui-l\xc3\xa0.',
        'Tu ne te f\xc3\xa2cheras pas si je te donne mon avis?',
        "Tu ne vois pas l'avis en rose.",
        'Tu peux sortir, je te licencie.'],
    'PlayHardball': [
        'Tu veux employer les grands moyens?',
        "N'essaie pas d'employer tous les moyens avec moi.",
        'Ne prends pas tes grands airs!',
        'Tu es vraiment moyen(ne).',
        'Et voil\xc3\xa0 le bon moyen...',
        "Tu vas avoir besoin d'un bon moyen pour t'en sortir.",
        "Je vais te chasser d'ici \xc3\xa0 grande vitesse.",
        "Une fois que je t'aurai touch\xc3\xa9(e), tu rentreras en courant chez toi.",
        "C'est ton grand d\xc3\xa9part!",
        'Ton jeu est tr\xc3\xa8s moyen.',
        'Je vais tout faire pour que tu sortes.',
        "Je t'envoie promener dans les grandes largeurs!"],
    'PoundKey': [
        'Il est temps que je r\xc3\xa9ponde \xc3\xa0 quelques appels.',
        "J'aimerais faire un appel en PCV.",
        "Dring dring, c'est pour toi!",
        'Je vais bien toucher quelque chose.',
        'Je devais te rappeler.',
        'Cela devrait provoquer une sonnerie.',
        'Je vais juste faire ce num\xc3\xa9ro.',
        "Je t'appelle pour te faire une surprise.",
        "Je vais t'appeler.",
        "All\xc3\xb4 Toon, c'est pour toi."],
    'PowerTie': [
        "Je t'appellerai plus tard, tu as l'air d'avoir un n\xc5\x93ud \xc3\xa0 l'estomac.",
        'Tu te pr\xc3\xa9pares \xc3\xa0 faire un trait l\xc3\xa0-dessus?',
        'Tu vas te faire cravater.',
        "Tu ferais mieux d'apprendre \xc3\xa0 faire un n\xc5\x93ud de cravate.",
        'Je vais te nouer la langue!',
        "Tu n'as encore jamais vu quelqu'un se faire cravater comme \xc3\xa7a!",
        'Tu fais attention aux rayures?',
        'Je vais te rayer de la carte!',
        'Je rayonne!',
        'Par les pouvoirs qui me sont conf\xc3\xa9r\xc3\xa9s, je te raie de la liste.'],
    'PowerTrip': [
        'Fais tes valises, on fait un m\xc3\xa9ga voyage.',
        "Tu n'as pas perdu tes manies?",
        "C'est une manie que tu as de partir en vacances.",
        'Comment se sont pass\xc3\xa9es les vacances?',
        "C'est une vraie manie!",
        "\xc3\x87a a l'air m\xc3\xa9ga ennuyeux.",
        'Maintenant tu vois qui est le plus puissant!',
        'Je suis bien plus puissant que toi.',
        'Qui a les m\xc3\xa9ga pouvoirs maintenant ?',
        'Tu ne peux pas te battre contre ma puissance.',
        'La puissance est corrompue, en particulier dans mon cas.'],
    'Quake': [
        'Tremblons, mes fr\xc3\xa8res.',
        "J'ai la tremblote!",
        'Je te vois trembler dans tes chaussures.',
        'Voil\xc3\xa0 la terre qui tremble!',
        "Celui-ci est en-dehors de l'\xc3\xa9chelle de Richter.",
        'La terre va trembler!',
        "H\xc3\xa9, qu'est-ce qui tremble comme \xc3\xa7a? Toi!",
        'Tu as d\xc3\xa9j\xc3\xa0 ressenti un tremblement de terre ?',
        'Tu es sur un terrain instable!'],
    'RazzleDazzle': [
        'Chante avec moi.',
        'Tu as peur de perdre ton dentier ?',
        'Je ne suis pas charmant ?',
        "Je vais t'impressionner.",
        'Mon dentiste fait un excellent travail.',
        'Ils ne sont pas \xc3\xa9patants?',
        "Difficile de croire qu'ils ne sont pas r\xc3\xa9els.",
        'Ils ne sont pas choquants?',
        '\xc3\x87a va d\xc3\xa9coiffer.',
        'Je me lave les dents apr\xc3\xa8s tous les repas.',
        'Dis "Cheese!"'],
    'RedTape': [
        '\xc3\x87a va \xc3\xaatre bien emball\xc3\xa9.',
        'Tu vas rester coll\xc3\xa9(e) l\xc3\xa0 un bon moment.',
        "J'en ai un plein rouleau.",
        'On va voir si tu peux y couper.',
        '\xc3\x87a va devenir collant.',
        "J'esp\xc3\xa8re que tu es claustrophobe.",
        "Tu es d'un temp\xc3\xa9rament collant!",
        "Je vais t'occuper un peu.",
        'Essaie donc de sortir de l\xc3\xa0.',
        'On va voir si \xc3\xa7a colle entre nous.'],
    'ReOrg': [
        "Tu n'aimes pas la mani\xc3\xa8re dont j'ai r\xc3\xa9organis\xc3\xa9 les choses?",
        "Peut-\xc3\xaatre qu'un peu plus d'organisation serait de mise.",
        "Tout n'est pas si mauvais, tu as juste un peu besoin de r\xc3\xa9organisation.",
        "Est-ce que tu appr\xc3\xa9cies mes capacit\xc3\xa9s d'organisation ?",
        "J'essaye juste de donner un nouvel aspect aux choses.",
        "Tu dois t'organiser!",
        "Tu m'as l'air de faire dans la d\xc3\xa9sorganisation.",
        'Reste l\xc3\xa0 pendant que je te r\xc3\xa9organise.',
        "Je vais attendre que tu aies le temps de t'organiser.",
        '\xc3\x87a ne te d\xc3\xa9range pas si je r\xc3\xa9organise un peu?'],
    'RestrainingOrder': [
        'Tu devrais faire la jonction.',
        "Je t'ass\xc3\xa8ne une injonction!",
        "Tu n'as pas le droit de t'approcher \xc3\xa0 moins de deux m\xc3\xa8tres de moi.",
        'Tu ferais peut-\xc3\xaatre mieux de garder tes distances.',
        'Tu devrais avoir une injonction.',
        Cogs + '! Ma\xc3\xaetrisez ce Toon!Essaie de te ma\xc3\xaetriser.',
        "J'esp\xc3\xa8re que je ne suis pas trop une contrainte pour toi.",
        'Voyons si tu peux te lib\xc3\xa9rer de ces contraintes!',
        "Je te donne l'injonction de te ma\xc3\xaetriser!",
        'Pourquoi ne commen\xc3\xa7ons-nous pas par les contraintes de base ?'],
    'Rolodex': [
        'Ta fiche est quelque part l\xc3\xa0-dedans.',
        'Voil\xc3\xa0 la fiche de la chasse aux nuisibles.',
        'Je vais te donner une fiche.',
        'Ton num\xc3\xa9ro est juste l\xc3\xa0.',
        'Je te couvre de A \xc3\xa0 Z.',
        'Tu vas avoir la t\xc3\xaate qui tourne.',
        'Va donc faire un tour.',
        'Attention aux bouts de papier.',
        "J'ai des doigts pour trier.",
        "Est-ce que c'est comme \xc3\xa7a que je peux te contacter ?",
        'Je voudrais \xc3\xaatre certain que nous allons rester en contact.'],
    'RubberStamp': [
        'Je fais toujours bonne impression.',
        'Il est important de bien appuyer.',
        'Une impression parfaite \xc3\xa0 chaque fois.',
        'Je voudrais que tu imprimes.',
        "Tu dois \xc3\xaatre RETOURN\xc3\x89 \xc3\xa0 L'ENVOYEUR.",
        'Tu es dans la pile ANNUL\xc3\x89.',
        'Tu es en livraison PRIORITAIRE.',
        'Je voudrais \xc3\xaatre certain que tu as RE\xc3\x87U mon message!',
        'Tu ne vas nulle part - tu es en PORT PAY\xc3\x89 par le DESTINATAIRE.',
        'Je veux une r\xc3\xa9ponse URGENTE.'],
    'RubOut': [
        'Et maintenant un acte de disparition.',
        "J'ai l'impression de t'avoir perdu quelque part.",
        "J'ai d\xc3\xa9cid\xc3\xa9 de te gommer.",
        'Je gomme toujours tous les obstacles.',
        'Je vais simplement effacer cette erreur.',
        'Je peux faire dispara\xc3\xaetre tous les ennuis.',
        "J'aime les choses nettes et propres.",
        'Essaie de mettre la gomme.',
        'Je te vois...je ne te vois plus.',
        'Cela va finir par p\xc3\xa2lir.',
        'Je vais \xc3\xa9liminer le probl\xc3\xa8me.',
        "Laisse-moi m'occuper de tes zones \xc3\xa0 probl\xc3\xa8mes."],
    'Sacked': [
        'On dirait que tu vas te faire licencier.',
        "L'affaire est dans le sac.",
        'Tu as une licence de vol?',
        'De chasse ou de p\xc3\xaache ?',
        'Mes ennemis vont \xc3\xaatre \xc3\xa0 la porte!',
        "J'ai le record de Toontown pour les licenciements.",
        "On n'a plus besoin de toi ici.",
        'Tu as pass\xc3\xa9 assez de temps ici, tu es renvoy\xc3\xa9(e)!',
        'Laisse-moi te mettre en bo\xc3\xaete.',
        'Tu ne peux pas te d\xc3\xa9fendre si je veux te mettre dehors!'],
    'Schmooze': [
        'Tu ne verras jamais \xc3\xa7a venir.',
        '\xc3\x87a fera bien sur toi.',
        'Tu as gagn\xc3\xa9 \xc3\xa7a.',
        'Je ne voulais pas baver.',
        'La flatterie m\xc3\xa8ne partout.',
        'Je vais en rajouter une couche.',
        "C'est le moment d'en rajouter.",
        'Je vais me mettre de ton bon c\xc3\xb4t\xc3\xa9!',
        '\xc3\x87a m\xc3\xa9rite une bonne tape dans le dos.',
        'Je vais chanter tes louanges.',
        'Je suis navr\xc3\xa9 de te faire tomber de ton pi\xc3\xa9destal, mais...'],
    'Shake': [
        "Tu es juste \xc3\xa0 l'\xc3\xa9picentre.",
        'Tu es juste sur une faille.',
        '\xc3\x87a va secouer.',
        "Je crois que c'est une catastrophe naturelle.",
        "C'est un d\xc3\xa9sastre de proportions sismiques.",
        "Celui-ci est en dehors de l'\xc3\xa9chelle de Richter.",
        "C'est le moment de se mettre \xc3\xa0 l'abri.",
        'Tu as un air troubl\xc3\xa9.',
        'Attention la secousse!',
        'Je vais te secouer, pas te faire tourner.',
        '\xc3\x87a devrait te secouer.',
        "J'ai un bon plan pour s'\xc3\xa9chapper."],
    'Shred': [
        'Je dois me d\xc3\xa9barrasser de quelques d\xc3\xa9chets.',
        "J'augmente ma capacit\xc3\xa9 de traitement.",
        'Je crois que je vais me d\xc3\xa9barrasser de toi maintenant.',
        'On va pouvoir d\xc3\xa9truire les preuves.',
        "Il n'y a plus aucune fa\xc3\xa7on de prouver \xc3\xa7a maintenant.",
        'Vois si tu peux assembler toutes les pi\xc3\xa8ces.',
        'Cela devrait te remettre \xc3\xa0 la bonne taille.',
        'Je vais jeter cette id\xc3\xa9e.',
        'Il ne faut pas que \xc3\xa7a tombe entre de mauvaises mains.',
        'Vite venu, vite parti.',
        "Ce n'est pas ton dernier fragment d'espoir ?"],
    'Spin': [
        "Tu veux qu'on aille faire un tour ?",
        '\xc3\x80 quelle vitesse tournes-tu?',
        '\xc3\x87a va te faire tourner la t\xc3\xaate!',
        "C'est le tour que prennent les choses.",
        "Je vais t'emmener faire un tour.",
        'Que feras-tu quand ce sera ton tour ?',
        'Surveille-moi \xc3\xa7a. Je ne voudrais pas que \xc3\xa7a tourne trop vite!',
        'Tu vas tourner longtemps comme \xc3\xa7a?',
        'Mes attaques vont te donner le tournis!'],
    'Synergy': [
        'Je transmets cela au comit\xc3\xa9.',
        'Ton projet a \xc3\xa9t\xc3\xa9 annul\xc3\xa9.',
        'Ton budget a \xc3\xa9t\xc3\xa9 r\xc3\xa9duit.',
        'Nous allons restructurer ton service.',
        "J'ai mis \xc3\xa7a au vote et tu as perdu.",
        "Je viens de recevoir l'accord final.",
        "Il n'y a pas de probl\xc3\xa8mes, il n'y a que des solutions.",
        'Je te recontacte \xc3\xa0 ce sujet.',
        'Revenons \xc3\xa0 cette affaire.',
        "Consid\xc3\xa8re que c'est un manque de synergie."],
    'Tabulate': [
        "\xc3\x87a ne s'additionne pas!",
        'Si je compte bien, tu as perdu.',
        'Tu comptes bien toutes les colonnes.',
        'Je te fais le total dans un instant.',
        'Tu es pr\xc3\xaat(e) \xc3\xa0 compter tout \xc3\xa7a?',
        'Ta facture est payable d\xc3\xa8s maintenant.',
        'Il est temps de faire une estimation.',
        "J'aime bien mettre les choses en ordre.",
        'Et les r\xc3\xa9sultats au pointage sont...',
        'Ces chiffres devraient \xc3\xaatre tr\xc3\xa8s puissants.'],
    'TeeOff': [
        'Tu ne fais pas le poids.',
        'Gare \xc3\xa0 toi!',
        'Je suis vex\xc3\xa9.',
        'Pourquoi es-tu en col\xc3\xa8re ?',
        "Essaye simplement d'\xc3\xa9viter le danger.",
        'Scrongneugneu!',
        'Tu vas prendre la mouche \xc3\xa0 tous les coups.',
        'Tu es sur mon chemin.',
        "J'ai une bonne prise sur la situation.",
        'Attention le petit oiseau va se f\xc3\xa2cher!',
        'Garde un \xc5\x93il sur moi!',
        '\xc3\x87a te d\xc3\xa9range si je joue ?'],
    'Tremor': [
        'Tu as senti \xc3\xa7a?',
        "Tu n'as pas peur d'un petit fr\xc3\xa9missement n'est-ce pas?",
        'Au commencement \xc3\xa9tait le fr\xc3\xa9missement.',
        "Tu as l'air de trembler.",
        'Je vais un peu secouer les choses!',
        'Tu te pr\xc3\xa9pare \xc3\xa0 sursauter ?',
        "Qu'est-ce qui ne va pas? Tu as l'air d'accuser la secousse.",
        'Crainte et tremblements!',
        'Pourquoi trembles-tu de peur ?'],
    'Watercooler': [
        '\xc3\x87a devrait te rafra\xc3\xaechir.',
        'Tu ne trouves pas \xc3\xa7a rafra\xc3\xaechissant ?',
        'Je livre les boissons.',
        'Directement du robinet dans ton gosier.',
        "C'est quoi le probl\xc3\xa8me, c'est juste de l'eau de source.",
        "Ne t'inqui\xc3\xa8te pas, c'est filtr\xc3\xa9.",
        'Ah, un autre client satisfait.',
        "C'est l'heure de ta livraison quotidienne.",
        "J'esp\xc3\xa8re que les couleurs ne vont pas d\xc3\xa9teindre.",
        'Tu as envie de boire ?',
        "Tout s'en va \xc3\xa0 la lessive.",
        "C'est toi qui paies \xc3\xa0 boire."],
    'Withdrawal': [
        'Je crois que tu es \xc3\xa0 d\xc3\xa9couvert.',
        "J'esp\xc3\xa8re que ton compte est suffisamment approvisionn\xc3\xa9.",
        'Prends \xc3\xa7a, avec les int\xc3\xa9r\xc3\xaats.',
        "Ton solde n'est pas en \xc3\xa9quilibre.",
        'Tu vas bient\xc3\xb4t devoir faire un d\xc3\xa9p\xc3\xb4t.',
        'Tu as souffert de la r\xc3\xa9cession \xc3\xa9conomique.',
        'Je crois que tu as un passage \xc3\xa0 vide.',
        'Tes finances sont sur le d\xc3\xa9clin.',
        'Je pr\xc3\xa9vois une baisse d\xc3\xa9finitive.',
        "C'est un revers de fortune."],
    'WriteOff': [
        'Laisse-moi augmenter tes pertes.',
        "Profitons d'une mauvaise affaire.",
        "C'est l'heure d'\xc3\xa9quilibrer les comptes.",
        '\xc3\x87a ne va pas faire bien dans ton bilan.',
        'Je suis \xc3\xa0 la recherche de quelques dividendes.',
        'Tu dois tenir compte de tes pertes.',
        'Tu peux oublier les bonus.',
        'Je vais m\xc3\xa9langer tes comptes.',
        'Tu vas avoir quelques pertes.',
        '\xc3\x87a va te faire mal au solde.']}
BuildingWaitingForVictors = ('En attente des autres joueurs...',)
ElevatorHopOff = 'Quitter'
CogsIncExt = ' SA'
CogsIncModifier = '%s' + CogsIncExt
CogsInc = string.upper(Cogs) + CogsIncExt
DoorKnockKnock = 'Toc, toc.'
DoorWhosThere = 'Qui est l\xc3\xa0?'
DoorWhoAppendix = 'qui?'
DoorNametag = 'Porte'
FADoorCodes_UNLOCKED = None
FADoorCodes_TALK_TO_TOM = 'Tu as besoin de gags! Va en parler \xc3\xa0 Tom Tuteur!'
FADoorCodes_DEFEAT_FLUNKY_HQ = 'Reviens ici quand tu auras vaincu le Laquaistic!'
FADoorCodes_TALK_TO_HQ = "Va chercher ta r\xc3\xa9compense aupr\xc3\xa8s d'Harry au QG!"
FADoorCodes_WRONG_DOOR_HQ = "Mauvaise porte! Prends l'autre porte pour aller au terrain de jeux!"
FADoorCodes_GO_TO_PLAYGROUND = 'Mauvais chemin! Tu dois aller au terrain de jeux!'
FADoorCodes_DEFEAT_FLUNKY_TOM = "Marche jusqu'\xc3\xa0 ce Laquaistic pour te battre avec lui!"
FADoorCodes_TALK_TO_HQ_TOM = 'Va chercher ta r\xc3\xa9compense au QG des Toons!'
FADoorCodes_SUIT_APPROACHING = None
FADoorCodes_BUILDING_TAKEOVER = 'Fais attention! Il y a un COG l\xc3\xa0-dedans!'
FADoorCodes_DISGUISE_INCOMPLETE = "Tu vas te faire attraper si tu rentres l\xc3\xa0-dedans habill\xc3\xa9 en Toon! Tu dois d'abord terminer ton d\xc3\xa9guisement de Cog!n\nConstruis ton d\xc3\xa9guisement de Cog avec des pi\xc3\xa8ces de l'usine."
FADoorCodes_SB_DISGUISE_INCOMPLETE = "Tu vas te faire attraper si tu rentres l\xc3\xa0-dedans habill\xc3\xa9 en Toon! Tu dois d'abord terminer ton d\xc3\xa9guisement de Cog!n\nConstruis ton d\xc3\xa9guisement de Cog avec des pi\xc3\xa8ces de l'usine."
FADoorCodes_CB_DISGUISE_INCOMPLETE = "Tu vas te faire prendre si tu entres ici en Toon! Tu dois d'abord terminer ton d\xc3\xa9guisement de Caissbot!\n\nTermine ton d\xc3\xa9guisement de Caissbot en r\xc3\xa9ussissant des d\xc3\xa9fitoons au Pays des R\xc3\xaaves."
FADoorCodes_LB_DISGUISE_INCOMPLETE = "Tu vas te faire attraper si tu rentres l\xc3\xa0-dedans habill\xc3\xa9 en Toon! Tu dois d'abord terminer ton d\xc3\xa9guisement de Loibot !\n\nAssemble ton d\xc3\xa9guisement de Loibot en terminant les d\xc3\xa9fitoons qui sont apr\xc3\xa8s le Pays des R\xc3\xaaves de Donald."
KnockKnockContestJokes = {
    2100: [
        'Tank',
        'Tank il ne regarde pas, lance-lui un g\xc3\xa2teau!'],
    2200: [
        'Audrey',
        "Audrey mieux sortir d'ici, voil\xc3\xa0 les Cogs qui arrivent!"],
    2300: [
        'Hadrien',
        'Hadrien que quelques pi\xc3\xa8ces Cog et on y va!'],
    3300: {
        10: [
            'Aladdin',
            'Aladdin mauvais go\xc3\xbbt...'],
        6: [
            'Bidule',
            "Bidule sais pas, d'o\xc3\xb9 ils viennent tous ces Cogs?"],
        30: [
            'Jambon',
            'Jambon, ils sont m\xc3\xaame tr\xc3\xa8s bons ces g\xc3\xa2teaux pour les Cogs.'],
        28: [
            'Isa\xc3\xafe',
            'Isa\xc3\xafe \xc3\xa0 la gare pour aller faire un tour de tramway.'],
        12: [
            'Jules',
            'Jules aurait pari\xc3\xa9, tu vas me laisser entrer dans un b\xc3\xa2timent Cog et je te donnerai un toonique.']}}
KnockKnockJokes = [
    [
        'Qui',
        "Il y a un mauvais \xc3\xa9cho par ici, n'est-ce pas?"],
    [
        'Douglas',
        "Douglas \xc3\xa0 la vanille \xc3\xa7a t'int\xc3\xa9resse ?"],
    [
        'Geoffrey',
        'Geoffrey bien une petite sieste, laisse-moi entrer.'],
    [
        'Justin',
        'Justin petit moment.'],
    [
        'Adh\xc3\xa9mar',
        'Adh\xc3\xa9mar pas ta voiture ?'],
    [
        'Annie',
        "Annie rien comprendre, pourquoi tu n'ouvres pas?"],
    [
        'Omer',
        "Omer veille, j'ai fini par te trouver."],
    [
        'Th\xc3\xa9r\xc3\xa8se',
        "Th\xc3\xa9r\xc3\xa8se, t'es l\xc3\xa0 sans bouger depuis tout ce temps?"],
    [
        'Sylvie',
        "Sylvie c'est un miracle, laisse-le au moins entrer."],
    [
        'Aude',
        'Aude toilette \xc3\xa0 la lavande ce matin ?'],
    [
        'Alex',
        "Alex T\xc3\xa9rieur, j'ai froid dehors."],
    [
        'Alain',
        'Alain T\xc3\xa9rieur, je voudrais entrer!'],
    [
        'Justine',
        "Justine petite minute, je n'en ai pas pour longtemps."],
    [
        'Vincent',
        'Vincent rien, et repart sans rien.'],
    [
        'Jean',
        "Jean ai marre que tu n'ouvres pas cette porte!"],
    [
        'Firmin',
        "Firmin peu la radio tu m'entendrais mieux."],
    [
        'Geoffroy',
        'Geoffroy dehors laisse-moi entrer.'],
    [
        'Jessica',
        'Jessica difficiles \xc3\xa0 traiter, d\xc3\xa9p\xc3\xaache-toi un peu.'],
    [
        'Djamila',
        'Djamila cl\xc3\xa9 sous la porte.'],
    [
        'Emma',
        'Emma claqu\xc3\xa9 la porte au nez!!'],
    [
        'Nicole',
        'Nicole rien du tout \xc3\xa7a doit rester propre.'],
    [
        'Yann-Adam',
        'Yann-Adam le frigo je peux entrer ?'],
    [
        'Louis',
        'Louis pas trop fine, d\xc3\xa9cid\xc3\xa9ment.'],
    [
        'M\xc3\xa9lusine',
        'M\xc3\xa9lusine des Cogs en faillite, au lieu de dormir.'],
    [
        'Kim',
        'Kim \xc3\xa9nerve, \xc3\xa0 ne pas ouvrir.'],
    [
        'Ella',
        'Ella pas envie de descendre ouvrir ?'],
    [
        'Jean',
        "Jean file un pull et j'arrive."],
    [
        'Roger',
        'Roger plus rien dans le frigo, tu peux aller faire les courses?'],
    [
        'John',
        'John D\xc5\x93uf est d\xc3\xa9j\xc3\xa0 pass\xc3\xa9 vendre de la mayonnaise ?'],
    [
        'Alain',
        "Alain d'Issoire! C'est \xc3\xa7a, bon dimanche."],
    [
        'Steve',
        "Steve a, j'y vais aussi."],
    [
        'Elvire',
        'Elvire pas sur ses gonds, ta porte.'],
    [
        'Jean',
        'Jean, bon, je peux entrer finalement ?'],
    [
        'Sarah',
        "Sarah fra\xc3\xaechit derni\xc3\xa8rement, j'ai froid dehors."],
    [
        'A\xc3\xafcha',
        'A\xc3\xafcha fait mal aux mains de frapper \xc3\xa0 ta porte.'],
    [
        'Sarah',
        'Sarah croche toujours au t\xc3\xa9l\xc3\xa9phone, tu ne veux vraiment pas me parler ?'],
    [
        'D\xc3\xa9borah',
        "D\xc3\xa9borah, dis, qu'il y a dans ton jardin, je peux les voir ?"],
    [
        'Eddy',
        'Eddy donc toi l\xc3\xa0-bas, tu vas finir par venir ?'],
    [
        '\xc3\x89lie',
        '\xc3\x89lie quoi? Le journal est d\xc3\xa9j\xc3\xa0 arriv\xc3\xa9?'],
    [
        'Mandy',
        'Mandy donc tu fais quoi l\xc3\xa0?'],
    [
        'Yvon',
        "Yvon pas revenir plus tard si tu n'ouvres pas!"],
    [
        'Isabelle',
        "Isabelle toujours \xc3\xa0 n'importe quelle heure."],
    [
        'Robin',
        "Robin, dis donc, c'est maintenant que tu arrives?"],
    [
        'Oscar',
        "Oscar, il n'est jamais \xc3\xa0 l'heure, je prendrai le train la prochaine fois."],
    [
        'L\xc3\xa9onard',
        "L\xc3\xa9onard j'aime pas, j'aime mieux les langoustines - merci quand m\xc3\xaame pour ton invitation."],
    [
        'G\xc3\xa9rard',
        'G\xc3\xa9rard, mais rarement vu \xc3\xa7a.'],
    [
        'Th\xc3\xa9a',
        "Th\xc3\xa9a l'heure, pour une fois?"],
    [
        'M\xc3\xa9dor',
        'M\xc3\xa9dor, M\xc3\xa9dor, mais comment veux-tu que je dorme si tu ne me laisses pas entrer ?'],
    [
        'Stella',
        "Stella mais c'est plus l\xc3\xa0."],
    [
        'Isidore',
        "Isidore que la nuit, il est parti \xc3\xa0 l'heure qu'il est."],
    [
        '\xc3\x89lodie',
        "\xc3\x89lodie, donc? C'est pas fini?"],
    [
        'Julien',
        'Julien du tout \xc3\xa0 te donner.'],
    [
        'Yvan',
        "Yvan quoi? J'ai besoin de rien."],
    [
        'Eug\xc3\xa8ne',
        'Eug\xc3\xa8ne pas du tout, prend ton temps.'],
    [
        'Sultan',
        'Sultan de travail, je ne peux pas dormir.'],
    [
        'Andr\xc3\xa9',
        'Mais Andr\xc3\xa9 donc.'],
    [
        'Alphonse',
        "Alphonse pas dans l'escalier en venant ouvrir."],
    [
        'Am\xc3\xa9lie',
        'Am\xc3\xa9lie donc ce qui est \xc3\xa9crit au lieu de redemander.'],
    [
        'Ang\xc3\xa8le',
        'Ang\xc3\xa8le pas du tout, il ne fait pas froid.'],
    [
        'Aubin',
        'Aubin dis donc, quand est-ce que tu arrives?'],
    [
        'C\xc3\xa9cile',
        "C\xc3\xa9cile est de bonne humeur qu'il vient ouvrir la porte ?"],
    [
        'Djemila',
        'Djemila cl\xc3\xa9 dans la serrure mais \xc3\xa7a ne marche pas.'],
    [
        '\xc3\x89l\xc3\xa9onore',
        "\xc3\x89l\xc3\xa9onore maintenant mais j'ai pas sa nouvelle adresse."],
    [
        'Huguette',
        "Huguette si quelqu'un d'autre arrive ?"],
    [
        'Isolde',
        'Isolde pas, tout est au prix fort.'],
    [
        'Jenny',
        "Jenny figues ni raisin, l'\xc3\xa9picerie a d\xc3\xa9m\xc3\xa9nag\xc3\xa9."],
    [
        'J\xc3\xa9r\xc3\xa9mie',
        'J\xc3\xa9r\xc3\xa9mie le courrier \xc3\xa0 la poste, maintenant je suis rentr\xc3\xa9.'],
    [
        'Jimmy',
        'Jimmy ton courrier dans la bo\xc3\xaete'],
    [
        'Johnny',
        'Johnny connais rien du tout, viens donc voir \xc3\xa7a.'],
    [
        'Julie',
        'Julie pas tr\xc3\xa8s bien ce qui est \xc3\xa9crit sur la porte.'],
    [
        'Cathy',
        'Cathy donc dit ?'],
    [
        'L\xc3\xa9o',
        'L\xc3\xa9o lit encore \xc3\xa0 cette heure-l\xc3\xa0?'],
    [
        'L\xc3\xa9on',
        "L\xc3\xa9on-dit, \xc3\xa7a ne m'int\xc3\xa9resse pas. Je pr\xc3\xa9f\xc3\xa8re que tu me dises la v\xc3\xa9rit\xc3\xa9."],
    [
        'Ma\xc3\xabl',
        'Ma\xc3\xabl dit toujours la m\xc3\xaame chose!'],
    [
        'Marin',
        'Marin du tout, je veux juste te dire bonjour.'],
    [
        'Quentin',
        'Quentin est l\xc3\xa0, on ouvre.'],
    [
        'Sacha',
        'Sacha pas, demande-lui directement.'],
    [
        'Stella',
        'Stella tu ouvres. R\xc3\xa9ponds!'],
    [
        'Th\xc3\xa9ophile',
        'Th\xc3\xa9ophile encore une fois, tu ne fais que t\xc3\xa9l\xc3\xa9phoner.'],
    [
        'Tudor',
        'Tudor tout le temps quand je passe te voir.'],
    [
        'V\xc3\xa9ra',
        "V\xc3\xa9ra bien qui c'est si tu descends ouvrir."],
    [
        'Xavier',
        'Xavier pas une sonnette la derni\xc3\xa8re fois?'],
    [
        'Yann',
        "Yann a plus, y'en aura la prochaine fois."],
    [
        'Yvon',
        'Yvon bien, merci de prendre des nouvelles!'],
    [
        'Odyss\xc3\xa9e',
        'Odyss\xc3\xa9e quoi toutes ces questions?'],
    [
        'Thor',
        'Thor ait le temps de descendre ouvrir ?'],
    [
        '\xc3\x89dith',
        "\xc3\x89dith a vu l'heure, il est bien temps d'arriver."],
    [
        'Jean-Aymar',
        "Jean-Aymar d'attendre."],
    [
        'Aubin',
        'Aubin dis donc, tu en mets un temps!'],
    [
        'Ahmed',
        "Ahmed d\xc3\xa9pens, j'ai fini par comprendre."],
    [
        'Henri',
        'Henri encore, de ta derni\xc3\xa8re blague.'],
    [
        'Aude',
        'Aude d\xc3\xa9sespoir, \xc3\xb4 rage.'],
    [
        'Ali',
        "Ali qu'a tort, comme d'habitude."],
    [
        'Gilles',
        "Gilles est de sauvetage aujourd'hui."],
    [
        'Hans',
        "Hans qui me concerne, j'aimerais bien que tu ouvres la porte."],
    [
        'Rom\xc3\xa9o',
        "Rom\xc3\xa9o lendemain ce que tu ne peux pas faire aujourd'hui."],
    [
        'Hild\xc3\xa9phonse',
        'Hild\xc3\xa9phonse la porte.'],
    [
        'Helmut',
        'Helmut le pain de la bouche!'],
    [
        'Hercule',
        'Hercule la voiture au fond de la cour.'],
    [
        'Myl\xc3\xa8ne',
        'Myl\xc3\xa8ne, mi-coton.'],
    [
        'C\xc3\xa9lestin',
        "C\xc3\xa9lestin ? Non c'est l'ouest."],
    [
        'Ondine',
        'Ondine o\xc3\xb9 ce soir ?'],
    [
        'Laurent',
        'Laurent-Outang, je cherche le zoo?'],
    [
        'Anne',
        'Anne pas dire.'],
    [
        'Edgar',
        'Edgar pas l\xc3\xa0, tu g\xc3\xaanes.'],
    [
        'Jos\xc3\xa9',
        'Jos\xc3\xa9 pas le dire.'],
    [
        'Samira',
        "Samira pas c'est trop petit."],
    [
        'Humphrey',
        'Humphrey peur celui-l\xc3\xa0!'],
    [
        'Saturnin',
        'Saturnin peu trop vite.'],
    [
        'Juste',
        'Juste pour voir.'],
    [
        'Aziza',
        'Aziza pouvait durer!'],
    [
        'Jonathan',
        'Jonathan que toi.'],
    [
        'Aubin',
        'Aubin, \xc3\xa7a alors! Je ne comptais pas sur toi.'],
    [
        'Yamamoto',
        "Yamamoto qu'a d\xc3\xa9rap\xc3\xa9, je cherche un garage."],
    [
        'Stanislav',
        'Stanislav tous les matins sous sa douche.'],
    [
        'Yvan-D\xc3\xa9d\xc3\xa9',
        "Yvan-D\xc3\xa9d\xc3\xa9, voitures d'occasion."],
    [
        'C\xc3\xa9line',
        'C\xc3\xa9line \xc3\xa9vitable.'],
    [
        'Jean-Phil\xc3\xa9mon',
        'Jean-Phil\xc3\xa9mon blouson et je viens.']]
SharedChatterGreetings = [
    'Salut, %!',
    'Youhouu %,\nravi de te voir.',
    "Je suis content que tu sois l\xc3\xa0 aujourd'hui!",
    'Bien le bonjour, %.']
SharedChatterComments = [
    "C'est un super nom, %.",
    "J'aime bien ton nom.",
    'Fais attention aux' + Cogs + '.On dirait que le tramway arrive!',
    'Je dois jouer \xc3\xa0 un jeu du tramway pour avoir quelques morceaux de tarte!',
    'Quelquefois, je joue aux jeux du tramway juste pour manger de la tarte aux fruits!',
    "Ouf, je viens d'arr\xc3\xaater un groupe de" + Cogs + ". J'ai besoin de repos!",
    'A\xc3\xafe, certains de ces' + Cogs + ' sont costauds!',
    "On dirait que tu t'amuses.",
    'Oh bon sang, quelle bonne journ\xc3\xa9e.',
    "J'aime bien ce que tu portes.",
    'Je crois bien que je vais aller \xc3\xa0 la p\xc3\xaache cet apr\xc3\xa8s-midi.',
    'Amuse-toi bien dans mon quartier.',
    "J'esp\xc3\xa8re que tu profites bien de ton s\xc3\xa9jour \xc3\xa0 Toontown!",
    "J'ai entendu dire qu'il neigeait dans le Glagla.",
    "Est-ce que tu as fait un tour de tramway aujourd'hui?",
    "J'aime bien rencontrer des nouveaux.",
    'A\xc3\xafe, il y a beaucoup de ' + Cogs + ' dans le Glagla.',
    "J'aime bien jouer \xc3\xa0 chat. Et toi ?",
    'Les jeux du tramway sont amusants.',
    "J'aime bien faire rire les gens.",
    "J'adore aider mes contacts.",
    "Hum, serais-tu perdu(e)? N'oublie pas que ta carte est dans ton journal de bord.",
    'Essaie de ne pas te noyer dans la paperasserie des ' + Cogs + '.',
    "J'ai entendu dire que " + Daisy + ' a plant\xc3\xa9 de nouvelles fleurs dans son jardin.',
    'Si tu appuies sur la touche "page pr\xc3\xa9c\xc3\xa9dente", tu peux regarder vers le haut!',
    'Si tu aides \xc3\xa0 reprendre des b\xc3\xa2timents aux Cogs, tu peux gagner une \xc3\xa9toile de bronze!',
    "Si tu appuies sur la touche de tabulation, tu peux voir diff\xc3\xa9rents points de vue de ce qui t'entoure!",
    'Si tu appuies sur la touche Ctrl, tu peux sauter!']
SharedChatterGoodbyes = [
    'Je dois partir maintenant, au revoir!',
    'Je crois que je vais aller faire un jeu du tramway.',
    'Eh bien, au revoir. \xc3\x80 bient\xc3\xb4t, %!',
    "Il vaudrait mieux que je me d\xc3\xa9p\xc3\xaache et que je m'occupe d'arr\xc3\xaater ces " + Cogs + '.',
    "C'est l'heure d'y aller.",
    'D\xc3\xa9sol\xc3\xa9, je dois partir.',
    'Au revoir.',
    '\xc3\x80 plus tard,%!',
    "Je crois que je vais aller m'entra\xc3\xaener \xc3\xa0 lancer des petits g\xc3\xa2teaux.",
    'Je vais me joindre \xc3\xa0 un groupe et arr\xc3\xaater des ' + Cogs + '.',
    "Je suis content(e) de t'avoir vu(e) aujourd'hui, %.",
    "J'ai beaucoup de choses \xc3\xa0 faire. Je ferais mieux de m'y mettre."]
MickeyChatter = ([
                     'Bienvenue \xc3\xa0 Toontown centre.',
                     "Salut, je m'appelle " + Mickey + '. Et toi ?'], [
                     'Dis donc, as-tu vu ' + Donald + '?',
                     'Je vais aller regarder le brouillard se lever sur les quais ' + Donald + '.',
                     'Si tu vois mon copain ' + Goofy + ', dis-lui bonjour de ma part.',
                     "J'ai entendu dire que " + Daisy + ' a plant\xc3\xa9 de nouvelles fleurs dans son jardin.'], [
                     'Je vais au pays musical voir ' + Minnie + '!',
                     'A\xc3\xafe, je suis en retard pour mon rendez-vous avec ' + Minnie + '!',
                     "On dirait que c'est l'heure du d\xc3\xaener pour " + Pluto + '.',
                     'Je crois que je vais aller nager aux quais ' + Donald + '.',
                     "C'est l'heure de faire la sieste. Je vais au Pays des r\xc3\xaaves."])
MinnieChatter = ([
                     'Bienvenue au Pays musical.',
                     "Salut, je m'appelle " + Minnie + '. Et toi ?'], [
                     'Les collines sont anim\xc3\xa9es par les notes de musique!',
                     'Tu as une chouette tenue, %.',
                     'Dis donc, as-tu vu ' + Mickey + '?',
                     'Si tu vois mon ami ' + Goofy + ', dis-lui bonjour de ma part.',
                     'A\xc3\xafe, il y a beaucoup de ' + Cogs + ' pr\xc3\xa8s du Pays des r\xc3\xaaves de ' + Donald + '.',
                     "J'ai entendu dire qu'il y a du brouillard sur les quais " + Donald + '.',
                     "N'oublie pas d'essayer le labyrinthe dans le jardin de " + Daisy + '.',
                     'Je crois bien que je vais aller chercher quelques airs de musique.',
                     'H\xc3\xa9 %, regarde donc par l\xc3\xa0-bas.',
                     "J'aime bien entendre de la musique.",
                     'Je parie que tu ne savais pas que le Pays musical de Minnie est aussi appel\xc3\xa9 le Haut-Bois? Hi hi!',
                     "J'aime bien jouer aux imitations. Et toi ?",
                     "J'aime bien faire rire les gens.",
                     'Oh l\xc3\xa0 l\xc3\xa0, \xc3\xa7a fait mal aux pieds de trotter toute la journ\xc3\xa9e avec des talons!',
                     'Belle chemise, %.',
                     "Est-ce que c'est un bonbon par terre ?"], [
                     'A\xc3\xafe, je suis en retard pour mon rendez-vous avec ' + Mickey + '!',
                     "On dirait que c'est l'heure du d\xc3\xaener pour " + Pluto + '.',
                     "C'est l'heure de faire la sieste. Je vais au Pays des r\xc3\xaaves."])
DaisyChatter = ([
                    'Bienvenue dans mon jardin!',
                    "Bonjour, je m'appelle" + Daisy + ". Comment t'appelles-tu?",
                    'Ravi de faire ta connaissance, %!'], [
                    'Ma fleur qui a gagn\xc3\xa9 le prix est au milieu du labyrinthe.',
                    "J'adore me promener dans le labyrinthe.",
                    "Je n'ai pas vu" + Goofy + ' de la journ\xc3\xa9e.',
                    'Je me demande o\xc3\xb9' + Goofy + ' se trouve.',
                    'As-tu vu' + Donald + '?Il est introuvable.',
                    'Si tu vois mon ami' + Minnie + ', dis-lui "Bonjour" de ma part.',
                    'Meilleurs sont tes outils de jardinage, et plus belles seront tes plantes.',
                    'Il y a beaucoup trop de' + Cogs + ' par ici' + lDonaldsDock + '.',
                    'Tu feras le bonheur de tes plantes si tu les arroses tous les jours.',
                    'Pour faire pousser une p\xc3\xa2querette rose, plante un bonbon jaune et un bonbon rouge ensemble.',
                    "C'est facile de faire pousser une p\xc3\xa2querette jaune, tu n'as qu'\xc3\xa0 planter un bonbon jaune.",
                    "Si tu vois du sable sous une plante, c'est qu'elle a besoin d'eau - faute de quoi elle va se faner!"],
                [
                    'Je vais au Pays musical pour voir %s!' % Minnie,
                    'Je suis en retard pour mon pique-nique avec %s!' % Donald,
                    'Je crois que je vais aller nager \xc3\xa0' + lDonaldsDock + '.',
                    'Oh, je commence \xc3\xa0 avoir sommeil. Je crois que je vais aller au Pays des R\xc3\xaaves'])
GoofyChatter = ([
                    'Bienvenue au jardin de ' + Daisy + '.',
                    "Salut, je m'appelle " + Goofy + '. Et toi ?',
                    'Wof, je suis content de te voir, %!'], [
                    "Bon sang, c'est facile de se perdre dans le labyrinthe!",
                    "N'oublie pas d'essayer le labyrinthe tant que tu es ici.",
                    "Je n'ai pas vu " + Daisy + ' de la journ\xc3\xa9e.',
                    'Je me demande o\xc3\xb9 se trouve ' + Daisy + '.',
                    'Dis donc, as-tu vu ' + Donald + '?',
                    'Si tu vois mon ami ' + Mickey + ', dis-lui bonjour de ma part.',
                    "Oh! J'ai oubli\xc3\xa9 le petit d\xc3\xa9jeuner de " + Mickey + '!',
                    'Wof, il y a beaucoup de ' + Cogs + ' pr\xc3\xa8s des quais ' + Donald + '.',
                    'On dirait que ' + Daisy + ' a plant\xc3\xa9 de nouvelles fleurs dans son jardin.',
                    '\xc3\x80 la succursale du Glagla de ma boutique \xc3\xa0 gags, les lunettes hypnotiques sont en vente pour seulement 1 bonbon!',
                    'La boutique \xc3\xa0 gags de Dingo propose les meilleurs blagues, astuces et chatouilles de tout Toontown!',
                    '\xc3\x80 la boutique \xc3\xa0 gags de Dingo, chaque tarte \xc3\xa0 la cr\xc3\xa8me est garantie faire rire ou tes bonbons te seront rembours\xc3\xa9s!'],
                [
                    'Je vais au Pays musical voir ' + Minnie + '!',
                    'A\xc3\xafe, je suis en retard pour mon rendez-vous avec ' + Donald + '!',
                    'Je crois que je vais aller nager aux quais ' + Donald + '.',
                    "C'est l'heure de faire la sieste. Je vais au Pays des r\xc3\xaaves."])
GoofySpeedwayChatter = ([
                            'Bienvenue au ' + lGoofySpeedway + '.',
                            "Salut, je m'appelle " + Goofy + '. Et toi ?',
                            'Ouah, sympa de te voir %!'], [
                            "Bon sang, j'ai vu une super course tout \xc3\xa0 l'heure.",
                            'Attention aux peaux de banane sur la piste!',
                            'Est-ce que tu as fait des am\xc3\xa9liorations sur ton kart r\xc3\xa9cemment ?',
                            "Nous venons d'acheter de nouvelles jantes dans le magasin de karts.",
                            'Dis-donc, tu as vu ' + Donald + '?',
                            'Si tu vois mon ami ' + Mickey + ', dis-lui bonjour de ma part.',
                            "Oh! J'ai oubli\xc3\xa9 de pr\xc3\xa9parer le petit d\xc3\xa9jeuner de " + Mickey + '!',
                            "Bon sang, c'est vrai qu'il y a un tas de " + Cogs + ' sur les ' + lDonaldsDock + '.',
                            '\xc3\x80 la succursale du Glagla de ma boutique \xc3\xa0 gags, les lunettes hypnotiques sont en vente pour seulement 1 bonbon!',
                            'La boutique \xc3\xa0 gags de Dingo propose les meilleurs blagues, astuces et chatouilles de tout Toontown!',
                            '\xc3\x80 la boutique \xc3\xa0 gags de Dingo, chaque tarte \xc3\xa0 la cr\xc3\xa8me est garantie de te faire rire ou tes bonbons te seront rembours\xc3\xa9s !'],
                        [
                            'Je vais au Pays Musical pour voir %s!' % Mickey,
                            'A\xc3\xafe, je suis en retard pour mon rendez-vous avec %s!' % Donald,
                            'Je crois que je vais aller nager aux ' + lDonaldsDock + '.',
                            "C'est l'heure de faire la sieste. Je vais au Pays des r\xc3\xaaves."])
DonaldChatter = ([
                     'Bienvenue au Pays des r\xc3\xaaves.',
                     "Salut, je m'appelle " + Donald + '. Et toi ?'], [
                     'Cet endroit me donne quelquefois la chair de poule.',
                     "N'oublie pas d'essayer le labyrinthe dans le jardin de" + Daisy + '.',
                     'Oh, bon sang! Quelle bonne journ\xc3\xa9e.',
                     'Dis donc, as-tu vu' + Mickey + '?',
                     'Si tu vois mon copain' + Goofy + ', dis-lui bonjour de ma part.Je crois bien que je vais aller \xc3\xa0 la p\xc3\xaache cet apr\xc3\xa8s-midi.',
                     'A\xc3\xafe, il y a beaucoup de ' + Cogs + ' pr\xc3\xa8s des quais ' + Donald + '.',
                     "H\xc3\xa9 dis donc, tu n'as pas encore fait un tour de bateau avec moi aux quais " + Donald + "?Je n'ai pas vu " + Daisy + ' de la journ\xc3\xa9e.',
                     "J'ai entendu dire que " + Daisy + ' a plant\xc3\xa9 de nouvelles fleurs dans son jardin.Coin coin.'],
                 [
                     'Je vais au Pays musical voir ' + Minnie + '!',
                     'A\xc3\xafe, je suis en retard pour mon rendez-vous avec ' + Daisy + '!',
                     'Je crois que je vais aller nager pr\xc3\xa8s de mes quais.',
                     'Je crois que je vais aller faire un tour de bateau pr\xc3\xa8s de mes quais.'])
for chatter in [
    MickeyChatter,
    DonaldChatter,
    MinnieChatter,
    GoofyChatter]:
    chatter[0].extend(SharedChatterGreetings)
    chatter[1].extend(SharedChatterComments)
    chatter[2].extend(SharedChatterGoodbyes)

FriendsListPanelNewFriend = 'Nouvel(le) ami(e)'
FriendsListPanelSecrets = 'Secrets'
FriendsListPanelOnlineFriends = 'CONTACTS\nEN LIGNE'
FriendsListPanelAllFriends = 'TOUS\nLES CONTACTS'
FriendsListPanelIgnoredFriends = 'TOONS\nIGNOR\xc3\x89S'
FriendsListPanelPets = 'ANIMAUX FAMILIERS\nA PROXIMIT\xc3\x89'
FriendsListPanelPlayers = 'TOUS LES AMIS\nDU JOUEUR'
FriendsListPanelOnlinePlayers = 'AMIS DU JOUEUR\nEN LIGNE'
DownloadForceAcknowledgeMsg = "D\xc3\xa9sol\xc3\xa9, tu ne peux pas avancer parce que le t\xc3\xa9l\xc3\xa9chargement de %(phase)s n'en est qu'\xc3\xa0 %(percent)s% %.\n\nR\xc3\xa9essaie plus tard."
TeaserTop = "D\xc3\xa9sol\xc3\xa9! Tu n'as pas acc\xc3\xa8s \xc3\xa0 ceci pendant l'essai gratuit.\n\nInscris-toi maintenant et profite de ces super fonctionnalit\xc3\xa9s :"
TeaserOtherHoods = 'Visite les 6 quartiers exceptionnels!'
TeaserTypeAName = 'Inscris le nom que tu pr\xc3\xa9f\xc3\xa8res pour ton Toon!'
TeaserSixToons = "Cr\xc3\xa9e jusqu'\xc3\xa0 6 Toons par compte!"
TeaserOtherGags = "Additionne 6 niveaux d'habilet\xc3\xa9\ndans 6 s\xc3\xa9ries de gags diff\xc3\xa9rentes!"
TeaserClothing = 'Ach\xc3\xa8te des v\xc3\xaatements originaux\npour personnaliser ton Toon!'
TeaserFurniture = 'Ach\xc3\xa8te et dispose des meubles dans ta maison!'
TeaserCogHQ = 'Infiltre des zones dangereuses sur\nle territoire des Cogs!'
TeaserSecretChat = '\xc3\x89change des secrets avec tes contacts\npour pouvoir discuter en ligne avec eux!'
TeaserCardsAndPosters = 'Participe aux concours et comp\xc3\xa9titions gagne des troph\xc3\xa9es et \naugmente ta reserve des rigolpoints! \nTon nom appara\xc3\xaetra sur www.toontown.fr'
TeaserHolidays = 'Participe \xc3\xa0 des \xc3\xa9v\xc3\xa9nements sp\xc3\xa9ciaux et\npassionnants et \xc3\xa0 des f\xc3\xaates!'
TeaserQuests = 'Rel\xc3\xa8ve des centaines de d\xc3\xa9fitoons pour sauver Toontown!'
TeaserEmotions = 'Ach\xc3\xa8te des \xc3\xa9motions pour rendre ton\nToon plus expressif!'
TeaserMinigames = 'Joue aux 8 sortes de mini jeux!'
TeaserKarting = "Fais la course contre d'autres Toons dans de super karts!"
TeaserKartingAccessories = ' Personnaliseton kart avec des accessoiressuper cool.'
TeaserGardening = 'Plante des fleurs, des statues et des arbres \xc3\xa0 gags pour embellir\n ta propri\xc3\xa9t\xc3\xa9.'
TeaserRental = 'Loue des articles de f\xc3\xaate amusants pour ta propri\xc3\xa9t\xc3\xa9 !'
TeaserBigger = 'Ach\xc3\xa8te des articles Toon meilleurs et plus gros !'
TeaserTricks = "Entra\xc3\xaene ton Doudou \xc3\xa0 faire des tours pour t'aider dans le combat !"
TeaserSubscribe = "S'inscrire maintenant"
TeaserContinue = "Continuer l'essai"
DownloadWatcherUpdate = 'T\xc3\xa9l\xc3\xa9chargement de: %s'
DownloadWatcherInitializing = 'Initialisation du t\xc3\xa9l\xc3\xa9chargement...'
LauncherPhaseNames = {
    0: 'Initialisation',
    3: 'Faire un Toon',
    3.5: 'Toontoriel',
    4: 'Terrain de jeux',
    5: 'Rues',
    5.5: 'Domaines',
    6: 'Quartiers I',
    7: 'B\xc3\xa2timents' + Cog,
    8: 'Quartiers II',
    9: 'QG Vendibot',
    10: 'QG Caissbot',
    11: Lawbot + ' HQ'}
LauncherProgress = '%(name)s (%(current)s sur %(total)s)'
LauncherStartingMessage = 'Lancement de Toontown en ligne de Disney...'
LauncherDownloadFile = 'T\xc3\xa9l\xc3\xa9chargement des mises \xc3\xa0 jour:' + LauncherProgress + '...'
LauncherDownloadFileBytes = 'T\xc3\xa9l\xc3\xa9chargement des mises \xc3\xa0 jour:' + LauncherProgress + ' : %(bytes)s'
LauncherDownloadFilePercent = 'T\xc3\xa9l\xc3\xa9chargement des mises \xc3\xa0 jour:' + LauncherProgress + ' : %(percent)s% %'
LauncherDecompressingFile = 'D\xc3\xa9compression des mises \xc3\xa0 jour:' + LauncherProgress + '...'
LauncherDecompressingPercent = 'D\xc3\xa9compression des mises \xc3\xa0 jour:' + LauncherProgress + '. : %(percent)s% %'
LauncherExtractingFile = 'Extraction des mises \xc3\xa0 jour:' + LauncherProgress + '...'
LauncherExtractingPercent = 'Extraction des mises \xc3\xa0 jour:' + LauncherProgress + ' : %(percent)s% %'
LauncherPatchingFile = 'Application des mises \xc3\xa0 jour:' + LauncherProgress + '...'
LauncherPatchingPercent = 'Application des mises \xc3\xa0 jour:' + LauncherProgress + ' : %(percent)s% %'
LauncherConnectProxyAttempt = 'En cours de connexion \xc3\xa0 Toontown: %s (proxy : %s) essai : %s'
LauncherConnectAttempt = 'En cours de connexion \xc3\xa0 Toontown: %s essai %s'
LauncherDownloadServerFileList = 'Mise \xc3\xa0 jour de Toontown...'
LauncherCreatingDownloadDb = 'Mise \xc3\xa0 jour de Toontown...'
LauncherDownloadClientFileList = 'Mise \xc3\xa0 jour de Toontown...'
LauncherFinishedDownloadDb = 'Mise \xc3\xa0 jour de Toontown...'
LauncherStartingToontown = 'Lancement de Toontown...'
LauncherStartingGame = 'Lancement de Toontown...'
LauncherRecoverFiles = 'Mise \xc3\xa0 jour de Toontown. R\xc3\xa9cup\xc3\xa9ration des fichiers...'
LauncherCheckUpdates = 'Recherche de mises \xc3\xa0 jour pour ' + LauncherProgress
LauncherVerifyPhase = 'Mise \xc3\xa0 jour de Toontown...'
AvatarChoiceMakeAToon = 'Faire un\nToon'
AvatarChoicePlayThisToon = 'Jouer\navec ce Toon'
AvatarChoiceSubscribersOnly = "S'inscrire\n\n\n\nMaintenant!"
AvatarChoiceDelete = 'Supprimer'
AvatarChoiceDeleteConfirm = 'Cela va supprimer %s pour toujours.'
AvatarChoiceNameRejected = 'Nom\nrefus\xc3\xa9'
AvatarChoiceNameApproved = 'Nom\naccord\xc3\xa9!'
AvatarChoiceNameReview = "En cours\nd'examen"
AvatarChoiceNameYourToon = 'Donne un nom\n\xc3\xa0 ton Toon!'
AvatarChoiceDeletePasswordText = 'Attention! Cela va supprimer %s pour toujours. Pour supprimer ce Toon, entre ton mot de passe.'
AvatarChoiceDeleteConfirmText = 'Attention! Cela va supprimer %(name)s pour toujours. Si tu es certain(e) de vouloir faire cela, entre "%(confirm)s" et clique sur OK.'
AvatarChoiceDeleteConfirmUserTypes = 'supprimer'
AvatarChoiceDeletePasswordTitle = 'Supprimer le Toon ?'
AvatarChoicePassword = 'Mot de passe'
AvatarChoiceDeletePasswordOK = lOK
AvatarChoiceDeletePasswordCancel = lCancel
AvatarChoiceDeleteWrongPassword = 'Ce mot de passe ne semble pas correspondre. Pour supprimer ce Toon, entre ton mot de passe.'
AvatarChoiceDeleteWrongConfirm = 'Tu n\'as pas entr\xc3\xa9 le bon mot. Pour supprimer %(name)s, entre "%(confirm)s" et clique sur OK. N\'entre pas les guillemets. Clique sur Annuler si tu as chang\xc3\xa9 d\'avis.'
AvatarChooserPickAToon = 'Choisis un Toon pour jouer'
AvatarChooserQuit = lQuit
TTAccountCallCustomerService = 'Appelez le Service clients au %s. '
TTAccountCustomerServiceHelp = "\nSi vous avez besoin d'aide, vous pouvez appeler le service clients au %s."
TTAccountIntractibleError = "Une erreur s'est produite."
DateOfBirthEntryMonths = [
    'Jan',
    'F\xc3\xa9v',
    'Mar',
    'Avr',
    'Mai',
    'Juin',
    'Juil',
    'Ao\xc3\xbbt',
    'Sep',
    'Oct',
    'Nov',
    'D\xc3\xa9c']
DateOfBirthEntryDefaultLabel = 'Date de naissance'
AchievePageTitle = 'R\xc3\xa9ussites\n (Bient\xc3\xb4t disponible)'
PhotoPageTitle = 'Photo\n (Bient\xc3\xb4t disponible)'
BuildingPageTitle = 'B\xc3\xa2timents\n (Bient\xc3\xb4t disponible)'
InventoryPageTitle = 'Gags'
InventoryPageDeleteTitle = 'SUPPRIMER LES GAGS'
InventoryPageTrackFull = 'Tu as tous les gags de la s\xc3\xa9rie %s.'
InventoryPagePluralPoints = 'Tu auras un nouveau gag de la s\xc3\xa9rie \n%(trackName)s lorsque tu\nauras %(numPoints)s points de %(trackName)s en plus.'
InventoryPageSinglePoint = 'Tu auras un nouveau gag de la s\xc3\xa9rie \n%(trackName)s lorsque tu\nauras %(numPoints)s points de %(trackName)s en plus.'
InventoryPageNoAccess = "Tu n'as pas encore acc\xc3\xa8s \xc3\xa0 la s\xc3\xa9rie %s."
NPCFriendPageTitle = 'Toons SOS'
NPCFriendPanelRemaining = 'Restant %s'
MapPageTitle = 'Carte'
MapPageBackToPlayground = 'au terrain de jeux'
MapPageBackToCogHQ = 'Retour au QG des Cogs'
MapPageGoHome = '\xc3\xa0 la maison'
MapPageYouAreHere = 'Tu es \xc3\xa0: %s\n%s'
MapPageYouAreAtHome = 'Tu es dans\nta propri\xc3\xa9t\xc3\xa9.'
MapPageYouAreAtSomeonesHome = 'Tu es chez %s.'
MapPageGoTo = 'Aller chez\n%s.'
OptionsPageTitle = 'Options'
OptionsPagePurchase = "S'inscrire!"
OptionsPageLogout = 'Se d\xc3\xa9connecter'
OptionsPageExitToontown = 'Quitter Toontown'
OptionsPageMusicOnLabel = 'Musique activ\xc3\xa9e.'
OptionsPageMusicOffLabel = 'Musique d\xc3\xa9sactiv\xc3\xa9e.'
OptionsPageSFXOnLabel = 'Effets sonores activ\xc3\xa9s.'
OptionsPageSFXOffLabel = 'Effets sonores d\xc3\xa9sactiv\xc3\xa9s.'
OptionsPageFriendsEnabledLabel = 'Demandes de nouveaux contacts accept\xc3\xa9es.'
OptionsPageFriendsDisabledLabel = 'Demandes de nouveaux contacts non accept\xc3\xa9es.'
OptionsPageSpeedChatStyleLabel = 'Couleur du Chat rapide'
OptionsPageDisplayWindowed = 'dans une fen\xc3\xaatre'
OptionsPageSelect = 'Choisir'
OptionsPageToggleOn = 'Activer'
OptionsPageToggleOff = 'D\xc3\xa9sactiver'
OptionsPageChange = 'Modifier'
OptionsPageDisplaySettings = 'Affichage: %(screensize)s, %(api)s'
OptionsPageDisplaySettingsNoApi = 'Affichage: %(screensize)s'
OptionsPageExitConfirm = 'Quitter Toontown ?'
DisplaySettingsTitle = "R\xc3\xa9glages d'affichage"
DisplaySettingsIntro = "Les r\xc3\xa9glages suivants sont utilis\xc3\xa9s pour configurer l'affichage de Toontown sur votre ordinateur. Il n'est sans doute pas indispensable de les modifier sauf si vous avez un probl\xc3\xa8me."
DisplaySettingsIntroSimple = "Vous pouvez accro\xc3\xaetre la r\xc3\xa9solution d'\xc3\xa9cran pour am\xc3\xa9liorer la lisibilit\xc3\xa9 du texte et des graphiques de Toontown, mais en fonction de votre carte graphique, certaines valeurs plus \xc3\xa9lev\xc3\xa9es risquent d'affecter le bon fonctionnement du jeu, voire de l'emp\xc3\xaacher compl\xc3\xa8tement de fonctionner."
DisplaySettingsApi = 'Interface graphique:'
DisplaySettingsResolution = 'R\xc3\xa9solution:'
DisplaySettingsWindowed = 'Dans une fen\xc3\xaatre'
DisplaySettingsFullscreen = 'Plein \xc3\xa9cran'
DisplaySettingsApply = 'Appliquer'
DisplaySettingsCancel = lCancel
DisplaySettingsApplyWarning = "Lorsque vous cliquez sur OK, les r\xc3\xa9glages d'affichage sont modifi\xc3\xa9s. Si la nouvelle configuration ne s'affiche pas correctement sur votre ordinateur, l'affichage revient automatiquement \xc3\xa0 sa configuration d'origine apr\xc3\xa8s %s secondes."
DisplaySettingsAccept = 'Cliquez sur OK pour conserver les nouveaux r\xc3\xa9glages ou sur Annuler pour revenir aux valeurs pr\xc3\xa9c\xc3\xa9dentes. Si vous ne cliquez sur rien, les r\xc3\xa9glages reviennent automatiquement aux valeurs pr\xc3\xa9c\xc3\xa9dentes apr\xc3\xa8s %s secondes.'
DisplaySettingsRevertUser = "Vos pr\xc3\xa9c\xc3\xa9dents r\xc3\xa9glages d'affichage ont \xc3\xa9t\xc3\xa9 restaur\xc3\xa9s."
DisplaySettingsRevertFailed = "Les r\xc3\xa9glages d'affichage s\xc3\xa9lectionn\xc3\xa9s ne peuvent pas fonctionner sur votre ordinateur. Vos pr\xc3\xa9c\xc3\xa9dents r\xc3\xa9glages d'affichage ont \xc3\xa9t\xc3\xa9 restaur\xc3\xa9s."
TrackPageTitle = 'Entra\xc3\xaenement \xc3\xa0 une s\xc3\xa9rie de gags'
TrackPageShortTitle = 'Entra\xc3\xaenement\naux gags'
TrackPageSubtitle = 'Termine des d\xc3\xa9fitoons pour apprendre \xc3\xa0 utiliser de nouveaux gags!'
TrackPageTraining = "Tu t'entra\xc3\xaenes pour utiliser les gags %s. \nLorsque tu auras termin\xc3\xa9 les 16 d\xc3\xa9fis, tu\npourras utiliser les gags %s lors des combats."
TrackPageClear = "Tu ne t'entra\xc3\xaenes pour aucune s\xc3\xa9rie de gags actuellement."
TrackPageFilmTitle = 'Entra\xc3\xaenement\naux gags %s\n.'
TrackPageDone = 'FIN'
QuestPageToonTasks = 'D\xc3\xa9fitoons'
QuestPageChoose = 'Choisis'
QuestPageDestination = '%s\n%s\n%s'
QuestPageNameAndDestination = '%s\n%s\n%s\n%s'
QuestPosterHQOfficer = lHQOfficerM
QuestPosterHQBuildingName = lToonHQ
QuestPosterHQStreetName = 'Une rue'
QuestPosterHQLocationName = 'Un quartier'
QuestPosterTailor = 'Tailleur'
QuestPosterTailorBuildingName = 'Boutique de pr\xc3\xaat-\xc3\xa0-porter'
QuestPosterTailorStreetName = 'Un terrain de jeux'
QuestPosterTailorLocationName = 'Un quartier'
QuestPosterPlayground = 'Sur le terrain de jeux'
QuestPosterAtHome = 'Chez toi'
QuestPosterInHome = 'Dans ta maison'
QuestPosterOnPhone = 'Sur ton t\xc3\xa9l\xc3\xa9phone'
QuestPosterEstate = 'Dans ta propri\xc3\xa9t\xc3\xa9'
QuestPosterAnywhere = "N'importe o\xc3\xb9"
QuestPosterAuxTo = '\xc3\xa0:'
QuestPosterAuxFrom = 'depuis:'
QuestPosterAuxFor = 'pour:'
QuestPosterAuxOr = 'ou:'
QuestPosterAuxReturnTo = 'Retourner \xc3\xa0:'
QuestPosterLocationIn = ' \xc3\xa0'
QuestPosterLocationOn = ' \xc3\xa0'
QuestPosterFun = "Juste pour s'amuser!"
QuestPosterFishing = 'ALLER P\xc3\x8aCHER'
QuestPosterComplete = 'TERMIN\xc3\x89'
ShardPageTitle = 'Districts'
ShardPageHelpIntro = 'Chaque district est une copie du monde de Toontown.'
ShardPageHelpWhere = ' Tu es actuellement dans le district de "%s".'
ShardPageHelpWelcomeValley = ' Tu es actuellement dans le district de la "Vall\xc3\xa9e de la Bienvenue", dans "%s".'
ShardPageHelpMove = ' Pour aller dans un nouveau district, clique sur son nom.'
ShardPagePopulationTotal = 'Population totale de Toontown:\n%d'
ShardPageScrollTitle = 'Nom Population'
ShardPageLow = 'Calme'
ShardPageMed = 'Id\xc3\xa9al'
ShardPageHigh = 'Complet'
ShardPageChoiceReject = "D\xc3\xa9sol\xc3\xa9, ce district est complet. Merci d'en essayer un autre."
SuitPageTitle = 'Galerie des Cogs'
SuitPageMystery = '???'
SuitPageQuota = '%s sur %s'
SuitPageCogRadar = '%s pr\xc3\xa9sents'
SuitPageBuildingRadarS = 'B\xc3\xa2timent %s'
SuitPageBuildingRadarP = 'B\xc3\xa2timents %s'
DisguisePageTitle = 'D\xc3\xa9guisement de\n' + Cog
DisguisePageMeritBar = 'Avancement au m\xc3\xa9rite'
DisguisePageMeritAlert = 'Pr\xc3\xaat pour la\npromotion!'
DisguisePageCogLevel = 'Niveau %s'
DisguisePageMeritFull = 'Plein'
DisguisePageMeritBar = 'Avancement au m\xc3\xa9rite'
DisguisePageCogPartRatio = '%d/%d'
FishPageTitle = 'P\xc3\xaache'
FishPageTitleTank = 'Seau de p\xc3\xaache'
FishPageTitleCollection = 'Album de p\xc3\xaache'
FishPageTitleTrophy = 'Troph\xc3\xa9es de p\xc3\xaache'
FishPageWeightStr = 'Poids:'
FishPageWeightLargeS = '%dkg'
FishPageWeightLargeP = '%dkg'
FishPageWeightSmallS = ' %dg'
FishPageWeightSmallP = ' %dg'
FishPageWeightConversion = 16
FishPageValueS = 'Valeur: %d bonbon'
FishPageValueP = 'Valeur: %d bonbons'
FishPageTotalValue = ''
FishPageCollectedTotal = 'Esp\xc3\xa8ces de poissons p\xc3\xaach\xc3\xa9es: %d sur %d'
FishPageRodInfo = 'Canne %s \n%d - %d livres'
FishPageTankTab = 'Seau'
FishPageCollectionTab = 'Album'
FishPageTrophyTab = 'Troph\xc3\xa9es'
FishPickerTotalValue = 'Seau: %s / %s\nValeur: %d bonbons'
UnknownFish = '???'
FishingRod = 'Canne %s'
FishingRodNameDict = {
    0: 'Brindille',
    1: 'Bambou',
    2: 'Bois dur',
    3: 'Acier',
    4: 'Or'}
FishTrophyNameDict = {
    0: 'Guppy',
    1: 'Vairon',
    2: 'Poisson',
    3: 'Poisson volant',
    4: 'Requin',
    5: 'Espadons',
    6: '\xc3\x89paulard'}
GardenPageTitle = 'Gardening'
GardenPageTitleBasket = 'Panier de fleurs'
GardenPageTitleCollection = 'Album de fleurs'
GardenPageTitleTrophy = 'Troph\xc3\xa9es de jardinage'
GardenPageTitleSpecials = 'Offres sp\xc3\xa9ciales jardinage'
GardenPageBasketTab = 'Panier'
GardenPageCollectionTab = 'Album'
GardenPageTrophyTab = 'Troph\xc3\xa9es'
GardenPageSpecialsTab = 'Offres sp\xc3\xa9ciales'
GardenPageCollectedTotal = 'Vari\xc3\xa9t\xc3\xa9s de fleurs rassembl\xc3\xa9es: %d sur %d'
GardenPageValueS = 'Valeur: %d bonbon'
GardenPageValueP = 'Valeur: %d bonbons'
FlowerPickerTotalValue = 'Panier: %s / %s\nValeur: %d bonbons'
GardenPageShovelInfo = '%s Pelle: %d / %d\n'
GardenPageWateringCanInfo = '%s Arrosoir: %d / %d'
KartPageTitle = 'Karts'
KartPageTitleCustomize = 'Customiser mon kart'
KartPageTitleRecords = 'Meilleurs records personnels'
KartPageTitleTrophy = 'Troph\xc3\xa9es de course'
KartPageCustomizeTab = 'Customiser'
KartPageRecordsTab = 'Records'
KartPageTrophyTab = 'Troph\xc3\xa9e'
KartPageTrophyDetail = 'Troph\xc3\xa9e %s : %s'
KartPageTickets = 'Tickets:'
KartPageConfirmDelete = "Supprimer l'accessoire ?"
KartShtikerDelete = 'Supprimer'
KartShtikerSelect = 'Choisir une cat\xc3\xa9gorie'
KartShtikerNoAccessories = 'Aucun accessoire achet\xc3\xa9'
KartShtikerBodyColors = 'Couleurs du kart'
KartShtikerAccColors = 'Couleurs des accessoires'
KartShtikerEngineBlocks = 'Accessoires du capot'
KartShtikerSpoilers = 'Accessoires du coffre'
KartShtikerFrontWheelWells = 'Accessoires des roues avant'
KartShtikerBackWheelWells = 'Accessoires des roues arri\xc3\xa8re'
KartShtikerRims = 'Accessoires des jantes'
KartShtikerDecals = 'Accessoires d\xc3\xa9calcomanie'
KartShtikerBodyColor = 'Couleur du kart'
KartShtikerAccColor = "Couleur de l'accessoire"
KartShtikerEngineBlock = 'Capot'
KartShtikerSpoiler = 'Coffre'
KartShtikerFrontWheelWell = 'Roue avant'
KartShtikerBackWheelWell = 'Roue arri\xc3\xa8re'
KartShtikerRim = 'Jante'
KartShtikerDecal = 'D\xc3\xa9calcomanie'
KartShtikerDefault = '%s par d\xc3\xa9faut'
KartShtikerNo = 'Aucun accessoire de %s'
QuestChoiceGuiCancel = lCancel
TrackChoiceGuiChoose = 'Choisir'
TrackChoiceGuiCancel = lCancel
TrackChoiceGuiHEAL = "Toonique te permet de soigner les autres Toons lors d'une bataille."
TrackChoiceGuiTRAP = 'Les pi\xc3\xa8ges sont des gags puissants qui doivent \xc3\xaatre utilis\xc3\xa9s avec les leurres.'
TrackChoiceGuiLURE = 'Utilise les leurres pour assommer les Cogs ou les attirer dans des pi\xc3\xa8ges.'
TrackChoiceGuiSOUND = 'Les gags de tapage affectent tous les Cogs mais ne sont pas tr\xc3\xa8s puissants.'
TrackChoiceGuiDROP = 'Les gags de chute font beaucoup de d\xc3\xa9g\xc3\xa2ts mais ne sont pas tr\xc3\xa8s pr\xc3\xa9cis.'
EmotePageTitle = 'Expressions / \xc3\x89motions'
EmotePageDance = 'Tu as construit la s\xc3\xa9quence de danse suivante:'
EmoteJump = 'Saut'
EmoteDance = 'Danse'
EmoteHappy = 'Content(e)'
EmoteSad = 'Triste'
EmoteAnnoyed = 'Agacement'
EmoteSleep = 'Sommeil'
SuitBaseNameWithLevel = '%(name)s\n%(dept)s\nNiveau %(level)s'
HealthForceAcknowledgeMessage = 'Tu ne peux pas quitter le terrain de jeux tant que ton rigolm\xc3\xa8tre ne sourit pas!'
InventoryTotalGags = 'Total des gags\n%d / %d'
InventoryDelete = 'SUPPRIMER'
InventoryDone = 'TERMIN\xc3\x89'
InventoryDeleteHelp = 'Clique sur un gag pour le SUPPRIMER.'
InventorySkillCredit = "Cr\xc3\xa9dit d'habilet\xc3\xa9: %s"
InventorySkillCreditNone = "Cr\xc3\xa9dit d'habilet\xc3\xa9: Aucun"
InventoryDetailAmount = '%(numItems)s / %(maxItems)s'
InventoryDetailData = 'Pr\xc3\xa9cision : %(accuracy)s\n%(damageString)s: %(damage)d\n%(singleOrGroup)s'
InventoryTrackExp = '%(curExp)s / %(nextExp)s'
InventoryUberTrackExp = '%(nextExp)s \xc3\xa0 terminer !'
InventoryGuestExp = "Nombre maxi d'invit\xc3\xa9s"
GuestLostExp = "Plus que le nombre maxi d'invit\xc3\xa9s"
InventoryAffectsOneCog = 'Affecte : Un' + Cog
InventoryAffectsOneToon = 'Affecte : Un Toon'
InventoryAffectsAllToons = 'Affecte : tous les Toons'
InventoryAffectsAllCogs = 'Affecte : tous les' + Cogs
InventoryHealString = 'Toonique'
InventoryDamageString = 'Dommages'
InventoryBattleMenu = 'MENU DU COMBAT'
InventoryRun = 'COURIR'
InventorySOS = 'SOS'
InventoryPass = 'PASSER'
InventoryClickToAttack = 'Clique sur\nun gag pour\nattaquer.'
InventoryDamageBonus = '(+%d)'
NPCForceAcknowledgeMessage = 'Tu dois faire un tour de tramway avant de partir.\n\n\n\n\n\n\nTu trouveras le tramway pr\xc3\xa8s de la boutique \xc3\xa0 gags de Dingo.'
NPCForceAcknowledgeMessage2 = 'Bien, tu as termin\xc3\xa9 ta recherche dans le tramway!\nVa voir le quartier g\xc3\xa9n\xc3\xa9ral des Toons pour recevoir ta r\xc3\xa9compense.\n\n\n\n\n\n\n\nLe quartier g\xc3\xa9n\xc3\xa9ral des Toons est situ\xc3\xa9 pr\xc3\xa8s du centre du terrain de jeux.'
NPCForceAcknowledgeMessage3 = "N'oublie pas de faire un tour de tramway.\n\n\n\n\n\nTu trouveras le tramway pr\xc3\xa8s de la boutique \xc3\xa0 gags de Dingo."
NPCForceAcknowledgeMessage4 = 'Bravo! Tu as termin\xc3\xa9 ton premier d\xc3\xa9fitoon!\n\n\n\n\n\n\nVa voir le quartier g\xc3\xa9n\xc3\xa9ral des Toons pour recevoir ta r\xc3\xa9compense.'
NPCForceAcknowledgeMessage5 = "N'oublie pas ton d\xc3\xa9fitoon!\n\n\n\n\n\n\n\n\n\n\nTu peux trouver des Cogs a vaincre de l'autre c\xc3\xb4t\xc3\xa9 de tunnels comme celui-ci."
NPCForceAcknowledgeMessage6 = 'F\xc3\xa9licitations pour avoir vaincu ces Cogs!\n\n\n\n\n\n\n\n\n\nReviens au quartier g\xc3\xa9n\xc3\xa9ral des Toons aussi vite que possible.'
NPCForceAcknowledgeMessage7 = "N'oublie pas de te faire un(e) ami(e)!\n\n\n\n\n\n\n\nClique sur un autre joueur et utilise le bouton Nouvel(le) ami(e)."
NPCForceAcknowledgeMessage8 = "Super! Tu t'es fait un(e) nouvel(le) ami(e)!\n\n\n\n\n\n\n\n\nTu dois retourner au quartier g\xc3\xa9n\xc3\xa9ral des Toons maintenant."
NPCForceAcknowledgeMessage9 = 'Tu as bien utilis\xc3\xa9 le t\xc3\xa9l\xc3\xa9phone!\n\n\n\n\n\n\n\n\nRetourne au quartier g\xc3\xa9n\xc3\xa9ral des Toons pour demander ta r\xc3\xa9compense.'
ToonSleepString = '. . . ZZZ . . .'
MovieTutorialReward1 = 'Tu as re\xc3\xa7u 1 point de lancer! Quand tu en auras 10, tu pourras recevoir un nouveau gag!'
MovieTutorialReward2 = "Tu as re\xc3\xa7u 1 point d'\xc3\xa9claboussure! Quand tu en auras 10, tu pourras avoir un nouveau gag!"
MovieTutorialReward3 = 'Bon travail! Tu as termin\xc3\xa9 ton premier d\xc3\xa9fitoon!'
MovieTutorialReward4 = 'Va chercher ta r\xc3\xa9compense au quartier g\xc3\xa9n\xc3\xa9ral des Toons!'
MovieTutorialReward5 = 'Amuse-toi!'
Battle_Input_Timeout = 50.0
BattleGlobalTracks = [
    'toonique',
    'pi\xc3\xa8ge',
    'leurre',
    'tapage',
    'lancer',
    '\xc3\xa9claboussure',
    'chute']
BattleGlobalNPCTracks = [
    'rechargement',
    'Toons marquent',
    'Cogs ratent']
BattleGlobalAvPropStrings = (('Plume', 'M\xc3\xa9gaphone', 'Tube de rouge \xc3\xa0 l\xc3\xa8vres', 'Canne en bambou',
                              'Poussi\xc3\xa8re de f\xc3\xa9e', 'Balles de jonglage', 'Plongeon'), (
                             'Peau de banane', 'R\xc3\xa2teau', 'Billes', 'Sable mouvant', 'Trappe', 'TNT',
                             'Chemin de fer'), ('Billet de 1 euro', 'Petit aimant', 'Billet de 5 euros', 'Gros aimant',
                                                'Billet de 10 euros', 'Lunettes hypnotiques', 'Pr\xc3\xa9sentation'), (
                             'Sonnette de v\xc3\xa9lo', 'Sifflet', 'Clairon', 'Klaxon',
                             "Trompe d'\xc3\xa9l\xc3\xa9phant", 'Corne de brume',
                             'Chanteuse d\xe2\x80\x99op\xc3\xa9ra'), (
                             'Petit g\xc3\xa2teau', 'Tranche de tarte aux fruits',
                             'Tranche de tarte \xc3\xa0 la cr\xc3\xa8me', 'Tarte aux fruits enti\xc3\xa8re',
                             'Tarte \xc3\xa0 la cr\xc3\xa8me enti\xc3\xa8re', "G\xc3\xa2teau d'anniversaire",
                             'G\xc3\xa2teau de mariage'), (
                             'Fleur \xc3\xa0 \xc3\xa9clabousser', "Verre d'eau", 'Pistolet \xc3\xa0 eau',
                             "Bouteille d'eau gazeuse", "Lance d'incendie", "Nuage d'orage", 'Geyser'), (
                             'Pot de fleurs', 'Sac de sable', 'Enclume', 'Gros poids', 'Coffre-fort',
                             'Piano \xc3\xa0 queue', 'Toontanic'))
BattleGlobalAvPropStringsSingular = (('une plume', 'un m\xc3\xa9gaphone', 'un tube de rouge \xc3\xa0 l\xc3\xa8vres',
                                      'une canne en bambou', 'de la poussi\xc3\xa8re de f\xc3\xa9e',
                                      'un jeu de balles de jonglage', 'un Plongeon'), (
                                     'une peau de banane', 'un r\xc3\xa2teau', 'un jeu de billes',
                                     'un peu de sable mouvant', 'une trappe', 'du TNT', 'un Chemin de fer'), (
                                     'un billet de 1 euro', 'un petit aimant', 'un billet de 5 euros', 'un gros aimant',
                                     'un billet de 10 euros', 'une paire de lunettes hypnotiques',
                                     'une Pr\xc3\xa9sentation'), (
                                     'une sonnette de v\xc3\xa9lo', 'un sifflet', 'un clairon', 'un klaxon',
                                     "une trompe d'\xc3\xa9l\xc3\xa9phant", 'une corne de brume',
                                     'une Chanteuse d\xe2\x80\x99op\xc3\xa9ra'), (
                                     'un petit g\xc3\xa2teau', 'une tranche de tarte aux fruits',
                                     'une tranche de tarte \xc3\xa0 la cr\xc3\xa8me',
                                     'une tarte aux fruits enti\xc3\xa8re',
                                     'une tarte \xc3\xa0 la cr\xc3\xa8me enti\xc3\xa8re',
                                     "un g\xc3\xa2teau d'anniversaire", 'un G\xc3\xa2teau de mariage'), (
                                     'une fleur \xc3\xa0 \xc3\xa9clabousser', "un verre d'eau",
                                     'un pistolet \xc3\xa0 eau', "une bouteille d'eau gazeuse", "une lance d'incendie",
                                     "un nuage d'orage", 'un Geyser'), (
                                     'un pot de fleurs', 'un sac de sable', 'une enclume', 'un gros poids',
                                     'un coffre-fort', 'un piano \xc3\xa0 queue', 'le Toontanic'))
BattleGlobalAvPropStringsPlural = (('Plumes', 'M\xc3\xa9gaphones', 'Tubes de rouge \xc3\xa0 l\xc3\xa8vres',
                                    'Cannes en bambou', 'Poussi\xc3\xa8res de f\xc3\xa9e', 'jeux de balles de jonglage',
                                    'Plongeons'), (
                                   'Peaux de bananes', 'R\xc3\xa2teaux', 'jeux de billes', 'morceaux de sable mouvant',
                                   'Trappes', 'b\xc3\xa2tons de TNT', 'Chemins de fer'), (
                                   'Billets de 1 euro', 'Petits aimants', 'Billets de 5 euros', 'Gros aimants',
                                   'Billets de 10 euros', 'Paires de lunettes hypnotiques', 'Pr\xc3\xa9sentations'), (
                                   'Sonnettes de v\xc3\xa9lo', 'Sifflets', 'Clairons', 'Klaxons',
                                   "Trompes d'\xc3\xa9l\xc3\xa9phants", 'Cornes de brume',
                                   'Chanteuses d\xe2\x80\x99op\xc3\xa9ra'), (
                                   'Petits g\xc3\xa2teaux', 'Tranches de tarte aux fruits',
                                   'Tranches de tarte \xc3\xa0 la cr\xc3\xa8me', 'Tartes aux fruits enti\xc3\xa8res',
                                   'Tartes \xc3\xa0 la cr\xc3\xa8me enti\xc3\xa8res', "G\xc3\xa2teaux d'anniversaire",
                                   'G\xc3\xa2teaux de mariage'), (
                                   'Fleurs \xc3\xa0 \xc3\xa9clabousser', "Verres d'eau", 'Pistolets \xc3\xa0 eau',
                                   "Bouteilles d'eau gazeuse", "Lances d'incendie", "Nuages d'orage", 'Geysers'), (
                                   'Pots de fleurs', 'Sacs de sable', 'Enclumes', 'Gros poids', 'Coffres-forts',
                                   'Pianos \xc3\xa0 queue', 'Paquebots'))
BattleGlobalAvTrackAccStrings = ('Moyenne', 'Parfaite', 'Faible', 'Forte', 'Moyenne', 'Forte', 'Faible')
BattleGlobalLureAccLow = 'Faible'
BattleGlobalLureAccMedium = 'Moyen'
AttackMissed = 'RAT\xc3\x89'
NPCCallButtonLabel = 'APPEL'
LoaderLabel = 'Chargement...'
HeadingToHood = 'En route %(to)s %(hood)s...'
HeadingToYourEstate = 'En direction de ta propri\xc3\xa9t\xc3\xa9...'
HeadingToEstate = 'En direction de la propri\xc3\xa9t\xc3\xa9 de %s...'
HeadingToFriend = "En direction de la propri\xc3\xa9t\xc3\xa9 de l'ami(e) de %s..."
HeadingToPlayground = 'En direction du terrain de jeux...'
HeadingToStreet = 'En route %(to)s %(street)s...'
TownBattleRun = 'Revenir en courant au terrain de jeux?'
TownBattleChooseAvatarToonTitle = 'QUEL TOON ?'
TownBattleChooseAvatarCogTitle = 'QUEL ' + string.upper(Cog) + '?'
TownBattleChooseAvatarBack = 'RETOUR'
TownBattleSOSNoFriends = "Pas d'contacts \xc3\xa0 appeler!"
TownBattleSOSWhichFriend = 'Appeler quel(le) ami(e)?'
TownBattleSOSNPCFriends = 'Toons sauv\xc3\xa9s'
TownBattleSOSBack = 'RETOUR'
TownBattleToonSOS = 'SOS'
TownBattleUndecided = '?'
TownBattleHealthText = '%(hitPoints)s/%(maxHit)s'
TownBattleWaitTitle = 'En attente des\nautres joueurs...'
TownSoloBattleWaitTitle = 'Patiente...'
TownBattleWaitBack = 'RETOUR'
TownBattleSOSPetSearchTitle = 'Recherche du Doudou\n%s...'
TownBattleSOSPetInfoTitle = '%s est %s'
TownBattleSOSPetInfoOK = lOK
TrolleyHFAMessage = 'Tu ne peux pas monter dans le tramway avant que ton rigolm\xc3\xa8tre ne sourie.'
TrolleyTFAMessage = 'Tu ne peux pas monter dans le tramway avant que ' + Mickey + ' ne te le dise.'
TrolleyHopOff = lQuit
FishingExit = 'Sortie'
FishingCast = 'Lancer'
FishingAutoReel = 'Moulinet automatique'
FishingItemFound = 'Tu as attrap\xc3\xa9 :'
FishingCrankTooSlow = 'Trop\nlent'
FishingCrankTooFast = 'Trop\nrapide'
FishingFailure = "Tu n'as rien attrap\xc3\xa9!"
FishingFailureTooSoon = "Ne commence pas \xc3\xa0 faire remonter ta ligne avant de voir une touche. Attends que ton flotteur se mette \xc3\xa0 s'enfoncer et \xc3\xa0 remonter rapidement!"
FishingFailureTooLate = 'Remonte bien ta ligne avant que le poisson ne se d\xc3\xa9croche!'
FishingFailureAutoReel = "Le moulinet automatique n'a pas fonctionn\xc3\xa9 cette fois-ci. Tourne la manivelle \xc3\xa0 la main, juste \xc3\xa0 la bonne vitesse, pour avoir les meilleurs chances d'attraper quelque chose!"
FishingFailureTooSlow = "Tu as tourn\xc3\xa9 la manivelle trop lentement. Certains poissons sont plus rapides que d'autres. Essaie de conserver la ligne de vitesse au centre!"
FishingFailureTooFast = "Tu as tourn\xc3\xa9 la manivelle trop rapidement. Certains poissons sont plus lents que d'autres. Essaie de conserver la ligne de vitesse au centre!"
FishingOverTankLimit = "Ton seau de p\xc3\xaache est plein. Va vendre tes poissons au vendeur de l'animalerie et reviens."
FishingBroke = "Tu n'as plus de bonbons pour app\xc3\xa2ter! Va faire un tour de tramway ou vends des poissons aux vendeurs de l'animalerie pour avoir d'autres bonbons."
FishingHowToFirstTime = 'Clique sur le bouton de lancer et d\xc3\xa9place le curseur vers le bas. Plus tu glisses vers le bas, plus ton lancer sera fort. Ajuste ton angle pour atteindre les poissons.\n\n Essaie maintenant!'
FishingHowToFailed = 'Clique sur le bouton de lancer et d\xc3\xa9place le curseur vers le bas. Plus tu glisses vers le bas, plus ton lancer sera fort. Ajuste ton angle pour atteindre les poissons.\n\n Essaie encore maintenant!'
FishingBootItem = 'Une vieille chaussure'
FishingJellybeanItem = '%s bonbons'
FishingNewEntry = 'Nouvelle esp\xc3\xa8ce!'
FishingNewRecord = 'Nouveau record!'
FishPokerCashIn = 'Encaisser\n%s\n%s'
FishPokerLock = 'Bloquer'
FishPokerUnlock = 'D\xc3\xa9bloquer'
FishPoker5OfKind = '5 identiques'
FishPoker4OfKind = 'Carr\xc3\xa9'
FishPokerFullHouse = 'Plein'
FishPoker3OfKind = 'Brelan'
FishPoker2Pair = '2 paires'
FishPokerPair = 'Paire'
TutorialGreeting1 = 'Salut,%s!'
TutorialGreeting2 = 'Salut,%s!\nViens par ici!'
TutorialGreeting3 = 'Salut,%s!\nViens par ici!\nUtilise les fl\xc3\xa8ches!'
TutorialMickeyWelcome = 'Bienvenue \xc3\xa0 Toontown!'
TutorialFlippyIntro = 'Je te pr\xc3\xa9sente mon ami ' + Flippy + '...'
TutorialFlippyHi = 'Salut,%s!'
TutorialQT1 = 'Tu peux parler en utilisant ceci.'
TutorialQT2 = 'Tu peux parler en utilisant ceci.\nClique dessus, puis choisis "Salut".'
TutorialChat1 = "Tu peux parler en utilisant l'un de ces boutons."
TutorialChat2 = 'Le bouton bleu te permet de chatter avec le clavier.'
TutorialChat3 = 'Fais attention! La plupart des autres joueurs ne comprendront pas ce que tu dis lorsque tu utilises le clavier.'
TutorialChat4 = 'Le bouton vert ouvre le %s.'
TutorialChat5 = 'Tout le monde peut te comprendre si tu utilises le %s.'
TutorialChat6 = 'Essaie de dire "salut".'
TutorialBodyClick1 = 'Tr\xc3\xa8s bien!'
TutorialBodyClick2 = "Ravi de t'avoir rencontr\xc3\xa9! Tu veux que nous soyons contacts?"
TutorialBodyClick3 = 'Pour devenir ami(e) avec ' + Flippy + ', clique sur lui...'
TutorialHandleBodyClickSuccess = 'Bon travail!'
TutorialHandleBodyClickFail = "Ce n'est pas \xc3\xa7a. Essaie de cliquer juste sur " + Flippy + '...'
TutorialFriendsButton = 'Maintenant, clique sur le bouton "contacts" sous l\'image de ' + Flippy + " dans l'angle droit."
TutorialHandleFriendsButton = 'Ensuite, clique sur le bouton "oui".'
TutorialOK = lOK
TutorialYes = lYes
TutorialNo = lNo
TutorialFriendsPrompt = 'Veux-tu devenir ami(e) avec ' + Flippy + '?'
TutorialFriendsPanelMickeyChat = Flippy + ' veut bien \xc3\xaatre ton ami. Clique sur "OK" pour terminer.'
TutorialFriendsPanelYes = Flippy + ' a dit oui!'
TutorialFriendsPanelNo = "\xc3\x87a n'est pas tr\xc3\xa8s gentil!"
TutorialFriendsPanelCongrats = "Bravo! Tu t'es fait ton premier ami."
TutorialFlippyChat1 = 'Reviens me voir quand tu seras pr\xc3\xaat pour ton premier d\xc3\xa9fitoon!'
TutorialFlippyChat2 = 'Je serai \xc3\xa0 la Mairie de Toontown!'
TutorialAllFriendsButton = 'Tu peux voir tous tes contacts en cliquant sur le bouton "contacts". Essaye donc...'
TutorialEmptyFriendsList = "Pour l'instant, ta liste est vide parce que " + Flippy + " n'est pas v\xc3\xa9ritablement un joueur."
TutorialCloseFriendsList = 'Clique sur le bouton " Fermer "\npour faire dispara\xc3\xaetre la liste.'
TutorialShtickerButton = "Le bouton dans l'angle inf\xc3\xa9rieur droit ouvre ton journal de bord. Essaye-le..."
TutorialBook1 = 'Le journal contient de nombreuses informations utiles comme cette carte de Toontown.'
TutorialBook2 = 'Tu peux aussi y voir les progr\xc3\xa8s de tes d\xc3\xa9fitoons.'
TutorialBook3 = 'Lorsque tu as fini, clique de nouveau sur le bouton repr\xc3\xa9sentant un livre pour le fermer.'
TutorialLaffMeter1 = 'Tu as aussi besoin de \xc3\xa7a...'
TutorialLaffMeter2 = "Tu as aussi besoin de \xc3\xa7a...\nC'est ton rigolm\xc3\xa8tre."
TutorialLaffMeter3 = 'Lorsque les ' + Cogs + " t'attaquent, il baisse."
TutorialLaffMeter4 = 'Lorsque tu es sur les terrains de jeux comme celui-ci, il remonte.'
TutorialLaffMeter5 = "Lorsque tu finis des d\xc3\xa9fitoons, tu re\xc3\xa7ois des r\xc3\xa9compenses, comme l'augmentation de ta rigo-limite."
TutorialLaffMeter6 = 'Fais attention! Si les ' + Cogs + ' te battent, tu perds tous tes gags.'
TutorialLaffMeter7 = 'Pour avoir plus de gags, joue aux jeux du tramway.'
TutorialTrolley1 = "Suis-moi jusqu'au tramway!"
TutorialTrolley2 = 'Monte \xc3\xa0 bord!'
TutorialBye1 = 'Joue \xc3\xa0 des jeux!'
TutorialBye2 = 'Joue \xc3\xa0 des jeux!\nAch\xc3\xa8te des gags!'
TutorialBye3 = 'Va voir ' + Flippy + ' quand tu auras fini!'
TutorialForceAcknowledgeMessage = 'Tu vas dans le mauvais sens! Va trouver ' + Mickey + '!'
PetTutorialTitle1 = 'Le panneau des Doudous'
PetTutorialTitle2 = 'Chat rapide des Doudous'
PetTutorialTitle3 = 'Catalogue des Doudous'
PetTutorialNext = 'Page suivante'
PetTutorialPrev = 'Page pr\xc3\xa9c\xc3\xa9dente'
PetTutorialDone = 'Termin\xc3\xa9'
PetTutorialPage1 = 'Clique sur un Doudou pour afficher le panneau des Doudous. L\xc3\xa0 tu pourras nourrir, cajoler et appeler le Doudou.'
PetTutorialPage2 = "Utilise la nouvelle zone 'Animaux familiers' dans le menu de Chat rapide pour que le Doudou fasse un tour. S'il le fait, r\xc3\xa9compense-le et il s'am\xc3\xa9liorera!"
PetTutorialPage3 = 'Ach\xc3\xa8te de nouveaux tours pour les Doudous dans le catalogue de Clarabelle. De meilleures tours donnent de meilleures tooniques!'


def getPetGuiAlign():
    TextNode = TextNode
    import pandac.PandaModules
    return TextNode.ACenter


GardenTutorialTitle1 = 'Jardinage'
GardenTutorialTitle2 = 'Fleurs'
GardenTutorialTitle3 = 'Arbres'
GardenTutorialTitle4 = 'Comment faire'
GardenTutorialTitle5 = 'Statues'
GardenTutorialNext = 'Page suivante'
GardenTutorialPrev = 'Page pr\xc3\xa9c\xc3\xa9dente'
GardenTutorialDone = 'Termin\xc3\xa9'
GardenTutorialPage1 = 'Embellis ta propri\xc3\xa9t\xc3\xa9 avec un jardin! Tu peux y planter des fleurs, y faire pousser des arbres, y r\xc3\xa9colter des gags super puissants et le d\xc3\xa9corer avec des statues!'
GardenTutorialPage2 = "Les fleurs sont d\xc3\xa9licates et demandent des recettes tr\xc3\xa8s particuli\xc3\xa8res \xc3\xa0 base de bonbons. Une fois qu'elles ont pouss\xc3\xa9, tu peux les mettre dans une brouette pour aller les vendre et faire gonfler ton rigolm\xc3\xa8tre."
GardenTutorialPage3 = "Utilise un gag que tu as dans ton inventaire pour planter un arbre. Apr\xc3\xa8s quelques jours, ce gag sera encore plus puissant! N'oublie pas d'en prendre soin, ou tu perdras l'augmentation de puissance."
GardenTutorialPage4 = "Marche jusqu'\xc3\xa0 ces endroits pour planter, arroser, b\xc3\xaacher ou faire la cueillette dans ton jardin."
GardenTutorialPage5 = 'Les statues sont vendues dans le Catalogue vachement branch\xc3\xa9 de Clarabelle. Am\xc3\xa9liore ton habilet\xc3\xa9 pour avoir acc\xc3\xa8s aux statues les plus extravagantes!'
PlaygroundDeathAckMessage = 'Les ' + Cogs + " ont pris tous tes gags!\n\nTu es triste. Tu ne peux pas quitter le terrain de jeux avant d'avoir retrouv\xc3\xa9 la joie de vivre."
ForcedLeaveFactoryAckMsg = "Le contrema\xc3\xaetre de l'usine a \xc3\xa9t\xc3\xa9 vaincu avant que tu ne le trouves. Tu n'as pas r\xc3\xa9cup\xc3\xa9r\xc3\xa9 de pi\xc3\xa8ces de Cogs."
ForcedLeaveMintAckMsg = "Le Superviseur de cet \xc3\xa9tage de la Fabrique \xc3\xa0 Sous a \xc3\xa9t\xc3\xa9 vaincu avant que tu ne puisses l'atteindre. Tu n'as pas r\xc3\xa9cup\xc3\xa9r\xc3\xa9 de euros Cog."
HeadingToFactoryTitle = 'En route %s...'
ForemanConfrontedMsg = "%s est en train de combattre le contrema\xc3\xaetre de l'usine!"
MintBossConfrontedMsg = '%s est en train de combattre le Superviseur!'
StageBossConfrontedMsg = '%s se bat contre le juriste!'
stageToonEnterElevator = "%s \nest maintenant dans l'ascenseur"
ForcedLeaveStageAckMsg = "Le juriste a \xc3\xa9t\xc3\xa9 vaincu avant que tu ne le trouves. Tu n'as pas r\xc3\xa9cup\xc3\xa9r\xc3\xa9 de convocations du jury."
MinigameWaitingForOtherPlayers = "En attente d'autres joueurs..."
MinigamePleaseWait = 'Patiente un peu...'
DefaultMinigameTitle = 'Nom du mini jeu'
DefaultMinigameInstructions = 'Instructions du mini jeu'
HeadingToMinigameTitle = 'En route vers: %s...'
MinigamePowerMeterLabel = 'T\xc3\xa9moin de puissance'
MinigamePowerMeterTooSlow = 'Trop\nlent'
MinigamePowerMeterTooFast = 'Trop\nrapide'
MinigameTemplateTitle = 'Mod\xc3\xa8le de mini jeu'
MinigameTemplateInstructions = "C'est un mod\xc3\xa8le de mini jeu. Utilise-le pour cr\xc3\xa9er des mini jeux."
CannonGameTitle = 'Jeu du canon'
CannonGameInstructions = "Envoie ton Toon dans le ch\xc3\xa2teau d'eau aussi vite que tu peux. Utilise les fl\xc3\xa8ches du clavier ou la souris pour diriger le canon. Sois rapide et gagne une belle r\xc3\xa9compense pour tout le monde!"
CannonGameReward = 'R\xc3\x89COMPENSE'
TugOfWarGameTitle = 'Tir \xc3\xa0 la corde'
TugOfWarInstructions = "Appuie alternativement sur les fl\xc3\xa8ches gauche et droite \xc3\xa0 la vitesse qu'il faut pour aligner la barre verte avec la ligne rouge. N'appuie pas trop rapidement ou trop lentement, tu pourrais finir dans l'eau!"
TugOfWarGameGo = 'PARTEZ!'
TugOfWarGameReady = 'Pr\xc3\xaat...'
TugOfWarGameEnd = 'Bien jou\xc3\xa9!'
TugOfWarGameTie = '\xc3\x89galit\xc3\xa9!'
TugOfWarPowerMeter = 'T\xc3\xa9moin de puissance'
PatternGameTitle = 'Imite ' + Minnie
PatternGameInstructions = Minnie + ' va te montrer une suite de pas de danse. ' + 'Essaie de reproduire la danse de ' + Minnie + ' comme tu la vois en utilisant les fl\xc3\xa8ches!'
PatternGameWatch = 'Regarde ces pas de danse...'
PatternGameGo = 'PARTEZ!'
PatternGameRight = 'Bien, %s!'
PatternGameWrong = 'A\xc3\xafe!'
PatternGamePerfect = "C'\xc3\xa9tait parfait, %s!"
PatternGameBye = "Merci d'avoir jou\xc3\xa9!"
PatternGameWaitingOtherPlayers = "En attente d'autres joueurs..."
PatternGamePleaseWait = 'Patiente un peu...'
PatternGameFaster = 'Tu as \xc3\xa9t\xc3\xa9\nplus rapide!'
PatternGameFastest = 'Tu as \xc3\xa9t\xc3\xa9\nle(la) plus rapide!'
PatternGameYouCanDoIt = 'Allez!\nTu peux y arriver!'
PatternGameOtherFaster = '\na \xc3\xa9t\xc3\xa9 plus rapide!'
PatternGameOtherFastest = '\na \xc3\xa9t\xc3\xa9 le(la) plus rapide!'
PatternGameGreatJob = 'Bon travail!'
PatternGameRound = 'Partie %s!'
PatternGameImprov = 'Bien jou\xc3\xa9 ! Maintenant monte !'
WaitingForJoin = 90
RaceGameTitle = "Jeu de l'oie"
RaceGameInstructions = "Clique sur un nombre. Choisis bien! Tu n'avances que si personne d'autre n'a choisi le m\xc3\xaame nombre."
RaceGameWaitingChoices = 'Attente du choix des autres joueurs...'
RaceGameCardText = '%(name)s tire: %(reward)s'
RaceGameCardTextBeans = '%(name)s re\xc3\xa7oit: %(reward)s'
RaceGameCardTextHi1 = '%(name)s est un Toon fabuleux!'
RaceGameForwardOneSpace = " avance d'une case"
RaceGameForwardTwoSpaces = ' avance de 2 cases'
RaceGameForwardThreeSpaces = ' avance de 3 cases'
RaceGameBackOneSpace = " recule d'une case"
RaceGameBackTwoSpaces = ' recule de 2 cases'
RaceGameBackThreeSpaces = ' recule de 3 cases'
RaceGameOthersForwardThree = ' tous les autres avancent\nde 3 cases'
RaceGameOthersBackThree = 'tous les autres reculent\nde 3 cases'
RaceGameInstantWinner = 'Gagnant!'
RaceGameJellybeans2 = '2 bonbons'
RaceGameJellybeans4 = '4 bonbons'
RaceGameJellybeans10 = '10 bonbons!'
RingGameTitle = 'Jeu des anneaux'
RingGameInstructionsSinglePlayer = "Essaie de nager en passant dans autant d'anneaux %s que tu pourras. Utilise les fl\xc3\xa8ches pour nager."
RingGameInstructionsMultiPlayer = 'Essaie de nager en passant dans les anneaux %s. Les autres joueurs essaieront de passer les anneaux des autres couleurs. Utilise les fl\xc3\xa8ches pour nager.'
RingGameMissed = 'RAT\xc3\x89'
RingGameGroupPerfect = 'GROUPE\nPARFAIT!!'
RingGamePerfect = 'PARFAIT!'
RingGameGroupBonus = 'BONUS DE GROUPE'
ColorRed = 'rouges'
ColorGreen = 'verts'
ColorOrange = 'orange'
ColorPurple = 'violets'
ColorWhite = 'blancs'
ColorBlack = 'noirs'
ColorYellow = 'jaunes'
DivingGameTitle = 'Chasse aux tr\xc3\xa9sors aquatique'
DivingInstructionsSinglePlayer = 'Les tr\xc3\xa9sors apparaissent au fond du lac. Utilise les fl\xc3\xa8ches du clavier pour nager. \xc3\x89vite les poissons et rapporte les tr\xc3\xa9sors dans le bateau.'
DivingInstructionsMultiPlayer = 'Les tr\xc3\xa9sors apparaissent au fond du lac. Utilise les fl\xc3\xa8ches de ton clavier pour nager. Travailler ensemble pour rapporter les tr\xc3\xa9sors dans le bateau.'
DivingGameTreasuresRetrieved = 'Recherch\xc3\xa9 Tr\xc3\xa9sors'
TargetGameTitle = 'Jeu du parapluie'
TargetGameInstructionsSinglePlayer = 'Atterris sur les cibles pour marquer des points'
TargetGameInstructionsMultiPlayer = 'Atterris sur les cibles pour marquer des points'
TargetGameBoard = 'Manche %s - Garder le meilleur score'
TargetGameCountdown = 'Lancement forc\xc3\xa9 dans %s secondes'
TargetGameCountHelp = 'Touche di\xc3\xa8se et fl\xc3\xa8ches droite et gauche pour allumer, stop pour lancer'
TargetGameFlyHelp = 'Appuyer pour ouvrir le parapluie'
TargetGameFallHelp = 'Utilise les fl\xc3\xa8ches du clavier pour atterrir sur les cibles'
TargetGameBounceHelp = "En rebondissant, tu peux t'\xc3\xa9carter de la cible"
TagGameTitle = 'Jeu du chat'
TagGameInstructions = 'R\xc3\xa9cup\xc3\xa8re les tr\xc3\xa9sors. Tu ne peux pas r\xc3\xa9cup\xc3\xa9rer les tr\xc3\xa9sors quand tu es chat!'
TagGameYouAreIt = 'Tu es chat!'
TagGameSomeoneElseIsIt = '%s est chat!'
MazeGameTitle = 'Jeu du labyrinthe'
MazeGameInstructions = 'R\xc3\xa9cup\xc3\xa8re les tr\xc3\xa9sors. Essaie de les avoir tous, mais fais attention aux ' + Cogs + '!'
CatchGameTitle = 'Jeu du verger'
CatchGameInstructions = 'Attrape des %(fruit)s, autant que tu peux. Attention aux ' + Cogs + ', et essaie de ne pas attraper des %(badThing)s!'
CatchGamePerfect = 'PARFAIT!'
CatchGameApples = 'pommes'
CatchGameOranges = 'oranges'
CatchGamePears = 'poires'
CatchGameCoconuts = 'noix de coco'
CatchGameWatermelons = 'past\xc3\xa8ques'
CatchGamePineapples = 'ananas'
CatchGameAnvils = 'enclumes'
PieTossGameTitle = 'Jeu du lancer de tartes'
PieTossGameInstructions = 'Envoie des tartes dans les cibles.'
MinigameRulesPanelPlay = 'JOUER'
GagShopName = 'La boutique \xc3\xa0 gags de Dingo'
GagShopPlayAgain = 'REJOUER\n'
GagShopBackToPlayground = 'RETOUR AU\nTERRAIN DE JEUX'
GagShopYouHave = 'Tu as %s \xc3\xa0 d\xc3\xa9penser'
GagShopYouHaveOne = 'Tu as 1 bonbon \xc3\xa0 d\xc3\xa9penser'
GagShopTooManyProps = "D\xc3\xa9sol\xc3\xa9, tu as trop d'accessoires"
GagShopDoneShopping = 'ACHATS\n TERMIN\xc3\x89S'
GagShopTooManyOfThatGag = 'D\xc3\xa9sol\xc3\xa9, tu as d\xc3\xa9j\xc3\xa0 assez de %s'
GagShopInsufficientSkill = "Tu n'es pas encore assez habile pour cela"
GagShopYouPurchased = 'Tu as achet\xc3\xa9 %s'
GagShopOutOfJellybeans = "D\xc3\xa9sol\xc3\xa9, tu n'as plus de bonbons!"
GagShopWaitingOtherPlayers = 'En attente des autres joueurs...'
GagShopPlayerDisconnected = '%s est d\xc3\xa9connect\xc3\xa9(e)'
GagShopPlayerExited = '%s est parti(e)'
GagShopPlayerPlayAgain = 'Jouer encore'
GagShopPlayerBuying = 'Achat en cours'
GenderShopQuestionMickey = 'Pour faire un gar\xc3\xa7on Toon, clique ici!'
GenderShopQuestionMinnie = 'Pour faire une fille Toon, clique ici!'
GenderShopFollow = 'Suis-moi!'
GenderShopSeeYou = '\xc3\x80 plus tard!'
GenderShopBoyButtonText = 'Gar\xc3\xa7on'
GenderShopGirlButtonText = 'Fille'
BodyShopHead = 'T\xc3\xaate'
BodyShopBody = 'Corps'
BodyShopLegs = 'Jambes'
ColorShopHead = 'T\xc3\xaate'
ColorShopBody = 'Corps'
ColorShopLegs = 'Jambes'
ColorShopToon = 'Toon'
ColorShopParts = 'Parties'
ColorShopAll = 'Tout'
ClothesShopShorts = 'Short'
ClothesShopShirt = 'Chemise'
ClothesShopBottoms = 'Bas'
MakeAToonDone = 'Fini'
MakeAToonCancel = lCancel
MakeAToonNext = lNext
MakeAToonLast = 'Retour'
CreateYourToon = 'Clique sur les fl\xc3\xa8ches pour cr\xc3\xa9er ton Toon.'
CreateYourToonTitle = 'Cr\xc3\xa9e ton Toon'
CreateYourToonHead = 'Clique sur les fl\xc3\xa8ches "t\xc3\xaate" pour choisir diff\xc3\xa9rents animaux.'
MakeAToonClickForNextScreen = "Clique sur la fl\xc3\xa8che ci-dessous pour aller \xc3\xa0 l'\xc3\xa9cran suivant."
PickClothes = 'Clique sur les fl\xc3\xa8ches pour choisir des v\xc3\xaatements!'
PickClothesTitle = 'Choisis tes v\xc3\xaatements'
PaintYourToon = 'Clique sur les fl\xc3\xa8ches pour peindre ton Toon!'
PaintYourToonTitle = 'Peins ton Toon'
MakeAToonYouCanGoBack = 'Tu peux aussi retourner en arri\xc3\xa8re pour changer ton corps!'
MakeAFunnyName = 'Choisis un nom amusant pour ton Toon!'
MustHaveAFirstOrLast1 = 'Ton Toon devrait avoir un pr\xc3\xa9nom ou un nom de famille, tu ne penses pas?'
MustHaveAFirstOrLast2 = 'Tu ne veux pas que ton Toon ait de pr\xc3\xa9nom ou de nom de famille ?'
ApprovalForName1 = "C'est \xc3\xa7a, ton Toon m\xc3\xa9rite un super nom!"
ApprovalForName2 = 'Les noms Toon sont les meilleurs noms!'
MakeAToonLastStep = "Derni\xc3\xa8re \xc3\xa9tape avant d'aller \xc3\xa0 Toontown!"
PickANameYouLike = 'Choisis un nom que tu aimes!'
NameToonTitle = 'Donne un nom \xc3\xa0 ton Toon'
TitleCheckBox = 'Titre'
FirstCheckBox = 'Pr\xc3\xa9nom'
LastCheckBox = 'Nom'
RandomButton = 'Al\xc3\xa9atoire'
NameShopSubmitButton = 'Envoyer'
TypeANameButton = 'Entre un nom'
TypeAName = "Tu n'aimes pas ces noms?\nClique ici -->"
PickAName = 'Essaie le jeu Choisis-un-nom!\nClique ici -->'
PickANameButton = 'Choisis un nom'
RejectNameText = "Ce nom n'est pas autoris\xc3\xa9. Essaie encore."
WaitingForNameSubmission = 'Envoi de ton nom...'
PetNameMaster = 'PetNameMaster_french.txt'
PetshopUnknownName = 'Nom:???'
PetshopDescGender = 'Sexe:\t%s'
PetshopDescCost = 'Co\xc3\xbbte:\t%s bonbons'
PetshopDescTrait = 'Caract\xc3\xa8re:\t%s'
PetshopDescStandard = 'Standard'
PetshopCancel = lCancel
PetshopSell = 'Vendre tes poissons'
PetshopAdoptAPet = 'Adopter un Doudou'
PetshopReturnPet = 'Rapporter ton Doudou'
PetshopAdoptConfirm = 'Adopter %s pour %d bonbons?'
PetshopGoBack = 'Retourner'
PetshopAdopt = 'Adopter'
PetshopReturnConfirm = 'Rapporter %s?'
PetshopReturn = 'Rapporter'
PetshopChooserTitle = 'LES DOUDOUS DU JOUR'
PetshopGoHomeText = 'Est-ce que tu veux aller dans ta propri\xc3\xa9t\xc3\xa9 pour jouer avec ton nouveau Doudou?'
NameShopNameMaster = 'NameMaster_french.txt'
NameShopPay = 'Inscris-toi!'
NameShopPlay = 'Essai gratuit'
NameShopOnlyPaid = "Seuls les utilisateurs payants\npeuvent donner un nom \xc3\xa0 leurs Toons.\nJusqu'\xc3\xa0 ce que tu t'inscrives,\nton nom sera\n"
NameShopContinueSubmission = "Continuer l'envoi"
NameShopChooseAnother = 'Choisir un autre nom'
NameShopToonCouncil = 'Le Conseil de Toontown\nva examiner ton\nnom.  ' + "L'examen peut\nprendre quelques jours.\nPendant que tu attends,\nton nom sera\n "
PleaseTypeName = 'Entre ton nom:'
AllNewNames = 'Tous les noms\ndoivent \xc3\xaatre approuv\xc3\xa9s\npar le Conseil de Toontown.'
NameShopNameRejected = 'Le nom que tu as\nenvoy\xc3\xa9 a \xc3\xa9t\xc3\xa9 refus\xc3\xa9.'
NameShopNameAccepted = 'F\xc3\xa9licitations!\nLe nom que tu as\nenvoy\xc3\xa9 a\n\xc3\xa9t\xc3\xa9 accept\xc3\xa9!'
NoPunctuation = 'Tu ne peux pas utiliser de signes de ponctuation dans ton nom!'
PeriodOnlyAfterLetter = 'Tu peux utiliser un point dans ton nom, mais seulement apr\xc3\xa8s une lettre.'
ApostropheOnlyAfterLetter = 'Tu peux utiliser une apostrophe dans ton nom, mais seulement apr\xc3\xa8s une lettre.'
NoNumbersInTheMiddle = "Les caract\xc3\xa8res num\xc3\xa9riques ne peuvent pas appara\xc3\xaetre au milieu d'un mot."
ThreeWordsOrLess = 'Ton nom doit comporter trois mots maximum.'
CopyrightedNames = (
'Mickey', 'Mickey Mouse', 'Mickey Mouse', 'Minnie', 'Minnie Mouse', 'Minnie Mouse', 'Donald', 'Donald Duck',
'Donald Duck', 'Pluto', 'Dingo')
NumToColor = [
    'Blanc',
    'P\xc3\xaache',
    'Rouge vif',
    'Rouge',
    'Bordeaux',
    'Terre de Sienne',
    'Brun',
    'Brun clair',
    'Corail',
    'Orange',
    'Jaune',
    'Cr\xc3\xa8me',
    'Jaune-vert',
    'Citron vert',
    'Vert marin',
    'Vert',
    'Bleu clair',
    'Turquoise',
    'Bleu',
    'Pervenche',
    'Bleu roi',
    'Bleu ardoise',
    'Violet',
    'Lavande',
    'Rose']
AnimalToSpecies = {
    'dog': 'Chien',
    'cat': 'Chat',
    'mouse': 'Souris',
    'horse': 'Cheval',
    'rabbit': 'Lapin',
    'duck': 'Canard',
    'monkey': 'Singe',
    'bear': 'Ours',
    'pig': 'cochon'}
NameTooLong = 'Ce nom est trop long. Essaie encore.'
ToonAlreadyExists = "Tu as d\xc3\xa9j\xc3\xa0 un Toon qui s'appelle %s!"
NameAlreadyInUse = 'Ce nom est d\xc3\xa9j\xc3\xa0 utilis\xc3\xa9!'
EmptyNameError = "Tu dois indiquer un nom d'abord."
NameError = 'D\xc3\xa9sol\xc3\xa9. Ce nom ne pourra pas convenir.'
NCTooShort = 'Ce nom est trop court.'
NCNoDigits = 'Ton nom ne peut pas contenir de chiffres.'
NCNeedLetters = 'Chaque mot de ton nom doit contenir des lettres.'
NCNeedVowels = 'Chaque mot de ton nom doit contenir des voyelles.'
NCAllCaps = 'Ton nom ne peut pas \xc3\xaatre enti\xc3\xa8rement en majuscules.'
NCMixedCase = 'Ton nom a trop de majuscules.'
NCBadCharacter = 'Ton nom ne peut pas contenir le caract\xc3\xa8re "%s"'
NCGeneric = 'D\xc3\xa9sol\xc3\xa9, ce nom ne pourra pas convenir.'
NCTooManyWords = 'Ton nom ne peut pas comporter plus de quatre mots.'
NCDashUsage = 'Les tirets ne peuvent \xc3\xaatre utilis\xc3\xa9s que pour relier deux mots ensemble.(comme dans "Bou-Bou").'
NCCommaEdge = 'Ton nom ne peut pas commencer ou se terminer par une virgule.'
NCCommaAfterWord = 'Tu ne peux pas commencer un mot par une virgule.'
NCCommaUsage = 'Ce nom n\'utilise pas les virgules correctement. Les virgules doiventassembler deux mots, comme dans le nom "Dr Couac, m\xc3\xa9decin".Les virgules doivent aussi \xc3\xaatre suivies d\'un espace.'
NCPeriodUsage = 'Ce nom n\'utilise pas les points correctement. Les points sontseulement autoris\xc3\xa9s dans des mots tels que "M.","doct.","prof.", etc.'
NCApostrophes = "Ton nom a trop d'apostrophes."
RemoveTrophy = lToonHQ + ' : Les ' + Cogs + ' ont repris un des b\xc3\xa2timents que tu avais sauv\xc3\xa9s!'
STOREOWNER_TOOKTOOLONG = 'Tu as besoin de plus de temps pour r\xc3\xa9fl\xc3\xa9chir ?'
STOREOWNER_GOODBYE = '\xc3\x80 plus tard!'
STOREOWNER_NEEDJELLYBEANS = 'Tu dois faire un tour de tramway pour avoir des bonbons.'
STOREOWNER_GREETING = 'Choisis ce que tu veux acheter.'
STOREOWNER_BROWSING = "Tu peux regarder, mais tu auras besoin d'un ticket d'habillement pour acheter."
STOREOWNER_NOCLOTHINGTICKET = "Tu as besoin d'un ticket d'habillement pour acheter des v\xc3\xaatements."
STOREOWNER_NOFISH = "Reviens ici pour vendre des poissons \xc3\xa0 l'animalerie en \xc3\xa9change de bonbons."
STOREOWNER_THANKSFISH = "Merci! L'animalerie va les adorer. Au revoir!"
STOREOWNER_THANKSFISH_PETSHOP = 'Ce sont de beaux sp\xc3\xa9cimens! Merci.'
STOREOWNER_PETRETURNED = "Ne t'inquiete pas. Nous trouverons une bonne maison pour ton Doudou."
STOREOWNER_PETADOPTED = 'F\xc3\xa9licitations pour ton nouveau Doudou! Tu peux jouer avec lui dans ta propri\xc3\xa9t\xc3\xa9.'
STOREOWNER_PETCANCELED = "N'oublie pas: si tu vois un Doudou qui te pla\xc3\xaet, adopte-le avant que quelqu'un d'autre ne le fasse!"
STOREOWNER_NOROOM = "Hmm...tu devrais faire de la place dans ton placard avant d'acheter de nouveaux v\xc3\xaatements.\n"
STOREOWNER_CONFIRM_LOSS = 'Ton placard est plein. Tu vas perdre les v\xc3\xaatements que tu portais.'
STOREOWNER_OK = lOK
STOREOWNER_CANCEL = lCancel
STOREOWNER_TROPHY = 'Oh l\xc3\xa0 l\xc3\xa0! Tu as trouv\xc3\xa9 %s sur %s poissons. \xc3\x87a m\xc3\xa9rite un troph\xc3\xa9e et une rigol-augmentation!'
SuitInvasionBegin1 = lToonHQ + ': Une invasion de Cogs a commenc\xc3\xa9!!!'
SuitInvasionBegin2 = lToonHQ + ': Les %s ont pris Toontown!!!'
SuitInvasionEnd1 = lToonHQ + ": L'invasion des %s est termin\xc3\xa9e!!!"
SuitInvasionEnd2 = lToonHQ + ': Les Toons nous ont sauv\xc3\xa9s une fois de plus!!!'
SuitInvasionUpdate1 = lToonHQ + ": L'invasion de Cogs en est \xc3\xa0 %s Cogs!!!"
SuitInvasionUpdate2 = lToonHQ + ': Nous devons battre ces %s!!!'
SuitInvasionBulletin1 = lToonHQ + ': Il y a une invasion de Cogs en cours!!!'
SuitInvasionBulletin2 = lToonHQ + ': Les %s ont pris Toontown!!!'
LeaderboardTitle = 'Arm\xc3\xa9e de Toons'
QuestScriptTutorialMickey_1 = 'Toontown compte un nouveau citoyen! Est-ce que tu as des gags en plus?'
QuestScriptTutorialMickey_2 = 'Bien s\xc3\xbbr, %s!'
QuestScriptTutorialMickey_3 = 'Tom Tuteur va te parler des Cogs.\x7Je dois y aller!'
QuestScriptTutorialMickey_4 = 'Viens ici! Utilise les fl\xc3\xa8ches pour te d\xc3\xa9placer.'
QuestScriptTutorialMinnie_1 = 'Toontown compte une nouvelle citoyenne! Est-ce que tu as des gags en plus?'
QuestScriptTutorialMinnie_2 = 'Bien s\xc3\xbbr, %s!'
QuestScriptTutorialMinnie_3 = 'Tom Tuteur va te parler des Cogs.\x7Je dois y aller!'
QuestScript101_1 = 'Ce sont les COGS. Ce sont des robots qui essaient de prendre Toontown.'
QuestScript101_2 = 'Il y a diff\xc3\xa9rentes sortes de COGS et...'
QuestScript101_3 = '...ils transforment de bons b\xc3\xa2timents Toon...'
QuestScript101_4 = '...en affreuses b\xc3\xa2tisses Cog!'
QuestScript101_5 = 'Mais les COGS ne comprennent pas les blagues!'
QuestScript101_6 = 'Un bon gag les arr\xc3\xaate.'
QuestScript101_7 = 'Il y a des quantit\xc3\xa9s de gags; prends ceux-l\xc3\xa0 pour commencer.'
QuestScript101_8 = "Oh! Tu as aussi besoin d'un rigolm\xc3\xa8tre!"
QuestScript101_9 = 'Si ton rigolm\xc3\xa8tre descend trop bas, tu seras triste!'
QuestScript101_10 = 'Un Toon heureux est un Toon en bonne sant\xc3\xa9!'
QuestScript101_11 = 'OH NON! Il y a un COG devant ma boutique!'
QuestScript101_12 = "AIDE-MOI, S'IL TE PLA\xc3\x8eT! Va vaincre ce COG!"
QuestScript101_13 = 'Voil\xc3\xa0 ton premier d\xc3\xa9fitoon!'
QuestScript101_14 = 'D\xc3\xa9p\xc3\xaache-toi! Va battre ce Laquaistic!'
QuestScript110_1 = 'Bon travail pour avoir vaincu ce Laquaistic. Je vais te donner un journal de bord...'
QuestScript110_2 = 'Ce journal est plein de choses int\xc3\xa9ressantes.'
QuestScript110_3 = 'Ouvre-le, et je vais te montrer.'
QuestScript110_4 = 'La carte montre o\xc3\xb9 tu as \xc3\xa9t\xc3\xa9.'
QuestScript110_5 = 'Tourne la page pour voir tes gags...'
QuestScript110_6 = "Oh oh! Tu n'as pas de gags! Je vais te donner un d\xc3\xa9fi."
QuestScript110_7 = 'Tourne la page pour voir tes d\xc3\xa9fis.'
QuestScript110_8 = 'Fais un tour de tramway, et gagne des bonbons pour acheter des gags!'
QuestScript110_9 = "Pour aller jusqu'au tramway, sors par la porte qui est derri\xc3\xa8re moi et va jusqu'au terrain de jeux."
QuestScript110_10 = 'Maintenant, ferme le livre et trouve le tramway!'
QuestScript110_11 = 'Retourne au QG des Toons quand tu as fini. Au revoir!'
QuestScriptTutorialBlocker_1 = 'Bien le bonjour!'
QuestScriptTutorialBlocker_2 = 'Bonjour ?'
QuestScriptTutorialBlocker_3 = 'Oh! Tu ne sais pas utiliser le Chat rapide!'
QuestScriptTutorialBlocker_4 = 'Clique sur le bouton pour dire quelque chose.'
QuestScriptTutorialBlocker_5 = 'Tr\xc3\xa8s bien!\x7L\xc3\xa0 o\xc3\xb9 tu vas, il y a plein de Toons \xc3\xa0 qui parler.'
QuestScriptTutorialBlocker_6 = "Si tu veux chatter avec tes contacts \xc3\xa0 l'aide du clavier, tu peux utiliser un autre bouton."
QuestScriptTutorialBlocker_7 = '\xc3\x87a s\'appelle le bouton "Chat". Tu dois \xc3\xaatre officiellement citoyen de Toontown pour l\'utiliser.'
QuestScriptTutorialBlocker_8 = 'Bonne chance! \xc3\x80 plus tard!'
QuestScriptGagShop_1 = 'Bienvenue \xc3\xa0 la Boutique \xc3\xa0 gags!'
QuestScriptGagShop_1a = "C'est l\xc3\xa0 que viennent les Toons pour acheter des gags qu'ils utiliseront contre les Cogs."
QuestScriptGagShop_3 = "Pour acheter des gags, clique sur les boutons de gag. Essaie d'en avoir maintenant!"
QuestScriptGagShop_4 = 'Super! Tu peux utiliser ces gags lors des combats contre les Cogs.'
QuestScriptGagShop_5 = "Voila un aper\xc3\xa7u des gags avanc\xc3\xa9s de lancer et d'\xc3\xa9claboussure..."
QuestScriptGagShop_6 = "Quand tu as fini d'acheter des gags, clique sur ce bouton pour retourner au terrain de jeu."
QuestScriptGagShop_7 = 'Normalement, tu peux utiliser ce bouton pour jouer \xc3\xa0 un autre jeu du tramway...'
QuestScriptGagShop_8 = "...mais tu n'as pas le temps de faire un autre jeu maintenant. On t'attend au quartier g\xc3\xa9n\xc3\xa9ral des Toons!"
QuestScript120_1 = "Bien, tu as trouv\xc3\xa9 le tramway!\x7Au fait, as-tu rencontr\xc3\xa9 Bob le Banquier ?\x7Il aime bien les sucreries.\x7Pourquoi n'irais-tu pas te pr\xc3\xa9senter en lui emportant ce sucre d'orge comme cadeau?"
QuestScript120_2 = 'Bob le Banquier est dans la banque de Toontown.'
QuestScript121_1 = "Miam, merci pour ce sucre d'orge.\x7Dis donc, si tu peux m'aider, je te donnerai une r\xc3\xa9compense.\x7Ces Cogs ont vol\xc3\xa9 les cl\xc3\xa9s de mon coffre. Va battre des Cogs pour trouver une cl\xc3\xa9 vol\xc3\xa9e.\x7Quand tu auras trouv\xc3\xa9 une cl\xc3\xa9, ram\xc3\xa8ne-la moi."
QuestScript130_1 = "Bien, tu as trouv\xc3\xa9 le tramway!\x7Pendant qu'on y est, j'ai re\xc3\xa7u un paquet pour le Professeur Pete aujourd'hui.\x7\xc3\x87a doit \xc3\xaatre la nouvelle craie qu'il a command\xc3\xa9e.\x7Peux-tu lui apporter s'il te pla\xc3\xaet ?\x7Il est dans l'\xc3\xa9cole."
QuestScript131_1 = "Oh, merci pour la craie.\x7Quoi?!?\x7Ces Cogs ont vol\xc3\xa9 mon tableau. Va vaincre des Cogs pour retrouver le tableau qu'ils m'ont vol\xc3\xa9.\x7Quand tu l'auras trouv\xc3\xa9, ram\xc3\xa8ne-le moi."
QuestScript140_1 = "Bien, tu as trouv\xc3\xa9 le tramway!\x7Pendant qu'on y est, j'ai un ami, Larry le Libraire, qui est un rat de biblioth\xc3\xa8que.\x7J'ai pris ce livre pour lui la derni\xc3\xa8re fois que j'ai \xc3\xa9t\xc3\xa9 aux quais Donald.\x7Pourrais-tu lui apporter ? Il est \xc3\xa0 la biblioth\xc3\xa8que, d'habitude."
QuestScript141_1 = "Oh, oui, ce livre compl\xc3\xa8te presque ma collection.\x7Voyons \xc3\xa7a...\x7Ah, oh...\x7Mais o\xc3\xb9 est-ce que j'ai mis mes lunettes?\x7Je les avais juste avant que ces Cogs ne prennent mon b\xc3\xa2timent.\x7Va vaincre des Cogs pour retrouver les lunettes qu'ils m'ont vol\xc3\xa9es.\x7Quand tu les auras retrouv\xc3\xa9es, reviens me voir pour avoir une r\xc3\xa9compense."
QuestScript145_1 = "Je vois que tu n'as pas eu de probl\xc3\xa8mes avec le tramway!\x7\xc3\x89coute, les Cogs ont vol\xc3\xa9 notre brosse \xc3\xa0 tableaux.\x7Va dans les rues et combats les Cogs jusqu'a ce que tu retrouves la brosse.\x7Pour atteindre les rues, passe par un des tunnels comme celui-ci :"
QuestScript145_2 = "Quand tu auras retrouv\xc3\xa9 notre brosse, ramene-la ici.\x7N'oublie pas : si tu as besoin de gags, va faire un tour de tramway.\x7De meme, si tu as besoin de r\xc3\xa9cup\xc3\xa9rer des rigolpoints, ramasse des c\xc3\xb4nes de glace sur le terrain de jeu."
QuestScript150_1 = 'Oh... le prochain d\xc3\xa9fi pourrait \xc3\xaatre trop difficile pour que tu le fasses tout(e) seul(e)!'
QuestScript150_2 = 'Pour te faire des contacts, trouve un autre joueur et utilise le bouton Nouvel ami.'
QuestScript150_3 = "Une fois que tu t'es fait un(e) ami(e), reviens ici."
QuestScript150_4 = 'Certains d\xc3\xa9fis sont trop difficiles pour un Toon seul!'
MissingKeySanityCheck = 'Ignorer'
SellbotBossName = 'Premier Vice-\nPr\xc3\xa9sident'
CashbotBossName = 'Vice-\nPr\xc3\xa9sident'
LawbotBossName = 'Chief Justice'
BossCogNameWithDept = '%(name)s\n%(dept)s'
BossCogPromoteDoobers = 'En vertu des pouvoirs qui me sont conf\xc3\xa9r\xc3\xa9s, tu es promu au grade %s. F\xc3\xa9licitations!'
BossCogDoobersAway = {
    's': 'Va! Et r\xc3\xa9alise cette vente!'}
BossCogWelcomeToons = 'Bienvenue aux nouveaux Cogs!'
BossCogPromoteToons = 'En vertu des pouvoirs qui me sont conf\xc3\xa9r\xc3\xa9s, tu es promu au grade %s. F\xc3\xa9licitations!'
CagedToonInterruptBoss = 'H\xc3\xa9! Hou! H\xc3\xa9 l\xc3\xa0-bas!'
CagedToonRescueQuery = 'Alors les Toons, vous \xc3\xaates venus me sauver ?'
BossCogDiscoverToons = 'Eh? Des Toons! D\xc3\xa9guis\xc3\xa9s!'
BossCogAttackToons = "\xc3\x80 l'attaque!!"
CagedToonDrop = [
    "Bon travail! Tu l'\xc3\xa9puises!",
    "Ne le l\xc3\xa2chez pas! Il va s'enfuir!",
    'Vous \xc3\xaates super les copains!',
    "Fantastique! Vous l'avez presque maintenant!"]
CagedToonPrepareBattleTwo = "Attention, il essaie de s'enfuir!\x7Aidez-moi, tout le monde - montez jusque l\xc3\xa0 et arr\xc3\xaatez-le!"
CagedToonPrepareBattleThree = 'Youpi, je suis presque libre!\x7Maintenant vous devez attaquer le vice-pr\xc3\xa9sident des Cogs directement.\x7J\'ai tout un lot de tartes que vous pouvez utiliser!\x7Sautez en l\'air et touchez le fond de ma cage, je vous donnerai des tartes.\x7Appuyez sur la touche "Inser" pour lancer les tartes une fois que vous les avez!'
BossBattleNeedMorePies = 'Vous avez besoin de plus de tartes!'
BossBattleHowToGetPies = "Sautez en l'air pour toucher la cage et avoir des tartes."
BossBattleHowToThrowPies = 'Appuyez sur la touche "Inser" pour lancer les tartes!'
CagedToonYippee = 'G\xc3\xa9nial!'
CagedToonThankYou = "C'est super d'\xc3\xaatre libre!\x7Merci pour toute votre aide!\x7Je suis \xc3\xa0 votre service.\x7Si jamais vous avez besoin d'aide pour un combat, vous pouvez m'appeler!\x7Cliquez simplement sur le bouton SOS pour m'appeler."
CagedToonPromotion = '\x7Dis donc - ce vice-pr\xc3\xa9sident Cog a laiss\xc3\xa9 derri\xc3\xa8re lui les papiers de ta promotion.\x7Je vais les envoyer pour toi en sortant, pour que tu aies ta promotion!'
CagedToonLastPromotion = '\x7Waou, tu as atteint le niveau %s sur ton costume de Cog!\x7Les Cogs ne montent pas en grade plus haut que \xc3\xa7a.\x7Tu ne peux plus monter ton costume de Cog en grade, mais tu peux \xc3\xa9videmment continuer \xc3\xa0 sauver des Toons!'
CagedToonHPBoost = '\x7Tu as sauv\xc3\xa9 beaucoup de Toons dans ce QG.\x7Le Conseil de Toontown a d\xc3\xa9cid\xc3\xa9 de te donner un autre rigolpoint. F\xc3\xa9licitations!'
CagedToonMaxed = "\x7Je vois que tu as un costume de Cog de niveau %s. Tr\xc3\xa8s impressionnant!\x7De la part du Conseil de Toontown, merci d'\xc3\xaatre revenu(e) sauver encore plus de Toons!"
CagedToonGoodbye = '\xc3\x80 la prochaine!'
CagedToonBattleThree = {
    10: 'Joli saut, %(toon)s. Voil\xc3\xa0 quelques tartes!',
    11: 'Salut, %(toon)s! Prenez des tartes!',
    12: 'H\xc3\xa9 l\xc3\xa0,%(toon)s! Vous avez des tartes maintenant!',
    20: "H\xc3\xa9, %(toon)s! Sautez jusqu'\xc3\xa0 ma cage et prenez des tartes \xc3\xa0 lancer!",
    21: 'H\xc3\xa9, %(toon)s! Utilisez la touche "Ctrl" pour sauter et toucher ma cage!',
    100: 'Appuyez sur la touche "Inser" pour lancer une tarte!',
    101: 'Le compteur bleu montre \xc3\xa0 quelle hauteur ta tarte va monter.',
    102: "Essaie d'abord de lancer une tarte sous son ch\xc3\xa2ssis pour bousiller son m\xc3\xa9canisme.",
    103: "Attends que la porte s'ouvre, et lance une tarte \xc3\xa0 l'int\xc3\xa9rieur.",
    104: "Lorsqu'il est \xc3\xa9tourdi, frappe-le au visage ou au torse pour le renverser!",
    105: "Tu sauras que tu l'as frapp\xc3\xa9 comme il faut quand tu verras une tache de couleur.",
    106: 'Si tu frappes un Toon avec une tarte, cela donne \xc3\xa0 ce Toon un rigolpoint!'}
CagedToonBattleThreeMaxGivePies = 12
CagedToonBattleThreeMaxTouchCage = 21
CagedToonBattleThreeMaxAdvice = 106
CashbotBossHadEnough = "\xc3\x87a suffit. J'en ai assez de ces Toons si \xc3\xa9nervants!"
CashbotBossOuttaHere = "J'ai un train \xc3\xa0 prendre!"
ResistanceToonName = 'In\xc3\xa8s Pionne'
ResistanceToonCongratulations = "Tu y es arriv\xc3\xa9(e)! F\xc3\xa9licitations!\x7Tu es un membre de valeur de la R\xc3\xa9sistance!\x7Voici une phrase tr\xc3\xa8s sp\xc3\xa9ciale que tu peux utiliser en cas de situation difficile :\x7%s\x7Quand tu la prononces, %s.\x7Mais tu ne peux l'utiliser qu'une seule fois, alors choisis bien ton moment!"
ResistanceToonToonupInstructions = 'Tous les Toons qui sont pr\xc3\xa8s de toi vont gagner %s rigolpoints.'
ResistanceToonToonupAllInstructions = 'Tous les Toons qui sont pr\xc3\xa8s de toi vont gagner un renouvellement de tout leur stock de rigolpoints.'
ResistanceToonMoneyInstructions = 'Tous les Toons qui sont pr\xc3\xa8s de toi vont gagner %s bonbons.'
ResistanceToonMoneyAllInstructions = 'Tous les Toons qui sont pr\xc3\xa8s de toi vont remplir leurs pots de bonbons.'
ResistanceToonRestockInstructions = 'Tous les Toons qui sont pr\xc3\xa8s de toi vont compl\xc3\xa9ter leur stock de "%s" gags.'
ResistanceToonRestockAllInstructions = 'Tous les Toons qui sont pr\xc3\xa8s de toi vont compl\xc3\xa9ter enti\xc3\xa8rement leur stock de gags.'
ResistanceToonLastPromotion = '\x7Waouh, tu as atteint le niveau %s de ton costume de Cog!\x7Les Cogs ne vont jamais plus haut que ce niveau.\x7Tu ne peux plus rien ajouter \xc3\xa0 ton costume de Cog mais tu peux bien s\xc3\xbbr continuer \xc3\xa0 travailler pour la R\xc3\xa9sistance!'
ResistanceToonHPBoost = '\x7Tu as beaucoup fait pour la R\xc3\xa9sistance.\x7Le Conseil des Toons a d\xc3\xa9cid\xc3\xa9 de te donner un autre rigolpoint. F\xc3\xa9licitations!'
ResistanceToonMaxed = "\x7Je vois que tu as un costume de Cog de niveau %s. Tr\xc3\xa8s impressionnant!\x7De la part du Conseil des Toons, merci d'\xc3\xaatre revenu pour secourir encore plus de Toons!"
CashbotBossCogAttack = 'Attrapez-les!!!'
ResistanceToonWelcome = "\xc3\x87a y est, tu y es arriv\xc3\xa9! Suis-moi jusqu'au coffre-fort principal avant que le Vice-Pr\xc3\xa9sident ne nous trouve!"
ResistanceToonTooLate = 'Zut alors! Nous arrivons trop tard!'
CashbotBossDiscoverToons1 = 'Ah-AH!'
CashbotBossDiscoverToons2 = 'Il me semblait bien que \xc3\xa7a sentait le Toon par ici! Imposteurs!'
ResistanceToonKeepHimBusy = 'Occupe-le! Je vais pr\xc3\xa9parer un pi\xc3\xa8ge!'
ResistanceToonWatchThis = 'Regarde \xc3\xa7a!'
CashbotBossGetAwayFromThat = 'Eh! Ne touche pas \xc3\xa0 \xc3\xa7a!'
ResistanceToonCraneInstructions1 = "Prends le contr\xc3\xb4le d'un aimant en montant sur un podium."
ResistanceToonCraneInstructions2 = 'Utilise les fl\xc3\xa8ches de ton clavier pour d\xc3\xa9placer la grue et appuie sur la touche Ctrl pour attraper un objet.'
ResistanceToonCraneInstructions3 = 'Attrape un coffre-fort avec un aimant et fais tomber le casque de s\xc3\xa9curit\xc3\xa9 du Vice-Pr\xc3\xa9sident.'
ResistanceToonCraneInstructions4 = 'Une fois que le casque est tomb\xc3\xa9, prends un goon d\xc3\xa9sactiv\xc3\xa9 et frappe-le \xc3\xa0 la t\xc3\xaate!'
ResistanceToonGetaway = 'Eek! Courons!'
CashbotCraneLeave = 'Quitter la grue'
CashbotCraneAdvice = 'Utilise les fl\xc3\xa8ches de ton clavier pour d\xc3\xa9placer la grue au-dessus.'
CashbotMagnetAdvice = 'Maintiens la touche Ctrl enfonc\xc3\xa9e pour attraper des objets.'
CashbotCraneLeaving = 'En train de quitter la grue'
MintElevatorRejectMessage = "Tu ne peux pas entrer dans les Fabriques \xc3\xa0 Sous avant d'avoir compl\xc3\xa9t\xc3\xa9 ton %s costume de Cog."
BossElevatorRejectMessage = "Tu ne peux pas monter dans cet ascenseur avant d'avoir gagn\xc3\xa9 une promotion."
FurnitureTypeName = 'Meuble'
PaintingTypeName = 'Tableau'
ClothingTypeName = 'V\xc3\xaatement'
ChatTypeName = 'Phrase de Chat rapide'
EmoteTypeName = 'Le\xc3\xa7ons de com\xc3\xa9die'
BeanTypeName = 'Bonbons'
PoleTypeName = 'Canne \xc3\xa0 p\xc3\xaache'
WindowViewTypeName = 'Vue de la fen\xc3\xaatre'
PetTrickTypeName = 'Entra\xc3\xaenement du Doudou'
GardenTypeName = 'Mat\xc3\xa9riaux de jardinage'
RentalTypeName = 'Article \xc3\xa0 louer'
GardenStarterTypeName = 'Kit de jardinage'
RentalTime = 'Heures de'
RentalCannon = 'Canons!'
EstateCannonGameEnd = 'La location du jeu du canon est termin\xc3\xa9e.'
GameTableRentalEnd = 'La location de la table de jeu est termin\xc3\xa9e.'
MessageConfirmRent = 'Commencer \xc3\xa0 louer? Annule pour enregistrer la location pour plus tard'
MessageConfirmGarden = 'Veux-tu vraiment commencer un jardin?'
FurnitureYourOldCloset = 'ton ancienne armoire'
FurnitureYourOldBank = 'ton ancienne tirelire'
ChatItemQuotes = '"%s"'
FurnitureNames = {
    100: 'Fauteuil',
    105: 'Fauteuil',
    110: 'Chaise',
    120: 'Chaise de bureau',
    130: 'Chaise en rondins',
    140: 'Chaise homard',
    145: 'Chaise de survie',
    150: 'Tabouret selle',
    160: 'Chaise locale',
    170: 'Chaise g\xc3\xa2teau',
    200: 'Lit',
    205: 'Lit',
    210: 'Lit',
    220: 'Lit baignoire',
    230: 'Lit feuille',
    240: 'Lit bateau',
    250: 'Hamac cactus',
    260: 'Lit cr\xc3\xa8me glac\xc3\xa9e',
    300: 'Piano m\xc3\xa9canique',
    310: 'Orgue',
    400: 'Chemin\xc3\xa9e',
    410: 'Chemin\xc3\xa9e',
    420: 'Chemin\xc3\xa9e ronde',
    430: 'Chemin\xc3\xa9e',
    440: 'Chemin\xc3\xa9e pomme',
    500: 'Armoire',
    502: 'Armoire pour 15 v\xc3\xaatements',
    510: 'Armoire',
    512: 'Armoire pour 15 v\xc3\xaatements',
    600: 'Petite lampe',
    610: 'Lampe haute',
    620: 'Lampe de table',
    625: 'Lampe de table',
    630: 'Lampe Daisy',
    640: 'Lampe Daisy',
    650: 'Lampe m\xc3\xa9duse',
    660: 'Lampe m\xc3\xa9duse',
    670: 'Lampe cow-boy',
    700: 'Chaise capitonn\xc3\xa9e',
    705: 'Chaise capitonn\xc3\xa9e',
    710: 'Divan',
    715: 'Divan',
    720: 'Divan foin',
    730: 'Divan sabl\xc3\xa9',
    800: 'Bureau',
    810: 'Bureau en rondins',
    900: 'Porte-parapluie',
    910: 'Portemanteau',
    920: 'Poubelle',
    930: 'Champignon rouge',
    940: 'Champignon jaune',
    950: 'Portemanteau',
    960: '\xc3\x89tal onneau',
    970: 'Cactus',
    980: 'Tipi',
    1000: 'Grand tapis',
    1010: 'Tapis rond',
    1015: 'Tapis rond',
    1020: 'Petit tapis',
    1030: 'Paillasson',
    1100: 'Vitrine',
    1110: 'Vitrine',
    1120: 'Biblioth\xc3\xa8que haute',
    1130: 'Biblioth\xc3\xa8que basse',
    1140: 'Coffre Sundae',
    1200: "Table d'appui",
    1210: 'Petite table',
    1215: 'Petite table',
    1220: 'Table de salon',
    1230: 'Table de salon',
    1240: 'Table de plongeur',
    1250: 'Table cookie',
    1260: 'Table de chevet',
    1300: 'Tirelire de 1000 bonbons',
    1310: 'Tirelire de 2500 bonbons',
    1320: 'Tirelire de 5000 bonbons',
    1330: 'Tirelire de 7500 bonbons',
    1340: 'Tirelire de 10000 bonbons',
    1399: 'T\xc3\xa9l\xc3\xa9phone',
    1400: 'Toon C\xc3\xa9zanne',
    1410: 'Fleurs',
    1420: 'Mickey contemporain',
    1430: 'Toon Rembrandt',
    1440: 'Paysage Toon',
    1441: 'Cheval de Whistler',
    1442: '\xc3\x89toile Toon',
    1443: 'Pas une tarte',
    1500: 'Radio',
    1510: 'Radio',
    1520: 'Radio',
    1530: 'T\xc3\xa9l\xc3\xa9vision',
    1600: 'Vase bas',
    1610: 'Vase haut',
    1620: 'Vase bas',
    1630: 'Vase haut',
    1640: 'Vase bas',
    1650: 'Vase bas',
    1660: 'Vase corail',
    1661: 'Vase coquillage',
    1700: 'Chariot de pop-corn',
    1710: 'Coccinelle',
    1720: 'Fontaine',
    1725: 'Machine \xc3\xa0 laver',
    1800: 'Aquarium',
    1810: 'Aquarium',
    1900: 'Poisson-scie',
    1910: 'Requin-marteau',
    1920: 'Cornes porte-manteau',
    1930: 'Sombrero classique',
    1940: 'Sombrero fantaisie',
    1950: 'Attrapeur de r\xc3\xaaves',
    1960: 'Fer \xc3\xa0 cheval',
    1970: 'Portrait de bison',
    2000: 'Balan\xc3\xa7oire bonbon',
    2010: 'Toboggan g\xc3\xa2teau',
    3000: 'Baignoire Banana Split',
    10000: 'Petite citrouille',
    10010: 'Grande citrouille'}
ClothingArticleNames = ('Chemise', 'Chemise', 'Chemise', 'Short', 'Short', 'Jupe', 'Short')
ClothingTypeNames = {
    1400: 'Chemise de Mathieu',
    1401: 'Chemise de Jessica',
    1402: 'Chemise de Marissa'}
SurfaceNames = ('Papier peint', 'Moulures', 'Rev\xc3\xaatement de sol', 'Lambris', 'Bordure')
WallpaperNames = {
    1000: 'Parchemin',
    1100: 'Milan',
    1200: 'Douvres',
    1300: 'Victoria',
    1400: 'Newport',
    1500: 'Pastoral',
    1600: 'Arlequin',
    1700: 'Lune',
    1800: '\xc3\x89toiles',
    1900: 'Fleurs',
    2000: 'Jardin de printemps',
    2100: 'Jardin classique',
    2200: 'Jour de course',
    2300: 'Marqu\xc3\xa9!',
    2400: 'Nuage 9',
    2500: 'Vigne vierge',
    2600: 'Printemps',
    2700: 'Kokeshi',
    2800: 'Petits bouquets',
    2900: 'Poisson ange',
    3000: 'Bulles',
    3100: 'Bulles',
    3200: '\xc3\x80 la p\xc3\xaache',
    3300: 'Poisson stop',
    3400: 'Hippocampe',
    3500: 'Coquillages',
    3600: "Sous l'eau",
    3700: 'Bottes',
    3800: 'Cactus',
    3900: 'Chapeau de cow-boy',
    10100: 'Chats',
    10200: 'Chauve-souris',
    11000: 'Flocons de neige',
    11100: 'Houx',
    11200: 'Bonhomme de neige',
    13000: 'Tr\xc3\xa8fle',
    13100: 'Tr\xc3\xa8fle',
    13200: 'Arc-en-ciel',
    13300: 'Tr\xc3\xa8fle'}
FlooringNames = {
    1000: 'Parquet',
    1010: 'Moquette',
    1020: 'Carrelage losange',
    1030: 'Carrelage losange',
    1040: 'Pelouse',
    1050: 'Briques beiges',
    1060: 'Briques rouges',
    1070: 'Carrelage carr\xc3\xa9',
    1080: 'Pierre',
    1090: 'Bois',
    1100: 'Terre',
    1110: 'Pavage de bois',
    1120: 'Carrelage',
    1130: "Nid d'abeilles",
    1140: 'Eau',
    1150: 'Carrelage plage',
    1160: 'Carrelage plage',
    1170: 'Carrelage plage',
    1180: 'Carrelage plage',
    1190: 'Sable',
    10000: 'Gla\xc3\xa7on',
    10010: 'Igloo',
    11000: 'Tr\xc3\xa8fle',
    11010: 'Tr\xc3\xa8fle'}
MouldingNames = {
    1000: 'Noueux',
    1010: 'Peint',
    1020: 'Dent\xc3\xa9',
    1030: 'Fleurs',
    1040: 'Fleurs',
    1050: 'Coccinelle'}
WainscotingNames = {
    1000: 'Peint',
    1010: 'Panneau de bois',
    1020: 'Bois'}
WindowViewNames = {
    10: 'Grand jardin',
    20: 'Jardin sauvage',
    30: 'Jardin grec',
    40: 'Paysage urbain',
    50: 'Far West',
    60: "Sous l'oc\xc3\xa9an",
    70: '\xc3\x8ele tropicale',
    80: 'Nuit \xc3\xa9toil\xc3\xa9e',
    90: 'Lagon Tiki',
    100: 'Fronti\xc3\xa8re gel\xc3\xa9e',
    110: 'Pays fermier',
    120: 'Camp local',
    130: 'Grand rue'}
NewCatalogNotify = 'De nouveaux articles sont pr\xc3\xaats \xc3\xa0 \xc3\xaatre command\xc3\xa9s par t\xc3\xa9l\xc3\xa9phone!'
NewDeliveryNotify = "Un colis t'attend dans ta bo\xc3\xaete aux lettres!"
CatalogNotifyFirstCatalog = "Ton premier catalogue est arriv\xc3\xa9! Tu peux l'utiliser pour commander de nouveaux objets pour toi ou pour ta maison."
CatalogNotifyNewCatalog = 'Ton catalogue N\xc2\xb0%s est arriv\xc3\xa9! Tu peux utiliser ton t\xc3\xa9l\xc3\xa9phone pour commander des articles dans le catalogue de Clarabelle.'
CatalogNotifyNewCatalogNewDelivery = "Un colis t'attend dans ta bo\xc3\xaete aux lettres! Ton catalogue N\xc2\xb0%s est aussi arriv\xc3\xa9!"
CatalogNotifyNewDelivery = "Un colis t'attend dans ta bo\xc3\xaete aux lettres!"
CatalogNotifyNewCatalogOldDelivery = "Ton catalogue N\xc2\xb0%s est arriv\xc3\xa9, et des objets t'attendent encore dans ta bo\xc3\xaete aux lettres!"
CatalogNotifyOldDelivery = "Des articles t'attendent encore dans ta bo\xc3\xaete aux lettres!"
CatalogNotifyInstructions = 'Clique sur le bouton "Retour \xc3\xa0 la maison" sur la carte de ton journal de bord, puis va jusqu\'au t\xc3\xa9l\xc3\xa9phone qui est dans ta maison.'
CatalogNewDeliveryButton = 'Nouvelle\nlivraison!'
CatalogNewCatalogButton = 'Nouveau\ncatalogue'
CatalogSaleItem = 'Vente!'
DistributedMailboxEmpty = "Ta bo\xc3\xaete aux lettres est vide pour l'instant. Reviens ici chercher les articles que tu as command\xc3\xa9s par t\xc3\xa9l\xc3\xa9phone quand ils seront livr\xc3\xa9s!"
DistributedMailboxWaiting = "Ta bo\xc3\xaete aux lettres est vide pour l'instant, mais le paquet que tu as command\xc3\xa9 est en chemin. Reviens voir plus tard!"
DistributedMailboxReady = 'Ta commande est arriv\xc3\xa9e!'
DistributedMailboxNotOwner = "D\xc3\xa9sol\xc3\xa9, ce n'est pas ta bo\xc3\xaete aux lettres."
DistributedPhoneEmpty = "Tu peux utiliser n'importe quel t\xc3\xa9l\xc3\xa9phone pour commander des articles pour toi et pour ta maison. De nouveaux articles seront propos\xc3\xa9s dans l'avenir.\n\nAucun article n'est disponible \xc3\xa0 la commande maintenant, mais reviens voir plus tard!"
Clarabelle = 'Clarabelle'
MailboxExitButton = 'Fermer bo\xc3\xaete\naux lettres'
MailboxAcceptButton = 'Accepter'
MailBoxDiscard = 'Refuser'
MailBoxDiscardVerify = 'Es-tu s\xc3\xbbr de vouloir rejeter %s ?'
MailboxOneItem = 'Ta bo\xc3\xaete aux lettres contient 1 objet.'
MailboxNumberOfItems = 'Ta bo\xc3\xaete aux lettres contient %s objets.'
MailboxGettingItem = 'R\xc3\xa9cup\xc3\xa9ration de %s dans la bo\xc3\xaete aux lettres.'
MailboxGiftTag = 'Cadeau de\xc2\xa0: %s'
MailboxGiftTagAnonymous = 'Anonyme'
MailboxItemNext = 'Objet\nsuivant'
MailboxItemPrev = 'Objet\npr\xc3\xa9c\xc3\xa9dent'
MailboxDiscard = 'Rejeter'
MailboxLeave = 'Accepter'
CatalogCurrency = 'bonbons'
CatalogHangUp = 'Raccrocher'
CatalogNew = 'NOUVEAUT\xc3\x89'
CatalogBackorder = 'PR\xc3\x89-COMMANDE'
CatalogPagePrefix = 'Page'
CatalogGreeting = "Bonjour! Merci d'avoir appel\xc3\xa9 le catalogue de Clarabelle. Que puis-je pour toi?"
CatalogGoodbyeList = [
    'Au revoir!',
    'Rappelle bient\xc3\xb4t!',
    'Merci de ton appel!',
    'OK, au revoir!',
    'Au revoir!']
CatalogHelpText1 = 'Tourne la page pour voir les articles qui sont en vente.'
CatalogSeriesLabel = 'S\xc3\xa9rie %s'
CatalogGiftFor = 'Acheter un cadeau pour :'
CatalogGiftTo = 'Pour : %s'
CatalogGiftToggleOn = "Arr\xc3\xaater d'acheter\ndes cadeaux"
CatalogGiftToggleOff = 'Acheter des\ncadeaux'
CatalogGiftToggleWait = "En train d'essayer!..."
CatalogGiftToggleNoAck = 'Indisponible'
CatalogPurchaseItemAvailable = 'Parfait ! Peut commencer \xc3\xa0 utiliser ton cadeau d\xc3\xa8s maintenant.'
CatalogPurchaseGiftItemAvailable = 'Parfait ! Ton cadeau pour %s sera livr\xc3\xa9 dans sa bo\xc3\xaete aux lettres.'
CatalogPurchaseItemOnOrder = 'F\xc3\xa9licitations! Ton achat sera bient\xc3\xb4t livr\xc3\xa9 dans ta bo\xc3\xaete aux lettres.'
CatalogPurchaseGiftItemOnOrder = ' Parfait ! Ton cadeau pour %s sera livr\xc3\xa9 dans sa bo\xc3\xaete aux lettres.'
CatalogAnythingElse = 'Puis-je autre chose pour toi?'
CatalogPurchaseClosetFull = 'Ton placard est plein. Tu peux acheter cet article, mais tu devras supprimer quelque chose de ton placard pour faire de la place quand il arrivera.\n\nTu veux quand m\xc3\xaame acheter cet article ?'
CatalogAcceptClosetFull = 'Ton placard est plein. Tu dois rentrer et supprimer quelque chose de ton placard pour faire de la place pour cet objet avant de pouvoir le sortir de la bo\xc3\xaete aux lettres.'
CatalogAcceptShirt = 'Tu portes maintenant ta nouvelle chemise. Ce que tu portais avant a \xc3\xa9t\xc3\xa9 mis dans ton placard.'
CatalogAcceptShorts = 'Tu portes maintenant ton nouveau short. Ce que tu portais avant a \xc3\xa9t\xc3\xa9 mis dans ton placard.'
CatalogAcceptSkirt = 'Tu portes maintenant ta nouvelle jupe. Ce que tu portais avant a \xc3\xa9t\xc3\xa9 mis dans ton placard.'
CatalogAcceptPole = 'Tu peux maintenant attraper des poissons plus gros avec ta nouvelle canne!'
CatalogAcceptPoleUnneeded = 'Tu as d\xc3\xa9j\xc3\xa0 une canne meilleure que celle-ci!'
CatalogAcceptChat = 'Tu poss\xc3\xa8des maintenant une nouvelle phrase de Chat rapide.'
CatalogAcceptEmote = 'Tu poss\xc3\xa8des maintenant une nouvelle \xc3\xa9motion !'
CatalogAcceptBeans = 'Tu as re\xc3\xa7u des bonbons !'
CatalogAcceptRATBeans = 'Ta r\xc3\xa9compense de recrue Toon est arriv\xc3\xa9e!'
CatalogAcceptGarden = 'Tes mat\xc3\xa9riaux de jardinage sont arriv\xc3\xa9s!'
CatalogAcceptPet = 'Tu poss\xc3\xa8des maintenant un nouveau tour pour ton Doodle !'
CatalogPurchaseHouseFull = 'Ta maison est pleine. Tu peux acheter cet article, mais tu devras supprimer quelque chose dans ta maison pour faire de la place quand il arrivera.\n\nTu veux quand m\xc3\xaame acheter cet article ?'
CatalogAcceptHouseFull = 'Ta maison est pleine. Tu dois rentrer et supprimer quelque chose dans ta maison pour faire de la place pour cet objet avant de pouvoir le sortir de la bo\xc3\xaete aux lettres.'
CatalogAcceptInAttic = 'Ton nouvel article est maintenant dans ton grenier. Pour le placer dans ta maison, va \xc3\xa0 l\'int\xc3\xa9rieur et clique sur le bouton "D\xc3\xa9placer les meubles".'
CatalogAcceptInAtticP = 'Tes nouveaux articles sont maintenant dans ton grenier. Pour les placer dans ta maison, va \xc3\xa0 l\'int\xc3\xa9rieur et clique sur le bouton "D\xc3\xa9placer les meubles".'
CatalogPurchaseMailboxFull = "Ta bo\xc3\xaete aux lettres est pleine! Tu ne peux pas acheter cet article avant d'avoir sorti des articles de ta bo\xc3\xaete aux lettres pour y faire de la place."
CatalogPurchaseGiftMailboxFull = 'La bo\xc3\xaete aux lettres de %s est pleine ! Tu ne peux pas acheter cet article.'
CatalogPurchaseOnOrderListFull = "Tu as trop d'articles en commande actuellement. Tu ne peux pas commander d'autres articles avant que ceux que tu as d\xc3\xa9j\xc3\xa0 command\xc3\xa9s ne soient arriv\xc3\xa9s."
CatalogPurchaseGiftOnOrderListFull = "%s a actuellement trop d'articles en commande."
CatalogPurchaseGeneralError = "L'article n'a pas pu \xc3\xaatre achet\xc3\xa9 \xc3\xa0 cause d'une erreur interne au jeu: code d'erreur %s."
CatalogPurchaseGiftGeneralError = "Le cadeau n'a pas pu \xc3\xaatre offert \xc3\xa0 ton(tes) %(friend) en raison d'une erreur interne %(error) au jeu."
CatalogPurchaseGiftNotAGift = "Cet article n'a pas pu \xc3\xaatre envoy\xc3\xa9 \xc3\xa0 %s parce qu'il n'est pas assez avanc\xc3\xa9 dans le jeu."
CatalogPurchaseGiftWillNotFit = "Cet article n'a pas pu \xc3\xaatre envoy\xc3\xa9 \xc3\xa0 %s parce qu'il ne lui correspond pas."
CatalogPurchaseGiftLimitReached = "Cet article n'a pas pu \xc3\xaatre envoy\xc3\xa9 \xc3\xa0 %s parce qu'il le poss\xc3\xa8de d\xc3\xa9j\xc3\xa0."
CatalogPurchaseGiftNotEnoughMoney = "Cet article n'a pas pu \xc3\xaatre envoy\xc3\xa9 \xc3\xa0 %s parce que tu n'as pas les moyens de l'acheter."
CatalogAcceptGeneralError = "L'article n'a pas pu \xc3\xaatre retir\xc3\xa9 de ta bo\xc3\xaete aux lettres \xc3\xa0 cause d'une erreur interne au jeu: code d'erreur %s."
CatalogAcceptRoomError = "Tu n'as pas de place pour mettre cet article. Tu vas devoir te d\xc3\xa9barasser de quelquechose."
CatalogAcceptLimitError = "Tu poss\xc3\xa8des d\xc3\xa9j\xc3\xa0 beaucoup d'exemplaires de cet article. Tu vas devoir te d\xc3\xa9barasser de quelquechose."
CatalogAcceptFitError = "Cela ne t'ira pas ! Tu dois en faire don \xc3\xa0 un toon qui en a besoin."
CatalogAcceptInvalidError = "Cet article n'est plus \xc3\xa0 la mode. Tu dois en faire don \xc3\xa0 un toon qui en a besoin."
MailboxOverflowButtonDicard = 'Supprimer'
MailboxOverflowButtonLeave = 'Garder'
HDMoveFurnitureButton = 'D\xc3\xa9placer\nles meubles'
HDStopMoveFurnitureButton = 'Meubles\nplac\xc3\xa9s'
HDAtticPickerLabel = 'Dans le grenier'
HDInRoomPickerLabel = 'Dans la pi\xc3\xa8ce'
HDInTrashPickerLabel = '\xc3\x80 la poubelle'
HDDeletePickerLabel = 'Supprimer ?'
HDInAtticLabel = 'Grenier'
HDInRoomLabel = 'Pi\xc3\xa8ce'
HDInTrashLabel = 'Poubelle'
HDToAtticLabel = 'Mettre\nau grenier'
HDMoveLabel = 'D\xc3\xa9placer'
HDRotateCWLabel = 'Tourner vers la droite'
HDRotateCCWLabel = 'Tourner vers la gauche'
HDReturnVerify = 'Remettre cet objet dans le grenier ?'
HDReturnFromTrashVerify = 'Ressortir cet objet de la poubelle et le mettre dans le grenier ?'
HDDeleteItem = 'Clique sur OK pour mettre cet objet \xc3\xa0 la poubelle ou sur Annuler pour le garder.'
HDNonDeletableItem = 'Tu ne peux pas supprimer les objets de ce type!'
HDNonDeletableBank = 'Tu ne peux pas supprimer ta tirelire!'
HDNonDeletableCloset = 'Tu ne peux pas supprimer ton armoire!'
HDNonDeletablePhone = 'Tu ne peux pas supprimer ton t\xc3\xa9l\xc3\xa9phone!'
HDNonDeletableNotOwner = 'Tu ne peux pas supprimer les affaires de %s!'
HDHouseFull = "Ta maison est pleine. Tu dois supprimer quelque chose d'autre dans ta maison ou ton grenier avant de pouvoir ressortir cet article de la poubelle."
HDHelpDict = {
    'DoneMoving': 'Terminer la d\xc3\xa9coration de la pi\xc3\xa8ce.',
    'Attic': 'Voir la liste des objets qui sont au grenier. Les objets qui ne sont pas dans ta pi\xc3\xa8ce sont au grenier.',
    'Room': 'Voir la liste des objets qui sont dans la pi\xc3\xa8ce. Utile pour retrouver des objets perdus.',
    'Trash': 'Voir les objets qui sont dans la poubelle. Les objets les plus anciens sont supprim\xc3\xa9s apr\xc3\xa8s un temps ou si la poubelle d\xc3\xa9borde.',
    'ZoomIn': 'Agrandir la vue de la pi\xc3\xa8ce.',
    'ZoomOut': '\xc3\x89loigner la vue de la pi\xc3\xa8ce.',
    'SendToAttic': 'Stocker le meuble actuel dans le grenier.',
    'RotateLeft': 'Tourner vers la gauche.',
    'RotateRight': 'Tourner vers la droite.',
    'DeleteEnter': 'Passer en mode suppression.',
    'DeleteExit': 'Sortir du mode suppression.',
    'FurnitureItemPanelDelete': 'Mettre %s \xc3\xa0 la poubelle.',
    'FurnitureItemPanelAttic': 'Mettre %s dans la pi\xc3\xa8ce.',
    'FurnitureItemPanelRoom': 'Remettre %s au grenier.',
    'FurnitureItemPanelTrash': 'Remettre %s au grenier.'}
MessagePickerTitle = 'Tu as trop de phrases. Pour pouvoir acheter\n"%s"\n tu dois choisir une chose \xc3\xa0 retirer:'
MessagePickerCancel = lCancel
MessageConfirmDelete = 'Es-tu certain de vouloir retirer "%s" de ton menu de Chat rapide ?'
CatalogBuyText = 'Acheter'
CatalogRentText = 'Louer'
CatalogGiftText = 'Cadeau'
CatalogOnOrderText = 'En commande'
CatalogPurchasedText = 'D\xc3\xa9j\xc3\xa0\nachet\xc3\xa9'
CatalogGiftedText = 'Offert\n\xc3\xa0 toi'
CatalogPurchasedGiftText = 'D\xc3\xa9j\xc3\xa0\nPoss\xc3\xa9d\xc3\xa9'
CatalogMailboxFull = 'Pas de place'
CatalogNotAGift = "N'est pas un cadeau"
CatalogNoFit = 'ne va pas'
CatalogPurchasedMaxText = 'Maximum\nd\xc3\xa9j\xc3\xa0 achet\xc3\xa9'
CatalogVerifyPurchase = 'Acheter %(item)s pour %(price)s bonbons?'
CatalogVerifyRent = 'Louer %(item)s pour le prix de %(price)s bonbons?'
CatalogVerifyGift = 'Acheter %(item)s pour %(price)s bonbons comme cadeau pour %(friend)s?'
CatalogOnlyOnePurchase = "Tu ne peux avoir qu'un de ces articles \xc3\xa0 la fois. Si tu ach\xc3\xa8tes celui-l\xc3\xa0, il remplacera %(old)s.\n\nEs-tu certain(e) de vouloir acheter %(item)s pour %(price)s bonbons?"
CatalogExitButtonText = 'Raccrocher'
CatalogCurrentButtonText = 'Articles actuels'
CatalogPastButtonText = 'Articles pr\xc3\xa9c\xc3\xa9dents'
TutorialHQOfficerName = 'Harry du QG'
NPCToonNames = {
    20000: 'Tom Tuteur',
    999: 'Toon Tailleur',
    1000: lToonHQ,
    20001: Flippy,
    2001: Flippy,
    2002: 'Bob le Banquier',
    2003: 'Professeur Pete',
    2004: 'Tammy le Tailleur',
    2005: 'Larry le Libraire',
    2006: 'Vincent - Vendeur',
    2011: 'V\xc3\xa9ronique - Vendeuse',
    2007: lHQOfficerM,
    2008: lHQOfficerM,
    2009: lHQOfficerF,
    2010: lHQOfficerF,
    2012: "Vendeur de l'animalerie",
    2013: 'M. Vacarme',
    2014: 'Melle Vadrouille',
    2015: 'M. Vagabond',
    2101: 'Daniel le Dentiste',
    2102: 'Sherry le Sh\xc3\xa9rif',
    2103: 'Kitty Lerhume',
    2104: lHQOfficerM,
    2105: lHQOfficerM,
    2106: lHQOfficerF,
    2107: lHQOfficerF,
    2108: 'Canary Minederien',
    2109: 'Souffle douleur',
    2110: 'A. Fiche',
    2111: 'Diego Ladanse',
    2112: 'Dr Tom',
    2113: 'Rollo le Magnifique',
    2114: 'Rose D\xc3\xa9vent',
    2115: 'D\xc3\xa9d\xc3\xa9 Coupage',
    2116: 'Costaud McDougal',
    2117: 'Madame Putride',
    2118: 'Jesse Jememoque',
    2119: 'Meryl Semarre',
    2120: 'Professeur Morderire',
    2121: 'Madame Marrante',
    2122: 'Harry Lesinge',
    2123: 'Emile Esime',
    2124: 'Ga\xc3\xabtan Pipourtoi',
    2125: 'Lazy Mut',
    2126: 'Professeur Lagaffe',
    2127: 'Woody Troissous',
    2128: 'Loulou Fifou',
    2129: 'Frank Fort',
    2130: 'Sylvie Brateur',
    2131: 'Jeanne Laplume',
    2132: 'Daffy Don',
    2133: 'Dr E. Phorique',
    2134: 'Simone Silence-on-tourne',
    2135: 'Marie Satourne',
    2136: 'Sal Amandre',
    2137: 'Heureux Kikomulisse',
    2138: 'Gaston',
    2139: 'Bernard Bavunpeu',
    2140: 'Billy le p\xc3\xaacheur',
    2201: 'Pierre le Postier',
    2202: 'Paul Ochon',
    2203: lHQOfficerM,
    2204: lHQOfficerM,
    2205: lHQOfficerF,
    2206: lHQOfficerF,
    2207: 'Tony Truant',
    2208: 'Nicole Lacolle',
    2209: 'Henri Gole',
    2210: 'Val\xc3\xa9rie Golotte',
    2211: 'Sally Salive',
    2212: 'Max Imum',
    2213: 'Lucy Rustine',
    2214: 'Dino Zore',
    2215: 'Jean Aimarre',
    2216: 'Lady Sparue',
    2217: 'Jones Requin',
    2218: 'Fanny Larant',
    2219: 'Lanouille',
    2220: 'Louis Leroc',
    2221: 'Tina Pachang\xc3\xa9',
    2222: "Electre O'Cardiogramme",
    2223: 'Sasha Touille',
    2224: 'Joe Lefumeux',
    2225: 'Toumou le p\xc3\xaacheur',
    2301: 'Dr Faismarcher',
    2302: 'Professeur Tortillard',
    2303: 'Nancy Nanny',
    2304: lHQOfficerM,
    2305: lHQOfficerM,
    2306: lHQOfficerF,
    2307: lHQOfficerF,
    2308: 'Nancy Gaz',
    2309: 'Gros Bruce',
    2311: "Frank O'Debord",
    2312: 'Dr Sensible',
    2313: 'Lucy Boulette',
    2314: 'Ned Lafronde',
    2315: 'Val\xc3\xa9rie Deveau',
    2316: 'Cindy Ka',
    2318: 'Mac Aroni',
    2319: 'Annick',
    2320: 'Alfonse Danslebrouillard',
    2321: 'Vif le p\xc3\xaacheur',
    1001: 'Willy - Vendeur',
    1002: 'Billy - Vendeur',
    1003: lHQOfficerM,
    1004: lHQOfficerF,
    1005: lHQOfficerM,
    1006: lHQOfficerF,
    1007: 'Alain T\xc3\xa9rieur',
    1008: "Vendeur de l'animalerie",
    1009: 'M. Ouahouah',
    1010: 'Melle Ronron',
    1011: 'Mme Glouglou',
    1101: 'Sam Suffit',
    1102: 'Capitaine Carl',
    1103: "Frank L'\xc3\xa9caille",
    1104: 'Docteur Squale',
    1105: 'Amiral Crochet',
    1106: 'Mme Amidon',
    1107: 'Jim Nastic',
    1108: lHQOfficerM,
    1109: lHQOfficerF,
    1110: lHQOfficerM,
    1111: lHQOfficerF,
    1112: 'Gary Glouglou',
    1113: 'Anna-Lise Deussan',
    1114: 'Mick Robe',
    1115: 'Sheila Seiche, Avocate',
    1116: 'Bernard Bernache',
    1117: 'Capitaine Hautlecoeur',
    1118: 'Choppy McDougal',
    1121: 'Marthe Aupiqueur',
    1122: 'Petit Sal\xc3\xa9',
    1123: "Electre O'Magn\xc3\xa9tique",
    1124: 'Simon Strueux',
    1125: 'Elvire Debord',
    1126: 'Barnab\xc3\xa9 le p\xc3\xaacheur',
    1201: 'Barbara Bernache',
    1202: 'Art',
    1203: 'Ahab',
    1204: 'Rocky Roc',
    1205: lHQOfficerM,
    1206: lHQOfficerF,
    1207: lHQOfficerM,
    1208: lHQOfficerF,
    1209: 'Professeur Planche',
    1210: 'Yaka Saut\xc3\xa9',
    1211: 'Sarah Lenti',
    1212: 'Loulou Languedebois',
    1213: 'Dante Dauphin',
    1214: 'Aim\xc3\xa9 Duse',
    1215: 'Jean Peuplu',
    1216: 'Seymour Linet',
    1217: 'C\xc3\xa9cile Savet',
    1218: 'Tim Pacifique',
    1219: 'Yvon Alot',
    1220: 'Minnie Stair',
    1221: 'McKee Labulle',
    1222: 'A. Marre',
    1223: 'Sid Seiche',
    1224: 'Anna Conda',
    1225: 'Bonzo Boitrop',
    1226: 'Ho Hisse',
    1227: 'Coral',
    1228: 'Rozo le p\xc3\xaacheur',
    1301: 'Ernest',
    1302: 'Ginette',
    1303: 'G\xc3\xa9rard',
    1304: 'Hillary Varien',
    1305: lHQOfficerM,
    1306: lHQOfficerF,
    1307: lHQOfficerM,
    1308: lHQOfficerF,
    1309: 'Ecume de mer',
    1310: 'Ted Tentacule',
    1311: 'Jean Reveux',
    1312: 'Ga\xc3\xabtan Coque',
    1313: 'G\xc3\xa9rard Timon',
    1314: 'Ralph Rouill\xc3\xa9',
    1315: 'Docteur D\xc3\xa9rive',
    1316: 'Elodie Toire',
    1317: 'Paule Pylone',
    1318: 'Barnab\xc3\xa9 Bou\xc3\xa9e',
    1319: 'David Bienosec',
    1320: 'Aldo Plate',
    1321: 'Dinah Esservi',
    1322: 'Peter Coussin',
    1323: 'Ned Savon',
    1324: 'Perle D\xc3\xa9mer',
    1325: 'Ned Setter',
    1326: 'G. Lafritte',
    1327: 'Cindy Nosore',
    1328: 'Sam Ouraille',
    1329: 'Shelly Beaucoup',
    1330: 'Icare Bonize',
    1331: 'Guy Rlande',
    1332: 'Martin le p\xc3\xaacheur',
    3001: 'Ang\xc3\xa8le Ici',
    3002: lHQOfficerM,
    3003: lHQOfficerF,
    3004: lHQOfficerM,
    3005: lHQOfficerM,
    3006: 'Lenny - Vendeur',
    3007: 'Penny - Vendeuse',
    3008: 'Warren Fagot\xc3\xa9',
    3009: "Vendeur de l'animalerie",
    3010: 'M. Cabo',
    3011: 'Melle Cabriole',
    3012: 'M. Cadichon',
    3101: 'M. Lapin',
    3102: 'Tante Ang\xc3\xa8le',
    3103: 'Tanguy',
    3104: 'Bonnie',
    3105: 'Freddy Frigo',
    3106: 'Paul Poulemouill\xc3\xa9e',
    3107: 'Patty Touteseule',
    3108: 'Ted Tobogan',
    3109: 'Patricia',
    3110: 'Jack Pot',
    3111: 'O. Tain',
    3112: 'Allan Bic',
    3113: 'Harry Hyst\xc3\xa9rique',
    3114: 'Nathan Pastrop',
    3115: lHQOfficerM,
    3116: lHQOfficerF,
    3117: lHQOfficerM,
    3118: lHQOfficerM,
    3119: 'Carl Magne',
    3120: 'Mike Mouffles',
    3121: 'Joe Courant',
    3122: 'Lucy Luge',
    3123: 'Nicole Apon',
    3124: 'Lance Iceberg',
    3125: 'Colonel M\xc3\xa2chetout',
    3126: 'Colette Erol',
    3127: 'Alex T\xc3\xa9rieur',
    3128: 'George Lacolle',
    3129: 'Brigitte Boulanger',
    3130: 'Sandy',
    3131: 'Pablo Paresseux',
    3132: 'Braise Cendrar',
    3133: 'Dr Jevoismieux',
    3134: 'S\xc3\xa9bastien Toutseul',
    3135: 'Nelly Qu\xc3\xa9fi\xc3\xa9',
    3136: 'Claude Iqu\xc3\xa9',
    3137: 'M. Gel',
    3138: 'M. Empot\xc3\xa9',
    3139: 'Virginie Aimaitropaul',
    3140: 'Lucile la p\xc3\xaacheuse',
    3201: 'Tante Artique',
    3202: 'Tremblotte',
    3203: 'Walt',
    3204: 'Dr Ivan Deslunettes',
    3205: 'Boris Tourne',
    3206: 'Victoire Alarrach\xc3\xa9',
    3207: 'Dr Marmotter',
    3208: 'Phil Electrique',
    3209: 'Geoffroy Auxmains',
    3210: 'Sam Simiesque',
    3211: 'Gaelle Seg\xc3\xa8le',
    3212: 'Freddy Frigo',
    3213: lHQOfficerM,
    3214: lHQOfficerF,
    3215: lHQOfficerM,
    3216: lHQOfficerM,
    3217: 'Pierre Lasueur',
    3218: 'Lou Minaire',
    3219: 'Tom Tandem',
    3220: 'G. Ternue',
    3221: 'Nelly Neige',
    3222: 'Moricette Decuisine',
    3223: 'Chappy',
    3224: 'Agnes Kimo',
    3225: 'Frimas Ladouce',
    3226: 'Prosp\xc3\xa8re No\xc3\xabl',
    3227: 'Ray Ondesoleil',
    3228: 'Maurice Quetout',
    3229: 'Hernie Discale',
    3230: 'Benjy Boule-\xc3\xa0-z\xc3\xa9ro',
    3231: 'Choppy',
    3232: 'Albert le p\xc3\xaacheur',
    3301: 'Cathou Coupet',
    3302: 'Bjorn Bord',
    3303: 'Dr Flic-Flac',
    3304: 'Eddie le Y\xc3\xa9ti',
    3305: 'Mac Ram\xc3\xa9e',
    3306: 'Paul H\xc3\xa8re',
    3307: 'P\xc3\xaacheuse Fr\xc3\xa9d\xc3\xa9rique',
    3308: 'Marcel Glassault',
    3309: 'Th\xc3\xa9o Citron',
    3310: 'Professeur Flocon',
    3311: 'Cella Glasse',
    3312: 'J. Boulet de Mars',
    3313: lHQOfficerM,
    3314: lHQOfficerF,
    3315: lHQOfficerM,
    3316: lHQOfficerF,
    3317: 'Chris Crisse',
    3318: 'Alan Sthiver',
    3319: 'Bo Nedlaine',
    3320: 'Lisette Frisquette',
    3321: 'C\xc3\xa9dric Piolet',
    3322: 'Corinne Za',
    3323: 'Aurore Beau-R\xc3\xa9al',
    3324: 'Mandra Gore',
    3325: 'Alban Quise',
    3326: 'Blanche',
    3327: 'J. Gault',
    3328: 'R\xc3\xa9mi Taine',
    3329: 'Isaure Beti\xc3\xa8re',
    4001: 'Molly Masson',
    4002: lHQOfficerM,
    4003: lHQOfficerF,
    4004: lHQOfficerF,
    4005: lHQOfficerF,
    4006: 'Doe - Vendeur',
    4007: 'Ray - Vendeur',
    4008: 'Bernard Mony',
    4009: "Vendeur de l'animalerie",
    4010: 'M. Chris',
    4011: 'M. Neil',
    4012: 'Melle Western',
    4101: 'Tom',
    4102: 'Fifi',
    4103: 'Dr Tefaispasdebile',
    4104: lHQOfficerM,
    4105: lHQOfficerF,
    4106: lHQOfficerF,
    4107: lHQOfficerF,
    4108: 'Cl\xc3\xa9ment de Sol',
    4109: 'Carlos',
    4110: 'M\xc3\xa9tro Gnome',
    4111: 'Adam Levent',
    4112: 'Fa',
    4113: 'Madame Mani\xc3\xa8re',
    4114: 'Eric Ochet',
    4115: 'Labelle Decadix',
    4116: 'Piccolo',
    4117: 'Mandy Lynn',
    4118: 'Andr\xc3\xa9 Sansfrapper',
    4119: 'Moe Zart',
    4120: 'Viola Coussin',
    4121: 'Ray Mineur',
    4122: 'Armanthe R\xc3\xa9glisse',
    4123: "Ted l'\xc3\xa9clair",
    4124: 'Riff Iffifi',
    4125: 'M\xc3\xa9lodie Dantan',
    4126: 'Bel Canto',
    4127: 'Am\xc3\xa9d\xc3\xa9 Chausson',
    4128: 'Luciano Lescoop',
    4129: 'Terry Golo',
    4130: 'R\xc3\xa9mi Crophone',
    4131: 'Abraham Armoire',
    4132: 'Sally Tristounet',
    4133: 'D. Tach\xc3\xa9',
    4134: 'Dave Disco',
    4135: 'S\xc3\xa9raphin Ducompte',
    4136: 'Patty Pause',
    4137: 'Tony Doiseau',
    4138: 'R\xc3\xa9mi Depain',
    4139: 'Harmony Ka',
    4140: 'Ned Maladroit',
    4141: 'Jojo le p\xc3\xaacheur',
    4201: 'Tina',
    4202: 'Barry',
    4203: 'Jack B\xc3\xbbcheron',
    4204: lHQOfficerM,
    4205: lHQOfficerF,
    4206: lHQOfficerF,
    4207: lHQOfficerF,
    4208: 'Elise',
    4209: 'Mo V\xc3\xa9gou',
    4211: 'Carl Concerto',
    4212: 'Funeste Fun\xc3\xa8bre',
    4213: 'Fran Chement',
    4214: 'Tina Crampon',
    4215: 'Tim Rouletropr\xc3\xa8s',
    4216: 'K. Outchouc',
    4217: 'Anton Beaugar\xc3\xa7on',
    4218: 'Vanessa Vapasdutout',
    4219: 'Sid Sonate',
    4220: 'Jean-Bi\xc3\xa8re',
    4221: 'Moe Madrigal',
    4222: 'John Deuf',
    4223: 'Penny Souffleur',
    4224: 'Jim Jongle',
    4225: 'Holly St\xc3\xa9rie',
    4226: 'Georgina Gorge',
    4227: 'Francesca Taphonique',
    4228: 'August Ave',
    4229: 'June Comprendsrien',
    4230: 'Julius C\xc3\xa9sure',
    4231: 'Steffi Nalise',
    4232: 'Marie Toivite',
    4233: 'Charlie Lacarpe',
    4234: 'Guy Tare',
    4235: 'Larry le p\xc3\xaacheur',
    4301: 'Yuki',
    4302: 'Anna',
    4303: 'L\xc3\xa9o',
    4304: lHQOfficerM,
    4305: lHQOfficerF,
    4306: lHQOfficerF,
    4307: lHQOfficerF,
    4308: 'Tabatha',
    4309: 'M\xc3\xa9m\xc3\xa9 Chignon',
    4310: 'Marthe Ingale',
    4311: 'Charlie Mande',
    4312: 'Ma Sage',
    4313: 'Muget Muet',
    4314: 'Dino Dodo',
    4315: 'Karen Rouages',
    4316: 'Tim Tango',
    4317: 'Sue Bitto',
    4318: 'Bob Marlin',
    4319: 'K. Zou',
    4320: 'Camille Cloda',
    4321: 'Luky Luth',
    4322: 'Henry Thme',
    4323: 'Hanna Purna',
    4324: 'Ellie',
    4325: 'Braque Labanque',
    4326: 'Jonathan Plurien',
    4327: 'Flim Flam',
    4328: 'Wagner',
    4329: 'Tyler Prompteur',
    4330: 'Quentin',
    4331: 'M. Costello',
    4332: 'Ziggy',
    4333: 'Harry',
    4334: 'Freddie Fastoche',
    4335: 'Serge le p\xc3\xaacheur',
    5001: lHQOfficerM,
    5002: lHQOfficerM,
    5003: lHQOfficerF,
    5004: lHQOfficerF,
    5005: 'Prune - Vendeuse',
    5006: 'Rose - Vendeuse',
    5007: 'Bonnie Menteuse',
    5008: "Vendeur de l'animalerie",
    5009: 'Mme Flore Halie',
    5010: 'M. Tom Hatte',
    5011: 'M. Ray Glisse',
    5101: 'Eug\xc3\xa8ne',
    5102: 'Susan',
    5103: 'Piaf',
    5104: 'Parpaillon',
    5105: 'Jack',
    5106: 'Bjorn le Barbier',
    5107: 'Felipe le Postier',
    5108: "Janette l'Aubergiste",
    5109: lHQOfficerM,
    5110: lHQOfficerM,
    5111: lHQOfficerF,
    5112: lHQOfficerF,
    5113: 'Dr Lacouenne',
    5114: 'Affaiblissement',
    5115: 'Ros\xc3\xa9e Dumatin',
    5116: 'R. Noncule',
    5117: 'P\xc3\xa9tale',
    5118: 'Victor Nemuse',
    5119: 'Barry Dicule',
    5120: 'La taupe',
    5121: 'Paula Ro\xc3\xafd',
    5122: 'A. Masse',
    5123: 'Diane Avecnouscesoir',
    5124: 'Chen Av\xc3\xa9lo',
    5125: 'A. Sperge',
    5126: 'Madame M\xc3\xa8re',
    5127: 'Polly Poll\xc3\xa8ne',
    5128: 'Salma Range',
    5129: 'Sally la p\xc3\xaacheuse',
    5201: 'Jacquot',
    5202: 'Cynthia',
    5203: 'Citronelle',
    5204: 'Bert',
    5205: 'Omar Souin',
    5206: 'Ray Zainblanc',
    5207: 'Sophie Stiqu\xc3\xa9e',
    5208: 'Samantha Pir',
    5209: lHQOfficerM,
    5210: lHQOfficerM,
    5211: lHQOfficerF,
    5212: lHQOfficerF,
    5213: 'Gros Balourd',
    5214: 'Sam Gratte',
    5215: 'Henry Chisson',
    5216: 'Jim Lassenteur',
    5217: 'Walter Ego',
    5218: 'Rocky Groseille',
    5219: 'Mo Viette',
    5220: 'Adam Telle',
    5221: 'Flamant rose',
    5222: 'P\xc3\xa9tronille Hiliste',
    5223: 'Marc Assin',
    5224: 'Oncle Balourd',
    5225: 'Pamela Asaplace',
    5226: 'Pierre Mousse',
    5227: 'B. Gonia',
    5228: 'Avi Dit\xc3\xa9',
    5229: 'Lili la p\xc3\xaacheuse',
    5301: lHQOfficerM,
    5302: lHQOfficerM,
    5303: lHQOfficerM,
    5304: lHQOfficerM,
    5305: 'Crystelle',
    5306: 'S. Cargot',
    5307: 'Cyril Semarre',
    5308: 'Nell Ronchon',
    5309: 'Romaine',
    5310: 'Thimoth\xc3\xa9',
    5311: 'Jonas Ticot',
    5312: 'Eug\xc3\xa8ne',
    5313: "Zucchini l'entra\xc3\xaeneur",
    5314: 'Merlin Sect',
    5315: 'Oncle Boueux',
    5316: 'Oncle Patapouf',
    5317: 'Lima, d\xc3\xa9tective',
    5318: 'C\xc3\xa9sar',
    5319: 'Rose',
    5320: 'J. Boul\xc3\xa9e',
    5321: 'Professeur Ch\xc3\xa8vrefeuille',
    5322: 'Rose la p\xc3\xaacheuse',
    8001: 'Benjamin Salor',
    8002: 'Yvon Affond-Lacaisse',
    8003: 'Emma Nicourt',
    8004: 'Phil Assent',
    9001: 'M\xc3\xa9lusine Enfaillite',
    9002: 'Tom Pouce',
    9003: 'Denis Doiseau',
    9004: lHQOfficerF,
    9005: lHQOfficerF,
    9006: lHQOfficerM,
    9007: lHQOfficerM,
    9008: 'Jill - Vendeuse',
    9009: 'Phil - Vendeur',
    9010: 'U. Zure',
    9011: "Vendeur de l'animalerie",
    9012: 'Melle Isabelle Bulle',
    9013: 'Mme Doroth\xc3\xa9e Dor',
    9014: 'M. Pierre Pionce',
    9101: 'Ed',
    9102: 'Big Mama',
    9103: 'P. J.',
    9104: 'Fay Debeauxr\xc3\xaaves',
    9105: 'Professeur Baillebeaucoup',
    9106: 'Max',
    9107: 'C\xc3\xa2line',
    9108: 'Matt Heula',
    9109: 'Daphn\xc3\xa9 Puis\xc3\xa9',
    9110: 'Kathy Mini',
    9111: 'Ali Mentation',
    9112: 'Lou Laberceuse',
    9113: 'Jacques Horloge',
    9114: 'Emma Scara',
    9115: 'B\xc3\xa9b\xc3\xa9 MacDougal',
    9116: 'Celui qui danse avec les moutons',
    9117: 'Sam Suffit',
    9118: 'Stella Lune',
    9119: 'Rocco',
    9120: 'Aron Flebeaucoup',
    9121: 'Serena D\xc3\xa0lanuitomb\xc3\xa9e',
    9122: 'Serge Souslesyeux',
    9123: 'Teddy Blaireau',
    9124: 'Nina Lamparo',
    9125: 'Dr Chassieux',
    9126: 'Th\xc3\xa9r\xc3\xa8se Eveill\xc3\xa9',
    9127: 'Tabby Tude',
    9128: 'Am\xc3\xa9d\xc3\xa9 Brouilletoitoutseul',
    9129: 'Am\xc3\xa9lie Decamp',
    9130: 'Paul Potdechambre',
    9131: 'Susan Sieste',
    9132: lHQOfficerF,
    9133: lHQOfficerF,
    9134: lHQOfficerF,
    9135: lHQOfficerF,
    9136: 'Titine la p\xc3\xaacheuse',
    9201: 'Nesdor',
    9202: 'Orville',
    9203: 'Plume',
    9204: 'Claire de Moune',
    9205: 'Olivier Daure',
    9206: 'Ph\xc3\xa8dre Don',
    9207: 'Sacha Lumea',
    9208: 'Dave Bigleau',
    9209: 'Dr Drin',
    9210: 'Mike Mac',
    9211: 'Aurore',
    9212: 'Ph\xc5\x93be Lancre',
    9213: 'Fortun\xc3\xa9 Dargent',
    9214: 'Dr Ouffe',
    9215: 'Honor\xc3\xa9',
    9216: 'Tartine',
    9217: 'Linda Kapok',
    9218: 'Rita Thasse',
    9219: 'La comtesse',
    9220: 'Matt Thuvu',
    9221: 'P\xc3\xa8re San',
    9222: 'Ron Chonneau',
    9223: 'Fay Dodeau',
    9224: 'Sandie Marchand',
    9225: '\xc3\x89lodie Dont',
    9226: 'Laurent Lauronpat',
    9227: '\xc3\x89douard Sagrate',
    9228: 'Michu Chotte',
    9229: 'Eva Sandor-Mir',
    9230: 'Pierrot',
    9231: 'L\xc3\xa9o Galleau',
    9232: 'Ros\xc3\xa9e de Lune',
    9233: lHQOfficerM,
    9234: lHQOfficerM,
    9235: lHQOfficerM,
    9236: lHQOfficerM,
    9237: 'S. Andr\xc3\xa9'}
zone2TitleDict = {
    2513: ('Mairie de Toontown', ''),
    2514: ('Banque de Toontown', ''),
    2516: ('Ecole de Toontown', ''),
    2518: ('Biblioth\xc3\xa8que de Toontown', ''),
    2519: ('Boutique \xc3\xa0 gags', ''),
    2520: ('Quartier G\xc3\xa9n\xc3\xa9ral des Toons', ''),
    2521: ('Boutique de pr\xc3\xaat-\xc3\xa0-porter', ''),
    2522: ('ANIMALERIE', ''),
    2601: ('Tout-sourire - R\xc3\xa9parations dentaires', ''),
    2602: ('', ''),
    2603: ('Mineurs Pince-sans-rire', ''),
    2604: ('Qui vivra, verrat', ''),
    2605: ('Usine \xc3\xa0 pancartes de Toontown', ''),
    2606: ('', ''),
    2607: ('Haricots sauteurs', ''),
    2610: ('Dr. Tom Lepitre', ''),
    2611: ('', ''),
    2616: ('Barbefolle - D\xc3\xa9guisements', ''),
    2617: ('Cascades Comiques', ''),
    2618: ('Nouba & Co', ''),
    2621: ('Avions en papier', ''),
    2624: ('Aux joyeux hooligans', ''),
    2625: ('La maison du p\xc3\xa2t\xc3\xa9 rat\xc3\xa9', ''),
    2626: ('Chez Jesse - R\xc3\xa9paration de blagues', ''),
    2629: ('Le coin du rire', ''),
    2632: ("L'\xc3\xa9cole des clowns", ''),
    2633: ('Th\xc3\xa9-hier - Salon de th\xc3\xa9', ''),
    2638: ('Th\xc3\xa9\xc3\xa2tre de Toontown', ''),
    2639: ('Monnaie de singe', ''),
    2643: ('Bouteilles en bo\xc3\xaete', ''),
    2644: ('Farces farcies', ''),
    2649: ('Magasin de jeux', ''),
    2652: ('', ''),
    2653: ('', ''),
    2654: ('Le\xc3\xa7ons de rire', ''),
    2655: ("Dr\xc3\xb4le d'argent - Caisse d'\xc3\xa9pargne", ''),
    2656: ("Voitures de clown d'occasion", ''),
    2657: ('Pirouettes de Pierrette', ''),
    2659: ("L'univers des vibrateurs", ''),
    2660: ('Machines \xc3\xa0 chatouilles', ''),
    2661: ('Daffy Taffy', ''),
    2662: ('Dr E. Phorique', ''),
    2663: ('Th\xc3\xa9\xc3\xa2tre de Toontown', ''),
    2664: ('Les mimes marrants', ''),
    2665: ('Le Man\xc3\xa8ge - Agence de voyages', ''),
    2666: ('Bouteilles de gaz hilarant', ''),
    2667: ('Au bon temps', ''),
    2669: ('Chez Gaston - ballons pas folichons', ''),
    2670: ('Fourchettes \xc3\xa0 soupe', ''),
    2671: ('Quartier G\xc3\xa9n\xc3\xa9ral des Toons', ''),
    2701: ('', ''),
    2704: ('Th\xc3\xa9\xc3\xa2tre de Toontown', ''),
    2705: ('Tony Truant - Bruits en tout genre', ''),
    2708: ('Colle bleue', ''),
    2711: ('Bureau de poste de Toontown', ''),
    2712: ('Caf\xc3\xa9 des gloussements', ''),
    2713: ('Caf\xc3\xa9 du rire', ''),
    2714: ('Th\xc3\xa9\xc3\xa2tre de Toontown', ''),
    2716: ('Dr \xc3\x83le de soupe', ''),
    2717: ('Bo\xc3\xaetes en bouteille', ''),
    2720: ('Plaies et Bosses - R\xc3\xa9parations de voitures', ''),
    2725: ('', ''),
    2727: ('Bouteilles et bo\xc3\xaetes Selter', ''),
    2728: ('Cr\xc3\xa8me de jour \xc3\xa9vanescente', ''),
    2729: ('Ornithorynques 14 carats', ''),
    2730: ('La gazette du rire', ''),
    2731: ('', ''),
    2732: ('Spaghettis et barbituriques', ''),
    2733: ('Cerf-volants en fonte', ''),
    2734: ('Tasses et soucoupes volantes', ''),
    2735: ('Le P\xc3\xa9tard mouill\xc3\xa9', ''),
    2739: ('R\xc3\xa9paration de fous rires', ''),
    2740: ("P\xc3\xa9tards d'occasion", ''),
    2741: ('', ''),
    2742: ('Quartier G\xc3\xa9n\xc3\xa9ral des Toons', ''),
    2743: ('', ''),
    2744: ('', ''),
    2747: ('Encre visible', ''),
    2748: ('Rions un peu', ''),
    2801: ('Coussins sonores', ''),
    2802: ('Boulets de d\xc3\xa9molition gonflables', ''),
    2803: ('Th\xc3\xa9\xc3\xa2tre de Toontown', ''),
    2804: ('Dr. Faismarcher, chiropracteur', ''),
    2805: ('', ''),
    2809: ('Salle de gym Le Poids lent', ''),
    2814: ('Th\xc3\xa9\xc3\xa2tre de Toontown', ''),
    2818: ('Au p\xc3\xa2t\xc3\xa9 volant', ''),
    2821: ('', ''),
    2822: ('Sandwichs au poulet synth\xc3\xa9tique', ''),
    2823: ('Glaces hilarantes', ''),
    2824: ('Cin\xc3\xa9ma des blagues', ''),
    2829: ('Balivernes', ''),
    2830: ("Les piques d'Annick", ''),
    2831: ('La maison du rire du professeur Tortillard', ''),
    2832: ('Quartier G\xc3\xa9n\xc3\xa9ral des Toons', ''),
    2833: ('', ''),
    2834: ('Salle des urgences des morts de rire', ''),
    2836: ('', ''),
    2837: ('Hardi - S\xc3\xa9minaires', ''),
    2839: ('A la nouille am\xc3\xa8re', ''),
    2841: ('', ''),
    1506: ('Boutique \xc3\xa0 gags', ''),
    1507: ('Quartier G\xc3\xa9n\xc3\xa9ral des Toons', ''),
    1508: ('Boutique de pr\xc3\xaat-\xc3\xa0-porter', ''),
    1510: ('ANIMALERIE', ''),
    1602: ("Gilets de sauvetage d'occasion", ''),
    1604: ('Costumes de bain - Nettoyage \xc3\xa0 sec', ''),
    1606: ("Crochet - R\xc3\xa9paration d'horloges", ''),
    1608: ('Le Lof', ''),
    1609: ("A l'app\xc3\xa2t rance", ''),
    1612: ('Banque Sixsous', ''),
    1613: ("La Pieuvre, cabinet d'avocats", ''),
    1614: ('Toutes voiles devant - Boutique', ''),
    1615: ("Yatch qu'\xc3\xa0 demander!", ''),
    1616: ('Barbe Noire - Salon de beaut\xc3\xa9', ''),
    1617: ('La mer \xc3\xa0 voir - Opticien', ''),
    1619: ("L'\xc3\xa9corcaire - Chirurgie arboricole", ''),
    1620: ('Babord-tribord', ''),
    1621: ('Salle de gym La poupe', ''),
    1622: ('Gymnote - Electricit\xc3\xa9 g\xc3\xa9n\xc3\xa9rale', ''),
    1624: ('R\xc3\xa9paration de couteaux et de peignes', ''),
    1626: ('La perche rare - Tenues de soir\xc3\xa9e', ''),
    1627: ('La cabane de Sam Suffit', ''),
    1628: ('Accordeur de thons', ''),
    1629: ('Quartier G\xc3\xa9n\xc3\xa9ral des Toons', ''),
    1701: ("Ecole maternelle des p'tits loups", ''),
    1703: ('Bar Accuda - Restaurant chinois', ''),
    1705: ('Voiles \xc3\xa0 vendre', ''),
    1706: ('La m\xc3\xa9duse m\xc3\xa9dus\xc3\xa9e', ''),
    1707: ("C'est assez - Boutique de cadeaux", ''),
    1709: ('G\xc3\xa9l\xc3\xa9e de m\xc3\xa9duse', ''),
    1710: ('La belle bernache', ''),
    1711: ('Restaurant de la pleine mer', ''),
    1712: ('Salle de gymnote', ''),
    1713: ('Chez Art - Cartes en tous genres', ''),
    1714: ('Auberge du moulinet', ''),
    1716: ('Maillots de bains pour sir\xc3\xa8nes', ''),
    1717: ('Mi pacifique, mi raisin', ''),
    1718: ('Soci\xc3\xa9t\xc3\xa9 de taxi le Naufrage', ''),
    1719: ("Soci\xc3\xa9t\xc3\xa9 Je m'cache \xc3\xa0 l'eau", ''),
    1720: ('Au requin malin', ''),
    1721: ('Tout pour la mer', ''),
    1723: ('Au royaume des algues', ''),
    1724: ('Au m\xc3\xa9rou amoureux', ''),
    1725: ("J'en pince pour toi - Crabes frais", ''),
    1726: ('Bi\xc3\xa8re \xc3\xa0 flots', ''),
    1727: ('Je rame pour vous', ''),
    1728: ('Limules porte-bonheur', ''),
    1729: ('Quartier G\xc3\xa9n\xc3\xa9ral des Toons', ''),
    1802: ('Les petits p\xc3\xa9ch\xc3\xa9s', ''),
    1804: ('Salle de gym Les mollusques', ''),
    1805: ('Un petit ver pour le d\xc3\xa9jeuner', ''),
    1806: ('Toucoule - Chapelier', ''),
    1807: ('Co\xc3\xbbte que soute', ''),
    1808: ('App\xc3\xa2t si vite!', ''),
    1809: ('Seaux rouill\xc3\xa9s', ''),
    1810: ("L'ancre noire", ''),
    1811: ('M\xc3\xa9rou tu vas chercher tout \xc3\xa7a?', ''),
    1813: ('A m\xc3\xa2ts couverts, conseiller', ''),
    1814: ('Le Ho Hisse', ''),
    1815: ('Quoi de neuf dockteur ?', ''),
    1818: ('Caf\xc3\xa9 des sept mers', ''),
    1819: ('Au d\xc3\xaener des dockers', ''),
    1820: ("L'hame\xc3\xa7on gob\xc3\xa9 - Farces et attrapes", ''),
    1821: ('Chez Neptoon', ''),
    1823: ('A la pomme de m\xc3\xa2t', ''),
    1824: ('Au chien pas gai', ''),
    1825: ('Le hareng sort! March\xc3\xa9 aux poissons', ''),
    1826: ('Le placard de G\xc3\xa9rard', ''),
    1828: ("Palais du lest d'Ernest", ''),
    1829: ("Merlan l'enchanteur", ''),
    1830: ('O sole et mio - Objets trouv\xc3\xa9s', ''),
    1831: ('Une perle \xc3\xa0 domicile', ''),
    1832: ('Sup\xc3\xa9rette La Go\xc3\xa9lette', ''),
    1833: ("Costumes pour gaillards d'avant", ''),
    1834: ('Tranchement ridicule!', ''),
    1835: ('Quartier G\xc3\xa9n\xc3\xa9ral des Toons', ''),
    4503: ('Boutique \xc3\xa0 gags', ''),
    4504: ('Quartier G\xc3\xa9n\xc3\xa9ral des Toons', ''),
    4506: ('Boutique de pr\xc3\xaat-\xc3\xa0-porter', ''),
    4508: ('ANIMALERIE', ''),
    4603: ('Tom-Tom - Tambours', ''),
    4604: ('A quatre temps', ''),
    4605: ("Fifi - Violons d'Ingres", ''),
    4606: ('La case des castagnettes', ''),
    4607: ('V\xc3\xaatements Toon branch\xc3\xa9s', ''),
    4609: ('Dot, Raie, Mie - Pianos', ''),
    4610: ('Attention refrain!', ''),
    4611: ("Diapasons \xc3\xa0 l'unisson", ''),
    4612: ('Dr. Tefaispasdebile - Dentiste', ''),
    4614: ('On rase gratis pour une chanson', ''),
    4615: ('Pizz\xc3\xa9ria chez Piccolo', ''),
    4617: ('La mandoline joyeuse', ''),
    4618: ('Salles des c\xc3\xa9sures', ''),
    4619: ('En avant la musique!', ''),
    4622: ('Oreillers \xc3\xa0 mentonni\xc3\xa8re', ''),
    4623: ('B\xc3\xa9mols \xc3\xa0 la di\xc3\xa8se', ''),
    4625: ('Tuba de dentifrice', ''),
    4626: ('Notations', ''),
    4628: ('Assurance accidentelle', ''),
    4629: ('Riff - Assiettes en papier', ''),
    4630: ('La musique est notre force', ''),
    4631: ('Canto de vous conna\xc3\xaetre!', ''),
    4632: ('Boutique de la danse des heures', ''),
    4635: ('Le quotidien des cantatrices', ''),
    4637: ('Pour la bonne mesure', ''),
    4638: ('Boutique Hard Rock', ''),
    4639: ('Les quatre saisons - Antiquit\xc3\xa9s', ''),
    4641: ("L'actualit\xc3\xa9 du y\xc3\xa9y\xc3\xa9", ''),
    4642: ('D. Tach\xc3\xa9 - Nettoyage \xc3\xa0 sec', ''),
    4645: ('Club 88', ''),
    4646: ('', ''),
    4648: ('Le Toon siffleur - D\xc3\xa9m\xc3\xa9nageurs', ''),
    4649: ('Quartier G\xc3\xa9n\xc3\xa9ral des Toons', ''),
    4652: ('Boutique des doubles-croches', ''),
    4653: ('', ''),
    4654: ('Haut perch\xc3\xa9 - Toitures', ''),
    4655: ('La cl\xc3\xa9 de sol - Ecole de cuisine', ''),
    4656: ('', ''),
    4657: ('Quatuor du barbier', ''),
    4658: ('Pianos en chute libre', ''),
    4659: ('Quartier G\xc3\xa9n\xc3\xa9ral des Toons', ''),
    4701: ("L'eau de rose - Ecole de valse", ''),
    4702: (' Timbre de bois - Fournitures pour b\xc3\xbbcherons', ''),
    4703: ('Gros Bizet \xc3\xa0 tous!', ''),
    4704: ('Tina - Concerts de concertina', ''),
    4705: ('Il est d\xc3\xa9j\xc3\xa0 cithare ?', ''),
    4707: ("Studio d'effets sonores Doppler", ''),
    4709: ("Pirouettes - Magasin d'alpinisme", ''),
    4710: ('Polka tu routes si vite ? Auto-\xc3\xa9cole', ''),
    4712: ('Mets un b\xc3\xa9mol! R\xc3\xa9paration de pneus', ''),
    4713: ('Dos di\xc3\xa8se - V\xc3\xaatements de luxe pour hommes', ''),
    4716: ('Harmonicas \xc3\xa0 quatre voix', ''),
    4717: ('Sonate pas ta faute! Assurance automobile', ''),
    4718: ('Chopins de bi\xc3\xa8re et autres ustensiles de cuisine', ''),
    4719: ('Camping-cars Madrigal', ''),
    4720: ('Le bon Toon', ''),
    4722: ('Doublures pour ouvertures', ''),
    4723: ('Bach \xc3\xa0 toi! Jeux et balan\xc3\xa7oires', ''),
    4724: ('(Cale)sons blancs pour filles et gar\xc3\xa7ons', ''),
    4725: ('Le barbier baryton', ''),
    4727: ('Cordes vocales tress\xc3\xa9es', ''),
    4728: ('Chante en sourdine!', ''),
    4729: ("Librairie J'aime lyre", ''),
    4730: ('Lettre \xc3\xa0 un pou', ''),
    4731: ('Des Toons de bon ton', ''),
    4732: ('Etude brute ? Troupe de th\xc3\xa9\xc3\xa2tre', ''),
    4733: ('', ''),
    4734: ('', ''),
    4735: ('Soufflet pour accord\xc3\xa9ons', ''),
    4736: ('Hyminent - Pr\xc3\xa9paratifs de mariage', ''),
    4737: ('Harpe H\xc3\xb4nneur', ''),
    4738: ('M\xc3\xa9canique cantique - Cadeaux', ''),
    4739: ('Quartier G\xc3\xa9n\xc3\xa9ral des Toons', ''),
    4801: ("Cr\xc3\xaap'chignon", ''),
    4803: ('Quelle Mezzo! Service de domestiques', ''),
    4804: ('Ecole myxolidienne pour serveurs de barres', ''),
    4807: ('Massage des Brahms et des jambes', ''),
    4809: ("C'est une cata-strophe!", ''),
    4812: ('', ''),
    4817: ("Magasin d'animaux ternaires", ''),
    4819: ('Chez Yuki - Uk\xc3\xa9l\xc3\xa9l\xc3\xa9s', ''),
    4820: ('', ''),
    4821: ('Chez Anna - Croisi\xc3\xa8res', ''),
    4827: ('Montres Lamesure', ''),
    4828: ('Ravel - R\xc3\xa9veils et horloges', ''),
    4829: ('Chez Pachelbel - Obus pour canons et fugues', ''),
    4835: ('Ursatz pour Kool Katz', ''),
    4836: ('Reggae royal', ''),
    4838: ('Ecole de kazoologie', ''),
    4840: ('Coda Pop - Boissons musicales', ''),
    4841: ('Lyre et Lyre', ''),
    4842: ('Soci\xc3\xa9t\xc3\xa9 Lasyncope', ''),
    4843: ('', ''),
    4844: ('Moto - deux roues', ''),
    4845: ("Les \xc3\xa9l\xc3\xa9gies \xc3\xa9l\xc3\xa9gantes d'Ellie", ''),
    4848: ("De haute luth - Caisse d'\xc3\xa9pargne", ''),
    4849: ('', ''),
    4850: ("L'accord emprunt\xc3\xa9 - Pr\xc3\xaateur sur gages", ''),
    4852: ('Flasques fleuries pour fl\xc3\xbbtes', ''),
    4853: ('Chez L\xc3\xa9o - Garde-feu', ''),
    4854: ('Chez Wagner - Vid\xc3\xa9os de violons voil\xc3\xa9s', ''),
    4855: ('R\xc3\xa9seau de radeau-diffusion', ''),
    4856: ('', ''),
    4862: ('Les quadrilles quintessencielles de Quentin', ''),
    4867: ('M. Costello - Kazoos \xc3\xa0 gogo', ''),
    4868: ('', ''),
    4870: ('Chez Ziggy - Zoo et Zigeunermusik', ''),
    4871: ('Chez Harry - Harmonies harmonieuses', ''),
    4872: ('Freddie Fastoche - Touches de piano', ''),
    4873: ('Quartier G\xc3\xa9n\xc3\xa9ral des Toons', ''),
    5501: ('Boutique \xc3\xa0 gags', ''),
    5502: ('Quartier G\xc3\xa9n\xc3\xa9ral des Toons', ''),
    5503: ('Boutique de pr\xc3\xaat-\xc3\xa0-porter', ''),
    5505: ('ANIMALERIE', ''),
    5601: ("L'\xc5\x93il de bouillon - Optom\xc3\xa9trie", ''),
    5602: ('Eug\xc3\xa8ne Coulissant - Cravates', ''),
    5603: ('Arr\xc3\xaate tes salades!', ''),
    5604: ('Gai, gai, marions-les!', ''),
    5605: ('Sols et meubles', ''),
    5606: ('P\xc3\xa9tales', ''),
    5607: ('Bureau de composte', ''),
    5608: ('Pop corn y\xc3\xa9y\xc3\xa9', ''),
    5609: ('La baie au tr\xc3\xa9sor', ''),
    5610: ("L'\xc5\x93il au beurre noir - Cours de boxe", ''),
    5611: ('Les gags de la Taupe', ''),
    5613: ('La meule \xc3\xa0 z\xc3\xa9ro - Barbier', ''),
    5615: ('Chez Piaf - Graines pour oiseaux', ''),
    5616: ('Auberge de la goutte', ''),
    5617: ('Chez Parpaillon - Papillons', ''),
    5618: ('Deux pois deux mesures', ''),
    5619: ('Chez Jack - Haricots g\xc3\xa9ants', ''),
    5620: ('Auberge du rateau', ''),
    5621: ('La critique du Raisin pur', ''),
    5622: ('La petite reine - claude - Bicyclettes', ''),
    5623: ('Bains moussants pour oiseaux', ''),
    5624: ('Ecoute ta m\xc3\xa8re', ''),
    5625: ('Dur de la feuille', ''),
    5626: ("Travaux d'aiguille (de pin)", ''),
    5627: ('Quartier G\xc3\xa9n\xc3\xa9ral des Toons', ''),
    5701: ('Le bambou du tunnel', ''),
    5702: ('Les rateaux de Jacquot', ''),
    5703: ('Cynthia - Magasin de photosynth\xc3\xa8ses', ''),
    5704: ("Citronelle Citron - Voitures d'occasion", ''),
    5705: ('Meubles en herbe \xc3\xa0 puce', ''),
    5706: (' 14 carottes - Bijoutiers', ''),
    5707: ('Fruit musical', ''),
    5708: ('Sans soucis - Agence de voyages', ''),
    5709: ('Astroturf - Tondeuses', ''),
    5710: ('Gym des narcisses', ''),
    5711: ('Bonneterie de jardin', ''),
    5712: ('Statues squottes', ''),
    5713: ('Buis clos', ''),
    5714: ("Bouteilles d'eau de roche", ''),
    5715: ('La Meule nouvelle', ''),
    5716: ("Qui s'y frotte s'y pique - Pr\xc3\xaateur sur gages", ''),
    5717: ('La fleur qui mouille', ''),
    5718: ('Le ch\xc3\xa8vre-feuille - Animalerie', ''),
    5719: ("Sauge d'une nuit d'\xc3\xa9t\xc3\xa9 - D\xc3\xa9tective priv\xc3\xa9", ''),
    5720: ('La feuille de vigne - Pr\xc3\xaat-\xc3\xa0-porter masculin', ''),
    5721: ('Routabaga 66 - Restaurant', ''),
    5725: ("Boutique du grain d'orge", ''),
    5726: ('Bert', ''),
    5727: ("Le trou sans fond - Caisse d'\xc3\xa9pargne", ''),
    5728: ('Quartier G\xc3\xa9n\xc3\xa9ral des Toons', ''),
    5802: ('Quartier G\xc3\xa9n\xc3\xa9ral des Toons', ''),
    5804: ('La vase de Soisson', ''),
    5805: ('Le cerveau lent', ''),
    5809: ("Dr\xc3\xb4le d'oiseau - Ecole de clowns", ''),
    5810: ('Ca ne rom \xc3\xa0 rain!', ''),
    5811: ('Auberge Inn', ''),
    5815: ('Des racines & des herbes', ''),
    5817: ('Pommes et oranges', ''),
    5819: ('Pantalons vert citron', ''),
    5821: ('Centre de squash', ''),
    5826: ("Mat\xc3\xa9riel d'\xc3\xa9levage de fourmis", ''),
    5827: ('Terre bon march\xc3\xa9', ''),
    5828: ('Meubles Molasson', ''),
    5830: ('Vide ton sac (de patates)', ''),
    5833: ('Bar \xc3\xa0 salades', ''),
    5835: ("S\xc3\xa9jour en pots chez l'habitant", ''),
    5836: ('Salles de bain J. Boul\xc3\xa9e', ''),
    5837: ("L'\xc3\xa9cole de la vigne", ''),
    9501: ('Biblioth\xc3\xa8que des berceuses', ''),
    9503: ('Bar du roupillon', ''),
    9504: ('Boutique \xc3\xa0 gags', ''),
    9505: ('Quartier G\xc3\xa9n\xc3\xa9ral des Toons', ''),
    9506: ('Boutique de pr\xc3\xaat-\xc3\xa0-porter', ''),
    9508: ('ANIMALERIE', ''),
    9601: ('Auberge des c\xc3\xa2lins', ''),
    9602: ('Sommes au rabais', ''),
    9604: ('Chez Ed - Edredons redondants', ''),
    9605: ('Confection de bonnets de nuit', ''),
    9607: ('Big Mama - Pyjamas des Bahamas', ''),
    9608: ('Quand le chat dort, les souris dansent', ''),
    9609: ('Roupillon pour trois ronds', ''),
    9613: ('Th\xc3\xa9\xc3\xa2tre du pays des r\xc3\xaaves', ''),
    9616: ('La veilleuse - Electricit\xc3\xa9 g\xc3\xa9n\xc3\xa9rale', ''),
    9617: ("L'enfant do - Petites musiques de nuit", ''),
    9619: ('Relax Max', ''),
    9620: ('PJ - Service de taxi', ''),
    9622: ('Horloges du sommeil', ''),
    9625: ('Histoire en boucle - Salon de beaut\xc3\xa9', ''),
    9626: ('Histoiries Dodo', ''),
    9627: ('Le tipi endormi', ''),
    9628: ('Sam Suffit - Calendriers', ''),
    9629: ("\xc3\x80 l'\xc3\xa9dredon d'argent", ''),
    9630: ('Marchand de sable', ''),
    9631: ("Temps d'arr\xc3\xaat - Horloger", ''),
    9633: ('Th\xc3\xa9\xc3\xa2tre du pays des r\xc3\xa9ves', ''),
    9634: ('Je ronfle, donc je suis', ''),
    9636: ('Assurance pour insomniaques', ''),
    9639: ("Maison de l'hibernation", ''),
    9640: ('Nous meublons vos r\xc3\xaaves', ''),
    9642: ('A la sciure de mon front', ''),
    9643: ('Les yeux clos - Optom\xc3\xa9trie', ''),
    9644: ("Combats d'oreillers nocturnes", ''),
    9645: ('Auberge Viensmeborder', ''),
    9647: ('Fais ton lit! Magasin de bricolage', ''),
    9649: ('Bonnet blanc et blanc bonnet', ''),
    9650: ('R\xc3\xa9parateur de soupirs', ''),
    9651: ('La vie est un ronflement tranquille', ''),
    9652: ('Quartier G\xc3\xa9n\xc3\xa9ral des Toons', ''),
    9703: ('Agence de voyages Vol de Nuit', ''),
    9704: ('Animalerie du Hibou', ''),
    9705: ("Garage de la Panne d'Oreiller", ''),
    9706: ('Cabinet dentaire La Petite Souris', ''),
    9707: ('Jardinerie de La B\xc3\xa2illerie', ''),
    9708: ('Le Lys Douillet - Fleuriste', ''),
    9709: ('Au Sommeil de Plomb - Plombier', ''),
    9710: ("Rev'optique", ''),
    9711: ('Service de r\xc3\xa9veil par t\xc3\xa9l\xc3\xa9phone', ''),
    9712: ('Nous comptons les moutons pour vous!', ''),
    9713: ('Roupille & Pionce, Avocats', ''),
    9714: ('Croisi\xc3\xa8re de r\xc3\xaave - Accastillage', ''),
    9715: ("Banque du Doudou d'Or", ''),
    9716: ('Le Lit en Cath\xc3\xa9drale, farces at attrapes', ''),
    9717: ('P\xc3\xa2tisserie du Croissant de Lune', ''),
    9718: ('Sandwiches du Marchand de Sable', ''),
    9719: ("Tout pour l'Oreiller", ''),
    9720: ("Cours d'\xc3\xa9locution pour somnambules", ''),
    9721: ('Tapis du Loir', ''),
    9722: ('Les Yeux Ferm\xc3\xa9s - Spectacles en tous genres', ''),
    9725: ('Pyjamas du Chat', ''),
    9727: ('Ronfl\xc3\xa9, perdu', ''),
    9736: ("Agence pour l'emploi M\xc3\xa9tiers de R\xc3\xaave", ''),
    9737: ('Au Tutu qui dort - \xc3\x89cole de danse', ''),
    9738: ('Maison Ronflon', ''),
    9740: ("Le Sabre Nocturne - Salle d'armes", ''),
    9741: ("\xc3\x80 l'Acarien Vorace - Destructeur de nuisibles", ''),
    9744: ('Cr\xc3\xa8me antirides Hicule', ''),
    9752: ('Carburants Soporifiques', ''),
    9753: ('Cr\xc3\xa8mes de Luna Glac\xc3\xa9es', ''),
    9754: ('Randonn\xc3\xa9es \xc3\xa9questres - Poney de Nuit', ''),
    9755: ('Cin\xc3\xa9ma La Ronflette', ''),
    9756: ('', ''),
    9759: ('Institut de beaut\xc3\xa9 du Bois - Dormant', ''),
    3507: ('Boutique \xc3\xa0 gags', ''),
    3508: ('Quartier g\xc3\xa9n\xc3\xa9ral des Toons', ''),
    3509: ('Boutique de pr\xc3\xaat-\xc3\xa0-porter', ''),
    3511: ('ANIMALERIE', ''),
    3601: ('Aurore bor\xc3\xa9ale - Electricit\xc3\xa9 g\xc3\xa9n\xc3\xa9rale', ''),
    3602: ('Bonnets de p\xc3\xa2ques', ''),
    3605: ('', ''),
    3607: ('Le vieillard du blizzard', ''),
    3608: ('A en perdre la boule (de neige)!', ''),
    3610: ('Sup\xc3\xa9rette Les Mirettes', ''),
    3611: ('M. Lapin - Chasse-neige', ''),
    3612: ("Conception d'igloos", ''),
    3613: ('Glaces et miroirs', ''),
    3614: ("Fabriquant de flocons d'avoine", ''),
    3615: ('Omelettes norv\xc3\xa9giennes', ''),
    3617: ('Voyages en ballon \xc3\xa0 air froid', ''),
    3618: ('Boule de neige! Gestion de crise', ''),
    3620: ('Atelier de ski', ''),
    3621: ('Glacier La fonte des neiges', ''),
    3622: ('', ''),
    3623: ('Croque-monsieur', ''),
    3624: ('Sandwichs froids', ''),
    3625: ('Tante Ang\xc3\xa8le - Radiateurs', ''),
    3627: ('Chenil St Bernard', ''),
    3629: ('La soupe aux pois - Caf\xc3\xa9', ''),
    3630: ('Agence de voyage Laglisse', ''),
    3634: ('T\xc3\xa9l\xc3\xa9si\xc3\xa8ges rembourr\xc3\xa9s', ''),
    3635: ("Bois de chauffage d'occasion", ''),
    3636: ('Chair de poule bon march\xc3\xa9', ''),
    3637: ('Les patins de Patricia', ''),
    3638: ('H\xc3\xaatre ou ne pas h\xc3\xaatre', ''),
    3641: ('Chez Tanguy - B\xc3\xa2teaux \xc3\xa0 dormir debout', ''),
    3642: ("L'\xc5\x93il du cyclone - Opticien", ''),
    3643: ('Chambre (froide) de danse', ''),
    3644: ('Gla\xc3\xa7ons fondus', ''),
    3647: ('Au pingouin sanguin - Magasin de smokings', ''),
    3648: ('Glace instantan\xc3\xa9e', ''),
    3649: ('Hambrrghers', ''),
    3650: ('Articlit\xc3\xa9s', ''),
    3651: ('Freddy Frigo - Saucisses congel\xc3\xa9es', ''),
    3653: ('Bijoux glac\xc3\xa9s', ''),
    3654: ('Quartier g\xc3\xa9n\xc3\xa9ral des Toons', ''),
    3702: ('Stockage hivernal', ''),
    3703: ('', ''),
    3705: ('Gla\xc3\xa7ons pour deux', ''),
    3706: ('Babas au rhume', ''),
    3707: ('Mon igloo est mon royaume', ''),
    3708: ('Chez Pluto', ''),
    3710: ('Restaurant en chute libre', ''),
    3711: ('', ''),
    3712: ('Au royaume du d\xc3\xa9luge', ''),
    3713: ('Les dents qui claquent - Dentiste polaire', ''),
    3715: ('Les bonnes soupes de Tante Artique', ''),
    3716: ('Salage et poivrage des routes', ''),
    3717: ('Juneau sais pas ce que vous voulez dire', ''),
    3718: ('Inventeur de chambres \xc3\xa0 air', ''),
    3719: ('Gla\xc3\xa7on en cornet', ''),
    3721: ('Aux bonnes affaires glissantes', ''),
    3722: ("Boutique d'apr\xc3\xa8s-ski", ''),
    3723: ('Chez Tremblotte - globes des neiges', ''),
    3724: ('La chronique des rhumeurs', ''),
    3725: ('Alluge-toi un instant', ''),
    3726: ('Couvertures solaires', ''),
    3728: ('Chasse-neige \xc3\xa0 la pelle', ''),
    3729: ('', ''),
    3730: ('Achat et vente de bonhommes de neige', ''),
    3731: ('Chemin\xc3\xa9es portatives', ''),
    3732: ('Au nez gel\xc3\xa9', ''),
    3734: ('Regards glac\xc3\xa9s - Optom\xc3\xa9trie', ''),
    3735: ('Calottes glaciaires', ''),
    3736: ('Cubes de glace bon march\xc3\xa9', ''),
    3737: ('Restaurant de la pente', ''),
    3738: ('Chaud devant!', ''),
    3739: ('Quartier g\xc3\xa9n\xc3\xa9ral des Toons', ''),
    3801: (lToonHQ, ''),
    3806: ('Croisi\xc3\xa8res Tartiflette', ''),
    3807: ("Nuages d'occasion", ''),
    3808: ('G\xc3\xaete Gilet', ''),
    3809: ('Glaces de d\xc3\xa9couverte', ''),
    3810: ('Pelisses Municipales', ''),
    3811: ("L'Ange Neige", ''),
    3812: ('Chaussons pour chatons', ''),
    3813: ('Apr\xc3\xa8s-skis biod\xc3\xa9gradables', ''),
    3814: ('Pailles \xc3\xa0 gla\xc3\xa7ons', ''),
    3815: ('Chalet Frisquet', ''),
    3816: ('Au gui tout neuf', ''),
    3817: ('Club Le Verglas', ''),
    3818: ('La pelle des c\xc3\xaemes', ''),
    3819: ('Ramonage et d\xc3\xa9givrage', ''),
    3820: ('Blanchisserie de neige', ''),
    3821: ("Sports d'hibernation", ''),
    3823: ('Fondation des Pluies', ''),
    3824: ('Froids les marrons!', ''),
    3825: ('Chapeaux tout frais', ''),
    3826: ('Saperlichaussette!', ''),
    3827: ('Couronnes de gui', ''),
    3828: ('Le potager du bonhomme de neige', ''),
    3829: ('Frigo D\xc3\xa9co', ''),
    3830: ('Voyons Voir, d\xc3\xa9givrage de monocles', '')}
ClosetTimeoutMessage = "D\xc3\xa9sol\xc3\xa9, tu n'as plus\n le temps."
ClosetNotOwnerMessage = "Ce n'est pas ton placard, mais tu peux essayer les v\xc3\xaatements."
ClosetPopupOK = lOK
ClosetPopupCancel = lCancel
ClosetDiscardButton = 'Supprimer'
ClosetAreYouSureMessage = 'Tu as supprim\xc3\xa9 des v\xc3\xaatements. Veux-tu vraiment les supprimer?'
ClosetYes = lYes
ClosetNo = lNo
ClosetVerifyDelete = 'Vraiment supprimer %s?'
ClosetShirt = 'cette chemise'
ClosetShorts = 'ce short'
ClosetSkirt = 'cette jupe'
ClosetDeleteShirt = 'Supprimer\nchemise'
ClosetDeleteShorts = 'Supprimer\nshort'
ClosetDeleteSkirt = 'Supprimer\njupe'
EstateOwnerLeftMessage = 'D\xc3\xa9sol\xc3\xa9, le(la) propri\xc3\xa9taire de cette maison est parti(e). Retour au terrain de jeux dans %s secondes'
EstatePopupOK = lOK
EstateTeleportFailed = 'Impossible de retourner \xc3\xa0 la maison. Essaie encore!'
EstateTeleportFailedNotFriends = "D\xc3\xa9sol\xc3\xa9, %s est chez un Toon avec qui tu n'es pas ami(e)."
EstateTargetGameStart = 'Le jeu des cibles tooniques a commenc\xc3\xa9!'
EstateTargetGameInst = 'Plus tu tires dans la cible rouge, et plus tu remportes de tooniques.'
EstateTargetGameEnd = 'le jeu des cibles tooniques est maintenant termin\xc3\xa9...'
EstateCannonGameEnd = 'La location du jeu de canon est termin\xc3\xa9e.'
AvatarsHouse = 'Maison %s\n'
BankGuiCancel = lCancel
BankGuiOk = lOK
DistributedBankNoOwner = "D\xc3\xa9sol\xc3\xa9, ce n'est pas ta tirelire."
DistributedBankNotOwner = "D\xc3\xa9sol\xc3\xa9, ce n'est pas ta tirelire."
FishGuiCancel = lCancel
FishGuiOk = 'Tout vendre'
FishTankValue = 'Salut,%(name)s! Tu as %(num)s poisson(s) dans ton seau pour une valeur totale de %(value)s bonbon(s). Veux-tu vendre le tout ?'
FlowerGuiCancel = lCancel
FlowerGuiOk = 'Tout vendre'
FlowerBasketValue = "%(name)s, tu as %(num)s fleurs dans ton panier d'une valeur totale de %(value)s bonbons. Veux-tu toutes les vendre?"


def GetPossesive(name):
    if name[-1:] == 's':
        possesive = 'de ' + name
    else:
        possesive = 'de ' + name
    return possesive


PetTrait2descriptions = {
    'hungerThreshold': ('A toujours faim', 'A souvent faim', 'A quelquefois faim', 'A rarement faim'),
    'boredomThreshold': ("S'ennuie toujours", "S'ennuie souvent", "S'ennuie quelquefois", "S'ennuie rarement"),
    'angerThreshold': ('Toujours ronchon', 'Souvent ronchon', 'Quelquefois ronchon', 'Rarement ronchon'),
    'forgetfulness': ('Oublie toujours', 'Oublie souvent', 'Oublie quelquefois', 'Oublie rarement'),
    'excitementThreshold': (
    'Tr\xc3\xa8s calme', 'Plut\xc3\xb4t calme', 'Plut\xc3\xb4t excit\xc3\xa9', 'Tr\xc3\xa8s excit\xc3\xa9'),
    'sadnessThreshold': ('Toujours triste', 'Souvent triste', 'Quelquefois triste', 'Rarement triste'),
    'restlessnessThreshold': (
    'Toujours agit\xc3\xa9', 'Souvent agit\xc3\xa9', 'Quelquefois agit\xc3\xa9', 'Rarement agit\xc3\xa9'),
    'playfulnessThreshold': ('Rarement joueur', 'Quelquefois joueur', 'Souvent joueur', 'Toujours joueur'),
    'lonelinessThreshold': ('Toujours solitaire', 'Souvent solitaire', 'Quelquefois solitaire', 'Rarement solitaire'),
    'fatigueThreshold': (
    'Toujours fatigu\xc3\xa9', 'Souvent fatigu\xc3\xa9', 'Quelquefois fatigu\xc3\xa9', 'Rarement fatigu\xc3\xa9'),
    'confusionThreshold': ('Toujours perplexe', 'souvent perplexe', 'Quelquefois perplexe', 'Rarement perplexe'),
    'surpriseThreshold': ('Toujours surpris', 'souvent surpris', 'Quelquefois surpris', 'Rarement surpris'),
    'affectionThreshold': (
    'Rarement affectueux', 'Quelquefois affectueux', 'Souvent affectueux', 'Toujours affectueux')}
FireworksInstructions = lToonHQ + ': Appuie sur la touche "Page pr\xc3\xa9c\xc3\xa9dente" pour mieux voir.'
FireworksJuly4Beginning = lToonHQ + ': Welcome to summer fireworks! Enjoy the show!'
FireworksJuly4Ending = lToonHQ + ': Hope you enjoyed the show! Have a great summer!'
FireworksFebruary14Beginning = lToonHQ + ': Joyeuse Saint Valentin \xc3\xa0 tous les amoureux!'
FireworksFebruary14Ending = lToonHQ + ': Joyeuse Saint Valentin \xc3\xa0 tous les amoureux!'
FireworksJuly14Beginning = lToonHQ + ": Feux d'artifices du 14 Juillet: Profitez du spectacle!"
FireworksJuly14Ending = lToonHQ + ': Nous esp\xc3\xa9rons que vous avez profit\xc3\xa9 du spectacle!'
FireworksOctober31Beginning = lToonHQ + ": Bons feux d'artifice!"
FireworksOctober31Ending = lToonHQ + ": Nous esp\xc3\xa9rons que vous avez aim\xc3\xa9 les feux d'artifice!"
FireworksNewYearsEveBeginning = lToonHQ + ": Bonne ann\xc3\xa9e! Profitez du feu d'artifice!"
FireworksNewYearsEveEnding = lToonHQ + ': Nous esp\xc3\xa9rons que vous avez profit\xc3\xa9 du spectacle! Bonne ann\xc3\xa9e!'
FireworksBeginning = lToonHQ + ": Bons feux d'artifice!"
FireworksEnding = lToonHQ + ": Nous esp\xc3\xa9rons que vous avez aim\xc3\xa9 les feux d'artifice!"
TIP_NONE = 0
TIP_GENERAL = 1
TIP_STREET = 2
TIP_MINIGAME = 3
TIP_COGHQ = 4
TIP_ESTATE = 5
TIP_KARTING = 6
TipTitle = 'ASTUCE TOON:'
TipDict = {
    TIP_NONE: ('',),
    TIP_GENERAL: (
    'Pour v\xc3\xa9rifier rapidement les progr\xc3\xa8s de ton d\xc3\xa9fitoon, maintiens enfonc\xc3\xa9e la touche "Fin".',
    'Pour v\xc3\xa9rifier rapidement ta page de gags, maintiens enfonc\xc3\xa9e la touche "Premi\xc3\xa8re page".',
    'Pour ouvrir ta liste d\'contacts, appuie sur la touche "F7".',
    'Pour ouvrir ou fermer ton journal de bord, appuie sur la touche "F8".',
    'Pour regarder vers le haut, appuie sur la touche "Page pr\xc3\xa9c\xc3\xa9dente"; pour regarder vers le bas, appuie sur la touche "Page suivante".',
    'Appuie sur la touche "Contr\xc3\xb4le" pour sauter.',
    'Appuie sur la touche "F9" pour faire une capture d\'\xc3\xa9cran qui sera enregistr\xc3\xa9e dans le dossier Toontown de ton ordinateur.',
    "Tu peux changer ta r\xc3\xa9solution d'\xc3\xa9cran, r\xc3\xa9gler le son et d'autres options dans la page d'options du journal de bord.",
    'Essaie les v\xc3\xaatements de tes contacts, qui sont dans les placards de leur maison.',
    'Tu peux rentrer chez toi gr\xc3\xa2ce au bouton "Retour \xc3\xa0 la maison" sur ta carte.',
    'Chaque fois que tu termines un d\xc3\xa9fitoon avec succ\xc3\xa8s, tes rigolpoints sont automatiquement ajout\xc3\xa9s.',
    "Tu peux voir la collection dans les boutiques de pr\xc3\xaat-\xc3\xa0-porter m\xc3\xaame sans ticket d'habillement.",
    "Les r\xc3\xa9compenses de certains d\xc3\xa9fitoons te permettent d'avoir plus de gags et de bonbons.",
    "Tu peux avoir jusqu'\xc3\xa0 50 contacts sur ta liste d'contacts.",
    "La r\xc3\xa9compense de certains d\xc3\xa9fitoons te permet de te t\xc3\xa9l\xc3\xa9porter jusqu'aux terrains de jeux de Toontown par la carte du journal de bord.",
    'R\xc3\xa9cup\xc3\xa8re tes rigolpoints sur les terrains de jeux en ramassant des tr\xc3\xa9sors tels que des \xc3\xa9toiles et des cornets de glace.',
    'Si tu as besoin de te soigner rapidement apr\xc3\xa8s un combat difficile, va chez toi et ramasse des cornets de glace.',
    'Pour changer la visualisation de ton Toon, appuie sur la touche de tabulation.',
    'Quelquefois tu peux trouver plusieurs d\xc3\xa9fitoons diff\xc3\xa9rents propos\xc3\xa9s pour la m\xc3\xaame r\xc3\xa9compense. Fais ton choix!',
    'Trouver des contacts qui font le m\xc3\xaame d\xc3\xa9fitoon que toi est une mani\xc3\xa8re amusante de progresser dans le jeu.',
    "Tu n'as jamais besoin d'enregistrer ta progression dans Toontown. Les serveurs de Toontown enregistrent toutes les informations n\xc3\xa9cessaires en continu.",
    "Tu peux parler en chuchotant \xc3\xa0 d'autres Toons en cliquant sur eux ou en les s\xc3\xa9lectionnant dans ta liste d'contacts.",
    'Certaines phrases du Chat rapide provoquent une \xc3\xa9motion anim\xc3\xa9e sur ton Toon.',
    'Si tu te trouves dans une zone o\xc3\xb9 il y a trop de monde, tu peux essayer de changer de district. Va \xc3\xa0 la page des districts dans le journal de bord et choisis-en un autre.',
    "Si tu sauves activement des b\xc3\xa2timents, une \xc3\xa9toile de bronze, d'argent ou d'or s'affichera au-dessus de ton Toon.",
    "Si tu sauves assez de b\xc3\xa2timents pour avoir une \xc3\xa9toile au-dessus de la t\xc3\xaate, tu pourras trouver ton nom affich\xc3\xa9 sur le tableau d'un Quartier G\xc3\xa9n\xc3\xa9ral des Toons.",
    "Les b\xc3\xa2timents sauv\xc3\xa9s sont quelquefois recaptur\xc3\xa9s par les Cogs. La seule fa\xc3\xa7on de conserver ton \xc3\xa9toile est d'aller sauver plus de b\xc3\xa2timents.",
    'Les noms de tes amis appara\xc3\xaetront en bleu.',
    "Essaie d'avoir toutes les esp\xc3\xa8ces de poisson de Toontown!",
    'Chaque mare rec\xc3\xa8le diff\xc3\xa9rentes sortes de poissons. Essaie-les toutes!',
    "Lorsque ton seau de p\xc3\xaache est plein, tu peux vendre tes poissons aux vendeurs de l'animalerie sur les terrains de jeux.",
    "Tu peux vendre tes poissons au vendeur de l'animalerie, pr\xc3\xa8s des mares ou dans les animaleries m\xc3\xaame.",
    'Les cannes \xc3\xa0 p\xc3\xaache plus solides attrapent de plus gros poissons mais requi\xc3\xa8rent plus de bonbons.',
    'Tu peux acheter des cannes \xc3\xa0 p\xc3\xaache plus solides dans le catalogue.',
    "Les plus gros poissons valent plus de bonbons \xc3\xa0 l'animalerie.",
    "Les poissons plus rares valent plus de bonbons \xc3\xa0 l'animalerie.",
    'Tu peux quelquefois trouver des sacs de bonbons en p\xc3\xaachant.',
    'Certains d\xc3\xa9fitoons n\xc3\xa9cessitent de p\xc3\xaacher des objets dans les mares.',
    'Les mares des terrains de jeux ont des poissons diff\xc3\xa9rents de ceux des mares des rues.',
    "Certains poissons sont vraiment rares. Continue \xc3\xa0 p\xc3\xaacher jusqu'\xc3\xa0 ce que tu les aies tous!",
    'La mare que tu as chez toi contient des poissons qui ne peuvent pas \xc3\xaatre trouv\xc3\xa9s ailleurs.',
    '\xc3\x80 chaque fois que tu as attrap\xc3\xa9 10 esp\xc3\xa8ces, tu gagnes un troph\xc3\xa9e de p\xc3\xaache!',
    'Tu peux voir quels poissons tu as p\xc3\xaach\xc3\xa9s dans ton journal de bord.',
    'Certains troph\xc3\xa9es de p\xc3\xaache te valent une rigol-augmentation.',
    'La p\xc3\xaache est une bonne fa\xc3\xa7on de gagner plus de bonbons.', "Adopte un Doudou au magasin d'animaux!",
    "Les magasins d'animaux ont de nouveaux Doudous \xc3\xa0 vendre tous les jours.",
    "Rends-toi dans les magasins d'animaux tous les jours pour voir quels nouveaux Doudous ils ont.",
    'Dans les diff\xc3\xa9rents quartiers, il y a des Doudous diff\xc3\xa9rents \xc3\xa0 adopter.',
    'Fais chauffer ton super moteur et mets un coup de turbo \xc3\xa0 ta rigo-limite.',
    'Rends-toi dans le Circuit Dingo par le tunnel en forme de pneu qui se trouve dans Toontown Central.',
    'Gagne des rigolpoints au Circuit Dingo.', 'Le Circuit Dingo a six pistes de course diff\xc3\xa9rentes.'),
    TIP_STREET: ('Il existe quatre types de Cogs : les Loibots, les Caissbots, les Vendibots et les Chefbots.',
                 'Chaque s\xc3\xa9rie de gags est associ\xc3\xa9e \xc3\xa0 diff\xc3\xa9rents niveaux de pr\xc3\xa9cision et de d\xc3\xa9g\xc3\xa2ts.',
                 'Les gags de tapage affectent tous les Cogs mais r\xc3\xa9veillent les Cogs leurr\xc3\xa9s.',
                 'Battre les Cogs en ordre strat\xc3\xa9gique peut grandement augmenter tes chances de gagner les batailles.',
                 'La s\xc3\xa9rie de gags "toonique" te permet de soigner les autres Toons lors d\'une bataille.',
                 "Les points d'exp\xc3\xa9rience des gags sont doubl\xc3\xa9s pendant une invasion de Cogs!",
                 "Plusieurs Toons peuvent faire \xc3\xa9quipe et utiliser la m\xc3\xaame s\xc3\xa9rie de gags lors d'une bataille pour infliger plus de d\xc3\xa9g\xc3\xa2ts aux Cogs.",
                 "Lors des batailles, les gags sont utilis\xc3\xa9s dans l'ordre affich\xc3\xa9 sur le menu des gags, de haut en bas.",
                 "La rang\xc3\xa9e de points lumineux sur les ascenseurs des b\xc3\xa2timents des Cogs indiquent combien d'\xc3\xa9tages ils contiennent.",
                 'Clique sur un Cog pour avoir plus de d\xc3\xa9tails.',
                 "L'utilisation de gags de haut niveau contre des Cogs de bas niveau ne donne pas de points d'exp\xc3\xa9rience.",
                 "Un gag qui donnera de l'exp\xc3\xa9rience s'affiche sur fond bleu sur le menu des gags lors de la bataille.",
                 "L'exp\xc3\xa9rience des gags est multipli\xc3\xa9e lorsqu'ils sont utilis\xc3\xa9s \xc3\xa0 l'int\xc3\xa9rieur des b\xc3\xa2timents des Cogs. Les \xc3\xa9tages les plus hauts ont des coefficients de multiplication plus grands.",
                 "Lorsqu'un Cog est vaincu, chacun des Toons ayant particip\xc3\xa9 est cr\xc3\xa9dit\xc3\xa9 de la victoire sur ce Cog lorsque la bataille est termin\xc3\xa9e.",
                 'Chaque rue de Toontown a diff\xc3\xa9rents types et niveaux de Cogs.',
                 "Il n'y a pas de Cogs sur les trottoirs.",
                 "Dans les rues, tu peux entendre des blagues en t'approchant des portes lat\xc3\xa9rales.",
                 "Certains d\xc3\xa9fitoons t'entra\xc3\xaenent \xc3\xa0 de nouvelles s\xc3\xa9ries de gags. Tu ne pourras choisir que six des sept s\xc3\xa9ries de gags, alors choisis bien!",
                 "Les pi\xc3\xa8ges ne sont utiles que si toi ou tes contacts vous mettez d'accord pour utiliser les leurres lors d'une bataille.",
                 'Les leurres de plus haut niveau sont moins susceptibles de manquer leur cible.',
                 'Les gags de plus bas niveau ont une pr\xc3\xa9cision moindre contre les Cogs de haut niveau.',
                 "Les Cogs ne peuvent plus attaquer une fois qu'ils ont \xc3\xa9t\xc3\xa9 leurr\xc3\xa9s lors d'un combat.",
                 "Lorsque tes contacts et toi aurez repris un b\xc3\xa2timent aux Cogs, vos portraits seront affich\xc3\xa9s \xc3\xa0 l'int\xc3\xa9rieur du b\xc3\xa2timent en guise de r\xc3\xa9compense.",
                 "L'utilisation d'un gag toonique sur un Toon qui a un rigolm\xc3\xa8tre au maximum ne donne pas d'exp\xc3\xa9rience toonique.",
                 "Les Cogs sont bri\xc3\xa8vement assomm\xc3\xa9s lorsqu'ils sont frapp\xc3\xa9s par un gag. Cela augmente la chance que les autres gags du m\xc3\xaame tour le frappent.",
                 "Les gags de chute ont de faibles chances d'atteindre leur but, mais la pr\xc3\xa9cision est accrue lorsque les Cogs ont auparavant \xc3\xa9t\xc3\xa9 frapp\xc3\xa9s par un autre gag lors du m\xc3\xaame tour.",
                 'Lorsque tu as vaincu suffisamment de Cogs, tu peux utiliser le d\xc3\xa9tecteur de Cogs en cliquant sur les ic\xc3\xb4nes du d\xc3\xa9tecteur sur la page de la galerie des Cogs dans ton journal de bord.',
                 "Pendant une bataille, les tirets (-) et les X indiquent quel Cog tes \xc3\xa9quipiers sont en train d'attaquer.",
                 'Pendant une bataille, un voyant lumineux sur les Cogs indique leur \xc3\xa9tat de sant\xc3\xa9 : vert signifie en bonne sant\xc3\xa9, rouge au bord de la destruction.',
                 'Un maximum de quatre Toons peuvent combattre simultan\xc3\xa9ment.',
                 "Dans la rue, les Cogs prendront plus facilement part \xc3\xa0 une bataille contre plusieurs Toons qu'\xc3\xa0 une bataille contre un seul Toon.",
                 'Les deux Cogs les plus difficiles de chaque type ne se trouvent que dans les b\xc3\xa2timents.',
                 'Les gags de chute ne fonctionnent jamais contre les Cogs leurr\xc3\xa9s.',
                 'Les Cogs ont tendance \xc3\xa0 attaquer le Toon qui leur a caus\xc3\xa9 le plus de d\xc3\xa9g\xc3\xa2ts.',
                 'Les gags de tapage ne donnent pas de bonus contre les Cogs leurr\xc3\xa9s.',
                 "Si tu attends trop longtemps avant d'attaquer un Cog leurr\xc3\xa9, il se r\xc3\xa9veille. Les leurres de plus haut niveau durent plus longtemps.",
                 'Il y a des mares dans toutes les rues de Toontown. Certaines rues ont des esp\xc3\xa8ces de poissons uniques.'),
    TIP_MINIGAME: (
    'Apr\xc3\xa8s avoir rempli ton pot de bonbons, tous les bonbons que tu gagnes aux jeux du tramway sont automatiquement vers\xc3\xa9s dans ta tirelire.',
    'Tu peux utiliser les fl\xc3\xa8ches du clavier au lieu de la souris dans le jeu du tramway "Imite Minnie".',
    'Dans le jeu du canon, tu peux utiliser les fl\xc3\xa8ches du clavier pour d\xc3\xa9placer ton canon et appuyer sur la touche "Contr\xc3\xb4le" pour tirer.',
    'Dans le jeu des anneaux, des points suppl\xc3\xa9mentaires sont attribu\xc3\xa9s quand le groupe entier r\xc3\xa9ussit \xc3\xa0 nager dans les anneaux.',
    'Un jeu parfait d\'"Imite Minnie" double tes points.',
    'Dans le tir \xc3\xa0 la corde, tu re\xc3\xa7ois plus de bonbons si tu joues contre un Cog plus fort.',
    'La difficult\xc3\xa9 des jeux du tramway varie selon les quartiers, Toontown centre a les plus faciles et le Pays des r\xc3\xaaves de Donald les plus difficiles.',
    "Certains jeux du tramway ne peuvent \xc3\xaatre jou\xc3\xa9s qu'en groupe."),
    TIP_COGHQ: ("Tu dois terminer ton d\xc3\xa9guisement de Cog avant d'entrer dans le b\xc3\xa2timent du Chef.",
                'Tu peux sauter sur les gardes du corps des Cogs pour les d\xc3\xa9sactiver temporairement.',
                "Tu dois faire enti\xc3\xa8rement ton d\xc3\xa9guisement Loibot avant d'aller voir le Juge.",
                'Additionne les m\xc3\xa9rites Cogs par tes victoires sur les Cogs.',
                'Tu obtiens plus de m\xc3\xa9rites avec des Cogs de plus haut niveau.',
                'Lorsque tu as additionn\xc3\xa9 assez de m\xc3\xa9rites Cogs pour gagner une promotion, va voir le vice-pr\xc3\xa9sident des Vendibots !',
                'Tu peux parler comme un Cog lorsque tu portes ton d\xc3\xa9guisement de Cog.',
                "Jusqu'\xc3\xa0 huit Toons peuvent faire \xc3\xa9quipe pour combattre le vice-pr\xc3\xa9sident des Vendibots.",
                'Le vice-pr\xc3\xa9sident des Vendibots est tout en haut du quartier g\xc3\xa9n\xc3\xa9ral des Cogs.',
                "\xc3\x80 l'int\xc3\xa9rieur des usines des Cogs, monte les escaliers pour arriver jusqu'au contrema\xc3\xaetre.",
                "Chaque fois que tu te bats dans l'usine, tu gagnes une pi\xc3\xa8ce de ton d\xc3\xa9guisement de Cog.",
                'Tu peux visualiser le progr\xc3\xa8s de ton d\xc3\xa9guisement de Cog dans ton journal de bord.',
                'Tu peux visualiser le progr\xc3\xa8s de tes m\xc3\xa9rites sur ta page de d\xc3\xa9guisements dans ton journal de bord.',
                "Assure-toi d'avoir suffisamment de gags et un rigolm\xc3\xa8tre au maximum avant d'aller voir le vice-pr\xc3\xa9sident.",
                'Si tu as une promotion, ton d\xc3\xa9guisement de Cog est mis \xc3\xa0 jour.',
                "Tu dois vaincre le contrema\xc3\xaetre de l'usine pour r\xc3\xa9cup\xc3\xa9rer une pi\xc3\xa8ce du d\xc3\xa9guisement de Cog.",
                'R\xc3\xa9cup\xc3\xa8re des Convocations du Jury en d\xc3\xa9fiant des Loibots.',
                "Tu re\xc3\xa7ois plus de M\xc3\xa9rites, d'euros Cog ou de Convocations du Jury en combattant des Cogs de plus haut niveau.",
                'Quand tu as r\xc3\xa9cup\xc3\xa9r\xc3\xa9 assez de Convocations du Jury pour gagner une promotion, va voir le Juge  !',
                "Tu dois faire enti\xc3\xa8rement ton d\xc3\xa9guisement Loibot avant d'aller voir le Juge.",
                "Jusqu'\xc3\xa0 huit Toons peuvent combattre ensemble le Juge Loibot.",
                "Cela paie d'\xc3\xaatre perplexe : Les Cogs virtuels dans le QG Loibot ne t'accableront pas de Convocations du Jury.",
                ' Gagne des pi\xc3\xa8ces de costume de Caissbot comme r\xc3\xa9compense en terminant les d\xc3\xa9fitoons qui sont propos\xc3\xa9s dans le Pays des R\xc3\xaaves de Donald.',
                ' Les Caissbots fabriquent et font circuler leur argent, les euros Cogs, \xc3\xa0 partir de trois Fabriques \xc3\xa0 Sous - Pi\xc3\xa8ce, Euro et Lingot.',
                " Attends que le directeur financier soit \xc3\xa9tourdi avant de lui lancer un coffre dessus, ou il pourrait l'utiliser comme casque.\xc2\xa0Frapper le casque avec un autre coffre est la seule mani\xc3\xa8re de le faire\xc2\xa0tomber.",
                ' Gagne des pi\xc3\xa8ces de costume de Loibot comme r\xc3\xa9compense en terminant les d\xc3\xa9fitoons pour le professeur Flocon.',
                ' Ca paie de r\xc3\xa9soudre les probl\xc3\xa8mes\xc2\xa0: les Cogs virtuels du QG Loibot ne vont pas te r\xc3\xa9compenser avec des notices du jury.'),
    TIP_ESTATE: ('Les Doudous peuvent comprendre certaines expressions de Chat rapide. Essaie-les!',
                 'Utilise le menu "Animaux familiers" du Chat rapide pour demander \xc3\xa0 ton Doudou de faire des tours.',
                 'Tu peux apprendre des tours aux Doudous avec les le\xc3\xa7ons du catalogue vachement branch\xc3\xa9 de Clarabelle.',
                 'R\xc3\xa9compense ton Doudou quand il fait des tours.',
                 'Si tu te rends chez un ami, ton Doudou viendra aussi.',
                 'Donne un bonbon \xc3\xa0 ton Doudou quand il a faim.',
                 "Clique sur un Doudou pour afficher un menu gr\xc3\xa2ce auquel tu pourras le nourrir, le cajoler et l'appeler.",
                 'Les Doudous aiment la compagnie. Invite tes contacts \xc3\xa0 venir jouer!',
                 'Chaque Doudou a une personnalit\xc3\xa9 unique.',
                 "Tu peux rapporter ton Doudou et en adopter un nouveau \xc3\xa0 l'animalerie.",
                 'Quand un Doudou fait un tour, les Toons qui sont aux alentours sont soign\xc3\xa9s.',
                 "Les Doudous font leurs tours de mieux en mieux avec de l'entra\xc3\xaenement. Un peu de pers\xc3\xa9v\xc3\xa9rance!",
                 'Les tours plus avanc\xc3\xa9s des Doudous soignent plus vite les Toons.',
                 'Les Doudous exp\xc3\xa9riment\xc3\xa9s peuvent faire plus de tours avant de se fatiguer.',
                 "Tu peux voir une liste des Doudous qui sont \xc3\xa0 proximit\xc3\xa9 dans ta liste d'contacts.",
                 'Ach\xc3\xa8te des fournitures dans le catalogue de Clarabelle pour d\xc3\xa9corer ta maison.',
                 'La tirelire de ta maison contient des bonbons suppl\xc3\xa9mentaires.',
                 'Le placard de ta maison contient des v\xc3\xaatements suppl\xc3\xa9mentaires.',
                 'Rends-toi dans la maison de ton ami et essaie ses v\xc3\xaatements.',
                 'Ach\xc3\xa8te de meilleures cannes \xc3\xa0 p\xc3\xaache dans le catalogue de Clarabelle.',
                 'Ach\xc3\xa8te de plus grandes tirelires dans le catalogue de Clarabelle.',
                 'Appelle Clarabelle avec le t\xc3\xa9l\xc3\xa9phone qui est dans ta maison.',
                 'Clarabelle vend un placard plus grand qui contient plus de v\xc3\xaatements.',
                 "Fais de la place dans ton placard avant d'utiliser un ticket d'habillement.",
                 'Clarabelle vend tout ce dont tu as besoin pour d\xc3\xa9corer ta maison.',
                 'V\xc3\xa9rifie ta bo\xc3\xaete aux lettres pour trouver ta livraison apr\xc3\xa8s avoir command\xc3\xa9 chez Clarabelle.',
                 "Les v\xc3\xaatements du catalogue de Clarabelle sont livr\xc3\xa9s dans l'heure.",
                 "Le papier peint et le rev\xc3\xaatement de sol du catalogue de Clarabelle sont livr\xc3\xa9s dans l'heure.",
                 'Les meubles du catalogue de Clarabelle sont livr\xc3\xa9s un jour plus tard.',
                 'Stocke plus de meubles dans ton grenier.',
                 'Tu seras averti(e) par Clarabelle quand un nouveau catalogue sera pr\xc3\xaat.',
                 'Tu seras averti(e) par Clarabelle quand un nouveau catalogue sera pr\xc3\xaat.',
                 'Les nouveaux catalogues sont livr\xc3\xa9s chaque semaine.',
                 'Cherche les articles de vacances en \xc3\xa9dition limit\xc3\xa9e dans le catalogue.',
                 'Mets les meubles dont tu ne veux plus \xc3\xa0 la poubelle.',
                 'Certains poissons, comme le hareng saur, sont plus communs dans les propri\xc3\xa9t\xc3\xa9s des Toons.',
                 'Tu peux inviter tes contacts sur ta propri\xc3\xa9t\xc3\xa9 en utilisant le Chat rapide.',
                 'Est-ce que tu savais que la couleur de ta maison est assortie \xc3\xa0 celle de ton panneau Choisis un Toon ?'),
    TIP_KARTING: ('Ach\xc3\xa8te un Roadster, un Utilitoon ou une Berline au Centre Auto Dingo.',
                  "Customise ton kart avec des autocollants, des baguettes et plein d'autres d\xc3\xa9co au Centre Auto Dingo.",
                  'Gagne des tickets en faisant la course sur le Circuit Dingo.',
                  'Les tickets sont la seule monnaie accept\xc3\xa9e par le Centre Auto Dingo.',
                  ' Tu dois d\xc3\xa9poser des tickets pour pouvoir faire la course.',
                  'Une page sp\xc3\xa9ciale de ton journal de bord te permet de customiser ton kart.',
                  'Une page sp\xc3\xa9ciale de ton journal de bord te permet de consulter tes scores sur chaque piste.',
                  "Une page sp\xc3\xa9ciale de ton journal de bord te permet d'afficher tes troph\xc3\xa9es.",
                  'Le Colis\xc3\xa9e Tortill\xc3\xa9 est la piste la plus facile du Circuit Dingo.',
                  ' Les Landes L\xc3\xa9g\xc3\xa8res est la piste qui a le plus de collines et de bosses du Circuit Dingo.',
                  'Le Boulevard du Blizzard est la piste la plus excitante du Circuit Dingo.')}
FishGenusNames = {
    0: 'Baudruche',
    2: 'Poisson-chat',
    4: 'Poisson-clown',
    6: 'Poisson surgel\xc3\xa9',
    8: '\xc3\x89toile de mer',
    10: 'Hareng saur',
    12: 'Poisson chien',
    14: 'Anguille douce',
    16: 'Requin nourrice',
    18: 'Crabe-roi',
    20: 'Poisson-lune',
    22: 'Hippocampe',
    24: "Requin d'eau douce",
    26: 'Bar \xc3\xa0 coudas',
    28: 'Truite coupe-gorge',
    30: 'Thon tonl\xc3\xa9on',
    32: 'M\xc3\xa9duse m\xc3\xa9dus\xc3\xa9e',
    34: 'Raie tissante'}
FishSpeciesNames = {
    0: ('Poisson baudruche', 'Baudruche \xc3\xa0 air chaud', 'Baudruche m\xc3\xa9t\xc3\xa9o', 'Baudruche \xc3\xa0 eau',
        'Baudruche rouge'),
    2: (
    'Poisson-chat', 'Poisson-chat siamois', 'Poisson-chat piteau', 'Poisson-chat de goutti\xc3\xa8re', 'Poisson matou'),
    4: ('Poisson-clown', 'Poisson-clown triste', 'Poisson-pitre', 'Poisson-cirque'),
    6: ('Poisson surgel\xc3\xa9',),
    8: ('\xc3\x89toile de mer', '\xc3\x89toile de mer lu', '\xc3\x89toile de mer s\xc3\xa9d\xc3\xa8s',
        '\xc3\x89toile de mer credi', '\xc3\x89toile de mer ciatous'),
    10: ('Hareng saur',),
    12: (
    'Poisson chien', 'Poisson-chien de tra\xc3\xaeneau', 'Poisson-chien-chien', 'Poisson dalmatien', 'Poisson chiot'),
    14: ('Anguille douce', 'Anguille rette \xc3\xa9lectrique'),
    16: ('Requin nourrice', 'Requin nourrice tique', 'Requin nourrice tourne'),
    18: ('Crabe-roi', "Crabe roi d'Alaska", 'Vieux crabe roi'),
    20: (
    'Poisson-lune', 'Poisson pleine lune', 'Poisson demi-lune', 'Poisson nouvelle lune', 'Poisson croissant de lune',
    'Poisson \xc3\xa9quinoxe'),
    22: ('Hippocampe', 'Hippocampe oscillant', 'Hippocampe percheron', 'Hippocampe oriental'),
    24: ("Requin d'eau douce", 'Requin de baignoire', 'Requin de piscine', 'Requin olympique'),
    26: ('Bar tabba', 'Bar amine', 'Bar ratin', 'Bar ricade', 'Bar sovie', 'Bar rac\xc3\xa9', 'Bar cadaire',
         'Bar bouill\xc3\xa9'),
    28: ('Truite coupe-gorge', 'Truite capitaine', 'Truite scorbut'),
    30: ('Thon tonl\xc3\xa9on', 'Thon-clave', 'Thon-suret', 'Thon bola', 'Thon duras\xc3\xa9'),
    32: ('M\xc3\xa9duse m\xc3\xa9dus\xc3\xa9e', 'Poisson-cacahu\xc3\xa8te', 'Poisson pan\xc3\xa9', 'Poisson fraise',
         'Poisson raisin'),
    34: ('Raie tissante',)}
CogPartNames = (
'Cuisse gauche', 'Tibia gauche', 'Pied gauche', 'Cuisse droite', 'Tibia droit', 'Pied droit', '\xc3\x89paule gauche',
'\xc3\x89paule droite', 'Poitrine', 'Compteur de sant\xc3\xa9', 'Bassin', 'Bras gauche', 'Avant-bras gauche',
'Main gauche', 'Bras droit', 'Avant-bras droit', 'Main droite')
CogPartNamesSimple = ('Haut du torse',)
FishFirstNames = (
'', 'Ang\xc3\xa9line', 'Arctique', 'B\xc3\xa9b\xc3\xa9', 'Bermuda', 'Grand', 'Fontaine', 'Bubule', 'Buster', 'Candy',
'Capitaine', 'Ciboulette', 'Choupette', 'Corail', 'Docteur', 'Toussale', 'Empereur', 'M\xc3\xa2chefer', 'Gros', 'Filou',
'Palmyre', 'Polochon', 'Totoche', 'Doudou', 'Jack', 'Roi', "P'tit", 'Marin', 'Mamzelle', 'Monsieur', 'Pomme',
'Petit-Doigt', 'Prince', 'Princesse', 'Professeur', 'Bouboule', 'Reine', 'Mirage', 'Ray', 'Rosie', 'Robert', 'Poivre',
'Nicole', 'Sandy', '\xc3\x89caille', "Dent d'or", 'Sire', 'Sacha', 'Pantoufle', 'Chipeur', 'Mini', 'S\xc3\xa9bastien',
"P'tit-Pois", '\xc3\x89toile', "Sucre d'orge", 'Super', 'Tigre', 'Microbe', 'Moustache')
FishLastPrefixNames = (
'', 'Laplage', 'Noir', 'Bleu', 'Marcassin', 'Lavache', 'Minou', 'Aufond', 'Double', 'Est', 'Chichi', '\xc3\x89caille',
'Plat', 'Frais', 'G\xc3\xa9ant', 'Dorpur', 'Dor\xc3\xa9', 'Gris', 'Vert', 'Goinfre', 'Jacasse', 'Gel\xc3\xa9e', 'Dame',
'Cuir', 'Citron', 'Long', 'Nord', 'Oc\xc3\xa9an', 'Octo', 'Huile', 'Perle', 'Mousse', 'Rouge', 'Ruban', 'Fleuve', 'Roc',
'Rubis', 'Barre', 'Sel', 'Mer', 'Argent', 'Tuba', 'Semelle', 'Sud', 'H\xc3\xa9risse', 'Surf', 'Sabre', 'Tigre',
'Triple', 'Tropical', 'Thon', 'Coucou', 'Faible', 'Ouest', 'Blanc', 'Jaune')
FishLastSuffixNames = (
'', 'balle', 'basse', 'ventre', 'punaise', 'vole', 'beurre', 'dents', 'botte', 'crabe', 'ronchon', 'tambour', 'palme',
'poisson', 'nette', 'nageoire', 'flou', 'grogne', 't\xc3\xaate', 'veste', 'saut', 'sardine', 'lune', 'bouche', 'mulet',
'cou', 'nez', 'perche', 'rauque', 'coureur', 'voile', 'requin', 'coquille', 'soie', 'bave', 'vif', 'pue', 'queue',
'crapaud', 'truite', 'eau')
SellbotLegFactorySpecMainEntrance = 'Entr\xc3\xa9e principale'
SellbotLegFactorySpecLobby = 'Accueil'
SellbotLegFactorySpecLobbyHallway = "Couloir de l'accueil"
SellbotLegFactorySpecGearRoom = 'Salle des pignons'
SellbotLegFactorySpecBoilerRoom = 'Chaufferie'
SellbotLegFactorySpecEastCatwalk = 'Passerelle est'
SellbotLegFactorySpecPaintMixer = 'M\xc3\xa9langeur \xc3\xa0 peinture'
SellbotLegFactorySpecPaintMixerStorageRoom = 'R\xc3\xa9serve du m\xc3\xa9langeur \xc3\xa0 peinture'
SellbotLegFactorySpecWestSiloCatwalk = 'Passerelle du silo ouest'
SellbotLegFactorySpecPipeRoom = 'Salle des tuyaux'
SellbotLegFactorySpecDuctRoom = 'Salle des canalisations'
SellbotLegFactorySpecSideEntrance = 'Entr\xc3\xa9e lat\xc3\xa9rale'
SellbotLegFactorySpecStomperAlley = 'All\xc3\xa9e des pas perdus'
SellbotLegFactorySpecLavaRoomFoyer = 'Accueil des sanitaires'
SellbotLegFactorySpecLavaRoom = 'Sanitaires'
SellbotLegFactorySpecLavaStorageRoom = 'R\xc3\xa9serve des sanitaires'
SellbotLegFactorySpecWestCatwalk = 'Passerelle ouest'
SellbotLegFactorySpecOilRoom = 'Salle du p\xc3\xa9trole'
SellbotLegFactorySpecLookout = "Poste d'observation"
SellbotLegFactorySpecWarehouse = 'R\xc3\xa9serve'
SellbotLegFactorySpecOilRoomHallway = 'Entr\xc3\xa9e de la salle du p\xc3\xa9trole'
SellbotLegFactorySpecEastSiloControlRoom = 'Salle de contr\xc3\xb4le du silo est'
SellbotLegFactorySpecWestSiloControlRoom = 'Salle de contr\xc3\xb4le du silo ouest'
SellbotLegFactorySpecCenterSiloControlRoom = 'Salle de contr\xc3\xb4le du silo central'
SellbotLegFactorySpecEastSilo = 'Silo est'
SellbotLegFactorySpecWestSilo = 'Silo ouest'
SellbotLegFactorySpecCenterSilo = 'Silo central'
SellbotLegFactorySpecEastSiloCatwalk = 'Passerelle du silo est'
SellbotLegFactorySpecWestElevatorShaft = "Puits de l'ascenseur ouest"
SellbotLegFactorySpecEastElevatorShaft = "Puits de l'ascenseur est"
FishBingoBingo = 'BINGO!'
FishBingoVictory = 'VICTOIRE!!'
FishBingoJackpot = 'JACKPOT!'
FishBingoGameOver = 'JEU TERMIN\xc3\x89'
FishBingoIntermission = 'La pause\nse termine dans :'
FishBingoNextGame = 'Le prochain jeu\ncommence dans :'
FishBingoTypeNormal = 'Classique'
FishBingoTypeCorners = 'Quatre coins'
FishBingoTypeDiagonal = 'Diagonales'
FishBingoTypeThreeway = 'Trois voies'
FishBingoTypeBlockout = 'GRILLE ENTIERE!'
FishBingoStart = "C'est l'heure du loto des poissons! Rends-toi sur n'importe quel ponton libre pour jouer!"
FishBingoEnd = "J'esp\xc3\xa8re que le loto des poissons t'a plu."
FishBingoHelpMain = "Bienvenue au loto des poissons de Toontown! Tout le monde \xc3\xa0 la mare s'active pour remplir la grille avant la fin du temps imparti."
FishBingoHelpFlash = 'Quand tu attrapes un poisson, clique sur un des carr\xc3\xa9s clignotants pour marquer la grille.'
FishBingoHelpNormal = "C'est une grille de loto classique. Tu gagnes si tu remplis n'importe quel rang\xc3\xa9e verticalement, horizontalement ou diagonalement."
FishBingoHelpDiagonals = 'Remplis les deux diagonales pour gagner.'
FishBingoHelpCorners = 'Une grille de coins facile. Remplis les quatre coins pour gagner.'
FishBingoHelpThreeway = "Trois voies. Remplis les deux diagonales et la rang\xc3\xa9e du milieu pour gagner. \xc3\x87a n'est pas facile!"
FishBingoHelpBlockout = 'Grille enti\xc3\xa8re! Remplis la grille enti\xc3\xa8re pour gagner. Tu joues contre toutes les autres mares pour remporter un \xc3\xa9norme jackpot!'
FishBingoOfferToSellFish = 'Ton seau est plein de poissons. Est-ce que tu voudrais en vendre ?'
FishBingoJackpot = 'Gain: %s bonbons!'
FishBingoJackpotWin = 'Gain: %s bonbons!'
ResistanceToonupMenu = 'Toonique'
ResistanceToonupItem = '%s Toonique'
ResistanceToonupItemMax = 'Max'
ResistanceToonupChat = 'Toons du Monde entier, Toonique!'
ResistanceRestockMenu = '\xc3\x80 vos gags'
ResistanceRestockItem = '\xc3\x80 vos gags %s'
ResistanceRestockItemAll = 'Tous'
ResistanceRestockChat = 'Toons du Monde entier, \xc3\xa0 vos gags!'
ResistanceMoneyMenu = 'Bonbons'
ResistanceMoneyItem = '%s bonbons'
ResistanceMoneyChat = 'Toons du Monde entier, d\xc3\xa9pensez avec sagesse!'
ResistanceEmote1 = NPCToonNames[9228] + ': Bienvenue dans la r\xc3\xa9sistance!'
ResistanceEmote2 = NPCToonNames[
                       9228] + ": Utilise ton nouvel \xc3\xa9moticone pour t'identifier aupr\xc3\xa8s des autres membres."
ResistanceEmote3 = NPCToonNames[9228] + ': Bonne chance!'
KartUIExit = 'Laisser le kart'
KartShop_Cancel = lCancel
KartShop_BuyKart = 'Acheter un kart'
KartShop_BuyAccessories = 'Acheter des accessoires'
KartShop_BuyAccessory = 'Acheter un accessoire'
KartShop_Cost = 'Prix: %d tickets'
KartShop_ConfirmBuy = 'Acheter cette %s pour %d tickets?'
KartShop_NoAvailableAcc = "Aucun accessoire de ce type n'est disponible."
KartShop_FullTrunk = 'Ton coffre est plein.'
KartShop_ConfirmReturnKart = 'Tu veux vraiment rendre ton kart actuel?'
KartShop_ConfirmBoughtTitle = 'Bravo!'
KartShop_NotEnoughTickets = 'Pas assez de tickets!'
KartView_Rotate = 'Faire tourner'
KartView_Right = 'Droite'
KartView_Left = 'Gauche'
StartingBlock_NotEnoughTickets = "Tu n'as pas assez de tickets! Fais plut\xc3\xb4t une course d'entra\xc3\xaenement."
StartingBlock_NoBoard = 'Les inscriptions sont termin\xc3\xa9es pour cette course. Tu dois attendre que la prochaine course commence.'
StartingBlock_NoKart = "Il te faut d'abord un kart! Va donc voir un des vendeurs du magasin de kart."
StartingBlock_Occupied = 'Ce plot de d\xc3\xa9part est actuellement occup\xc3\xa9! Essaie un autre endroit.'
StartingBlock_TrackClosed = 'Nous sommes d\xc3\xa9sol\xc3\xa9s, cette piste est ferm\xc3\xa9e pour cause de r\xc3\xa9fection.'
StartingBlock_EnterPractice = "Tu veux participer \xc3\xa0 une course d'entra\xc3\xaenement ?"
StartingBlock_EnterNonPractice = 'Veux-tu participer \xc3\xa0 une course %s pour %s tickets?'
StartingBlock_EnterShowPad = 'Veux-tu garer ta voiture ici?'
StartingBlock_KickSoloRacer = 'Les combats de Toons et les Grands Prix requi\xc3\xa8rent deux pilotes ou plus.'
StartingBlock_Loading = 'Allons \xc3\xa0 la course!'
LeaderBoard_Time = 'Temps'
LeaderBoard_Name = 'Nom du pilote'
LeaderBoard_Daily = 'Scores quotidiens'
LeaderBoard_Weekly = 'Scores hebdomadaires'
LeaderBoard_AllTime = 'Meilleurs scores de tous les temps'
RecordPeriodStrings = [
    LeaderBoard_Daily,
    LeaderBoard_Weekly,
    LeaderBoard_AllTime]
KartRace_RaceNames = [
    'Entra\xc3\xaenement',
    'Combat de Toons',
    'Tournoi']
from toontown.racing import RaceGlobals

KartRace_Go = 'Partez!'
KartRace_Reverse = ' Invers\xc3\xa9'
KartRace_TrackNames = {
    RaceGlobals.RT_Speedway_1: 'Stade Cinglette',
    RaceGlobals.RT_Speedway_1_rev: 'Stade Cinglette' + KartRace_Reverse,
    RaceGlobals.RT_Rural_1: 'Piste Champ\xc3\xaatre',
    RaceGlobals.RT_Rural_1_rev: 'Piste Champ\xc3\xaatre' + KartRace_Reverse,
    RaceGlobals.RT_Urban_1: 'Circuit de la Ville',
    RaceGlobals.RT_Urban_1_rev: 'Circuit de la Ville' + KartRace_Reverse,
    RaceGlobals.RT_Speedway_2: 'Colis\xc3\xa9e Tortill\xc3\xa9',
    RaceGlobals.RT_Speedway_2_rev: 'Colis\xc3\xa9e Tortill\xc3\xa9' + KartRace_Reverse,
    RaceGlobals.RT_Rural_2: 'Landes L\xc3\xa9g\xc3\xa8res',
    RaceGlobals.RT_Rural_2_rev: 'Landes L\xc3\xa9g\xc3\xa8res' + KartRace_Reverse,
    RaceGlobals.RT_Urban_2: 'Bld du Blizzard',
    RaceGlobals.RT_Urban_2_rev: 'Bld du Blizzard' + KartRace_Reverse}
KartRace_Unraced = 'S/O'
KartDNA_KartNames = {
    0: 'Berline',
    1: 'Roadster',
    2: 'Utilitoon'}
KartDNA_AccNames = {
    1000: 'Filtre \xc3\xa0 air',
    1001: 'Carburateur quadruple',
    1002: 'Aigle en vol',
    1003: 'Cornes de b\xc5\x93uf',
    1004: 'Six cylindres en ligne',
    1005: 'Petit d\xc3\xa9flecteur',
    1006: 'Arbre \xc3\xa0 cames simple',
    1007: 'D\xc3\xa9flecteur moyen',
    1008: 'Carburateur monocorps',
    1009: 'Klaxon \xc3\xa0 soufflet',
    1010: 'D\xc3\xa9flecteur ray\xc3\xa9',
    2000: 'Aileron espace',
    2001: 'Roue de secours avec rustines',
    2002: 'Arceau de s\xc3\xa9curit\xc3\xa9',
    2003: 'Ailette simple',
    2004: 'Double aileron',
    2005: 'Aileron simple',
    2006: 'Roue de secours standard',
    2007: 'Ailette simple',
    2008: 'sp9',
    2009: 'sp10',
    3000: 'Klaxon 2 tons',
    3001: 'Pare-chocs de Freddie',
    3002: 'Bas de caisse Cobalt',
    3003: 'Pots lat\xc3\xa9raux Cobra',
    3004: 'Pots lat\xc3\xa9raux droits',
    3005: 'Pare-chocs dentel\xc3\xa9s',
    3006: 'Bas de caisse carbone',
    3007: 'Bas de caisse bois',
    3008: 'fw9',
    3009: 'fw10',
    4000: 'Pots arri\xc3\xa8res courb\xc3\xa9s',
    4001: 'Pare-chocs Splash',
    4002: 'Double \xc3\xa9chappement',
    4003: 'Doubles ailettes simples',
    4004: 'Bavettes simples',
    4005: '\xc3\x89chappement de quad',
    4006: 'Doubles \xc3\xa9largisseurs de caisse',
    4007: 'M\xc3\xa9ga \xc3\xa9chappement',
    4008: 'Doubles ailettes ray\xc3\xa9es',
    4009: 'Doubles ailettes bulle',
    4010: 'Bavettes ray\xc3\xa9es',
    4011: 'Bavettes Mickey',
    4012: 'Bavettes dentel\xc3\xa9es',
    5000: 'Turbo',
    5001: 'Lune',
    5002: 'Roue avec rustine',
    5003: 'Trois rayons',
    5004: 'Couvercle peinture',
    5005: 'C\xc5\x93ur',
    5006: 'Mickey',
    5007: 'Cinq boulons',
    5008: 'Daisy',
    5009: 'Basket-ball',
    5010: 'Hypno',
    5011: 'Tribal',
    5012: 'Pierre pr\xc3\xa9cieuse',
    5013: 'Cinq rayons',
    5014: 'Pacotille',
    6000: 'Num\xc3\xa9ro cinq',
    6001: '\xc3\x89claboussure',
    6002: 'Damiers',
    6003: 'Flammes',
    6004: 'C\xc5\x93urs',
    6005: 'Bulles',
    6006: 'Tigre',
    6007: 'Fleurs',
    6008: '\xc3\x89clair',
    6009: 'Ange',
    7000: 'Vertanis',
    7001: 'P\xc3\xaache',
    7002: 'Rouge vif',
    7003: 'Rouge',
    7004: 'Bordeaux',
    7005: 'Sienne',
    7006: 'Marron',
    7007: 'Havane',
    7008: 'Corail',
    7009: 'Orange',
    7010: 'Jaune',
    7011: 'Cr\xc3\xa8me',
    7012: 'Citrine',
    7013: 'Citron vert',
    7014: 'Vert marin',
    7015: 'Vert',
    7016: 'Bleu clair',
    7017: 'Bleuaqua',
    7018: 'Bleu',
    7019: 'Bleupervenche',
    7020: 'Bleu roi',
    7021: 'Bleu ardoise',
    7022: 'Violet',
    7023: 'Lavande',
    7024: 'Rose',
    7025: 'Gris',
    7026: 'Noir'}
RaceHoodSpeedway = 'Circuit'
RaceHoodRural = 'Champ\xc3\xaatre'
RaceHoodUrban = 'Ville'
RaceTypeCircuit = 'Tournoi'
RaceQualified = 'Tu es qualifi\xc3\xa9(e)'
RaceSwept = 'Tu les as balay\xc3\xa9s'
RaceWon = 'Tu as gagn\xc3\xa9'
Race = 'parcours'
Races = 'parcours'
Total = 'total'
GrandTouring = 'Grand Tour'


def getTrackGenreString(genreId):
    genreStrings = [
        'Circuit',
        'Pays',
        'Ville']
    return genreStrings[genreId].lower()


def getTunnelSignName(trackId, padId):
    if trackId == 2 and padId == 0:
        return 'panneau ville1_tunnel'
    elif trackId == 1 and padId == 0:
        return 'panneau campagne_tunnel1'
    else:
        genreId = RaceGlobals.getTrackGenre(trackId)
        return 'panneau %s_%stunnel' % (padId + 1, RaceGlobals.getTrackGenreString(genreId))


KartTrophyDescriptions = [
    RaceQualified + ' pour ' + str(RaceGlobals.QualifiedRaces[0]) + ' ' + Race + ' ' + RaceHoodSpeedway,
    RaceQualified + ' pour ' + str(RaceGlobals.QualifiedRaces[1]) + ' ' + Races + ' ' + RaceHoodSpeedway,
    RaceQualified + ' pour ' + str(RaceGlobals.QualifiedRaces[2]) + ' ' + Races + ' ' + RaceHoodSpeedway,
    RaceQualified + ' pour ' + str(RaceGlobals.QualifiedRaces[0]) + ' ' + Race + ' ' + RaceHoodRural,
    RaceQualified + ' pour ' + str(RaceGlobals.QualifiedRaces[1]) + ' ' + Races + ' ' + RaceHoodRural,
    RaceQualified + ' pour ' + str(RaceGlobals.QualifiedRaces[2]) + ' ' + Races + ' ' + RaceHoodRural,
    RaceQualified + ' pour ' + str(RaceGlobals.QualifiedRaces[0]) + ' ' + Race + ' ' + RaceHoodUrban,
    RaceQualified + ' pour ' + str(RaceGlobals.QualifiedRaces[1]) + ' ' + Races + ' ' + RaceHoodUrban,
    RaceQualified + ' pour ' + str(RaceGlobals.QualifiedRaces[2]) + ' ' + Races + ' ' + RaceHoodUrban,
    RaceQualified + ' pour ' + str(RaceGlobals.TotalQualifiedRaces) + ' ' + Races + ' au ' + Total,
    RaceWon + ' ' + str(RaceGlobals.WonRaces[0]) + ' ' + Race + ' ' + RaceHoodSpeedway,
    RaceWon + ' ' + str(RaceGlobals.WonRaces[1]) + ' ' + Races + ' ' + RaceHoodSpeedway,
    RaceWon + ' ' + str(RaceGlobals.WonRaces[2]) + ' ' + Races + ' ' + RaceHoodSpeedway,
    RaceWon + ' ' + str(RaceGlobals.WonRaces[0]) + ' ' + Race + ' ' + RaceHoodRural,
    RaceWon + ' ' + str(RaceGlobals.WonRaces[1]) + ' ' + Races + ' ' + RaceHoodRural,
    RaceWon + ' ' + str(RaceGlobals.WonRaces[2]) + ' ' + Races + ' ' + RaceHoodRural,
    RaceWon + ' ' + str(RaceGlobals.WonRaces[0]) + ' ' + Race + ' ' + RaceHoodUrban,
    RaceWon + ' ' + str(RaceGlobals.WonRaces[1]) + ' ' + Races + ' ' + RaceHoodUrban,
    RaceWon + ' ' + str(RaceGlobals.WonRaces[2]) + ' ' + Races + ' ' + RaceHoodUrban,
    RaceWon + ' ' + str(RaceGlobals.TotalWonRaces) + ' ' + Races + ' au ' + Total,
    RaceQualified + ' pour ' + str(RaceGlobals.WonCircuitRaces[0]) + ' ' + Race + ' ' + RaceTypeCircuit,
    RaceQualified + ' pour ' + str(RaceGlobals.WonCircuitRaces[1]) + ' ' + Races + ' ' + RaceTypeCircuit,
    RaceQualified + ' pour ' + str(RaceGlobals.WonCircuitRaces[2]) + ' ' + Races + ' ' + RaceTypeCircuit,
    RaceWon + ' ' + str(RaceGlobals.WonCircuitRaces[0]) + ' ' + Race + ' ' + RaceTypeCircuit,
    RaceWon + ' ' + str(RaceGlobals.WonCircuitRaces[1]) + ' ' + Races + ' ' + RaceTypeCircuit,
    RaceWon + ' ' + str(RaceGlobals.WonCircuitRaces[2]) + ' ' + Races + ' ' + RaceTypeCircuit,
    RaceSwept + ' dans ' + str(RaceGlobals.SweptCircuitRaces[0]) + ' ' + Race + ' ' + RaceTypeCircuit,
    RaceSwept + ' dans ' + str(RaceGlobals.SweptCircuitRaces[1]) + ' ' + Races + ' ' + RaceTypeCircuit,
    RaceSwept + ' dans ' + str(RaceGlobals.SweptCircuitRaces[2]) + ' ' + Races + ' ' + RaceTypeCircuit,
    GrandTouring,
    str(RaceGlobals.TrophiesPerCup) + ' Troph\xc3\xa9es gagn\xc3\xa9s aux courses de kart! Rigol-augmentation!',
    str(RaceGlobals.TrophiesPerCup * 2) + ' Troph\xc3\xa9es gagn\xc3\xa9s aux courses de kart! Rigol-augmentation!',
    str(RaceGlobals.TrophiesPerCup * 3) + ' Troph\xc3\xa9es gagn\xc3\xa9s aux courses de kart! Rigol-augmentation!']
KartRace_TitleInfo = 'Pr\xc3\xa9pare-toi pour la course'
KartRace_SSInfo = "Bienvenue au stade Cinglette!\nPied au plancher, et on s'accroche. \xc3\x87a va secouer!\n"
KartRace_CoCoInfo = "Bienvenue au Colis\xc3\xa9e Tortill\xc3\xa9 ! Utilise l'inclinaison des virages pour maintenir ta vitesse !\n"
KartRace_RRInfo = 'Bienvenue sur la piste Champ\xc3\xaatre!\nAttention aux animaux, reste bien sur la piste!\n'
KartRace_AAInfo = "Bienvenue aux Landes l\xc3\xa9g\xc3\xa8res ! Tiens bien ton chapeau ! \xc3\x87a a l'air d'\xc3\xaatre plein de bosses par ici...\n"
KartRace_CCInfo = 'Bienvenue sur le circuit de la Ville!\nAttention aux pi\xc3\xa9tons quand tu fonces \xc3\xa0 travers la ville!\n'
KartRace_BBInfo = "Bienvenue au Boulevard du Blizzard ! Attention \xc3\xa0 ta vitesse. Il se peut qu'il y ait de la glace par l\xc3\xa0-bas.\n"
KartRace_GeneralInfo = 'Utilise la touche Contr\xc3\xb4le pour lancer les gags que tu ramasses sur la piste, et les fl\xc3\xa8ches pour diriger ton kart.'
KartRace_TrackInfo = {
    RaceGlobals.RT_Speedway_1: KartRace_SSInfo + KartRace_GeneralInfo,
    RaceGlobals.RT_Speedway_1_rev: KartRace_SSInfo + KartRace_GeneralInfo,
    RaceGlobals.RT_Speedway_2: KartRace_CoCoInfo + KartRace_GeneralInfo,
    RaceGlobals.RT_Speedway_2_rev: KartRace_CoCoInfo + KartRace_GeneralInfo,
    RaceGlobals.RT_Rural_1: KartRace_RRInfo + KartRace_GeneralInfo,
    RaceGlobals.RT_Rural_1_rev: KartRace_RRInfo + KartRace_GeneralInfo,
    RaceGlobals.RT_Rural_2: KartRace_AAInfo + KartRace_GeneralInfo,
    RaceGlobals.RT_Rural_2_rev: KartRace_AAInfo + KartRace_GeneralInfo,
    RaceGlobals.RT_Urban_1: KartRace_CCInfo + KartRace_GeneralInfo,
    RaceGlobals.RT_Urban_1_rev: KartRace_CCInfo + KartRace_GeneralInfo,
    RaceGlobals.RT_Urban_2: KartRace_BBInfo + KartRace_GeneralInfo,
    RaceGlobals.RT_Urban_2_rev: KartRace_BBInfo + KartRace_GeneralInfo}
KartRecordStrings = {
    RaceGlobals.Daily: 'quotidien',
    RaceGlobals.Weekly: 'hebdomadaire',
    RaceGlobals.AllTime: 'de tous les temps'}
KartRace_FirstSuffix = 'er'
KartRace_SecondSuffix = '\xc3\xa8me'
KartRace_ThirdSuffix = ' rd'
KartRace_FourthSuffix = ' th'
KartRace_WrongWay = 'Sens\ninterdit!'
KartRace_LapText = 'Tour %s'
KartRace_FinalLapText = 'Dernier tour!'
KartRace_Exit = 'Sortir de la course'
KartRace_NextRace = 'Course suivante'
KartRace_Leave = 'Quitter la course'
KartRace_Qualified = 'Qualifi\xc3\xa9(e)!'
KartRace_Record = 'Record!'
KartRace_RecordString = 'Tu as \xc3\xa9tabli un nouveau %s record pour %s! Ton bonus est de %s tickets.'
KartRace_Tickets = ' Tickets'
KartRace_Exclamations = '!'
KartRace_Deposit = 'D\xc3\xa9p\xc3\xb4t'
KartRace_Winnings = 'Gains'
KartRace_Bonus = 'Bonus'
KartRace_RaceTotal = 'Total course'
KartRace_CircuitTotal = 'Circuit entier'
KartRace_Trophies = 'Troph\xc3\xa9es'
KartRace_Zero = '0'
KartRace_Colon = ':'
KartRace_TicketPhrase = '%s' + KartRace_Tickets
KartRace_DepositPhrase = KartRace_Deposit + KartRace_Colon + '\n'
KartRace_QualifyPhrase = 'Qualifi\xc3\xa9:\n'
KartRace_RaceTimeout = 'Tu as fini apr\xc3\xa8s la fin de la course. Tes tickets ont \xc3\xa9t\xc3\xa9 rembours\xc3\xa9s. Essaie encore!'
KartRace_RaceTimeoutNoRefund = "Tu as mis trop de temps \xc3\xa0 finir la course. Tes tickets n'ont pas \xc3\xa9t\xc3\xa9 rembours\xc3\xa9s parce que le Grand Prix a d\xc3\xa9j\xc3\xa0 commenc\xc3\xa9. Essaie \xc3\xa0 nouveau !"
KartRace_RacerTooSlow = 'Tu as mis trop de temps \xc3\xa0 finir la course. Tes tickets ne te sont pas rembours\xc3\xa9s. Fais une autre course !'
KartRace_PhotoFinish = "Photo \xc3\xa0 l'arriv\xc3\xa9e"
KartRace_CircuitPoints = 'Score'
CircuitRaceStart = 'Le Grand Prix Toontown au Circuit Dingo va commencer !  Pour gagner la comp\xc3\xa9tition, remporte le maximum de points en trois courses cons\xc3\xa9cutives !'
CircuitRaceEnd = "Le Grand Prix Toontown est termin\xc3\xa9 pour aujourd'hui.  Rendez-vous lundi prochain pour une nouvelle \xc3\xa9dition."
TrickOrTreatMsg = 'Tu as d\xc3\xa9j\xc3\xa0\ntrouv\xc3\xa9 cette friandise.'
LawbotBossTempIntro0 = "Bon, on a quoi au registre aujourd'hui ?"
LawbotBossTempIntro1 = "Ha, on a le proc\xc3\xa8s d'un Toon !"
LawbotBossTempIntro2 = "L'accusation a de bonnes cartes."
LawbotBossTempIntro3 = "Et voil\xc3\xa0 les avocats commis d'office."
LawbotBossTempIntro4 = 'Attendez une minute... Vous \xc3\xaates des Toons !'
LawbotBossTempJury1 = 'La s\xc3\xa9lection du jury va maintenant commencer.'
LawbotBossHowToGetEvidence = 'Touche la barre des t\xc3\xa9moins pour obtenir des preuves.'
LawbotBossTrialChat1 = 'La s\xc3\xa9ance est ouverte.'
LawbotBossHowToThrowPies = 'Appuie sur la touche \xc2\xab Inser \xc2\xbb pour envoyer les preuves\n sur les avocats ou dans la balance !'
LawbotBossNeedMoreEvidence = 'Il te faut plus de preuves !'
LawbotBossDefenseWins1 = "Ce n'est pas possible ! La d\xc3\xa9fense a gagn\xc3\xa9 ?"
LawbotBossDefenseWins2 = 'Non. Je d\xc3\xa9clare le proc\xc3\xa8s nul ! Un nouveau proc\xc3\xa8s va \xc3\xaatre programm\xc3\xa9.'
LawbotBossDefenseWins3 = 'Hmmmpfff. Je serai dans mon cabinet !'
LawbotBossProsecutionWins = 'Je suis en faveur du plaignant'
LawbotBossReward = 'Je d\xc3\xa9cerne une promotion et le pouvoir de convoquer des Cogs'
LawbotBossLeaveCannon = 'Laisse le canon'
LawbotBossPassExam = 'Alors comme \xc3\xa7a, tu as r\xc3\xa9ussi le concours du barreau.'
LawbotBossTaunts = [
    "%s, je te trouve coupable d'outrage \xc3\xa0 la cour !",
    'Objection accord\xc3\xa9e !',
    'Rayez \xc3\xa7a du proc\xc3\xa8s-verbal.',
    'Ton appel a \xc3\xa9t\xc3\xa9 rejet\xc3\xa9. Je te condamne \xc3\xa0 la tristesse !',
    "Silence dans l'audience !"]
LawbotBossAreaAttackTaunt = "Vous \xc3\xaates tous coupables d'outrage \xc3\xa0 la cour!"
WitnessToonName = 'Bumpy Bourdonnette'
WitnessToonPrepareBattleTwo = "Oh non! Il n'y a que des Cogs dans le jury!\x7Vite, utilise les canons et tire sur des jur\xc3\xa9s Toons sur le banc des jur\xc3\xa9s.\x7Nous avons besoin de %d pour \xc3\xa9quilibrer la balance."
WitnessToonNoJuror = 'Oh l\xc3\xa0 l\xc3\xa0, aucun jur\xc3\xa9 Toon. \xc3\x87a va \xc3\xaatre un proc\xc3\xa8s difficile.'
WitnessToonOneJuror = 'Super! Il y a 1Toon parmi les jur\xc3\xa9s!'
WitnessToonSomeJurors = 'Super! Il y a %d Toons parmi les jur\xc3\xa9s!'
WitnessToonAllJurors = 'Fantastique! Tous les jur\xc3\xa9s sont des Toons!'
WitnessToonPrepareBattleThree = 'D\xc3\xa9p\xc3\xaache-toi de toucher la barre des t\xc3\xa9moins pour obtenir des preuves.\x7Appuie sur la touche \xc2\xabInser\xc2\xbb pour envoyer les preuves sur les avocats ou sur la d\xc3\xa9fense.'
WitnessToonCongratulations = 'Tu as r\xc3\xa9ussi! Merci pour cette d\xc3\xa9fense spectaculaire!\x7Prends ces papiers que le Juge a oubli\xc3\xa9s.\x7Avec \xc3\xa7a, tu pourras convoquer des Cogs \xc3\xa0 partir de ta page de Galerie de Cogs.'
WitnessToonLastPromotion = "\x7Wow, tu as atteint le niveau %s sur ton costume de Cog!\x7C'est la plus haute promotion que peuvent atteindre les Cogs.\x7Tu ne peux plus monter ton costume de Cog en grade, mais tu peux \xc3\xa9videmment continuer \xc3\xa0 travailler pour la r\xc3\xa9sistance!"
WitnessToonHPBoost = '\x7Tu as fait beaucoup de travail pour la r\xc3\xa9sistance.\x7Le Conseil des Toons a d\xc3\xa9cid\xc3\xa9 de te donner un autre rigolpoint. F\xc3\xa9licitations!'
WitnessToonMaxed = "\x7Je vois que tu as un costume de Cog de niveau %s. Tr\xc3\xa8s impressionnant!\x7Le Conseil des Toons te remercie d'\xc3\xaatre revenu d\xc3\xa9fendre encore plus de Toons!"
WitnessToonBonus = 'Merveilleux! Tous les avocats sont \xc3\xa9tourdis. Le poids de tes preuves est %s fois plus lourd pendant %s secondes.'
WitnessToonJuryWeightBonusSingular = {
    6: "C'est un cas difficile. Tu as %d jur\xc3\xa9 Toon. Par cons\xc3\xa9quent, tes preuves ont un bonus de poids de %d.",
    7: "C'est un cas tr\xc3\xa8s difficile. Tu as %d jur\xc3\xa9 Toon. Par cons\xc3\xa9quent, tes preuves ont un bonus de poids de %d.",
    8: "C'est le cas le plus difficile. Tu as %d jur\xc3\xa9 Toon. Par cons\xc3\xa9quent, tes preuves ont un bonus de poids de %d."}
WitnessToonJuryWeightBonusPlural = {
    6: "C'est un cas difficile. Tu as %d jur\xc3\xa9s Toon. Par cons\xc3\xa9quent, tes preuves ont un bonus de poids de %d.",
    7: "C'est un cas tr\xc3\xa8s difficile. Tu as %d jur\xc3\xa9s Toon. Par cons\xc3\xa9quent, tes preuves ont un bonus de poids de %d.",
    8: "C'est le cas le plus difficile. Tu as %d jur\xc3\xa9s Toon. Par cons\xc3\xa9quent, tes preuves ont un bonus de poids de %d."}
IssueSummons = 'Convocation'
SummonDlgTitle = 'Convoquer un Cog'
SummonDlgButton1 = 'Convoquer un Cog'
SummonDlgButton2 = 'Assigner un b\xc3\xa2timent Cog'
SummonDlgButton3 = 'Convoquer une invasion de Cogs'
SummonDlgSingleConf = 'Veux-tu convoquer un %s?'
SummonDlgBuildingConf = 'Veux-tu convoquer un %s \xc3\xa0 se rendre dans un b\xc3\xa2timent Toon \xc3\xa0 proximit\xc3\xa9?'
SummonDlgInvasionConf = 'Veux-tu convoquer une invasion de %s?'
SummonDlgNumLeft = "Il t'en reste %s."
SummonDlgDelivering = 'Envoi des convocations...'
SummonDlgSingleSuccess = 'Tu as r\xc3\xa9ussi \xc3\xa0 convoquer le Cog.'
SummonDlgSingleBadLoc = 'Malheureusement, les Cogs ne sont pas autoris\xc3\xa9s \xc3\xa0 entrer ici. Essaie un autre endroit.'
SummonDlgBldgSuccess = 'Tu as r\xc3\xa9ussi \xc3\xa0 convoquer les Cogs. %s a accept\xc3\xa9 de les laisser prendre provisoirement le contr\xc3\xb4le de %s!'
SummonDlgBldgSuccess2 = 'Tu as r\xc3\xa9ussi \xc3\xa0 convoquer les Cogs. Un commer\xc3\xa7ant a accept\xc3\xa9 de les laisser prendre provisoirement le contr\xc3\xb4le de son magasin!'
SummonDlgBldgBadLoc = "Malheureusement, il n'y a aucun b\xc3\xa2timent Toon \xc3\xa0 proximit\xc3\xa9 que les Cogs peuvent prendre."
SummonDlgInvasionSuccess = "Tu as r\xc3\xa9ussi \xc3\xa0 convoquer les Cogs. C'est une invasion!"
SummonDlgInvasionBusy = "On ne trouve pas de %s pour l'instant. Essaie \xc3\xa0 nouveau quand l'invasion de Cogs sera termin\xc3\xa9e."
SummonDlgInvasionFail = "D\xc3\xa9sol\xc3\xa9. L'invasion de Cogs a \xc3\xa9chou\xc3\xa9."
SummonDlgShopkeeper = 'Le commer\xc3\xa7ant'
PolarPlaceEffect1 = NPCToonNames[3306] + ': Bienvenue \xc3\xa0 la Place Polaire!'
PolarPlaceEffect2 = NPCToonNames[3306] + ': Essaie pour voir si la taille te va.'
PolarPlaceEffect3 = NPCToonNames[3306] + ': Ton nouveau look ne marchera que' + lTheBrrrgh + '.'
LaserGameMine = 'Recherche de cr\xc3\xa2ne!'
LaserGameRoll = 'Correspondance'
LaserGameAvoid = '\xc3\x89vite les cr\xc3\xa2nes'
LaserGameDrag = 'Mets en trois de la m\xc3\xaame\ncouleur sur une rang\xc3\xa9e'
LaserGameDefault = 'Jeu inconnu'
PinballHiScore = 'Score \xc3\xa9lev\xc3\xa9: %s\n'
PinballHiScoreAbbrev = '...'
PinballYourBestScore = 'Ton meilleur score:\n'
PinballScore = 'Score: %d x %d ='
PinballScoreHolder = '%s\n'
GagTreeFeather = 'Arbre \xc3\xa0 gags \xc3\xa0 plumes'
GagTreeJugglingBalls = 'Arbre \xc3\xa0 gags \xc3\xa0 balles de jonglage'
StatuaryFountain = 'Fontaine'
StatuaryToonStatue = 'Statue de Toon'
StatuaryDonald = 'Statue de Donald'
StatuaryMinnie = 'Statue de Minnie'
StatuaryMickey1 = 'Statue de Mickey'
StatuaryMickey2 = 'Fontaine de Mickey'
StatuaryGardenAccelerator = 'Engrais Pousse-Instantan\xc3\xa9e'
FlowerColorStrings = [
    'Rouge',
    'Orange',
    'Violet',
    'Bleu',
    'Rose',
    'Jaune',
    'Blanc',
    'Vert']
FlowerSpeciesNames = {
    49: 'P\xc3\xa2querette',
    50: 'Tulipe',
    51: '\xc5\x92illet',
    52: 'Lys',
    53: 'Jonquille',
    54: 'Pens\xc3\xa9e',
    55: 'P\xc3\xa9tunia',
    56: 'Rose'}
FlowerFunnyNames = {
    49: ("P\xc3\xa2querette d'\xc3\xa9cole", 'P\xc3\xa2querette paresseuse', "P\xc3\xa2querette d'\xc3\xa9t\xc3\xa9",
         'P\xc3\xa2querette frisquette', 'P\xc3\xa2querette houpl\xc3\xa0l\xc3\xa0', 'P\xc3\xa2querette guillerette',
         'P\xc3\xa2querette follette', 'P\xc3\xa2querette brumette'),
    50: ('Unelipe', 'Tulipe', 'Trilipe'),
    51: ('\xc5\x92illet myope', '\xc5\x92illet rapide', '\xc5\x92illet hybride', '\xc5\x92illet louche',
         '\xc5\x92illet mod\xc3\xa8le'),
    52: (
    'Mugatine', 'Lys t\xc3\xa9ria', 'Lys tigri', 'Lys poire', 'Lys pique', 'Pneu-lys', 'Lys t\xc3\xa8re', 'Lys bis'),
    53: ('Jonquirille', 'Jonquifolle', 'Jonquirafe', 'Jonquipasse'),
    54: (
    'Pens\xc3\xa9e \xc3\xa0 rien', 'Chim-pens\xc3\xa9e', 'Pens\xc3\xa9e zy', 'Pensargarine', 'Pens\xc3\xa9e folle'),
    55: ('P\xc3\xa9tugniagnian', 'R\xc3\xa9gitunia'),
    56: ('Rose estivale', 'Rose des bl\xc3\xa9s', 'Rose colorante', 'Rose malodorante', 'Rose distill\xc3\xa9e')}
FlowerVarietyNameFormat = '%s %s'
FlowerUnknown = '????'
ShovelNameDict = {
    0: '\xc3\x89tain',
    1: 'Bronze',
    2: 'Argent',
    3: 'Or'}
WateringCanNameDict = {
    0: 'Petit',
    1: 'Moyen',
    2: 'Grand',
    3: '\xc3\x89norme'}
GardeningPlant = 'Plante'
GardeningWater = 'Eau'
GardeningRemove = 'Retirer'
GardeningPick = 'Cueillir'
GardeningFull = 'Full'
GardeningSkill = 'Habilet\xc3\xa9'
GardeningWaterSkill = 'Habilet\xc3\xa9 \xc3\xa0 arroser'
GardeningShovelSkill = 'Habilet\xc3\xa9 avec la pelle'
GardeningNoSkill = "Pas d'habilet\xc3\xa9 am\xc3\xa9lior\xc3\xa9e"
GardeningPlantFlower = 'Plante\nFleur'
GardeningPlantTree = 'Plante\nArbre'
GardeningPlantItem = 'Plante\nArticle'
PlantingGuiOk = 'Plante'
PlantingGuiCancel = 'Annuler'
PlantingGuiReset = 'Tout effacer'
GardeningChooseBeans = 'Choisis les bonbons que tu veux planter'
GardeningChooseBeansItem = 'Choisis les bonbons que tu veux planter.'
GardenShovelLevelUp = 'F\xc3\xa9licitations, tu as gagn\xc3\xa9 une pelle %(shovel)s! Tu as ma\xc3\xaetris\xc3\xa9 les fleurs de %(oldbeans)d bonbons! Pour avancer, tu dois cueillir des fleurs de %(newbeans)d bonbons.'
GardenShovelSkillLevelUp = 'F\xc3\xa9licitations! Tu as ma\xc3\xaetris\xc3\xa9 les fleurs de %(oldbeans)d bonbons! Pour avancer, tu dois cueillir des fleurs de %(newbeans)d bonbons.'
GardenShovelSkillMaxed = 'Extraordinaire! Tu as explos\xc3\xa9 ton habilet\xc3\xa9 avec la pelle!'
GardenWateringCanLevelUp = 'F\xc3\xa9licitations, tu as gagn\xc3\xa9 un nouvel arrosoir!'
GardenMiniGameWon = 'F\xc3\xa9licitations, tu as arros\xc3\xa9 la plante!'
ShovelTin = "Pelle d'\xc3\xa9tain"
ShovelSteel = 'Pelle de bronze'
ShovelSilver = "Pelle d'argent"
ShovelGold = "Pelle d'or"
WateringCanSmall = 'Petit arrosoir'
WateringCanMedium = 'Arrosoir moyen'
WateringCanLarge = 'Grand arrosoir'
WateringCanHuge = '\xc3\x89norme arrosoir'
BeanColorWords = ('rouge', 'vert', 'orange', 'violet', 'bleu', 'rose', 'jaune', 'bleu de cyan', 'argent\xc3\xa9')
PlantItWith = ' Plante avec %s.'
MakeSureWatered = " Prends d'abord soin d`arroser toutes tes plantes."
UseFromSpecialsTab = 'Utilise les onglets sp\xc3\xa9ciaux de ta page de jardinage.'
UseSpecial = "Utilise l'outil sp\xc3\xa9cial"
UseSpecialBadLocation = 'Tu ne peux utiliser cela que dans ton jardin.'
UseSpecialSuccess = 'Bravo! Les plantes que tu as arros\xc3\xa9es viennent de pousser.'
ConfirmWiltedFlower = "Le plant de %(plant)s est fan\xc3\xa9. Veux-tu vraiment le retirer? Ce plant n'ira pas dans ton panier de fleurs, et ton habilet\xc3\xa9 n'augmentera pas."
ConfirmUnbloomingFlower = "Le plant de %(plant)s ne fleurit pas. Veux-tu vraiment le retirer? Ce plant n'ira pas dans ton panier de fleurs, et ton habilet\xc3\xa9 n'augmentera pas."
ConfirmNoSkillupFlower = "Veux-tu vraiment cueillir le plant de %(plant)s? Ce plant ira dans ton panier de fleurs, mais ton habilet\xc3\xa9 n'augmentera PAS."
ConfirmSkillupFlower = 'Veux-tu vraiment cueillir le plant de %(plant)s? Il ira dans ton panier de fleurs. Ton habilet\xc3\xa9 augmentera aussi.'
ConfirmMaxedSkillFlower = "Veux-tu vraiment cueillir le plant de %(plant)s? Il ira dans ton panier de fleurs. Ton habilet\xc3\xa9 n'augmentera PAS car elle est d\xc3\xa9j\xc3\xa0 au maximum."
ConfirmBasketFull = "Ton panier de fleurs est plein. Tu dois d'abord vendre des fleurs."
ConfirmRemoveTree = 'Veux-tu vraiment retirer le pied de %(tree)s?'
ConfirmWontBeAbleToHarvest = ' Si tu retires cet arbre, tu ne pourras pas r\xc3\xa9colter de gags dans les arbres de plus haut niveau.'
ConfirmRemoveStatuary = 'Veux-tu vraiment supprimer d\xc3\xa9finitivement le plant de %(item)s?'
ResultPlantedSomething = 'F\xc3\xa9licitations ! Tu viens de planter un %s.'
ResultPlantedSomethingAn = 'F\xc3\xa9licitations ! Tu viens de mettre en terre un plant de %s.'
ResultPlantedNothing = "\xc3\x87a n'a pas march\xc3\xa9. Essaie une nouvelle combinaison de bonbons."
GardenGagTree = 'Arbre \xc3\xa0 gags'
GardenUberGag = '\xc3\x9cber Gag'


def getRecipeBeanText(beanTuple):
    retval = ''
    if not beanTuple:
        return retval

    allTheSame = True
    for index in range(len(beanTuple)):
        if index + 1 < len(beanTuple):
            if not beanTuple[index] == beanTuple[index + 1]:
                allTheSame = False
                break

        beanTuple[index] == beanTuple[index + 1]

    if allTheSame:
        if len(beanTuple) > 1:
            retval = '%d bonbons %s' % (len(beanTuple), BeanColorWords[beanTuple[0]])
        else:
            retval = 'un bonbon %s' % BeanColorWords[beanTuple[0]]
    else:
        retval += 'un'
        maxBeans = len(beanTuple)
        for index in range(maxBeans):
            if index == maxBeans - 1:
                retval += ' et un bonbon %s' % BeanColorWords[beanTuple[index]]
                continue
            if index == 0:
                retval += ' %s' % BeanColorWords[beanTuple[index]]
                continue
            retval += ', %s' % BeanColorWords[beanTuple[index]]

    return retval


GardenTextMagicBeans = 'Bonbons magiques'
GardenTextMagicBeansB = 'Quelques autres bonbons'
GardenSpecialDiscription = 'Ce texte doit expliquer comment utiliser un certain outil sp\xc3\xa9cial pour le jardin'
GardenSpecialDiscriptionB = 'Ce texte doit expliquer comment utiliser un certain outil sp\xc3\xa9cial pour le jardin, en pleine face !'
GardenTrophyAwarded = 'Oh l\xc3\xa0 l\xc3\xa0! Tu as cueilli %s sur %s fleurs. \xc3\x87a m\xc3\xa9rite un troph\xc3\xa9e et une rigol-augmentation!'
GardenTrophyNameDict = {
    0: 'Brouette',
    1: 'Pelles',
    2: 'Fleur',
    3: 'Arrosoir',
    4: 'Requin',
    5: 'Poisson-scie',
    6: 'Orque'}
SkillTooLow = 'Habilet\xc3\xa9\ntrop faible'
NoGarden = 'Pas de\njardins'


def isVowelStart(str):
    retval = False
    if str and len(str) > 0:
        vowels = [
            'A',
            'E',
            'I',
            'O',
            'U']
        firstLetter = str.upper()[0:1]
        if firstLetter in vowels:
            retval = True

    return retval


def getResultPlantedSomethingSentence(flowerName):
    if isVowelStart(flowerName):
        retval = ResultPlantedSomethingAn % flowerName
    else:
        retval = ResultPlantedSomething % flowerName
    return retval


TravelGameTitle = 'Les Jeudis du Tramway'
TravelGameInstructions = 'Clique vers le haut ou vers le bas pour d\xc3\xa9finir ton nombre de votes. Clique sur le bouton pour voter. Atteins ton objectif secret pour remporter des bonus de bonbons. Gagne plus de votes en obtenant de bons r\xc3\xa9sultats dans les autres jeux.'
TravelGameRemainingVotes = 'Votes restants :'
TravelGameUse = 'Utiliser'
TravelGameVotesWithPeriod = 'votes.'
TravelGameVotesToGo = 'votes restants'
TravelGameVoteToGo = 'votes restants'
TravelGameUp = 'HAUT'
TravelGameDown = 'BAS.'
TravelGameVoteWithExclamation = 'Vote !'
TravelGameWaitingChoices = 'Attendre que les autres joueurs votent...'
TravelGameDirections = [
    'HAUT',
    'BAS']
TravelGameTotals = 'Totaux'
TravelGameReasonVotesPlural = 'Le tramway se dirige vers le %(dir)s, avec une avance de %(numVotes)d votes.'
TravelGameReasonVotesSingular = 'Le tramway se dirige vers le %(dir)s, avec une avance de %(numVotes)d vote.'
TravelGameReasonPlace = '%(name)s brise le lien. Le tramway se dirige vers le %(dir)s.'
TravelGameReasonRandom = 'Le tramway se dirige de mani\xc3\xa8re al\xc3\xa9atoire vers le %(dir)s.'
TravelGameOneToonVote = '%(name)s a utilis\xc3\xa9 %(numVotes)s votes restants %(dir)s\n'
TravelGameBonusBeans = '%(numBeans)d Bonbons'
TravelGamePlaying = 'Ensuite, le %(game)s Jeu du Tramway.'
TravelGameGotBonus = '%(name)s a obtenu un bonus de %(numBeans)s bonbons !'
TravelGameNoOneGotBonus = "Personne n'a atteint son objectif secret. Chacun remporte 1 bonbon."
TravelGameConvertingVotesToBeans = ''
TravelGameGoingBackToShop = 'Il reste un seul joueur. En route pour la boutique \xc3\xa0 gags de Dingo.'
PairingGameTitle = 'Jeu de m\xc3\xa9moire Toon'
PairingGameInstructions = "Appuie sur Effacer pour ouvrir une carte. Pour remporter un point, il faut assortir deux cartes. Fais une combinaison avec l'\xc3\xa9clat bonus et remporte un point en plus. Remporte des points suppl\xc3\xa9mentaires en effectuant de petits lancers."
PairingGameInstructionsMulti = "Appuie sur Effacer pour ouvrir une carte. Appuie sur Ctrl pour demander \xc3\xa0 un autre joueur d'ouvrir une carte. Pour remporter un point, il faut assortir deux cartes. Fais une combinaison avec l'\xc3\xa9clat bonus et remporte un point en plus. Remporte des points suppl\xc3\xa9mentaires en effectuant de petits lancers."
PairingGamePerfect = 'PARFAIT !'
PairingGameFlips = 'Lancers :'
PairingGamePoints = 'Points :'
TrolleyHolidayStart = "Les Jeudis du Tramway est sur le point de commencer. Pour jouer, monte \xc3\xa0 bord de n'importe quel tramway contenant au moins deux Toons."
TrolleyHolidayOngoing = "Bienvenue ! Les Jeudis du Tramway est en cours d'ex\xc3\xa9cution."
TrolleyHolidayEnd = "Les Jeudis du Tramway est termin\xc3\xa9 pour aujourd'hui. \xc3\x80 la semaine prochaine !"
TrolleyWeekendStart = "Le Weekend du Tramway est sur le point de commencer ! Pour jouer, monte \xc3\xa0 bord de n'importe quel tramway contenant au moins deux Toons."
TrolleyWeekendEnd = "Le Weekend du Tramway est termin\xc3\xa9 pour aujourd'hui."
VineGameTitle = 'Jeu des Lianes'
VineGameInstructions = 'Atteins la liane la plus \xc3\xa0 droite \xc3\xa0 temps. Appuie sur les fl\xc3\xa8ches Haut ou Bas du clavier pour grimper le long de la liane. Appuie sur les fl\xc3\xa8ches Droite ou Gauche pour changer de direction et sauter. Plus tu es en bas de la liane, plus il est facile de sauter. Ramasse les bananes si tu peux, mais \xc3\xa9vite les chauves-souris et les araign\xc3\xa9es.'
