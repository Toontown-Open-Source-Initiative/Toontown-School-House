# File: T (Python 2.4)

import string
import time
from toontown.toonbase.TTLocalizer_portuguese_Property import *
ExtraKeySanityCheck = 'Ignore-me'
commitmanString = 'bugfix! I changed this'
commitmanSting2 = 'another string!'
commitmantst = 'kptmptest - removable'
InterfaceFont = 'phase_3/models/fonts/ImpressBT.ttf'
ToonFont = 'phase_3/models/fonts/ImpressBT.ttf'
SuitFont = 'phase_3/models/fonts/HGHanKointai.ttc'
SignFont = 'phase_3/models/fonts/MickeyFont'
MinnieFont = 'phase_3/models/fonts/MinnieFont'
FancyFont = 'phase_3/models/fonts/Comedy'
NametagFonts = ('phase_3/models/fonts/AnimGothic', 'phase_3/models/fonts/Aftershock', 'phase_3/models/fonts/JiggeryPokery', 'phase_3/models/fonts/Ironwork', 'phase_3/models/fonts/HastyPudding', 'phase_3/models/fonts/Comedy', 'phase_3/models/fonts/Humanist', 'phase_3/models/fonts/Portago', 'phase_3/models/fonts/Musicals', 'phase_3/models/fonts/Scurlock', 'phase_3/models/fonts/Danger', 'phase_3/models/fonts/Alie', 'phase_3/models/fonts/OysterBar', 'phase_3/models/fonts/RedDogSaloon')
NametagFontNames = ('Usu\xc3\xa1rio', 'Tremido', 'Arrepiante', 'Exorbitante', 'Bobo', 'Doido', 'Pratico', 'Nautico', 'Caprichoso', 'Estremecer', 'A\xc3\xa7\xc3\xa3o', 'Po\xc3\xa9tico', 'Passeio', 'Ocidental')
NametagLabel = 'Nome'
UnpaidNameTag = 'Basico'
GM_1 = 'CONSELHO TOON'
GM_2 = 'TROPA TOON'
GM_3 = 'SOLDADO DA RESIST\xc3\x8aNCIA'
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
Daisy = 'Margarida'
SockHopDaisy = 'SockHopDaisy'
Goofy = 'Pateta'
SuperGoofy = 'SuperGoofy'
Pluto = 'Pluto'
WesternPluto = 'WesternPluto'
Flippy = 'Flippy'
Chip = 'Tico'
Dale = 'Teco'
JailbirdDale = 'P\xc3\xa1ssaro de cadeia Teco'
PoliceChip = 'Pol\xc3\xadcia Tico'
lTheBrrrgh = 'O Brrrgh'
lDaisyGardens = 'Jardim da Margarida'
lDonaldsDock = 'Porto do Donald'
lDonaldsDreamland = 'Sonhol\xc3\xa2ndia do Donald'
lMinniesMelodyland = 'Melodil\xc3\xa2ndia da Minnie'
lToontownCentral = 'Centro de Toontown'
lToonHQ = 'Quartel dos Toons'
lSellbotHQ = 'Quartel do Rob\xc3\xb4 Vendedor'
lGoofySpeedway = 'Aut\xc3\xb3dromo do Pateta'
lOutdoorZone = 'Bosque de Bolotas de Tico e Teco'
lGolfZone = 'Minigolfe de Tico e Teco'
lPartyHood = 'Terra do Festas'
GlobalStreetNames = {
    20000: ('para o', 'no', 'Terra\xc3\xa7o do Tutorial'),
    1000: ('para o', 'no', 'Parque'),
    1100: ('para o', 'no', 'Boulevard das Cracas'),
    1200: ('para a', 'na', 'Rua da Alga Marinha'),
    1300: ('para a', 'na', 'Travessa do Farol'),
    2000: ('para o', 'no', 'Parque'),
    2100: ('para a', 'na', 'Rua da Bobeira'),
    2200: ('para a', 'na', 'Travessa dos Tontos'),
    2300: ('para o', 'no', 'Largo do Auge da Gra\xc3\xa7a'),
    3000: ('para o', 'no', 'Parque'),
    3100: ('para a', 'na', 'Via dos Le\xc3\xb5es Marinhos'),
    3200: ('para a', 'na', 'Rua da Chuva de Neve'),
    3300: ('para o', 'no', 'Lugar Polar'),
    4000: ('para o', 'no', 'Parque'),
    4100: ('para a', 'na', 'Avenida do Tom Alto'),
    4200: ('para o', 'no', 'Boulevard do Bar\xc3\xadtono'),
    4300: ('para o', 'no', 'Terra\xc3\xa7o do Tenor'),
    5000: ('para o', 'no', 'Parque'),
    5100: ('para a', 'na', 'Rua das Nogueiras'),
    5200: ('para a', 'na', 'Rua das Amendoeiras'),
    5300: ('para a', 'na', 'Rua dos Carvalhos'),
    9000: ('para o', 'no', 'Parque'),
    9100: ('para a', 'na', 'Travessa da Can\xc3\xa7\xc3\xa3o de Ninar'),
    9200: ('para o', 'no', 'Alameda do Pijama'),
    10000: ('', '', ''),
    10100: ('para o', 'no', 'Sal\xc3\xa3o do Quartel do Rob\xc3\xb4-chefe'),
    10200: ('para a', 'na', 'Sede do Clube'),
    10500: ('para o', 'no', 'Tr\xc3\xaas da Frente'),
    10600: ('para o', 'no', 'Seis do Meio'),
    10700: ('para o', 'no', 'Nove de Tr\xc3\xa1s'),
    11000: ('', '', ''),
    11100: ('para o', 'no', 'Sal\xc3\xa3o do ' + lSellbotHQ),
    11200: ('para a', 'na', 'F\xc3\xa1brica do Rob\xc3\xb4 Vendedor'),
    11500: ('para a', 'na', 'F\xc3\xa1brica do Rob\xc3\xb4 Vendedor'),
    12000: ('', '', ''),
    12100: ('para o', 'no', 'Sal\xc3\xa3o do Quartel do Rob\xc3\xb4 Mercen\xc3\xa1rio'),
    12500: ('para a', 'na', 'Casa da Moeda'),
    12600: ('para a', 'na', 'Casa da Moeda de D\xc3\xb3lar'),
    12700: ('para a', 'na', 'Casa da Moeda de Barras de Ouro'),
    13000: ('', '', ''),
    13100: ('para o', 'no', 'Sal\xc3\xa3o do Quartel do Rob\xc3\xb4 da Lei'),
    13200: ('para o', 'no', 'Lobby do Escrit\xc3\xb3rio do Promotor'),
    13300: ('para o', 'no', 'Escrit\xc3\xb3rio da Lei A'),
    13400: ('para o', 'no', 'Escrit\xc3\xb3rio da Lei B'),
    13500: ('para o', 'no', 'Escrit\xc3\xb3rio da Lei C'),
    13600: ('para o', 'no', 'Escrit\xc3\xb3rio da Lei D') }
DonaldsDock = ('para o', 'no', lDonaldsDock)
ToontownCentral = ('para o', 'no', lToontownCentral)
TheBrrrgh = ('para', 'em', lTheBrrrgh)
MinniesMelodyland = ('para a', 'na', lMinniesMelodyland)
DaisyGardens = ('para os', 'nos', lDaisyGardens)
OutdoorZone = ('para a', 'na', lOutdoorZone)
FunnyFarm = ('para a', 'na', 'Fazenda Divertida')
GoofySpeedway = ('para o', 'no', lGoofySpeedway)
DonaldsDreamland = ('para a', 'na', lDonaldsDreamland)
BossbotHQ = ('para o', 'no', 'Quartel do Rob\xc3\xb4-chefe')
SellbotHQ = ('para o', 'no', lSellbotHQ)
CashbotHQ = ('para o', 'no', 'Quartel do Rob\xc3\xb4 Mercen\xc3\xa1rio')
LawbotHQ = ('para o', 'no', 'Quartel do Rob\xc3\xb4 da Lei')
Tutorial = ('para o', 'no', 'Toon-torial')
MyEstate = ('para a', 'na', 'sua casa')
WelcomeValley = ('para o', 'no', 'Vale Boas-vindas')
GolfZone = ('para a', 'na', lGolfZone)
PartyHood = ('para a', 'na', lPartyHood)
Factory = 'F\xc3\xa1brica'
Headquarters = 'Quartel'
SellbotFrontEntrance = 'Entrada principal'
SellbotSideEntrance = 'Entrada lateral'
Office = 'Escrit\xc3\xb3rio'
FactoryNames = {
    0: 'Molde da f\xc3\xa1brica',
    11500: 'F\xc3\xa1brica do Cog Rob\xc3\xb4 Vendedor',
    13300: 'Escrit\xc3\xb3rio de Cogs Policiais' }
FactoryTypeLeg = 'Perna'
FactoryTypeArm = 'Bra\xc3\xa7o'
FactoryTypeTorso = 'Busto'
MintFloorTitle = 'Andar %s'
lCancel = 'Cancelar'
lClose = 'Fechar'
lOK = 'OK'
lNext = 'Pr\xc3\xb3ximo'
lQuit = 'Sair'
lYes = 'Sim'
lNo = 'N\xc3\xa3o'
sleep_auto_reply = '%s is sleeping right now'
lHQOfficerF = 'Oficial do Quartel'
lHQOfficerM = 'Oficial do Quartel'
MickeyMouse = 'Mickey Mouse'
AIStartDefaultDistrict = 'Vila dos Idiotas'
Cog = 'Cog'
Cogs = 'Cogs'
ACog = 'um Cog'
TheCogs = 'os Cogs'
ASkeleton = 'um Esqueletocog'
Skeleton = 'Esqueletocogs'
SkeletonP = 'Esqueletocogs'
Av2Cog = 'um Cog Vers\xc3\xa3o 2.0'
v2Cog = 'Cog Vers\xc3\xa3o 2.0'
v2CogP = 'Cogs Vers\xc3\xa3o 2.0'
ASkeleton = 'um Esqueletocog'
Foreman = 'Supervisor da f\xc3\xa1brica'
ForemanP = 'Supervisores da f\xc3\xa1brica'
AForeman = 'um Supervisor da f\xc3\xa1brica'
CogVP = Cog + ' VP'
CogVPs = 'Cogs VPs'
ACogVP = ACog + ' VP'
Supervisor = 'Supervisor da Casa da Moeda'
SupervisorP = 'Supervisores da Casa da Moeda'
ASupervisor = 'um Supervisor da Casa da Moeda'
CogCFO = Cog + 'Diretor Financeiro'
CogCFOs = 'Diretores Financeiros Cogs'
ACogCFO = ACog + 'Diretor Financeiro'
TheFish = 'o Peixe'
AFish = 'um peixe'
Level = 'n\xc3\xadvel'
QuestsCompleteString = 'Concluir'
QuestsNotChosenString = 'N\xc3\xa3o escolhido'
Period = '.'
Laff = 'Risada'
QuestInLocationString = ' %(inPhrase)s %(location)s'
QuestsDefaultGreeting = ('Ol\xc3\xa1, _avName_!', 'Oi, _avName_!', 'E a\xc3\xad, _avName_?', 'Diga a\xc3\xad, _avName_!', 'Bem-vindo, _avName_!', 'Tudo certo, _avName_?', 'Como vai voc\xc3\xaa, _avName_?', 'Ol\xc3\xa1 _avName_!')
QuestsDefaultIncomplete = ('Como est\xc3\xa1 indo aquela tarefa, _avName_?', 'Parece que voc\xc3\xaa ainda tem mais trabalho a fazer naquela tarefa!', 'Continue com o bom trabalho, _avName_!', 'Continue tentando concluir aquela tarefa. Eu sei que voc\xc3\xaa consegue!', 'Continue tentando concluir a tarefa. Contamos com voc\xc3\xaa!', 'Continue trabalhando naquela Tarefa Toon!')
QuestsDefaultIncompleteProgress = ('Voc\xc3\xaa veio ao lugar certo, mas, primeiramente, precisa concluir sua Tarefa Toon.', 'Ao terminar a Tarefa Toon, volte aqui.', 'Volte quando tiver terminado sua Tarefa Toon.')
QuestsDefaultIncompleteWrongNPC = ('Bom trabalho naquela Tarefa Toon. Voc\xc3\xaa deveria visitar _toNpcName_._where_', 'Parece que voc\xc3\xaa est\xc3\xa1 pronto para concluir sua Tarefa Toon. V\xc3\xa1 ver _toNpcName_._where_.', 'V\xc3\xa1 ver _toNpcName_ para concluir sua Tarefa Toon._where_')
QuestsDefaultComplete = ('Bom trabalho! Aqui est\xc3\xa1 a sua recompensa...', '\xc3\x93timo trabalho, _avName_! Tome esta recompensa...', 'Excelente trabalho, _avName_! Aqui est\xc3\xa1 a sua recompensa...')
QuestsDefaultLeaving = ('Tchau!', 'At\xc3\xa9 logo!', 'At\xc3\xa9 mais, _avName_.', 'Te vejo por a\xc3\xad, _avName_!', 'Boa sorte!', 'Divirta-se em Toontown!', 'Vejo voc\xc3\xaa depois!')
QuestsDefaultReject = ('Ol\xc3\xa1.', 'Posso ajudar?', 'Como vai voc\xc3\xaa?', 'E a\xc3\xad, pessoal?', 'Estou um pouco ocupado agora, _avName_.', 'Sim?', 'Tudo certo, _avName_!', 'Bem-vindo, _avName_!', 'Ei, _avName_! Tudo bem?', 'Voc\xc3\xaa sabia que pode abrir seu \xc3\x81lbum Toon clicando em F8?', 'Voc\xc3\xaa pode usar seu mapa para se teletransportar de volta ao p\xc3\xa1tio!', 'Voc\xc3\xaa pode ficar amigo de outros jogadores clicando neles.', 'Voc\xc3\xaa pode descobrir mais sobre um ' + Cog + ' clicando nele.', 'Junte tesouros nos p\xc3\xa1tios para encher seu Ris\xc3\xb4metro.', 'Os edif\xc3\xadcios ' + Cog + ' s\xc3\xa3o lugares perigosos! N\xc3\xa3o entre neles sozinho!', 'Quando voc\xc3\xaa perde uma batalha, os ' + Cogs + ' tomam todas as suas piadas.', 'Para obter mais piadas, jogue no Bondinho!', 'Voc\xc3\xaa pode obter mais Pontos de risadas completando as Tarefas Toon.', 'Toda Tarefa Toon d\xc3\xa1 uma recompensa a voc\xc3\xaa.', 'Algumas recompensas permitem que voc\xc3\xaa carregue consigo mais Piadas.', 'Se voc\xc3\xaa vencer uma batalha, ganhar\xc3\xa1 cr\xc3\xa9ditos de Tarefa Toon para cada ' + Cog + ' derrotado.', 'Se voc\xc3\xaa recuperar um edif\xc3\xadcio ' + Cog + ', entre e ver\xc3\xa1 um agradecimento especial do propriet\xc3\xa1rio!', 'Se pressionar a tecla Page Up, poder\xc3\xa1 ver acima de voc\xc3\xaa!', 'Se voc\xc3\xaa pressionar a tecla Tab, poder\xc3\xa1 ver os arredores sob diversos \xc3\xa2ngulos!', "Para mostrar aos amigos secretos o que est\xc3\xa1 pensando, coloque '.' antes do pensamento.", 'Se um ' + Cog + ' estiver atordoado, ser\xc3\xa1 mais dif\xc3\xadcil para ele desviar de objetos cadentes.', 'Cada tipo de edif\xc3\xadcio ' + Cog + ' possui um visual diferente.', 'Derrotar os ' + Cogs + ' nos andares mais altos de um edif\xc3\xadcio dar\xc3\xa1 a voc\xc3\xaa maiores recompensas de habilidade.')
QuestsDefaultTierNotDone = ('Ol\xc3\xa1, _avName_! Voc\xc3\xaa deve concluir sua Tarefa Toon atual antes de come\xc3\xa7ar uma nova.', 'E a\xc3\xad? Voc\xc3\xaa precisa concluir suas Tarefas Toon atuais antes de come\xc3\xa7ar uma nova.', 'Oi, _avName_! Para que eu possa dar a voc\xc3\xaa uma nova Tarefa Toon, voc\xc3\xaa precisa terminar as que voc\xc3\xaa tem.')
QuestsDefaultQuest = None
QuestsDefaultVisitQuestDialog = ('Ouvi falar que _toNpcName_ est\xc3\xa1 procurando por voc\xc3\xaa._where_', 'Passe por l\xc3\xa1 e visite _toNpcName_ quando tiver um tempinho._where_', 'Visite _toNpcName_ da pr\xc3\xb3xima vez em que estiver passando por aquele caminho._where_', 'Se tiver um tempinho, pare e diga ol\xc3\xa1 para _toNpcName_._where_', '_toNpcName_ dar\xc3\xa1 a voc\xc3\xaa sua nova Tarefa Toon._where_')
QuestsLocationArticle = ''

def getLocalNum(num):
    if num <= 9:
        return str(num) + ''
    else:
        return str(num)

QuestsItemNameAndNum = '%(num)s %(name)s'
QuestsCogQuestProgress = '%(progress)s de %(numCogs)s derrotados'
QuestsCogQuestHeadline = 'PROCURADO'
QuestsCogQuestSCStringS = 'Eu preciso derrotar %(cogName)s%(cogLoc)s'
QuestsCogQuestSCStringP = 'Eu preciso derrotar alguns %(cogName)s%(cogLoc)s.'
QuestsCogQuestDefeat = 'Derrotar %s'
QuestsCogQuestDefeatDesc = '%(numCogs)s %(cogName)s'
QuestsCogNewNewbieQuestObjective = 'Ajude um novo Toon a derrotar %s'
QuestsCogNewNewbieQuestCaption = 'Ajude um novo Toon que tenha %d risadas ou menos que isso'
QuestsCogOldNewbieQuestObjective = 'Ajude um Toon com %(laffPoints)d risadas, ou menos, a dominar %(objective)s'
QuestsCogOldNewbieQuestCaption = 'Ajude um Toon com %d risadas, ou menos'
QuestsCogNewbieQuestAux = 'Derrotar:'
QuestsNewbieQuestHeadline = 'APRENDIZ'
QuestsCogTrackQuestProgress = '%(progress)s de %(numCogs)s derrotados'
QuestsCogTrackQuestHeadline = 'PROCURADO'
QuestsCogTrackQuestSCStringS = 'Eu preciso derrotar %(cogText)s%(cogLoc)s.'
QuestsCogTrackQuestSCStringP = 'Eu preciso derrotar alguns %(cogText)s%(cogLoc)s.'
QuestsCogTrackQuestDefeat = 'Derrotar %s'
QuestsCogTrackDefeatDesc = '%(numCogs)s %(trackName)s'
QuestsCogLevelQuestProgress = '%(progress)s de %(numCogs)s derrotados'
QuestsCogLevelQuestHeadline = 'PROCURADO'
QuestsCogLevelQuestDefeat = 'Derrotar %s'
QuestsCogLevelQuestDesc = 'um N\xc3\xadvel %(level)s+ Cog'
QuestsCogLevelQuestDescC = '%(count)s N\xc3\xadvel %(level)s+ Cogs'
QuestsCogLevelQuestDescI = 'algum N\xc3\xadvel %(level)s+ Cogs'
QuestsCogLevelQuestSCString = 'Eu preciso derrotar %(objective)s%(location)s.'
QuestsBuildingQuestFloorNumbers = ('', 'dois+', 'tr\xc3\xaas+', 'quatro+', 'cinco+')
QuestsBuildingQuestBuilding = 'Edif\xc3\xadcio'
QuestsBuildingQuestBuildings = 'Edif\xc3\xadcios'
QuestsBuildingQuestHeadline = 'DERROTAR'
QuestsBuildingQuestProgressString = '%(progress)s de %(num)s derrotados'
QuestsBuildingQuestString = 'Derrotar %s'
QuestsBuildingQuestSCString = 'Eu preciso derrotar %(objective)s%(location)s.'
QuestsBuildingQuestDesc = 'um Edif\xc3\xadcio %(type)s'
QuestsBuildingQuestDescF = 'um Edif\xc3\xadcio %(type)s de %(floors)s andares'
QuestsBuildingQuestDescC = '%(count)s Edif\xc3\xadcios %(type)s'
QuestsBuildingQuestDescCF = '%(count)s Edif\xc3\xadcios %(type)s de %(floors)s andares'
QuestsBuildingQuestDescI = 'alguns Edif\xc3\xadcios %(type)s'
QuestsBuildingQuestDescIF = 'alguns Edif\xc3\xadcios %(type)s de %(floors)s andares'
QuestFactoryQuestFactory = 'F\xc3\xa1brica'
QuestsFactoryQuestFactories = 'F\xc3\xa1bricas'
QuestsFactoryQuestHeadline = 'DERROTAR'
QuestsFactoryQuestProgressString = '%(progress)s de %(num)s derrotados'
QuestsFactoryQuestString = 'Derrotar %s'
QuestsFactoryQuestSCString = 'Eu preciso derrotar %(objective)s%(location)s.'
QuestsFactoryQuestDesc = 'uma F\xc3\xa1brica %(type)s'
QuestsFactoryQuestDescC = '%(count)s F\xc3\xa1bricas %(type)s'
QuestsFactoryQuestDescI = 'algumas F\xc3\xa1bricas %(type)s'
QuestMintQuestMint = 'Casa da Moeda'
QuestsMintQuestMints = 'Casas da Moeda'
QuestsMintQuestHeadline = 'DERROTAR'
QuestsMintQuestProgressString = '%(progress)s de %(num)s derrotados'
QuestsMintQuestString = 'Derrotar %s'
QuestsMintQuestSCString = 'Preciso derrotar %(objective)s%(location)s.'
QuestsMintQuestDesc = 'uma Casa da Moeda dos Cogs'
QuestsMintQuestDescC = '%(count)s Casas da Moeda dos Cogs'
QuestsMintQuestDescI = 'algumas Casas da Moeda dos Cogs'
QuestsRescueQuestProgress = '%(progress)s de %(numToons)s salvos'
QuestsRescueQuestHeadline = 'SALVAMENTO'
QuestsRescueQuestSCStringS = 'Preciso salvar um Toon%(toonLoc)s.'
QuestsRescueQuestSCStringP = 'Preciso salvar alguns Toons%(toonLoc)s.'
QuestsRescueQuestRescue = 'Salvar %s'
QuestsRescueQuestRescueDesc = '%(numToons)s Toons'
QuestsRescueQuestToonS = 'um Toon'
QuestsRescueQuestToonP = 'Toons'
QuestsRescueQuestAux = 'Salvar:'
QuestsRescueNewNewbieQuestObjective = 'Ajudar um novo Toon a salvar %s'
QuestsRescueOldNewbieQuestObjective = 'Ajude um Toon com %(laffPoints)de risadas, ou menos, a resgatar %(objective)s'
QuestCogPartQuestCogPart = 'Parte do Processo Cog'
QuestsCogPartQuestFactories = 'F\xc3\xa1bricas'
QuestsCogPartQuestHeadline = 'RECUPERAR'
QuestsCogPartQuestProgressString = '%(progress)s de %(num)s recuperados'
QuestsCogPartQuestString = 'Recuperar %s'
QuestsCogPartQuestSCString = 'Preciso recuperar %(objective)s%(location)s.'
QuestsCogPartQuestAux = 'Recuperar:'
QuestsCogPartQuestDesc = 'uma Parte do Processo Cog'
QuestsCogPartQuestDescC = '%(count)s Parte(s) do Processo Cog'
QuestsCogPartQuestDescI = 'algumas Partes do Processo Cog'
QuestsCogPartNewNewbieQuestObjective = 'Ajude um novo Toon a recuperar %s'
QuestsCogPartOldNewbieQuestObjective = 'Ajude um Toon com %(laffPoints)de risadas, ou menos, a recuperar %(objective)s'
QuestsDeliverGagQuestProgress = '%(progress)s de %(numGags)s entregues'
QuestsDeliverGagQuestHeadline = 'ENTREGAR'
QuestsDeliverGagQuestToSCStringS = 'Preciso entregar %(gagName)s.'
QuestsDeliverGagQuestToSCStringP = 'Preciso entregar algumas %(gagName)s.'
QuestsDeliverGagQuestSCString = 'Preciso fazer uma entrega.'
QuestsDeliverGagQuestString = 'Entregar %s'
QuestsDeliverGagQuestStringLong = 'Entregar %s a _toNpcName_.'
QuestsDeliverGagQuestInstructions = 'Voc\xc3\xaa pode comprar esta piada na Loja de Piadas quando tiver acesso a ela.'
QuestsDeliverItemQuestProgress = ''
QuestsDeliverItemQuestHeadline = 'ENTREGAR'
QuestsDeliverItemQuestSCString = 'Preciso entregar %(article)s%(itemName)s.'
QuestsDeliverItemQuestString = 'Entregar %s'
QuestsDeliverItemQuestStringLong = 'Entregar %s a _toNpcName_.'
QuestsVisitQuestProgress = ''
QuestsVisitQuestHeadline = 'VISITAR'
QuestsVisitQuestStringShort = 'Visitar'
QuestsVisitQuestStringLong = 'Visitar _toNpcName_'
QuestsVisitQuestSeeSCString = 'Preciso ver %s.'
QuestsRecoverItemQuestProgress = '%(progress)s de %(numItems)s recuperados'
QuestsRecoverItemQuestHeadline = 'RECUPERAR'
QuestsRecoverItemQuestSeeHQSCString = 'Preciso ver um ' + lHQOfficerM + '.'
QuestsRecoverItemQuestReturnToHQSCString = 'Preciso devolver %s para um ' + lHQOfficerM + '.'
QuestsRecoverItemQuestReturnToSCString = 'Preciso devolver %(item)s para %(npcName)s.'
QuestsRecoverItemQuestGoToHQSCString = 'Preciso ir a um Quartel dos Toons.'
QuestsRecoverItemQuestGoToPlaygroundSCString = 'Preciso ir ao P\xc3\xa1tio %s.'
QuestsRecoverItemQuestGoToStreetSCString = 'Preciso ir %(to)s %(street)s em %(hood)s.'
QuestsRecoverItemQuestVisitBuildingSCString = 'Preciso visitar %s%s.'
QuestsRecoverItemQuestWhereIsBuildingSCString = 'Onde \xc3\xa9 %s%s?'
QuestsRecoverItemQuestRecoverFromSCString = 'Preciso recuperar %(item)s de %(holder)s%(loc)s.'
QuestsRecoverItemQuestString = 'Recuperar %(item)s de %(holder)s'
QuestsRecoverItemQuestHolderString = '%(level)s %(holder)d+ %(cogs)s'
QuestsTrackChoiceQuestHeadline = 'ESCOLHER'
QuestsTrackChoiceQuestSCString = 'Preciso escolher entre %(trackA)s e %(trackB)s.'
QuestsTrackChoiceQuestMaybeSCString = 'Talvez eu deva escolher %s.'
QuestsTrackChoiceQuestString = 'Escolha entre %(trackA)s e %(trackB)s'
QuestsFriendQuestHeadline = 'AMIGO'
QuestsFriendQuestSCString = 'Preciso fazer um amigo.'
QuestsFriendQuestString = 'Fazer um amigo'
QuestsMailboxQuestHeadline = 'CORRESPOND\xc3\x8aNCIA'
QuestsMailboxQuestSCString = 'Preciso verificar minha correspond\xc3\xaancia.'
QuestsMailboxQuestString = 'Verificar sua correspond\xc3\xaancia'
QuestsPhoneQuestHeadline = 'CLARABELA'
QuestsPhoneQuestSCString = 'Preciso ligar para Clarabela.'
QuestsPhoneQuestString = 'Ligar para Clarabela'
QuestsFriendNewbieQuestString = 'Fa\xc3\xa7a %d amigos %d risadas ou menos'
QuestsFriendNewbieQuestProgress = '%(progress)s de %(numFriends)s feitos'
QuestsFriendNewbieQuestObjective = 'Fa\xc3\xa7a amizade com %d novos Toons'
QuestsTrolleyQuestHeadline = 'BONDINHO'
QuestsTrolleyQuestSCString = 'Preciso pegar o bondinho.'
QuestsTrolleyQuestString = 'Andar no bondinho'
QuestsTrolleyQuestStringShort = 'Pegar o bondinho'
QuestsMinigameNewbieQuestString = '%d Minijogos'
QuestsMinigameNewbieQuestProgress = '%(progress)s de %(numMinigames)s jogados'
QuestsMinigameNewbieQuestObjective = 'Divirta-se com %d minijogos com a ajuda de novos Toons'
QuestsMinigameNewbieQuestSCString = 'Preciso participar de minijogos com novos Toons.'
QuestsMinigameNewbieQuestCaption = 'Ajude um novo Toon %d risadas ou menos'
QuestsMinigameNewbieQuestAux = 'Jogar:'
QuestsMaxHpReward = 'Seu Limite de risadas foi aumentado em %s.'
QuestsMaxHpRewardPoster = 'Recompensa: %s ponto de Acr\xc3\xa9scimo de risadas'
QuestsMoneyRewardSingular = 'Voc\xc3\xaa ganha 1 balinha.'
QuestsMoneyRewardPlural = 'Voc\xc3\xaa ganha %s balinhas.'
QuestsMoneyRewardPosterSingular = 'Recompensa: 1 balinha'
QuestsMoneyRewardPosterPlural = 'Recompensa: %s balinhas'
QuestsMaxMoneyRewardSingular = 'Agora, voc\xc3\xaa pode carregar 1 balinha.'
QuestsMaxMoneyRewardPlural = 'Agora, voc\xc3\xaa pode carregar %s balinhas.'
QuestsMaxMoneyRewardPosterSingular = 'Recompensa: Carregue 1 balinha'
QuestsMaxMoneyRewardPosterPlural = 'Recompensa: Carregue %s balinhas'
QuestsMaxGagCarryReward = 'Voc\xc3\xaa ganha %(name)s. Agora, voc\xc3\xaa pode carregar %(num)s piadas.'
QuestsMaxGagCarryRewardPoster = 'Recompensa: %(name)s (%(num)s)'
QuestsMaxQuestCarryReward = 'Agora, voc\xc3\xaa pode ter %s Tarefas Toon.'
QuestsMaxQuestCarryRewardPoster = 'Recompensa: Carregue %s Tarefas Toon'
QuestsTeleportReward = 'Agora, voc\xc3\xaa tem acesso por teletransporte a %s.'
QuestsTeleportRewardPoster = 'Recompensa: Acesso por teletransporte a %s'
QuestsTrackTrainingReward = 'Agora, voc\xc3\xaa pode treinar para "%s" piadas.'
QuestsTrackTrainingRewardPoster = 'Recompensa: Treinamento de piadas'
QuestsTrackProgressReward = 'Agora, voc\xc3\xaa tem o quadro %(frameNum)s da anima\xc3\xa7\xc3\xa3o do tipo %(trackName)s.'
QuestsTrackProgressRewardPoster = 'Recompensa: "Quadro %(frameNum)s da anima\xc3\xa7\xc3\xa3o do tipo %(trackName)s"'
QuestsTrackCompleteReward = 'Agora, voc\xc3\xaa pode carregar e usar "%s" piadas.'
QuestsTrackCompleteRewardPoster = 'Recompensa: Treinamento final do tipo %s'
QuestsClothingTicketReward = 'Voc\xc3\xaa pode trocar de roupa'
QuestsClothingTicketRewardPoster = 'Recompensa: Bilhete de roupas'
TIPQuestsClothingTicketReward = 'Voc\xc3\xaa pode trocar de roupa'
TIPQuestsClothingTicketRewardPoster = 'Recompensa: Bilhete de roupas'
QuestsCheesyEffectRewardPoster = 'Recompensa: %s'
QuestsCogSuitPartReward = 'Agora, voc\xc3\xaa tem uma %(cogTrack)s %(part)s pe\xc3\xa7a de vestimenta de Cog.'
QuestsCogSuitPartRewardPoster = 'Recompensa: %(cogTrack)s %(part)s Pe\xc3\xa7a'
QuestsStreetLocationThisPlayground = 'neste p\xc3\xa1tio'
QuestsStreetLocationThisStreet = 'nesta rua'
QuestsStreetLocationNamedPlayground = 'no p\xc3\xa1tio %s'
QuestsStreetLocationNamedStreet = 'na %(toStreetName)s em %(toHoodName)s'
QuestsLocationString = '%(string)s%(location)s'
QuestsLocationBuilding = "O edif\xc3\xadcio de %s's chama-se"
QuestsLocationBuildingVerb = 'o qual \xc3\xa9'
QuestsLocationParagraph = '\x7%(building)s "%(buildingName)s"...\x7...%(buildingVerb)s %(street)s.'
QuestsGenericFinishSCString = 'Preciso terminar uma Tarefa Toon.'
QuestsMediumPouch = 'Sacola m\xc3\xa9dia'
QuestsLargePouch = 'Sacola grande'
QuestsSmallBag = 'Bolsa pequena'
QuestsMediumBag = 'Bolsa m\xc3\xa9dia'
QuestsLargeBag = 'Bolsa grande'
QuestsSmallBackpack = 'Mochila pequena'
QuestsMediumBackpack = 'Mochila m\xc3\xa9dia'
QuestsLargeBackpack = 'Mochila grande'
QuestsItemDict = {
    1: [
        'Par de \xc3\xb3culos',
        'Pares de \xc3\xb3culos',
        'um '],
    2: [
        'Chave',
        'Chaves',
        'uma '],
    3: [
        'Quadro-negro',
        'Quadros-negros',
        'um '],
    4: [
        'Livro',
        'Livros',
        'um '],
    5: [
        'Chocolate',
        'Chocolates',
        'um '],
    6: [
        'Peda\xc3\xa7o de giz',
        'Peda\xc3\xa7os de giz',
        'um '],
    7: [
        'Receita',
        'Receitas',
        'uma '],
    8: [
        'Nota',
        'Notas',
        'uma '],
    9: [
        'Calculadora',
        'Calculadoras',
        'uma '],
    10: [
        'Pneu de carro de palha\xc3\xa7o',
        'Pneus de carro de palha\xc3\xa7o',
        'um '],
    11: [
        'Bomba de ar',
        'Bombas de ar',
        'uma '],
    12: [
        'Tinta de polvo',
        'Tintas de polvo',
        'uma '],
    13: [
        'Pacotes',
        'Pacotes',
        'um '],
    14: [
        'Recibo de peixe dourado',
        'Recibos de peixe dourado',
        'um '],
    15: [
        'Peixe dourado',
        'Peixe dourado',
        'um '],
    16: [
        '\xc3\x93leo',
        '\xc3\x93leos',
        'um pouco de '],
    17: [
        'Graxa',
        'Graxas',
        'um pouco de '],
    18: [
        '\xc3\x81gua',
        '\xc3\x81guas',
        'uma '],
    19: [
        'Relat\xc3\xb3rio de engrenagens',
        'Relat\xc3\xb3rios de engrenagens',
        'um '],
    20: [
        'Apagador de quadro-negro',
        'Apagadores de quadro-negro',
        'a '],
    110: [
        'Bilhete de Roupa DICA',
        'Bilhetes de Roupa',
        'um'],
    1000: [
        'Bilhete de roupas',
        'Bilhetes de roupas',
        'um '],
    2001: [
        'C\xc3\xa2mara de ar',
        'C\xc3\xa2maras de ar',
        'uma '],
    2002: [
        'Receita de mon\xc3\xb3culo',
        'Receita de mon\xc3\xb3culo',
        'uma '],
    2003: [
        'Arma\xc3\xa7\xc3\xa3o de \xc3\xb3culos',
        'Arma\xc3\xa7\xc3\xb5es de \xc3\xb3culos',
        'algumas '],
    2004: [
        'Mon\xc3\xb3culo',
        'Mon\xc3\xb3culos',
        'um '],
    2005: [
        'Grande peruca branca',
        'Grandes perucas brancas',
        'uma '],
    2006: [
        'Alqueire de cascalho',
        'Alqueires de cascalho',
        'um '],
    2007: [
        'Engrenagem Cog',
        'Engrenagens de Cog',
        'uma '],
    2008: [
        'Carta marinha',
        'Cartas marinhas',
        'uma '],
    2009: [
        'Bra\xc3\xa7adeira suja',
        'Bra\xc3\xa7adeiras sujas',
        'uma '],
    2010: [
        'Bra\xc3\xa7adeira limpa',
        'Bra\xc3\xa7adeiras limpas',
        'uma '],
    2011: [
        'Mola de rel\xc3\xb3gio',
        'Molas de rel\xc3\xb3gio',
        'uma '],
    2012: [
        'Contrapeso',
        'Contrapesos',
        'um '],
    4001: [
        'Estoque da Tina',
        'Estoques da Tina',
        ''],
    4002: [
        'Estoque da Cavaca',
        'Estoques da Cavaca',
        ''],
    4003: [
        'Formul\xc3\xa1rio de estoque',
        'Formul\xc3\xa1rios de estoque',
        'um '],
    4004: [
        'Estoque da Fifi',
        'Estoques da Fifi',
        ''],
    4005: [
        'Passagem do Al\xc3\xaa Nhador',
        'Passagens do Al\xc3\xaa Nhador',
        ''],
    4006: [
        'Passagem da T\xc3\xa1bata',
        'Passagens da T\xc3\xa1bata',
        ''],
    4007: [
        'Passagem do Barry',
        'Passagens do Barry',
        ''],
    4008: [
        'Castanhola fosca',
        'Castanholas foscas',
        ''],
    4009: [
        'Tinta de lula azul',
        'Tintas de lula azul',
        'obter '],
    4010: [
        'Castanhola polida',
        'Castanholas polidas',
        'uma '],
    4011: [
        'Letra de m\xc3\xbasica do L\xc3\xa9o',
        'Letras de m\xc3\xbasicas do L\xc3\xa9o',
        ''],
    5001: [
        'Gravata de seda',
        'Gravatas de seda',
        'uma '],
    5002: [
        'Terno listrado',
        'Ternos listrados',
        'um '],
    5003: [
        'Tesoura',
        'Tesouras',
        'uma '],
    5004: [
        'Cart\xc3\xa3o-postal',
        'Cart\xc3\xb5es-postais',
        'um '],
    5005: [
        'Caneta',
        'Canetas',
        'uma '],
    5006: [
        'Tinteiro',
        'Tinteiros',
        'um '],
    5007: [
        'Bloco de notas',
        'Blocos de notas',
        'um '],
    5008: [
        'Cofre de escrit\xc3\xb3rio',
        'Cofres de escrit\xc3\xb3rio',
        'um '],
    5009: [
        'Saco de ra\xc3\xa7\xc3\xa3o para p\xc3\xa1ssaros',
        'Sacos de ra\xc3\xa7\xc3\xa3o para p\xc3\xa1ssaros',
        'um '],
    5010: [
        'Roda dentada',
        'Rodas dentadas',
        'uma '],
    5011: [
        'Salada',
        'Saladas',
        'uma '],
    5012: [
        'Chave para os Jardins da Margarida',
        'Chaves para os Jardins da Margarida',
        'uma '],
    5013: [
        'Mapa do ' + lSellbotHQ,
        'Mapas do ' + lSellbotHQ,
        'alguns '],
    5014: [
        'Memorando do ' + lSellbotHQ,
        'Memorandos do ' + lSellbotHQ,
        'um '],
    5015: [
        'Memorando do ' + lSellbotHQ,
        'Memorandos do ' + lSellbotHQ,
        'um '],
    5016: [
        'Memorando do ' + lSellbotHQ,
        'Memorandos do ' + lSellbotHQ,
        'um '],
    5017: [
        'Memorando do ' + lSellbotHQ,
        'Memorandos do ' + lSellbotHQ,
        'um '],
    3001: [
        'Bola de futebol',
        'Bolas de futebol',
        'uma '],
    3002: [
        'Tobog\xc3\xa3',
        'Tobog\xc3\xa3s',
        'um '],
    3003: [
        'Cubo de gelo',
        'Cubos de gelo',
        'um '],
    3004: [
        'Carta de amor',
        'Cartas de amor',
        'uma '],
    3005: [
        'C\xc3\xa3o-lingui\xc3\xa7a',
        'c\xc3\xa3es-lingui\xc3\xa7a',
        'um '],
    3006: [
        'Anel de noivado',
        'An\xc3\xa9is de noivado',
        'um '],
    3007: [
        'Bigode de sardinha',
        'Bigodes de sardinhas',
        'um pouco de '],
    3008: [
        'Po\xc3\xa7\xc3\xa3o calmante',
        'Po\xc3\xa7\xc3\xb5es calmantes',
        'uma '],
    3009: [
        'Dente quebrado',
        'Dentes quebrados',
        'um '],
    3010: [
        'Dente de ouro',
        'Dentes de ouro',
        'um '],
    3011: [
        'P\xc3\xa3o de pinha',
        'P\xc3\xa3es de pinha',
        'um '],
    3012: [
        'Coco em peda\xc3\xa7os',
        'Cocos em peda\xc3\xa7os',
        'um pouco de '],
    3013: [
        'Colher simples',
        'Colheres simples',
        'uma '],
    3014: [
        'Sapo falante',
        'Sapos falantes',
        'um '],
    3015: [
        'Casquinha de sorvete',
        'Casquinhas de sorvete',
        'uma '],
    3016: [
        'P\xc3\xb3 de peruca',
        'P\xc3\xb3s de perucas',
        'um pouco de '],
    3017: [
        'Patinho de borracha',
        'Patinhos de borracha',
        'um '],
    3018: [
        'Dados de pel\xc3\xbacia',
        'Dados de pel\xc3\xbacia',
        'alguns '],
    3019: [
        'Microfone',
        'Microfones',
        'um '],
    3020: [
        'Teclado el\xc3\xa9trico',
        'Teclados el\xc3\xa9tricos',
        'um '],
    3021: [
        'Sapatos de plataforma',
        'Sapatos de plataforma',
        'alguns '],
    3022: [
        'Caviar',
        'Caviar',
        'um pouco de '],
    3023: [
        'P\xc3\xb3 de arroz',
        'P\xc3\xb3 de arroz',
        'um pouco de '],
    3024: [
        'Fio',
        'Fios',
        'alguns '],
    3025: [
        'Agulha de Tric\xc3\xb4',
        'Agulhas de Tric\xc3\xb4',
        'uma '],
    3026: [
        '\xc3\x81libi',
        '\xc3\x81libis',
        'um '],
    3027: [
        'Term\xc3\xb4metro Externo',
        'Term\xc3\xb4metros Externos',
        'um '],
    6001: [
        'Plano do Quartel do Rob\xc3\xb4 Mercen\xc3\xa1rio',
        'Planos do Quartel do Rob\xc3\xb4 Mercen\xc3\xa1rio',
        'algum '],
    6002: [
        'Vara de pescar',
        'Varas de pescar',
        'uma '],
    6003: [
        'Cinto de seguran\xc3\xa7a',
        'Cintos de seguran\xc3\xa7a',
        'um '],
    6004: [
        'Par de pin\xc3\xa7as',
        'Pares de pin\xc3\xa7as',
        'um '],
    6005: [
        'Abajur de leitura',
        'Abajures de leitura',
        'um '],
    6006: [
        'C\xc3\xadtara',
        'C\xc3\xadtaras',
        'uma '],
    6007: [
        'Zamboni',
        'Zambonis',
        'uma '],
    6008: [
        'Zabuton de zebra',
        'Zabutons de zebra',
        'uma '],
    6009: [
        'Zinnias',
        'Zinnias',
        'alguns '],
    6010: [
        'Discos de forr\xc3\xb3',
        'Discos de forr\xc3\xb3',
        'algum '],
    6011: [
        'Abobrinha',
        'Abobrinhas',
        'uma '],
    6012: [
        'Palet\xc3\xb3 zoot',
        'Palet\xc3\xb3s zoot',
        'um '],
    7001: [
        'Cama comum',
        'Camas comuns',
        'uma '],
    7002: [
        'Cama elegante',
        'Camas elegantes',
        'uma '],
    7003: [
        'Colcha azul',
        'Colchas azuis',
        'uma '],
    7004: [
        'Colcha estampada',
        'Colchas estampadas ',
        'uma'],
    7005: [
        'Travesseiros',
        'Travesseiros',
        'alguns '],
    7006: [
        'Travesseiros duros',
        'Travesseiros duros ',
        'um'],
    7007: [
        'Pijamas',
        'Pijamas',
        'um par de '],
    7008: [
        'Pijamas com p\xc3\xa9s',
        'Pijamas com p\xc3\xa9s',
        'um par de '],
    7009: [
        'Pijamas com p\xc3\xa9s marrons',
        'Pijamas com p\xc3\xa9s marrons',
        'um par de '],
    7010: [
        'Pijamas com p\xc3\xa9s f\xc3\xbacsia',
        'Pijamas com p\xc3\xa9s f\xc3\xbacsia',
        'um par de '],
    7011: [
        'Coral de couve-flor',
        'Coral de couve-flor',
        'algumas '],
    7012: [
        'Alga-marinha viscosa',
        'Alga-marinha viscosa',
        'um '],
    7013: [
        'Pil\xc3\xa3o',
        'Pil\xc3\xb5es',
        'um '],
    7014: [
        'Pote de creme para rugas',
        'Potes de creme para rugas',
        'um '] }
QuestsHQOfficerFillin = lHQOfficerM
QuestsHQWhereFillin = ''
QuestsHQBuildingNameFillin = lToonHQ
QuestsHQLocationNameFillin = 'em qualquer bairro'
QuestsTailorFillin = 'Costureiro'
QuestsTailorWhereFillin = ''
QuestsTailorBuildingNameFillin = 'Loja de Roupas'
QuestsTailorLocationNameFillin = 'em qualquer bairro'
QuestsTailorQuestSCString = 'Preciso ir ao Costureiro.'
QuestMovieQuestChoiceCancel = 'Volte mais tarde se precisar de uma Tarefa Toon! Tchau!'
QuestMovieTrackChoiceCancel = 'Volte quando j\xc3\xa1 tiver decidido o que fazer! Tchau!'
QuestMovieQuestChoice = 'Escolha uma Tarefa Toon.'
QuestMovieTrackChoice = 'J\xc3\xa1 decidiu o que escolher? Escolha um tipo ou volte mais tarde.'
GREETING = 0
QUEST = 1
INCOMPLETE = 2
INCOMPLETE_PROGRESS = 3
INCOMPLETE_WRONG_NPC = 4
COMPLETE = 5
LEAVING = 6
TheBrrrghTrackQuestDict = {
    GREETING: '',
    QUEST: 'Agora, voc\xc3\xaa est\xc3\xa1 pronto.\x7Saia e refresque a cabe\xc3\xa7a at\xc3\xa9 descobrir que tipo voc\xc3\xaa gostaria de escolher.\x7Escolha bem, pois voc\xc3\xaa n\xc3\xa3o poder\xc3\xa1 mudar.\x7Quando tiver certeza, volte aqui.',
    INCOMPLETE_PROGRESS: 'Escolha bem.',
    INCOMPLETE_WRONG_NPC: 'Escolha bem.',
    COMPLETE: '\xc3\x93tima escolha!',
    LEAVING: 'Boa sorte. Volte aqui quando tiver dominado sua nova habilidade.' }
QuestDialog_3225 = {
    QUEST: 'Puxa, obrigado por vir, _avName_!\x7Os Cogs que est\xc3\xa3o no bairro assustaram o rapaz que faz as entregas.\x7Eu n\xc3\xa3o tenho quem entregue esta salada para _toNpcName_!\x7Voc\xc3\xaa poderia fazer isso por mim? Muit\xc3\xadssimo obrigado!_where_' }
QuestDialog_2910 = {
    QUEST: 'De volta t\xc3\xa3o r\xc3\xa1pido assim?\x7\xc3\x93timo trabalho com aquela mola.\x7O \xc3\xbaltimo item \xc3\xa9 um contrapeso.\x7Passe l\xc3\xa1, veja com _toNpcName_ e traga o que voc\xc3\xaa conseguir._where_' }
QuestDialogDict = {
    160: {
        GREETING: '',
        QUEST: 'Ok, agora acho que voc\xc3\xaa est\xc3\xa1 pronto para um desafio maior.\x7Derrote 3 Rob\xc3\xb4s-chefe.',
        INCOMPLETE_PROGRESS: 'Os ' + Cogs + ' est\xc3\xa3o soltos pelas ruas e pelos t\xc3\xbaneis.',
        INCOMPLETE_WRONG_NPC: 'Bom trabalho com os Rob\xc3\xb4s-chefe. V\xc3\xa1 agora para o Quartel dos Toons para receber sua recompensa!',
        COMPLETE: QuestsDefaultComplete,
        LEAVING: QuestsDefaultLeaving },
    161: {
        GREETING: '',
        QUEST: 'Ok, agora acho que voc\xc3\xaa est\xc3\xa1 pronto para um desafio maior.\x7Derrote 3 Rob\xc3\xb4s da Lei.',
        INCOMPLETE_PROGRESS: 'Os ' + Cogs + ' est\xc3\xa3o soltos pelas rua e pelos t\xc3\xbaneis.',
        INCOMPLETE_WRONG_NPC: 'Bom trabalho com os Rob\xc3\xb4s da Lei. V\xc3\xa1 agora para o Quartel dos Toons para receber sua recompensa!',
        COMPLETE: QuestsDefaultComplete,
        LEAVING: QuestsDefaultLeaving },
    162: {
        GREETING: '',
        QUEST: 'Ok, agora acho que voc\xc3\xaa est\xc3\xa1 pronto para um desafio maior.\x7Derrote 3 Rob\xc3\xb4s Mercen\xc3\xa1rios.',
        INCOMPLETE_PROGRESS: 'Os ' + Cogs + ' est\xc3\xa3o soltos pelas ruas e pelos t\xc3\xbaneis.',
        INCOMPLETE_WRONG_NPC: 'Bom trabalho com os Rob\xc3\xb4s Mercen\xc3\xa1rios. V\xc3\xa1 agora para o Quartel dos Toons para receber sua recompensa!',
        COMPLETE: QuestsDefaultComplete,
        LEAVING: QuestsDefaultLeaving },
    163: {
        GREETING: '',
        QUEST: 'Ok, agora acho que voc\xc3\xaa est\xc3\xa1 pronto para um desafio maior.\x7Derrote 3 Rob\xc3\xb4s Vendedores.',
        INCOMPLETE_PROGRESS: 'Os ' + Cogs + ' est\xc3\xa3o soltos pelas ruas e pelos t\xc3\xbaneis.',
        INCOMPLETE_WRONG_NPC: 'Bom trabalho com os Rob\xc3\xb4s Vendedores. V\xc3\xa1 agora para o Quartel dos Toons para receber sua recompensa!',
        COMPLETE: QuestsDefaultComplete,
        LEAVING: QuestsDefaultLeaving },
    164: {
        QUEST: 'Parece que voc\xc3\xaa precisa de novas piadas.\x7Visite o Flippy, talvez ele possa ajud\xc3\xa1-lo._where_' },
    165: {
        QUEST: 'Ol\xc3\xa1.\x7Parece que voc\xc3\xaa precisa praticar suas piadas.\x7Toda vez que voc\xc3\xaa atinge um Cog com uma de suas piadas, sua experi\xc3\xaancia aumenta.\x7Quando tiver experi\xc3\xaancia suficiente, voc\xc3\xaa ser\xc3\xa1 capaz de usar uma piada ainda melhor.\x7V\xc3\xa1 praticar suas piadas derrotando 4 Cogs.' },
    166: {
        QUEST: 'Bom trabalho com aqueles Cogs.\x7Sabia que existem quatro tipos diferentes de Cogs?\x7Eles s\xc3\xa3o os Rob\xc3\xb4s da Lei, os Rob\xc3\xb4s Mercen\xc3\xa1rios, os Rob\xc3\xb4s Vendedores e os Rob\xc3\xb4s-chefe.\x7Voc\xc3\xaa pode diferenci\xc3\xa1-los pela cor e pelas etiquetas com os nomes.\x7Para praticar, derrote 4 Rob\xc3\xb4s-chefe.' },
    167: {
        QUEST: 'Bom trabalho com aqueles Cogs.\x7Sabia que existem quatro tipos diferentes de Cogs?\x7Eles s\xc3\xa3o os Rob\xc3\xb4s da Lei, os Rob\xc3\xb4s Mercen\xc3\xa1rios, os Rob\xc3\xb4s Vendedores e os Rob\xc3\xb4s-chefe.\x7Voc\xc3\xaa pode diferenci\xc3\xa1-los pela cor e pelas etiquetas com os nomes.\x7Para praticar, derrote 4 Rob\xc3\xb4s da Lei.' },
    168: {
        QUEST: 'Bom trabalho com aqueles Cogs.\x7Sabia que existem quatro tipos diferentes de Cogs?\x7Eles s\xc3\xa3o os Rob\xc3\xb4s da Lei, os Rob\xc3\xb4s Mercen\xc3\xa1rios, os Rob\xc3\xb4s Vendedores e os Rob\xc3\xb4s-chefe.\x7Voc\xc3\xaa pode diferenci\xc3\xa1-los pela cor e pelas etiquetas com os nomes.\x7Para praticar, derrote 4 Rob\xc3\xb4s Vendedores.' },
    169: {
        QUEST: 'Bom trabalho com aqueles Cogs.\x7Sabia que existem quatro tipos diferentes de Cogs?\x7Eles s\xc3\xa3o os Rob\xc3\xb4s da Lei, os Rob\xc3\xb4s Mercen\xc3\xa1rios, os Rob\xc3\xb4s Vendedores e os Rob\xc3\xb4s-chefe.\x7Voc\xc3\xaa pode diferenci\xc3\xa1-los pela cor e pelas etiquetas com os nomes.\x7Para praticar, derrote 4 Rob\xc3\xb4s Mercen\xc3\xa1rios.' },
    170: {
        QUEST: 'Bom trabalho; agora voc\xc3\xaa sabe a diferen\xc3\xa7a entre os 4 tipos de Cogs.\x7Acho que voc\xc3\xaa est\xc3\xa1 pronto para come\xc3\xa7ar a treinar o seu terceiro tipo de piada.\x7Fale com _toNpcName_ para escolher o seu pr\xc3\xb3ximo tipo de piada - ele pode dar alguns conselhos especiais para voc\xc3\xaa._where_' },
    171: {
        QUEST: 'Bom trabalho; agora voc\xc3\xaa sabe a diferen\xc3\xa7a entre os 4 tipos de Cogs.\x7Acho que voc\xc3\xaa est\xc3\xa1 pronto para come\xc3\xa7ar a treinar o seu terceiro tipo de piada.\x7Fale com _toNpcName_ para escolher o seu pr\xc3\xb3ximo tipo de piada - ele pode dar alguns conselhos especiais para voc\xc3\xaa._where_' },
    172: {
        QUEST: 'Bom trabalho; agora voc\xc3\xaa sabe a diferen\xc3\xa7a entre os 4 tipos de Cogs.\x7Acho que voc\xc3\xaa est\xc3\xa1 pronto para come\xc3\xa7ar a treinar o seu terceiro tipo de piada.\x7Fale com _toNpcName_ para escolher o seu pr\xc3\xb3ximo tipo de piada - ela pode dar alguns conselhos especiais para voc\xc3\xaa._where_' },
    175: {
        GREETING: '',
        QUEST: 'Voc\xc3\xaa sabia que possui sua pr\xc3\xb3pria casa Toon?\x7A vaca Clarabela administra um cat\xc3\xa1logo telef\xc3\xb4nico no qual voc\xc3\xaa pode escolher e encomendar m\xc3\xb3veis para decorar sua casa.\x7Voc\xc3\xaa tamb\xc3\xa9m pode comprar frases do Chat R\xc3\xa1pido, roupas e outras coisas muito legais!\x7Pedirei \xc3\xa0 Clarabela para enviar agora a voc\xc3\xaa seu primeiro cat\xc3\xa1logo.\x7Voc\xc3\xaa receber\xc3\xa1 um cat\xc3\xa1logo com novos itens toda semana!\x7V\xc3\xa1 para sua casa e use o seu telefone para ligar para Clarabela.',
        INCOMPLETE_PROGRESS: 'V\xc3\xa1 para casa e use o seu telefone para ligar para Clarabela.',
        COMPLETE: 'Espero que voc\xc3\xaa se divirta fazendo encomendas com Clarabela!\x7 Acabei de redecorar minha casa. Est\xc3\xa1 Toont\xc3\xa1stica!\x7Continue com as Tarefas Toon para ganhar mais recompensas!',
        LEAVING: QuestsDefaultLeaving },
    400: {
        GREETING: '',
        QUEST: 'Lan\xc3\xa7amento e Esguicho s\xc3\xa3o tipos \xc3\xb3timos, mas voc\xc3\xaa vai precisar de mais piadas para lutar com Cogs de n\xc3\xadveis mais altos.\x7Quando voc\xc3\xaa se juntar com outros Toons para enfrentar os Cogs, pode combinar ataques para conseguir danos maiores ao inimigo.\x7Tente diferentes combina\xc3\xa7\xc3\xb5es de Piadas para ver o que funciona melhor.\x7Para o seu pr\xc3\xb3ximo tipo, escolha as Sonoras ou Toonar.\x7As Sonoras s\xc3\xa3o especiais, pois quando atingem algum Cog, todos os outros tamb\xc3\xa9m sofrem danos.\x7As Toonar permitem curar outros Toons durante a batalha.\x7Quando estiver pronto para decidir, venha aqui e escolha uma.',
        INCOMPLETE_PROGRESS: 'De volta t\xc3\xa3o r\xc3\xa1pido? Ok, voc\xc3\xaa est\xc3\xa1 pronto para escolher?',
        INCOMPLETE_WRONG_NPC: 'Pense bem sobre sua decis\xc3\xa3o antes de escolher.',
        COMPLETE: 'Boa decis\xc3\xa3o. Agora, antes de usar estas piadas, voc\xc3\xaa deve treinar.\x7Voc\xc3\xaa deve completar uma s\xc3\xa9rie de Tarefas Toon como treinamento.\x7Cada tarefa dar\xc3\xa1 a voc\xc3\xaa um \xc3\xbanico quadro da anima\xc3\xa7\xc3\xa3o do seu ataque de piadas.\x7Quando voc\xc3\xaa coletar todas as 15, poder\xc3\xa1 obter a tarefa Treinamento final de piadas, que lhe permitir\xc3\xa1 usar suas novas piadas.\x7Voc\xc3\xaa pode verificar seu progresso no \xc3\x81lbum Toon.',
        LEAVING: QuestsDefaultLeaving },
    1039: {
        QUEST: 'Visite _toNpcName_ se desejar transitar pela cidade com mais facilidade._where_' },
    1040: {
        QUEST: 'Visite _toNpcName_ se desejar transitar pela cidade com mais facilidade._where_' },
    1041: {
        QUEST: 'Oi! O que o traz aqui?\x7Todo mundo usa o buraco port\xc3\xa1til para andar por Toontown.\x7\xc3\x89, voc\xc3\xaa pode se teletransportar at\xc3\xa9 seus amigos, usando a Lista de amigos, ou at\xc3\xa9 qualquer bairro, usando o mapa no \xc3\x81lbum Toon.\x7\xc3\x89 claro que voc\xc3\xaa precisa consegui-lo!\x7Olha, eu posso ativar seu acesso por teletransporte at\xc3\xa9 o Centro de Toontown se voc\xc3\xaa ajudar um amigo meu.\x7Parece que os Cogs est\xc3\xa3o dando problema na Travessa dos Tontos. Visite _toNpcName_._where_' },
    1042: {
        QUEST: 'Oi! O que o traz aqui?\x7Todo mundo usa o buraco port\xc3\xa1til para andar por Toontown.\x7\xc3\x89, voc\xc3\xaa pode se teletransportar at\xc3\xa9 seus amigos, usando a Lista de amigos, ou at\xc3\xa9 qualquer bairro, usando o mapa no \xc3\x81lbum Toon.\x7\xc3\x89 claro que voc\xc3\xaa precisa consegui-lo!\x7Olha, eu posso ativar seu acesso por teletransporte at\xc3\xa9 o Centro de Toontown se voc\xc3\xaa ajudar um amigo meu.\x7Parece que os Cogs est\xc3\xa3o dando problema na Travessa dos Tontos. Visite _toNpcName_._where_' },
    1043: {
        QUEST: 'Oi! O que o traz aqui?\x7Todo mundo usa o buraco port\xc3\xa1til para andar por Toontown.\x7\xc3\x89, voc\xc3\xaa pode se teletransportar at\xc3\xa9 seus amigos, usando a Lista de amigos, ou at\xc3\xa9 qualquer bairro, usando o mapa no \xc3\x81lbum Toon.\x7\xc3\x89 claro que voc\xc3\xaa precisa consegui-lo!\x7Olha, eu posso ativar seu acesso por teletransporte at\xc3\xa9 o Centro de Toontown se voc\xc3\xaa ajudar um amigo meu.\x7Parece que os Cogs est\xc3\xa3o dando problema na Travessa dos Tontos. Visite _toNpcName_._where_' },
    1044: {
        QUEST: 'Puxa, obrigado por passar por aqui. Eu realmente preciso de ajuda.\x7Como voc\xc3\xaa pode ver, eu n\xc3\xa3o tenho clientes.\x7O meu livro de receitas secreto est\xc3\xa1 perdido e ningu\xc3\xa9m mais vem ao meu restaurante.\x7A \xc3\xbaltima vez que eu o vi foi pouco antes de os Cogs tomarem meu edif\xc3\xadcio.\x7Voc\xc3\xaa pode me ajudar recuperando quatro de minhas receitas favoritas?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Conseguiu recuperar minhas receitas?' },
    1045: {
        QUEST: 'Valeu mesmo!\x7Logo terei de volta minha cole\xc3\xa7\xc3\xa3o completa e poderei reabrir meu restaurante.\x7Ah, h\xc3\xa1 uma nota aqui para voc\xc3\xaa - algo sobre acesso por teletransporte?\x7Diz: "obrigado por ajudar meu amigo e, por favor, entregue isto ao Quartel dos Toons".\x7Bem, valeu mesmo - tchau!',
        LEAVING: '',
        COMPLETE: 'Ah, sim, aqui diz que voc\xc3\xaa foi de grande ajuda para alguns dos caras mais legais da Travessa dos Tontos.\x7Diz tamb\xc3\xa9m que voc\xc3\xaa precisa de acesso por teletransporte para o Centro de Toontown.\x7Bem, considere concedido.\x7Agora, voc\xc3\xaa pode se teletransportar de volta para o p\xc3\xa1tio, de praticamente qualquer lugar de Toontown.\x7Basta abrir o seu mapa e clicar em Centro de Toontown.' },
    1046: {
        QUEST: 'Os Rob\xc3\xb4s Mercen\xc3\xa1rios t\xc3\xaam importunado bastante a Financeira Dinheiro Feliz.\x7Passe por l\xc3\xa1 e veja se h\xc3\xa1 algo que voc\xc3\xaa possa fazer._where_' },
    1047: {
        QUEST: 'Os Rob\xc3\xb4s Mercen\xc3\xa1rios t\xc3\xaam se infiltrado no banco e roubado nossas calculadoras.\x7Recupere 5 calculadoras dos Rob\xc3\xb4s Mercen\xc3\xa1rios.\x7Para evitar que voc\xc3\xaa fique indo para l\xc3\xa1 e para c\xc3\xa1, traga-as todas de uma vez.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Ainda procurando pelas calculadoras?' },
    1048: {
        QUEST: 'Uau! Valeu mesmo por encontrar nossas calculadoras.\x7Humm... Elas parecem danificadas.\x7Voc\xc3\xaa poderia lev\xc3\xa1-las para a loja de _toNpcName_, "M\xc3\xa1quinas de Cosquinhas", nesta rua?\x7Veja se podem consert\xc3\xa1-las.',
        LEAVING: '' },
    1049: {
        QUEST: 'O que \xc3\xa9 isto? Calculadoras quebradas?\x7Rob\xc3\xb4s Mercen\xc3\xa1rios?\x7Bem, vamos dar uma olhada...\x7\xc3\x89, as engrenagens est\xc3\xa3o partidas mas eu estou sem essa pe\xc3\xa7a...\x7Sabe o que poderia dar jeito? Algumas engrenagens de Cog, das grandes, dos Cogs maiores...\x7Engrenagens de Cogs de n\xc3\xadvel 3 devem servir. Precisarei de 2 para cada m\xc3\xa1quina, 10 no total.\x7Traga-as todas de uma vez e eu as consertarei!',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Lembre-se, eu preciso de 10 engrenagens para consertar as m\xc3\xa1quinas.' },
    1053: {
        QUEST: 'Ah sim, isto deve servir.\x7Tudo consertado agora, gr\xc3\xa1tis.\x7Leve-as de volta para a Dinheiro Feliz e diga ol\xc3\xa1 a ela por mim.',
        LEAVING: '',
        COMPLETE: 'Calculadoras consertadas?\x7Bom trabalho. Tenho certeza de que tenho algo por aqui para recompensar voc\xc3\xaa...' },
    1054: {
        QUEST: '_toNpcName_ precisa de alguma ajuda com seus carros de palha\xc3\xa7o._where_' },
    1055: {
        QUEST: 'Ol\xc3\xa1\xc3\xa1\xc3\xa1\xc3\xa1! Eu n\xc3\xa3o consigo encontrar os pneus para este carro de palha\xc3\xa7o em lugar nenhum!\x7Voc\xc3\xaa acha que pode me ajudar?\x7Eu acho que o Tito Tonto pode ter jogado os pneus no lago do p\xc3\xa1tio do Centro de Toontown.\x7Se voc\xc3\xaa ficar em um dos cais de l\xc3\xa1, poder\xc3\xa1 tentar pescar os pneus para mim.',
        GREETING: 'Iuhuu!',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Voc\xc3\xaa est\xc3\xa1 tendo problemas para pescar os 4 pneus?' },
    1056: {
        QUEST: 'Demor\xc3\xb4\xc3\xb4! Agora, este velho carro de palha\xc3\xa7o vai poder voltar \xc3\xa0s ruas!\x7Ei, eu pensei que tivesse uma bomba de ar aqui para inflar estes pneus...\x7Acho que _toNpcName_ pegou emprestado.\x7Voc\xc3\xaa poderia pedir de volta para mim?_where_',
        LEAVING: '' },
    1057: {
        QUEST: 'E a\xc3\xad?\x7Uma bomba de pneus?\x7Vamos fazer o seguinte: voc\xc3\xaa me ajuda a retirar das ruas alguns desses Cogs de alto n\xc3\xadvel...\x7E, ent\xc3\xa3o, darei a voc\xc3\xaa a bomba de pneus.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Isso \xc3\xa9 o melhor que voc\xc3\xaa pode fazer?' },
    1058: {
        QUEST: 'Bom trabalho! Eu sabia que voc\xc3\xaa conseguiria.\x7Aqui est\xc3\xa1 a bomba. Estou certo de que _toNpcName_ ficar\xc3\xa1 feliz em receb\xc3\xaa-la de volta.',
        LEAVING: '',
        GREETING: '',
        COMPLETE: 'Dez! Agora est\xc3\xa1 tudo certo!\x7Por falar nisso, obrigado por me ajudar.\x7Aqui, tome isto.' },
    1059: {
        QUEST: '_toNpcName_ est\xc3\xa1 com poucos suprimentos. Quem sabe voc\xc3\xaa pode ajud\xc3\xa1-lo?_where_' },
    1060: {
        QUEST: 'Valeu mesmo por passar aqui!\x7Os Cogs roubam sempre a minha tinta e, por isso, ela est\xc3\xa1 quase no fim.\x7Voc\xc3\xaa poderia pescar um pouco de tinta de polvo para mim no lago?\x7Para pescar, basta ficar parado em um cais perto do lago.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Voc\xc3\xaa est\xc3\xa1 tendo problemas para pescar?' },
    1061: {
        QUEST: '\xc3\x93timo, valeu pela tinta!\x7Sabe de uma coisa, se voc\xc3\xaa eliminasse alguns daqueles Ratos de Escrit\xc3\xb3rio...\x7A\xc3\xad minha tinta n\xc3\xa3o acabaria t\xc3\xa3o r\xc3\xa1pido.\x7Derrote 6 Ratos de Escrit\xc3\xb3rio no Centro de Toontown para receber sua recompensa.',
        LEAVING: '',
        COMPLETE: 'Valeu! Vou recompensar voc\xc3\xaa pela sua ajuda.',
        INCOMPLETE_PROGRESS: 'Eu acabei de ver mais alguns Ratos de Escrit\xc3\xb3rio.' },
    1062: {
        QUEST: '\xc3\x93timo, valeu pela tinta!\x7Sabe de uma coisa? Se voc\xc3\xaa eliminasse alguns daqueles Sanguessugas...\x7A\xc3\xad minha tinta n\xc3\xa3o acabaria t\xc3\xa3o r\xc3\xa1pido.\x7Derrote 6 Sanguessugas no Centro de Toontown para receber sua recompensa.',
        LEAVING: '',
        COMPLETE: 'Valeu! Vou recompensar voc\xc3\xaa pela sua ajuda.',
        INCOMPLETE_PROGRESS: 'Eu acabei de ver mais alguns Sanguessugas.' },
    900: {
        QUEST: 'Fiquei sabendo que _toNpcName_ precisa de ajuda com um pacote._where_' },
    1063: {
        QUEST: 'Ol\xc3\xa1! Legal voc\xc3\xaa ter vindo.\x7Um Cog roubou um pacote muito importante bem debaixo do meu nariz.\x7Veja se voc\xc3\xaa consegue recuper\xc3\xa1-lo. Eu acho que ele era de n\xc3\xadvel 3...\x7Ent\xc3\xa3o, derrote Cogs de n\xc3\xadvel 3 at\xc3\xa9 encontrar meu pacote.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'N\xc3\xa3o teve sorte de encontrar o pacote, n\xc3\xa9?' },
    1067: {
        QUEST: '\xc3\x89 ele mesmo, est\xc3\xa1 tudo certo!\x7Ei, o endere\xc3\xa7o est\xc3\xa1 borrado...\x7Tudo o que eu posso ler \xc3\xa9 que \xc3\xa9 para um Dr. - o resto est\xc3\xa1 ileg\xc3\xadvel.\x7Talvez seja para _toNpcName_? Voc\xc3\xaa pode levar para ele?_where_',
        LEAVING: '' },
    1068: {
        QUEST: 'Eu n\xc3\xa3o estava esperando um pacote. Talvez seja para o Dr. E.U. F\xc3\xb3rico.\x7Meu assistente ia passar mesmo l\xc3\xa1 hoje, ent\xc3\xa3o pedirei a ele que verifique para voc\xc3\xaa.\x7Nesse meio tempo, voc\xc3\xaa se importaria de se livrar de alguns dos Cogs que est\xc3\xa3o na minha rua?\x7Derrote 10 Cogs no Centro de Toontown.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Meu assistente ainda n\xc3\xa3o voltou.' },
    1069: {
        QUEST: 'O Dr. F\xc3\xb3rico disse que tamb\xc3\xa9m n\xc3\xa3o estava esperando nenhum pacote.\x7Infelizmente um Rob\xc3\xb4 Mercen\xc3\xa1rio roubou o pacote de meu assistente no caminho de volta.\x7Voc\xc3\xaa poderia tentar peg\xc3\xa1-lo de volta?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'N\xc3\xa3o teve sorte de encontrar o pacote, n\xc3\xa9?' },
    1070: {
        QUEST: 'O Dr. F\xc3\xb3rico disse que tamb\xc3\xa9m n\xc3\xa3o estava esperando nenhum pacote.\x7Infelizmente um Rob\xc3\xb4 Vendedor roubou o pacote de meu assistente no caminho de volta.\x7Sinto muito, mas voc\xc3\xaa ter\xc3\xa1 que encontrar esse Rob\xc3\xb4 Vendedor para peg\xc3\xa1-lo de volta.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'N\xc3\xa3o teve sorte de encontrar o pacote, n\xc3\xa9?' },
    1071: {
        QUEST: 'O Dr. F\xc3\xb3rico disse que tamb\xc3\xa9m n\xc3\xa3o estava esperando nenhum pacote.\x7Infelizmente um Rob\xc3\xb4-chefe roubou o pacote de meu assistente no caminho de volta.\x7Voc\xc3\xaa poderia tentar peg\xc3\xa1-lo de volta?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'N\xc3\xa3o teve sorte de encontrar o pacote, n\xc3\xa9?' },
    1072: {
        QUEST: '\xc3\x93timo, voc\xc3\xaa o pegou de volta!\x7Talvez voc\xc3\xaa deva tentar entreg\xc3\xa1-lo a _toNpcName_, pode ser para ele._where_',
        LEAVING: '' },
    1073: {
        QUEST: 'Puxa, obrigado por trazer meus pacotes para mim.\x7Espere um segundo, eu estava esperando dois. Voc\xc3\xaa poderia verificar com _toNpcName_ e ver se ele est\xc3\xa1 com o outro?',
        INCOMPLETE: 'Conseguiu encontrar meu outro pacote?',
        LEAVING: '' },
    1074: {
        QUEST: 'Ele disse que havia outro pacote? Talvez os Cogs o tenham roubado tamb\xc3\xa9m.\x7Derrote Cogs at\xc3\xa9 encontrar o segundo pacote.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'N\xc3\xa3o teve sorte de encontrar o outro pacote, n\xc3\xa9?' },
    1075: {
        QUEST: 'No final das contas, acho que n\xc3\xa3o havia um segundo pacote!\x7Corra e leve-o para _toNpcName_, com minhas desculpas.',
        COMPLETE: 'Ei, meu pacote est\xc3\xa1 aqui!\x7J\xc3\xa1 que voc\xc3\xaa parece ser um Toon t\xc3\xa3o prestativo, isto vai ser fichinha.',
        LEAVING: '' },
    1076: {
        QUEST: 'Houve alguns problemas na Peixinhos Dourados Ki-late.\x7_toNpcName_ provavelmente podem precisar de voc\xc3\xaa._where_' },
    1077: {
        QUEST: 'Legal voc\xc3\xaa ter vindo. Os Cogs roubaram todos os meus peixes dourados.\x7Eu acho que os Cogs querem vend\xc3\xaa-los para ganhar dinheiro f\xc3\xa1cil.\x7H\xc3\xa1 muitos anos, aqueles 5 peixes t\xc3\xaam sido minhas \xc3\xbanicas companhias nesta pequena loja ...\x7Se voc\xc3\xaa pudesse recuper\xc3\xa1-los, eu agradeceria muito.\x7Tenho certeza de que os Cogs est\xc3\xa3o com meus peixes.\x7Derrote Cogs at\xc3\xa9 encontrar meus peixes dourados.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Consiga meus peixes dourados de volta.' },
    1078: {
        QUEST: 'Puxa, voc\xc3\xaa recuperou meus peixes!\x7H\xc3\xa3? O que \xc3\xa9 isto - um recibo?\x7Ai, ai... Acho que eles s\xc3\xa3o Cogs mesmo.\x7Eu n\xc3\xa3o consigo decifrar este recibo. Voc\xc3\xaa poderia lev\xc3\xa1-lo para _toNpcName_ e ver se ele consegue l\xc3\xaa-lo?_where_',
        INCOMPLETE: 'O que _toNpcName_ disse sobre o recibo?',
        LEAVING: '' },
    1079: {
        QUEST: 'Humm, deixe-me ver este recibo.\x7...Ah, sim, diz que 1 peixe dourado foi vendido para um Puxa-saco.\x7O recibo n\xc3\xa3o menciona o que aconteceu com os outros 4 peixes.\x7Talvez voc\xc3\xaa deva tentar encontrar esse Puxa-saco.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Acho que n\xc3\xa3o h\xc3\xa1 mais nada em que eu possa ajudar.\x7Por que voc\xc3\xaa n\xc3\xa3o tenta encontrar aquele peixe dourado?' },
    1092: {
        QUEST: 'Humm, deixe-me ver este recibo.\x7...Ah, sim, diz que 1 peixe dourado foi vendido para um Farsante.\x7O recibo n\xc3\xa3o menciona o que aconteceu com os outros 4 peixes.\x7Talvez voc\xc3\xaa deva tentar encontrar esse Farsante.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Acho que n\xc3\xa3o h\xc3\xa1 mais nada em que eu possa ajudar.\x7Por que voc\xc3\xaa n\xc3\xa3o tenta encontrar aquele peixe dourado?' },
    1080: {
        QUEST: 'Ah, gra\xc3\xa7as aos c\xc3\xa9us! Voc\xc3\xaa encontrou Oscar - ele \xc3\xa9 o meu favorito.\x7O que foi, Oscar? H\xc3\xa3-h\xc3\xa3... Verdade? ... Est\xc3\xa3o?\x7Oscar diz que os outros 4 escaparam para dentro do lago no p\xc3\xa1tio.\x7Voc\xc3\xaa poderia reuni-los para mim?\x7\xc3\x89 s\xc3\xb3 pesc\xc3\xa1-los no lago.',
        LEAVING: '',
        COMPLETE: 'Nossa, estou t\xc3\xa3\xc3\xa3\xc3\xa3o feliz! Estou junto com meus companheiros novamente!\x7Voc\xc3\xaa merece uma bela recompensa por isso!',
        INCOMPLETE_PROGRESS: 'Voc\xc3\xaa est\xc3\xa1 tendo problemas para pescar esses peixes?' },
    1081: {
        QUEST: '_toNpcName_ parece estar numa situa\xc3\xa7\xc3\xa3o grudenta. Ela, com certeza, apreciaria alguma ajuda._where_' },
    1082: {
        QUEST: 'Eu derramei supercola e estou presa - presa pra valer!\x7Se houver uma maneira de sair, eu gostaria de saber.\x7Isso me d\xc3\xa1 uma ideia; abra os olhos.\x7Derrote alguns Rob\xc3\xb4s Vendedores e traga de volta um pouco de \xc3\xb3leo.',
        LEAVING: '',
        GREETING: '',
        INCOMPLETE_PROGRESS: 'Voc\xc3\xaa pode me ajudar a descolar daqui?' },
    1083: {
        QUEST: 'Bem, o \xc3\xb3leo ajudou um pouco, mas eu ainda n\xc3\xa3o consigo me mexer.\x7O que mais poderia ajudar? \xc3\x89 dif\xc3\xadcil dizer.\x7Isso me d\xc3\xa1 uma ideia; vale a pena tentar.\x7Derrote alguns Rob\xc3\xb4s da Lei e me traga graxa.',
        LEAVING: '',
        GREETING: '',
        INCOMPLETE_PROGRESS: 'Voc\xc3\xaa pode me ajudar a descolar daqui?' },
    1084: {
        QUEST: 'N\xc3\xa3o, isso n\xc3\xa3o ajudou. Isso realmente n\xc3\xa3o \xc3\xa9 engra\xc3\xa7ado.\x7Eu coloquei a graxa bem ali,\x7Isso me d\xc3\xa1 uma ideia, n\xc3\xa3o me deixe esquecer.\x7Derrote alguns Rob\xc3\xb4s Mercen\xc3\xa1rios e traga \xc3\xa1gua para umedecer.',
        LEAVING: '',
        GREETING: '',
        COMPLETE: 'Oba! Estou livre da supercola,\x7Como recompensa, dou este presente a voc\xc3\xaa.\x7Voc\xc3\xaa pode rir um pouco mais enquanto luta e, ent\xc3\xa3o...\x7Ah, n\xc3\xa3o! J\xc3\xa1 estou presa aqui novamente!',
        INCOMPLETE_PROGRESS: 'Voc\xc3\xaa pode me ajudar a descolar daqui?' },
    1085: {
        QUEST: '_toNpcName_ est\xc3\xa1 fazendo uma pesquisa sobre os Cogs.\x7V\xc3\xa1 falar com ele para ver se ele precisa da sua ajuda._where_' },
    1086: {
        QUEST: '\xc3\x89 verdade, estou fazendo um estudo sobre os Cogs.\x7Eu quero aprender sobre o comportamento deles.\x7Com certeza ajudaria se voc\xc3\xaa pudesse reunir algumas engrenagens de Cogs.\x7Mas elas t\xc3\xaam que ser de Cogs de n\xc3\xadvel 2, pelo menos, para serem grandes o suficiente para o exame visual.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'N\xc3\xa3o conseguiu encontrar engrenagens suficientes?' },
    1089: {
        QUEST: 'Certo, vamos dar uma olhada. Estas s\xc3\xa3o amostras excelentes!\x7Hummm...\x7Certo, aqui est\xc3\xa1 meu relat\xc3\xb3rio. Leve isto de volta imediatamente para o Quartel dos Toons.',
        INCOMPLETE: 'Voc\xc3\xaa entregou meu relat\xc3\xb3rio no Quartel?',
        COMPLETE: 'Bom trabalho _avName_, n\xc3\xb3s assumiremos a partir daqui.',
        LEAVING: '' },
    1090: {
        QUEST: '_toNpcName_ tem informa\xc3\xa7\xc3\xb5es \xc3\xbateis para voc\xc3\xaa._where_' },
    1091: {
        QUEST: 'Fiquei sabendo que o Quartel dos Toons est\xc3\xa1 trabalhando em uma esp\xc3\xa9cie de Radar de Cogs.\x7Ele permite ver onde os Cogs est\xc3\xa3o, para que seja mais f\xc3\xa1cil encontr\xc3\xa1-los.\x7A P\xc3\xa1gina de Cogs em seu \xc3\x81lbum Toon \xc3\xa9 a chave.\x7Ao derrotar Cogs suficientes, voc\xc3\xaa pode sintonizar os sinais deles e rastrear onde est\xc3\xa3o.\x7Continue derrotando Cogs para ficar pronto.',
        COMPLETE: 'Bom trabalho! Voc\xc3\xaa provavelmente vai poder fazer uso disso...',
        LEAVING: '' },
    401: {
        GREETING: '',
        QUEST: 'Agora, voc\xc3\xaa tem que escolher o pr\xc3\xb3ximo tipo de piada que deseja aprender.\x7Decida e depois volte aqui quando estiver pronto para escolher.',
        INCOMPLETE_PROGRESS: 'Pense bem sobre sua decis\xc3\xa3o antes de escolher.',
        INCOMPLETE_WRONG_NPC: 'Pense bem sobre sua decis\xc3\xa3o antes de escolher.',
        COMPLETE: 'Uma boa decis\xc3\xa3o...',
        LEAVING: QuestsDefaultLeaving },
    2201: {
        QUEST: 'Aqueles cogs trai\xc3\xa7oeiros est\xc3\xa3o envolvidos nisto novamente.\x7_toNpcName_ reportou outro item ausente. Pare um pouco aqui e veja se consegue acertar isso._where_' },
    2202: {
        QUEST: 'Oi, _avName_. Ainda bem que voc\xc3\xaa est\xc3\xa1 aqui. Um M\xc3\xa3o de vaca de m\xc3\xa1 apar\xc3\xaancia acabou de passar por aqui e saiu com uma c\xc3\xa2mara de ar.\x7Temo que ele possa us\xc3\xa1-la para seus planos diab\xc3\xb3licos.\x7Veja se voc\xc3\xaa consegue encontr\xc3\xa1-la e traz\xc3\xaa-la de volta.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Conseguiu achar minha c\xc3\xa2mara de ar?',
        COMPLETE: 'Voc\xc3\xaa encontrou minha c\xc3\xa2mara de ar! Voc\xc3\xaa \xc3\xa9 legal MESMO! Olha aqui, tome a sua recompensa...' },
    2203: {
        QUEST: 'Os cogs est\xc3\xa3o espalhando o caos no banco.\x7V\xc3\xa1 at\xc3\xa9 o Capit\xc3\xa3o Carl\xc3\xa3o e veja o que voc\xc3\xaa pode fazer._where_' },
    2204: {
        QUEST: 'Bem-vindo a bordo, colega.\x7Droga! Aqueles cogs patifes quebraram meu mon\xc3\xb3culo e eu n\xc3\xa3o vivo sem ele.\x7Seja um bom marujo e leve esta receita para o Dr. Quiqueres para trazer um novo para mim._where_',
        GREETING: '',
        LEAVING: '' },
    2205: {
        QUEST: 'O que \xc3\xa9 isso?\x7Puxa, eu adoraria poder trabalhar nesta receita, mas os cogs t\xc3\xaam furtado meus suprimentos.\x7Se voc\xc3\xaa pegasse a arma\xc3\xa7\xc3\xa3o dos \xc3\xb3culos de um Puxa-saco eu provavelmente poderia ajud\xc3\xa1-lo.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Sinto muito. Sem arma\xc3\xa7\xc3\xb5es de Puxa-saco, n\xc3\xa3o tem mon\xc3\xb3culo!' },
    2206: {
        QUEST: 'Excelente!\x7S\xc3\xb3 um segundo...\x7Sua receita est\xc3\xa1 pronta. Leve este mon\xc3\xb3culo diretamente ao Capit\xc3\xa3o Carl\xc3\xa3o._where_',
        GREETING: '',
        LEAVING: '',
        COMPLETE: 'Alto!\x7Voc\xc3\xaa vai ganhar sua condecora\xc3\xa7\xc3\xa3o, afinal de contas.\x7Aqui est\xc3\xa1.' },
    2207: {
        QUEST: 'H\xc3\xa1 um Cog na loja da Craca B\xc3\xa1rbara!\x7\xc3\x89 melhor voc\xc3\xaa ir para l\xc3\xa1 imediatamente._where_' },
    2208: {
        QUEST: 'Droga! Voc\xc3\xaa se desencontrou dele, gracinha.\x7Havia um Golpe Sujo aqui. Ele levou a minha grande peruca branca.\x7Ele disse que era para o chefe dele e mencionou algo como "precedente legal".\x7Se voc\xc3\xaa puder peg\xc3\xa1-la de volta, ficarei eternamente grata.',
        LEAVING: '',
        GREETING: '',
        INCOMPLETE_PROGRESS: 'Ainda n\xc3\xa3o o encontrou?\x7Ele \xc3\xa9 alto e tem uma cabe\xc3\xa7a pontuda.',
        COMPLETE: 'Voc\xc3\xaa a encontrou!?\x7Voc\xc3\xaa \xc3\xa9 uma gracinha!\x7Sua recompensa \xc3\xa9 mais do que merecida...' },
    2209: {
        QUEST: 'Moby est\xc3\xa1 se preparando para uma viagem importante.\x7Visite-o e veja o que pode fazer para ajud\xc3\xa1-lo._where_' },
    2210: {
        QUEST: 'Sua ajuda ser\xc3\xa1 bem-vinda.\x7O Quartel dos Toons me pediu para fazer uma viagem e ver se consigo descobrir de onde os cogs est\xc3\xa3o vindo.\x7Precisarei de algumas coisas para o meu navio, mas n\xc3\xa3o tenho muitas balinhas.\x7Passe pela loja da Alice e pegue um pouco de cascalho para mim. Voc\xc3\xaa ter\xc3\xa1 que fazer um favor para ela para poder pegar o cascalho._where_',
        GREETING: 'E a\xc3\xad, _avName_',
        LEAVING: '' },
    2211: {
        QUEST: 'Ent\xc3\xa3o, o Moby quer cascalho, n\xc3\xa9?\x7Ele ainda est\xc3\xa1 me devendo por aquele \xc3\xbaltimo alqueire.\x7Eu lhe darei se voc\xc3\xaa conseguir eliminar cinco Microempres\xc3\xa1rios na minha rua.',
        INCOMPLETE_PROGRESS: 'N\xc3\xa3o, seu bobinho! Eu disse CINCO microempres\xc3\xa1rios...',
        GREETING: 'O que posso fazer por voc\xc3\xaa?',
        LEAVING: '' },
    2212: {
        QUEST: 'Trato \xc3\xa9 trato.\x7Aqui est\xc3\xa1 o cascalho para aquele fominha do Moby._where_',
        GREETING: 'Ora, ora, o que temos aqui...',
        LEAVING: '' },
    2213: {
        QUEST: 'Excelente trabalho. Eu sabia que ela encontraria uma sa\xc3\xadda.\x7Agora, eu preciso pegar uma carta de navega\xc3\xa7\xc3\xa3o com o M\xc3\xa1rio.\x7Acho que meu cr\xc3\xa9dito l\xc3\xa1 tamb\xc3\xa9m n\xc3\xa3o \xc3\xa9 t\xc3\xa3o bom, portanto, voc\xc3\xaa vai ter que negociar com ele._where_',
        GREETING: '',
        LEAVING: '' },
    2214: {
        QUEST: 'Sim, eu tenho a carta de navega\xc3\xa7\xc3\xa3o que o Moby quer.\x7E se voc\xc3\xaa estiver disposto a trabalhar para consegui-la, eu a darei para voc\xc3\xaa.\x7Estou tentando construir um astrol\xc3\xa1bio para navegar pelas estrelas.\x7Preciso de tr\xc3\xaas engrenagens de Cog para constru\xc3\xad-la.\x7Volte aqui quando encontr\xc3\xa1-las.',
        INCOMPLETE_PROGRESS: 'Como est\xc3\xa1 indo com aquelas engrenagens de Cog?',
        GREETING: 'Bem-vindo!',
        LEAVING: 'Boa sorte!' },
    2215: {
        QUEST: 'Oh! Essas engrenagens v\xc3\xa3o ser \xc3\xbateis mesmo.\x7Aqui est\xc3\xa1 a carta. Leve para o Moby, com meus cumprimentos._where_',
        GREETING: '',
        LEAVING: '',
        COMPLETE: 'Bem, agora sim. Estou pronto para zarpar!\x7Eu o levaria comigo se voc\xc3\xaa n\xc3\xa3o fosse novato. Leve isto, ent\xc3\xa3o.' },
    901: {
        QUEST: 'Se estiver disposto, o Salgado est\xc3\xa1 precisando de ajuda na loja dele..._where_' },
    2902: {
        QUEST: 'Voc\xc3\xaa \xc3\xa9 o novo recruta?\x7Bom, bom. Talvez voc\xc3\xaa possa me ajudar.\x7Estou construindo um caranguejo pr\xc3\xa9-fabricado gigante para confundir os cogs.\x7Eu vou precisar de uma bra\xc3\xa7adeira. Visite o M\xc3\xa1rio e me traga uma._where_' },
    2903: {
        QUEST: 'Ol\xc3\xa1!\x7Sim, eu ouvi falar no caranguejo gigante que Salgado est\xc3\xa1 construindo.\x7A melhor bra\xc3\xa7adeira que tenho est\xc3\xa1 meio suja.\x7Seja gentil e passe pela lavanderia antes de lev\xc3\xa1-la para ele._where_',
        LEAVING: 'Valeu!' },
    2904: {
        QUEST: 'Voc\xc3\xaa deve ser o amigo do M\xc3\xa1rio.\x7Acho que posso limpar isso rapidinho.\x7S\xc3\xb3 um minuto...\x7Aqui est\xc3\xa1. Nova em folha!\x7Diga ol\xc3\xa1 ao Salgado por mim._where_' },
    2905: {
        QUEST: 'Ah, era exatamente o que eu queria.\x7J\xc3\xa1 que voc\xc3\xaa est\xc3\xa1 aqui, eu tamb\xc3\xa9m vou precisar de uma mola de rel\xc3\xb3gio de corda bem grande.\x7V\xc3\xa1 at\xc3\xa9 a loja do Gancho e veja se ele tem uma._where_' },
    2906: {
        QUEST: 'Uma mola bem grande?\x7Sinto muito, mas a maior que tenho ainda \xc3\xa9 pequena.\x7Talvez eu consiga montar uma com as molas do gatilho de rev\xc3\xb3lver de \xc3\xa1gua.\x7Traga-me tr\xc3\xaas dessas piadas e eu vou ver o que posso fazer.' },
    2907: {
        QUEST: 'Vamos dar uma olhada...\x7Arrasou. Simplesmente arrasou.\x7Algumas vezes eu surpreendo at\xc3\xa9 a mim mesmo.\x7Aqui est\xc3\xa1: uma mola grande para o Salgado!_where_',
        LEAVING: 'Bon Voyage!' },
    2911: {
        QUEST: 'Ficaria feliz em ajudar nisso, _avName_.\x7Mas temo que as ruas n\xc3\xa3o estejam mais t\xc3\xa3o seguras.\x7Por que voc\xc3\xaa n\xc3\xa3o vai derrotar alguns Rob\xc3\xb4s Mercen\xc3\xa1rios? Depois a gente conversa.',
        INCOMPLETE_PROGRESS: 'Eu ainda acho que voc\xc3\xaa precisa fazer que as ruas fiquem mais seguras.' },
    2916: {
        QUEST: 'Sim, eu tenho um peso para o Salgado.\x7No entanto, acho que seria mais seguro se voc\xc3\xaa derrotasse alguns Rob\xc3\xb4s Vendedores primeiro.',
        INCOMPLETE_PROGRESS: 'Ainda n\xc3\xa3o. Derrote mais alguns Rob\xc3\xb4s Vendedores.' },
    2921: {
        QUEST: 'Humm, acho que poderia ceder um peso.\x7Mas eu me sentiria melhor se n\xc3\xa3o houvesse tantos Rob\xc3\xb4s-chefe por a\xc3\xad.\x7Derrote seis deles e volte aqui.',
        INCOMPLETE_PROGRESS: 'Acho que ainda n\xc3\xa3o est\xc3\xa1 seguro...' },
    2925: {
        QUEST: 'Tudo pronto?\x7Bem, acho que agora est\xc3\xa1 suficientemente seguro.\x7Aqui est\xc3\xa1 o contrapeso para o Salgado._where_' },
    2926: {
        QUEST: 'Bem, isso \xc3\xa9 tudo.\x7Deixe-me ver se funciona.\x7Humm, um pequeno problema.\x7N\xc3\xa3o estou conseguindo obter energia, pois aquele edif\xc3\xadcio Cog est\xc3\xa1 bloqueando meu painel solar.\x7Voc\xc3\xaa poderia domin\xc3\xa1-lo para mim?',
        INCOMPLETE_PROGRESS: 'Ainda sem energia. E aquele edif\xc3\xadcio?',
        COMPLETE: 'S\xc3\xbaper! Voc\xc3\xaa \xc3\xa9 um destruidor de cogs e tanto! Tome isto aqui como recompensa...' },
    3200: {
        QUEST: 'Acabo de receber uma liga\xc3\xa7\xc3\xa3o do _toNpcName_.\x7Ele est\xc3\xa1 tendo um dia dif\xc3\xadcil. Talvez voc\xc3\xaa possa ajud\xc3\xa1-lo!\x7Passe por l\xc3\xa1 e veja do que ele precisa._where_' },
    3201: {
        QUEST: 'Puxa, obrigado por vir!\x7Preciso de algu\xc3\xa9m para levar esta nova gravata de seda para _toNpcName_.\x7Voc\xc3\xaa poderia fazer isso para mim?_where_' },
    3203: {
        QUEST: 'Ah, esta deve ser a gravata que eu pedi! Obrigado!\x7Ela combina com o terno listrado que acabei de terminar, logo ali.\x7Ei, o que aconteceu com o terno?\x7Oh, n\xc3\xa3o! Os Cogs devem ter roubado meu terno novo!\x7Derrote Cogs at\xc3\xa9 encontrar meu terno e traga-o de volta para mim.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Voc\xc3\xaa j\xc3\xa1 encontrou meu terno? Tenho certeza de que os Cogs o pegaram!',
        COMPLETE: 'Legal! Voc\xc3\xaa encontrou meu terno novo!\x7Viu, eu disse que os Cogs estavam com ele! Aqui est\xc3\xa1 a sua recompensa...' },
    3204: {
        QUEST: '_toNpcName_ acabou de ligar para informar um roubo.\x7Por que voc\xc3\xaa n\xc3\xa3o passa por l\xc3\xa1 e v\xc3\xaa se consegue resolver as coisas?_where_' },
    3205: {
        QUEST: 'Ol\xc3\xa1, _avName_! Voc\xc3\xaa veio me ajudar?\x7Acabei de expulsar um Sanguessuga de minha loja. Puxa! Foi horr\xc3\xadvel.\x7Mas agora n\xc3\xa3o encontro minha tesoura em lugar nenhum! Tenho certeza de que o Sanguessuga a levou.\x7Encontre-o e recupere minha tesoura.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Voc\xc3\xaa ainda est\xc3\xa1 procurando minha tesoura?',
        COMPLETE: 'Minha tesoura! Valeu mesmo, viu? Aqui est\xc3\xa1 a sua recompensa...' },
    3206: {
        QUEST: 'Parece que _toNpcName_ est\xc3\xa1 tendo problemas com alguns Cogs.\x7V\xc3\xa1 ver se voc\xc3\xaa pode ajud\xc3\xa1-lo._where_' },
    3207: {
        QUEST: 'Oi, _avName_! Obrigado por vir!\x7Um monte de Duplos Sentidos invadiu minha loja e roubou uma pilha de cart\xc3\xb5es-postais de meu balc\xc3\xa3o.\x7V\xc3\xa1 e derrote todos os Duplos Sentidos e recupere meus cart\xc3\xb5es-postais!',
        INCOMPLETE_PROGRESS: 'N\xc3\xa3o h\xc3\xa1 cart\xc3\xb5es-postais suficientes! Continue procurando!',
        COMPLETE: 'Ah, valeu! Agora eu posso entregar a correspond\xc3\xaancia na hora certa! Aqui est\xc3\xa1 a sua recompensa...' },
    3208: {
        QUEST: 'Ultimamente temos recebido reclama\xc3\xa7\xc3\xb5es dos moradores sobre os Reis da Incerta.\x7Veja se consegue derrotar 10 Reis da Incerta para ajudar nossos colegas Toons nos Jardins da Margarida.' },
    3209: {
        QUEST: 'Valeu mesmo por derrotar os Reis da Incerta!\x7Mas agora os Operadores de Telemarketing ficaram fora de controle.\x7Derrote 10 Operadores de Telemarketing nos Jardins da Margarida e volte aqui para pegar sua recompensa.' },
    3247: {
        QUEST: 'Ultimamente, temos recebido reclama\xc3\xa7\xc3\xb5es dos moradores sobre os Sanguessugas.\x7Veja se consegue derrotar 20 Sanguessugas para ajudar nossos colegas Toons nos Jardins da Margarida.' },
    3210: {
        QUEST: 'Oh, n\xc3\xa3o, a Seivas Florais da Rua das Amendoeiras est\xc3\xa1 sem flores!\x7Para ajudar, leve dez de suas flores com esguicho.\x7Mas veja primeiramente se tem realmente 10 flores com esguicho em seu estoque.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Preciso ter 10 flores com esguicho. Voc\xc3\xaa n\xc3\xa3o tem o suficiente!' },
    3211: {
        QUEST: 'Puxa, valeu mesmo, viu? Estas flores com esguicho v\xc3\xa3o salvar a p\xc3\xa1tria.\x7Mas estou com medo daqueles Cogs l\xc3\xa1 fora.\x7Voc\xc3\xaa pode me ajudar e derrotar alguns desses Cogs?\x7Volte aqui depois de derrotar 20 Cogs nesta rua.',
        INCOMPLETE_PROGRESS: 'Ainda h\xc3\xa1 Cogs l\xc3\xa1 fora para serem derrotados! Continue trabalhando!',
        COMPLETE: 'Ah, valeu! Isso ajudou muito. Sua recompensa \xc3\xa9...' },
    3212: {
        QUEST: '_toNpcName_ precisa de ajuda para procurar por algo que ela perdeu.\x7V\xc3\xa1 visit\xc3\xa1-la e veja o que pode fazer._where_' },
    3213: {
        QUEST: 'Oi, _avName_. Voc\xc3\xaa pode me ajudar?\x7N\xc3\xa3o sei onde coloquei minha caneta. Acho que alguns Cogs pegaram-na.\x7Derrote Cogs para encontrar minha caneta roubada.',
        INCOMPLETE_PROGRESS: 'Voc\xc3\xaa j\xc3\xa1 encontrou minha caneta?' },
    3214: {
        QUEST: 'Sim, \xc3\xa9 a minha caneta! Valeu!\x7Mas, enquanto voc\xc3\xaa estava fora, eu percebi que meu tinteiro tamb\xc3\xa9m desapareceu.\x7Derrote Cogs para encontrar meu tinteiro.',
        INCOMPLETE_PROGRESS: 'Ainda estou procurando meu tinteiro!' },
    3215: {
        QUEST: 'Demais! Agora tenho minha caneta e meu tinteiro de volta!\x7Mas voc\xc3\xaa nem vai acreditar!\x7Meu bloco de notas sumiu! Eles devem t\xc3\xaa-lo roubado tamb\xc3\xa9m!\x7Derrote Cogs para encontrar meu bloco de notas roubado e, ent\xc3\xa3o, traga-o de volta para ter sua recompensa.',
        INCOMPLETE_PROGRESS: 'E meu bloco de notas?' },
    3216: {
        QUEST: '\xc3\x89 o meu bloco de notas! Maneiro! Sua recompensa \xc3\xa9...\x7Ei! Onde ela est\xc3\xa1?\x7Sua recompensa estava bem aqui no cofre de meu escrit\xc3\xb3rio. Mas o cofre inteiro sumiu!\x7D\xc3\xa1 para acreditar? Aqueles cogs roubaram sua recompensa!\x7Derrote Cogs para recuperar meu cofre.\x7Quando voc\xc3\xaa o trouxer de volta, eu lhe darei sua recompensa.',
        INCOMPLETE_PROGRESS: 'Continue procurando o cofre! Sua recompensa est\xc3\xa1 l\xc3\xa1 dentro!',
        COMPLETE: 'Finalmente! Seu novo saco de piadas est\xc3\xa1 dentro daquele cofre. Aqui est\xc3\xa1...' },
    3217: {
        QUEST: 'Temos feito alguns estudos sobre a mec\xc3\xa2nica dos Rob\xc3\xb4s Vendedores.\x7N\xc3\xb3s ainda precisamos estudar algumas pe\xc3\xa7as de forma mais detalhada.\x7Traga-nos uma roda dentada de algum Dr. Sabe-com-quem-est\xc3\xa1-falando.\x7Voc\xc3\xaa poder\xc3\xa1 conseguir uma quando o Cog estiver explodindo.' },
    3218: {
        QUEST: 'Muito bom! Agora precisamos de uma roda dentada de um Amigo da On\xc3\xa7a.\x7Estas s\xc3\xa3o mais dif\xc3\xadceis de conseguir, portanto, continue tentando.' },
    3219: {
        QUEST: 'Demais! Agora precisamos de apenas mais uma roda dentada.\x7Desta vez, precisamos de uma de um Agitador.\x7Talvez voc\xc3\xaa precise procurar esses Cogs nos edif\xc3\xadcios dos Rob\xc3\xb4s Vendedores.\x7Quando achar a roda, traga-a aqui para receber sua recompensa.' },
    3244: {
        QUEST: 'Temos feito alguns estudos sobre a mec\xc3\xa2nica dos Rob\xc3\xb4s da Lei.\x7N\xc3\xb3s ainda precisamos estudar algumas pe\xc3\xa7as de forma mais detalhada.\x7Traga-nos uma roda dentada de algum Perseguidor de Ambul\xc3\xa2ncias.\x7Voc\xc3\xaa poder\xc3\xa1 conseguir uma quando o Cog estiver explodindo.' },
    3245: {
        QUEST: 'Muito bom! Agora precisamos de uma roda dentada de um Golpe Sujo.\x7Estas s\xc3\xa3o mais dif\xc3\xadceis de conseguir, portanto, continue tentando.' },
    3246: {
        QUEST: 'Demais! Agora precisamos de apenas mais uma roda dentada.\x7Desta vez, de um Rela\xc3\xa7\xc3\xb5es P\xc3\xbablicas.\x7Quando peg\xc3\xa1-la, traga-a aqui para conseguir sua recompensa.' },
    3220: {
        QUEST: 'Acabei de saber que _toNpcName_ estava perguntando por voc\xc3\xaa.\x7Por que voc\xc3\xaa n\xc3\xa3o passa por l\xc3\xa1 e v\xc3\xaa o que ela quer?_where_' },
    3221: {
        QUEST: 'Oi, _avName_! A\xc3\xad est\xc3\xa1 voc\xc3\xaa!\x7Ouvi dizer que voc\xc3\xaa \xc3\xa9 especialista em ataques com esguicho.\x7Preciso de algu\xc3\xa9m para dar um bom exemplo a todos os Toons nos Jardins da Margarida.\x7Use seus ataques com esguicho para derrotar v\xc3\xa1rios Cogs.\x7Incentive seus amigos a usarem o esguicho tamb\xc3\xa9m.\x7Quando tiver derrotado 20 Cogs, volte aqui para pegar sua recompensa!' },
    3222: {
        QUEST: '\xc3\x89 hora de demonstrar sua Toonmizade.\x7Se voc\xc3\xaa recuperar, com sucesso, um n\xc3\xbamero de edif\xc3\xadcios de Cogs, ganhar\xc3\xa1 o direito de fazer tr\xc3\xaas buscas.\x7Primeiramente, derrote dois edif\xc3\xadcios de Cogs.\x7Sinta-se \xc3\xa0 vontade para chamar seus amigos para ajud\xc3\xa1-lo.' },
    3223: {
        QUEST: 'Bom trabalho naqueles edif\xc3\xadcios!\x7Agora, derrote mais dois.\x7Os edif\xc3\xadcios devem ter, pelo menos, dois andares.' },
    3224: {
        QUEST: 'Fant\xc3\xa1stico!\x7Agora \xc3\xa9 s\xc3\xb3 derrotar mais dois edif\xc3\xadcios.\x7Eles devem ter, pelo menos, tr\xc3\xaas andares.\x7Quando terminar, volte para pegar sua recompensa!',
        COMPLETE: 'Voc\xc3\xaa conseguiu, _avName_!\x7Voc\xc3\xaa demonstrou uma elevada Toonmizade.',
        GREETING: '' },
    3225: {
        QUEST: '_toNpcName_ diz que precisa de ajuda.\x7Por que voc\xc3\xaa n\xc3\xa3o vai at\xc3\xa9 l\xc3\xa1 e v\xc3\xaa o que pode fazer para ajud\xc3\xa1-la?_where_' },
    3235: {
        QUEST: 'Ah, esta \xc3\xa9 a salada que pedi!\x7Obrigada por traz\xc3\xaa-la para mim.\x7Todos esses Cogs devem ter amedrontado novamente o entregador de _toNpcName_ .\x7Por que voc\xc3\xaa n\xc3\xa3o nos faz um favor e derrota alguns desses Cogs l\xc3\xa1 fora?\x7Derrote 10 Cogs nos Jardins da Margarida e, ent\xc3\xa3o, v\xc3\xa1 at\xc3\xa9 _toNpcName_.',
        INCOMPLETE_PROGRESS: 'Voc\xc3\xaa est\xc3\xa1 trabalhando na elimina\xc3\xa7\xc3\xa3o de Cogs para mim?\x7Isto \xc3\xa9 maravilhoso! Continue com o bom trabalho!',
        COMPLETE: 'Oh, muito obrigada por derrotar aqueles Cogs!\x7Agora, acho que poderei manter minha escala normal de entregas.\x7Sua recompensa \xc3\xa9...',
        INCOMPLETE_WRONG_NPC: 'V\xc3\xa1 contar a _toNpcName_ sobre os Cogs que voc\xc3\xaa derrotou._where_' },
    3236: {
        QUEST: 'H\xc3\xa1 muitos Rob\xc3\xb4s da Lei por a\xc3\xad.\x7Voc\xc3\xaa pode fazer sua parte para ajudar!\x7Derrote 3 edif\xc3\xadcios de Rob\xc3\xb4s da Lei.' },
    3237: {
        QUEST: 'Bom trabalho naqueles edif\xc3\xadcios de Rob\xc3\xb4s da Lei!\x7Mas agora h\xc3\xa1 muitos Rob\xc3\xb4s Vendedores!\x7Derrote 3 edif\xc3\xadcios de Rob\xc3\xb4s Vendedores e volte para buscar sua recompensa.' },
    3238: {
        QUEST: 'Ah n\xc3\xa3o! Um Cog "Amizade F\xc3\xa1cil" roubou a Chave para os Jardins da Margarida!\x7Veja se voc\xc3\xaa consegue recuper\xc3\xa1-la.\x7Lembre-se, o Amizade F\xc3\xa1cil s\xc3\xb3 pode ser encontrado dentro dos edif\xc3\xadcios de Rob\xc3\xb4s Vendedores.' },
    3239: {
        QUEST: 'Voc\xc3\xaa achou uma chave, tudo bem, mas esta n\xc3\xa3o \xc3\xa9 a correta!\x7Precisamos da chave dos Jardins da Margarida.\x7Continue de olho! Ela ainda est\xc3\xa1 com algum Cog "Amizade F\xc3\xa1cil"!' },
    3242: {
        QUEST: 'Ah n\xc3\xa3o! Um Cog Macaco velho roubou a Chave para os Jardins da Margarida!\x7Veja se voc\xc3\xaa consegue recuper\xc3\xa1-la.\x7Lembre-se, os Macacos-velhos s\xc3\xb3 podem ser encontrados dentro dos edif\xc3\xadcios de Rob\xc3\xb4s da Lei.' },
    3243: {
        QUEST: 'Voc\xc3\xaa achou uma chave, tudo bem, mas esta n\xc3\xa3o \xc3\xa9 a correta!\x7Precisamos da chave dos Jardins da Margarida.\x7Continue de olho! Ela ainda est\xc3\xa1 com algum Cog Macaco velho!' },
    3240: {
        QUEST: 'Acabei de saber que um Macaco velho roubou um saco de ra\xc3\xa7\xc3\xa3o para p\xc3\xa1ssaros de _toNpcName_ .\x7Derrote Macacos velhos at\xc3\xa9 recuperar a ra\xc3\xa7\xc3\xa3o para p\xc3\xa1ssaros do Flor\xc3\xaancio e lev\xc3\xa1-la de volta para ele.\x7Os Macacos velhos s\xc3\xb3 s\xc3\xa3o encontrados dentro de edif\xc3\xadcios de Rob\xc3\xb4s da Lei._where_',
        COMPLETE: 'Ah, muito obrigado por encontrar minha ra\xc3\xa7\xc3\xa3o para p\xc3\xa1ssaros!\x7Sua recompensa \xc3\xa9...',
        INCOMPLETE_WRONG_NPC: 'Bom trabalho na recupera\xc3\xa7\xc3\xa3o da ra\xc3\xa7\xc3\xa3o para p\xc3\xa1ssaros!\x7Agora, leve-a para _toNpcName_._where_' },
    3241: {
        QUEST: 'Alguns dos edif\xc3\xadcios de Cogs est\xc3\xa3o ficando altos demais e isso j\xc3\xa1 est\xc3\xa1 incomodando.\x7Veja se voc\xc3\xaa consegue derrubar alguns dos edif\xc3\xadcios mais altos.\x7Recupere 5 edif\xc3\xadcios de 3 andares, ou mais altos, e volte para pegar sua recompensa.' },
    3250: {
        QUEST: 'A Detetive Linda da Rua dos Carvalhos recebeu informa\xc3\xa7\xc3\xb5es sobre um Quartel de Rob\xc3\xb4s Vendedores.\x7V\xc3\xa1 at\xc3\xa9 l\xc3\xa1 e ajude-a a investigar.' },
    3251: {
        QUEST: 'H\xc3\xa1 algo estranho acontecendo por aqui.\x7H\xc3\xa1 tantos Rob\xc3\xb4s Vendedores!\x7Ouvi dizer que eles organizaram seu pr\xc3\xb3prio quartel no final desta rua.\x7V\xc3\xa1 at\xc3\xa9 l\xc3\xa1 e veja o que consegue descobrir.\x7Encontre Cogs Rob\xc3\xb4s Vendedores em seu quartel, derrote 5 deles e volte aqui.' },
    3252: {
        QUEST: 'Ok, desembucha.\x7O que voc\xc3\xaa disse?\x7Quartel de Rob\xc3\xb4s Vendedores?? Ah n\xc3\xa3o!!! Algo tem que ser feito.\x7Devemos avisar a Ju\xc3\xadza Gala. Ela saber\xc3\xa1 o que fazer.\x7V\xc3\xa1 at\xc3\xa9 l\xc3\xa1 e conte a ela o que descobrimos. \xc3\x89 s\xc3\xb3 descer a rua.' },
    3253: {
        QUEST: 'Sim, posso ajud\xc3\xa1-lo? Estou muito ocupada.\x7H\xc3\xa3? Quartel de Cogs?\x7H\xc3\xa3? Besteira. Isto nunca poderia acontecer.\x7Voc\xc3\xaa deve estar enganado. Absurdo.\x7H\xc3\xa3? N\xc3\xa3o discuta comigo.\x7Ok, ent\xc3\xa3o, traga alguma prova.\x7Se os Rob\xc3\xb4s Vendedores realmente est\xc3\xa3o construindo este Quartel de Cogs, qualquer Cog de l\xc3\xa1 estar\xc3\xa1 carregando mapas.\x7Cogs amam trabalhar com papelada, sabe?\x7Derrote Rob\xc3\xb4s Vendedores at\xc3\xa9 encontrar os mapas.\x7Traga-os aqui, e eu talvez acredite em voc\xc3\xaa.' },
    3254: {
        QUEST: 'Voc\xc3\xaa de novo, h\xc3\xa3? Mapas? Voc\xc3\xaa est\xc3\xa1 com eles?\x7Deixe-me v\xc3\xaa-los! Humm... Uma f\xc3\xa1brica?\x7Deve ser l\xc3\xa1 que eles est\xc3\xa3o construindo os Rob\xc3\xb4s Vendedores... E o que \xc3\xa9 isso?\x7Sim, exatamente como eu suspeitava. Eu sabia o tempo todo.\x7Eles est\xc3\xa3o construindo um Quartel de Rob\xc3\xb4s Vendedores.\x7Isso n\xc3\xa3o \xc3\xa9 bom. Preciso fazer algumas liga\xc3\xa7\xc3\xb5es. Estou muito ocupada. Adeus!\x7H\xc3\xa3? Ah sim, leve estes mapas de volta para a Detetive Linda.\x7Ela poder\xc3\xa1 decifr\xc3\xa1-los melhor.',
        COMPLETE: 'O que a Ju\xc3\xadza Gala disse?\x7N\xc3\xb3s t\xc3\xadnhamos raz\xc3\xa3o? Ah, n\xc3\xa3o. Vamos ver estes mapas.\x7Humm... Parece que os Rob\xc3\xb4s Vendedores constru\xc3\xadram uma f\xc3\xa1brica com maquin\xc3\xa1rio para fazer Cogs.\x7Parece muito perigoso. Fique de fora at\xc3\xa9 que voc\xc3\xaa tenha mais Pontos de risadas.\x7Quando voc\xc3\xaa tiver mais Pontos de risadas, teremos muito mais a aprender sobre o Quartel dos Rob\xc3\xb4s Vendedores.\x7Aqui est\xc3\xa1 sua recompensa. Bom trabalho!' },
    3255: {
        QUEST: '_toNpcName_ est\xc3\xa1 investigando o ' + lSellbotHQ + '.\x7Veja se voc\xc3\xaa consegue ajudar._where_' },
    3256: {
        QUEST: '_toNpcName_ est\xc3\xa1 investigando o ' + lSellbotHQ + '.\x7Veja se voc\xc3\xaa consegue ajudar._where_' },
    3257: {
        QUEST: '_toNpcName_ est\xc3\xa1 investigando o ' + lSellbotHQ + '.\x7Veja se voc\xc3\xaa consegue ajudar._where_' },
    3258: {
        QUEST: 'H\xc3\xa1 muita confus\xc3\xa3o sobre o que os Cogs pretendem com seu novo Quartel.\x7Preciso que voc\xc3\xaa traga algumas informa\xc3\xa7\xc3\xb5es diretamente deles.\x7Se n\xc3\xb3s conseguirmos quatro memorandos internos de Rob\xc3\xb4s Vendedores dentro de seu Quartel, isso ajudar\xc3\xa1 a esclarecer as coisas.\x7Traga o primeiro memorando para mim para que possamos nos informar melhor.' },
    3259: {
        QUEST: 'Demais! Vamos ver o que diz o memorando...\x7"A/C Rob\xc3\xb4s Vendedores:"\x7"Estarei em meu escrit\xc3\xb3rio no topo das Torres Rob\xc3\xb4s Vendedores promovendo Cogs a n\xc3\xadveis mais altos."\x7"Quando voc\xc3\xaa tiver m\xc3\xa9ritos suficientes, entre no elevador do sagu\xc3\xa3o para falar comigo".\x7"O intervalo chegou ao fim. De volta ao trabalho!"\x7"Assinado, Rob\xc3\xb4 Vendedor VP"\x7Ah\xc3\xa1.... Flippy vai querer ver isto. Enviarei a ele imediatamente.\x7V\xc3\xa1 buscar o segundo memorando e traga aqui.' },
    3260: {
        QUEST: 'Que bom, voc\xc3\xaa est\xc3\xa1 de volta. Deixe-me ver o que voc\xc3\xaa encontrou....\x7"A/C Rob\xc3\xb4s Vendedores:"\x7"As Torres Rob\xc3\xb4s Vendedores instalaram um novo sistema de seguran\xc3\xa7a para afastar todos os Toons."\x7"Os Toons que forem encontrados nas Torres Rob\xc3\xb4s Vendedores ser\xc3\xa3o detidos para interrogat\xc3\xb3rio".\x7"Encontrem-se no sagu\xc3\xa3o para um coquetel, no qual discutiremos o assunto."\x7"Assinado, Amizade F\xc3\xa1cil"\x7Muito interessante... Passarei imediatamente esta informa\xc3\xa7\xc3\xa3o adiante.\x7Traga o terceiro memorando.' },
    3261: {
        QUEST: 'Excelente trabalho _avName_! O que diz o memorando?\x7"A/C Rob\xc3\xb4s Vendedores:"\x7"De algum modo, os Toons encontraram um jeito de se infiltrarem nas Torres Rob\xc3\xb4s Vendedores."\x7"Ligarei para voc\xc3\xaas esta noite na hora do jantar para fornecer os detalhes."\x7"Assinado, Operador de Telemarketing"\x7Humm... Queria saber como os Toons est\xc3\xa3o conseguindo se infiltrar....\x7Traga mais um memorando e acho que assim teremos informa\xc3\xa7\xc3\xb5es suficientes.',
        COMPLETE: 'Eu sabia que voc\xc3\xaa conseguiria! Ok, o memorando diz...\x7"A/C Rob\xc3\xb4s Vendedores:"\x7"Ontem, estava almo\xc3\xa7ando com Dr. Celebridade."\x7"Ele disse que o VP tem estado bastante ocupado nestes dias."\x7"Ele s\xc3\xb3 receber\xc3\xa1 os Cogs que merecem promo\xc3\xa7\xc3\xa3o."\x7"Esqueci de dizer, o Amigo da On\xc3\xa7a jogar\xc3\xa1 golfe comigo no domingo."\x7"Assinado, Dr. Sabe-com-quem-est\xc3\xa1-falando"\x7Bem... _avName_, isto foi muito \xc3\xbatil.\x7Aqui est\xc3\xa1 sua recompensa.' },
    3262: {
        QUEST: '_toNpcName_ tem novas informa\xc3\xa7\xc3\xb5es sobre a F\xc3\xa1brica do ' + lSellbotHQ + '.\x7V\xc3\xa1 ver o que ele tem a dizer._where_' },
    3263: {
        GREETING: 'Ol\xc3\xa1, parceiro!',
        QUEST: 'Eu sou o Treinador Abobrinha, mas voc\xc3\xaa pode me chamar de Treinador A.\x7Eu sou a favor de treinos com a raquete e alongamento, se \xc3\xa9 que voc\xc3\xaa me entende.\x7Ou\xc3\xa7a, os Rob\xc3\xb4s Vendedores terminaram uma enorme f\xc3\xa1brica para produzir Rob\xc3\xb4s Vendedores 24 horas por dia.\x7Re\xc3\xbana um grupo de parceiros Toon e raquetada na f\xc3\xa1brica!\x7Dentro do Quartel do Rob\xc3\xb4 Vendedor, procure pelo t\xc3\xbanel que leva at\xc3\xa9 a f\xc3\xa1brica e, ent\xc3\xa3o, entre no elevador.\x7Voc\xc3\xaa j\xc3\xa1 tem que estar com as piadas e os pontos de risadas completos e ter Toons fortes como guias.\x7Para retardar o progresso dos Rob\xc3\xb4s Vendedores, derrote o Supervisor dentro da f\xc3\xa1brica.\x7Parece um grande exerc\xc3\xadcio, se \xc3\xa9 que fui bem claro.',
        LEAVING: 'Te vejo por a\xc3\xad, parceiro!',
        COMPLETE: 'Ei, parceiro, bom trabalho naquela F\xc3\xa1brica!\x7Parece que voc\xc3\xaa encontrou parte de um terno de Cog.\x7Deve ser uma sobra do processo de fabrica\xc3\xa7\xc3\xa3o de Cogs.\x7Isto pode vir a calhar. Continue coletando estas partes quando tiver um tempo livre.\x7Quem sabe, quando voc\xc3\xaa coletar um terno de Cog completo, poder\xc3\xa1 vir a ser \xc3\xbatil para alguma coisa....' },
    4001: {
        GREETING: '',
        QUEST: 'Agora, voc\xc3\xaa tem que escolher o pr\xc3\xb3ximo tipo de piada que deseja aprender.\x7Decida e depois volte aqui quando estiver pronto para escolher.',
        INCOMPLETE_PROGRESS: 'Pense bem sobre sua decis\xc3\xa3o antes de escolher.',
        INCOMPLETE_WRONG_NPC: 'Pense bem sobre sua decis\xc3\xa3o antes de escolher.',
        COMPLETE: 'Uma boa decis\xc3\xa3o...',
        LEAVING: QuestsDefaultLeaving },
    4002: {
        GREETING: '',
        QUEST: 'Agora voc\xc3\xaa tem que escolher o pr\xc3\xb3ximo tipo de piada que deseja aprender.\x7Decida e depois volte aqui quando estiver pronto para escolher.',
        INCOMPLETE_PROGRESS: 'Pense bem sobre sua decis\xc3\xa3o antes de escolher.',
        INCOMPLETE_WRONG_NPC: 'Pense bem sobre sua decis\xc3\xa3o antes de escolher.',
        COMPLETE: 'Uma boa decis\xc3\xa3o...',
        LEAVING: QuestsDefaultLeaving },
    4200: {
        QUEST: 'Aposto que o Tom iria gostar de ter alguma ajuda na pesquisa que ele est\xc3\xa1 fazendo._where_' },
    4201: {
        GREETING: 'Tudo certo?',
        QUEST: 'Estou bastante preocupado com a onda de roubos de instrumentos musicais.\x7Estou conduzindo uma pesquisa com meus amigos comerciantes.\x7Talvez seja poss\xc3\xadvel encontrar um padr\xc3\xa3o para me ajudar a resolver este caso.\x7Pe\xc3\xa7a a Tina o controle de estoque de concertina._where_' },
    4202: {
        QUEST: 'Sim, eu falei com Tom nesta manh\xc3\xa3.\x7O estoque est\xc3\xa1 bem aqui.\x7Leve para ele imediatamente, ok?_where_' },
    4203: {
        QUEST: 'Demais! Um a menos...\x7Agora pe\xc3\xa7a o da Cavaca._where_' },
    4204: {
        QUEST: 'Ah! O estoque!\x7Esqueci completamente.\x7Aposto que consigo fazer enquanto voc\xc3\xaa derrota 10 cogs.\x7Passe por aqui depois, e eu prometo que estar\xc3\xa1 pronto.',
        INCOMPLETE_PROGRESS: '31, 32... DROGA!\x7Voc\xc3\xaa me fez perder a conta!',
        GREETING: '' },
    4205: {
        QUEST: 'Ah, a\xc3\xad est\xc3\xa1 voc\xc3\xaa.\x7Obrigada por me dar algum tempo.\x7Leve isto para o Tom e diga ol\xc3\xa1 por mim._where_' },
    4206: {
        QUEST: 'Humm, muito interessante.\x7Agora estamos chegando a algum lugar.\x7Ok, o \xc3\xbaltimo estoque \xc3\xa9 o da Fifi._where_' },
    4207: {
        QUEST: 'Estoque?\x7Como posso fazer o estoque se n\xc3\xa3o tenho o formul\xc3\xa1rio?\x7V\xc3\xa1 at\xc3\xa9 o Clave e veja se ele tem um para mim._where_',
        INCOMPLETE_PROGRESS: 'Algum sinal daquele formul\xc3\xa1rio?' },
    4208: {
        QUEST: 'Claro que eu tenho um formul\xc3\xa1rio de estoque, monsenhor!\x7Mas eles n\xc3\xa3o s\xc3\xa3o de gra\xc3\xa7a, sabe?.\x7Fa\xc3\xa7amos o seguinte. Eu troco por uma torta de creme inteira.',
        GREETING: 'Ei, monsenhor!',
        LEAVING: 'Boa sorte...',
        INCOMPLETE_PROGRESS: 'Um peda\xc3\xa7o n\xc3\xa3o adianta.\x7Estou com fome, monsenhor. Eu preciso da torta INTEIRA.' },
    4209: {
        GREETING: '',
        QUEST: 'Humm...\x7Muito gostoso!\x7Aqui est\xc3\xa1 o formul\xc3\xa1rio para Fifi._where_' },
    4210: {
        GREETING: '',
        QUEST: 'Valeu, foi uma grande ajuda.\x7Vamos ver...Violinos: 2\x7Tudo pronto! Aqui est\xc3\xa1!',
        COMPLETE: 'Bom trabalho, _avName_.\x7Tenho certeza de que solucionarei este caso agora.\x7Por que voc\xc3\xaa n\xc3\xa3o o soluciona?' },
    4211: {
        QUEST: 'Veja, o Dr. Triturador est\xc3\xa1 ligando de cinco em cinco minutos. Voc\xc3\xaa pode conversar com ele e ver qual o problema?_where_' },
    4212: {
        QUEST: 'Puxa! Estou feliz de ver que o Quartel dos Toons finalmente mandou algu\xc3\xa9m.\x7N\xc3\xa3o tenho um cliente h\xc3\xa1 dias.\x7S\xc3\xa3o estes malditos Destruidores de N\xc3\xbameros que est\xc3\xa3o em todo lugar.\x7Acho que eles est\xc3\xa3o ensinando maus h\xc3\xa1bitos de higiene oral a nossos moradores.\x7Derrote dez deles e vamos ver se o neg\xc3\xb3cio anda.',
        INCOMPLETE_PROGRESS: 'Ainda sem clientes. Mas continue assim!' },
    4213: {
        QUEST: 'Sabe, talvez n\xc3\xa3o sejam os Destruidores de N\xc3\xbameros, no final das contas.\x7Talvez sejam apenas os Rob\xc3\xb4s Mercen\xc3\xa1rios em geral.\x7Derrote vinte deles e, com alguma sorte, algu\xc3\xa9m vir\xc3\xa1, pelo menos, para um check-up.',
        INCOMPLETE_PROGRESS: 'Eu sei que vinte \xc3\xa9 muito. Mas tenho certeza de que vai valer a pena.' },
    4214: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Eu n\xc3\xa3o consigo entender!\x7Ainda n\xc3\xa3o h\xc3\xa1 UM BENDITO fregu\xc3\xaas.\x7Talvez precisemos ir at\xc3\xa9 a fonte.\x7Tente recuperar um edif\xc3\xadcio Cog de Rob\xc3\xb4s Mercen\xc3\xa1rios.\x7Isso deve funcionar...',
        INCOMPLETE_PROGRESS: 'Oh, por favor! Apenas um m\xc3\xadsero prediozinho...',
        COMPLETE: 'Ainda n\xc3\xa3o h\xc3\xa1 uma alma sequer aqui.\x7Mas, pense bem.\x7Eu n\xc3\xa3o tinha mesmo clientes antes da invas\xc3\xa3o dos cogs!\x7Realmente agrade\xc3\xa7o toda a sua ajuda.\x7Isto deve ajudar voc\xc3\xaa a prosseguir.' },
    4215: {
        QUEST: 'A Ana precisa desesperadamente da ajuda de algu\xc3\xa9m.\x7Por que voc\xc3\xaa n\xc3\xa3o passa l\xc3\xa1 e v\xc3\xaa o que pode fazer?_where_' },
    4216: {
        QUEST: 'Obrigada por chegar t\xc3\xa3o r\xc3\xa1pido!\x7Parece que os cogs sumiram com v\xc3\xa1rias passagens dos meus clientes.\x7A Cavaca disse que viu um Amigo da On\xc3\xa7a saindo daqui com as garras cheias de passagens.\x7Veja se voc\xc3\xaa consegue recuperar a passagem do Al\xc3\xaa Nhador para o Alasca.',
        INCOMPLETE_PROGRESS: 'Aqueles Amigos da On\xc3\xa7a podem estar em qualquer lugar agora...' },
    4217: {
        QUEST: 'Legal! Voc\xc3\xaa encontrou!\x7Agora seja um cavalheiro e entregue ao Al\xc3\xaa Nhador para mim, est\xc3\xa1 bem?_where_' },
    4218: {
        QUEST: 'Genial, estupendo, fabuloso!\x7Alasca, aqui vou eu!\x7N\xc3\xa3o aguento mais esses cogs infernais.\x7Olha, acho que a Ana precisa de voc\xc3\xaa de novo._where_' },
    4219: {
        QUEST: 'Exatamente, voc\xc3\xaa adivinhou!\x7Preciso de voc\xc3\xaa para derrotar aquelas pestes dos Amigos da On\xc3\xa7a para recuperar a passagem da T\xc3\xa1bata para o Festival de Jazz.\x7Voc\xc3\xaa sabe como fazer...',
        INCOMPLETE_PROGRESS: 'H\xc3\xa1 mais l\xc3\xa1 fora, em algum lugar...' },
    4220: {
        QUEST: 'Gracinha!\x7Voc\xc3\xaa poderia entregar este tamb\xc3\xa9m?_where_' },
    4221: {
        GREETING: '',
        LEAVING: 'Fica frio...',
        QUEST: 'Legal, cara!\x7Agora estou na cidade dos gordinhos, _avName_.\x7Antes de sair fora, \xc3\xa9 melhor falar com a Ana Banana de novo..._where_' },
    4222: {
        QUEST: 'Este \xc3\xa9 o \xc3\xbaltimo, prometo!\x7Agora procure pela passagem do Barry para o grande concurso de cantores.',
        INCOMPLETE_PROGRESS: 'Vamos l\xc3\xa1, _avName_.\x7O Barry est\xc3\xa1 contando com voc\xc3\xaa.' },
    4223: {
        QUEST: 'Isto deve alegrar o Barry._where_' },
    4224: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Ol\xc3\xa1, Ol\xc3\xa1, OL\xc3\x81!\x7Magn\xc3\xadfico!\x7S\xc3\xb3 conhe\xc3\xa7o eu mesmo e os caras que v\xc3\xa3o fazer a faxina. \x7A Ana disse para voc\xc3\xaa passar l\xc3\xa1 e pegar a sua recompensa._where_\x7Tchau, Tchau, TCHAU!',
        COMPLETE: 'Obrigado por toda a sua ajuda, _avName_.\x7Voc\xc3\xaa \xc3\xa9 realmente um tesouro aqui de Toontown.\x7Falando em tesouros...' },
    902: {
        QUEST: 'V\xc3\xa1 ver o L\xc3\xa9o.\x7Ele precisa de algu\xc3\xa9m para entregar uma mensagem para ele._where_' },
    4903: {
        QUEST: 'Cara!\x7Minhas castanholas est\xc3\xa3o foscas e tenho um grande show hoje \xc3\xa0 noite.\x7Leve-as para o Carlos e veja se ele pode dar um polimento nelas._where_' },
    4904: {
        QUEST: 'Sim, acho que posso polir esta pe\xc3\xa7a. Mas preciso de alguma tinta azul de lula',
        GREETING: 'Ol\xc3\xa1!',
        LEAVING: 'Tchau!',
        INCOMPLETE_PROGRESS: 'Voc\xc3\xaa pode achar uma lula perto de algum p\xc3\xader de pesca.' },
    4905: {
        QUEST: 'Claro! Isso mesmo!\x7Agora, preciso de um minuto para polir isto. Por que voc\xc3\xaa n\xc3\xa3o trabalha na recupera\xc3\xa7\xc3\xa3o de um pr\xc3\xa9dio de um andar enquanto trabalho por aqui?',
        GREETING: 'Ola!',
        LEAVING: 'Tchau!',
        INCOMPLETE_PROGRESS: 'S\xc3\xb3 mais um minutinho...' },
    4906: {
        QUEST: 'Muito bom!\x7Aqui est\xc3\xa3o as castanholas do L\xc3\xa9o._onde_' },
    4907: {
        GREETING: '',
        QUEST: 'Maneiro, cara!\x7Elas est\xc3\xa3o incr\xc3\xadveis!\x7Agora preciso que voc\xc3\xaa consiga uma c\xc3\xb3pia da letra da \xe2\x80\x9cM\xc3\xbasica de Natal\xe2\x80\x9d da Heidi._where_' },
    4908: {
        QUEST: 'E a\xc3\xad pessoal!\x7Humm, Eu n\xc3\xa3o tenho uma c\xc3\xb3pia dessa m\xc3\xbasica \xc3\xa0 m\xc3\xa3o.\x7Se voc\xc3\xaa me der um tempinho, eu posso transcrever de cabe\xc3\xa7a.\x7Por que voc\xc3\xaa n\xc3\xa3o d\xc3\xa1 uma voltinha e aproveita para recuperar um edif\xc3\xadcio de dois andares enquanto escrevo?' },
    4909: {
        QUEST: 'Desculpe.\x7Minha mem\xc3\xb3ria est\xc3\xa1 ficando meio confusa.\x7Se voc\xc3\xaa recuperar um edif\xc3\xadcio de tr\xc3\xaas andares, tenho certeza de que estarei pronta quando voltar...' },
    4910: {
        QUEST: 'Tudo pronto!\x7Desculpe a demora.\x7Leve isto para o L\xc3\xa9o._where_',
        GREETING: '',
        COMPLETE: 'Caramba, cara!\x7Meu show vai detonar!\x7Falando em detonar, voc\xc3\xaa pode detonar alguns cogs com isto...' },
    5247: {
        QUEST: 'Este bairro est\xc3\xa1 ficando perigoso...\x7Voc\xc3\xaa deve estar querendo aprender alguns truques novos.\x7_toNpcName_ me ensinou tudo que sei, ent\xc3\xa3o, talvez ele possa ajudar voc\xc3\xaa tamb\xc3\xa9m._where_' },
    5248: {
        GREETING: 'Ah, sim.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Voc\xc3\xaa parece estar empenhado na miss\xc3\xa3o.',
        QUEST: 'Ah, bem-vindo, novo aprendiz.\x7Eu sei de tudo que h\xc3\xa1 para saber sobre o jogo de tortas.\x7Por\xc3\xa9m, antes de come\xc3\xa7armos o seu treinamento, \xc3\xa9 necess\xc3\xa1rio uma pequena demonstra\xc3\xa7\xc3\xa3o.\x7Saia e derrote dez dos maiores Cogs.' },
    5249: {
        GREETING: 'Humm.',
        QUEST: 'Excelente!\x7Agora demonstre sua habilidade como pescador.\x7Coloquei ontem tr\xc3\xaas dados de pel\xc3\xbacia no lago.\x7Pesque-os e traga-os para mim.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Parece que voc\xc3\xaa n\xc3\xa3o \xc3\xa9 t\xc3\xa3o h\xc3\xa1bil com a vara e o molinete.' },
    5250: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Ah\xc3\xa1! Estes dados ficar\xc3\xa3o \xc3\xb3timos pendurados no retrovisor do meu carro de bois!\x7Agora, mostre para mim que voc\xc3\xaa sabe distinguir seus inimigos.\x7Volte quando tiver recuperado dois dos edif\xc3\xadcios mais altos dos Rob\xc3\xb4s da Lei.',
        INCOMPLETE_PROGRESS: 'Os edif\xc3\xadcios deram problema para voc\xc3\xaa?' },
    5258: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Ah\xc3\xa1! Estes dados ficar\xc3\xa3o \xc3\xb3timos pendurados no retrovisor do meu carro de bois!\x7Agora, mostre para mim que voc\xc3\xaa sabe distinguir seus inimigos.\x7Volte quando tiver recuperado dois dos edif\xc3\xadcios mais altos dos Rob\xc3\xb4s-chefes.',
        INCOMPLETE_PROGRESS: 'Os edif\xc3\xadcios deram problema para voc\xc3\xaa?' },
    5259: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Ah\xc3\xa1! Estes dados ficar\xc3\xa3o \xc3\xb3timos pendurados no retrovisor do meu carro de bois!\x7Agora, mostre para mim que voc\xc3\xaa sabe distinguir seus inimigos.\x7Volte quando tiver recuperado dois dos edif\xc3\xadcios mais altos dos Rob\xc3\xb4s Mercen\xc3\xa1rios.',
        INCOMPLETE_PROGRESS: 'Os edif\xc3\xadcios deram problema para voc\xc3\xaa?' },
    5260: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Ah\xc3\xa1! Estes dados ficar\xc3\xa3o \xc3\xb3timos pendurados no retrovisor do meu carro de bois!\x7Agora, mostre para mim que voc\xc3\xaa sabe distinguir seus inimigos.\x7Volte quando tiver recuperado dois dos edif\xc3\xadcios mais altos dos Rob\xc3\xb4s Vendedores.',
        INCOMPLETE_PROGRESS: 'Os edif\xc3\xadcios deram problema para voc\xc3\xaa?' },
    5200: {
        QUEST: 'Aqueles cogs trai\xc3\xa7oeiros est\xc3\xa3o envolvidos nisto novamente.\x7_toNpcName_ percebeu que tem outro item ausente. Pare um pouco aqui e veja se consegue acertar isso._where_' },
    5201: {
        GREETING: '',
        QUEST: 'Oi, _avName_. Acho que eu devo agradecer a voc\xc3\xaa por ter vindo.\x7Um grupo desses Ca\xc3\xa7a-talentos chegou e roubou minha bola de futebol.\x7O l\xc3\xadder disse que eu tinha que fazer alguns cortes e tomou a bola de mim!\x7Voc\xc3\xaa pode trazer de volta a minha bola?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Conseguiu achar minha bola de futebol?',
        COMPLETE: 'Dez! Encontrei! Olha aqui, tome a sua recompensa...' },
    5261: {
        GREETING: '',
        QUEST: 'Oi, _avName_. Acho que eu devo agradecer a voc\xc3\xaa por ter vindo.\x7Um grupo desses Duas Caras chegou e roubou minha bola de futebol.\x7O l\xc3\xadder disse que eu tinha que fazer alguns cortes e tomou a bola de mim!\x7Voc\xc3\xaa pode trazer de volta a minha bola?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Conseguiu achar minha bola de futebol?',
        COMPLETE: 'Dez! Encontrei! Olha aqui, tome a sua recompensa...' },
    5262: {
        GREETING: '',
        QUEST: 'Oi, _avName_. Acho que eu devo agradecer a voc\xc3\xaa por ter vindo.\x7Um grupo desses Sacos de Dinheiro chegou e roubou minha bola de futebol.\x7O l\xc3\xadder disse que eu tinha que fazer alguns cortes e tomou a bola de mim!\x7Voc\xc3\xaa pode trazer de volta a minha bola?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Conseguiu achar minha bola de futebol?',
        COMPLETE: 'Dez! Encontrei! Olha aqui, tome a sua recompensa...' },
    5263: {
        GREETING: '',
        QUEST: 'Oi, _avName_. Acho que eu devo agradecer a voc\xc3\xaa por ter vindo.\x7Um grupo desses Rela\xc3\xa7\xc3\xb5es P\xc3\xbablicas chegou e roubou minha bola de futebol.\x7O l\xc3\xadder disse que eu tinha que fazer alguns cortes e tomou a bola de mim!\x7Voc\xc3\xaa pode trazer de volta a minha bola?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Conseguiu achar minha bola de futebol?',
        COMPLETE: 'Dez! Encontrei! Olha aqui, tome a sua recompensa...' },
    5202: {
        QUEST: 'O Brrrgh foi invadido por alguns dos mais tem\xc3\xadveis Cogs j\xc3\xa1 vistos.\x7Voc\xc3\xaa provavelmente desejar\xc3\xa1 carregar mais piadas consigo.\x7Ouvi falar que _toNpcName_ tem uma sacola grande que voc\xc3\xaa pode usar para carregar mais piadas._where_' },
    5203: {
        GREETING: 'H\xc3\xa3? Voc\xc3\xaa est\xc3\xa1 no meu time de tren\xc3\xb3?',
        QUEST: 'O que \xc3\xa9 isto? Voc\xc3\xaa quer uma bolsa?\x7Eu tinha uma aqui em algum lugar... Acho que est\xc3\xa1 no meu tobog\xc3\xa3?\x7S\xc3\xb3 que... Eu n\xc3\xa3o vejo o meu tobog\xc3\xa3 desde a grande corrida!\x7Talvez um destes Cogs o tenha pego.',
        LEAVING: 'Voc\xc3\xaa viu meu tobog\xc3\xa3?',
        INCOMPLETE_PROGRESS: 'Quem \xc3\xa9 voc\xc3\xaa novamente? Desculpe, estou meio confuso depois da batida.' },
    5204: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Este \xc3\xa9 o meu tobog\xc3\xa3? N\xc3\xa3o vejo nenhuma sacola aqui.\x7Acho que o Cabe\xc3\xa7\xc3\xa3o Kika estava na equipe... Ser\xc3\xa1 que est\xc3\xa1 com ele?_where_' },
    5205: {
        GREETING: 'Ai, minha cabe\xc3\xa7a!',
        LEAVING: '',
        QUEST: 'H\xc3\xa3? Tobi? Ah, a bolsa?\x7Bom, acho que ele estava na nossa equipe de tobog\xc3\xa3?\x7Minha cabe\xc3\xa7a d\xc3\xb3i tanto que n\xc3\xa3o consigo pensar direito.\x7Voc\xc3\xaa consegue para mim alguns cubos de gelo no lago congelado para eu p\xc3\xb4r na minha cabe\xc3\xa7a?',
        INCOMPLETE_PROGRESS: 'Aaiii, minha cabe\xc3\xa7a est\xc3\xa1 me matando! Tem gelo a\xc3\xad?' },
    5206: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Ahhh, agora me sinto bem melhor!\x7Ent\xc3\xa3o voc\xc3\xaa est\xc3\xa1 procurando a bolsa do Tobi, n\xc3\xa9?\x7Acho que ela foi parar na cabe\xc3\xa7a do \xc3\x81lvaro Asno depois da batida._where_' },
    5207: {
        GREETING: 'Iiiiiiiiiip!',
        LEAVING: '',
        QUEST: 'O que \xc3\xa9 bolsa? Quem \xc3\xa9 Cabe\xc3\xa7\xc3\xa3o?\x7Tenho medo de edif\xc3\xadcios! Voc\xc3\xaa detona edif\xc3\xadcio, eu dou bolsa!',
        INCOMPLETE_PROGRESS: 'Mais edif\xc3\xadcios! Ainda com medo!',
        COMPLETE: 'Ooooh! Mim gosta voc\xc3\xaa!' },
    5208: {
        GREETING: '',
        LEAVING: 'Iiiiiiiiiiik!',
        QUEST: 'Ooooh! Mim gosta voc\xc3\xaa!\x7Vai pra Cl\xc3\xadnica do Esqui. Sacola l\xc3\xa1.' },
    5209: {
        GREETING: 'Valeu, garoto!',
        LEAVING: 'At\xc3\xa9 mais!',
        QUEST: 'Cara, o \xc3\x81lvaro Asno \xc3\xa9 doido!\x7Se voc\xc3\xaa fosse maluco que nem o \xc3\x81lvaro, eu daria a bolsa para voc\xc3\xaa, cara.\x7Vai ensacar uns Cogs para poder pegar a sua sacola, cara! Essa agora!',
        INCOMPLETE_PROGRESS: 'Tem certeza de que voc\xc3\xaa \xc3\xa9 radical o bastante para isso? Vai ensacar mais Cogs.',
        COMPLETE: 'Caramba, voc\xc3\xaa \xc3\xa9 irado! Aquilo foi um bando de Cogs que voc\xc3\xaa ensacou!\x7Toma a sua bolsa!' },
    5210: {
        QUEST: '_toNpcName_ est\xc3\xa1 gamada em algu\xc3\xa9m do bairro, mas \xc3\xa9 segredo.\x7Se voc\xc3\xaa ajud\xc3\xa1-la, ela pode lhe dar uma boa recompensa._where_' },
    5211: {
        GREETING: 'Bu\xc3\xa1!',
        QUEST: 'Passei a noite passada inteira escrevendo uma carta para o cachorro que eu amo.\x7Mas, antes mesmo que eu pudesse entregar a ele, um daqueles Cogs asquerosos com bico veio e a tomou de mim.\x7Voc\xc3\xaa consegue peg\xc3\xa1-la de volta para mim?',
        LEAVING: 'Bu\xc3\xa1!',
        INCOMPLETE_PROGRESS: 'Por favor, encontre minha carta.' },
    5264: {
        GREETING: 'Bu\xc3\xa1!',
        QUEST: 'Passei a noite passada inteira escrevendo uma carta para o cachorro que eu amo.\x7Mas, antes mesmo que eu pudesse entregar a ele, um daqueles Cogs asquerosos de barbatana veio e a tomou de mim.\x7Voc\xc3\xaa consegue peg\xc3\xa1-la de volta para mim?',
        LEAVING: 'Bu\xc3\xa1!',
        INCOMPLETE_PROGRESS: 'Por favor, encontre minha carta.' },
    5265: {
        GREETING: 'Bu\xc3\xa1!',
        QUEST: 'Passei a noite passada inteira escrevendo uma carta para o cachorro que eu amo.\x7Mas, antes mesmo que eu pudesse entregar a ele, um daqueles Cogs asquerosos de Amizade F\xc3\xa1cil veio e a tomou de mim.\x7Voc\xc3\xaa consegue peg\xc3\xa1-la de volta para mim?',
        LEAVING: 'Bu\xc3\xa1!',
        INCOMPLETE_PROGRESS: 'Por favor, encontre minha carta.' },
    5266: {
        GREETING: 'Bu\xc3\xa1!',
        QUEST: 'Passei a noite passada inteira escrevendo uma carta para o cachorro que eu amo.\x7Mas, antes mesmo que eu pudesse entregar a ele, um daqueles Cogs Aventureiros Corporativos asquerosos veio e a tomou de mim.\x7Voc\xc3\xaa consegue peg\xc3\xa1-la de volta para mim?',
        LEAVING: 'Bu\xc3\xa1!',
        INCOMPLETE_PROGRESS: 'Por favor, encontre minha carta.' },
    5212: {
        QUEST: 'Oh, obrigada por encontrar a minha carta!\x7Por favor, voc\xc3\xaa poderia entreg\xc3\xa1-la ao c\xc3\xa3o mais lindo do bairro? Por favor! Por favor!',
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Voc\xc3\xaa n\xc3\xa3o entregou a minha carta, n\xc3\xa3o \xc3\xa9?' },
    5213: {
        GREETING: 'Enfeiti\xc3\xa7ado, com certeza.',
        QUEST: 'N\xc3\xa3o posso dar aten\xc3\xa7\xc3\xa3o \xc3\xa0 sua carta, sabe.\x7Todos os meus c\xc3\xa3ezinhos foram levados!\x7Se voc\xc3\xaa os trouxer de volta, a gente volta a conversar.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Tadinhos dos meus c\xc3\xa3ezinhos!' },
    5214: {
        GREETING: '',
        LEAVING: 'Tchauzinho!',
        QUEST: 'Gra\xc3\xa7as a voc\xc3\xaa minhas belezinhas voltaram.\x7Vamos ver a carta agora...\nMmmm, parece que tenho outra admiradora secreta.\x7Isso exigir\xc3\xa1 uma visita ao meu querido amigo Carlo.\x7Aposto como voc\xc3\xaa vai ador\xc3\xa1-lo._where_' },
    5215: {
        GREETING: 'He, he...',
        LEAVING: 'Volte aqui, sim, sim.',
        INCOMPLETE_PROGRESS: 'Ainda h\xc3\xa1 alguns grandalh\xc3\xb5es na \xc3\xa1rea. Volte aqui para falar conosco quando eles forem embora.',
        QUEST: 'Quem mandou voc\xc3\xaa? N\xc3\xa3o gostamos muito de Snobs, n\xc3\xa3o...\x7Mas gostamos menos ainda de Cogs...\x7Expulse os grandalh\xc3\xb5es e ajudaremos voc\xc3\xaas, ajudaremos.' },
    5216: {
        QUEST: 'Falamos que ajudar\xc3\xadamos voc\xc3\xaa.\x7Ent\xc3\xa3o, pegue este anel e leve \xc3\xa0 garota.',
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Voc\xc3\xaa ainda est\xc3\xa1 com o anel???',
        COMPLETE: 'Oh querrrrido!!! Obrigado!!!\x7Ah, tamb\xc3\xa9m tenho algo especial para voc\xc3\xaa.' },
    5217: {
        QUEST: 'Parece que _toNpcName_ pode dar uma ajuda._where_' },
    5218: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Tenho certeza de que h\xc3\xa1 mais Amizades F\xc3\xa1ceis por aqui em algum lugar.',
        QUEST: 'Socorro!!! Socorro!!! Assim n\xc3\xa3o d\xc3\xa1!\x7Esses Amizades F\xc3\xa1ceis est\xc3\xa3o me deixando maluco!!!' },
    5219: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'N\xc3\xa3o s\xc3\xa3o s\xc3\xb3 estes. S\xc3\xb3 vi um!!!',
        QUEST: 'Ah, obrigado, mas agora s\xc3\xa3o os Aventureiros Corporativos!!!\x7Voc\xc3\xaa tem que me ajudar!!!' },
    5220: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'N\xc3\xa3o, n\xc3\xa3o, n\xc3\xa3o, havia um aqui agora mesmo!',
        QUEST: 'Agora, eu percebo que s\xc3\xa3o aqueles Agiotas!!!\x7Pensei que voc\xc3\xaa ia me salvar!!!' },
    5221: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Sabe de uma coisa, talvez n\xc3\xa3o sejam os Cogs coisa nenhuma!\x7Voc\xc3\xaa pode pedir \xc3\xa0 Hil\xc3\xa1ria para fazer para mim uma po\xc3\xa7\xc3\xa3o calmante? Talvez isto ajude...._where_' },
    5222: {
        LEAVING: '',
        QUEST: 'Esse Am\xc3\xa9rico \xc3\xa9 mesmo uma figura!\x7Vou preparar algo que vai dar jeito nele rapidinho!\x7Puxa, parece que estou sem bigodes de sardinha...\x7Seja legal comigo e corra l\xc3\xa1 no lago para pegar alguns para mim.',
        INCOMPLETE_PROGRESS: 'J\xc3\xa1 pegou aqueles bigodes para mim?' },
    5223: {
        QUEST: 'OK. Obrigada!\x7Tome, leve agora para o Am\xc3\xa9rico. Isto deve acalm\xc3\xa1-lo de uma vez por todas.',
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'V\xc3\xa1 logo, leve a po\xc3\xa7\xc3\xa3o para o Am\xc3\xa9rico.' },
    5224: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'V\xc3\xa1 pegar aqueles Macacos velhos para mim, ok?',
        QUEST: 'Puxa vida, gra\xc3\xa7as a Deus voc\xc3\xaa voltou!\x7Passe logo para c\xc3\xa1 esta po\xc3\xa7\xc3\xa3o!!!\x7Glub, glub, glub...\x7Que gosto horr\xc3\xadvel!\x7Sabe de uma coisa? Sinto-me bem mais calmo. Agora que eu posso pensar com mais clareza, me toquei que...\x7Eram os Macacos-velhos que estavam me enlouquecendo todo este tempo!!!',
        COMPLETE: 'Nossa! Agora eu posso relaxar!\x7Tenho certeza de que h\xc3\xa1 alguma coisa aqui que posso dar a voc\xc3\xaa. Aqui, leve isto!' },
    5225: {
        QUEST: 'Desde o acidente com o p\xc3\xa3o de nabo, Felipe Nervosinho ficou furioso com _toNpcName_.\x7Quem sabe voc\xc3\xaa n\xc3\xa3o consegue ajudar o Pio a acertar os ponteiros entre eles?_where_' },
    5226: {
        QUEST: 'Isso mesmo, voc\xc3\xaa deve ter ouvido falar que o Felipe Nervosinho est\xc3\xa1 furioso comigo...\x7Eu estava s\xc3\xb3 tentando ser legal oferecendo o p\xc3\xa3o de nabo.\x7Quem sabe voc\xc3\xaa n\xc3\xa3o consegue alegr\xc3\xa1-lo.\x7O Felipe detesta aqueles Cogs Rob\xc3\xb4s Mercen\xc3\xa1rios, principalmente os edif\xc3\xadcios deles.\x7Se voc\xc3\xaa recuperar alguns edif\xc3\xadcios de Rob\xc3\xb4s Mercen\xc3\xa1rios, talvez ajude.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Quem sabe alguns edif\xc3\xadcios a mais?' },
    5227: {
        QUEST: 'Demais! V\xc3\xa1 dizer ao Felipe o que voc\xc3\xaa fez._where_' },
    5228: {
        QUEST: 'Puxa, ele fez isso mesmo?\x7Esse Pio acha que pode se safar f\xc3\xa1cil, n\xc3\xa9?\x7S\xc3\xb3 quebrou meu dente, s\xc3\xb3 isso que ele fez, com aquele p\xc3\xa3o de nabo dele!\x7Se voc\xc3\xaa levar o meu dente para o Dr. Ban Guela para mim, quem sabe ele consegue dar jeito.',
        GREETING: 'Mmmmrrf.',
        LEAVING: 'Resmungo, resmungo.',
        INCOMPLETE_PROGRESS: 'Voc\xc3\xaa de novo? Pensei que voc\xc3\xaa estava indo levar meu dente para consertar.' },
    5229: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Ainda estou ajeitando o dente. Vai demorar um pouco.',
        QUEST: '\xc3\x89, este dente parece estar ruim mesmo, mas tudo bem.\x7Eu acho que posso fazer uma coisa aqui, mas ainda vai demorar um pouco.\x7Voc\xc3\xaa n\xc3\xa3o quer dar cabo de alguns daqueles Cogs Rob\xc3\xb4s Mercen\xc3\xa1rios das ruas enquanto espera?\x7Eles est\xc3\xa3o assustando os meus clientes.' },
    5267: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Ainda estou ajeitando o dente. Vai demorar um pouco.',
        QUEST: '\xc3\x89, este dente parece estar ruim mesmo, mas tudo bem.\x7Eu acho que posso fazer uma coisa aqui, mas ainda vai demorar um pouco.\x7Voc\xc3\xaa n\xc3\xa3o quer dar cabo de alguns daqueles Cogs Rob\xc3\xb4s Vendedores das ruas enquanto espera?\x7Eles est\xc3\xa3o assustando os meus clientes.' },
    5268: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Ainda estou ajeitando o dente. Vai demorar um pouco.',
        QUEST: '\xc3\x89, este dente parece estar ruim mesmo, mas tudo bem.\x7Eu acho que posso fazer uma coisa aqui, mas ainda vai demorar um pouco.\x7Voc\xc3\xaa n\xc3\xa3o quer dar cabo de alguns daqueles Cogs Rob\xc3\xb4s da Lei das ruas enquanto espera?\x7Eles est\xc3\xa3o assustando os meus clientes.' },
    5269: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Ainda estou ajeitando o dente. Vai demorar um pouco.',
        QUEST: '\xc3\x89, este dente parece estar ruim mesmo, mas tudo bem.\x7Eu acho que posso fazer uma coisa aqui, mas ainda vai demorar um pouco.\x7Voc\xc3\xaa n\xc3\xa3o quer dar cabo de alguns daqueles Cogs Rob\xc3\xb4s-chefe das ruas enquanto espera?\x7Eles est\xc3\xa3o assustando os meus clientes.' },
    5230: {
        GREETING: '',
        QUEST: 'Ainda bem que voc\xc3\xaa voltou!\x7Desisti de consertar aquele dente velho e, em vez de consert\xc3\xa1-lo, fiz um novo dente de ouro para o Felipe.\x7S\xc3\xb3 que um Bar\xc3\xa3o Ladr\xc3\xa3o entrou aqui e o levou, infelizmente.\x7Ser\xc3\xa1 que voc\xc3\xaa n\xc3\xa3o consegue peg\xc3\xa1-lo? Vamos, apresse-se!',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Voc\xc3\xaa j\xc3\xa1 achou aquele dente?' },
    5270: {
        GREETING: '',
        QUEST: 'Ainda bem que voc\xc3\xaa voltou!\x7Desisti de consertar aquele dente velho e, em vez de consert\xc3\xa1-lo, fiz um novo dente de ouro para o Felipe.\x7S\xc3\xb3 que um Rei da Cocada Preta entrou aqui e o levou, infelizmente.\x7Ser\xc3\xa1 que voc\xc3\xaa n\xc3\xa3o consegue peg\xc3\xa1-lo? Vamos, apresse-se!',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Voc\xc3\xaa j\xc3\xa1 achou aquele dente?' },
    5271: {
        GREETING: '',
        QUEST: 'Ainda bem que voc\xc3\xaa voltou!\x7Desisti de consertar aquele dente velho e, em vez de consert\xc3\xa1-lo, fiz um novo dente de ouro para o Felipe.\x7S\xc3\xb3 que o Dr. Celebridade entrou aqui e o levou, infelizmente.\x7Ser\xc3\xa1 que voc\xc3\xaa n\xc3\xa3o consegue peg\xc3\xa1-lo? Vamos, apresse-se!',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Voc\xc3\xaa j\xc3\xa1 achou aquele dente?' },
    5272: {
        GREETING: '',
        QUEST: 'Ainda bem que voc\xc3\xaa voltou!\x7Desisti de consertar aquele dente velho e, em vez de consert\xc3\xa1-lo, fiz um novo dente de ouro para o Felipe.\x7S\xc3\xb3 que um Figur\xc3\xa3o entrou aqui e o levou, infelizmente.\x7Ser\xc3\xa1 que voc\xc3\xaa n\xc3\xa3o consegue peg\xc3\xa1-lo? Vamos, apresse-se!',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Voc\xc3\xaa j\xc3\xa1 achou aquele dente?' },
    5231: {
        QUEST: 'Legal, \xc3\xa9 este dente mesmo!\x7Por que voc\xc3\xaa n\xc3\xa3o corre para lev\xc3\xa1-lo para o Felipe?',
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Aposto como o Felipe vai adorar ver o dente novo dele.' },
    5232: {
        QUEST: 'Puxa, obrigado.\x7Mmmrrrfffffff\x7E a\xc3\xad, que tal, hein?\x7Ok, tudo bem, pode dizer ao Pio que eu o perd\xc3\xb4o.',
        LEAVING: '',
        GREETING: '' },
    5233: {
        QUEST: 'Legal, muito bom saber disso.\x7Achei mesmo que meu velho amigo Felipe n\xc3\xa3o podia ficar com raiva de mim.\x7Para agradecer e ser gentil, preparei para ele este p\xc3\xa3o de pinha.\x7Ser\xc3\xa1 que voc\xc3\xaa podia correr l\xc3\xa1 e entregar a ele para mim?',
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Melhor se apressar. O p\xc3\xa3o de pinha s\xc3\xb3 \xc3\xa9 bom quando est\xc3\xa1 quente.',
        COMPLETE: 'Puxa, o que \xc3\xa9 isto? Para mim?\x7Nham, nham...\x7Ohhhhhh! Meu dente! Aquele Pio Arrepio!\x7Tudo bem, n\xc3\xa3o foi sua culpa. Tome aqui, leve isto por todo o trabalho que demos a voc\xc3\xaa.' },
    903: {
        QUEST: 'Voc\xc3\xaa deve se aprontar para ver _toNpcName_, o Mago do Lago Congelado, para o seu teste final._where_' },
    5234: {
        GREETING: '',
        QUEST: 'Ah\xc3\xa1! Voc\xc3\xaa voltou.\x7Antes de voc\xc3\xaa come\xc3\xa7ar, precisamos comer.\x7Traga para a gente alguns peda\xc3\xa7os de coco para o nosso caldo.\x7O coco em peda\xc3\xa7os s\xc3\xb3 pode ser conseguido nos Cogs Rei da Cocada Preta.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Ainda precisamos de coco em peda\xc3\xa7os.' },
    5278: {
        GREETING: '',
        QUEST: 'Ah\xc3\xa1! Voc\xc3\xaa voltou.\x7Antes de voc\xc3\xaa come\xc3\xa7ar, precisamos comer.\x7Traga para a gente caviar para o nosso caldo.\x7O caviar s\xc3\xb3 pode ser conseguido nos Cogs Dr. Celebridade.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Ainda precisamos de caviar.' },
    5235: {
        GREETING: '',
        QUEST: 'Homens simples comem com colheres simples.\x7Os Cogs levaram minha colher simples, por isso, eu simplesmente n\xc3\xa3o posso comer.\x7Pegue minha colher de volta. Acho que foi um Bar\xc3\xa3o Ladr\xc3\xa3o.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Eu simplesmente preciso da minha colher.' },
    5279: {
        GREETING: '',
        QUEST: 'Homens simples comem com colheres simples.\x7Os Cogs levaram minha colher simples, por isso, eu n\xc3\xa3o posso comer.\x7Pegue minha colher de volta. Acho que foi um Figur\xc3\xa3o.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Eu simplesmente preciso da minha colher.' },
    5236: {
        GREETING: '',
        QUEST: 'Muito obrigado.\x7Slurp, slurp...\x7Ahhh, agora, voc\xc3\xaa precisa pegar um sapo falante. Tente pesc\xc3\xa1-lo no lago.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Cad\xc3\xaa o sapo falante?' },
    5237: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Voc\xc3\xaa n\xc3\xa3o conseguiu a sobremesa ainda.',
        QUEST: 'Ah, isto \xc3\xa9, com certeza, um sapo falante. Passe para c\xc3\xa1.\x7O que voc\xc3\xaa me diz, sapo?\x7Uh huh.\x7Uh huh...\x7O sapo falou. Precisamos da sobremesa.\x7Traga para a gente algumas casquinhas de sorvete da _toNpcName_.\x7Por alguma raz\xc3\xa3o, o sapo gosta de sorvete sabor feij\xc3\xa3o vermelho._where_' },
    5238: {
        GREETING: '',
        QUEST: 'Ent\xc3\xa3o, o mago mandou voc\xc3\xaa aqui. Sinto dizer que acabamos de ficar sem as casquinhas sabor feij\xc3\xa3o vermelho.\x7Voc\xc3\xaa nem imagina, mas um bando de Cogs entrou aqui e as levou.\x7Eles disseram que iam lev\xc3\xa1-las para o Dr. Celebridade, ou alguma baboseira parecida.\x7Certamente, apreciaria se voc\xc3\xaa pudesse recuper\xc3\xa1-las para mim.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'J\xc3\xa1 achou todas as minhas casquinhas de sorvete?' },
    5280: {
        GREETING: '',
        QUEST: 'Ent\xc3\xa3o, o mago mandou voc\xc3\xaa aqui. Sinto dizer que acabamos de ficar sem as casquinhas sabor feij\xc3\xa3o vermelho.\x7Voc\xc3\xaa nem imagina, mas um bando de Cogs entrou aqui e as levou.\x7Eles disseram que iam lev\xc3\xa1-las para O Rei da Cocada Preta, ou alguma baboseira parecida.\x7Certamente, apreciaria se voc\xc3\xaa pudesse recuper\xc3\xa1-las para mim.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'J\xc3\xa1 achou todas as minhas casquinhas de sorvete?' },
    5239: {
        QUEST: 'Obrigado por trazer de volta as minhas casquinhas de sorvete!\x7Tome uma para o Pequeno Grande Anci\xc3\xa3o.',
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: '\xc3\x89 melhor voc\xc3\xaa levar este sorvete para o Pequeno Grande Anci\xc3\xa3o antes que ele derreta.' },
    5240: {
        GREETING: '',
        QUEST: 'Muito bem. Aqui est\xc3\xa1, sapo...\x7Slurp, slurp...\x7Ok, agora estamos quase prontos.\x7Se voc\xc3\xaa pudesse apenas trazer um pozinho para secar as minhas m\xc3\xa3os...\x7Acho que das perucas daqueles Cogs Figur\xc3\xb5es \xc3\xa0s vezes sai p\xc3\xb3.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Achou algum p\xc3\xb3?' },
    5281: {
        GREETING: '',
        QUEST: 'Muito bem. Aqui est\xc3\xa1, sapo...\x7Slurp, slurp...\x7Ok, agora estamos quase prontos.\x7Se voc\xc3\xaa pudesse apenas trazer um pozinho para secar as minhas m\xc3\xa3os...\x7Acho que aqueles Cogs Drs. Celebridades \xc3\xa0s vezes t\xc3\xaam p\xc3\xb3 para o nariz.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Achou algum p\xc3\xb3?' },
    5241: {
        QUEST: 'Ok.\x7Como j\xc3\xa1 disse antes, para lan\xc3\xa7ar uma torta pra valer, n\xc3\xa3o basta jog\xc3\xa1-la com a m\xc3\xa3o...\x7...\xc3\x89 preciso jogar com a alma.\x7N\xc3\xa3o sei exatamente o que isto significa, portanto, sentarei e contemplarei voc\xc3\xaa em seu trabalho de recuperar edif\xc3\xadcios.\x7Volte quando tiver conclu\xc3\xaddo a sua tarefa.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Sua tarefa ainda n\xc3\xa3o est\xc3\xa1 conclu\xc3\xadda.' },
    5242: {
        GREETING: '',
        QUEST: 'Embora eu ainda n\xc3\xa3o saiba sobre o que estou falando, voc\xc3\xaa realmente merece.\x7Dou a voc\xc3\xaa, ent\xc3\xa3o, uma tarefa final...\x7O sapo falante precisa de uma namorada.\x7Ache uma sapa falante. O sapo falou.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Cad\xc3\xaa a sapa falante?',
        COMPLETE: 'Puxa! Estou cansado com todo esse esfor\xc3\xa7o. Preciso descansar agora.\x7Agora, pegue a sua recompensa e saia.' },
    5243: {
        QUEST: 'Soares Suado est\xc3\xa1 come\xc3\xa7ando a feder no in\xc3\xadcio da rua.\x7Fala com ele para tomar um banho ou algo do g\xc3\xaanero?_where_' },
    5244: {
        GREETING: '',
        QUEST: '\xc3\x89, acho que suei demais aqui.\x7Mmmm, se eu pudesse consertar aquele vazamento no encanamento do meu chuveiro...\x7Acho que a engrenagem de um daqueles Cogs pequenos bastaria para o conserto.\x7V\xc3\xa1 achar uma engrenagem de um Microempres\xc3\xa1rio para a gente tentar consertar.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Onde est\xc3\xa1 aquela engrenagem que voc\xc3\xaa ia conseguir?' },
    5245: {
        GREETING: '',
        QUEST: '\xc3\x89, parece que funcionou.\x7Mas eu fico solit\xc3\xa1rio quando tomo banho...\x7Ser\xc3\xa1 que voc\xc3\xaa poderia pescar um patinho de borracha para me fazer companhia?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'N\xc3\xa3o acha o patinho de borracha?' },
    5246: {
        QUEST: 'O patinho \xc3\xa9 \xc3\xb3timo, mas...\x7Todos aqueles edif\xc3\xadcios aqui em volta me deixam com os nervos em frangalhos.\x7Eu me sentiria bem melhor se houvesse menos edif\xc3\xadcios por aqui.',
        LEAVING: '',
        COMPLETE: 'Ok, agora eu vou tomar banho. Ah, aqui est\xc3\xa1 uma coisinha para voc\xc3\xaa.',
        INCOMPLETE_PROGRESS: 'Ainda estou preocupado com os edif\xc3\xadcios.' },
    5251: {
        QUEST: 'V\xc3\xadtor Vest\xc3\xadbulo devia estar fazendo um show nesta noite.\x7Ouvi falar que ele estava tendo problemas com o equipamento._where_' },
    5252: {
        GREETING: '',
        QUEST: '\xc3\x89 isso a\xc3\xad! Seria bom mesmo aceitar a sua ajuda.\x7Aqueles Cogs entraram aqui e levaram todas as engrenagens do meu equipamento enquanto eu estava descarregando a caminhonete.\x7Voc\xc3\xaa pode me dar uma m\xc3\xa3ozinha e conseguir de volta o meu microfone?',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Cara, eu n\xc3\xa3o consigo cantar sem o microfone.' },
    5253: {
        GREETING: '',
        QUEST: 'Legal, voc\xc3\xaa conseguiu meu microfone de volta.\x7Valeu, mas...\x7Eu preciso mesmo do meu teclado para poder fazer um som.\x7Acho que um daqueles Aventureiros Corporativos o levaram.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'N\xc3\xa3o conseguiu pegar o meu teclado?' },
    5273: {
        GREETING: '',
        QUEST: 'Legal, voc\xc3\xaa conseguiu meu microfone de volta.\x7Valeu, mas...\x7Eu preciso mesmo do meu teclado para poder fazer um som.\x7Acho que um daqueles Amizades F\xc3\xa1ceis o levaram.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'N\xc3\xa3o conseguiu pegar o meu teclado?' },
    5274: {
        GREETING: '',
        QUEST: 'Legal, voc\xc3\xaa conseguiu meu microfone de volta.\x7Valeu, mas...\x7Eu preciso mesmo do meu teclado para poder fazer um som.\x7Acho que um daqueles Agiotas o levaram.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'N\xc3\xa3o conseguiu pegar o meu teclado?' },
    5275: {
        GREETING: '',
        QUEST: 'Legal, voc\xc3\xaa conseguiu meu microfone de volta.\x7Valeu, mas...\x7Eu preciso mesmo do meu teclado para poder fazer um som.\x7Acho que um daqueles Macacos velhos o levaram.',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'N\xc3\xa3o conseguiu pegar o meu teclado?' },
    5254: {
        GREETING: '',
        QUEST: 'Tudo em cima! Agora estou na parada.\x7Se ao menos eles n\xc3\xa3o tivessem levado meus sapatos de plataforma...\x7Aqueles sapatos provavelmente acabaram com algum Dr. Celebridade, creio eu.',
        LEAVING: '',
        COMPLETE: 'Tudo bem!! Estou pronto agora.\x7Ol\xc3\xa1 Brrrgh!!!\x7H\xc3\xa3? Onde est\xc3\xa1 todo mundo?\x7Ok, pegue isto e re\xc3\xbana alguns f\xc3\xa3s, est\xc3\xa1 bem?',
        INCOMPLETE_PROGRESS: 'N\xc3\xa3o posso me apresentar sem sapatos, n\xc3\xa9?' },
    5282: {
        GREETING: '',
        QUEST: 'Tudo em cima! Agora, estou na parada.\x7Se ao menos eles n\xc3\xa3o tivessem levado meus sapatos de plataforma...\x7Aqueles sapatos provavelmente acabaram com algum Rei da Cocada Preta, creio eu.',
        LEAVING: '',
        COMPLETE: 'Tudo bem!! Estou pronto agora.\x7Ol\xc3\xa1 Brrrgh!!!\x7H\xc3\xa3? Onde est\xc3\xa1 todo mundo?\x7Ok, pegue isto e re\xc3\xbana alguns f\xc3\xa3s, est\xc3\xa1 bem?',
        INCOMPLETE_PROGRESS: 'N\xc3\xa3o posso me apresentar sem sapatos, n\xc3\xa9?' },
    5283: {
        GREETING: '',
        QUEST: 'Tudo em cima! Agora estou na parada.\x7Se ao menos eles n\xc3\xa3o tivessem levado meus sapatos de plataforma...\x7Aqueles sapatos provavelmente acabaram com algum Bar\xc3\xa3o Ladr\xc3\xa3o, creio eu.',
        LEAVING: '',
        COMPLETE: 'Tudo bem!! Estou pronto agora.\x7Ol\xc3\xa1 Brrrgh!!!\x7H\xc3\xa3? Onde est\xc3\xa1 todo mundo?\x7Ok, pegue isto e re\xc3\xbana alguns f\xc3\xa3s, est\xc3\xa1 bem?',
        INCOMPLETE_PROGRESS: 'N\xc3\xa3o posso me apresentar sem sapatos, n\xc3\xa9?' },
    5284: {
        GREETING: '',
        QUEST: 'Tudo em cima! Agora, estou na parada.\x7Se ao menos eles n\xc3\xa3o tivessem levado meus sapatos de plataforma...\x7Aqueles sapatos provavelmente acabaram com algum Figur\xc3\xa3o, creio eu.',
        LEAVING: '',
        COMPLETE: 'Tudo bem!! Estou pronto agora.\x7Ol\xc3\xa1 Brrrgh!!!\x7H\xc3\xa3? Onde est\xc3\xa1 todo mundo?\x7Ok, pegue isto e re\xc3\xbana alguns f\xc3\xa3s, est\xc3\xa1 bem?',
        INCOMPLETE_PROGRESS: 'N\xc3\xa3o posso me apresentar sem sapatos, n\xc3\xa9?' },
    5255: {
        QUEST: 'Parece que voc\xc3\xaa pode usar mais pontos de risadas.\x7Talvez _toNpcName_ entre em um acordo com voc\xc3\xaa.\x7N\xc3\xa3o deixe de firmar o acordo por escrito..._where_' },
    5256: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Trato \xc3\xa9 trato.',
        QUEST: 'Ent\xc3\xa3o, voc\xc3\xaa est\xc3\xa1 atr\xc3\xa1s de pontos de risadas, n\xc3\xa9?\x7Se eu tenho uma proposta para voc\xc3\xaa!?\x7\xc3\x89 s\xc3\xb3 tomar conta de alguns Cogs Rob\xc3\xb4s-chefe para mim...\x7A\xc3\xad eu dou uma inje\xc3\xa7\xc3\xa3o de \xc3\xa2nimo nos seus pontos.' },
    5276: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Trato \xc3\xa9 trato.',
        QUEST: 'Ent\xc3\xa3o, voc\xc3\xaa est\xc3\xa1 atr\xc3\xa1s de pontos de risadas, n\xc3\xa9?\x7Se eu tenho uma proposta para voc\xc3\xaa!?\x7\xc3\x89 s\xc3\xb3 tomar conta de alguns Cogs Rob\xc3\xb4s da Lei para mim...\x7A\xc3\xad eu dou uma inje\xc3\xa7\xc3\xa3o de \xc3\xa2nimo nos seus pontos.' },
    5257: {
        GREETING: '',
        LEAVING: '',
        COMPLETE: 'Ok, mas tenho certeza de que falei para voc\xc3\xaa reunir alguns Cogs Rob\xc3\xb4s da Lei.\x7Bom, se voc\xc3\xaa est\xc3\xa1 falando, tudo bem, mas, ent\xc3\xa3o, fica me devendo uma.',
        INCOMPLETE_PROGRESS: 'Acho que voc\xc3\xaa n\xc3\xa3o terminou ainda.',
        QUEST: 'Voc\xc3\xaa est\xc3\xa1 dizendo que acabou? Derrotou todos os Cogs?\x7Voc\xc3\xaa deve ter entendido errado, nosso trato era para os Cogs Rob\xc3\xb4s Vendedores.\x7Tenho certeza de que disse para voc\xc3\xaa derrotar alguns Cogs Rob\xc3\xb4s Vendedores para mim.' },
    5277: {
        GREETING: '',
        LEAVING: '',
        COMPLETE: 'Ok, mas tenho certeza de que falei para voc\xc3\xaa reunir alguns Cogs Rob\xc3\xb4s da Lei.\x7Bom, se voc\xc3\xaa est\xc3\xa1 falando, tudo bem, mas, ent\xc3\xa3o, fica me devendo uma.',
        INCOMPLETE_PROGRESS: 'Acho que voc\xc3\xaa n\xc3\xa3o terminou ainda.',
        QUEST: 'Voc\xc3\xaa est\xc3\xa1 dizendo que acabou? Derrotou todos os Cogs?\x7Voc\xc3\xaa deve ter entendido errado, nosso trato era para os Cogs Rob\xc3\xb4s Mercen\xc3\xa1rios.\x7Tenho certeza de que disse para voc\xc3\xaa derrotar alguns Cogs Rob\xc3\xb4s Mercen\xc3\xa1rios para mim.' },
    5301: {
        QUEST: 'Eu n\xc3\xa3o posso ajudar com os pontos de Risada, mas talvez _toNpcName_ fa\xc3\xa7a neg\xc3\xb3cio com voc\xc3\xaa.\x7Mas ele \xc3\xa9 um pouco temperamental..._where_' },
    5302: {
        GREETING: '',
        LEAVING: '',
        COMPLETE: 'Eu te disse o qu\xc3\xaa?\x7Valeu mesmo! Aqui est\xc3\xa1 o seu ponto de Risada!',
        INCOMPLETE_PROGRESS: 'Oi!\x7O que est\xc3\xa1 fazendo aqui de novo!',
        QUEST: 'Um ponto de Risada? Acho que n\xc3\xa3o!\x7Claro, mas s\xc3\xb3 se der um jeito em alguns desses Rob\xc3\xb4s da Lei antes.' },
    5303: {
        QUEST: lTheBrrrgh + ' est\xc3\xa1 repleto de Cogs perigosos.\x7Se fosse voc\xc3\xaa, carregaria mais piadas por aqui.\x7Ouvi dizer que  _toNpcName_ pode fazer uma bolsa maior para voc\xc3\xaa se estiver a fim de trabalhar._where_' },
    5304: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Deve haver bastante Rob\xc3\xb4s da Lei l\xc3\xa1 fora.\x7Ent\xc3\xa3o mexa-se!',
        QUEST: 'Uma bolsa maior?\x7Eu at\xc3\xa9 poderia arranjar uma proc\xc3\xaa.\x7Mas vou precisar de fios.\x7Uns Rob\xc3\xb4s da Lei roubaram os meus fios ontem de manh\xc3\xa3.' },
    5305: {
        GREETING: 'Ol\xc3\xa1!',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Vai atacar mais uns cogs.\x7Essa cor ainda n\xc3\xa3o pegou.',
        QUEST: 'Esse \xc3\xa9 um fio bom!\x7Mas n\xc3\xa3o seria a minha primeira escolha de cor.\x7Vou te dizer...\x7Vai l\xc3\xa1 fora e derrote alguns dos cogs mais dif\xc3\xadceis...\x7E eu come\xc3\xa7o a a trabalhar em tingir este fio.' },
    5306: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Eles t\xc3\xaam que estar l\xc3\xa1 em algum lugar...',
        QUEST: 'Bem, este fio est\xc3\xa1 todo tingido. Mas tem um probleminha.\x7N\xc3\xa3o consigo encontrar as minhas agulhas de tric\xc3\xb4.\x7O \xc3\xbaltimo lugar que estavam foi no lago.' },
    5307: {
        GREETING: '',
        LEAVING: 'Muito obrigado!',
        INCOMPLETE_PROGRESS: 'Roma n\xc3\xa3o foi tricotada em um dia!',
        QUEST: 'Essas s\xc3\xa3o as minhas agulhas.\x7Enquanto eu tricoto, que tal fazer uma limpeza em alguns dos pr\xc3\xa9dios grandes?',
        COMPLETE: '\xc3\x93timo trabalho!\x7E falando em trabalho \xc3\xb3timo...\x7Aqui est\xc3\xa1 a sua nova bolsa!' },
    5308: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Ouvi dizer que _toNpcName_ tem problemas legais.\x7Voc\xc3\xaa pode passar l\xc3\xa1 e dar uma olhada?_where_' },
    5309: {
        GREETING: 'Que bom ver voc\xc3\xaa...',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'R\xc3\xa1pido, por favor! A rua est\xc3\xa1 transbordando com eles!',
        QUEST: 'Os Rob\xc3\xb4s da Lei tomaram conta daqui.\x7Temo que eles v\xc3\xa3o me levar a julgamento.\x7Voc\xc3\xaa poderia me ajudar a tir\xc3\xa1-los desta rua?' },
    5310: {
        GREETING: '',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'Acho que os ou\xc3\xa7o vindo por mim...',
        QUEST: 'Obrigado. Sinto-me um pouco melhor agora.\x7 Mas tem mais uma coisa...\x7Voc\xc3\xaa poderia ir at\xc3\xa9 a casa de  _toNpcName_ e me conseguir um \xc3\xa1libi?_where_' },
    5311: {
        GREETING: 'O QUEEE!!!!',
        LEAVING: '',
        INCOMPLETE_PROGRESS: 'N\xc3\xa3o posso ajud\xc3\xa1-lo se n\xc3\xa3o encontrar!',
        QUEST: '\xc3\x81libi?! Mas que \xc3\xb3tima ideia!\x7E traga duas!\x7Aposto que um Macaco velho deve ter alguns...' },
    5312: {
        GREETING: 'Finalmente!',
        LEAVING: '',
        INCOMPLETE_PROGRESS: '',
        COMPLETE: 'Ufa! Que al\xc3\xadvio \xc3\xa9 ter isso.\x7Aqui est\xc3\xa1 a sua recompensa...',
        QUEST: 'S\xc3\xbaper! \xc3\x89 melhor voc\xc3\xaa voltar at\xc3\xa9 _toNpcName_!' },
    6201: {
        QUEST: 'Elle \xc3\x89trica precisa de ajuda. Voc\xc3\xaa pode passar l\xc3\xa1 e dar uma m\xc3\xa3ozinha a ela?_where_' },
    6202: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Um cliente! Beleza! Em que posso ajudar?\x7Como assim, voc\xc3\xaa me ajudar? AH! Voc\xc3\xaa n\xc3\xa3o \xc3\xa9 um cliente.\x7Agora me lembrei. Voc\xc3\xaa veio para me ajudar com aqueles Cogs horrorosos.\x7Na verdade, eu aceitaria sua ajuda, voc\xc3\xaa sendo um cliente ou n\xc3\xa3o.\x7Se voc\xc3\xaa fizer uma pequena limpa nas ruas, dou uma coisa a voc\xc3\xaa.',
        INCOMPLETE_PROGRESS: 'Se voc\xc3\xaa n\xc3\xa3o quiser eletricidade, n\xc3\xa3o posso ajudar at\xc3\xa9 que derrote aqueles Cogs.',
        COMPLETE: 'Bom trabalho com aqueles Cogs, _avName_.\x7Agora, voc\xc3\xaa tem certeza de que n\xc3\xa3o quer um choquezinho? Pode ser \xc3\xbatil....\x7N\xc3\xa3o? OK, voc\xc3\xaa que sabe.\x7H\xc3\xa3? Ah sim, lembro. Aqui est\xc3\xa1. Com certeza, vai ajudar voc\xc3\xaa a deter aqueles Cogs nojentos.\x7Continue assim!' },
    6206: {
        QUEST: 'Bem, _avName_, n\xc3\xa3o tenho nada para voc\xc3\xaa agora.\x7Espera a\xc3\xad! Acho que a C\xc3\xa9lia Sesta estava procurando ajuda. Por que n\xc3\xa3o vai encontr\xc3\xa1-la?_where_' },
    6207: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Nunca enriquecerei com aqueles malditos Cogs atrapalhando os meus neg\xc3\xb3cios!\x7Voc\xc3\xaa tem que me ajudar, _avName_.\x7Elimine alguns edif\xc3\xadcios de Cogs para salvar a vizinhan\xc3\xa7a e ajudarei voc\xc3\xaa em sua poupan\xc3\xa7a.',
        INCOMPLETE_PROGRESS: 'O que farei agora? Voc\xc3\xaa n\xc3\xa3o conseguiu se livrar dos edif\xc3\xadcios?',
        COMPLETE: 'Agora, vou entrar na grana! Agora sim!\x7Vou passar todo o meu tempo livre pescando. Agora, deixe-me enriquecer sua vida um pouquinho.\x7L\xc3\xa1 vai!' },
    6211: {
        QUEST: 'Oi, _avName_! Ouvi dizer que a Linda Legal estava procurando voc\xc3\xaa.\x7Passa l\xc3\xa1 para fazer uma visitinha a ela._where_' },
    6212: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'E a\xc3\xad! Nossa, como \xc3\xa9 bom ver voc\xc3\xaa!\x7Fiquei trabalhando nesta secret\xc3\xa1ria eletr\xc3\xb4nica nas horas vagas, mas faltam algumas pe\xc3\xa7as.\x7Preciso de mais tr\xc3\xaas varas, e as do Conta-moedinha parecem perfeitas.\x7Voc\xc3\xaa poderia tentar encontrar algumas varas de pescar para mim?',
        INCOMPLETE_PROGRESS: 'Ainda \xc3\xa0 procura daquelas varas de pescar?' },
    6213: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Ah, estas aqui j\xc3\xa1 ajudam.\x7Engra\xc3\xa7ado. Eu tinha certeza de que havia um cinto de seguran\xc3\xa7a extra por aqui, mas n\xc3\xa3o consigo encontr\xc3\xa1-lo.\x7Voc\xc3\xaa pode pegar um de uns Sacos de Dinheiro para mim? Valeu!',
        INCOMPLETE: 'Olha, eu s\xc3\xb3 posso ajudar voc\xc3\xaa depois que conseguir aquele cinto de seguran\xc3\xa7a.' },
    6214: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Agora sim. Vai funcionar que \xc3\xa9 uma beleza.\x7Onde est\xc3\xa1 meu alicate? N\xc3\xa3o vou poder ajustar isto aqui sem o alicate.\x7Talvez as pin\xc3\xa7as da M\xc3\xa3o de vaca ajudem.\x7Se voc\xc3\xaa conseguir encontr\xc3\xa1-las, dou a voc\xc3\xaa uma coisa que vai ajudar na batalha com os Cogs.',
        INCOMPLETE_PROGRESS: 'Nada das pin\xc3\xa7as ainda, n\xc3\xa9? Vai procurando.',
        COMPLETE: 'Beleza! Agora \xc3\xa9 s\xc3\xb3 fazer o ajuste aqui.\x7Parece que agora est\xc3\xa1 funcionando. Estou de novo na ativa!\x7Na verdade, falta ainda o telefone. Mas, estou satisfeito com a sua ajuda.\x7Acho que isso vai ajudar voc\xc3\xaa com os Cogs. Boa sorte!' },
    6221: {
        QUEST: 'Ouvi dizer que Pedro estava atr\xc3\xa1s da sua ajuda. Veja o que pode fazer por ele._where_' },
    6222: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Qual\xc3\xa9? Chegou no point certo. N\xc3\xa3o estou legal.\x7\xc3\x89 isso a\xc3\xad, tava procurando ajuda pra me livrar daqueles Cogs. Eles chegam e ficam mandando em mim.\x7Bem que voc\xc3\xaa podia mandar aqueles Rob\xc3\xb4s-chefe se aposentarem. Voc\xc3\xaa n\xc3\xa3o vai se arrepender.',
        INCOMPLETE_PROGRESS: 'E a\xc3\xad, _avName_, qual foi?\x7Vai l\xc3\xa1 atr\xc3\xa1s dos Rob\xc3\xb4s-chefe. A gente tem um trato, falou?\x7O Pedro aqui tem palavra.',
        COMPLETE: 'Qual\xc3\xa9, _avName_! Agora, voc\xc3\xaa est\xc3\xa1 bem na fita.\x7Quero ver os Rob\xc3\xb4s-chefe chefiar agora, n\xc3\xa9 n\xc3\xa3o?\x7Vamo l\xc3\xa1! Um tremendo acr\xc3\xa9scimo pra voc\xc3\xaa. Agora, v\xc3\xaa se n\xc3\xa3o entra em nenhuma fria, falou?' },
    6231: {
        QUEST: 'O Zez\xc3\xa9 ouviu um boato na Alameda do Pijama sobre um Quartel do Rob\xc3\xb4 Mercen\xc3\xa1rio.\x7Vai l\xc3\xa1 e veja se consegue ajud\xc3\xa1-lo._where_' },
    6232: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Soube de umas coisas estranhas que est\xc3\xa3o acontecendo.\x7Talvez sejam as pulgas, mas deve ter alguma coisa rolando.\x7Todos esses Rob\xc3\xb4s Mercen\xc3\xa1rios!\x7Acho que abriram outro quartel bem na Alameda do Pijama.\x7O Py Jama sabe o caminho.\x7V\xc3\xa1 ver _toNpcName_ _where_ Pergunte a ele se viu alguma coisa.',
        INCOMPLETE_PROGRESS: 'Ainda n\xc3\xa3o viu o Py Jama? O que voc\xc3\xaa est\xc3\xa1 esperando?\x7Ai, essas malditas pulgas!' },
    6233: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'E a\xc3\xad, _avName_, para onde voc\xc3\xaa est\xc3\xa1 indo?\x7Para o Quartel dos Rob\xc3\xb4s Mercen\xc3\xa1rios?? Eu n\xc3\xa3o vi nada.\x7Voc\xc3\xaa pode ir at\xc3\xa9 o final da Alameda do Pijama e ver se \xc3\xa9 verdade?\x7Encontre alguns Cogs do Rob\xc3\xb4 Mercen\xc3\xa1rio no quartel, derrote alguns deles e venha me contar.',
        INCOMPLETE_PROGRESS: 'J\xc3\xa1 encontrou o Quartel? Voc\xc3\xaa precisar\xc3\xa1 derrotar alguns Rob\xc3\xb4s Mercen\xc3\xa1rios para localiz\xc3\xa1-lo.' },
    6234: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'O qu\xc3\xaa?! Existe mesmo um Quartel de Rob\xc3\xb4s Mercen\xc3\xa1rios?\x7\xc3\x89 melhor voc\xc3\xaa ir e contar a Zez\xc3\xa9 agora mesmo!\x7Quem poderia imaginar que existiria um Quartel de Cogs na rua bem em frente a ele?',
        INCOMPLETE_PROGRESS: 'O que Zez\xc3\xa9 disse? Voc\xc3\xaa ainda n\xc3\xa3o o encontrou?' },
    6235: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Estou tentado para ouvir o que o Py Jamas disse.\x7Hmm... Precisamos de mais informa\xc3\xa7\xc3\xb5es sobre esse neg\xc3\xb3cio de Cog, mas preciso me livrar dessas pulgas!\x7Eu sei! VOC\xc3\x8a pode descobrir mais coisas!\x7V\xc3\xa1 derrotar os Rob\xc3\xb4s Mercen\xc3\xa1rios no Quartel at\xc3\xa9 encontrar alguns planos, depois venha direto pra c\xc3\xa1!',
        INCOMPLETE_PROGRESS: 'Nada ainda? Continue procurando esses Cogs!\x7Eles devem ter algum plano!',
        COMPLETE: 'Voc\xc3\xaa conseguiu os planos?\x7Excelente! Vejamos o que diz aqui.\x7Entendi... os Rob\xc3\xb4s Mercen\xc3\xa1rios constru\xc3\xadram uma Casa da Moeda para fabricar grana Cog.\x7Deve estar CHEIA de Rob\xc3\xb4s Mercen\xc3\xa1rios. Precisamos averiguar.\x7E se voc\xc3\xaa se disfar\xc3\xa7asse? Hmmm...J\xc3\xa1 sei! Acho que tenho uma pe\xc3\xa7a de vestimenta de Cog aqui em algum lugar....\x7Aqui est\xc3\xa1! Isto aqui \xc3\xa9 para compensar o trabalho. Agrade\xc3\xa7o novamente pela ajuda!' },
    6241: {
        QUEST: 'A Condessa est\xc3\xa1 procurando voc\xc3\xaa por toda parte! Visite-a logo para que pare de ligar _where_' },
    6242: {
        GREETING: '',
        LEAVING: '',
        QUEST: '_avName_, conto com a sua ajuda!\x7Sabe, esses Cogs est\xc3\xa3o fazendo tanto barulho que eu simplesmente n\xc3\xa3o consigo me concentrar.\x7Perco a conta dos carneirinhos a todo instante!\x7Se voc\xc3\xaa acabar com esse barulho, te dou uma ajuda! Pode contar com isso!\x7Mas, onde eu parei mesmo? Ah sim: cento e trinta e seis, cento e trinta e sete....',
        INCOMPLETE_PROGRESS: 'Quatrocentos e quarenta e dois... Quatrocentos e quarenta e tr\xc3\xaas...\x7O qu\xc3\xaa? Voc\xc3\xaa j\xc3\xa1 voltou? Mas ainda tem tanto barulho!\x7Essa n\xc3\xa3o, perdi a conta novamente.\x7 Um...dois...tr\xc3\xaas....',
        COMPLETE: 'Quinhentos e noventa e tr\xc3\xaas... Quinhentos e noventa e quatro...\x7Ol\xc3\xa1? Ah, eu sabia que poderia contar com a sua ajuda! Agora, o sil\xc3\xaancio voltou.\x7Pegue aqui, por todos esses Destruidores de N\xc3\xbameros.\x7Contar? Agora preciso come\xc3\xa7ar a contar tudo outra vez! Um...dois....' },
    6251: {
        QUEST: 'Pobre Z\xc3\xa9firo, o z\xc3\xadper dela quebrou e, agora, ela n\xc3\xa3o consegue fazer as entregas de seus clientes. Ela certamente precisa de sua ajuda._where_' },
    6252: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Oi _avName_. Voc\xc3\xaa est\xc3\xa1 aqui para ajudar com minhas entregas?\x7Isso \xc3\xa9 \xc3\xb3timo! Com esse z\xc3\xadper quebrado \xc3\xa9 muito dif\xc3\xadcil fazer as entregas sozinha.\x7Deixe-me ver... Ok, vai ser f\xc3\xa1cil. O Vaqueiro George pediu uma c\xc3\xadtara semana passada.\x7Voc\xc3\xaa poderia lev\xc3\xa1-la para ele? _where_',
        INCOMPLETE_PROGRESS: 'Oi! Esqueceu alguma coisa? O Vaqueiro George est\xc3\xa1 esperando pela c\xc3\xadtara.' },
    6253: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Minha c\xc3\xadtara! Finalmente! Caramba, mal posso esperar para toc\xc3\xa1-la.\x7Poderia agradecer \xc3\xa0 Z\xc3\xa9firo por mim?',
        INCOMPLETE_PROGRESS: 'Obrigado novamente pela c\xc3\xadtara. A Z\xc3\xa9firo n\xc3\xa3o tem mais entregas para voc\xc3\xaa fazer?' },
    6254: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Essa foi r\xc3\xa1pida. Qual ser\xc3\xa1 o pr\xc3\xb3ximo item da minha lista?\x7Ah sim! Mestre M\xc3\xa1rio pediu um Zamboni. Aquele zombeteiro.\x7Poderia levar para ele?_where_',
        INCOMPLETE_PROGRESS: 'Aquele Zamboni precisa ser levado para o Mestre M\xc3\xa1rio._where_' },
    6255: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Tudo certo! O Zamboni que eu pedi!\x7Agora, se n\xc3\xa3o houvesse tantos Cogs por a\xc3\xad, eu teria algum tempo para us\xc3\xa1-lo.\x7Seja gentil e cuide de alguns desses Rob\xc3\xb4s Mercen\xc3\xa1rios para mim, tudo bem?',
        INCOMPLETE_PROGRESS: 'Esses Rob\xc3\xb4s Mercen\xc3\xa1rios s\xc3\xa3o dur\xc3\xb5es, n\xc3\xa3o s\xc3\xa3o? Assim, eu n\xc3\xa3o consigo testar o meu Zamboni.' },
    6256: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Excelente! Agora, eu posso testar o meu Zamboni.\x7Diga \xc3\xa0 Z\xc3\xa9firo que eu estarei l\xc3\xa1 para fazer um outro pedido na pr\xc3\xb3xima semana.',
        INCOMPLETE_PROGRESS: 'Por enquanto \xc3\xa9 s\xc3\xb3 isso. A Z\xc3\xa9firo n\xc3\xa3o est\xc3\xa1 esperando por voc\xc3\xaa?' },
    6257: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Ent\xc3\xa3o, o Mestre M\xc3\xa1rio ficou satisfeito com o Zamboni? Excelente.\x7Quem \xc3\xa9 o pr\xc3\xb3ximo? Ah, o Bob Boc\xc3\xa3o pediu uma almofada zabuton com listras de zebra.\x7Aqui est\xc3\xa1! Poderia ir at\xc3\xa9 a casa dele?_where_',
        INCOMPLETE_PROGRESS: 'Acho que o Bob Boc\xc3\xa3o precisa da almofada zabuton para meditar.' },
    6258: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Ah, minha almofada zabuton finalmente. Agora, eu posso meditar.\x7Quem consegue se concentrar com aquela algazarra? Todos aqueles Cogs!\x7J\xc3\xa1 que voc\xc3\xaa est\xc3\xa1 aqui, poderia cuidar de alguns desses Cogs?\x7S\xc3\xb3 assim eu poderei usar minha almofada zabuton em paz.',
        INCOMPLETE_PROGRESS: 'Ainda h\xc3\xa1 muito barulho com esses Cogs! Quem consegue se concentrar?' },
    6259: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Paz e sil\xc3\xaancio afinal. Obrigado, _avName_.\x7Diga \xc3\xa0 Z\xc3\xa9firo que estou muito satisfeito. OM....',
        INCOMPLETE_PROGRESS: 'A Z\xc3\xa9firo ligou procurando por voc\xc3\xaa. \xc3\x89 melhor voc\xc3\xaa ir ver o que ela precisa.' },
    6260: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Estou feliz em saber que o Bob Boc\xc3\xa3o est\xc3\xa1 satisfeito com sua almofada zabuton de zebra.\x7Ah, estas z\xc3\xadnias acabaram de chegar para a Rosa Sonada.\x7J\xc3\xa1 que voc\xc3\xaa parece t\xc3\xa3o animado para fazer entregas, talvez possa levar essas z\xc3\xadnias para ela, n\xc3\xa3o \xc3\xa9?_where_',
        INCOMPLETE_PROGRESS: 'Essas z\xc3\xadnias v\xc3\xa3o murchar se voc\xc3\xaa n\xc3\xa3o fizer logo a entrega.' },
    6261: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Que lindas z\xc3\xadnias! Certamente que \xc3\xa9 entrega da Z\xc3\xa9firo.\x7Quer dizer, \xc3\xa9 SUA entrega, _avName_. Agrade\xc3\xa7a \xc3\xa0 Z\xc3\xa9firo por mim!',
        INCOMPLETE_PROGRESS: 'N\xc3\xa3o se esque\xc3\xa7a de agradecer \xc3\xa0 Z\xc3\xa9firo pelas z\xc3\xadnias!' },
    6262: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Que bom que voltou, _avName_. Voc\xc3\xaa \xc3\xa9 bastante veloz.\x7Vejamos... Qual \xc3\xa9 o pr\xc3\xb3ximo item da lista a ser entregue? Discos de forr\xc3\xb3 para Jatha Cordada._where_',
        INCOMPLETE_PROGRESS: 'Tenho certeza de que Jatha Cordada est\xc3\xa1 esperando por esses discos de forr\xc3\xb3.' },
    6263: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Discos de forr\xc3\xb3? N\xc3\xa3o me lembro de ter pedido discos de forr\xc3\xb3.\x7Ah, aposto que foi Denis Nar quem pediu._where_',
        INCOMPLETE_PROGRESS: 'N\xc3\xa3o, esses discos de forr\xc3\xb3 s\xc3\xa3o para Denis Nar._where_' },
    6264: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Finalmente, meus discos de forr\xc3\xb3! Pensei que a Z\xc3\xa9firo tivesse se esquecido.\x7Poderia levar essa abobrinha para ela? Ela encontrar\xc3\xa1 algu\xc3\xa9m que esteja querendo uma. Valeu!',
        INCOMPLETE_PROGRESS: 'Eu j\xc3\xa1 tenho muitas abobrinhas. Leve esta para Z\xc3\xa9firo.' },
    6265: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Abobrinha? Hmm. Bem, algu\xc3\xa9m ir\xc3\xa1 querer, tenho certeza.\x7Ok, estamos quase terminando com a minha lista. Mais uma entrega a fazer.\x7Nen\xc3\xaa Crespo pediu um palet\xc3\xb3 zoot._where_',
        INCOMPLETE_PROGRESS: 'Se voc\xc3\xaa n\xc3\xa3o entregar esse palet\xc3\xb3 zoot ao Nen\xc3\xaa Crespo,\x7 ele ficar\xc3\xa1 todo amarrotado.' },
    6266: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Era uma vez... Ah! Voc\xc3\xaa n\xc3\xa3o est\xc3\xa1 aqui para ouvir uma hist\xc3\xb3ria, n\xc3\xa3o \xc3\xa9?\x7\xc3\x89 a entrega do meu terno zoot? Beleza! Uau, isso aqui \xc3\xa9 demais.\x7Ei, poderia dar um recado meu para a Z\xc3\xa9firo? Precisarei de abotoaduras de zirc\xc3\xb4nio para usar com o palet\xc3\xb3. Valeu!',
        INCOMPLETE_PROGRESS: 'Voc\xc3\xaa deu o meu recado \xc3\xa0 Z\xc3\xa9firo?',
        COMPLETE: 'Abotoaduras de zirc\xc3\xb4nio, certo? Bem, verei o que posso fazer por ele.\x7Seja como for, voc\xc3\xaa tem sido muito \xc3\xbatil e n\xc3\xa3o posso deixar voc\xc3\xaa ir sem nada.\x7Aqui est\xc3\xa1 um GRANDE acr\xc3\xa9scimo para ajudar a derrotar esses Cogs!' },
    6271: {
        QUEST: 'Solano Sonolento est\xc3\xa1 tendo problemas e voc\xc3\xaa talvez possa ajud\xc3\xa1-lo. Por que voc\xc3\xaa n\xc3\xa3o d\xc3\xa1 uma passada na loja dele?_where_' },
    6272: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'O qu\xc3\xaa? H\xc3\xa3? Eu devo ter cochilado.\x7Sabe, esses edif\xc3\xadcios de Cogs est\xc3\xa3o cheios de m\xc3\xa1quinas que realmente me d\xc3\xa3o um sono.\x7Eu ou\xc3\xa7o esse zumbido o dia inteiro e...\x7H\xc3\xa3? Ah, sim, est\xc3\xa1 certo. Se voc\xc3\xaa pudesse se livrar de alguns desses edif\xc3\xadcios de Cogs, eu conseguiria ficar acordado.',
        INCOMPLETE_PROGRESS: 'Zzzzz...h\xc3\xa3? Ah, \xc3\xa9 voc\xc3\xaa, _avName_.\x7J\xc3\xa1 est\xc3\xa1 de volta? Eu s\xc3\xb3 estava tirando uma sonequinha.\x7Volte quando acabar com esses edif\xc3\xadcios.',
        COMPLETE: 'O qu\xc3\xaa? Eu ca\xc3\xad no sono um minutinho.\x7Agora que aqueles edif\xc3\xadcios de Cogs viraram p\xc3\xb3, finalmente posso relaxar.\x7Valeu pela ajuda, _avName_.\x7Vejo voc\xc3\xaa depois! Acho que vou tirar uma sonequinha.' },
    6281: {
        QUEST: 'V\xc3\xa1 em frente e ligue para o Ursinho de P. L\xc3\xbacia. Ele tem um trabalho para voc\xc3\xaa._where_' },
    6282: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'O que voc\xc3\xaa disse? N\xc3\xa3o, eu n\xc3\xa3o tenho um baralho pra voc\xc3\xaa.\x7Ah, \xc3\xa9 um trabalho! Por que voc\xc3\xaa n\xc3\xa3o disse logo? Voc\xc3\xaa precisa falar alto.\x7Esses Cogs n\xc3\xa3o me deixam hibernar. Se voc\xc3\xaa ajudar a tornar a Sonhol\xc3\xa2ndia mais silenciosa,\x7eu lhe darei uma coisinha.',
        INCOMPLETE_PROGRESS: 'Voc\xc3\xaa derrotou os bogs? Que bogs?\x7Ah, os Cogs! Por que voc\xc3\xaa n\xc3\xa3o disse logo?\x7Hmm, ainda tem barulho. O que acha de derrotar mais alguns?',
        COMPLETE: 'Voc\xc3\xaa se divertiu? H\xc3\xa3? Ah!\x7Voc\xc3\xaa conseguiu! Beleza. Muito legal voc\xc3\xaa ter me ajudado.\x7Eu achei isso nos fundos da loja, mas n\xc3\xa3o tem utilidade para mim.\x7Talvez voc\xc3\xaa descubra o que fazer com isso. At\xc3\xa9 logo, _avName_!' },
    6291: {
        QUEST: 'Os Cogs arrombaram o Banco A Fraldinha de Dormir! V\xc3\xa1 at\xc3\xa9 o Guilherme Sonoleve e veja se voc\xc3\xaa pode ajud\xc3\xa1-lo.' },
    6292: {
        QUEST: 'Aqueles malditos Cogs do Rob\xc3\xb4 Mercen\xc3\xa1rio! Eles roubaram meus abajures de leitura!\x7Eu preciso deles de volta agora mesmo. Voc\xc3\xaa pode procurar por eles?\x7Se voc\xc3\xaa encontrar meus abajures, talvez eu possa ajudar a encontrar o Diretor Financeiro.\x7Depressa!',
        INCOMPLETE_PROGRESS: 'Eu preciso dos abajures de volta. Continue procurando!',
        COMPLETE: 'Voc\xc3\xaa voltou! E trouxe meus abajures!\x7N\xc3\xa3o tenho como agradecer o favor, mas posso dar isto a voc\xc3\xaa.' },
    7201: {
        QUEST: 'Nana de Nina estava \xc3\xa0 sua procura, _avName_. Ela precisa de ajuda._where_' },
    7202: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Ah! Estou t\xc3\xa3o feliz em ver voc\xc3\xaa, _avName_. Espero que possa me ajudar!\x7Aqueles malditos Cogs assustaram o pessoal da entrega e n\xc3\xa3o tenho mais camas no estoque.\x7Poderia ir ao Pedro Fuso e trazer uma cama para mim?_where_',
        INCOMPLETE_PROGRESS: 'O Pedro tinha alguma cama? Tinha certeza de que ele teria uma.',
        COMPLETE: '' },
    7203: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Uma cama? Isso mesmo, aqui est\xc3\xa1 uma prontinha para viagem.\x7Entregue a cama pra Nana por mim, OK? Cama, Nana...\x7"Rimou!" H\xc3\xa1-h\xc3\xa1!\x7Muito engra\xc3\xa7ado. N\xc3\xa3o? Bem, mas leve para ela, por favor.',
        INCOMPLETE_PROGRESS: 'A Nana gostou da cama?',
        COMPLETE: '' },
    7204: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Essa cama n\xc3\xa3o est\xc3\xa1 legal. Ela \xc3\xa9 muito simples.\x7Voc\xc3\xaa poderia ir at\xc3\xa9 l\xc3\xa1 e ver se ele tem alguma coisa mais sofisticada?\x7Tenho certeza de que n\xc3\xa3o vai demorar nadinha.',
        INCOMPLETE_PROGRESS: 'Estou certa de que o Pedro tem uma cama mais sofisticada.',
        COMPLETE: '' },
    7205: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'N\xc3\xa3o acertei na mosca com essa cama, n\xc3\xa3o \xc3\xa9? Tenho uma aqui que servir\xc3\xa1.\x7S\xc3\xb3 tem um pequeno problema: \xc3\xa9 preciso mont\xc3\xa1-la primeiro.\x7Enquanto eu resolvo esse problema, voc\xc3\xaa pode se livrar de alguns Cogs que est\xc3\xa3o l\xc3\xa1 fora?\x7Aqueles terr\xc3\xadveis Cogs jogaram uma chave inglesa nos m\xc3\xb3veis.\x7Volte quando terminar e a cama estar\xc3\xa1 pronta.',
        INCOMPLETE_PROGRESS: 'Ainda n\xc3\xa3o terminei a montagem da cama.\x7Quando voc\xc3\xaa tiver acabado com os Cogs, ela estar\xc3\xa1 pronta.',
        COMPLETE: '' },
    7206: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'E a\xc3\xad _avName_!\x7Voc\xc3\xaa fez um excelente trabalho com aqueles Cogs.\x7A cama j\xc3\xa1 est\xc3\xa1 prontinha. Voc\xc3\xaa pode entreg\xc3\xa1-la para mim?\x7Agora que aqueles Cogs se foram, as coisas est\xc3\xa3o r\xc3\xa1pidas por aqui!',
        INCOMPLETE_PROGRESS: 'Acho que a Nana est\xc3\xa1 esperando pela entrega da cama.',
        COMPLETE: 'Que cama ador\xc3\xa1vel!\x7Agora, meus clientes ficar\xc3\xa3o satisfeitos. Obrigada, _avName_.\x7Olha s\xc3\xb3, talvez voc\xc3\xaa possa usar isto. Algu\xc3\xa9m deixou isso aqui.' },
    7209: {
        QUEST: 'V\xc3\xa1 at\xc3\xa9 a Lua de Mel. Ela precisa de ajuda._where_' },
    7210: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Ah! Estou t\xc3\xa3o feliz em ver voc\xc3\xaa, _avName_. Eu preciso muito de ajuda!\x7N\xc3\xa3o consigo tirar o meu sono reparador h\xc3\xa1 s\xc3\xa9culos. Veja voc\xc3\xaa, aqueles Cogs roubaram a minha colcha.\x7Voc\xc3\xaa pode correr e ver se o Marcelo tem alguma coisa em azul?_where_',
        INCOMPLETE_PROGRESS: 'O que o Marcelo falou sobre a colcha azul?',
        COMPLETE: '' },
    7211: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Ent\xc3\xa3o, a Mel quer uma colcha, n\xc3\xa9?\x7De que cor? AZUL?!\x7Bem, eu terei de fazer uma especialmente para ela. Tudo o que eu tenho aqui \xc3\xa9 em vermelho.\x7Escuta... Se voc\xc3\xaa for derrotar alguns Cogs l\xc3\xa1 fora, farei uma colcha azul especialmente para ela.\x7Colchas azuis... O que ser\xc3\xa1 da pr\xc3\xb3xima vez?',
        INCOMPLETE_PROGRESS: 'Ainda estou trabalhando na colcha azul, _avName_. Continue a derrotar esses Cogs!',
        COMPLETE: '' },
    7212: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Que bom ver voc\xc3\xaa novamente. Tenho algo pra voc\xc3\xaa!\x7Aqui est\xc3\xa1 a colcha, e \xc3\xa9 azul. Ela vai adorar.',
        INCOMPLETE_PROGRESS: 'A Mel gostou da colcha?',
        COMPLETE: '' },
    7213: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Minha colcha? N\xc3\xa3o, n\xc3\xa3o est\xc3\xa1 legal.\x7\xc3\x89 XADREZ! Como algu\xc3\xa9m pode dormir com uma estampa t\xc3\xa3o CHAMATIVA?\x7Voc\xc3\xaa ter\xc3\xa1 que lev\xc3\xa1-la de volta e trazer uma outra colcha.\x7Tenho certeza de que ele tem outras.',
        INCOMPLETE_PROGRESS: 'Eu simplesmente n\xc3\xa3o vou aceitar uma colcha xadrez. Veja o que Marcelo pode fazer.',
        COMPLETE: '' },
    7214: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'O qu\xc3\xaa? Ela n\xc3\xa3o gosta de XADREZ?\x7Hmm... Deixe-me ver o que eu tenho aqui.\x7Isso vai levar algum tempo. Por que voc\xc3\xaa n\xc3\xa3o cuida de alguns Cogs enquanto eu tento encontrar algo diferente?\x7Terei alguma coisa quando voc\xc3\xaa estiver de volta.',
        INCOMPLETE_PROGRESS: 'Ainda estou procurando uma colcha diferente. Como est\xc3\xa1 indo com os Cogs?',
        COMPLETE: '' },
    7215: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Ei, bom trabalho com os Cogs!\x7Aqui est\xc3\xa1, \xc3\xa9 azul e n\xc3\xa3o \xc3\xa9 xadrez.\x7Espero que ela goste de estampado.\x7Leve a colcha para a Mel.',
        INCOMPLETE_PROGRESS: 'Isso \xc3\xa9 tudo o que eu tenho para voc\xc3\xaa agora.\x7Por favor, leve esta colcha para a Mel.',
        COMPLETE: 'Ah! Que linda! Estampado combina muito bem comigo.\x7\xc3\x89 hora do meu sono reparador! At\xc3\xa9 logo, _avName_.\x7O qu\xc3\xaa? Voc\xc3\xaa ainda est\xc3\xa1 aqui? N\xc3\xa3o v\xc3\xaa que estou tentando dormir?\x7Tome isto aqui e me deixe descansar. Devo estar medonha!' },
    7218: {
        QUEST: 'Dafne Sonolinda precisa de ajuda._where_' },
    7219: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Ah, _avName_, estou t\xc3\xa3o feliz em ver voc\xc3\xaa! Aqueles Cogs levaram meus travesseiros.\x7Voc\xc3\xaa pode ver se o Lel\xc3\xaa tem alguns travesseiros?_where_\x7Tenho certeza de que ele pode ajudar.',
        INCOMPLETE_PROGRESS: 'O Lel\xc3\xaa tem algum travesseiro para mim?',
        COMPLETE: '' },
    7220: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Como vai? A Dafne precisa de alguns travesseiros, n\xc3\xa9? Bem, voc\xc3\xaa veio ao lugar certo, parceria!\x7H\xc3\xa1 mais travesseiros aqui do que espinhos em um cacto.\x7Aqui est\xc3\xa1, _avName_. Leve estes para Dafne, com os meus cumprimentos.\x7\xc3\x89 sempre um prazer ajudar uma mocinha.',
        INCOMPLETE_PROGRESS: 'Os travesseiros eram macios o suficiente para uma pequena dama?',
        COMPLETE: '' },
    7221: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Voc\xc3\xaa trouxe os travesseiros! Valeu!\x7Ei, espere um segundo! Esses travesseiros s\xc3\xa3o muito macios.\x7Macios demais para mim. Preciso de travesseiros mais duros.\x7Leve estes de volta para o Lel\xc3\xaa e veja o que mais ele tem. Valeu.',
        INCOMPLETE_PROGRESS: 'N\xc3\xa3o! Muito macios. Pe\xc3\xa7a ao Lel\xc3\xaa outros travesseiros.',
        COMPLETE: '' },
    7222: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Muito macios, n\xc3\xa9? Bem, deixe-me ver o que tenho....\x7Hmm... Eu achava que tinha um mont\xc3\xa3o de travesseiros duros. Onde eles est\xc3\xa3o?\x7Ah! Lembrei. Eu estava vendo se conseguia devolv\xc3\xaa-los, ent\xc3\xa3o devem estar no estoque.\x7Que tal eliminar alguns desses edif\xc3\xadcios de Cogs l\xc3\xa1 fora enquanto eu pego os travesseiros no estoque, parceria?',
        INCOMPLETE_PROGRESS: 'Os edif\xc3\xadcios de Cog s\xc3\xa3o duros de roer. Mas esses travesseiros n\xc3\xa3o s\xc3\xa3o.\x7Continuarei procurando.',
        COMPLETE: '' },
    7223: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'J\xc3\xa1 est\xc3\xa1 de volta? Est\xc3\xa1 tudo bem. Veja, encontrei os travesseiros que a Dafne queria.\x7Agora \xc3\xa9 s\xc3\xb3 levar para ela. Eles s\xc3\xa3o duros o suficiente para quebrar um dente!',
        INCOMPLETE_PROGRESS: '\xc3\x89, esses travesseiros s\xc3\xa3o bastante duros. Espero que a Dafne goste deles.',
        COMPLETE: 'Eu sabia que o Lel\xc3\xaa teria alguns travesseiros mais duros.\x7Ah sim, estes s\xc3\xa3o perfeitos. Bons e duros.\x7Por acaso esta pe\xc3\xa7a de vestimenta de Cog seria \xc3\xbatil para voc\xc3\xaa? Pode levar.' },
    7226: {
        QUEST: 'Passe l\xc3\xa1 na Cuca P. Gol. Ela perdeu o pijama._where_' },
    7227: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'N\xc3\xa3o tenho pijamas! Eles sumiram!\x7O que vou fazer? Ah! J\xc3\xa1 sei!\x7V\xc3\xa1 at\xc3\xa9 a Mama. Ela ter\xc3\xa1 pijamas para mim._where_',
        INCOMPLETE_PROGRESS: 'A Mama tem pijamas para mim?',
        COMPLETE: '' },
    7228: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'E a\xc3\xad, pequeno Toon? A Mama tem os melhores pijamas das Bahamas.\x7Ah, quer algo para a Cuca P. Gol, n\xc3\xa9? Bem, deixe-me ver o que tenho aqui.\x7Aqui est\xc3\xa1. Agora, ela pode dormir com estilo!\x7Voc\xc3\xaa pode correr e levar isso para ela? N\xc3\xa3o posso deixar a loja sozinha agora.\x7Obrigada, _avName_. Vejo voc\xc3\xaa por a\xc3\xad!',
        INCOMPLETE_PROGRESS: 'Voc\xc3\xaa precisa levar esse pijama para a Cuca P. Gol._where_',
        COMPLETE: '' },
    7229: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'A Mama mandou esse para mim? Ah...\x7Ela n\xc3\xa3o tem nenhum pijama com p\xc3\xa9s?\x7Eu sempre uso pijamas com p\xc3\xa9s. Todo mundo usa esse tipo de pijama...\x7Leve este de volta e pe\xc3\xa7a a ela que encontre um com p\xc3\xa9s.',
        INCOMPLETE_PROGRESS: 'Meu pijama precisa ter p\xc3\xa9s. Veja o que a Mama pode fazer.',
        COMPLETE: '' },
    7230: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'P\xc3\xa9s? Deixe-me pensar....\x7Espere a\xc3\xad! Eu tenho um perfeito!\x7Tchan! Pijama com p\xc3\xa9s. Um lindo pijama azul com p\xc3\xa9s. O melhor de toda a face da terra.\x7Voc\xc3\xaa pode levar para ela? Valeu!',
        INCOMPLETE_PROGRESS: 'A Cuca P. Gol gostou do pijama azul com p\xc3\xa9s?',
        COMPLETE: '' },
    7231: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Bem, este TEM p\xc3\xa9s, mas n\xc3\xa3o posso usar pijama azul!\x7Pergunte \xc3\xa0 Mama se ela tem uma cor diferente.',
        INCOMPLETE_PROGRESS: 'Tenho certeza de que a Mama tem pijamas em uma cor diferente e com p\xc3\xa9s.',
        COMPLETE: '' },
    7232: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Que pena. Estes s\xc3\xa3o os \xc3\xbanicos pijamas com p\xc3\xa9s que eu tenho.\x7Ah, tive uma ideia. V\xc3\xa1 perguntar \xc3\xa0 outra Cuca. Ela talvez tenha algum pijama com p\xc3\xa9s._where_',
        INCOMPLETE_PROGRESS: 'N\xc3\xa3o, aqueles s\xc3\xa3o os \xc3\xbanicos que eu tenho. V\xc3\xa1 at\xc3\xa9 a outra Cuca para ver o que ela tem._where_',
        COMPLETE: '' },
    7233: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Pijama com p\xc3\xa9s? Sem d\xc3\xbavida.\x7Como assim, este \xc3\xa9 azul? Ela n\xc3\xa3o quer azul?\x7Nossa, vai ser um pouco dif\xc3\xadcil. Veja, que tal este?\x7Ele n\xc3\xa3o \xc3\xa9 azul e TEM p\xc3\xa9s.',
        INCOMPLETE_PROGRESS: 'Eu adoro marrom, voc\xc3\xaa n\xc3\xa3o?\x7Espero que a Cuca P. Gol goste....',
        COMPLETE: '' },
    7234: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'N\xc3\xa3o, este n\xc3\xa3o \xc3\xa9 azul, mas ningu\xc3\xa9m com o meu tom de pele poderia usar marrom.\x7N\xc3\xa3o e n\xc3\xa3o. Ele vai fazer o caminho de volta, e voc\xc3\xaa ir\xc3\xa1 com ele! Veja o que mais a Cuca tem.',
        INCOMPLETE_PROGRESS: 'A Cuca deve ter mais pijamas. Nada de marrom!',
        COMPLETE: '' },
    7235: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'N\xc3\xa3o pode ser marrom tamb\xc3\xa9m. Hmm....\x7Eu sei que tenho outros.\x7Vai demorar um pouquinho para encontr\xc3\xa1-los. Vamos fazer um trato.\x7Eu procuro outro pijama se voc\xc3\xaa derrotar alguns desses edif\xc3\xadcios de Cog. Eles perturbam demais.\x7Terei o pijama quando voc\xc3\xaa voltar, _avName_.',
        INCOMPLETE_PROGRESS: 'Voc\xc3\xaa precisa eliminar mais alguns edif\xc3\xadcios de Cog enquanto eu procuro outro pijama.',
        COMPLETE: '' },
    7236: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Voc\xc3\xaa fez um excelente trabalho com esses Cogs! Valeu!\x7Achei este pijama para a Cuca P. Gol; espero que ela goste.\x7Leve-o para ela. Obrigada.',
        INCOMPLETE_PROGRESS: 'A Cuca P. Gol est\xc3\xa1 esperando pelo pijama, _avName_.',
        COMPLETE: 'Um pijama f\xc3\xbacsia com p\xc3\xa9s! Perr-feito!\x7Ah, agora estou pronta. Vejamos....\x7Acho que devo lhe dar alguma coisa por ter me ajudado.\x7Talvez voc\xc3\xaa possa usar isto. Algu\xc3\xa9m deixou aqui.' },
    7239: {
        QUEST: 'V\xc3\xa1 at\xc3\xa9 a M\xc3\xa1ki Agem. Ela est\xc3\xa1 procurando ajuda._where_' },
    7240: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Aqueles malditos Cogs levaram meu creme para rugas!\x7Meus clientes PRECISAM do creme para rugas enquanto eu trabalho neles.\x7V\xc3\xa1 at\xc3\xa9 o Ded\xc3\xa9 Descanso e veja se ele tem a minha f\xc3\xb3rmula especial no estoque._where_',
        INCOMPLETE_PROGRESS: 'Eu me recuso a trabalhar em algu\xc3\xa9m sem o creme para rugas.\x7Veja o que o Ded\xc3\xa9 Descanso tem para mim.' },
    7241: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'A M\xc3\xa1ki Agem \xc3\xa9 uma figura exigente. Ela n\xc3\xa3o vai se contentar com a minha f\xc3\xb3rmula comum.\x7Isso significa que eu precisarei de alguns corais de couve-flor, meu ingrediente especial supersecreto. Mas eu n\xc3\xa3o tenho nada no estoque.\x7Voc\xc3\xaa poderia pescar alguns na lagoa? Assim que voc\xc3\xaa conseguir os corais, eu farei um lote de creme para a M\xc3\xa1ki Agem.',
        INCOMPLETE_PROGRESS: 'Precisarei do coral de couve-flor para fazer o lote de creme para rugas.' },
    7242: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Uau, que belo coral de couve-flor!\x7Ok, vejamos... Um pouco disto e uma pitada daquilo... Agora, um bocado de alga-marinha.\x7Essa n\xc3\xa3o, onde est\xc3\xa1 a alga-marinha? Parece que estou sem alga-marinha tamb\xc3\xa9m.\x7Voc\xc3\xaa pode voltar \xc3\xa0 lagoa e pescar uma boa alga-marinha viscosa?',
        INCOMPLETE_PROGRESS: 'Nem uma laminazinha de alga-marinha viscosa na loja.\x7N\xc3\xa3o posso fazer o creme sem ela.' },
    7243: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Aaaah! Que \xc3\xb3tima alga-marinha viscosa voc\xc3\xaa trouxe, _avName_.\x7Agora, \xc3\xa9 s\xc3\xb3 espremer algumas p\xc3\xa9rolas no pil\xc3\xa3o.\x7Ih, onde est\xc3\xa1 o meu pil\xc3\xa3o? Como vou fazer sem o pil\xc3\xa3o?\x7Aposto que aquele maldito Agiota o pegou quando esteve aqui!\x7Voc\xc3\xaa precisa me ajudar a encontr\xc3\xa1-lo! Ele estava indo ao Quartel do Rob\xc3\xb4 Mercen\xc3\xa1rio!',
        INCOMPLETE_PROGRESS: 'Eu simplesmente n\xc3\xa3o consigo triturar as p\xc3\xa9rolas sem um pil\xc3\xa3o.\x7Malditos Agiotas!' },
    7244: {
        GREETING: '',
        LEAVING: '',
        QUEST: '\xc3\x93timo! Voc\xc3\xaa trouxe o meu pil\xc3\xa3o!\x7Agora voltemos ao trabalho. Triture aqui... Misture l\xc3\xa1 e...\x7Pronto! Diga \xc3\xa0 M\xc3\xa1ki Agem que \xc3\xa9 de boa qualidade e est\xc3\xa1 fresquinho.',
        INCOMPLETE_PROGRESS: 'Voc\xc3\xaa precisa entregar isso para a M\xc3\xa1ki Agem enquanto est\xc3\xa1 fresco.\x7Ela \xc3\xa9 muito exigente.',
        COMPLETE: 'O Ded\xc3\xa9 Descanso n\xc3\xa3o tinha frasco de creme maior que este? N\xc3\xa3o?\x7Bem, acho que vou pedir mais quando o meu acabar.\x7At\xc3\xa9 logo, _avName_.\x7O qu\xc3\xaa? Voc\xc3\xaa ainda est\xc3\xa1 aqui? N\xc3\xa3o v\xc3\xaa que estou tentando trabalhar?\x7Tome isto aqui.' },
    11000: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Se est\xc3\xa1 interessado em pe\xc3\xa7as de disfarce de Rob\xc3\xb4s da Lei, visite _toNpcName_.\x7Ouvi dizer que ele precisa de ajuda na sua pesquisa sobre o clima._where_' },
    11001: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Sim, sim. Eu tenho pe\xc3\xa7as de disfarce de Rob\xc3\xb4s da Lei.\x7Mas n\xc3\xa3o tenho interesse nelas.\x7O foco da minha pesquisa s\xc3\xa3o as flutua\xc3\xa7\xc3\xb5es na temperatura ambiente de Toontown.\x7Eu troco com voc\xc3\xaa as minhas pe\xc3\xa7as de disfarce por term\xc3\xb4metros de cogs.\x7Voc\xc3\xaa pode come\xc3\xa7ar em %s.' % GlobalStreetNames[2100][-1],
        INCOMPLETE_PROGRESS: 'Tentou procurar em %s?' % GlobalStreetNames[2100][-1],
        COMPLETE: 'Ah, \xc3\xb3timo!\x7Como eu temia...\x7Ah, \xc3\xa9! Aqui est\xc3\xa1 a sua pe\xc3\xa7a de disfarce.' },
    11002: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Para mais pe\xc3\xa7as de disfarce, visite _toNpcName_ de novo.\x7Ouvi dizer que ele precisa de assistentes de pesquisa._where_' },
    11003: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Mais pe\xc3\xa7as de disfarce de Rob\xc3\xb4 da Lei?\x7Bem, se voc\xc3\xaa insiste...\x7mas eu vou precisar de outro term\xc3\xb4metro de Cog.\x7Desta vez, procure em %s.' % GlobalStreetNames[2200][-1],
        INCOMPLETE_PROGRESS: 'Voc\xc3\xaa est\xc3\xa1 procurando em %s, certo?' % GlobalStreetNames[2200][-1],
        COMPLETE: 'Obrigado!\x7E aqui est\xc3\xa1 a sua pe\xc3\xa7a de disfarce.' },
    11004: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Se precisa de mais pe\xc3\xa7as de disfarce de Rob\xc3\xb4 da Lei, v\xc3\xa1 falar com o _toNpcName_.\x7Ouvi que ele ainda precisa de ajuda com a pesquisa sobre o clima._where_' },
    11005: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Voc\xc3\xaa est\xc3\xa1 me saindo bastante \xc3\xbatil!\x7Voc\xc3\xaa pode dar uma ollhada em %s?' % GlobalStreetNames[2300][-1],
        INCOMPLETE_PROGRESS: 'Tem certeza de que est\xc3\xa1 procurando em %s?' % GlobalStreetNames[2300][-1],
        COMPLETE: 'Humm, n\xc3\xa3o gostei muito da apar\xc3\xaancia disto...\x7mas aqui est\xc3\xa1 a sua pe\xc3\xa7a de disfarce...' },
    11006: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Voc\xc3\xaa-sabe-quem precisa de mais medi\xc3\xa7\xc3\xb5es de temperatura.\x7D\xc3\xaa uma passada se quiser mais uma pe\xc3\xa7a de disfarce._where_' },
    11007: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'J\xc3\xa1 de volta?\x7Que dedica\xc3\xa7\xc3\xa3o...\x7A pr\xc3\xb3xima parada \xc3\xa9 %s.' % GlobalStreetNames[1100][-1],
        INCOMPLETE_PROGRESS: 'Voc\xc3\xaa j\xc3\xa1 tentou observar %s?' % GlobalStreetNames[1100][-1],
        COMPLETE: 'Isso! Parece que voc\xc3\xaa est\xc3\xa1 pegando o jeito da coisa!\x7A sua pe\xc3\xa7a de disfarce...' },
    11008: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Se estiver a fim de mais uma pe\xc3\xa7a de disfarce de Rob\xc3\xb4 da Lei..._where_' },
    11009: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Engra\xc3\xa7ado encontrar voc\xc3\xaa aqui!\x7Agora, eu preciso de medi\xc3\xa7\xc3\xb5es em %s.' % GlobalStreetNames[1200][-1],
        INCOMPLETE_PROGRESS: 'Voc\xc3\xaa est\xc3\xa1 procurando em %s, certo?' % GlobalStreetNames[1200][-1],
        COMPLETE: 'Muito obrigado.\x7O seu disfarce deve estar quase pronto...' },
    11010: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Acredito que _toNpcName_ tem mais um trabalho para voc\xc3\xaa._where_' },
    11011: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Que bom ver voc\xc3\xaa de novo, _avName_!\x7Voc\xc3\xaa pode fazer uma medi\xc3\xa7\xc3\xa3o em %s, por favor?' % GlobalStreetNames[1300][-1],
        INCOMPLETE_PROGRESS: 'Tentou procurar em %s?' % GlobalStreetNames[1300][-1],
        COMPLETE: '\xc3\x93timo trabalho!\x7Aqui est\xc3\xa1 a sua merecida recompensa!' },
    11012: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Voc\xc3\xaa sabe o que fazer._where_' },
    11013: {
        GREETING: '',
        LEAVING: '',
        QUEST: '_avName_, meu caro!\x7Voc\xc3\xaa pode ir at\xc3\xa9 %s e encontrar mais um term\xc3\xb4metro para mim?' % GlobalStreetNames[5100][-1],
        INCOMPLETE_PROGRESS: 'Tem certeza de que est\xc3\xa1 procurando em %s?' % GlobalStreetNames[5100][-1],
        COMPLETE: 'Excelente!\x7Com a sua ajuda, a minha pesquisa est\xc3\xa1 caminhando!\x7Aqui est\xc3\xa1 a sua recompensa.' },
    11014: {
        GREETING: '',
        LEAVING: '',
        QUEST: '_toNpcName_ estava pedindo por voc\xc3\xaa.\x7Parece que voc\xc3\xaa causou uma boa impress\xc3\xa3o!_where_' },
    11015: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Bem-vindo de volta!\x7Estive esperando.\x7A pr\xc3\xb3xima medi\xc3\xa7\xc3\xa3o tem que ser em %s.' % GlobalStreetNames[5200][-1],
        INCOMPLETE_PROGRESS: 'Voc\xc3\xaa est\xc3\xa1 procurando em %s, certo?' % GlobalStreetNames[5200][-1],
        COMPLETE: 'Obrigado!\x7Aqui est\xc3\xa1 sua recompensa.' },
    11016: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Se precisa completar o seu disfarce de Rob\xc3\xb4 da Lei...\x7_toNpcName_ pode ajudar voc\xc3\xaa._where_' },
    11017: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Ol\xc3\xa1, Cientista de Pesquisas Iniciante!\x7Ainda precisamos de medi\xc3\xa7\xc3\xb5es de %s.' % GlobalStreetNames[5300][-1],
        INCOMPLETE_PROGRESS: 'Tentou procurar em %s?' % GlobalStreetNames[5300][-1],
        COMPLETE: '\xc3\x93timo trabalho!\x7Aqui est\xc3\xa1 o seu neg\xc3\xb3cio de Rob\xc3\xb4 da Lei...' },
    11018: {
        GREETING: '',
        LEAVING: '',
        QUEST: '_toNpcName_ tem outro trabalho para voc\xc3\xaa.\x7Se ainda n\xc3\xa3o tiver se cansado dele..._where_' },
    11019: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Ent\xc3\xa3o.\x7Pronto para outra recupera\xc3\xa7\xc3\xa3o?\x7Desta vez, tente %s.' % GlobalStreetNames[4100][-1],
        INCOMPLETE_PROGRESS: 'Tem certeza de que est\xc3\xa1 procurando em %s?' % GlobalStreetNames[4100][-1],
        COMPLETE: 'Mais um!\x7Nossa, voc\xc3\xaa \xc3\xa9 a efici\xc3\xaancia em pessoa!' },
    11020: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Ainda est\xc3\xa1 atr\xc3\xa1s de pe\xc3\xa7as de disfarce de Rob\xc3\xb4 da Lei?_where_' },
    11021: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Voc\xc3\xaa j\xc3\xa1 deve ter adivinhado...\x7mas eu preciso de medi\xc3\xa7\xc3\xb5es de %s.' % GlobalStreetNames[4200][-1],
        INCOMPLETE_PROGRESS: 'Voc\xc3\xaa est\xc3\xa1 procurando em %s, certo?' % GlobalStreetNames[4200][-1],
        COMPLETE: 'Quase l\xc3\xa1!\x7Aqui est\xc3\xa1...' },
    11022: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Odeio dizer isto, mas..._where_' },
    11023: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'O que acha de %s? Poderia conseguir um term\xc3\xb4metro de l\xc3\xa1 tamb\xc3\xa9m?' % GlobalStreetNames[4300][-1],
        INCOMPLETE_PROGRESS: 'Tentou procurar em %s?' % GlobalStreetNames[4300][-1],
        COMPLETE: 'Outro \xc3\xb3timo trabalho, _avName_' },
    11024: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'V\xc3\xa1 visitar o Professor se ainda precisar de pe\xc3\xa7as de disfarce._where_' },
    11025: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Acho que ainda precisamos de uma medi\xc3\xa7\xc3\xa3o de %s.' % GlobalStreetNames[9100][-1],
        INCOMPLETE_PROGRESS: 'Tem certeza de que est\xc3\xa1 procurando em %s?' % GlobalStreetNames[9100][-1],
        COMPLETE: 'Bom trabalho!\x7Acho que estamos chegando perto...' },
    11026: {
        GREETING: '',
        LEAVING: '',
        QUEST: '_toNpcName_ tem uma \xc3\xbaltima miss\xc3\xa3o para voc\xc3\xaa._where_' },
    11027: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'J\xc3\xa1 de volta?\x7A medi\xc3\xa7\xc3\xa3o final \xc3\xa9 em %s.' % GlobalStreetNames[9200][-1],
        INCOMPLETE_PROGRESS: 'Voc\xc3\xaa est\xc3\xa1 procurando em %s, certo?' % GlobalStreetNames[9200][-1],
        COMPLETE: 'Est\xc3\xa1 pronto!\x7Agora, voc\xc3\xaa j\xc3\xa1 pode se infiltrar no Escrit\xc3\xb3rio do Promotor P\xc3\xbablico e coletar Avisos de J\xc3\xbari.\x7Boa sorte e obrigado pela sua ajuda!' },
    12000: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Se quiser pe\xc3\xa7as de disfarce de Rob\xc3\xb4 Chefe, deve visitar _toNpcName_._where_' },
    12001: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Sim, posso pegar as suas pe\xc3\xa7as de Rob\xc3\xb4-Chefe.\x7Mas vou precisar de sua ajuda para completar a minha cole\xc3\xa7\xc3\xa3o de Rob\xc3\xb4-Chefe.\x7V\xc3\xa1 l\xc3\xa1 fora e derrote um Puxa-saco.   ',
        INCOMPLETE_PROGRESS: 'N\xc3\xa3o consegue encontrar um Puxa-saco? Que vergonha...',
        COMPLETE: 'Voc\xc3\xaa n\xc3\xa3o fracassou, n\xc3\xa3o \xc3\xa9?\\ aAqui est\xc3\xa1 a sua primeira pe\xc3\xa7a de disfarce. ' },
    12002: {
        GREETING: '',
        LEAVING: '',
        QUEST: '_toNpcName_ precisa de mais ajuda se voc\xc3\xaa puder._where_ ' },
    12003: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Outra pe\xc3\xa7a de disfarce?\x7Certamente...\x7Mas s\xc3\xb3 se voc\xc3\xaa derrotar um Rato de Escrit\xc3\xb3rio. ',
        INCOMPLETE_PROGRESS: 'Os Rato de Escrit\xc3\xb3rio podem ser encontrados nas ruas.',
        COMPLETE: 'Ele realmente foi um fracote! \\ aAqui est\xc3\xa1 sua segunda pe\xc3\xa7a de disfarce.' },
    12004: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'S\xc3\xb3 h\xc3\xa1 mesmo um lugar onde encontrar pe\xc3\xa7as de Rob\xc3\xb4-Chefe._where_' },
    12005: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Agora, preciso de um \xe2\x80\x9cVaquinha de Pres\xc3\xa9pio\xe2\x80\x9d...',
        INCOMPLETE_PROGRESS: 'O \xe2\x80\x9cVaquinha de Pres\xc3\xa9pio\xe2\x80\x9d pode ser encontrado nas ruas.',
        COMPLETE: 'Isso! Cara, voc\xc3\xaa \xc3\xa9 demais.\x7Aqui est\xc3\xa1 sua terceira pe\xc3\xa7a de disfarce.' },
    12006: {
        GREETING: '',
        LEAVING: '',
        QUEST: '_toNpcName_ tem mais pe\xc3\xa7as para voc\xc3\xaa... ' },
    12007: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Se voc\xc3\xaa derrotar um Micro\x4empres\xc3\xa1rio, darei a voc\xc3\xaa mais uma pe\xc3\xa7a.',
        INCOMPLETE_PROGRESS: 'Tente procurar em %s' % GlobalStreetNames[1100][-1],
        COMPLETE: 'Voc\xc3\xaa se saiu muito bem!\x7Aqui est\xc3\xa1 sua quarta pe\xc3\xa7a de disfarce.' },
    12008: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Direto para..._where_' },
    12009: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Agora estou atr\xc3\xa1s de um Fac\xc3\xa3o...',
        INCOMPLETE_PROGRESS: 'Algum problema? Tente procurar em %s' % GlobalStreetNames[3100][-1],
        COMPLETE: 'N\xc3\xa3o foi t\xc3\xa3o dif\xc3\xadcil!\x7Aqui est\xc3\xa1 sua quinta pe\xc3\xa7a de disfarce. ' },
    12010: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Acho que voc\xc3\xaa sabe aonde ir agora..._where_' },
    12011: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Um Ca\xc3\xa7a-\x4talentos \xc3\xa9 o pr\xc3\xb3ximo da minha lista.',
        INCOMPLETE_PROGRESS: 'Voc\xc3\xaa ter\xc3\xa1 mais sorte procurando em edif\xc3\xadcios.',
        COMPLETE: 'Vejo que n\xc3\xa3o teve problemas para ca\xc3\xa7ar um desses.\x7Aqui est\xc3\xa1 sua sexta pe\xc3\xa7a de disfarce. ' },
    12012: {
        GREETING: '',
        LEAVING: '',
        QUEST: '_toNpcName_ precisa de mais Rob\xc3\xb4s-Chefe. ' },
    12013: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'A seguir, preciso que voc\xc3\xaa localize um Aventureiro Corporativo.',
        INCOMPLETE_PROGRESS: 'Voc\xc3\xaa ter\xc3\xa1 mais sorte procurando em edif\xc3\xadcios.',
        COMPLETE: 'Voc\xc3\xaa leva mesmo jeito para isso!\x7Aqui est\xc3\xa1 sua s\xc3\xa9tima pe\xc3\xa7a de disfarce.' },
    12014: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Se quiser mais pe\xc3\xa7as de disfarce, v\xc3\xa1 para..._where_' },
    12015: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Agora, o mais precioso de todos: O um Rei da Cocada Preta!',
        INCOMPLETE_PROGRESS: 'Tente procurar em %s' % GlobalStreetNames[10000][-1],
        COMPLETE: 'Sabia que podia contar com voc\xc3\xaa para cortar...\x7Ah, n\xc3\xa3o importa.\x7Aqui est\xc3\xa1 sua pr\xc3\xb3xima pe\xc3\xa7a de disfarce. ' },
    12016: {
        GREETING: '',
        LEAVING: '',
        QUEST: '_toNpcName_ estava \xc3\xa0 sua procura...' },
    12017: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Agora, preciso que voc\xc3\xaa derrote um dos novos e mais trai\xc3\xa7oeiros Cogs de Rob\xc3\xb4-Chefe.',
        INCOMPLETE_PROGRESS: 'Tente procurar em %s' % GlobalStreetNames[10000][-1],
        COMPLETE: 'Eles s\xc3\xa3o mais fortes do que parecem, hein?\x7Acho que lhe devo uma pe\xc3\xa7a de disfarce. ' },
    12018: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Pode dar um giro at\xc3\xa9..._where_' },
    12019: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Esses Cogs vers\xc3\xa3o 2.0 s\xc3\xa3o muito interessantes.\x7Por favor, derrote mais um.  ',
        INCOMPLETE_PROGRESS: 'Tente procurar em %s' % GlobalStreetNames[10000][-1],
        COMPLETE: 'Valeu!\x7Mais uma pe\xc3\xa7a de disfarce chegando. ' },
    12020: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Se tiver a oportunidade, d\xc3\xaa uma parada e visite _toNpcName_.' },
    12021: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Imagino se puderem se regenerar...',
        INCOMPLETE_PROGRESS: 'Tente procurar em %s' % GlobalStreetNames[10000][-1],
        COMPLETE: 'Acho que n\xc3\xa3o.\x7Aqui est\xc3\xa1 sua pe\xc3\xa7a... ' },
    12022: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Voc\xc3\xaa sabe..._where' },
    12023: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Talvez n\xc3\xa3o sejam Rob\xc3\xb4s-Chefe afinal...',
        INCOMPLETE_PROGRESS: 'Tente procurar em %s' % GlobalStreetNames[10000][-1],
        COMPLETE: 'Hummm, acho que realmente s\xc3\xa3o Rob\xc3\xb4s-Chefe.\x7Consiga mais uma pe\xc3\xa7a. ' },
    12024: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Voc\xc3\xaa provavelmente j\xc3\xa1 sabe o que vou dizer...' },
    12025: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Talvez, de alguma maneira, estejam relacionados aos Esqueletocogs... ',
        INCOMPLETE_PROGRESS: 'Tente procurar em %s' % GlobalStreetNames[10000][-1],
        COMPLETE: 'Isso foi inconsequente...\x7Aqui est\xc3\xa1 sua pe\xc3\xa7a de disfarce. ' },
    12026: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Por favor, visite _toNpcName_ novamente.' },
    12027: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Ainda tenho d\xc3\xbavidas de que n\xc3\xa3o sejam algum tipo de Esqueletocogs...',
        INCOMPLETE_PROGRESS: 'Tente procurar em %s' % GlobalStreetNames[10000][-1],
        COMPLETE: 'Bem, talvez n\xc3\xa3o.\x7Aqui est\xc3\xa1 sua pr\xc3\xb3xima pe\xc3\xa7a. ' },
    12028: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Talvez seja o \xc3\xbaltimo lugar a que gostaria de ir. Mas...' },
    12029: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Esses novos Cogs ainda me deixam d\xc3\xbavidas.\x7Poderia derrotar mais um, por favor?',
        INCOMPLETE_PROGRESS: 'Tente procurar em %s' % GlobalStreetNames[10000][-1],
        COMPLETE: 'Fascinante. Simplesmente fascinante.\x7Uma pe\xc3\xa7a de disfarce pelos inconvenientes. ' },
    12030: {
        GREETING: '',
        LEAVING: '',
        QUEST: '_toNpcName_ est\xc3\xa1 come\xc3\xa7ando a parecer um disco riscado...' },
    12031: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'J\xc3\xa1 havia quase descoberto o que s\xc3\xa3o esses novos Cogs.\x7S\xc3\xb3 mais um... ',
        INCOMPLETE_PROGRESS: 'Tente procurar em %s' % GlobalStreetNames[10000][-1],
        COMPLETE: 'Sim, acho que encontrei algo importante.\x7Ah, sim.\x7Isso \xc3\xa9 para voc\xc3\xaa... ' },
    12032: {
        GREETING: '',
        LEAVING: '',
        QUEST: 'Voc\xc3\xaa precisa contar ao Flippy sobre isso...',
        INCOMPLETE_PROGRESS: 'Flippy est\xc3\xa1 no Toon Hall',
        COMPLETE: 'Um novo tipo de Cog!\x7Bom trabalho!\x7Aqui est\xc3\xa1 sua \xc3\xbaltima pe\xc3\xa7a de disfarce.  ' } }
ChatGarblerDog = [
    'au',
    'arf',
    'grrrr']
ChatGarblerCat = [
    'miau',
    'miu']
ChatGarblerMouse = [
    'quick',
    'quiiii',
    'quiiiiquiiii']
ChatGarblerHorse = [
    'r\xc3\xad\xc3\xad\xc3\xadrrrr',
    'brrr']
ChatGarblerRabbit = [
    'ick',
    'iipr',
    'iipi',
    'iicki']
ChatGarblerDuck = [
    'qu\xc3\xa1',
    'quack',
    'qu\xc3\xa1\xc3\xa1\xc3\xa1ck']
ChatGarblerMonkey = [
    'ooh',
    'ooo',
    'ahh']
ChatGarblerBear = [
    'grrrau',
    'grrr']
ChatGarblerPig = [
    'oinc',
    'oic',
    'rrroinc']
ChatGarblerDefault = [
    'bl\xc3\xa1']
Bossbot = 'Rob\xc3\xb4-chefe'
Lawbot = 'Rob\xc3\xb4 da Lei'
Cashbot = 'Rob\xc3\xb4 Mercen\xc3\xa1rio'
Sellbot = 'Rob\xc3\xb4 Vendedor'
BossbotS = 'um Rob\xc3\xb4-chefe'
LawbotS = 'um Rob\xc3\xb4 da Lei'
CashbotS = 'um Rob\xc3\xb4 Mercen\xc3\xa1rio'
SellbotS = 'um Rob\xc3\xb4 Vendedor'
BossbotP = 'Rob\xc3\xb4s-chefe'
LawbotP = 'Rob\xc3\xb4s da Lei'
CashbotP = 'Rob\xc3\xb4s Mercen\xc3\xa1rios'
SellbotP = 'Rob\xc3\xb4s Vendedores'
BossbotSkelS = 'um Esqueletocog %s' % Bossbot
LawbotSkelS = 'um Esqueletocog %s' % Lawbot
CashbotSkelS = 'um Esqueletocog %s' % Cashbot
SellbotSkelS = 'um Esqueletocog %s' % Sellbot
BossbotSkelP = 'Esqueletocogs %s' % BossbotP
LawbotSkelP = 'Esqueletocogs %s' % LawbotP
CashbotSkelP = 'Esqueletocogs %s' % CashbotP
SellbotSkelP = 'Esqueletocogs %s' % SellbotP
SkeleRevivePostFix = ' v2.0'
AvatarDetailPanelOK = lOK
AvatarDetailPanelCancel = lCancel
AvatarDetailPanelClose = lClose
AvatarDetailPanelLookup = 'Procurando detalhes de %s.'
AvatarDetailPanelFailedLookup = 'N\xc3\xa3o foi poss\xc3\xadvel obter detalhes de %s.'
AvatarDetailPanelPlayer = 'Jogador: %(player)s\nMundo: %(world)s'
AvatarDetailPanelPlayerShort = '%(player)s\nMundo: %(world)s\nLocal: %(location)s'
AvatarDetailPanelRealLife = 'Off-line'
AvatarDetailPanelOnline = 'Regi\xc3\xa3o: %(district)s\nLocal: %(location)s'
AvatarDetailPanelOnlinePlayer = 'Regi\xc3\xa3o: %(district)s\nLocal: %(location)s\nJogador: %(player)s'
AvatarDetailPanelOffline = 'Regi\xc3\xa3o: off-line\nLocal: off-line'
AvatarShowPlayer = 'Exibir Jogador'
OfflineLocation = 'Off-line'
PlayerToonName = 'Toon: %(toonname)s'
PlayerShowToon = 'Mostrar Toon'
PlayerPanelDetail = 'Detalhes do jogador'
AvatarPanelFriends = 'Amigos'
AvatarPanelWhisper = 'Cochichar'
AvatarPanelSecrets = 'Segredos'
AvatarPanelGoTo = 'Ir para'
AvatarPanelPet = 'Mostrar Rabisco'
AvatarPanelIgnore = 'Ignorar'
AvatarPanelIgnoreCant = 'OK'
AvatarPanelStopIgnoring = 'Parar de Ignorar'
AvatarPanelReport = 'Relatar'
AvatarPanelCogLevel = 'N\xc3\xadvel: %s'
AvatarPanelCogDetailClose = lClose
AvatarPanelDetail = 'Detalhes do Toon'
AvatarPanelGroupInvite = 'Convidar para Grupo'
AvatarPanelGroupRetract = 'Retirar Convite'
AvatarPanelGroupMember = 'J\xc3\xa1 no Grupo'
AvatarPanelGroupMemberKick = 'Remova'
ReportPanelTitle = 'Denunciar um Jogador'
ReportPanelBody = 'Este recurso enviar\xc3\xa1 uma den\xc3\xbancia completa a um Moderador. Em vez de denunciar, voc\xc3\xaa pode optar pelo seguinte:\n\n  - Teleportar-se para outra regi\xc3\xa3o\n  - Usar "Ignorar" no painel do Toon\n\nQuer mesmo denunciar %s para um Moderador?'
ReportPanelBodyFriends = 'Este recurso enviar\xc3\xa1 uma den\xc3\xbancia completa a um Moderador. Em vez de denunciar, voc\xc3\xaa pode optar pelo seguinte:\n\n  - Teleportar-se para outra regi\xc3\xa3o\n  - Romper sua amizade\n\nQuer mesmo denunciar %s para um Moderador?\n\n(Isso tamb\xc3\xa9m vai romper sua amizade)'
ReportPanelCategoryBody = 'Voc\xc3\xaa est\xc3\xa1 prestes a denunciar %s. Um Moderador ser\xc3\xa1 alertado sobre sua reclama\xc3\xa7\xc3\xa3o e tomar\xc3\xa1 medidas apropriadas contra quem estiver quebrando as regras. Escolha o motivo pelo qual est\xc3\xa1 denunciando %s:'
ReportPanelBodyPlayer = 'Este recurso ainda est\xc3\xa1 sendo desenvolvido e ser\xc3\xa1 disponibilizado em breve. Enquanto isso, voc\xc3\xaa pode fazer o seguinte:\n\n  - V\xc3\xa1 at\xc3\xa9 o DXD e termine a amizade por l\xc3\xa1.\n \xe2\x80\x93 Conte aos pais ou respons\xc3\xa1veis o que est\xc3\xa1 acontecendo.'
ReportPanelCategoryLanguage = 'Linguagem Rude'
ReportPanelCategoryPii = 'Compartilhar/Solicitar Informa\xc3\xa7\xc3\xb5es Pessoais'
ReportPanelCategoryRude = 'Comportamento Rude ou Mau'
ReportPanelCategoryName = 'Nome Ruim'
ReportPanelCategoryHacking = 'Hacking'
ReportPanelConfirmations = ('Voc\xc3\xaa est\xc3\xa1 prestes a denunciar que %s usou linguagem obscena, intolerante, preconceituosa ou sexualmente expl\xc3\xadcita.', 'Voc\xc3\xaa est\xc3\xa1 prestes a denunciar %s est\xc3\xa1 promovendo inseguran\xc3\xa7a ao divulgar ou solicitar um n\xc3\xbamero de telefone, sobrenome, endere\xc3\xa7o de e-mail, senha ou nome de conta.', 'Voc\xc3\xaa est\xc3\xa1 prestes a relatar que %s est\xc3\xa1 importunando, atormentando ou usando de comportamento radical para atrapalhar o jogo.', 'Voc\xc3\xaa est\xc3\xa1 prestes a relatar que %s criou um nome que n\xc3\xa3o segue as regras da Disney.', 'You are about to report that %s is hacking the game.')
ReportPanelWarning = "Levamos as den\xc3\xbancias muito a s\xc3\xa9rio. Sua den\xc3\xbancia ser\xc3\xa1 vista por um Moderador, que tomar\xc3\xa1 medidas contra qualquer um que quebrar nossas regras. Se for descoberto que sua conta tamb\xc3\xa9m quebrou as regras, ou se voc\xc3\xaa fizer den\xc3\xbancias falsas ou abusar do sistema 'Denunciar um Jogador', um Moderador pode tomar medidas contra sua conta. Tem certeza absoluta de que quer denunciar este jogador?"
ReportPanelThanks = 'Obrigado! Sua den\xc3\xbancia foi enviada a um Moderador para an\xc3\xa1lise. N\xc3\xa3o h\xc3\xa1 necessidade de nos contatarmos novamente sobre o problema. A equipe de modera\xc3\xa7\xc3\xa3o tomar\xc3\xa1 medidas adequadas contra um jogador que for descoberto quebrando as regras.'
ReportPanelRemovedFriend = 'Removemos automaticamente %s da sua Lista de Amigos.'
ReportPanelRemovedPlayerFriend = 'Removemos automaticamente %s como amigo Jogador, e voc\xc3\xaa n\xc3\xa3o o ver\xc3\xa1 mais como seu amigo em nenhum produto Disney.'
ReportPanelAlreadyReported = 'Voc\xc3\xaa j\xc3\xa1 denunciou %s nesta sess\xc3\xa3o. Um Moderador vai analisar sua den\xc3\xbancia anterior.'
IgnorePanelTitle = 'Ignorar um Jogador'
IgnorePanelAddIgnore = 'Quer ignorar %s pelo restante da sess\xc3\xa3o?'
IgnorePanelIgnore = 'Voc\xc3\xaa agora est\xc3\xa1 ignorando %s.'
IgnorePanelRemoveIgnore = 'Deseja parar de ignorar %s?'
IgnorePanelEndIgnore = 'Voc\xc3\xaa n\xc3\xa3o est\xc3\xa1 mais ignorando %s.'
IgnorePanelAddFriendAvatar = '%s est\xc3\xa1 entre seus amigos, voc\xc3\xaa n\xc3\xa3o pode ignor\xc3\xa1-lo(la)enquanto forem amigos(as).'
IgnorePanelAddFriendPlayer = '%s (%s)est\xc3\xa1 entre seus amigos, voc\xc3\xaa n\xc3\xa3o pode ignor\xc3\xa1-lo(la) enquanto forem amigos(as).'
PetPanelFeed = 'Alimentar'
PetPanelCall = 'Chamar'
PetPanelGoTo = 'Ir para'
PetPanelOwner = 'Mostrar dono'
PetPanelDetail = 'Detalhes do bichinho'
PetPanelScratch = 'Co\xc3\xa7ar'
PetDetailPanelTitle = 'Adestramento'
PetTrickStrings = {
    0: 'Pular',
    1: 'Dar a pata',
    2: 'Fingir de morto',
    3: 'Rolar',
    4: 'Dar cambalhota',
    5: 'Dan\xc3\xa7ar',
    6: 'Falar' }
PetMoodAdjectives = {
    'neutral': 'neutro',
    'hunger': 'faminto',
    'boredom': 'chateado',
    'excitement': 'animado',
    'sadness': 'triste',
    'restlessness': 'inquieto',
    'playfulness': 'brincalh\xc3\xa3o',
    'loneliness': 'solit\xc3\xa1rio',
    'fatigue': 'cansado',
    'confusion': 'confuso',
    'anger': 'zangado',
    'surprise': 'surpreso',
    'affection': 'carinhoso' }
SpokenMoods = {
    'neutral': 'neutral',
    'hunger': [
        'Estou cansado de balinhas em forma de feij\xc3\xa3o! Que tal me dar um peda\xc3\xa7o de torta?',
        'Que tal uma Balinha Vermelha? Estou enjoado das Verdes!',
        'Ah, aquelas balinhas em forma de feij\xc3\xa3o eram para plantar? Mas eu estou com fome!'],
    'boredom': [
        'Estou morrendo de t\xc3\xa9dio aqui!',
        'Voc\xc3\xaa n\xc3\xa3o achou que eu entendi voc\xc3\xaa, n\xc3\xa9?',
        'N\xc3\xb3s j\xc3\xa1 podemos FAZER alguma coisa?'],
    'excitement': [
        'OMD, \xc3\xa9 voc\xc3\xaa, \xc3\xa9 voc\xc3\xaa, \xc3\xa9 voc\xc3\xaa!',
        'hmmm, balinhas, hmmm!',
        'Tem como isso ficar ainda melhor?',
        'Feliz Semana Abril Toons!'],
    'sadness': [
        'N\xc3\xa3o vai, N\xc3\xa3o vai, N\xc3\xa3o vai, N\xc3\xa3o vai, N\xc3\xa3o vai, N\xc3\xa3o vai, N\xc3\xa3o vai, N\xc3\xa3o vai, N\xc3\xa3o vai, N\xc3\xa3o vai, N\xc3\xa3o vai...',
        'Vou ficar bem. Eu juro!',
        'Eu n\xc3\xa3o sei POR QUE estou triste. Apenas estou!!!'],
    'restlessness': [
        'Estou t\xc3\xa3\xc3\xa3\xc3\xa3\xc3\xa3\xc3\xa3o impaciente!!!'],
    'playfulness': [
        'Vamos brincar, Vamos brincar, Vamos brincar, Vamos brincar, Vamos brincar, Vamos brincar, Vamos brincar, Vamos brincar, Vamos brincar...',
        'Brinque comigo ou eu arrancarei algumas flores!',
        'Vamos dar uma volta por a\xc3\xad e a\xc3\xad e a\xc3\xad e a\xc3\xad e a\xc3\xad e a\xc3\xad...'],
    'loneliness': [
        'Onde voc\xc3\xaa esteve?',
        'Quer um abra\xc3\xa7o?',
        'Eu quero ir junto quando voc\xc3\xaa for lutar com os Cogs!'],
    'fatigue': [
        'Aquele mergulho no lago realmente me cansou!',
        'Ser um Doodle \xc3\xa9 cansativo!',
        'Eu preciso ir para a Terra do Sonho!'],
    'confusion': [
        'Onde estou? De novo, quem \xc3\xa9 voc\xc3\xaa?',
        'De novo, o que \xc3\xa9 Toon-up?',
        'Opa, eu estou entre voc\xc3\xaa e os Cogs! Fuja!'],
    'anger': [
        '... e voc\xc3\xaa ainda se pergunta por que eu nunca lhe dei um Toon-up?!!!',
        'Voc\xc3\xaa sempre se esquece de mim!',
        'Voc\xc3\xaa ama suas piadas mais do que a mim!'],
    'surprise': [
        'Claro, Doodles podem falar!',
        'Toons podem falar?!!',
        'Opa, de onde voc\xc3\xaa surgiu?'],
    'affection': [
        'Voc\xc3\xaa \xc3\xa9 o melhor Toon que j\xc3\xa1 EXISTIU!!!!!!!!!!',
        'Voc\xc3\xaa tem NO\xc3\x87\xc3\x83O do quanto \xc3\xa9 bacana?',
        'Eu tenho MUITA sorte de estar com voc\xc3\xaa!!!'] }
DialogQuestion = '?'
FriendsListLabel = 'Amigos'
TeleportPanelOK = lOK
TeleportPanelCancel = lCancel
TeleportPanelYes = lYes
TeleportPanelNo = lNo
TeleportPanelCheckAvailability = 'Tentando ir para %s.'
TeleportPanelNotAvailable = '%s est\xc3\xa1 ocupado(a) agora; tente novamente mais tarde.'
TeleportPanelIgnored = '%s est\xc3\xa1 ignorando voc\xc3\xaa.'
TeleportPanelNotOnline = '%s n\xc3\xa3o est\xc3\xa1 on-line neste momento.'
TeleportPanelWentAway = '%s saiu.'
TeleportPanelUnknownHood = 'Voc\xc3\xaa n\xc3\xa3o sabe ir para %s!'
TeleportPanelUnavailableHood = '%s n\xc3\xa3o est\xc3\xa1 dispon\xc3\xadvel agora; tente novamente mais tarde.'
TeleportPanelDenySelf = 'Voc\xc3\xaa n\xc3\xa3o pode ir l\xc3\xa1 por conta pr\xc3\xb3pria!'
TeleportPanelOtherShard = '%(avName)s est\xc3\xa1 na regi\xc3\xa3o %(shardName)s, e voc\xc3\xaa est\xc3\xa1 na regi\xc3\xa3o %(myShardName)s. Deseja ir para %(shardName)s?'
TeleportPanelBusyShard = '%(avName)s est\xc3\xa1 em uma Regi\xc3\xa3o lotada. Jogar em uma Regi\xc3\xa3o lotada pode afetar severamente o desempenho do jogo. Tem certeza de que quer mudar de regi\xc3\xa3o?'
BattleBldgBossTaunt = 'Sou o chefe.'
FactoryBossTaunt = 'Sou o Supervisor.'
FactoryBossBattleTaunt = 'Deixe-me te apresentar ao Supervisor.'
MintBossTaunt = 'Sou o Supervisor.'
MintBossBattleTaunt = 'Voc\xc3\xaa precisa falar com o Supervisor.'
StageBossTaunt = 'A minha Justi\xc3\xa7a n\xc3\xa3o \xc3\xa9 Cega'
StageBossBattleTaunt = 'Eu estou acima da Lei'
CountryClubBossTaunt = 'Sou o Presidente do Clube.'
CountryClubBossBattleTaunt = 'Voc\xc3\xaa precisa falar com o Presidente do Clube.'
ForcedLeaveCountryClubAckMsg = 'O Presidente do Clube foi derrotado antes que voc\xc3\xaa pudesse chegar a ele. Voc\xc3\xaa n\xc3\xa3o recuperou nenhuma A\xc3\xa7\xc3\xa3o.'
ToonHealJokes = [
    [
        'O que faz TIQUE-TIQUE-TIQUE-AU?',
        'Um c\xc3\xa3on\xc3\xb4metro!'],
    [
        'Por que o louco toma banho com o chuveiro desligado?',
        'Porque ele comprou xamp\xc3\xba para cabelos secos!'],
    [
        'Por que \xc3\xa9 dif\xc3\xadcil para o fantasma contar mentiras?',
        'Porque seus pensamentos s\xc3\xa3o transparentes.'],
    [
        'Do que a bailarina \xc3\xa9 chamada quando machuca o p\xc3\xa9 e se recusa a dan\xc3\xa7ar?',
        'P\xc3\xa9-n\xc3\xb3stica!'],
    [
        'O que a vaca foi fazer no espa\xc3\xa7o?',
        'Foi se encontrar com o v\xc3\xa1cuo!'],
    [
        'Por que o gato mia para a Lua e a Lua n\xc3\xa3o mia para o gato?',
        'Porque astro-no-mia!'],
    [
        'Por que as tartarugas n\xc3\xa3o ficam b\xc3\xaabadas?',
        'Porque elas s\xc3\xb3 t\xc3\xaam um casco!'],
    [
        'Por que o elefante usa t\xc3\xaanis vermelhos?',
        'Porque os branquinhos sujam muito.'],
    [
        'Por que a galinha atravessa a rua?',
        'Para chegar ao outro lado!'],
    [
        'Qual \xc3\xa9 a maior injusti\xc3\xa7a do Natal?',
        'O peru morre e a missa \xc3\xa9 do galo.'],
    [
        'Qual \xc3\xa9 o c\xc3\xbamulo dos trabalhos manuais?',
        'Tricotar com a linha do trem.'],
    [
        'O que \xc3\xa9 um vulc\xc3\xa3o?',
        'Uma montanha com solu\xc3\xa7o.'],
    [
        'O que \xc3\xa9 um pontinho vermelho, um azul e um rosa em cima de uma \xc3\xa1rvore?',
        'Um morangotango com urublue num pinkenick.'],
    [
        'Por que o elefante n\xc3\xa3o consegue tirar carteira de motorista?',
        'Porque ele s\xc3\xb3 d\xc3\xa1 trombada.'],
    [
        'O que um tijolo disse para o outro?',
        "Existe um 'ciumento' entre n\xc3\xb3s."],
    [
        'O que a porta disse para a chave?',
        'Vamos dar uma voltinha.'],
    [
        'O que o el\xc3\xa9tron fala quando atende ao telefone?',
        'Pr\xc3\xb3ton!'],
    [
        'Quem \xc3\xa9 o rei da horta?',
        'Rei Polho.'],
    [
        'Por que as pilhas s\xc3\xa3o melhores que os pol\xc3\xadticos?',
        'Porque elas t\xc3\xaam, pelo menos, um lado positivo.'],
    [
        'O que Benjamin Franklin disse quando inventou a eletricidade?',
        'Nada. Ele estava em estado de choque.'],
    [
        'Por que o cachorro balan\xc3\xa7a o rabo?',
        'Porque o rabo n\xc3\xa3o tem for\xc3\xa7a para balan\xc3\xa7ar o cachorro.'],
    [
        'Qual \xc3\xa9 o c\xc3\xbamulo da for\xc3\xa7a?',
        'Dobrar a esquina.'],
    [
        'O que n\xc3\xa3o \xc3\xa9 de comer, mas d\xc3\xa1 \xc3\xa1gua na boca?',
        'O copo.'],
    [
        'Quem \xc3\xa9 a m\xc3\xa3e do mingau?',
        'M\xc3\xa3e Zena.'],
    [
        'O que o Batman disse para o Robin na hora em que entraram no carro?',
        'BAT a porta!'],
    [
        'O que \xc3\xa9 um pontinho amarelo tomando sol?',
        '\xc3\x89 um fandango querendo virar baconzito.'],
    [
        'O que \xc3\xa9 um pontinho rosa no arm\xc3\xa1rio?',
        '\xc3\x89 um cupink.'],
    [
        'Quem \xc3\xa9 o tio da constru\xc3\xa7\xc3\xa3o?',
        'Tio Jolo.'],
    [
        'O que d\xc3\xa1 um cruzamento de um d\xc3\xa1lmata com um can\xc3\xa1rio?',
        'Uma on\xc3\xa7a pintada da Amaz\xc3\xb4nia.'],
    [
        'O que \xc3\xa9 uma por\xc3\xa7\xc3\xa3o de letras voando?',
        'Um bando de borboletras.'],
    [
        'O que \xc3\xa9 que viaja o mundo inteiro, mas fica o tempo todo em um canto s\xc3\xb3?',
        'O selo.'],
    [
        'O que \xc3\xa9 um pontinho verde em cima de um amarelo no canto da parede?',
        'Uma ervilha de castigo ajoelhada no milho.'],
    [
        'Por que o namoro da goiabada com o queijo n\xc3\xa3o deu certo?',
        'Porque o queijo era fresco.'],
    [
        'O que \xc3\xa9 um pontinho azul no guarda-roupas?',
        '\xc3\x89 uma bluesa.'],
    [
        'O que \xc3\xa9 um pontinho verde no fundo da piscina?',
        '\xc3\x89 uma ervilha... Segurando a respira\xc3\xa7\xc3\xa3o!'],
    [
        'O que \xc3\xa9 um pontinho vermelho e azul voando de um lado para o outro?',
        'Uma mosca fantasiada de Super-homem.'],
    [
        'Qual \xc3\xa9 o animal que tem mais de tr\xc3\xaas olhos e menos de quatro?',
        'O pi-olho, ou seja, 3,14.'],
    [
        'O que a aranha faz quando vai para a aula de dan\xc3\xa7a?',
        'Sapa-teia.'],
    [
        'Por que o pato tem ci\xc3\xbames do cavalo?',
        'Porque ele tem quatro patas.'],
    [
        'Quando voc\xc3\xaa tem certeza de que um ovo n\xc3\xa3o tem um pintinho dentro?',
        'Quando o ovo \xc3\xa9 de pata.'],
    [
        'Por que ningu\xc3\xa9m apareceu no enterro do elefante?',
        'Porque ningu\xc3\xa9m queria carregar o caix\xc3\xa3o.'],
    [
        'O que \xc3\xa9 que sempre aumenta, mas nunca diminui?',
        'A idade.'],
    [
        'O que \xc3\xa9 que tem muitos p\xc3\xa9s, mas n\xc3\xa3o fica de p\xc3\xa9?',
        'A centop\xc3\xa9ia.'],
    [
        'Em que esp\xc3\xa9cie de mato se senta o elefante quando chove?',
        'Mato molhado.'],
    [
        'Quem \xc3\xa9 que bate em voc\xc3\xaa, mas voc\xc3\xaa n\xc3\xa3o revida?',
        'O vento.'],
    [
        'O que \xc3\xa9 o c\xc3\xbamulo do contra-senso?',
        'Na casa de sa\xc3\xbade, s\xc3\xb3 haver doentes.'],
    [
        'Quando um jogador de futebol \xc3\xa9 um literato?',
        'Quando ele faz um gol de letra.'],
    [
        'Onde \xc3\xa9 que a sereia Ariel v\xc3\xaa filmes?',
        'No cinemar\xc3\xa9.'],
    [
        'O que \xc3\xa9 que atravessa a porta, mas nunca entra nem sai?',
        'A fechadura.'],
    [
        'Por que os rios s\xc3\xa3o considerados pregui\xc3\xa7osos?',
        'Porque n\xc3\xa3o saem dos seus leitos.'],
    [
        'Qual \xc3\xa9 a diferen\xc3\xa7a entre a galinha e o tecido?',
        'A galinha bota e o tecido desbota.'],
    [
        'Era uma vez uma orquestra que n\xc3\xa3o tocava nada. Qual o nome do filme?',
        'Os Intoc\xc3\xa1veis.'],
    [
        'Quando \xc3\xa9 que um ga\xc3\xbacho \xc3\xa9 chamado de mineiro?',
        'Quando trabalha em uma mina.'],
    [
        'O que dever\xc3\xadamos colocar embaixo da forca para que o condenado n\xc3\xa3o morra?',
        'Cedilha!'],
    [
        'O que \xc3\xa9 que todos n\xc3\xb3s temos, mas quando precisamos vamos ao mercado comprar?',
        'Canela!'],
    [
        'O que voc\xc3\xaa faz quando est\xc3\xa1 nadando em um oceano e um crocodilo ataca?',
        'Voc\xc3\xaa acorda.'],
    [
        'Quem \xc3\xa9 que nasce no rio, vive no rio e morre no rio, mas s\xc3\xb3 se molha se quiser?',
        'O carioca.'],
    [
        'O que \xc3\xa9 que est\xc3\xa1 no fim de tudo?',
        'A letra O.'],
    [
        'Qual \xc3\xa9 o \xc3\xbanico monstro que \xc3\xa9 bonzinho?',
        'Good-zila.'],
    [
        'O que \xc3\xa9 a \xc3\xbanica coisa que o vencedor da maratona perde?',
        'O f\xc3\xb4lego.'],
    [
        'O que acontece se voc\xc3\xaa alimentar uma vaca com flores?',
        'Ela dar\xc3\xa1 leite de rosas.'],
    [
        'O que \xc3\xa9 que tem seis olhos, mas n\xc3\xa3o pode ver?',
        'Tr\xc3\xaas ratinhos cegos.'],
    [
        'Afinal, o que \xc3\xa9 que sempre encontramos no final do t\xc3\xbanel?',
        'A letra L.'],
    [
        'Qual a palavra que tem duas letras e tr\xc3\xaas s\xc3\xadlabas?',
        'Arara!'],
    [
        'Por que os elefantes s\xc3\xa3o encontrados na \xc3\x81frica?',
        'Porque eles s\xc3\xa3o muito grandes para se esconderem.'],
    [
        'Onde estavam todos os moradores da cidade durante o \xc3\xbaltimo apag\xc3\xa3o?',
        'No escuro.'],
    [
        'Quando \xc3\xa9 que o cliente fica preso no banco?',
        'Quando fecha a conta-corrente.'],
    [
        'Quem \xc3\xa9 que vai a todos os casamentos sem ser convidado?',
        'O padre.'],
    [
        'Por que os dinossauros t\xc3\xaam pesco\xc3\xa7os longos?',
        'Porque eles t\xc3\xaam chul\xc3\xa9.'],
    [
        'Qual \xc3\xa9 a mulher que sempre aparece antes do nascer do sol?',
        'Aurora.'],
    [
        'Por que os elefantes nunca esquecem?',
        'Porque ningu\xc3\xa9m nunca fala nada para eles.'],
    [
        'Qual \xc3\xa9 o pa\xc3\xads que o criminoso n\xc3\xa3o gosta de visitar?',
        'O Cana-d\xc3\xa1.'],
    [
        'Por que o le\xc3\xa3o \xc3\xa9 considerado o rei das selvas?',
        'Porque ele \xc3\xa9 macho; se fosse f\xc3\xaamea, seria rainha.'],
    [
        "O que \xc3\xa9 um 'fuio'?",
        "\xc3\x89 um 'buiaco na paiede'."],
    [
        'Sou enrolado, tenho a cabe\xc3\xa7a rachada e vivo apertado?',
        'Parafuso.'],
    [
        'Por que o cachorro r\xc3\xb3i o osso?',
        'Porque ele n\xc3\xa3o consegue engolir o osso inteiro.'],
    [
        'Como \xc3\xa9 que voc\xc3\xaa impede um elefante de passar pelo buraco de uma agulha?',
        'Dando um n\xc3\xb3 no rabo dele.'],
    [
        'Em que lugar do mundo, o sono \xc3\xa9 mais profundo?',
        'No cemit\xc3\xa9rio.'],
    [
        'O que \xc3\xa9 que \xc3\xa9 menor que a boca de uma formiga?',
        'O que ela come.'],
    [
        'Um \xc3\xa9 pouco, dois \xc3\xa9 bom, tr\xc3\xaas \xc3\xa9 demais. O que s\xc3\xa3o quatro e cinco?',
        'Nove.'],
    [
        'Qual \xc3\xa9 a corrente que, por mais forte que seja, n\xc3\xa3o consegue segurar o navio?',
        'A corrente marinha.'],
    [
        'O que \xc3\xa9 que tem boca e um s\xc3\xb3 dente e chama a aten\xc3\xa7\xc3\xa3o de muita gente?',
        'O sino.'],
    [
        'Qual deve ser o comprimento m\xc3\xa1ximo de uma perna?',
        'O suficiente para alcan\xc3\xa7ar o ch\xc3\xa3o.'],
    [
        'O que \xc3\xa9 uma mol\xc3\xa9cula?',
        "\xc3\x89 uma 'Meninula Sap\xc3\xa9cula'."],
    [
        'Como se pode escrever a maior palavra do mundo?',
        'Com a caneta.'],
    [
        'Que refei\xc3\xa7\xc3\xa3o \xc3\xa9 colocada sobre a \xc3\xa1gua e n\xc3\xa3o afunda?',
        'A b\xc3\xb3ia.'],
    [
        'Qual o melhor castigo para um time de futebol que joga sujo?',
        'Levar um banho de gols.'],
    [
        'Por que os elefantes usam t\xc3\xaanis de corrida?',
        'Para fazer cooper, \xc3\xa9 claro.'],
    [
        'Por que os elefantes s\xc3\xa3o grandes e cinza?',
        'Porque, se eles fossem pequenos e amarelos, seriam can\xc3\xa1rios.'],
    [
        'O que \xc3\xa9 que tem na \xc3\xa1rvore, no futebol, no chap\xc3\xa9u e na casa?',
        'Copa.'],
    [
        'O que \xc3\xa9 que deixa um cachorro desconfiado?',
        'Uma pulga atr\xc3\xa1s da orelha.'],
    [
        'Por que o ' + Donald + ' espalhou a\xc3\xa7\xc3\xbacar no travesseiro?',
        'Porque ele queria ter doces sonhos.'],
    [
        'Por que o ' + Goofy + ' levou o pente dele ao dentista?',
        'Porque ele perdeu todos os dentes.'],
    [
        'Por que o ' + Goofy + ' usa a camisa no banho?',
        'Porque a etiqueta diz para lavar e usar.'],
    [
        'Qual o pa\xc3\xads est\xc3\xa1 na granja e a capital est\xc3\xa1 no pomar?',
        'Peru, capital Lima.'],
    [
        'Qual \xc3\xa9 o prato preferido da maioria das pessoas?',
        'O prato cheio.'],
    [
        'Como voc\xc3\xaa chama uma pessoa que leva outra para almo\xc3\xa7ar?',
        'Canibal.'],
    [
        'O que \xc3\xa9 um ponto amarelo no canto da sala?',
        '\xc3\x89 milho Santiago.'],
    [
        'O que \xc3\xa9 um ponto preto dentro do tubo de ensaio?',
        'Uma blackt\xc3\xa9ria.'],
    [
        'Por que o ' + Pluto + ' dorme com uma casca de banana?',
        'Para pular da cama cedo.'],
    [
        'Por que o rato usa t\xc3\xaanis marrom?',
        'Porque o branco est\xc3\xa1 lavando.'],
    [
        'O que \xc3\xa9 que a dentadura tem em comum com as estrelas?',
        'Ela sai \xc3\xa0 noite.'],
    [
        'O que \xc3\xa9 um pontinho preto no meio da estrada?',
        '\xc3\x89 um calhamblack.'],
    [
        'Por que o arque\xc3\xb3logo foi \xc3\xa0 fal\xc3\xaancia?',
        'Porque sua carreira estava uma ru\xc3\xadna.'],
    [
        'Como \xc3\xa9 que voc\xc3\xaa ficaria se atravessasse o Atl\xc3\xa2ntico no Titanic?',
        'Ensopado.'],
    [
        'O que \xc3\xa9 um pontinho amarelo no alto de um pr\xc3\xa9dio?',
        'Um milho suicida.'],
    [
        'Por que \xc3\xa9 que o milho suicida quer se suicidar?',
        'Porque o lugar onde ele mora \xc3\xa9 um baga\xc3\xa7o.'],
    [
        'O que \xc3\xa9 um pontinho vermelho l\xc3\xa1 embaixo do pr\xc3\xa9dio onde est\xc3\xa1 o milho suicida?',
        'Um milho bombeiro para salvar o milho suicida...'],
    [
        'Qual a cor mais barulhenta?',
        'A corneta.'],
    [
        'O que \xc3\xa9 que a banana suicida falou?',
        'Macacos me mordam!!!'],
    [
        'Qual o tipo de alimento de que o pol\xc3\xadtico mais gosta?',
        'As massas.'],
    [
        'O que a chamin\xc3\xa9 grande falou para a chamin\xc3\xa9 pequena?',
        'Voc\xc3\xaa \xc3\xa9 muito jovem para fumar.'],
    [
        'O que \xc3\xa9 um pontinho vermelho no p\xc3\xa2ntano?',
        '\xc3\x89 um jacared.'],
    [
        'O que \xc3\xa9 um pontinho azul no gramado?',
        'Uma formiguinha de cal\xc3\xa7a jeans.'],
    [
        'O que \xc3\xa9 um ponto brilhante no gramado?',
        'Uma formiguinha de aparelho nos dentes.'],
    [
        'O que \xc3\xa9 um pontinho marrom na pr\xc3\xa9-hist\xc3\xb3ria?',
        'Um browntossauro.'],
    [
        'Como se chama um dinossauro que nunca se atrasa?',
        'Prontossauro.'],
    [
        'O que \xc3\xa9 um pontinho vermelho num pedacinho de neve?',
        'Uma miniatura da bandeira do Jap\xc3\xa3o.'],
    [
        'O que \xc3\xa9 um pontinho dourado no gramado?',
        '\xc3\x89 uma formiguinha brincando de Jaspion.'],
    [
        'Qual e a comida que liga e desliga ?',
        'O StrogON-OFF.'],
    [
        'Por que o livro de matem\xc3\xa1tica ficou triste?',
        'Porque ele tinha muitos problemas.'],
    [
        'O que o tomate foi fazer no banco?',
        'Foi tirar extrato'],
    [
        'Como se faz para transformar um giz numa cobra?',
        "\xc3\x89 s\xc3\xb3 colocar o giz num copo de \xc3\xa1gua. A\xc3\xad o 'gizb\xc3\xb3ia'"],
    [
        'Qual \xc3\xa9 o c\xc3\xbamulo da rapidez?',
        'Fechar a gaveta, trancar e jogar a chave dentro.'],
    [
        'Qual \xc3\xa9 o c\xc3\xbamulo do ego\xc3\xadsmo?',
        'N\xc3\xa3o vou contar, s\xc3\xb3 eu que sei.'],
    [
        'Qual \xc3\xa9 o c\xc3\xbamulo da revolta?',
        'Morar sozinho, fugir de casa e deixar um bilhete dizendo que n\xc3\xa3o volta mais.'],
    [
        'Qual \xc3\xa9 o c\xc3\xbamulo do exagero?',
        'Passar manteiga no P\xc3\xa3o de A\xc3\xa7\xc3\xbacar.'],
    [
        'Qual \xc3\xa9 o c\xc3\xbamulo do arrependimento do carrasco?',
        'Pois \xc3\xa9, sempre que enforco algu\xc3\xa9m me d\xc3\xa1 um n\xc3\xb3 na garganta...'],
    [
        'Qual \xc3\xa9 o c\xc3\xbamulo da vis\xc3\xa3o?',
        'Derrubar dez faixas-pretas com um golpe de vista.'],
    [
        'Qual \xc3\xa9 o c\xc3\xbamulo da sorte?',
        'Ser atropelado por uma ambul\xc3\xa2ncia.'],
    [
        'Qual \xc3\xa9 o c\xc3\xbamulo da maldade?',
        'Colocar tachinhas na cadeira el\xc3\xa9trica.'],
    [
        'Qual \xc3\xa9 o c\xc3\xbamulo da burrice?',
        'Ser reprovado no exame de fezes.'],
    [
        'Qual \xc3\xa9 o c\xc3\xbamulo da economia?',
        'Usar o papel higi\xc3\xaanico dos dois lados.'],
    [
        'Qual \xc3\xa9 o c\xc3\xbamulo do esquecimento?',
        'Ih! Esqueci!'],
    [
        'Qual \xc3\xa9 o c\xc3\xbamulo da sede?',
        'Tomar um \xc3\xb4nibus.'],
    [
        'O que que faz ABC...Slurp...DEF...Slurp?',
        'Algu\xc3\xa9m tomando sopa de letrinhas.'],
    [
        'O que \xc3\xa9 que \xc3\xa9 verde e fica saltando sem parar em cima do sof\xc3\xa1?',
        'Uma ervilha que saiu do castigo.'],
    [
        'O que \xc3\xa9 que o tomate foi fazer no banco?',
        'Tirar extrato.'],
    [
        'Por que o m\xc3\xa9dico que trabalha \xc3\xa0 noite se veste de verde?',
        'Porque ele est\xc3\xa1 de plant\xc3\xa3o.'],
    [
        'O que \xc3\xa9 que \xc3\xa9 branco com pontinhos pretos e vermelhos?',
        'Um d\xc3\xa1lmata com catapora.'],
    [
        'O que a galinha foi fazer na igreja?',
        'Assistir \xc3\xa0 missa do galo.'],
    [
        'O que \xc3\xa9 o que \xc3\xa9? Cai em p\xc3\xa9 e corre deitado?',
        'N\xc3\xa3o \xc3\xa9 a chuva n\xc3\xa3o! \xc3\x89 uma minhoca de paraquedas.'],
    [
        'Por que \xc3\xa9 que n\xc3\xa3o \xc3\xa9 bom guardar o quibe no freezer?',
        'Porque l\xc3\xa1 dentro ele esfirra.'],
    [
        'O que o advogado do frango foi fazer na delegacia?',
        'Foi soltar a franga'],
    [
        'Por que o galo canta de olhos fechados?',
        'Porque ele j\xc3\xa1 sabe a m\xc3\xbasica de cor.'],
    [
        'Um peixe foi jogado de cima de um pr\xc3\xa9dio de vinte andares. Que peixe era esse?',
        'Um atum, porque quando ele caiu fez: Aaaaaaaaaaaa Tum!'],
    [
        'Como se faz omelete de chocolate?',
        'Com ovos de P\xc3\xa1scoa.'],
    [
        'Para que servem \xc3\xb3culos verdes?',
        'Para verde perto.'],
    [
        'Para que servem \xc3\xb3culos vermelhos?',
        "Para 'vermelhor'."],
    [
        'O que \xc3\xa9 verde por fora e amarela por dentro?',
        'Uma banana disfar\xc3\xa7ada de pepino.'],
    [
        'Qual \xc3\xa9 a parte do carro que se originou no Antigo Egito?',
        'Os fara\xc3\xb3is.'],
    [
        'Como \xc3\xa9 que a bruxa sai na chuva?',
        'De rodo.'],
    [
        'Por que o cachorro entrou na igreja?',
        'Porque ele \xc3\xa9 um c\xc3\xa3o pastor.'],
    [
        'Quem \xc3\xa9 o pai do volante?',
        'O painel.'],
    [
        'Como chamamos uma mulher que visitou uma planta\xc3\xa7\xc3\xa3o de uva?',
        'Vi\xc3\xbava.'],
    [
        'O que o amendoim falou para o elefante?',
        'Nada, o amendoim n\xc3\xa3o fala.'],
    [
        'O que os elefantes falam quando se esbarram?',
        'Mundo pequeno esse, n\xc3\xa9?'],
    [
        'O que o caixa falou para a registradora?',
        'Estou contando com voc\xc3\xaa.'],
    [
        'Por que o caminh\xc3\xa3o de frigor\xc3\xadfico n\xc3\xa3o sobe a ladeira?',
        "Porque 'elingui\xc3\xa7a'."],
    [
        'Qual \xc3\xa9 a comida que liga e desliga?',
        '\xc3\x89 o strogON-OFF.'],
    [
        'O que a vaca foi fazer na Argentina?',
        'Foi ver o Boi nos Ares.'],
    [
        'Qual \xc3\xa9 o peixe mais salgado que existe?',
        'O sal-m\xc3\xa3o.'],
    [
        'O que \xc3\xa9 um c\xc3\xa3o indeciso?',
        "\xc3\x89 um 'c\xc3\xa3o-fuso'."],
    [
        'Sabe por que o italiano n\xc3\xa3o come churrasco?',
        'Porque o macarr\xc3\xa3o n\xc3\xa3o cabe no espeto.'],
    [
        'Qual \xc3\xa9 o c\xc3\xbamulo da rapidez?',
        'Ir ao enterro de um parente e ainda encontr\xc3\xa1-lo vivo.'],
    [
        'Qual \xc3\xa9 o c\xc3\xbamulo do azar?',
        'Ser atropelado por um carro funer\xc3\xa1rio.'],
    [
        'Por que o jacar\xc3\xa9 tomou o cart\xc3\xa3o de cr\xc3\xa9dito do jacarezinho?',
        'Porque o jacarezinho gastou muito e mandou o jacarepagu\xc3\xa1.'],
    [
        'Qual \xc3\xa9 o c\xc3\xbamulo da burrice?',
        'Olhar pelo buraco da fechadura numa porta de vidro.'],
    [
        'Qual \xc3\xa9 o c\xc3\xbamulo da confian\xc3\xa7a?',
        'Jogar par-ou-\xc3\xadmpar pelo telefone?'],
    [
        'Qual \xc3\xa9 o c\xc3\xbamulo da paci\xc3\xaancia?',
        'Esvaziar uma piscina com conta-gotas.'],
    [
        'Qual \xc3\xa9 o c\xc3\xbamulo da trai\xc3\xa7\xc3\xa3o?',
        'Suicidar-se com uma punhalada nas costas.'],
    [
        'O que uma nuvem disse pra outra?',
        "'Nu-vem' n\xc3\xa3o."],
    [
        'Qual \xc3\xa9 o c\xc3\xbamulo da moleza?',
        'Correr sozinho e chegar em segundo.'],
    [
        'Por que o jacar\xc3\xa9 tirou o jacarezinho da escola?',
        "Porque ele 'reptil'."],
    [
        'Qual \xc3\xa9 o fim da picada?',
        'Quando o mosquito vai embora.'],
    [
        'O que o paraquedas disse para o paraquedista?',
        'T\xc3\xb4 contigo e n\xc3\xa3o abro.'],
    [
        'Qual \xc3\xa9 a cor mais barulhenta?',
        'A corneta.'],
    [
        'O que \xc3\xa9 um pontinho amarelo no c\xc3\xa9u?',
        'Um yellowc\xc3\xb3ptero.']]
MovieHealLaughterMisses = ('hmm', 'hehe', 'ah', 'R\xc3\xa1 r\xc3\xa1')
MovieHealLaughterHits1 = ('Ah ah ah', 'Ri, ri, ri', 'R\xc3\xa9, r\xc3\xa9', 'Ah, ah')
MovieHealLaughterHits2 = ('AH HAH HAH!', 'HO HO HO!', 'R\xc3\x81 R\xc3\x81 R\xc3\x81!')
MovieSOSCallHelp = '%s SOCORRO!'
MovieSOSWhisperHelp = '%s precisa de ajuda na batalha!'
MovieSOSObserverHelp = 'SOCORRO!'
MovieNPCSOSGreeting = 'Oi %s! \xc3\x89 uma satisfa\xc3\xa7\xc3\xa3o ajudar voc\xc3\xaa!'
MovieNPCSOSGoodbye = 'Vejo voc\xc3\xaa depois!'
MovieNPCSOSToonsHit = 'Os Toons sempre acertam!'
MovieNPCSOSCogsMiss = 'Os Cogs sempre erram!'
MovieNPCSOSRestockGags = 'Reabastecendo com %s piadas!'
MovieNPCSOSHeal = 'Curar'
MovieNPCSOSTrap = 'Armadilha'
MovieNPCSOSLure = 'Isca'
MovieNPCSOSSound = 'Sonora'
MovieNPCSOSThrow = 'Lan\xc3\xa7amento'
MovieNPCSOSSquirt = 'Esguicho'
MovieNPCSOSDrop = 'Cadente'
MovieNPCSOSAll = 'Todos'
MoviePetSOSTrickFail = 'Suspiro'
MoviePetSOSTrickSucceedBoy = 'Bom garoto!'
MoviePetSOSTrickSucceedGirl = 'Boa menina!'
MovieSuitCancelled = 'CANCELADO\nCANCELADO\nCANCELADO'
RewardPanelToonTasks = 'Tarefas Toon'
RewardPanelItems = 'Itens recuperados'
RewardPanelMissedItems = 'Itens n\xc3\xa3o-recuperados'
RewardPanelQuestLabel = 'Buscar %s'
RewardPanelCongratsStrings = [
    '\xc3\x89 isso a\xc3\xad!',
    'Parab\xc3\xa9ns!',
    'Uau!',
    'Legal!',
    'Caraca!',
    'Toont\xc3\xa1stico!']
RewardPanelNewGag = 'Nova piada %(gagName)s para %(avName)s!'
RewardPanelUberGag = '%(avName)s ganhou a piada %(gagName)s com %(exp)s pontos de experi\xc3\xaancia!'
RewardPanelEndTrack = 'Oba! %(avName)s chegou ao fim da Trilha de Piadas da piada %(gagName)s!'
RewardPanelMeritsMaxed = 'Maximizados'
RewardPanelMeritBarLabels = [
    'Bilhetes azuis',
    'Intima\xc3\xa7\xc3\xb5es',
    'Granas Cog',
    'M\xc3\xa9ritos']
RewardPanelMeritAlert = 'Pronto para a promo\xc3\xa7\xc3\xa3o!'
RewardPanelCogPart = 'Voc\xc3\xaa ganhou uma parte de disfarce de Cog!'
RewardPanelPromotion = '%s prepare-se para a promo\xc3\xa7\xc3\xa3o!'
CheesyEffectDescriptions = [
    ('Toon normal', 'voc\xc3\xaa ficar\xc3\xa1 normal'),
    ('Cabe\xc3\xa7\xc3\xa3o', 'voc\xc3\xaa ficar\xc3\xa1 com uma cabe\xc3\xa7a grande'),
    ('Cabecinha', 'voc\xc3\xaa ficar\xc3\xa1 com uma cabe\xc3\xa7a pequena'),
    ('Pernonas', 'voc\xc3\xaa ficar\xc3\xa1 com pernas grandes'),
    ('Perninhas', 'voc\xc3\xaa ficar\xc3\xa1 com pernas pequenas'),
    ('Toonz\xc3\xa3o', 'voc\xc3\xaa ficar\xc3\xa1 um pouco maior'),
    ('Toonzinho', 'voc\xc3\xaa ficar\xc3\xa1 um pouco menor'),
    ('Quadro reto', 'voc\xc3\xaa ficar\xc3\xa1 em duas dimens\xc3\xb5es'),
    ('Perfil reto', 'voc\xc3\xaa ficar\xc3\xa1 em duas dimens\xc3\xb5es'),
    ('Transparente', 'voc\xc3\xaa ficar\xc3\xa1 transparente'),
    ('Sem cor', 'voc\xc3\xaa ficar\xc3\xa1 sem cor'),
    ('Toon invis\xc3\xadvel', 'voc\xc3\xaa ficar\xc3\xa1 invis\xc3\xadvel')]
CheesyEffectIndefinite = 'At\xc3\xa9 que escolha outro efeito, %(effectName)s%(whileIn)s.'
CheesyEffectMinutes = 'Nos pr\xc3\xb3ximos %(time)s minutos, %(effectName)s%(whileIn)s.'
CheesyEffectHours = 'Nas pr\xc3\xb3ximas %(time)s horas, %(effectName)s%(whileIn)s.'
CheesyEffectDays = 'Nos pr\xc3\xb3ximos %(time)s dias, %(effectName)s%(whileIn)s.'
CheesyEffectWhileYouAreIn = ' enquanto estiver %s'
CheesyEffectExceptIn = ', exceto em %s'
SuitFlunky = 'Puxa-saco'
SuitPencilPusher = 'Rato de Escrit\xc3\xb3rio'
SuitYesman = 'Vaquinha de Pres\xc3\xa9pio'
SuitMicromanager = 'Micro\x4empres\xc3\xa1rio'
SuitDownsizer = 'Fac\xc3\xa3o'
SuitHeadHunter = 'Ca\xc3\xa7a-\x4talentos'
SuitCorporateRaider = 'Aventureiro Corporativo'
SuitTheBigCheese = 'O Rei da Cocada Preta'
SuitColdCaller = 'Rei da Incerta'
SuitTelemarketer = 'Operador de Tele\x4marketing'
SuitNameDropper = 'Dr. Sabe-com-\x4quem-est\xc3\xa1-\x4falando'
SuitGladHander = 'Amigo da On\xc3\xa7a'
SuitMoverShaker = 'Agitador'
SuitTwoFace = 'Duas Caras'
SuitTheMingler = 'Amizade F\xc3\xa1cil'
SuitMrHollywood = 'Dr. Celebridade'
SuitShortChange = 'Farsante'
SuitPennyPincher = 'M\xc3\xa3o de vaca'
SuitTightwad = 'P\xc3\xa3o-duro'
SuitBeanCounter = 'Conta-\x4moedinha'
SuitNumberCruncher = 'Destruidor de N\xc3\xbameros'
SuitMoneyBags = 'Sacos de Dinheiro'
SuitLoanShark = 'Agiota'
SuitRobberBaron = 'Bar\xc3\xa3o Ladr\xc3\xa3o'
SuitBottomFeeder = 'Comensal'
SuitBloodsucker = 'Sanguessuga'
SuitDoubleTalker = 'Duplo Sentido'
SuitAmbulanceChaser = 'Perseguidor de Ambul\xc3\xa2ncias'
SuitBackStabber = 'Golpe Sujo'
SuitSpinDoctor = 'Rela\xc3\xa7\xc3\xb5es P\xc3\xbablicas'
SuitLegalEagle = 'Macaco velho'
SuitBigWig = 'Figur\xc3\xa3o'
SuitFlunkyS = 'um Puxa-saco'
SuitPencilPusherS = 'um Rato de Escrit\xc3\xb3rio'
SuitYesmanS = 'uma Vaquinha de Pres\xc3\xa9pio'
SuitMicromanagerS = 'um Micro\x4empres\xc3\xa1rio'
SuitDownsizerS = 'um Fac\xc3\xa3o'
SuitHeadHunterS = 'um Ca\xc3\xa7a-talentos'
SuitCorporateRaiderS = 'um Aventureiro Corporativo'
SuitTheBigCheeseS = 'um Rei da Cocada Preta'
SuitColdCallerS = 'um Rei da Incerta'
SuitTelemarketerS = 'um Operador de Telemarketing'
SuitNameDropperS = 'um Dr. Sabe-com-\x4quem-est\xc3\xa1-\x4falando'
SuitGladHanderS = 'um Amigo da On\xc3\xa7a'
SuitMoverShakerS = 'um Agitador'
SuitTwoFaceS = 'um Duas Caras'
SuitTheMinglerS = 'um Amizade F\xc3\xa1cil'
SuitMrHollywoodS = 'um Dr. Celebridade'
SuitShortChangeS = 'um Farsante'
SuitPennyPincherS = 'um M\xc3\xa3o de vaca'
SuitTightwadS = 'um P\xc3\xa3o-duro'
SuitBeanCounterS = 'um Conta-\x4moedinha'
SuitNumberCruncherS = 'um Destruidor de N\xc3\xbameros'
SuitMoneyBagsS = 'um Sacos de Dinheiro'
SuitLoanSharkS = 'um Agiota'
SuitRobberBaronS = 'um Bar\xc3\xa3o Ladr\xc3\xa3o'
SuitBottomFeederS = 'um Comensal'
SuitBloodsuckerS = 'um Sanguessuga'
SuitDoubleTalkerS = 'um Duplo Sentido'
SuitAmbulanceChaserS = 'um Perseguidor de Ambul\xc3\xa2ncias'
SuitBackStabberS = 'um Golpe Sujo'
SuitSpinDoctorS = 'um Rela\xc3\xa7\xc3\xb5es P\xc3\xbablicas'
SuitLegalEagleS = 'um Macaco velho'
SuitBigWigS = 'um Figur\xc3\xa3o'
SuitFlunkyP = 'Puxa-sacos'
SuitPencilPusherP = 'Ratos de Escrit\xc3\xb3rio'
SuitYesmanP = 'Vaquinhas de Pres\xc3\xa9pio'
SuitMicromanagerP = 'Micro\x4empres\xc3\xa1rios'
SuitDownsizerP = 'Fac\xc3\xb5es'
SuitHeadHunterP = 'Ca\xc3\xa7a-\x4talentos'
SuitCorporateRaiderP = 'Aventureiros Corporativos'
SuitTheBigCheeseP = 'Os Reis da Cocada Preta'
SuitColdCallerP = 'Reis da Incerta'
SuitTelemarketerP = 'Operadores de Tele\x4marketing'
SuitNameDropperP = 'Drs. Sabe-com-\x4quem-est\xc3\xa1-\x4falando'
SuitGladHanderP = 'Amigos da On\xc3\xa7a'
SuitMoverShakerP = 'Agitadores'
SuitTwoFaceP = 'Duas Caras'
SuitTheMinglerP = 'Amizades F\xc3\xa1ceis'
SuitMrHollywoodP = 'Drs. Celebridade'
SuitShortChangeP = 'Farsantes'
SuitPennyPincherP = 'M\xc3\xa3os de vaca'
SuitTightwadP = 'P\xc3\xa3es-duros'
SuitBeanCounterP = 'Conta-\x4moedinhas'
SuitNumberCruncherP = 'Destruidores de N\xc3\xbameros'
SuitMoneyBagsP = 'Sacos de Dinheiro'
SuitLoanSharkP = 'Agiotas'
SuitRobberBaronP = 'Bar\xc3\xb5es Ladr\xc3\xb5es'
SuitBottomFeederP = 'Comensais'
SuitBloodsuckerP = 'Sanguessugas'
SuitDoubleTalkerP = 'Duplos Sentidos'
SuitAmbulanceChaserP = 'Perseguidores de Ambul\xc3\xa2ncias'
SuitBackStabberP = 'Golpes Sujos'
SuitSpinDoctorP = 'Rela\xc3\xa7\xc3\xb5es P\xc3\xbablicas'
SuitLegalEagleP = 'Macacos velhos'
SuitBigWigP = 'Figur\xc3\xb5es'
SuitFaceoffDefaultTaunts = [
    'Buuuuu!']
SuitAttackDefaultTaunts = [
    'Pega essa!',
    'Pode escrever!']
SuitAttackNames = {
    'Audit': 'Auditoria!',
    'Bite': 'Mordida!',
    'BounceCheck': 'Cheque sem fundos!',
    'BrainStorm': 'Grande ideia!',
    'BuzzWord': 'Palavra-chave!',
    'Calculate': 'Calcular!',
    'Canned': 'Enlatado!',
    'Chomp': 'Nhac!',
    'CigarSmoke': 'Fuma\xc3\xa7a de charuto!',
    'ClipOnTie': 'Prendedor de gravata!',
    'Crunch': 'Triturar!',
    'Demotion': 'Rebaixar!',
    'Downsize': 'Reduzir!',
    'DoubleTalk': 'Duplo sentido!',
    'EvictionNotice': 'Aviso de despejo!',
    'EvilEye': 'Mau-olhado!',
    'Filibuster': 'Enchedor de lingui\xc3\xa7a!',
    'FillWithLead': 'Pelot\xc3\xa3o de frente!',
    'FiveOClockShadow': 'Barba por fazer!',
    'FingerWag': 'Dedo na cara!',
    'Fired': 'Fogo!',
    'FloodTheMarket': 'Invadir o mercado!',
    'FountainPen': 'Caneta-tinteiro!',
    'FreezeAssets': 'Bens congelados!',
    'Gavel': 'Martelo!',
    'GlowerPower': 'Olhar raivoso!',
    'GuiltTrip': 'Sentimento de culpa!',
    'HalfWindsor': 'N\xc3\xb3 franc\xc3\xaas!',
    'HangUp': 'Desligar!',
    'HeadShrink': 'Analista!',
    'HotAir': 'Ar quente!',
    'Jargon': 'Jarg\xc3\xa3o!',
    'Legalese': 'Legal\xc3\xaas!',
    'Liquidate': 'Liquidar!',
    'MarketCrash': 'Queda da Bolsa!',
    'MumboJumbo': 'Bobeira!',
    'ParadigmShift': 'Desvio de paradigma!',
    'PeckingOrder': 'Hierarquia!',
    'PickPocket': 'Pivete!',
    'PinkSlip': 'Bilhete azul!',
    'PlayHardball': 'Jogo duro!',
    'PoundKey': 'Tecla de Jogo da velha!',
    'PowerTie': 'Gravata!',
    'PowerTrip': 'Viajou na autoridade!',
    'Quake': 'Terremoto!',
    'RazzleDazzle': 'Agito!',
    'RedTape': 'Burrocracia!',
    'ReOrg': 'ReOrg!',
    'RestrainingOrder': 'Repress\xc3\xa3o!',
    'Rolodex': 'Agenda telef\xc3\xb4nica!',
    'RubberStamp': 'Carimbo!',
    'RubOut': 'Apagar!',
    'Sacked': 'Ensacado!',
    'SandTrap': 'Trincheira!',
    'Schmooze': 'Bajula!',
    'Shake': 'Tremor!',
    'Shred': 'Retalho!',
    'SongAndDance': 'Conta prosa!',
    'Spin': 'Giro!',
    'Synergy': 'Sinergia!',
    'Tabulate': 'Tabular!',
    'TeeOff': 'Tacada!',
    'ThrowBook': 'Livro de lan\xc3\xa7amentos!',
    'Tremor': 'Tremor!',
    'Watercooler': 'Bebedouro!',
    'Withdrawal': 'Retirada!',
    'WriteOff': 'Baixa!' }
SuitAttackTaunts = {
    'Audit': [
        'Seus livros n\xc3\xa3o t\xc3\xaam balan\xc3\xa7o.',
        'Parece que voc\xc3\xaa est\xc3\xa1 no vermelho.',
        'Deixe-me ajud\xc3\xa1-lo com esses livros.',
        'Sua coluna de d\xc3\xa9bitos \xc3\xa9 muito alta.',
        'Vamos verificar os seus bens.',
        'Assim, voc\xc3\xaa vai ficar endividado.',
        'Vamos conferir direitinho o que voc\xc3\xaa deve.',
        'Assim, a sua conta vai ficar zerada.',
        '\xc3\x89 hora de voc\xc3\xaa se responsabilizar pelas suas despesas.',
        'Encontrei um erro nos seus livros.'],
    'Bite': [
        'Quer uma mordida?',
        'D\xc3\xa1 uma mordida!',
        'A sua mordida \xc3\xa9 maior do que voc\xc3\xaa pode mastigar.',
        'Minha mordida \xc3\xa9 maior do que o meu latido.',
        'Morde logo!',
        'Tome cuidado, eu mordo.',
        'Eu n\xc3\xa3o mordo s\xc3\xb3 quando estou encurralado.',
        'S\xc3\xb3 vou dar uma mordidinha.',
        'N\xc3\xa3o dei uma mordida o dia todo.',
        'S\xc3\xb3 quero uma mordida. \xc3\x89 pedir muito?'],
    'BounceCheck': [
        'Ah, que pena, voc\xc3\xaa n\xc3\xa3o tem gra\xc3\xa7a.',
        'Voc\xc3\xaa tem uma d\xc3\xadvida.',
        'Acho que este cheque \xc3\xa9 seu.',
        'Voc\xc3\xaa me devia isso.',
        'Estou cobrando esta d\xc3\xadvida.',
        'Este cheque n\xc3\xa3o vai ser mole.',
        'Voc\xc3\xaa ser\xc3\xa1 cobrado por isso.',
        'Feche a conta.',
        'Isso ter\xc3\xa1 um custo para voc\xc3\xaa.',
        'Queria trocar por dinheiro.',
        'Vou mandar isso de volta para voc\xc3\xaa.',
        'Esta conta est\xc3\xa1 salgada.',
        'Estou descontando o servi\xc3\xa7o.'],
    'BrainStorm': [
        'Acho que vai chover.',
        'Espero que voc\xc3\xaa esteja com o guarda-chuva.',
        'Quero orientar voc\xc3\xaa.',
        'Que tal uma saraivada b\xc3\xa1sica?',
        'Cad\xc3\xaa o seu brilho agora, Toon?',
        'Pronto para a chuvarada?',
        'Vou atacar voc\xc3\xaa como um furac\xc3\xa3o.',
        'Chamo isso de ataque-rel\xc3\xa2mpago.',
        'Adoro ser um desmancha-prazeres.'],
    'BuzzWord': [
        'Desculpe-me se estou te aborrecendo.',
        'Ouviu a \xc3\xbaltima?',
        'Veja se voc\xc3\xaa pega esta.',
        'Vamos cantarolar, Toon?',
        'Deixe-me defender voc\xc3\xaa.',
        'Vou "C" perfeitamente claro.',
        'Voc\xc3\xaa devia "C" mais cuidadoso.',
        'Veja se voc\xc3\xaa consegue desviar desse enxame.',
        'Cuidado, voc\xc3\xaa est\xc3\xa1 prestes a ser picado.',
        'Parece que a sua urtic\xc3\xa1ria \xc3\xa9 s\xc3\xa9ria.'],
    'Calculate': [
        'Estes n\xc3\xbameros fazem mesmo uma diferen\xc3\xa7a!',
        'Voc\xc3\xaa contou com isso?',
        'Fa\xc3\xa7a as contas, voc\xc3\xaa est\xc3\xa1 caindo.',
        'Deixe-me ajudar voc\xc3\xaa a somar isso.',
        'Voc\xc3\xaa registrou todas as suas despesas?',
        'De acordo com os meus c\xc3\xa1lculos, voc\xc3\xaa n\xc3\xa3o ficar\xc3\xa1 por muito tempo aqui.',
        'Aqui est\xc3\xa1 o total.',
        'Uau, a sua conta est\xc3\xa1 se multiplicando.',
        'Tente brincar com esses n\xc3\xbameros!',
        Cogs + ': 1 Toons: 0'],
    'Canned': [
        'Gosta fora da lata?',
        '"Lata" limpo?',
        'Fresquinho, sa\xc3\xaddo da lata!',
        'J\xc3\xa1 foi atacado alguma vez por enlatados?',
        'Gostaria de doar a voc\xc3\xaa este enlatado!',
        'Prepare-se para o "Vira-lata"!',
        'Voc\xc3\xaa acha que pode abrir a lata, na lata.',
        'Vou te jogar na lata!',
        'Vou transformar voc\xc3\xaa em um a-Toon em lata!',
        'Seu gosto n\xc3\xa3o \xc3\xa9 t\xc3\xa3o bom fora da lata.'],
    'Chomp': [
        'Olha s\xc3\xb3 esses comil\xc3\xb5es!',
        'Nhac, nhac, nhac!',
        'Aqui tem algo para mastigar.',
        'Procurando alguma coisa para mastigar?',
        'Por que voc\xc3\xaa n\xc3\xa3o mastiga um pouco disto?',
        'Eu vou jantar voc\xc3\xaa.',
        'Adoro comer Toons no caf\xc3\xa9 da manh\xc3\xa3!'],
    'ClipOnTie': [
        'Melhor se arrumar para a reuni\xc3\xa3o.',
        'Voc\xc3\xaa n\xc3\xa3o pode SAIR sem a gravata.',
        'Os  ' + Cogs + ' mais bem vestidos usam isto.Experimente este tamanho.',
        'Voc\xc3\xaa devia se vestir para arrasar.',
        'Sem gravata n\xc3\xa3o tem servi\xc3\xa7o...',
        'Precisa de ajuda para se vestir?',
        'Nada \xc3\xa9 t\xc3\xa3o poderoso quanto uma boa gravata.',
        'Vamos ver se serve.',
        'Esta vai apertar voc\xc3\xaa.',
        'Voc\xc3\xaa vai querer se vestir antes de SAIR.',
        'Acho que vou dar uma gravata em voc\xc3\xaa.'],
    'Crunch': [
        'Parece que voc\xc3\xaa est\xc3\xa1 espremido contra a parede.',
        'Hora de mexer a mand\xc3\xadbula!',
        'Vou dar alguma coisa para voc\xc3\xaa mascar!',
        'Triture isso!',
        'Mordida para viagem.',
        'Qual voc\xc3\xaa prefere, molinho ou crocante?',
        'Espero que esteja preparado para a hora da mand\xc3\xadbula.',
        'Parece que voc\xc3\xaa est\xc3\xa1 ficando amassadinho!',
        'Vou amassar voc\xc3\xaa como uma latinha.'],
    'Demotion': [
        'Voc\xc3\xaa est\xc3\xa1 descendo os degraus da empresa.',
        'Vou mandar voc\xc3\xaa de volta para a Expedi\xc3\xa7\xc3\xa3o.',
        'Est\xc3\xa1 na hora de virar a sua placa de identifica\xc3\xa7\xc3\xa3o.',
        'Voc\xc3\xaa est\xc3\xa1 caida\xc3\xa7o, palha\xc3\xa7o.',
        'Parece que voc\xc3\xaa est\xc3\xa1 ferrado.',
        'Voc\xc3\xaa n\xc3\xa3o vai a lugar nenhum.',
        'Voc\xc3\xaa est\xc3\xa1 em um beco sem sa\xc3\xadda.',
        'Voc\xc3\xaa n\xc3\xa3o vai se mover t\xc3\xa3o cedo.',
        'Voc\xc3\xaa n\xc3\xa3o vai a lugar nenhum.',
        'Vai ficar registrado em seu arquivo permanente.'],
    'Downsize': [
        'Desce!',
        'Sabe como descer?',
        'Vamos entrar direto no assunto.',
        'O que houve? Voc\xc3\xaa parece deprimido.',
        'Decaindo?',
        'O que \xc3\xa9 que est\xc3\xa1 caindo? Voc\xc3\xaa!',
        'Por que n\xc3\xa3o tem algu\xc3\xa9m do meu tamanho?',
        'Por que eu n\xc3\xa3o me\xc3\xa7o voc\xc3\xaa - ou ser\xc3\xa1 que \xc3\xa9 melhor dizer despe\xc3\xa7o?',
        'Quer um tamanho menor por apenas mais uma moeda?',
        'Experimente este tamanho!',
        'Tem em um tamanho menor.',
        'Este ataque \xc3\xa9 tamanho \xc3\xbanico!'],
    'EvictionNotice': [
        'Mudan\xc3\xa7a \xc3\xa0 vista.',
        'Arrume as malas, Toon.',
        '\xc3\x89 hora de arrumar outro lugar para morar.',
        'Considere-se servido.',
        'O seu aluguel est\xc3\xa1 atrasado.',
        'Isto vai te torpedear.',
        'Voc\xc3\xaa est\xc3\xa1 prestes a ser despejado.',
        'Vou espirrar voc\xc3\xaa daqui.',
        'Voc\xc3\xaa est\xc3\xa1 deslocado.',
        'Prepare-se para ser realocado.',
        'Voc\xc3\xaa est\xc3\xa1 abrigado.'],
    'EvilEye': [
        'Estou botando um mau-olhado em voc\xc3\xaa.',
        'Voc\xc3\xaa fica de olho vivo nisso para mim?',
        'Espere. Tem alguma coisa no meu olho.',
        'Estou de olho em voc\xc3\xaa!',
        'Voc\xc3\xaa pode botar o olho nisso aqui para mim?',
        'Tenho um olho gordo danado.',
        'Voc\xc3\xaa vai levar um soco no olho!',
        'Minha crueldade n\xc3\xa3o est\xc3\xa1 de molho, abre o olho!',
        'Vou colocar voc\xc3\xaa no olho do furac\xc3\xa3o!',
        'Estou dando com os olhos em voc\xc3\xaa.'],
    'Filibuster': [
        'Devo encher?',
        'Isso vai demorar um pouco.',
        'Poderia fazer isso o dia todo.',
        'N\xc3\xa3o preciso nem respirar fundo.',
        'Vou fazendo, fazendo, fazendo...',
        'Nunca fica cansado de fazer isso.',
        'Posso tagarelar sem parar.',
        'Tem problema se eu puxar a sua orelha?',
        'Acho que vou papear \xc3\xa0 vontade.',
        'Sempre consigo dar o meu recado.'],
    'FingerWag': [
        'J\xc3\xa1 te disse milhares de vezes.',
        'Olha aqui, Toon.',
        'N\xc3\xa3o me fa\xc3\xa7a rir.',
        'N\xc3\xa3o me fa\xc3\xa7a ir at\xc3\xa9 a\xc3\xad.',
        'J\xc3\xa1 cansei de repetir.',
        'Fim de papo, eu j\xc3\xa1 falei.',
        '\\Voc\xc3\xaa n\xc3\xa3o tem respeito por n\xc3\xb3s,  ' + Cogs + '.Acho que est\xc3\xa1 na hora de voc\xc3\xaa prestar aten\xc3\xa7\xc3\xa3o.',
        'Bl\xc3\xa1, Bl\xc3\xa1, Bl\xc3\xa1, Bl\xc3\xa1, Bl\xc3\xa1.',
        'N\xc3\xa3o me obrigue a interromper a reuni\xc3\xa3o.',
        'Ser\xc3\xa1 que eu vou ter que separar voc\xc3\xaas?',
        'J\xc3\xa1 passamos por isto antes.'],
    'Fired': [
        '\xc3\x89 fogo! O jeito \xc3\xa9 fazer um churrasquinho.',
        'Vai esquentar por aqui.',
        'Assim, o frio passa.',
        'Espero que voc\xc3\xaa tenha sangue frio.',
        'Quente, quent\xc3\xa3o e pelando.',
        'Melhor parar tudo, deitar no ch\xc3\xa3o e rolar!',
        'Voc\xc3\xaa est\xc3\xa1 fora daqui.',
        'O que voc\xc3\xaa acha de "bem-feito"?',
        'Pode dizer a\xc3\xad?',
        'Espero que tenha usado protetor solar.',
        'Est\xc3\xa1 se sentindo um pouco tostado?',
        'Voc\xc3\xaa vai arder em chamas.',
        'Voc\xc3\xaa vai ficar aceso que nem fogueira.',
        'Voc\xc3\xaa est\xc3\xa1 frito.',
        'Eu sou fogo na roupa.',
        'S\xc3\xb3 aticei o fogo um pouquinho, n\xc3\xa9?',
        'Olha, um churrasquinho crocante.',
        'Voc\xc3\xaa n\xc3\xa3o devia sair por a\xc3\xad malpassado.'],
    'FountainPen': [
        'Vai deixar mancha.',
        'Vamos assinar embaixo.',
        'Esteja preparado para alguns danos irrepar\xc3\xa1veis.',
        'Voc\xc3\xaa vai precisar de um bom tintureiro.',
        'Voc\xc3\xaa devia mudar.',
        'Esta caneta-tinteiro tem uma tinta legal.',
        'Aqui, vou usar a minha caneta.',
        'Voc\xc3\xaa entende a minha letra?',
        'Isso \xc3\xa9 que \xc3\xa9 carregar nas tintas.',
        'Seu desempenho babou.',
        'N\xc3\xa3o \xc3\xa9 chato quando isso acontece?'],
    'FreezeAssets': [
        'Seus bens s\xc3\xa3o meus.',
        'Est\xc3\xa1 sentindo um vento? \xc3\x89 o cheque voador.',
        'Espero que n\xc3\xa3o tenha planos.',
        'Isso vai manter voc\xc3\xaa na geladeira.',
        'Tem uma brisa fria no ar.',
        'O inverno est\xc3\xa1 chegando mais cedo neste ano.',
        'Voc\xc3\xaa est\xc3\xa1 sentido um calafrio?',
        'Vou cristalizar o meu plano.',
        'Voc\xc3\xaa vai ver, no duro.',
        'O gelo queima.',
        'Espero que goste de frios.',
        'Tenho muito sangue frio.'],
    'GlowerPower': [
        'Est\xc3\xa1 olhando para mim?',
        'Disseram que tenho olhos muito penetrantes.',
        'Gosto de estar no fio da navalha.',
        'Ca\xc3\xa7amba, caramba, meus quatro-olhos n\xc3\xa3o s\xc3\xa3o bambas?',
        'Estou de olho em voc\xc3\xaa, pirralho.',
        'Que tal estes olhos expressivos?',
        'Meus olhos s\xc3\xa3o o meu forte.',
        'Enche os olhos.',
        'Estou de olho, piolho.',
        'Olhe nos meus olhos...',
        'Podemos dar uma espiada no seu futuro?'],
    'GuiltTrip': [
        'Voc\xc3\xaa vai ficar com um baita sentimento de culpa!',
        'Est\xc3\xa1 se sentindo culpado?',
        '\xc3\x89 tudo culpa sua!',
        'Sempre ponho a culpa de tudo em voc\xc3\xaa.',
        'Afogue-se na pr\xc3\xb3pria culpa!',
        'Nunca mais falo contigo!',
        '\xc3\x89 melhor pedir desculpas.',
        'S\xc3\xb3 vou perdoar voc\xc3\xaa daqui a um milh\xc3\xa3o de anos!',
        'Est\xc3\xa1 preparado para viajar na maionese da culpa?',
        'Ligue para mim quando voltar de viagem.',
        'Quando voc\xc3\xaa volta de viagem?'],
    'HalfWindsor': [
        'Esta \xc3\xa9 a gravata mais elegante que voc\xc3\xaa j\xc3\xa1 viu!',
        'Procure n\xc3\xa3o apertar tanto.',
        'Voc\xc3\xaa n\xc3\xa3o viu nem metade do n\xc3\xb3 em que voc\xc3\xaa se meteu.',
        'Voc\xc3\xaa tem sorte de eu n\xc3\xa3o saber franc\xc3\xaas.',
        'Esta gravata \xc3\xa9 demais para voc\xc3\xaa.',
        'Aposto como voc\xc3\xaa nunca VIU um n\xc3\xb3 franc\xc3\xaas!',
        'Esta gravata n\xc3\xa3o \xc3\xa9 para o seu bico.',
        'Eu n\xc3\xa3o deveria ter gasto esta gravata com voc\xc3\xaa.',
        'Voc\xc3\xaa n\xc3\xa3o vale nem o n\xc3\xb3 desta gravata!'],
    'HangUp': [
        'Voc\xc3\xaa foi desconectado.',
        'Tchau!',
        'Est\xc3\xa1 na hora de terminar a sua conex\xc3\xa3o.',
        '...e n\xc3\xa3o ligue de novo!',
        'Clique!',
        'A conversa acabou.',
        'Estou cortando este fio.',
        'Acho que voc\xc3\xaa est\xc3\xa1 meio desligado.',
        'Parece que voc\xc3\xaa est\xc3\xa1 com mau contato.',
        'Seu tempo acabou.',
        'Espero que tenha ouvido em claro e bom som.',
        'Foi engano.'],
    'HeadShrink': [
        'Parece que voc\xc3\xaa tem ido ao analista.',
        'Querida, encolhi o analista.',
        'Espero que n\xc3\xa3o precise analisar o seu amor-pr\xc3\xb3prio.',
        'Voc\xc3\xaa se abriu?',
        'Analiso, logo existo.',
        'N\xc3\xa3o \xc3\xa9 nada que fa\xc3\xa7a voc\xc3\xaa perder a cabe\xc3\xa7a.',
        'Voc\xc3\xaa vai abrir a cabe\xc3\xa7a?',
        'Levanta essa cabe\xc3\xa7a! Ou ser\xc3\xa1 que \xc3\xa9 melhor abaixar?',
        'Os objetos podem ser maiores do que parecem.',
        'Os melhores Toons v\xc3\xaam nos menores frascos.'],
    'HotAir': [
        'Estamos tendo uma discuss\xc3\xa3o acalorada.',
        'Est\xc3\xa1 rolando uma onda de calor.',
        'Atingi o meu ponto de ebuli\xc3\xa7\xc3\xa3o.',
        'Que vento cortante.',
        'Odeio ter que te grelhar, mas...',
        'Lembre-se sempre: onde h\xc3\xa1 fuma\xc3\xa7a, h\xc3\xa1 fogo.',
        'Voc\xc3\xaa parece meio queimadinho.',
        'Outra reuni\xc3\xa3o que virou fuma\xc3\xa7a.',
        'Acho que est\xc3\xa1 na hora de botar lenha na fogueira.',
        'Deixe-me acender uma rela\xc3\xa7\xc3\xa3o de trabalho.',
        'Tenho umas observa\xc3\xa7\xc3\xb5es inflamadas pra voc\xc3\xaa.',
        'Ataque a\xc3\xa9reo!!!'],
    'Jargon': [
        'Que besteira.',
        'Veja se voc\xc3\xaa consegue ver algum sentido nisso.',
        'Espero que tenha sido claro como \xc3\xa1gua.',
        'Parece que vou ter que falar mais alto.',
        'Insisto em ter a palavra.',
        'Sou muito direto.',
        'Devo sustentar a minha opini\xc3\xa3o neste assunto.',
        'Olha, as palavras podem machucar voc\xc3\xaa.',
        'Entendeu o que eu quis dizer?',
        'Palavras, palavras, palavras, palavras, palavras.'],
    'Legalese': [
        'Voc\xc3\xaa deve se conformar e desistir.',
        'Voc\xc3\xaa vai ser derrotado, legalmente falando.',
        'Voc\xc3\xaa est\xc3\xa1 ciente das implica\xc3\xa7\xc3\xb5es legais?',
        'Voc\xc3\xaa n\xc3\xa3o est\xc3\xa1 acima da lei!',
        'Devia haver uma lei contra voc\xc3\xaa.',
        'N\xc3\xa3o h\xc3\xa1 lei marcial comigo!',
        'As opini\xc3\xb5es expressadas neste ataque n\xc3\xa3o s\xc3\xa3o compartilhadas pela Toontown On-line da Disney.',
        'N\xc3\xa3o podemos ser responsabilizados por danos sofridos neste ataque.',
        'Os resultados deste ataque podem variar.',
        'Este ataque n\xc3\xa3o tem validade legal quando proibido.',
        'Voc\xc3\xaa n\xc3\xa3o se enquadra no meu sistema legal!',
        'Voc\xc3\xaa n\xc3\xa3o sabe lidar com assuntos jur\xc3\xaddicos.'],
    'Liquidate': [
        'Gosto de manter as coisas fluindo.',
        'Voc\xc3\xaa est\xc3\xa1 com algum problema de fluxo de caixa?',
        'Vou ter que lavar os seus bens.',
        '\xc3\x89 hora de voc\xc3\xaa ser levado pelo fluxo.',
        'N\xc3\xa3o se esque\xc3\xa7a de que fica escorregadio quando est\xc3\xa1 molhado.',
        'Os n\xc3\xbameros est\xc3\xa3o correndo.',
        'Voc\xc3\xaa escorrega que nem sab\xc3\xa3o.',
        'Est\xc3\xa1 caindo tudo em cima de voc\xc3\xaa.',
        'Acho que voc\xc3\xaa vai por ralo abaixo.',
        'Voc\xc3\xaa tomou uma lavada.'],
    'MarketCrash': [
        'Vou acabar com a sua festa.',
        'Voc\xc3\xaa n\xc3\xa3o vai sobreviver \xc3\xa0 queda.',
        'Sou mais do que o mercado pode aguentar.',
        'Tenho uma queda por voc\xc3\xaa!',
        'Agora eu vou entrar detonando.',
        'Sou um verdadeiro drag\xc3\xa3o no mercado.',
        'Parece que o mercado est\xc3\xa1 em baixa.',
        '\xc3\x89 melhor voc\xc3\xaa sair fora rapidamente!',
        'Vender! Vender! Vender!',
        'Devo liderar a recess\xc3\xa3o?',
        'Todo mundo est\xc3\xa1 saindo fora, voc\xc3\xaa n\xc3\xa3o vai?'],
    'MumboJumbo': [
        'Deixe-me explicar melhor.',
        '\xc3\x89 muito simples.',
        'Vamos fazer desta maneira.',
        'Deixe-me ampliar para voc\xc3\xaa.',
        'Voc\xc3\xaa pode chamar isso de baboseira tecnol\xc3\xb3gica.',
        'Aqui est\xc3\xa3o meus eufemismos.',
        'Caramba, isso \xc3\xa9 que \xc3\xa9 encher a boca.',
        'Algumas pessoas me chamam de exagerado.',
        'Posso me meter?',
        'Acho que estas s\xc3\xa3o as palavras certas.'],
    'ParadigmShift': [
        'Cuidado! Eu saio pela tangente.',
        'Prepare-se para mudar radicalmente!N\xc3\xa3o \xc3\xa9 uma mudan\xc3\xa7a interessante?Voc\xc3\xaa vai ter que desviar de caminho.',
        'Agora \xc3\xa9 sua vez de desviar.',
        'Acabou o desvio!',
        'Voc\xc3\xaa nunca trabalhou tanto neste desvio.',
        'Estou transviando voc\xc3\xaa!',
        'Olhe para o meu rabo de olho!'],
    'PeckingOrder': [
        'Este aqui \xc3\xa9 para quem berra mais.',
        'Prepare-se para o grito de guerra.',
        'Por falta de um grito, morre um burro no atoleiro.',
        'Vou ganhar no grito.',
        'Voc\xc3\xaa est\xc3\xa1 no \xc3\xbaltimo grito da hierarquia.',
        'Se gritos resolvessem, porcos n\xc3\xa3o morreriam!',
        'A ordem est\xc3\xa1 valendo, no grito!',
        'Por que n\xc3\xa3o grito com algu\xc3\xa9m do meu tamanho? Ah!',
        'C\xc3\xa3o que ladra n\xc3\xa3o morde.'],
    'PickPocket': [
        'Deixe-me verificar os seus pertences.',
        'E a\xc3\xad, qual \xc3\xa9 o p\xc3\xb3?',
        '\xc3\x89 mais f\xc3\xa1cil do que tirar doce de crian\xc3\xa7a.',
        'Golpe de mestre.',
        'Deixa que eu seguro para voc\xc3\xaa.',
        'N\xc3\xa3o tire os olhos de minhas m\xc3\xa3os.',
        'As m\xc3\xa3os s\xc3\xa3o mais r\xc3\xa1pidas que os olhos.',
        'N\xc3\xa3o tenho nada para tirar da manga.',
        'A ger\xc3\xaancia n\xc3\xa3o se responsabiliza por extravio de itens.',
        'Achado n\xc3\xa3o \xc3\xa9 roubado.',
        'Voc\xc3\xaa nem vai sentir.',
        'Dois pra mim, um pra voc\xc3\xaa.',
        'Est\xc3\xa1 bom assim.',
        'Voc\xc3\xaa n\xc3\xa3o vai precisar mesmo...'],
    'PinkSlip': [
        'Tente imaginar que est\xc3\xa1 tudo azul.',
        'T\xc3\xa1 com medo? Voc\xc3\xaa est\xc3\xa1 azul!',
        'Com certeza, este bilhete vai fazer voc\xc3\xaa ficar azul.',
        '\xc3\x8apa, acho que mudei de cor, n\xc3\xa9?',
        'Olha l\xc3\xa1, voc\xc3\xaa n\xc3\xa3o quer ficar azul, ou quer?',
        'Este bilhete n\xc3\xa3o \xc3\xa9 branco, \xc3\xa9 azul.',
        'Estou azul de fome!',
        'Voc\xc3\xaa se importa que eu passe a\xc3\xad para ver se est\xc3\xa1 tudo azul?',
        'O azul n\xc3\xa3o \xc3\xa9 exatamente a sua cor.',
        'Toma seu bilhete azul e fora daqui!'],
    'PlayHardball': [
        'Ent\xc3\xa3o voc\xc3\xaa quer jogar bola comigo?',
        'Voc\xc3\xaa n\xc3\xa3o quer jogar bola comigo.',
        'Chuta forte!',
        'Passa, cara, passa!',
        'A\xc3\xad est\xc3\xa1 o passe...',
        'Voc\xc3\xaa vai precisar de um refresco do goleiro.',
        'Vou jogar voc\xc3\xaa para fora do campo.',
        'Depois que voc\xc3\xaa se contundir, vai direto para casa.',
        'S\xc3\xa3o 45 minutos do segundo tempo!',
        'Voc\xc3\xaa n\xc3\xa3o consegue jogar comigo!',
        'Vou atingir voc\xc3\xaa.',
        'Vou dar um chute com efeito na bola!'],
    'PoundKey': [
        '\xc3\x89 hora de retornar algumas liga\xc3\xa7\xc3\xb5es.',
        'Gostaria de fazer uma liga\xc3\xa7\xc3\xa3o a cobrar.',
        'Trrriiimmm - \xc3\xa9 para voc\xc3\xaa!',
        'Voc\xc3\xaa quer brincar com o Jogo da Velha?',
        'Tenho um m\xc3\xa9todo incr\xc3\xadvel para ganhar.',
        'Est\xc3\xa1 se sentindo nocauteado?',
        'Vou dar um golpe neste n\xc3\xbamero.',
        'Deixe-me ligar para fazer uma surpresinha.',
        'Vou ligar para voc\xc3\xaa.',
        'O.K. Toon, \xc3\xa9 o fim para voc\xc3\xaa.'],
    'PowerTie': [
        'Eu ligo mais tarde, voc\xc3\xaa parece enrolado na gravata.',
        'Voc\xc3\xaa est\xc3\xa1 pronto para uma gravata?',
        'Senhoras e senhores, esta \xc3\xa9 a gravata!',
        '\xc3\x89 melhor aprender a dar este n\xc3\xb3.',
        'Vou manter a sua l\xc3\xadngua dentro do n\xc3\xb3!',
        '\xc3\x89 a gravata mais horr\xc3\xadvel que voc\xc3\xaa j\xc3\xa1 comprou!',
        'Est\xc3\xa1 sentindo o aperto?',
        'Minha gravata \xc3\xa9 muito mais poderosa que a sua!',
        'Eu tenho o poder do n\xc3\xb3!',
        'Pelos poderes do n\xc3\xb3, vou engravatar voc\xc3\xaa.'],
    'PowerTrip': [
        'Fa\xc3\xa7a as malas, vamos fazer uma pequena viagem.',
        'Voc\xc3\xaa fez uma boa viagem?',
        'Boa viagem, acho que nos veremos na pr\xc3\xb3xima temporada.',
        'Como foi a viagem?',
        'Desculpe ter "viajado" dessa maneira!',
        'Voc\xc3\xaa parece viajand\xc3\xa3o.',
        'Agora, voc\xc3\xaa sabe quem \xc3\xa9 a autoridade!',
        'Tenho muito mais autoridade do que voc\xc3\xaa.',
        'Quem manda agora?',
        'Voc\xc3\xaa n\xc3\xa3o pode lutar contra o poder.',
        'O poder corrompe, principalmente em minhas m\xc3\xa3os!'],
    'Quake': [
        'Vamos balan\xc3\xa7ar, agitar e rolar.',
        'Tem muita vibra\xc3\xa7\xc3\xa3o por aqui!',
        'As suas canelas est\xc3\xa3o tremendo.',
        'A\xc3\xad vem ele, este \xc3\xa9 grande!',
        'Este est\xc3\xa1 fora da escala Richter.',
        'Agora \xc3\xa9 que a terra vai tremer!',
        'E a\xc3\xad, quem \xc3\xa9 que est\xc3\xa1 agitando? Voc\xc3\xaa!',
        'J\xc3\xa1 esteve em um terremoto?',
        'Agora, voc\xc3\xaa est\xc3\xa1 em territ\xc3\xb3rio de tremores!'],
    'RazzleDazzle': [
        'Leia os meus l\xc3\xa1bios.',
        'Que acha da minha dentadura?',
        'N\xc3\xa3o acha que tenho charme?',
        'Vou impressionar voc\xc3\xaa.',
        'Meu dentista faz um excelente trabalho.',
        'Cegadores, n\xc3\xa3o acha?',
        'N\xc3\xa3o d\xc3\xa1 nem para acreditar que n\xc3\xa3o \xc3\xa9 de verdade.',
        'Chocante, n\xc3\xa9?',
        'Vou dar um fim nisso.',
        'Passo o fio dental ap\xc3\xb3s cada refei\xc3\xa7\xc3\xa3o.',
        'Sorria!'],
    'RedTape': [
        'Isto deve acalmar o bicho.',
        'Vou te amarrar por um tempo.',
        'Voc\xc3\xaa est\xc3\xa1 acorrentado.',
        'Veja se consegue cortar caminho por aqui.',
        'O bicho vai pegar.',
        'Tomara que voc\xc3\xaa tenha claustrofobia.',
        'Vou me certificar de que voc\xc3\xaa n\xc3\xa3o vai escapulir.',
        'Vou ocupar voc\xc3\xaa com alguma coisa.',
        'Tente desatar o n\xc3\xb3.',
        'Espero que voc\xc3\xaa concorde com os t\xc3\xb3picos da reuni\xc3\xa3o.'],
    'ReOrg': [
        'Voc\xc3\xaa n\xc3\xa3o gostou da maneira como eu reorganizei as coisas!',
        'Talvez um pouco de organiza\xc3\xa7\xc3\xa3o seja bom.',
        'Voc\xc3\xaa n\xc3\xa3o \xc3\xa9 t\xc3\xa3o ruim assim, s\xc3\xb3 precisa se organizar.',
        'Voc\xc3\xaa gosta do meu tino para organiza\xc3\xa7\xc3\xa3o?',
        'S\xc3\xb3 pensei em dar um novo visual \xc3\xa0s coisas.',
        'Voc\xc3\xaa precisa se organizar!',
        'Voc\xc3\xaa parece um pouco desorganizado.',
        'Espera um pouco enquanto eu reorganizo os seus pensamentos.',
        'S\xc3\xb3 vou esperar at\xc3\xa9 que voc\xc3\xaa se organize um pouco mais.',
        'Voc\xc3\xaa se importa se eu s\xc3\xb3 der uma reorganizadinha?'],
    'RestrainingOrder': [
        'Voc\xc3\xaa precisa levar broncas de vez em quando.',
        'Estou te jogando na cara uma ordem repressora!',
        'Voc\xc3\xaa n\xc3\xa3o pode chegar nem um metro e meio perto de mim.',
        'Talvez seja melhor voc\xc3\xaa manter dist\xc3\xa2ncia.',
        'Entre na linha.',
        Cogs + '! Reprimam este Toon!',
        'Tente entrar na linha sozinho.',
        'Espero que eu esteja sendo bem repressor com voc\xc3\xaa.',
        'Veja se voc\xc3\xaa consegue acabar com essa repress\xc3\xa3o!',
        'Estou ordenando que voc\xc3\xaa se reprima!',
        'Por que n\xc3\xa3o come\xc3\xa7amos com uma repress\xc3\xa3o b\xc3\xa1sica?'],
    'Rolodex': [
        'O seu cart\xc3\xa3o est\xc3\xa1 aqui, em algum lugar.',
        'Aqui est\xc3\xa1 o n\xc3\xbamero do dedetizador.',
        'Quero dar o meu cart\xc3\xa3o a voc\xc3\xaa.',
        'Tenho o seu n\xc3\xbamero bem aqui.',
        'Tenho tudo aqui sobre voc\xc3\xaa, de A a Z.',
        'Voc\xc3\xaa vai se virar com isso.',
        'D\xc3\xaa um giro pelas p\xc3\xa1ginas.',
        'Cuidado com a papelada solta.',
        'Vou apontar o dedo para a letra que desejo.',
        '\xc3\x89 assim que eu consigo entrar em contato com voc\xc3\xaa?',
        'Quero ter certeza de que manteremos o contato.'],
    'RubberStamp': [
        'Eu sempre causo uma boa impress\xc3\xa3o.',
        '\xc3\x89 importante aplicar uma press\xc3\xa3o firme e bem distribu\xc3\xadda.',
        'Impressos perfeitos todas as vezes.',
        'Quero carimbar voc\xc3\xaa.',
        'Voc\xc3\xaa precisa ser DEVOLVIDO AO REMETENTE.',
        'Voc\xc3\xaa foi CANCELADO.',
        'Voc\xc3\xaa possui uma entrega de PRIORIDADE.',
        'Vou me certificar de que a minha mensagem foi RECEBIDA.',
        'Voc\xc3\xaa n\xc3\xa3o vai a lugar nenhum - voc\xc3\xaa tem uma TARIFA POSTAL A PAGAR.',
        'Preciso de uma resposta IMEDIATA.'],
    'RubOut': [
        'E agora, desapareceu!',
        'Sinto que perdi voc\xc3\xaa em algum lugar.',
        'Decidi deixar voc\xc3\xaa de fora.',
        'Eu sempre apago todos os obst\xc3\xa1culos.',
        'Vou s\xc3\xb3 apagar este erro.',
        'Posso fazer qualquer perturba\xc3\xa7\xc3\xa3o desaparecer.',
        'Gosto das coisas organizadas e limpas.',
        'Tente manter a anima\xc3\xa7\xc3\xa3o.',
        'Estou vendo voc\xc3\xaa... Agora, n\xc3\xa3o vejo voc\xc3\xaa.',
        'Vai ficar meio esmaecido.',
        'Vou eliminar o problema.',
        'Deixe-me cuidar das suas \xc3\xa1reas problem\xc3\xa1ticas.'],
    'Sacked': [
        'Parece que voc\xc3\xaa foi embrulhado.',
        'Est\xc3\xa1 no saco.',
        'Voc\xc3\xaa foi embolsado.',
        'Papel ou pl\xc3\xa1stico?',
        'Meus inimigos ser\xc3\xa3o ensacados!',
        'Eu tenho o recorde de Toontown de sacos por jogo.',
        'Voc\xc3\xaa n\xc3\xa3o \xc3\xa9 mais bem-vindo por aqui.',
        'O seu tempo acabou aqui, voc\xc3\xaa vai ser ensacado!',
        'Deixe-me ensacar isto para voc\xc3\xaa.',
        'Nenhuma defesa se iguala ao meu ataque com sacos!'],
    'Schmooze': [
        'Voc\xc3\xaa nunca vai ver quando chega.',
        'Vai ficar legal em voc\xc3\xaa.',
        'Voc\xc3\xaa conseguiu.',
        'N\xc3\xa3o quero despejar nada em voc\xc3\xaa.',
        'Como puxa-saco, eu vou longe.',
        'Agora, eu vou florear bastante.',
        '\xc3\x89 hora de carregar nas tintas.',
        'Vou ressaltar o seu lado bom.',
        'Isso merece um bom tapinha nas costas.',
        'Vou falar bem de voc\xc3\xaa para todo mundo.',
        'Detesto tir\xc3\xa1-lo do seu pedestal, mas...'],
    'Shake': [
        'Voc\xc3\xaa est\xc3\xa1 bem no epicentro.',
        'Voc\xc3\xaa est\xc3\xa1 em cima da falha.',
        'Vai ser um sacolejo s\xc3\xb3.',
        'Acho que isso \xc3\xa9 um desastre natural.',
        '\xc3\x89 um desastre de propor\xc3\xa7\xc3\xb5es s\xc3\xadsmicas.',
        'Este est\xc3\xa1 fora da escala Richter.',
        '\xc3\x89 hora de entrar na toca.',
        'Voc\xc3\xaa parece perturbado.',
        'Preparado para os solavancos?',
        'Voc\xc3\xaa vai sacolejar, e n\xc3\xa3o centrifugar.',
        'Isso vai agitar voc\xc3\xaa.',
        'Sugiro um bom plano de fuga.'],
    'Shred': [
        'Preciso me livrar de alguns fragmentos perigosos.',
        'As por\xc3\xa7\xc3\xb5es produzidas est\xc3\xa3o aumentando de quantidade.',
        'Acho que vou dispor de voc\xc3\xaa agora mesmo.',
        'Assim, a prova \xc3\xa9 eliminada.',
        'N\xc3\xa3o h\xc3\xa1 como provar isso agora.',
        'Veja se voc\xc3\xaa consegue juntar os peda\xc3\xa7os novamente.',
        'Assim, voc\xc3\xaa vai cortar as sobras e ficar do tamanho certo.',
        'Vou retalhar esta ideia todinha.',
        'N\xc3\xa3o queremos que isto caia nas m\xc3\xa3os erradas.',
        'F\xc3\xa1cil se tem, f\xc3\xa1cil se perde.',
        'N\xc3\xa3o \xc3\xa9 o seu \xc3\xbaltimo fio de esperan\xc3\xa7a?'],
    'Spin': [
        'O que me diz de sairmos para um giro?',
        'Voc\xc3\xaa usa a centrifuga\xc3\xa7\xc3\xa3o?',
        'Isto vai fazer a sua cabe\xc3\xa7a girar de verdade!',
        'Este \xc3\xa9 o meu giro das coisas.',
        'Vou levar voc\xc3\xaa para uma volta.',
        'Como \xc3\xa9 que voc\xc3\xaa d\xc3\xa1 a "volta" no seu tempo?',
        'Olha s\xc3\xb3: voc\xc3\xaa n\xc3\xa3o quer girar at\xc3\xa9 ficar tonto?',
        'Nossa, voc\xc3\xaa est\xc3\xa1 no meio de um furac\xc3\xa3o!',
        'Meus ataques v\xc3\xa3o fazer sua cabe\xc3\xa7a rodar!'],
    'Synergy': [
        'Vou encaminhar ao comit\xc3\xaa.',
        'O seu projeto foi cancelado.',
        'O seu centro de custos ser\xc3\xa1 cortado.',
        'Estamos reestruturando o seu setor.',
        'Colocamos em vota\xc3\xa7\xc3\xa3o, e voc\xc3\xaa perdeu.',
        'Acabei de receber a aprova\xc3\xa7\xc3\xa3o final.',
        'Uma boa equipe pode se livrar de qualquer problema.',
        'J\xc3\xa1 dou um retorno a voc\xc3\xaa sobre isso.',
        'Vamos direto ao que interessa.',
        'Vamos encarar isto como uma crise de sinergia.'],
    'Tabulate': [
        'Isto n\xc3\xa3o soma em nada.',
        'Pela minha conta, voc\xc3\xaa perdeu.',
        'Voc\xc3\xaa est\xc3\xa1 fazendo um bom c\xc3\xa1lculo.',
        'Vou fazer o seu total em um minuto.',
        'Est\xc3\xa1 preparado para estes n\xc3\xbameros?',
        'Sua conta j\xc3\xa1 est\xc3\xa1 vencida e pode ser paga.',
        '\xc3\x89 hora de calcular.',
        'Gosto de colocar as coisas em ordem.',
        'E a contagem \xc3\xa9...',
        'Estes n\xc3\xbameros devem ser muito poderosos.'],
    'TeeOff': [
        'Voc\xc3\xaa n\xc3\xa3o vai bem de condi\xc3\xa7\xc3\xb5es.',
        'Olha a frente!',
        'Confio no meu taco.',
        'Gandula, preciso do meu taco!',
        'Tente evitar este risco.',
        'D\xc3\xaa impulso!',
        '\xc3\x89 mesmo um furo dentro do outro.',
        'Voc\xc3\xaa est\xc3\xa1 no meu campo.',
        'Repara s\xc3\xb3 a precis\xc3\xa3o.',
        'Cuidado com o passarinho!',
        'Fique de olho na bola!',
        'Voc\xc3\xaa se importa se eu continuar a jogar?'],
    'Tremor': [
        'Voc\xc3\xaa sentiu?',
        'Voc\xc3\xaa n\xc3\xa3o tem medo de um tremorzinho de nada, ou tem?',
        'O tremor \xc3\xa9 apenas o come\xc3\xa7o.',
        'Voc\xc3\xaa parece tenso.',
        'Vou agitar as coisas um pouco!',
        'Tudo preparado para retumbar?',
        'O que houve? Voc\xc3\xaa parece balan\xc3\xa7ado.',
        'Tremedeira de medo!',
        'Por que est\xc3\xa1 tremendo de medo?'],
    'Watercooler': [
        'Certamente, isto vai refrescar voc\xc3\xaa.',
        'N\xc3\xa3o \xc3\xa9 refrescante?',
        'Fa\xc3\xa7o a entrega.',
        'Direto da fonte - at\xc3\xa9 a sua boca.',
        'Qual \xc3\xa9 o problema, \xc3\xa9 s\xc3\xb3 uma \xc3\xa1gua de nascente.',
        'N\xc3\xa3o se preocupe, \xc3\xa9 pura.',
        'Ah, outro cliente satisfeito.',
        '\xc3\x89 hora da entrega di\xc3\xa1ria.',
        'Espero que as suas cores n\xc3\xa3o desbotem.',
        'Quer beber?',
        'Sai tudo na lavagem.',
        'A bebida \xc3\xa9 com voc\xc3\xaa.'],
    'Withdrawal': [
        'Acho que voc\xc3\xaa est\xc3\xa1 no vermelho.',
        'Espero que o seu saldo seja o suficiente para cobrir isto.',
        'Olha que vou cobrar juros.',
        'O seu saldo est\xc3\xa1 diminuindo.',
        'Em breve, voc\xc3\xaa vai precisar fazer um dep\xc3\xb3sito.',
        'Voc\xc3\xaa sofreu um colapso financeiro.',
        'Acho que voc\xc3\xaa est\xc3\xa1 em baixa.',
        'Suas finan\xc3\xa7as deca\xc3\xadram.',
        'Prevejo um per\xc3\xadodo de vacas magras.',
        '\xc3\x89 uma invers\xc3\xa3o de valores.'],
    'WriteOff': [
        'Deixe-me aumentar as suas perdas.',
        'Vamos tirar o melhor proveito poss\xc3\xadvel de um mau neg\xc3\xb3cio.',
        '\xc3\x89 hora de fazer o balan\xc3\xa7o dos caixas.',
        'Isso n\xc3\xa3o vai ficar bom nos livros-caixa.',
        'Procuro alguns dividendos.',
        'Voc\xc3\xaa deve se responsabilizar por suas perdas.',
        'Pode esquecer o b\xc3\xb4nus.',
        'Vou bagun\xc3\xa7ar todas as suas contas.',
        'Voc\xc3\xaa est\xc3\xa1 prestes a sofrer algumas perdas.',
        'Isto vai afetar os seus resultados finais.'] }
BuildingWaitingForVictors = ('Aguardando outros jogadores...',)
ElevatorHopOff = 'Descer'
ElevatorStayOff = 'Se descer, ter\xc3\xa1 de esperar\nat\xc3\xa9 que o elevador parta ou fique vazio'
ElevatorLeaderOff = 'Somente seu l\xc3\xadder pode decidir quando deve descer.'
ElevatorHoppedOff = 'Voc\xc3\xaa precisa esperar o pr\xc3\xb3ximo elevador'
ElevatorMinLaff = 'Voc\xc3\xaa precisa de %s pontos de risada para poder subir neste elevador'
ElevatorHopOK = 'OK'
ElevatorGroupMember = 'Somente o l\xc3\xadder deste grupo pode\ndecidir quando deve entrar'
KartMinLaff = 'Voc\xc3\xaa precisa de %s pontos de risada para poder andar neste carte.'
CogsIncExt = ', Ltda.'
CogsIncModifier = '%s' + CogsIncExt
CogsInc = Cogs.upper() + CogsIncExt
CogdominiumsExt = ' Cogdominiums'
Cogdominiums = Cog.upper() + CogdominiumsExt
DoorKnockKnock = 'Toc, toc.'
DoorWhosThere = 'Quem \xc3\xa9?'
DoorWhoAppendix = ' Quem?'
DoorNametag = 'Porta'
FADoorCodes_UNLOCKED = None
FADoorCodes_TALK_TO_TOM = 'Voc\xc3\xaa precisa de piadas! V\xc3\xa1 falar com o Tutorial Tom!'
FADoorCodes_DEFEAT_FLUNKY_HQ = 'Volte aqui quando tiver derrotado o Puxa-saco!'
FADoorCodes_TALK_TO_HQ = 'V\xc3\xa1 pegar a sua recompensa com o Haroldo do Quartel!'
FADoorCodes_WRONG_DOOR_HQ = 'Porta errada! V\xc3\xa1 pela outra porta para o p\xc3\xa1tio!'
FADoorCodes_GO_TO_PLAYGROUND = 'Dire\xc3\xa7\xc3\xa3o errada! Voc\xc3\xaa precisa ir para o p\xc3\xa1tio!'
FADoorCodes_DEFEAT_FLUNKY_TOM = 'Ande at\xc3\xa9 o Puxa-saco para lutar com ele!'
FADoorCodes_TALK_TO_HQ_TOM = 'V\xc3\xa1 pegar a sua recompensa no Quartel dos Toons!'
FADoorCodes_SUIT_APPROACHING = None
FADoorCodes_BUILDING_TAKEOVER = 'Cuidado! Tem um COG l\xc3\xa1 dentro!'
FADoorCodes_SB_DISGUISE_INCOMPLETE = 'Voc\xc3\xaa vai ser pego se entrar l\xc3\xa1 como um Toon! Voc\xc3\xaa precisa completar o seu Disfarce de Cog primeiro!\n\nMonte o seu Disfarce de Cog com peda\xc3\xa7os da F\xc3\xa1brica.'
FADoorCodes_CB_DISGUISE_INCOMPLETE = 'Voc\xc3\xaa vai ser pego se entrar l\xc3\xa1 como um Toon! Voc\xc3\xaa precisa completar o seu Disfarce de Rob\xc3\xb4 Mercen\xc3\xa1rio primeiro!\n\nMonte o seu Disfarce de Rob\xc3\xb4 Mercen\xc3\xa1rio executando Tarefas Toon na Sonhol\xc3\xa2ndia.'
FADoorCodes_LB_DISGUISE_INCOMPLETE = 'Voc\xc3\xaa vai ser pego se entrar l\xc3\xa1 como um Toon! Voc\xc3\xaa precisa completar o seu Disfarce de Cog primeiro!\n\nMonte o seu Disfarce de Cog com peda\xc3\xa7os da F\xc3\xa1brica.'
FADoorCodes_BB_DISGUISE_INCOMPLETE = 'Voc\xc3\xaa vai ser pego se entrar l\xc3\xa1 como Toon! Primeiramente, voc\xc3\xaa precisa concluir seu Disfarce de Rob\xc3\xb4 Chefe!\n\nConstrua seu Disfarce de Rob\xc3\xb4 Chefe cumprindo as TarefasToon depois da Sonhol\xc3\xa2ndia do Donald.'
KnockKnockContestJokes = {
    2100: [
        'Jaque',
        'Jaque n\xc3\xa3o est\xc3\xa1 olhando, joga uma torta nele!'],
    2200: {
        28: [
            'Biscuit (Biscoito)',
            'Biscuitos (Biscoitos) me mordam, os Cogs v\xc3\xaam a\xc3\xad!'],
        41: [
            'Dewey',
            'Dewemos ir detonar mais alguns Cogs?'],
        40: [
            'Minnie',
            'Minnie-pessoas falaram comigo, e isso est\xc3\xa1 me enlouquecendo!'],
        27: [
            'Disguise',
            'A Disguisetante persegui\xc3\xa7\xc3\xa3o aos Cogs!'] },
    2300: [
        'Justa',
        'Justa gora peguei uns dois peda\xc3\xa7os de Cogs, pronto!'],
    3300: {
        10: [
            'Aladdin',
            'Aladdinheiro no ch\xc3\xa3o.'],
        6: [
            'Adon',
            'Adond\xc3\xa9 que esses Cogs t\xc3\xa3o saindo?'],
        30: [
            'Bacon',
            'Bacon uma torta ia bem.'],
        28: [
            'Isa\xc3\xadas',
            'Isa\xc3\xadas mas voltou-se.'],
        12: [
            'Julieta',
            'Julieta me chamando praquele pr\xc3\xa9dio Cog com voc\xc3\xaa pra eu te Toonar.'] } }
KnockKnockJokes = [
    [
        'Quem',
        'Aqui tem eco, n\xc3\xa3o?'],
    [
        'Kika',
        'Kikalor!'],
    [
        'Joe',
        'Voc\xc3\xaa \xc3\xa9 Joetromundo?'],
    [
        'Eudin',
        'Eudinovo por aqui!'],
    [
        'Sil\xc3\xaancio',
        'Pssss!'],
    [
        'Simb\xc3\xb3',
        'Simbora pra praia.'],
    [
        'Takent',
        'Takent ou frio?'],
    [
        'No\xc3\xa1',
        'No\xc3\xa1 de qu\xc3\xaa.'],
    [
        'N\xc3\xa3o sei',
        'Nem eu, j\xc3\xa1 te falei.'],
    [
        'Otudo',
        'Otudo ou nada?'],
    [
        'Totan',
        'Totan feliz que voc\xc3\xaa est\xc3\xa1 aqui!'],
    [
        'Osmar',
        'Osmartodontes n\xc3\xa3o existem mais!'],
    [
        'Silem',
        'Silembra de mim?'],
    [
        'Ostra',
        'Ostra vez?'],
    [
        'Aim\xc3\xa9e',
        'Aim\xc3\xa9e Tida?'],
    [
        'Zoom',
        'Zooma imediatamente daqui!'],
    [
        'Aiki',
        'Aiki medo!'],
    [
        'Quiba',
        'Quibagun\xc3\xa7a \xc3\xa9 essa'],
    [
        'Tas\xc3\xb3',
        'N\xc3\xa3o, tacompanhado.'],
    [
        'Iago',
        'Iagora, Jos\xc3\xa9?'],
    [
        "'T\xc3\xa1com'",
        "'T\xc3\xa1com' tudo, n\xc3\xa3o \xc3\xa9?"],
    [
        'T\xc3\xa1di',
        'T\xc3\xa1di gra\xc3\xa7a, \xc3\xa9? Meu nome \xc3\xa9  ' + Flippy + '.'],
    [
        'Opato',
        'Opato ' + Donald + ' Deduct.'],
    [
        'Masqui',
        'Masqui coisa, abre a porta logo.'],
    [
        'N\xc3\xa9nim.',
        'N\xc3\xa9nim gu\xc3\xa9m que te interesse, deixa eu entrar.'],
    [
        'Omos',
        'Omosquito que te picou.'],
    [
        'Col\xc3\xa9s',
        'Colesterol faz mal, sai fora.'],
    [
        'Breno',
        'Breno que eu te falei que esse cara vinha.'],
    [
        'Kiko',
        'Kiko-losso!'],
    [
        'Vaiv\xc3\xaa',
        'Vaiv\xc3\xaa que eu t\xc3\xb4 atrasado.'],
    [
        'Quente',
        'Quente viu e quem te v\xc3\xaa!'],
    [
        'Vopri',
        'Vopri-meiro, t\xc3\xb4 com medo.'],
    [
        'Eunum',
        'Eunum sei. Desculpe!'],
    [
        'Ubaldo',
        'Ubaldo \xc3\xa9 o marido da balda?'],
    [
        'Alfa',
        'Alface ou tomate?'],
    [
        'Ka',
        'Ka, L, M, N, O, P.'],
    [
        'Justa',
        'Justagora que eu ia jantar.'],
    [
        'Maki',
        'Makiagem \xc3\xa9 coisa para adultos.'],
    [
        'Loga',
        'Logagora que eu entrei no banho.'],
    [
        'Quessa',
        'Quessa B? Vou me mandar.'],
    [
        'Masqui',
        'Masqui droga - abre a porta e pronto!'],
    [
        "'Jaques'",
        "'Jaquesou' importante, voc\xc3\xaa deveria falar comigo primeiro."],
    [
        'Mid\xc3\xaa',
        'Mid\xc3\xaaxa em paz!'],
    [
        'Undi',
        'Undia \xc3\xa9 da ca\xc3\xa7a outro \xc3\xa9 do ca\xc3\xa7ador.'],
    [
        'Tudor',
        'Tudor que sobe, desce.'],
    [
        'Acara',
        'Acara-pu\xc3\xa7a serviu, hein?'],
    [
        'Aispe',
        'Aispe-ran\xc3\xa7a \xc3\xa9 a \xc3\xbaltima que morre.'],
    [
        'K\xc3\xaania',
        'K\xc3\xaania sabe?'],
    [
        'Bemki',
        'Bemki te vi l\xc3\xa1 fora.'],
    [
        'Jaca',
        'Jacar\xc3\xa9 no seco anda?'],
    [
        'Quenco',
        'Quenco-chicha o rabo espicha.'],
    [
        'T\xc3\xa1di',
        'T\xc3\xa1di brincadeira, n\xc3\xa9? Deixa eu rir, ent\xc3\xa3o.'],
    [
        'Ocess\xc3\xa1',
        'Ocess\xc3\xa1-be um monte de coisa, n\xc3\xa9?'],
    [
        'Temki',
        'Temki ter uma piada melhor que essa.'],
    [
        'Cet\xc3\xa1',
        'Cet\xc3\xa1 pensando que eu sou besta?'],
    [
        'V\xc3\xb4ti',
        'V\xc3\xb4ti botar pra correr.'],
    [
        'Donalda',
        'Donalda n\xc3\xa3o... S\xc3\xa3o cinquenta centavos.'],
    [
        'Alface',
        'Alface a face \xc3\xa9 mais emocionante.'],
    [
        'Ivo',
        'Ivo c\xc3\xaa n\xc3\xa3o sabia que n\xc3\xa3o tem ningu\xc3\xa9m em casa?'],
    [
        'Quessa',
        'Quessa B\xc3\xaa? Essa brincadeira est\xc3\xa1 um saco.'],
    [
        'Quenfo',
        'Quenfo \xc3\xa0 ro\xc3\xa7a perdeu a carro\xc3\xa7a.'],
    [
        'Justa',
        'Justagora que eu ia embora.'],
    [
        'Taca',
        'Taca m\xc3\xa3e primeiro!'],
    [
        'Tanaka',
        "'Tanaka-ra' que voc\xc3\xaa n\xc3\xa3o vai se dar bem!"],
    [
        'Quenfo',
        'Quenfo ao ar perdeu o lugar!'],
    [
        'So\xc3\xa9',
        'So\xc3\xa9 jeito de falar com um amigo?'],
    [
        'Daum',
        "'Daum' tempo, pode ser?"],
    [
        'Isadora',
        'Isadora, o que \xc3\xa9 que eu fa\xc3\xa7o?'],
    [
        'V\xc3\xaassi',
        "'V\xc3\xaassi' da pr\xc3\xb3xima vez toma mais cuidado!"],
    [
        'Te\xc3\xa1',
        'Te\xc3\xa1-doro, mas isso tamb\xc3\xa9m \xc3\xa9 demais.'],
    [
        'Carlota',
        'A Carlota est\xc3\xa1 presa na roda?'],
    [
        'Bu',
        'Eu nem me assustei.'],
    [
        'Tu',
        'Tu, cara de tatu!'],
    [
        'P\xc3\xb3',
        'P\xc3\xb3-su entrar?'],
    [
        'Sar\xc3\xa1',
        'Sar\xc3\xa1 que que tem outro jeito de entrar neste pr\xc3\xa9dio?'],
    [
        'Mico',
        'Miconta que novidade \xc3\xa9 essa!'],
    [
        'Numi',
        'Numi amola e me deixa entrar.'],
    [
        'Mi\xc3\xa1',
        'Mi\xc3\xa1-juda, a porta emperrou.'],
    [
        'Nuncre',
        'Nuncre dita em mim?'],
    [
        'Dianta',
        'n\xc3\xa3o Dianta falar, voc\xc3\xaa n\xc3\xa3o vai abrir a porta...'],
    [
        'Dorr\xc3\xa9',
        'Mi, F\xc3\xa1, Sol, L\xc3\xa1, Si!'],
    [
        'Dexeu',
        'Dexeu ver quem ta\xc3\xad.'],
    [
        'T\xc3\xa1ssia',
        'T\xc3\xa1ssia-chando, hem? Abre logo.'],
    [
        'Omeu',
        'Omeu Deus do c\xc3\xa9u!'],
    [
        'Diza\xc3\xad',
        'Diza\xc3\xad o qu\xc3\xaa?'],
    [
        'Inter',
        'Interessante esta brincadeira.'],
    [
        'Grato',
        'N\xc3\xa3o h\xc3\xa1 de qu\xc3\xaa.'],
    [
        'Quic\xc3\xa3o',
        'Quic\xc3\xa3o fus\xc3\xa3o \xc3\xa9 essa?'],
    [
        'Mam\xc3\xa3o',
        'Mam\xc3\xa3o mandou bater nesta daqui!'],
    [
        'Nunci',
        'Nunci deve comer de boca cheia.'],
    [
        'Kiko',
        'E o Kiko eu tenho que saber sobre isso?'],
    [
        'Sil\xc3\xaancio',
        'Pssss!'],
    [
        'Vossoc\xc3\xa1',
        'Eu n\xc3\xa3o, por favor.'],
    [
        'Pu',
        'Pu xavida, voc\xc3\xaa me enganou.'],
    [
        'Mi\xc3\xa1',
        'Mi\xc3\xa1 corda, n\xc3\xa3o me deixa perder o bondinho.'],
    [
        'N\xc3\xadvea',
        'Feliz Niveass\xc3\xa1rio!'],
    [
        'Sino',
        'O sino faz "bl\xc3\xa9m" n\xc3\xa3o "quem".'],
    [
        'Diki',
        'Diki lado voc\xc3\xaa est\xc3\xa1?'],
    [
        'Quer\xc3\xaa',
        'Quer\xc3\xaa n\xc3\xa3o \xc3\xa9 pod\xc3\xaa.'],
    [
        'Frankstein',
        'Frankstein, mas voc\xc3\xaa n\xc3\xa3o tem.'],
    [
        'Pra Z',
        'Pra Z em conhec\xc3\xaa-lo.'],
    [
        'Ex-conde',
        'Ex-conde-conde \xc3\xa9 legal.'],
    [
        'Apri',
        'Apri-ncesa despertou com o beijo do pr\xc3\xadncipe.'],
    [
        'Quacker',
        'Quacker uma, menos esta!'],
    [
        'Qualquerco',
        'Qualquerco-isa parecida com isto j\xc3\xa1 vai me ajudar.'],
    [
        'Quiqui',
        "'Quiqui' \xc3\xa9 isso?"],
    [
        'Ab\xc3\xa1',
        'Ab\xc3\xa1-xaqui, a chave caiu!'],
    [
        'P\xc3\xb3ba',
        'P\xc3\xb3ba-t\xc3\xaa, esqueci a piada!'],
    [
        'Urralo',
        'Urralo-ween j\xc3\xa1 passou!'],
    [
        'Sar\xc3\xa1',
        'Sar\xc3\xa1 que tem um m\xc3\xa9dico em casa?'],
    [
        'Aline',
        'Aline \xc3\xa9 reta ou curva?'],
    [
        'D\xc3\xb4dis',
        'D\xc3\xb4dis t\xc3\xb4mago.'],
    [
        'D\xc3\xb4di',
        'D\xc3\xb4di dente.'],
    [
        'Toco',
        'Toco dor de cabe\xc3\xa7a.'],
    [
        'Atch',
        'Sa\xc3\xbade.'],
    [
        'Aumen',
        'Aumen-te o volume, por favor.'],
    [
        'Zupra',
        'Zupra-sumo.'],
    [
        'Tup\xc3\xb3',
        'Tup\xc3\xb3 descer ali comigo?']]
SharedChatterGreetings = [
    'Oi, %!',
    'Iuhuuu %, legal ver voc\xc3\xaa.',
    'Estou feliz que voc\xc3\xaa esteja aqui hoje!',
    'Bom, oi pessoal, %.']
SharedChatterComments = [
    'Que nome legal, %.',
    'Gosto do seu nome.',
    'Cuidado com os ' + Cogs + '.Parece que o bondinho est\xc3\xa1 chegando!',
    'Preciso jogar um jogo no bondinho para ganhar algumas tortas!',
    '\xc3\x80s vezes, eu me divirto com os jogos no bondinho s\xc3\xb3 para comer a torta de frutas!',
    'Puxa, acabei de deter um bando de ' + Cogs + '. Preciso de descanso!',
    'Puxa vida, alguns desses ' + Cogs + ' s\xc3\xa3o grandalh\xc3\xb5es!',
    'Voc\xc3\xaa parece estar se divertindo.',
    'Nossa, que dia legal!',
    'Gostei da sua roupa.',
    'Acho que vou pescar esta tarde.',
    'Divirta-se no meu bairro.',
    'Espero que voc\xc3\xaa esteja aproveitando sua estada em Toontown!',
    'Ouvi falar que est\xc3\xa1 nevando no Brrrgh.',
    'Voc\xc3\xaa pegou o bondinho hoje?',
    'Gosto de conhecer pessoas novas.',
    'Uau, h\xc3\xa1 v\xc3\xa1rios  ' + Cogs + ' no Brrrgh.Eu adoro brincar de pique. E voc\xc3\xaa?',
    'Os jogos no bondinho s\xc3\xa3o divertidos.',
    'Adoro fazer as pessoas rirem.',
    '\xc3\x89 divertido ajudar meus amigos.',
    'Hum-hum, voc\xc3\xaa est\xc3\xa1 perdido? N\xc3\xa3o se esque\xc3\xa7a de que voc\xc3\xaa tem um mapa no \xc3\x81lbum Toon.',
    'Procure n\xc3\xa3o ficar atolado na Burocracia dos ' + Cogs + "'.",
    'Ouvi falar que a ' + Daisy + ' plantou novas flores no jardim.',
    'Se voc\xc3\xaa pressionar a tecla Page Up, poder\xc3\xa1 ver acima!',
    'Se voc\xc3\xaa ajudar a tomar os edif\xc3\xadcios dos Cogs, poder\xc3\xa1 ganhar uma estrela de bronze!',
    'Se voc\xc3\xaa pressionar a tecla Tab, poder\xc3\xa1 ver os arredores sob diversos \xc3\xa2ngulos!',
    'Se voc\xc3\xaa pressionar a tecla Ctrl, poder\xc3\xa1 descer!']
SharedChatterGoodbyes = [
    'Tenho que ir agora, tchau!',
    'Acho que vou jogar no bondinho.',
    'Bom, at\xc3\xa9 mais. Vejo voc\xc3\xaa por a\xc3\xad, %!',
    'Melhor eu me apressar e voltar ao trabalho para deter esses ' + Cogs + '.',
    'Preciso ir andando.',
    'Desculpe, mas tenho que ir.',
    'Tchau.',
    'Vejo voc\xc3\xaa mais tarde, %!',
    'Acho que vou praticar lan\xc3\xa7amento de bolinhos.',
    '\\Vou me juntar a um grupo para deter alguns  ' + Cogs + '.',
    'Foi legal ver voc\xc3\xaa hoje, %.',
    'Tenho muito a fazer hoje. \xc3\x89 melhor come\xc3\xa7ar logo.']
MickeyChatter = ([
    'Bem-vindo ao ' + lToontownCentral + '.',
    'Oi, meu nome \xc3\xa9 ' + Mickey + '. Qual \xc3\xa9 o seu?'], [
    'Ei, voc\xc3\xaa viu o ' + Donald + '?',
    'Vou ver o nevoeiro passar no ' + lDonaldsDock + '.',
    'Se voc\xc3\xaa vir o meu camarada ' + Goofy + ', d\xc3\xaa um oi para ele por mim.',
    'Ouvi falar que a ' + Daisy + ' plantou novas flores no jardim.'], [
    '\\Vou para a Melodil\xc3\xa2ndia ver a ' + Minnie + '!',
    'Caramba, estou atrasado para meu encontro com a ' + Minnie + '!',
    'Parece que \xc3\xa9 hora de ' + Pluto + ' jantar.',
    'Acho que vou nadar no ' + lDonaldsDock + '.',
    '\xc3\x89 hora de tirar um cochilo. Vou para a Sonhol\xc3\xa2ndia.'])
WinterMickeyCChatter = ([
    'Ol\xc3\xa1, eu sou o Mickey Noel!',
    'Bem-vindo \xc3\xa0 cidade das estrelas... ou melhor, a Toontown!',
    'Boas-Festas!',
    'Boas-Festas, %'], [
    'Cante a m\xc3\xbasica da esta\xc3\xa7\xc3\xa3o na Campainhas Ding-dong para o Mundo e Fel\xc3\xadcia certamente devolver\xc3\xa1 o favor!',
    'Nossa, este lugar est\xc3\xa1 bem decorado!',
    'Cante a m\xc3\xbasica da esta\xc3\xa7\xc3\xa3o na Campainhas Ding-dong para o Mundo e Fel\xc3\xadcia certamente devolver\xc3\xa1 o favor!',
    'Veja s\xc3\xb3 as luzes na \xc3\xa1rvore! Que maravilha!',
    'Cante a m\xc3\xbasica da esta\xc3\xa7\xc3\xa3o na Campainhas Ding-dong para o Mundo e Fel\xc3\xadcia certamente devolver\xc3\xa1 o favor!',
    'Nenhuma criatura est\xc3\xa1 se movendo, a n\xc3\xa3o ser este rato aqui!',
    'Cante a m\xc3\xbasica da esta\xc3\xa7\xc3\xa3o na Campainhas Ding-dong para o Mundo e Fel\xc3\xadcia certamente devolver\xc3\xa1 o favor!',
    'Adoro esta \xc3\xa9poca do ano!',
    'Cante a m\xc3\xbasica da esta\xc3\xa7\xc3\xa3o na Campainhas Ding-dong para o Mundo e Fel\xc3\xadcia certamente devolver\xc3\xa1 o favor!',
    'Eu estou muito feliz, e voc\xc3\xaa?',
    'Cante a m\xc3\xbasica da esta\xc3\xa7\xc3\xa3o na Campainhas Ding-dong para o Mundo e Fel\xc3\xadcia certamente devolver\xc3\xa1 o favor!',
    'Voc\xc3\xaa conhece alguma boa can\xc3\xa7\xc3\xa3o de Natal?',
    'Cante a m\xc3\xbasica da esta\xc3\xa7\xc3\xa3o na Campainhas Ding-dong para o Mundo e Fel\xc3\xadcia certamente devolver\xc3\xa1 o favor!',
    'Poxa! Eu adoro a \xc3\xa9poca das Festas!',
    'Cante a m\xc3\xbasica da esta\xc3\xa7\xc3\xa3o na Campainhas Ding-dong para o Mundo e Fel\xc3\xadcia certamente devolver\xc3\xa1 o favor!',
    'Acho que est\xc3\xa1 na hora de colocar luvas mais quentinhas!'], [
    'Tenha boas Festas!',
    'Tudo de bom para voc\xc3\xaa!',
    'Que pena que voc\xc3\xaa tem de ir embora. At\xc3\xa9 logo!',
    'Vou cantar can\xc3\xa7\xc3\xb5es de Natal com a Minnie!'])
ValentinesMickeyChatter = ([
    'Ol\xc3\xa1, eu sou o Mickey!Bem-vindo \xc3\xa0 Dia dos namorados!Feliz Dia dos namorados!Feliz Dia dos namorados, %'], [
    'O Amor est\xc3\xa1 no ar!  E borboletas tamb\xc3\xa9m!',
    'Aqueles cora\xc3\xa7\xc3\xb5es s\xc3\xa3o bons para melhorar o Laff!',
    'Espero que a Minnie goste do que eu trouxe para ela!',
    'O Cattlelog tem v\xc3\xa1rios presentes para o Dia dos namorados!',
    'D\xc3\xaa uma festa Dia dos namorados!',
    'Mostre aos Cogs, com uma torta na cara, que voc\xc3\xaa os ama!',
    'Estou levando a Minnie para o Kooky Caf\xc3\xa9!',
    'A Minnie vai querer chocolates ou flores?'], [
    'Adorei a sua visita!Diga \xc3\xa0 Minnie que a pegarei em breve!'])
WinterMickeyDChatter = ([
    'Ol\xc3\xa1, eu sou o Mickey Noel!',
    'Bem-vindo \xc3\xa0 cidade das estrelas... ou melhor, a Toontown!',
    'Boas-Festas!',
    'Boas-Festas, %'], [
    'Nossa, este lugar est\xc3\xa1 bem decorado!',
    'Veja s\xc3\xb3 as luzes na \xc3\xa1rvore! Que maravilha!',
    'Nenhuma criatura est\xc3\xa1 se movendo, a n\xc3\xa3o ser este rato aqui!',
    'Adoro esta \xc3\xa9poca do ano!',
    'Eu estou muito feliz, e voc\xc3\xaa?',
    'Voc\xc3\xaa conhece alguma boa can\xc3\xa7\xc3\xa3o de Natal?',
    'Poxa! Eu adoro a \xc3\xa9poca das Festas!',
    'Acho que est\xc3\xa1 na hora de colocar luvas mais quentinhas!'], [
    'Tenha boas Festas!',
    'Tudo de bom para voc\xc3\xaa!',
    'Que pena que voc\xc3\xaa tem de ir embora. At\xc3\xa9 logo!',
    'Vou cantar can\xc3\xa7\xc3\xb5es de Natal com a Minnie!'])
VampireMickeyChatter = ([
    'Bem-vindo ao ' + lToontownCentral + '.',
    'Oi, meu nome \xc3\xa9 ' + Mickey + '. Qual \xc3\xa9 o seu?',
    'Feliz Halloween!',
    'Feliz Halloween, %!',
    'Bem-vindo ao Centro da Cidade Assombrada... quero dizer, ao ' + lToontownCentral + '!'], [
    'Se voc\xc3\xaa acha que fazer travessuras \xc3\xa9 divertido, visite Ralf Desocupado, na S\xc3\xb3 Divers\xc3\xa3o, para ganhar uma gostosura!',
    '\xc3\x89 divertido vestir fantasias para o Halloween!',
    'Se voc\xc3\xaa acha que fazer travessuras \xc3\xa9 divertido, visite Ralf Desocupado, na S\xc3\xb3 Divers\xc3\xa3o, para ganhar uma gostosura!',
    'Voc\xc3\xaa gosta da minha fantasia?',
    'Se voc\xc3\xaa acha que fazer travessuras \xc3\xa9 divertido, visite Ralf Desocupado, na S\xc3\xb3 Divers\xc3\xa3o, para ganhar uma gostosura!',
    '%, tome cuidado com os Cogs Vampiros!',
    'Se voc\xc3\xaa acha que fazer travessuras \xc3\xa9 divertido, visite Ralf Desocupado, na S\xc3\xb3 Divers\xc3\xa3o, para ganhar uma gostosura!',
    'As decora\xc3\xa7\xc3\xb5es de Halloween ficaram \xc3\xb3timas, n\xc3\xa9?',
    'Se voc\xc3\xaa acha que fazer Divers\xc3\xb5es e Jogos, visite Ralf Desocupado, na S\xc3\xb3 Divers\xc3\xa3o, para ganhar uma gostosura!',
    'Tome cuidado com os gatos pretos!',
    'Se voc\xc3\xaa acha que fazer Divers\xc3\xb5es e Jogos, visite Ralf Desocupado, na S\xc3\xb3 Divers\xc3\xa3o, para ganhar uma gostosura!',
    'Voc\xc3\xaa viu o Toon com a cabe\xc3\xa7a de ab\xc3\xb3bora?',
    'Se voc\xc3\xaa acha que fazer Divers\xc3\xb5es e Jogos, visite Ralf Desocupado, na S\xc3\xb3 Divers\xc3\xa3o, para ganhar uma gostosura!',
    'Bu!  Eu assustei voc\xc3\xaa?',
    'Se voc\xc3\xaa acha que fazer Divers\xc3\xb5es e Jogos, visite Ralf Desocupado, na S\xc3\xb3 Divers\xc3\xa3o, para ganhar uma gostosura!',
    'N\xc3\xa3o se esque\xc3\xa7a de escovar as presas!',
    'Se voc\xc3\xaa acha que fazer Divers\xc3\xb5es e Jogos, visite Ralf Desocupado, na S\xc3\xb3 Divers\xc3\xa3o, para ganhar uma gostosura!',
    'N\xc3\xa3o se assuste, sou um vampiro bonzinho!',
    'Se voc\xc3\xaa acha que fazer Divers\xc3\xb5es e Jogos, visite Ralf Desocupado, na S\xc3\xb3 Divers\xc3\xa3o, para ganhar uma gostosura!',
    'Espero que voc\xc3\xaa esteja gostando da nossa divers\xc3\xa3o de Halloween!',
    'Se voc\xc3\xaa acha que fazer Divers\xc3\xb5es e Jogos, visite Ralf Desocupado, na S\xc3\xb3 Divers\xc3\xa3o, para ganhar uma gostosura!',
    'Os vampiros est\xc3\xa3o muito populares este ano!'], [
    'Vou olhar as decora\xc3\xa7\xc3\xb5es curiosas de Halloween.',
    'Vou a Melodil\xc3\xa2ndia fazer uma surpresa \xc3\xa0 ' + Minnie + '!',
    'Vou assustar outro Toon!  Shhh!',
    'Vou brincar de doces ou travessuras!',
    'Shhh, vem comigo.'])
MinnieChatter = ([
    'Bem-vindo \xc3\xa0 Melodil\xc3\xa2ndia.',
    'Oi, meu nome \xc3\xa9 ' + Minnie + '. Qual \xc3\xa9 o seu?'], [
    'As colinas ganham vida com o som da m\xc3\xbasica!',
    'Sua roupa \xc3\xa9 legal, %.',
    'Ei, voc\xc3\xaa viu o ' + Mickey + '?',
    'Se voc\xc3\xaa vir meu amigo ' + Goofy + ', d\xc3\xaa um oi para ele por mim.',
    'Uau, h\xc3\xa1 milhares de ' + Cogs + ' perto da ' + lDonaldsDreamland + '.',
    'Ouvi falar que tem neblina no ' + lDonaldsDock + '.',
    'N\xc3\xa3o deixe de experimentar o labirinto dos ' + lDaisyGardens + '.',
    'Acho que vou catar algumas can\xc3\xa7\xc3\xb5es.',
    'Ei, %, olha aquilo l\xc3\xa1.',
    'Adoro o som da m\xc3\xbasica.',
    'Aposto que voc\xc3\xaa n\xc3\xa3o sabia que a Melodil\xc3\xa2ndia tamb\xc3\xa9m \xc3\xa9 chamada de ToadaTown! Ah, ah, ah!',
    'Adoro jogo da mem\xc3\xb3ria. E voc\xc3\xaa?',
    'Gosto de fazer as pessoas rirem.',
    'Cara, andar sobre rodas o dia todo n\xc3\xa3o \xc3\xa9 moleza para os p\xc3\xa9s!',
    'Bonita camisa, %.',
    'Aquilo no ch\xc3\xa3o \xc3\xa9 uma balinha?'], [
    'Caramba, estou atrasada para o meu encontro com o ' + Mickey + '!',
    'Parece que \xc3\xa9 hora de ' + Pluto + ' jantar.',
    '\xc3\x89 hora de tirar um cochilo. Vou para a Sonhol\xc3\xa2ndia.'])
WinterMinnieCChatter = ([
    'Ol\xc3\xa1, eu sou a Minnie Noel!',
    'Bem-vindo \xc3\xa0 terra das can\xc3\xa7\xc3\xb5es de Natal!',
    'Boas-Festas!',
    'Boas-Festas, %!'], [
    'Voc\xc3\xaa vai ganhar muito mais do que um corte de cabelo se cantar para B\xc3\xa1rbara Sevilha na Um Penteado por Uma Can\xc3\xa7\xc3\xa3o!',
    'Solte a voz, Toon!',
    'Voc\xc3\xaa vai ganhar muito mais do que um corte de cabelo se cantar para B\xc3\xa1rbara Sevilha na Um Penteado por Uma Can\xc3\xa7\xc3\xa3o!',
    'Mostre como se canta, Toon!',
    'Voc\xc3\xaa vai ganhar muito mais do que um corte de cabelo se cantar para B\xc3\xa1rbara Sevilha na Um Penteado por Uma Can\xc3\xa7\xc3\xa3o!',
    'Voc\xc3\xaa consegue seguir a melodia de Melodyland?',
    'Voc\xc3\xaa vai ganhar muito mais do que um corte de cabelo se cantar para B\xc3\xa1rbara Sevilha na Um Penteado por Uma Can\xc3\xa7\xc3\xa3o!',
    'Essas l\xc3\xa2mpadas parecem estar bem quentinhas com o cachecol!',
    'Voc\xc3\xaa vai ganhar muito mais do que um corte de cabelo se cantar para B\xc3\xa1rbara Sevilha na Um Penteado por Uma Can\xc3\xa7\xc3\xa3o!',
    'Cantar \xc3\xa9 tudo!',
    'Voc\xc3\xaa vai ganhar muito mais do que um corte de cabelo se cantar para B\xc3\xa1rbara Sevilha na Um Penteado por Uma Can\xc3\xa7\xc3\xa3o!',
    'Sempre vou gostar de voc\xc3\xaa, mesmo cantando mal!',
    'Voc\xc3\xaa vai ganhar muito mais do que um corte de cabelo se cantar para B\xc3\xa1rbara Sevilha na Um Penteado por Uma Can\xc3\xa7\xc3\xa3o!',
    'Tudo fica mais bonito com flores!'], [
    'Divirta-se muito durante as Festas!',
    'Caminhos felizes!',
    'Mickey vai me levar para cantar can\xc3\xa7\xc3\xb5es de natal!'])
WinterMinnieDChatter = ([
    'Ol\xc3\xa1, eu sou a Minnie Noel!',
    'Bem-vindo \xc3\xa0 terra das can\xc3\xa7\xc3\xb5es de Natal!',
    'Boas-Festas!',
    'Boas-Festas, %!'], [
    'Solte a voz, Toon!',
    'Mostre como se canta, Toon!',
    'Voc\xc3\xaa consegue seguir a melodia de Melodyland?',
    'Essas l\xc3\xa2mpadas parecem estar bem quentinhas com o cachecol!',
    'Cantar \xc3\xa9 tudo!',
    "You can't go wrong with a song!",
    'Sempre vou gostar de voc\xc3\xaa, mesmo cantando mal!',
    'Tudo fica mais bonito com flores!'], [
    'Divirta-se muito durante as Festas!',
    'Caminhos felizes!',
    'Mickey vai me levar para cantar can\xc3\xa7\xc3\xb5es de natal!'])
ValentinesMinnieChatter = ([
    'Ol\xc3\xa1, eu sou a Minnie!',
    'Feliz Dia dos namorados!',
    'Feliz Dia dos namorados,  %'], [
    'Espero que o Mickey traga chocolates ou flores para mim!',
    'Aqueles cora\xc3\xa7\xc3\xb5es s\xc3\xa3o bons para melhorar o Laff!',
    'Eu quero ir a uma festa ValenToon!',
    'Espero que o Mickey me leve ao Kooky Caf\xc3\xa9!',
    'Mickey \xc3\xa9 um \xc3\xb3timo Dia dos namorados!',
    'O que voc\xc3\xaa trouxe para seu Dia dos namorados ',
    'O Mickey nunca perdeu um Dia dos namorados!'], [
    'Espalhe o amor!',
    'Adorei sua visita!'])
WitchMinnieChatter = ([
    'Bem-vindo a uma terra m\xc3\xa1gica... ou melhor, \xc3\xa0 Terra da Melodia!',
    'Ol\xc3\xa1, meu nome \xc3\xa9 Minnie M\xc3\xa1gica! Qual \xc3\xa9 o seu?',
    'Ol\xc3\xa1, acho voc\xc3\xaa um encanto!',
    'Feliz Halloween!',
    'Feliz Halloween, %!'], [
    'Ouvi dizer que T\xc3\xa1bata tem gostosuras para aqueles que sabem fazer travessuras l\xc3\xa1 na Gatinha Bacana!',
    '\xc3\x89 um dia m\xc3\xa1gico, n\xc3\xa3o acha?',
    'Ouvi dizer que T\xc3\xa1bata tem gostosuras para aqueles que sabem fazer travessuras l\xc3\xa1 na Gatinha Bacana!',
    'Onde eu coloquei meu livro de magia?',
    'Ouvi dizer que T\xc3\xa1bata tem gostosuras para aqueles que sabem fazer travessuras l\xc3\xa1 na Gatinha Bacana!',
    'Abracadabra!',
    'Ouvi dizer que T\xc3\xa1bata tem gostosuras para aqueles que sabem fazer travessuras l\xc3\xa1 na Gatinha Bacana!',
    'Toontown est\xc3\xa1 assustadora hoje!',
    'Ouvi dizer que T\xc3\xa1bata tem gostosuras para aqueles que sabem fazer travessuras l\xc3\xa1 na Gatinha Bacana!',
    'Voc\xc3\xaa tamb\xc3\xa9m est\xc3\xa1 vendo estrelas?',
    'Ouvi dizer que T\xc3\xa1bata tem gostosuras para aqueles que sabem fazer travessuras l\xc3\xa1 na Gatinha Bacana!',
    'Roxo \xc3\xa9 a minha cor favorita!',
    'Ouvi dizer que T\xc3\xa1bata tem gostosuras para aqueles que sabem fazer travessuras l\xc3\xa1 na Gatinha Bacana!',
    'Espero que o seu Halloween seja um susto s\xc3\xb3!',
    'Ouvi dizer que T\xc3\xa1bata tem gostosuras para aqueles que sabem fazer travessuras l\xc3\xa1 na Gatinha Bacana!',
    'Tome cuidado com as aranhas musicais!',
    'Ouvi dizer que T\xc3\xa1bata tem gostosuras para aqueles que sabem fazer travessuras l\xc3\xa1 na Gatinha Bacana!',
    'Espero que voc\xc3\xaa esteja gostando da nossa divers\xc3\xa3o de Halloween!'], [
    'Eu vou desaparecer agora!',
    'Est\xc3\xa1 na hora de desaparecer!',
    'Mickey vai me levar para pedir gostosuras!'])
DaisyChatter = ([
    'Bem-vindo(a) ao meu Jardim!',
    'Ol\xc3\xa1, meu nome \xc3\xa9 ' + Daisy + '. Qual o seu nome?',
    '\xc3\x89 muito bom ver voc\xc3\xaa, %!'], [
    'Minha flor premiada est\xc3\xa1 no centro do labirinto do jardim.',
    'Eu adoro andar pelo labirinto.',
    'Eu n\xc3\xa3o v\xc3\xad o ' + Goofy + ' hoje.',
    'Eu gostaria de saber onde o ' + Goofy + ' est\xc3\xa1.',
    'Voc\xc3\xaa viu o ' + Donald + '? Eu n\xc3\xa3o consigo encontr\xc3\xa1-lo em lugar algum.',
    'Se voc\xc3\xaa vir minha amiga ' + Minnie + ', por favor diga "Oi" por mim.',
    'Quanto melhor as ferramentas de jardinagem que voc\xc3\xaa tem, melhor ser\xc3\xa1 seu jardim.',
    'Existem muitos ' + Cogs + ' perto do ' + lDonaldsDock + '.',
    'Regando seu jardim diariamente voc\xc3\xaa deixa suas plantas felizes.',
    'Para cultivar uma Margarida Rosa, plante uma balinha amarela e uma vermelha juntas.',
    '\xc3\x89 facil cultivar uma Margarida Amarela. Basta plantar uma balinha amarela.',
    'Se voc\xc3\xaa vir areia embaixo de uma planta, est\xc3\xa1 na hora de regar ou ela morrer\xc3\xa1.'], [
    'Estou indo para Melodil\xc3\xa2ndia para ver %s!' % Minnie,
    'Preciso correr para o meu picnic com %s!' % Donald,
    'Acho que vou nadar no ' + lDonaldsDock + '.',
    'Oh, estou com sono. Acho que vou para a Sonhol\xc3\xa2ndia.'])
ValentinesDaisyChatter = ([
    'Ol\xc3\xa1, eu sou a Margarida!',
    'Feliz Dia dos namorados!',
    'Feliz Dia dos namorados,  %'], [
    'Espero que o Donald n\xc3\xa3o me traga outro Amore Eel!',
    "O Donald est\xc3\xa1 me levando ao 'Deep-Sea'!",
    'Com certeza, eu tenho rosas suficientes!',
    'Aqueles cora\xc3\xa7\xc3\xb5es s\xc3\xa3o bons para melhorar o Laff!',
    'Eu adoraria ir a uma festa Dia dos namorados!',
    'Este \xc3\xa9 um jardim onde o amor cresce!',
    '\xc3\x89 bom que o Donald n\xc3\xa3o durma novamente no Dia dos namorados!',
    'Talvez eu e o Donald possamos sair com o Mickey e a Minnie!'], [
    'Diga ao Donald que eu estou esperando por ele!',
    'Feliz Dia dos namorados!'])
WinterDaisyCChatter = ([
    'Bem-vindo ao \xc3\xbanico jardim que cresce no inverno!',
    'Boas-Festas!',
    'Boas-Festas, %!'], [
    'Suzana, da Artesanato P\xc3\xadnus, adora m\xc3\xbasica, ent\xc3\xa3o por que n\xc3\xa3o compor uma can\xc3\xa7\xc3\xa3o de Natal para ela?',
    'Meu jardim precisa de mais visco!',
    'Suzana, da Artesanato P\xc3\xadnus, adora m\xc3\xbasica, ent\xc3\xa3o por que n\xc3\xa3o compor uma can\xc3\xa7\xc3\xa3o de Natal para ela?',
    'Preciso plantar azevinho para o ano que vem!',
    'Suzana, da Artesanato P\xc3\xadnus, adora m\xc3\xbasica, ent\xc3\xa3o por que n\xc3\xa3o compor uma can\xc3\xa7\xc3\xa3o de Natal para ela?',
    'Vou pedir para o Pateta construir uma casa de biscoito de gengibre para mim!',
    'Suzana, da Artesanato P\xc3\xadnus, adora m\xc3\xbasica, ent\xc3\xa3o por que n\xc3\xa3o compor uma can\xc3\xa7\xc3\xa3o de Natal para ela?',
    'Essas luzes s\xc3\xa3o lindas!',
    'Suzana, da Artesanato P\xc3\xadnus, adora m\xc3\xbasica, ent\xc3\xa3o por que n\xc3\xa3o compor uma can\xc3\xa7\xc3\xa3o de Natal para ela?',
    'O azevinho deixa o ambiente mais alegre!',
    'Suzana, da Artesanato P\xc3\xadnus, adora m\xc3\xbasica, ent\xc3\xa3o por que n\xc3\xa3o compor uma can\xc3\xa7\xc3\xa3o de Natal para ela?',
    'Meu boneco de neve sempre derrete!',
    'Suzana, da Artesanato P\xc3\xadnus, adora m\xc3\xbasica, ent\xc3\xa3o por que n\xc3\xa3o compor uma can\xc3\xa7\xc3\xa3o de Natal para ela?',
    'Que pato mais enfeitado!',
    'Suzana, da Artesanato P\xc3\xadnus, adora m\xc3\xbasica, ent\xc3\xa3o por que n\xc3\xa3o compor uma can\xc3\xa7\xc3\xa3o de Natal para ela?',
    'Eu mesma que criei todas estas luzes!'], [
    'Tenha Festas cheias de alegria!',
    'Boa planta\xc3\xa7\xc3\xa3o!',
    'Diga a Donald para trazer meus presentes!',
    'Donald vai me levar para cantar can\xc3\xa7\xc3\xb5es de natal!'])
WinterDaisyDChatter = ([
    'Bem-vindo ao \xc3\xbanico jardim que cresce no inverno!',
    'Boas-Festas!',
    'Boas-Festas, %!'], [
    'Meu jardim precisa de mais visco!',
    'Preciso plantar azevinho para o ano que vem!',
    'Vou pedir para o Pateta construir uma casa de biscoito de gengibre para mim!',
    'Essas luzes s\xc3\xa3o lindas!',
    'O azevinho deixa o ambiente mais alegre!',
    'Meu boneco de neve sempre derrete!',
    'Que pato mais enfeitado!',
    'Eu mesma que criei todas estas luzes!'], [
    'Tenha Festas cheias de alegria!',
    'Boa planta\xc3\xa7\xc3\xa3o!',
    'Diga a Donald para trazer meus presentes!',
    'Donald vai me levar para cantar can\xc3\xa7\xc3\xb5es de natal!'])
HalloweenDaisyChatter = ([
    'Bem-vindo ao jardim fantasma... quer dizer, ao jardim da Margarida!',
    'Feliz Halloween!',
    'Feliz Halloween, %!'], [
    'Se voc\xc3\xaa tiver uma travessura, visite meu amigo J. Jardim, na Pousada P\xc3\xa1 de Coisa, para ganhar gostosuras!',
    'Quer dan\xc3\xa7ar?',
    'Se voc\xc3\xaa tiver uma travessura, visite meu amigo J. Jardim, na Pousada P\xc3\xa1 de Coisa, para ganhar gostosuras!',
    'Sou um pato com uma saia poodle!',
    'Se voc\xc3\xaa tiver uma travessura, visite meu amigo J. Jardim, na Pousada P\xc3\xa1 de Coisa, para ganhar gostosuras!',
    'A \xc3\xa1rvore pirata precisa de \xc3\xa1gua.',
    'Se voc\xc3\xaa tiver uma travessura, visite meu amigo J. Jardim, na Pousada P\xc3\xa1 de Coisa, para ganhar gostosuras!',
    'Gostosuras ou \xc3\xa1rvores!',
    'Se voc\xc3\xaa tiver uma travessura, visite meu amigo J. Jardim, na Pousada P\xc3\xa1 de Coisa, para ganhar gostosuras!',
    'Voc\xc3\xaa notou algo estranho nas \xc3\xa1rvores?',
    'Se voc\xc3\xaa tiver uma travessura, visite meu amigo J. Jardim, na Pousada P\xc3\xa1 de Coisa, para ganhar gostosuras!',
    'Eu deveria plantar algumas ab\xc3\xb3boras!',
    'Se voc\xc3\xaa tiver uma travessura, visite meu amigo J. Jardim, na Pousada P\xc3\xa1 de Coisa, para ganhar gostosuras!',
    'QUEM notou algo diferente nas l\xc3\xa2mpadas?',
    'Se voc\xc3\xaa tiver uma travessura, visite meu amigo J. Jardim, na Pousada P\xc3\xa1 de Coisa, para ganhar gostosuras!',
    'Eu realmente gosto do Halloween!',
    'Se voc\xc3\xaa tiver uma travessura, visite meu amigo J. Jardim, na Pousada P\xc3\xa1 de Coisa, para ganhar gostosuras!',
    'Gostosuras ou galhos!',
    'Se voc\xc3\xaa tiver uma travessura, visite meu amigo J. Jardim, na Pousada P\xc3\xa1 de Coisa, para ganhar gostosuras!',
    'Aposto que voc\xc3\xaa n\xc3\xa3o reparou nas l\xc3\xa2mpadas assustadoras!',
    'Se voc\xc3\xaa tiver uma travessura, visite meu amigo J. Jardim, na Pousada P\xc3\xa1 de Coisa, para ganhar gostosuras!',
    'Espero que voc\xc3\xaa esteja gostando da nossa divers\xc3\xa3o de Halloween!'], [
    'Donald vai me levar para pedir gostosuras!',
    'Vou dar uma olhada nas decora\xc3\xa7\xc3\xb5es divertidas de Halloween.'])
ChipChatter = ([
    'Boas-vindas a %s!' % lOutdoorZone,
    'Ol\xc3\xa1, sou ' + Chip + '. Qual \xc3\xa9 o seu nome?',
    'N\xc3\xa3o, eu sou ' + Chip + '.',
    '\xc3\x89 t\xc3\xa3o bom ver voc\xc3\xaa, %!',
    'Somos Tico e Teco!'], [
    'Gosto de golfe.',
    'Temos as melhores bolotas de Toontown.',
    'Os buracos de golfe com vulc\xc3\xb5es s\xc3\xa3o os mais desafiadores para mim.'], [
    'Vamos at\xc3\xa9 ' + lTheBrrrgh + ' brincar com %s.' % Pluto,
    'Vamos visitar %s e dar um jeito nele.' % Donald,
    'Acho que vou nadar no ' + lDonaldsDock + '.',
    'Oh, estou com sono. Acho que vou at\xc3\xa9 a Sonhol\xc3\xa2ndia.'])
ValentinesChipChatter = ([
    'Eu sou o Tico!',
    'Feliz Dia dos namorados!',
    'Feliz Dia dos namorados,  %!'], [
    'O que voc\xc3\xaa trouxe para mim no Dia dos namorados, Teco?',
    'Aqueles cora\xc3\xa7\xc3\xb5es s\xc3\xa3o bons para melhorar o Laff!',
    'Voc\xc3\xaa ser\xc3\xa1 meu ValenToon, Teco?',
    'O que voc\xc3\xaa pegou para os Cogs para o Dia dos namorados, Teco?',
    'Eu amo o Dia dos namorados!'], [
    'Volte quando quiser!'])
WinterChipChatter = ([
    'Boas-Festas!',
    'Vestidos como esquilos!',
    'Boas-Festas, %!'], [
    'Boas-Festas, Teco!',
    'E n\xc3\xb3s pens\xc3\xa1vamos que toda esta \xc3\xa1gua congelaria no inverno!',
    'Dever\xc3\xadamos trocar as bolas de golfe por bolas de neve!',
    'Se ao menos os esquilos soubessem cantar!',
    'Eu disse para VOC\xc3\x8a fazer isso!',
    'Eu disse para VOC\xc3\x8a fazer isso!'], [
    'Tenha Festas cheias de alegria!',
    'N\xc3\xa3o se esque\xc3\xa7a de dar um presente aos Cogs por n\xc3\xb3s!'])
HalloweenChipChatter = ([
    'Jogue um pouco de miniterror... quer dizer, minigolfe!',
    'Feliz Halloween!',
    'Feliz Halloween, %!'], [
    'Somos malucos por Halloween!',
    'Voc\xc3\xaa est\xc3\xa1 preso.',
    'Voc\xc3\xaa n\xc3\xa3o pode fugir do bra\xc3\xa7o longo da lei.',
    'Sou um Tira!',
    'Espero que esteja curtindo a nossa divers\xc3\xa3o de Halloween!',
    'Jogue golfe a acerte o Buraco do Medo.',
    'As balinhas s\xc3\xa3o mais doces do que as bolotas.',
    'Espero que voc\xc3\xaa esteja gostando da nossa divers\xc3\xa3o de Halloween!'], [
    '%, watch out for Bloodsucker Cogs!'])
DaleChatter = ([
    '\xc3\x89 t\xc3\xa3o bom ver voc\xc3\xaa, %!',
    'Ol\xc3\xa1, sou ' + Dale + '. Qual \xc3\xa9 o seu nome?',
    'Ol\xc3\xa1, sou ' + Chip + '.',
    'Boas-vindas a %s!' % lOutdoorZone,
    'Somos Tico e Teco!'], [
    'Gosto de piqueniques.',
    'As bolotas s\xc3\xa3o gostosas, experimente.',
    'Aqueles moinhos tamb\xc3\xa9m s\xc3\xa3o dif\xc3\xadceis.'], [
    'Hihihi, \xc3\xa9 divertido brincar com ' + Pluto + '.',
    'Sim, vamos dar um jeito em %s.' % Donald,
    'Ah, seria refrescante dar uma nadada.',
    'Estou ficando cansado, uma boa soneca cairia bem.'])
ValentinesDaleChatter = ([
    'Eu sou o Teco!',
    'Feliz Dia dos namorados!',
    'Feliz Dia dos namorados,  %!'], [
    'O mesmo do ano passado.  NADA!',
    'Eu perdi as nozes!',
    'Voc\xc3\xaa ser\xc3\xa1 meu Dia dos namorados, Tico?',
    'Uma torta na cara!',
    'Sim, \xc3\xa9 legal.'], [
    'N\xc3\xb3s estaremos livres durante todo o Dia dos namorados!'])
WinterDaleChatter = ([
    'Boas-Festas!',
    'Ol\xc3\xa1, somos dois elfos do Natal!',
    'Esquilos No\xc3\xa9is!',
    'Boas-Festas, %!'], [
    'Boas-Festas, Tico!',
    'E n\xc3\xb3s pens\xc3\xa1vamos que toda esta \xc3\xa1gua congelaria no inverno!',
    'Dever\xc3\xadamos trocar as bolas de golfe por bolas de neve!',
    'Se ao menos os esquilos soubessem cantar!',
    'Voc\xc3\xaa se lembrou de guardar as nozes para o inverno?',
    'Oh-oh!'], [
    'Tenha Festas cheias de alegria!',
    'N\xc3\xa3o se esque\xc3\xa7a de dar um presente aos cogs por n\xc3\xb3s!'])
HalloweenDaleChatter = ([
    'Feliz Halloween, %!',
    'Jogue um pouco de miniterror... quer dizer, minigolfe!',
    'Feliz Halloween!'], [
    'Somos malucos por Halloween!',
    '\xc3\x93timo, posso usar o restante!',
    'Mas seus bra\xc3\xa7os s\xc3\xa3o curtos!',
    'Achei que voc\xc3\xaa fosse uma Lasca!',
    'Jogue golfe a acerte o Buraco do Medo.',
    'As balas de milho s\xc3\xa3o mais doces do que as bolotas.',
    'Espero que esteja curtindo a nossa divers\xc3\xa3o de Halloween!'], [
    '%, tome cuidado com os Cogs Vampiros!'])
GoofyChatter = ([
    'Bem-vindo aos ' + lDaisyGardens + '.',
    'Oi, meu nome \xc3\xa9 ' + Goofy + '. Qual \xc3\xa9 o seu?',
    'Puxa, muito legal ver voc\xc3\xaa %!'], [
    'Cara, com certeza \xc3\xa9 f\xc3\xa1cil se perder no labirinto do jardim!',
    'N\xc3\xa3o deixe de tentar entrar no labirinto.',
    'N\xc3\xa3o vi a ' + Daisy + ' o dia todo.',
    'Onde ser\xc3\xa1 que a ' + Daisy + ' est\xc3\xa1?',
    'Ei, voc\xc3\xaa viu o ' + Donald + '?',
    'Se voc\xc3\xaa vir o meu amigo ' + Mickey + ', d\xc3\xaa um oi para ele por mim.',
    'Ah, n\xc3\xa3o! Esqueci de fazer o caf\xc3\xa9 da manh\xc3\xa3 do ' + Mickey + '!',
    'Puxa, com certeza h\xc3\xa1 muitos ' + Cogs + ' perto do ' + lDonaldsDock + '.',
    'Parece que a ' + Daisy + ' plantou novas flores no jardim.',
    'Na filial da minha Loja de Piadas no Brrrgh, h\xc3\xa1 \xc3\x93culos hipn\xc3\xb3ticos em promo\xc3\xa7\xc3\xa3o por apenas uma balinha!',
    'As Lojas de piadas do Pateta oferecem as melhores goza\xc3\xa7\xc3\xb5es, truques e com\xc3\xa9dias de toda Toontown!',
    'Nas Lojas de piadas do Pateta, todas as tortas na cara t\xc3\xaam garantia de fazer rir, ou voc\xc3\xaa tem as suas balinhas de volta!'], [
    '\\Vou para Melodil\xc3\xa2ndia para ver a  ' + Minnie + '!',
    'Caramba, estou atrasado para o meu jogo com o  ' + Donald + '!',
    'Acho que vou nadar no Porto do ' + lDonaldsDock + '.',
    '\xc3\x89 hora de tirar um cochilo. Vou para a Sonhol\xc3\xa2ndia.'])
WinterGoofyChatter = ([
    'Eu sou o Pateta e adoro a \xc3\xa9poca das Festas!',
    'Bem-vindo ao Circuito Bola de Neve!',
    'Boas-Festas!',
    'Boas-Festas, %!'], [
    'Quem precisa de renas quando se tem um kart veloz?',
    'Nossa! J\xc3\xa1 chegaram as Festas?',
    'Eu preciso dos meus protetores de orelha!',
    'Ainda n\xc3\xa3o comecei a comprar os presentes!',
    'N\xc3\xa3o dirija seu kart no gelo!',
    'Parece que faz apenas um ano que est\xc3\xa1vamos na \xc3\xa9poca das Festas!',
    'Deixe o seu kart todo enfeitado!',
    'Estes karts s\xc3\xa3o melhores do que qualquer tren\xc3\xb3 velho!',
    '\xc3\x89 dif\xc3\xadcil dirigir com a cabe\xc3\xa7a de um boneco de neve?'], [
    'Tenha Festas muito felizes!',
    'Dirija com cuidado!',
    'Cuidado com as renas aladas!'])
ValentinesGoofyChatter = ([
    'Eu sou o Pateta e estou animado para o Dia ValenToon!',
    'Feliz Dia dos namorados!',
    'Feliz Dia dos namorados,  %!'], [
    'Nossa!  J\xc3\xa1 \xc3\xa9 o Dia dos namorados?',
    'Eu ADORO corrida de kart!',
    'Seja bacana com os outros!',
    'Mostre ao seu amor o novo kart!',
    'Toons amam seus karts!',
    'Fa\xc3\xa7a alguns novos amigos na pista!'], [
    'Dirija com cuidado!',
    'Demonstre um pouco de amor!'])
GoofySpeedwayChatter = ([
    'Bem-vindo a ' + lGoofySpeedway + '.',
    'Oi, meu nome \xc3\xa9 ' + Goofy + '. Qual \xc3\xa9 o seu?',
    'Puxa, muito legal ver voc\xc3\xaa %!'], [
    'Cara, assisti a uma corrida maneira hoje.',
    'Cuidado com as cascas de banana na pista!',
    'Voc\xc3\xaa deu uma incrementada no seu kart?',
    'A gente acabou de pegar uns aros novos na loja do kart.',
    'Oi, voc\xc3\xaa viu ' + Donald + '?',
    'Se voc\xc3\xaa vir meu amigo ' + Mickey + ', diz que eu mandei um al\xc3\xb4.',
    'Ah, n\xc3\xa3o! Esqueci de preparar para ' + Mickey + ' o caf\xc3\xa9 da manh\xc3\xa3!',
    'Puxa, com certeza h\xc3\xa1 muitos ' + Cogs + ' perto de ' + lDonaldsDock + '.',
    'Na filial da minha Loja de Piadas no Brrrgh, h\xc3\xa1 \xc3\x93culos hipn\xc3\xb3ticos em promo\xc3\xa7\xc3\xa3o por apenas uma balinha!',
    'As Lojas de piadas do Pateta oferecem as melhores goza\xc3\xa7\xc3\xb5es, truques e com\xc3\xa9dias de toda Toontown!',
    'Nas Lojas de piadas do Pateta, todas as tortas na cara t\xc3\xaam garantia de fazer rir, ou voc\xc3\xaa tem as suas balinhas de volta!'], [
    'Vou para Melodil\xc3\xa2ndia para ver %s!' % Mickey,
    'Caramba, estou atrasado para o meu jogo com %s!' % Donald,
    'Acho que vou nadar no ' + lDonaldsDock + '.',
    '\xc3\x89 hora de tirar um cochilo. Vou para a Sonhol\xc3\xa2ndia.'])
SuperGoofyChatter = ([
    'Bem-vindo ao Supercircuito!',
    'Ol\xc3\xa1, eu sou o Superpateta! Qual \xc3\xa9 o seu nome?',
    'Feliz Halloween!',
    'Feliz Halloween, %!'], [
    'Estou me sentindo corajoso hoje!',
    'Algu\xc3\xa9m viu minha capa por a\xc3\xad? Ah, a\xc3\xad est\xc3\xa1 ela!',
    'Nossa! N\xc3\xa3o conhe\xc3\xa7o a minha pr\xc3\xb3pria for\xc3\xa7a!',
    'Algu\xc3\xa9m chamou um super-her\xc3\xb3i?',
    'Cuidado, Cogs! Eu salvarei o Halloween!',
    'N\xc3\xa3o h\xc3\xa1 nada mais assustador do que eu dirigindo um kart!',
    'Aposto que voc\xc3\xaa n\xc3\xa3o est\xc3\xa1 me reconhecendo por tr\xc3\xa1s da m\xc3\xa1scara!',
    '\xc3\x89 divertido vestir fantasias para o Halloween!',
    'Espero que voc\xc3\xaa esteja gostando da nossa divers\xc3\xa3o de Halloween!'], [
    'Preciso ir voando!',
    'Para o alto!',
    'Ser\xc3\xa1 que vou voando ou dirigindo at\xc3\xa9 a Doca do Donald?',
    'Nossa, feliz Halloween!'])
DonaldChatter = ([
    'Bem-vindo \xc3\xa0 Sonhol\xc3\xa2ndia.',
    'Oi, meu nome \xc3\xa9 ' + Donald + '. Qual \xc3\xa9 o seu?'], [
    '\xc3\x80s vezes este lugar me d\xc3\xa1 arrepios.',
    'N\xc3\xa3o deixe de experimentar o labirinto dos ' + lDaisyGardens + '.',
    'Nossa, que dia legal!',
    'Ei, voc\xc3\xaa viu o ' + Mickey + '?',
    'Se voc\xc3\xaa vir meu parceiro ' + Goofy + ', d\xc3\xaa um oi para ele por mim.',
    'Acho que vou pescar esta tarde.',
    'Uau, h\xc3\xa1 um monte de ' + Cogs + ' no ' + lDonaldsDock + '.',
    'Escuta, eu n\xc3\xa3o levei voc\xc3\xaa ainda para um passeio no ' + lDonaldsDock + '?',
    'N\xc3\xa3o vi a ' + Daisy + ' o dia todo.',
    'Ouvi falar que a ' + Daisy + ' plantou novas flores no jardim.',
    'Quack.'], [
    'Vou a Melodil\xc3\xa2ndia para ver a ' + Minnie + '!',
    'Ah n\xc3\xa3o, estou atrasado para o meu encontro com a ' + Daisy + '!',
    'Acho que vou nadar no meu cais.',
    'Acho que vou levar meu barco para um giro no meu cais.'])
WinterDreamlandCChatter = ([
    'Ol\xc3\xa1, eu sou o Donald Sonolento!',
    'Bem-vindo \xc3\xa0 Terra dos Sonhos!',
    'Boas-Festas!',
    'Boas-Festas, %!'], [
    'Samuel diz que aprender a cantar em Fala Dormindo \xc3\xa9 um verdadeiro privil\xc3\xa9gio. V\xc3\xa1 at\xc3\xa9 a Escola de Canto, cante uma can\xc3\xa7\xc3\xa3o e descubra por qu\xc3\xaa!',
    'Queria estar na minha cama, debaixo do cobertor!',
    'Samuel diz que aprender a cantar em Fala Dormindo \xc3\xa9 um verdadeiro privil\xc3\xa9gio. V\xc3\xa1 at\xc3\xa9 a Escola de Canto, cante uma can\xc3\xa7\xc3\xa3o e descubra por qu\xc3\xaa!',
    'Estou sonhando com uma Toontown toda branquinha!',
    'Samuel diz que aprender a cantar em Fala Dormindo \xc3\xa9 um verdadeiro privil\xc3\xa9gio. V\xc3\xa1 at\xc3\xa9 a Escola de Canto, cante uma can\xc3\xa7\xc3\xa3o e descubra por qu\xc3\xaa!',
    'Eu queria ter deixado leite e biscoitos!',
    'Samuel diz que aprender a cantar em Fala Dormindo \xc3\xa9 um verdadeiro privil\xc3\xa9gio. V\xc3\xa1 at\xc3\xa9 a Escola de Canto, cante uma can\xc3\xa7\xc3\xa3o e descubra por qu\xc3\xaa!',
    'Quando eu acordar, quero ver um monte de presentes!',
    'Samuel diz que aprender a cantar em Fala Dormindo \xc3\xa9 um verdadeiro privil\xc3\xa9gio. V\xc3\xa1 at\xc3\xa9 a Escola de Canto, cante uma can\xc3\xa7\xc3\xa3o e descubra por qu\xc3\xaa!',
    'Espero que eu n\xc3\xa3o durma durante as Festas!',
    'Samuel diz que aprender a cantar em Fala Dormindo \xc3\xa9 um verdadeiro privil\xc3\xa9gio. V\xc3\xa1 at\xc3\xa9 a Escola de Canto, cante uma can\xc3\xa7\xc3\xa3o e descubra por qu\xc3\xaa!',
    'Adoro tirar uma soneca no frio!',
    'Samuel diz que aprender a cantar em Fala Dormindo \xc3\xa9 um verdadeiro privil\xc3\xa9gio. V\xc3\xa1 at\xc3\xa9 a Escola de Canto, cante uma can\xc3\xa7\xc3\xa3o e descubra por qu\xc3\xaa!',
    'As \xc3\xa1rvores nas ruas est\xc3\xa3o cobertas de luzes!'], [
    'Uma boa-noite para todos!',
    'Doces sonhos!',
    'Quando eu acordar, vou cantar can\xc3\xa7\xc3\xb5es de Natal!'])
WinterDreamlandDChatter = ([
    'Ol\xc3\xa1, eu sou o Donald Sonolento!',
    'Bem-vindo \xc3\xa0 Terra dos Sonhos!',
    'Boas-Festas!',
    'Boas-Festas, %!'], [
    'Queria estar na minha cama, debaixo do cobertor!',
    'Estou sonhando com uma Toontown toda branquinha!',
    'Eu queria ter deixado leite e biscoitos!',
    'Quando eu acordar, quero ver um monte de presentes!',
    'Espero que eu n\xc3\xa3o durma durante as Festas!',
    'Adoro tirar uma soneca no frio!',
    'As \xc3\xa1rvores nas ruas est\xc3\xa3o cobertas de luzes!'], [
    'Uma boa-noite para todos!',
    'Doces sonhos!',
    'Quando eu acordar, vou cantar can\xc3\xa7\xc3\xb5es de Natal!'])
HalloweenDreamlandChatter = ([
    'Feliz Halloween!',
    'Feliz Halloween, %!',
    'Ol\xc3\xa1, eu sou o FrankenDonald'], [
    'Se voc\xc3\xaa conseguir fazer uma travessura com o meu amigo M\xc3\xa1ximo, poder\xc3\xa1 visitar o Relaxe ao M\xc3\xa1ximo e saborear uma gostosura!',
    'Meus sonhos est\xc3\xa3o assustadores hoje!',
    'Se voc\xc3\xaa conseguir fazer uma travessura com o meu amigo M\xc3\xa1ximo, poder\xc3\xa1 visitar o Relaxe ao M\xc3\xa1ximo e saborear uma gostosura!',
    'Acho que estou sonhando. Aquela l\xc3\xa2mpada virou uma bruxa!',
    'Se voc\xc3\xaa conseguir fazer uma travessura com o meu amigo M\xc3\xa1ximo, poder\xc3\xa1 visitar o Relaxe ao M\xc3\xa1ximo e saborear uma gostosura!',
    'Estou sonhando ou aquele Toon tem uma cabe\xc3\xa7a de ab\xc3\xb3bora?',
    'Se voc\xc3\xaa conseguir fazer uma travessura com o meu amigo M\xc3\xa1ximo, poder\xc3\xa1 visitar o Relaxe ao M\xc3\xa1ximo e saborear uma gostosura!',
    'Quando eu acordar, espero que n\xc3\xa3o esteja tudo t\xc3\xa3o assustador! ',
    'Se voc\xc3\xaa conseguir fazer uma travessura com o meu amigo M\xc3\xa1ximo, poder\xc3\xa1 visitar o Relaxe ao M\xc3\xa1ximo e saborear uma gostosura!',
    'Espero que eu n\xc3\xa3o durma durante o Halloween!',
    'Se voc\xc3\xaa conseguir fazer uma travessura com o meu amigo M\xc3\xa1ximo, poder\xc3\xa1 visitar o Relaxe ao M\xc3\xa1ximo e saborear uma gostosura!',
    'Espero que voc\xc3\xaa esteja gostando da nossa divers\xc3\xa3o de Halloween!'], [
    'Durma com as luzes acesas hoje!',
    'Quando eu acordar, vou pedir gostosuras!'])
ValentinesDreamlandChatter = ([
    'Ol\xc3\xa1, eu sou (bocejo) o Donald!',
    'Feliz Dia dos namorados!',
    'Feliz Dia dos namorados,  %!'], [
    'Espero n\xc3\xa3o dormir no Dia dos namorados!',
    'Estava sonhando com a Margarida!',
    'Eu tive um pesadelo no qual eu perdia o Dia dos namorados!',
    'Aqueles cora\xc3\xa7\xc3\xb5es s\xc3\xa3o bons para melhorar o Laff!',
    'D\xc3\xaa uma festa Dia dos namorados!',
    'Mostre aos Cogs, com uma torta na cara, que voc\xc3\xaa os ama!',
    'Eu n\xc3\xa3o poderia sonhar com um feriado melhor do que o Dia dos namorados!',
    'Eu amo dormir!'], [
    'Boa-noite!',
    'Acorde-me no Dia dos namorados!'])
HalloweenDonaldChatter = ([
    'Bem-vindo ao meu porto do Halloween!',
    'Se voc\xc3\xaa tiver gostosuras, poder\xc3\xa1 subir a bordo!',
    'Feliz Halloween!',
    'Feliz Halloween, %!'], [
    'Se voc\xc3\xaa n\xc3\xa3o se sente bem fazendo travessuras, procure Rudy, na Rid\xc3\xadquilhas, para ganhar uma gostosura! ',
    'Mas eu uso roupa de marinheiro todos os dias!',
    'Se voc\xc3\xaa n\xc3\xa3o se sente bem fazendo travessuras, procure Rudy, na Rid\xc3\xadquilhas, para ganhar uma gostosura! ',
    'Ab\xc3\xb3boras fazem \xc3\xb3timas lanternas!',
    'Se voc\xc3\xaa n\xc3\xa3o se sente bem fazendo travessuras, procure Rudy, na Rid\xc3\xadquilhas, para ganhar uma gostosura! ',
    'Nunca vi palmeiras com pernas peludas!',
    'Se voc\xc3\xaa n\xc3\xa3o se sente bem fazendo travessuras, procure Rudy, na Rid\xc3\xadquilhas, para ganhar uma gostosura! ',
    'Talvez eu me vista de pirata no pr\xc3\xb3ximo Halloween!',
    'Se voc\xc3\xaa n\xc3\xa3o se sente bem fazendo travessuras, procure Rudy, na Rid\xc3\xadquilhas, para ganhar uma gostosura! ',
    'Minhas gostosuras preferidas s\xc3\xa3o as estrelas-do-mar!',
    'Se voc\xc3\xaa n\xc3\xa3o se sente bem fazendo travessuras, procure Rudy, na Rid\xc3\xadquilhas, para ganhar uma gostosura! ',
    'Vou levar voc\xc3\xaa para pedir gostosuras pelo porto!',
    'Se voc\xc3\xaa n\xc3\xa3o se sente bem fazendo travessuras, procure Rudy, na Rid\xc3\xadquilhas, para ganhar uma gostosura! ',
    'Espero que essas aranhas continuem nas \xc3\xa1rvores!',
    'Se voc\xc3\xaa n\xc3\xa3o se sente bem fazendo travessuras, procure Rudy, na Rid\xc3\xadquilhas, para ganhar uma gostosura! ',
    'Por que os fantasmas n\xc3\xa3o se afogam? Porque eles usam boia!',
    'Se voc\xc3\xaa n\xc3\xa3o se sente bem fazendo travessuras, procure Rudy, na Rid\xc3\xadquilhas, para ganhar uma gostosura! ',
    'Espero que voc\xc3\xaa esteja gostando da nossa divers\xc3\xa3o de Halloween!'], [
    'Vamos partir para levar alguns sustos!',
    'Boa-assombra\xc3\xa7\xc3\xa3o!',
    'Vou dar uma olhada nas decora\xc3\xa7\xc3\xb5es assustadoras de Halloween.'])
ValentinesDonaldChatter = ([
    'Ol\xc3\xa1, eu sou o Donald!',
    'Feliz Dia dos namorados!',
    'Feliz Dia dos namorados,  %!'], [
    'Eu deveria levar a Margarida para algum lugar no Dia dos namorados?\xe2\x80\x9d',
    'S\xc3\xb3 mais uma volta no cais e eu pegarei alguma coisa para a Margarida.',
    'O que a Margarida gostaria de ganhar no Dia dos namorados?',
    'Aqueles cora\xc3\xa7\xc3\xb5es na \xc3\xa1gua s\xc3\xa3o bons para melhorar o Laff!',
    'D\xc3\xaa uma festa no Dia dos namorados!',
    'Mostre aos Cogs, com uma torta na cara, que voc\xc3\xaa os ama!',
    'Eu preciso pegar um Amore Eel para a Margarida!'], [
    'Aloha!',
    'Mande minhas lembran\xc3\xa7as aos Cogs!'])
WinterDonaldCChatter = ([
    'Bem-vindo \xc3\xa0 Parada de Barcos e Tren\xc3\xb3s do Donald!',
    'Todos a bordo para o cruzeiro das Festas!',
    'Boas-Festas!',
    'Boas-Festas, %!'], [
    'Ouvi dizer que Bob Botinho, da Presentes Golfinho Fofinho, d\xc3\xa1 um presente para aquele que tiver uma can\xc3\xa7\xc3\xa3o!',
    'Voc\xc3\xaa gostou da decora\xc3\xa7\xc3\xa3o de patinhos?',
    'Ouvi dizer que Bob Botinho, da Presentes Golfinho Fofinho, d\xc3\xa1 um presente para aquele que tiver uma can\xc3\xa7\xc3\xa3o!',
    'Por que h\xc3\xa1 neve nos postes?',
    'Ouvi dizer que Bob Botinho, da Presentes Golfinho Fofinho, d\xc3\xa1 um presente para aquele que tiver uma can\xc3\xa7\xc3\xa3o!',
    '\xc3\x89 bom que esta \xc3\xa1gua n\xc3\xa3o congele!',
    'Ouvi dizer que Bob Botinho, da Presentes Golfinho Fofinho, d\xc3\xa1 um presente para aquele que tiver uma can\xc3\xa7\xc3\xa3o!',
    'Como eles acenderam as luzes nessas \xc3\xa1rvores?',
    'Ouvi dizer que Bob Botinho, da Presentes Golfinho Fofinho, d\xc3\xa1 um presente para aquele que tiver uma can\xc3\xa7\xc3\xa3o!',
    'Ser\xc3\xa1 que este barco \xc3\xa9 melhor do que um tren\xc3\xb3?',
    'Ouvi dizer que Bob Botinho, da Presentes Golfinho Fofinho, d\xc3\xa1 um presente para aquele que tiver uma can\xc3\xa7\xc3\xa3o!',
    'Este barco n\xc3\xa3o precisa ser puxado por renas!',
    'Ouvi dizer que Bob Botinho, da Presentes Golfinho Fofinho, d\xc3\xa1 um presente para aquele que tiver uma can\xc3\xa7\xc3\xa3o!',
    'Fico feliz por n\xc3\xa3o ser um peru nesta \xc3\xa9poca do ano!',
    'Ouvi dizer que Bob Botinho, da Presentes Golfinho Fofinho, d\xc3\xa1 um presente para aquele que tiver uma can\xc3\xa7\xc3\xa3o!',
    'Meu presente para voc\xc3\xaa? Passeios de barco gr\xc3\xa1tis!',
    'Ouvi dizer que Bob Botinho, da Presentes Golfinho Fofinho, d\xc3\xa1 um presente para aquele que tiver uma can\xc3\xa7\xc3\xa3o!',
    'Espero que eu n\xc3\xa3o ganhe carv\xc3\xa3o de novo!',
    'Ouvi dizer que Bob Botinho, da Presentes Golfinho Fofinho, d\xc3\xa1 um presente para aquele que tiver uma can\xc3\xa7\xc3\xa3o!'], [
    'Todos a bordo para come\xc3\xa7ar a divers\xc3\xa3o das Festas!',
    'Lembre-se de dar uma gorjeta para o capit\xc3\xa3o do barco!',
    'Aproveite as Festas!'])
WinterDonaldDChatter = ([
    'Bem-vindo \xc3\xa0 Parada de Barcos e Tren\xc3\xb3s do Donald!',
    'Todos a bordo para o cruzeiro das Festas!',
    'Boas-Festas!',
    'Boas-Festas, %!'], [
    'Voc\xc3\xaa gostou da decora\xc3\xa7\xc3\xa3o de patinhos?',
    'Por que h\xc3\xa1 neve nos postes?',
    '\xc3\x89 bom que esta \xc3\xa1gua n\xc3\xa3o congele!',
    'Como eles acenderam as luzes nessas \xc3\xa1rvores?',
    'Ser\xc3\xa1 que este barco \xc3\xa9 melhor do que um tren\xc3\xb3?',
    'Este barco n\xc3\xa3o precisa ser puxado por renas!',
    'Fico feliz por n\xc3\xa3o ser um peru nesta \xc3\xa9poca do ano!',
    'Meu presente para voc\xc3\xaa? Passeios de barco gr\xc3\xa1tis!',
    'Espero que eu n\xc3\xa3o ganhe carv\xc3\xa3o de novo!'], [
    'Todos a bordo para come\xc3\xa7ar a divers\xc3\xa3o das Festas!',
    'Lembre-se de dar uma gorjeta para o capit\xc3\xa3o do barco!',
    'Aproveite as Festas!'])
WesternPlutoChatter = ([
    'Bu! N\xc3\xa3o se assuste, sou eu... Pluto!',
    'Feliz Halloween, parceiro!',
    'Feliz Halloween, %!'], [
    'Fred Cavanhaque, da N\xc3\xa3o H\xc3\xa1 Lugar como o Lar, troca gostosuras por travessuras, pois isso o faz se Neve \xc3\xa9 Doce Neve.',
    'Eu troco travessuras por gostosuras!',
    'Fred Cavanhaque, da N\xc3\xa3o H\xc3\xa1 Lugar como o Lar, troca gostosuras por travessuras, pois isso o faz se Neve \xc3\xa9 Doce Neve.',
    'Mickey vai me levar para pedir gostosuras mais tarde!',
    'Fred Cavanhaque, da N\xc3\xa3o H\xc3\xa1 Lugar como o Lar, troca gostosuras por travessuras, pois isso o faz se Neve \xc3\xa9 Doce Neve.',
    'Estou me sentindo mais nas Festas do que no Halloween!',
    'Fred Cavanhaque, da N\xc3\xa3o H\xc3\xa1 Lugar como o Lar, troca gostosuras por travessuras, pois isso o faz se Neve \xc3\xa9 Doce Neve.',
    'Auau! Esse \xc3\xa9 o jeito canino de pedir gostosuras!',
    'Fred Cavanhaque, da N\xc3\xa3o H\xc3\xa1 Lugar como o Lar, troca gostosuras por travessuras, pois isso o faz se Neve \xc3\xa9 Doce Neve.',
    'Espero que voc\xc3\xaa esteja gostando da nossa divers\xc3\xa3o de Halloween!',
    'Fred Cavanhaque, da N\xc3\xa3o H\xc3\xa1 Lugar como o Lar, troca gostosuras por travessuras, pois isso o faz se Neve \xc3\xa9 Doce Neve.',
    'Gosto de perseguir gatos pretos!'], [
    'Agora vou desenterrar uma gostosura!',
    'Vou procurar Mickey e ver se ele tem alguma gostosura!',
    'Vou assustar o Donald!'])
WinterPlutoCChatter = ([
    'Ol\xc3\xa1, eu sou o Pluto!',
    'Bem-vindo a Brrr. Aqui \xc3\xa9 frio o ano inteiro!',
    'Boas-Festas!',
    'Boas-Festas, %'], [
    'Abr\xc3\xa3o o Abomin\xc3\xa1vel adoraria uma can\xc3\xa7\xc3\xa3o, pois a Terra do Homem de Neve \xc3\xa9 um lugar solit\xc3\xa1rio para um p\xc3\xa9-grande.',
    'Eu mordi um picol\xc3\xa9 e fiquei com dor de cabe\xc3\xa7a!',
    'Abr\xc3\xa3o o Abomin\xc3\xa1vel adoraria uma can\xc3\xa7\xc3\xa3o, pois a Terra do Homem de Neve \xc3\xa9 um lugar solit\xc3\xa1rio para um p\xc3\xa9-grande.',
    '\xc3\x89 como viver em um globo de neve!',
    'Abr\xc3\xa3o o Abomin\xc3\xa1vel adoraria uma can\xc3\xa7\xc3\xa3o, pois a Terra do Homem de Neve \xc3\xa9 um lugar solit\xc3\xa1rio para um p\xc3\xa9-grande.',
    'Queria estar ao lado de uma boa fogueira!',
    'Abr\xc3\xa3o o Abomin\xc3\xa1vel adoraria uma can\xc3\xa7\xc3\xa3o, pois a Terra do Homem de Neve \xc3\xa9 um lugar solit\xc3\xa1rio para um p\xc3\xa9-grande.',
    'Au! Au! Eu preciso de um cachecol!',
    'Abr\xc3\xa3o o Abomin\xc3\xa1vel adoraria uma can\xc3\xa7\xc3\xa3o, pois a Terra do Homem de Neve \xc3\xa9 um lugar solit\xc3\xa1rio para um p\xc3\xa9-grande.',
    'Pelo menos meu focinho n\xc3\xa3o est\xc3\xa1 vermelho e brilhando!'], [
    'Divirta-se muito durante as Festas!',
    'Volte sempre que voc\xc3\xaa quiser ver neve!',
    'Mickey vai me levar para cantar can\xc3\xa7\xc3\xb5es de natal!'])
WinterPlutoDChatter = ([
    'Ol\xc3\xa1, eu sou o Pluto!',
    'Bem-vindo a Brrr. Aqui \xc3\xa9 frio o ano inteiro!',
    'Boas-Festas!',
    'Boas-Festas, %'], [
    'Eu mordi um picol\xc3\xa9 e fiquei com dor de cabe\xc3\xa7a!',
    '\xc3\x89 como viver em um globo de neve!',
    'Queria estar ao lado de uma boa fogueira!',
    'Au! Au! Eu preciso de um cachecol!',
    'Pelo menos meu focinho n\xc3\xa3o est\xc3\xa1 vermelho e brilhando!'], [
    'Divirta-se muito durante as Festas!',
    'Volte sempre que voc\xc3\xaa quiser ver neve!',
    'Mickey vai me levar para cantar can\xc3\xa7\xc3\xb5es de natal!'])
AFMickeyChatter = ([
    'Feliz Semana Abril Toons!',
    'Feliz Semana Abril Toons, %!'], [
    'Bem-vindo aos Jardins! Eu sou a ' + Daisy + '!',
    'Eu sou a ' + Daisy + ' e amo o jardim!',
    'A Semana Abril Toons \xc3\xa9 a mais boba do ano!',
    'O qu\xc3\xaa? Voc\xc3\xaa nunca viu um pato com orelhas de rato?',
    'Ol\xc3\xa1, eu sou a ' + Daisy + '! Quac!',
    'Este barulho \xc3\xa9 igual ao do pato!',
    'Parece que hoje eu estou diferente!',
    'Voc\xc3\xaa j\xc3\xa1 escutou o seu Doodle falar?A Gravidade tirou f\xc3\xa9rias!'], [
    'Tenha uma Louca Semana Abril Toons!',
    'Diga oi ao Mickey por mim!'])
AFMinnieChatter = ([
    'Feliz Semana Abril Toons!',
    'Feliz Semana Abril Toons, %!'], [
    'Bem-vindo a ' + lTheBrrrgh + '! Eu sou o ' + Pluto + '!',
    'Ol\xc3\xa1, eu sou o ' + Pluto + '! Qual \xc3\xa9 o seu nome?',
    'O qu\xc3\xaa? Voc\xc3\xaa nunca viu um cachorro com orelhas de rato?',
    'Parece que hoje eu estou diferente!',
    'Algu\xc3\xa9m tem biscoito para cachorro? Estou com fome!Au au! Meu nome \xc3\xa9 ' + Pluto + '!',
    'Isto n\xc3\xa3o \xc3\xa9 bobo?',
    'N\xc3\xa3o me fa\xc3\xa7a ca\xc3\xa7ar voc\xc3\xaa!',
    'A Semana Abril Toons \xc3\xa9 a mais boba do ano!',
    'Voc\xc3\xaa j\xc3\xa1 escutou o seu Doodle falar?',
    'A Gravidade tirou f\xc3\xa9rias!'], [
    'Tenha uma Louca Semana Abril Toons!',
    'Eu tenho que correr atr\xc3\xa1s dos carros, agora! Tchau!'])
AFDaisyChatter = ([
    'Feliz Semana Abril Toons!',
    'Feliz Semana Abril Toons, %!'], [
    'Bem-vindo a ' + lToontownCentral + '! Eu sou ' + Mickey + ' Mouse!',
    'Ol\xc3\xa1, eu sou o ' + Mickey + '! O rato mais feliz de Toontown!',
    'Se voc\xc3\xaa vir ' + Daisy + ', diga a ela ' + Mickey + ' que eu falei oi!',
    'O qu\xc3\xaa? Voc\xc3\xaa nunca viu um rato com penas?',
    'Isto n\xc3\xa3o \xc3\xa9 bobo?',
    'Parece que hoje eu estou diferente!',
    'A Semana Abril Toons \xc3\xa9 a mais boba do ano!',
    'Voc\xc3\xaa j\xc3\xa1 escutou o seu Doodle falar?',
    'A Gravidade tirou f\xc3\xa9rias!'], [
    'Tchau! Diga a eles ' + Mickey + ' enviou para voc\xc3\xaa!',
    'Se voc\xc3\xaa for aos ' + lDaisyGardens + ', diga ol\xc3\xa1 a ela por mim!'])
AFGoofySpeedwayChatter = ([
    'Feliz Semana Abril Toons!',
    'Feliz Semana Abril Toons, %!'], [
    'Bem-vindo \xc3\xa0 Terra dos Sonhos! Eu sou o ' + Donald + '!',
    'Ol\xc3\xa1, eu sou o ' + Donald + '! Ainda n\xc3\xa3o \xc3\xa9 a hora da soneca?',
    'Sabe, um pato precisa do seu sono de beleza!',
    'O qu\xc3\xaa? Voc\xc3\xaa nunca viu um pato com orelhas de cachorro?',
    'Puxa! Quero dizer, Quac!',
    'Esta seria uma \xc3\xb3tima pista de corrida... ou melhor, um lugar para tirar uma soneca!',
    'Parece que hoje eu estou diferente!',
    'A Semana Abril Toons \xc3\xa9 a mais boba do ano!',
    'Voc\xc3\xaa j\xc3\xa1 escutou o seu Doodle falar?',
    'A Gravidade tirou f\xc3\xa9rias!'], [
    'Se voc\xc3\xaa vir ' + Goofy + ', diga a ele ' + Donald + ' que eu mandei um oi!',
    'Tchau e boa-noite!'])
AFDonaldChatter = ([
    'Feliz Semana Abril Toons!',
    'Feliz Semana Abril Toons, %!'], [
    'Bem-vindo ao Circuito! Eu sou o ' + Goofy + '!',
    'Eu sou o' + Goofy + ' e estou sonhando que eu sou o' + Donald + '!',
    'Eu j\xc3\xa1 ouvi falar que son\xc3\xa2mbulos andam... mas dirigir??',
    'Puxa!  Que bobinho, digo, docinho' + Goofy + '!',
    'Como eu posso ver as corridas com meus olhos fechados?',
    '\xc3\x89 melhor eu tirar uma soneca antes da minha pr\xc3\xb3xima corrida!',
    'A Semana Abril Toons \xc3\xa9 a mais boba do ano!',
    'Parece que hoje eu estou diferente!',
    'Voc\xc3\xaa j\xc3\xa1 escutou o seu Doodle falar?',
    'A Gravidade tirou f\xc3\xa9rias!'], [
    'Tenha uma Louca Semana Abril Toons!',
    'Preciso trabalhar no meu kart!  Tchau!'])
AFDonaldDockChatter = ([
    'Feliz Semana Abril Toons!',
    'Feliz Semana Abril Toons, %!'], [
    'Todo mundo folga na Semana Abril Toons, menos eu!',
    'Eu sou o \xc3\xbanico que tem de trabalhar nesta semana!',
    'Eu s\xc3\xb3 descanso quando durmo!',
    'Todos os meus amigos est\xc3\xa3o fingindo ser outras pessoas!',
    'Rodando e rodando neste barco, o dia todo!',
    'Eu ouvi dizer que Margarida est\xc3\xa1 fingindo ser o Mickey!',
    'Estamos na semana mais boba do ano e eu a estou perdendo!',
    'Voc\xc3\xaa j\xc3\xa1 escutou o seu Doodle falar?',
    'A Gravidade tirou f\xc3\xa9rias!'], [
    'Tenha uma Louca Semana Abril Toons!',
    'Pregue uma pe\xc3\xa7a nos Cogs por mim!'])
AFPlutoChatter = ([
    'Feliz Semana Abril Toons!',
    'Feliz Semana Abril Toons, %!'], [
    'Bem-vindo \xc3\xa0 Terra da Melodia!  Eu sou a ' + Minnie + '!',
    'Oi, meu nome \xc3\xa9 ' + Minnie + ' Mouse!',
    'Eu s\xc3\xa3o t\xc3\xa3o feliz quanto uma ratinha pode ser!',
    'O qu\xc3\xaa? Voc\xc3\xaa nunca viu uma ratinha com orelhas de cachorro?',
    'Eu adoro quando ' + Mickey + ' e eu sa\xc3\xadmos para passear!',
    'O qu\xc3\xaa? Voc\xc3\xaa nunca ouviu um rato falar antes?',
    'A Semana Abril Toons \xc3\xa9 a mais boba do ano!',
    'Voc\xc3\xaa j\xc3\xa1 escutou o seu Doodle falar?',
    'A Gravidade tirou f\xc3\xa9rias!'], [
    'Tenha uma Louca Semana Abril Toons!',
    'Se voc\xc3\xaa vir ' + Pluto + ', diga a ele ' + Minnie + ' que eu mandei um oi!'])
AFChipChatter = ([
    'Feliz Semana Abril Toons!',
    'Feliz Semana Abril Toons, %!'], [
    'Oi, eu sou o ' + Dale + '!',
    'Como voc\xc3\xaa est\xc3\xa1, ' + Chip + '?',
    'Eu sempre achei que voc\xc3\xaa era ' + Dale + ', ' + Chip + '.',
    'Tem certeza de que voc\xc3\xaa \xc3\xa9 o ' + Chip + ' e n\xc3\xa3o o ' + Dale + ', ' + Chip + '?',
    'A Semana de Abril dos Toons \xc3\xa9 a mais boba do ano!'], [
    'Tchau de ' + Chip + ' e ' + Dale + '!'])
AFDaleChatter = ([
    'Feliz Semana Abril Toons!',
    'Feliz Semana Abril Toons, %!'], [
    'Oi, eu sou ' + Chip + '!',
    'Muito bem, ' + Dale + ' ... obrigado!',
    ' N\xc3\xa3o, eu sou o' + Chip + ', ' + Dale + '.',
    'Sim, ' + Dale + ' , eu sou o' + Chip + ', e n\xc3\xa3o o ' + Dale + '.',
    'Certamente, ' + Chip + '! Quero dizer, ' + Dale + '.'], [
    'Ou ' + Dale + ' e ' + Chip + '!'])
CLGoofySpeedwayChatter = ([
    'Bem-vindo ao ' + lGoofySpeedway + '.',
    'Oi, meu nome \xc3\xa9 ' + Goofy + '. Qual \xc3\xa9 o seu?',
    'Ohoh, que bom ver voc\xc3\xaa %!',
    'Ol\xc3\xa1!  Perdoe minhas roupas sujas, estava consertando aquele Quadro de Pontua\xc3\xa7\xc3\xa3o quebrado.'], [
    '\xc3\x89 bom que o Quadro de Pontua\xc3\xa7\xc3\xa3o esteja funcionando logo, pois o Fim de Semana do Grande Pr\xc3\xaamio est\xc3\xa1 chegando!',
    'Algu\xc3\xa9m quer comprar um kart meio usado? Ele j\xc3\xa1 apareceu no Quadro de Pontua\xc3\xa7\xc3\xa3o!',
    'O Fim de Semana do Grande do Pr\xc3\xaamio est\xc3\xa1 chegando, \xc3\xa9 melhor come\xc3\xa7ar a treinar.',
    'O Fim de Semana do Grande Pr\xc3\xaamio ser\xc3\xa1 de sexta-feira, 22, a segunda-feira, 25 de maio!',
    'Preciso de uma escada para descer aquele kart.',
    'Aquele Toon realmente queria aparecer no Quadro de Pontua\xc3\xa7\xc3\xa3o!',
    'Cara, acabei de ver uma corrida terr\xc3\xadvel.',
    'Cuidado com as cascas de banana na pista!',
    'Voc\xc3\xaa fez algumas melhorias em seu kart ultimamente?',
    'Precisamos adquirir alguns aros novos na loja de kart.',
    'Ei, voc\xc3\xaa viu o ' + Donald + '?',
    'Se vir o meu amigo ' + Mickey + ', mande lembran\xc3\xa7as a ele por mim.',
    'Puxa! Esqueci de preparar o caf\xc3\xa9 da manh\xc3\xa3 do ' + Mickey + '!',
    'Ohoh, tem um monte de ' + Cogs + ' perto do ' + lDonaldsDock + '.',
    'Nos galhos do Brrrgh da minha Loja de Brincadeiras, os \xc3\x93culos Hipnotizantes est\xc3\xa3o \xc3\xa0 venda por apenas 1 balinha!',
    'A Loja de Piadas do Pateta tem as melhores piadas, truques e brincadeiras divertidas de toda Toontown!',
    'Na Loja de Piadas do Pateta, at\xc3\xa9 uma torta na cara \xc3\xa9 garantia de boas risadas ou voc\xc3\xaa recebe suas balinhas de volta!'], [
    '\xc3\x89 bom eu fazer uma nova pintura no meu kart antes do Fim de Semana do Grande Pr\xc3\xaamio.',
    'Caramba, \xc3\xa9 melhor eu dar um jeito nesse Quadro de Pontua\xc3\xa7\xc3\xa3o quebrado!',
    'Espero ver todos voc\xc3\xaas no Fim de Semana do Grande Pr\xc3\xaamio!  Adeus!',
    '\xc3\x89 hora de dar uma cochilada. Vou para a Sonhol\xc3\xa2ndia sonhar com a vit\xc3\xb3ria no Grande Pr\xc3\xaamio.'])
GPGoofySpeedwayChatter = ([
    'Bem-vindo ao ' + lGoofySpeedway + '.',
    'Bem-vindo ao Fim de Semana do Grande Pr\xc3\xaamio!',
    'Oi, meu nome \xc3\xa9 ' + Goofy + '. Qual \xc3\xa9 o seu?',
    'Ohoh, que bom ver voc\xc3\xaa %!'], [
    'Voc\xc3\xaa est\xc3\xa1 na expectativa do Fim de Semana do Grande Pr\xc3\xaamio?',
    'A boa not\xc3\xadcia \xc3\xa9 que o Quadro de Pontua\xc3\xa7\xc3\xa3o est\xc3\xa1 pronto.',
    'Conseguimos consertar o Quadro de Pontua\xc3\xa7\xc3\xa3o bem na hora do Fim de Semana do Grande Pr\xc3\xaamio!',
    'Nunca encontramos aquele Toon!',
    'Cara, acabei de ver uma corrida terr\xc3\xadvel.',
    'Cuidado com as cascas de banana na pista!',
    'Voc\xc3\xaa fez algumas melhorias em seu kart ultimamente?',
    'Precisamos comprar alguns aros novos na loja de kart.',
    'Ohoh, voc\xc3\xaa viu o ' + Donald + '? Ele disse que estava vindo para o Grande Pr\xc3\xaamio!',
    'Se vir o meu amigo ' + Mickey + ', diga a ele que est\xc3\xa1 perdendo uma corrida incr\xc3\xadvel!',
    'Puxa! Esqueci de preparar o caf\xc3\xa9 da manh\xc3\xa3 do ' + Mickey + '!',
    'Ohoh, tem um monte de ' + Cogs + ' perto do ' + lDonaldsDock + '.',
    'Nos galhos do Brrrgh da minha Loja de Brincadeiras, os \xc3\x93culos Hipnotizantes est\xc3\xa3o \xc3\xa0 venda por apenas 1 balinha!',
    'A Loja de Piadas do Pateta tem as melhores piadas, truques e brincadeiras divertidas de toda Toontown!',
    'Na Loja de Piadas do Pateta, at\xc3\xa9 uma torta na cara \xc3\xa9 garantia de boas risadas ou voc\xc3\xaa recebe suas balinhas de volta!'], [
    'Boa sorte no Grande Pr\xc3\xaamio!',
    'Vou participar da pr\xc3\xb3xima corrida do Grande Pr\xc3\xaamio!',
    'Ohoh, acho que a pr\xc3\xb3xima corrida j\xc3\xa1 vai come\xc3\xa7ar!',
    'Puxa, \xc3\xa9 melhor verificar o novo Quadro de Pontua\xc3\xa7\xc3\xa3o e garantir que esteja funcionando bem!'])
SillyPhase1Chatter = [
    'Se n\xc3\xa3o viu o Medidor de Bobagens, v\xc3\xa1 para o Sal\xc3\xa3o de Desenhos!',
    'Toontown fica bobinha durante o dia!',
    'Porque as ondas de bobagem na batalha aumentam o n\xc3\xadvel de bobagem de Toontown!',
    'Os objetos da rua est\xc3\xa3o come\xc3\xa7ando a ganhar vida!',
    'Eu vi um hidrante se movendo na Rua da Bobagem!']
SillyPhase2Chatter = [
    'O N\xc3\xadvel de Bobagem continua subindo!',
    'O Medidor de Bobagens subiu demais e pirou!',
    'Algu\xc3\xa9m viu uma lixeira se movendo na Rua do Bordo!',
    'Muitos hidrantes na Rua da Bobagem ganharam vida!',
    'Uma caixa de correio na Travessa do Farol endoidou!',
    'V\xc3\xa1 ver o Medidor de Bobagens no Sal\xc3\xa3o de Desenhos!',
    'Continue causando aquelas ondas de bobagem!']
SillyPhase3Chatter = [
    'Os Cogs odiaram o fato de Toontown ter se tornado t\xc3\xa3o boba!',
    'Fique de olhos abertos para Invas\xc3\xb5es de Cogs!',
    'As Invas\xc3\xb5es de Cogs baixaram o n\xc3\xadvel de bobagem!',
    'O Medidor de Bobagens caiu ap\xc3\xb3s as Invas\xc3\xb5es de Cogs!',
    'Agora todas as ruas de Toontown t\xc3\xaam objetos animados!',
    'Toontown est\xc3\xa1 mais bobinha do que nunca!']
SillyPhase4Chatter = [
    'Os hidrantes tornam seus Itens de Esguicho mais eficazes!',
    'As caixas de correio fornecem um aperfei\xc3\xa7oamento especial aos seus Itens de Arremesso!',
    'Aquelas Lixeiras doidas podem dar a voc\xc3\xaa um Toon-up!',
    'Os objetos da rua podem lhe ajudar na batalha!',
    'Eu sei que vamos recuperar o Medidor de Bobagens logo!',
    'Aproveite a Toontown bobinha!']
for chatter in [
    MickeyChatter,
    DonaldChatter,
    MinnieChatter,
    GoofyChatter]:
    chatter[0].extend(SharedChatterGreetings)
    chatter[1].extend(SharedChatterComments)
    chatter[2].extend(SharedChatterGoodbyes)

BoringTopic = 'Boring'
EmceeDialoguePhase1Topic = 'EmceeDialoguePhase1'
EmceeDialoguePhase2Topic = 'EmceeDialoguePhase2'
EmceeDialoguePhase3Topic = 'EmceeDialoguePhase3'
EmceeDialoguePhase3_5Topic = 'EmceeDialoguePhase3.5'
EmceeDialoguePhase4Topic = 'EmceeDialoguePhase4'
EmceeDialoguePhase5Topic = 'EmceeDialoguePhase5'
EmceeDialoguePhase6Topic = 'EmceeDialoguePhase6'
toontownDialogues = {
    BoringTopic: {
        (1, 2018): [
            'Ol\xc3\xa1 Albert',
            'Parece que o n\xc3\xadvel de bobagem est\xc3\xa1 subindo',
            ' Sim, e se n\xc3\xa3o esque\xc3\xa7a dos April Toons!'],
        (2, 2019): [
            'Ol\xc3\xa1 Newton',
            'Gostaria de saber o quanto os grupos contribu\xc3\xadram para isso '],
        (3, 2020): [
            'Para que cumprimentar Albert e Newton',
            'O Halloween foi bem bobinho tamb\xc3\xa9m!'] },
    EmceeDialoguePhase1Topic: {
        (1, 2020): [
            'Amigos Toons, este \xc3\xa9 o Medidor de Bobagens!',
            'Ele registra a varia\xc3\xa7\xc3\xa3o do n\xc3\xadvel de bobagem de Toontown...',
            'Que est\xc3\xa1 causando a anima\xc3\xa7\xc3\xa3o dos objetos da rua!',
            'E VOC\xc3\x8a pode ajudar a aumentar esses n\xc3\xadveis!',
            'Lute com os Cogs para causar Ondas de Bobagem...',
            'Deixe Toontown mais bobinha do que nunca...',
            'E vamos observar o mundo ganhando vida!',
            'Agora vou repetir o que disse, s\xc3\xb3 mais uma vez.'] },
    EmceeDialoguePhase2Topic: {
        (1, 2020): [
            'Bom trabalho, Toons!',
            'Voc\xc3\xaas mantiveram aqueles n\xc3\xadveis em alta...',
            'E Toontown fica mais bobinha a cada dia que passa!',
            'Hidrantes, lixeiras e caixas de correio est\xc3\xa3o adquirindo vida...',
            'Deixando o mundo mais animado do que nunca!',
            'Voc\xc3\xaa sabe que os Cogs n\xc3\xa3o ficam felizes com isso...',
            'Mas com certeza os Toons est\xc3\xa3o!'] },
    EmceeDialoguePhase3Topic: {
        (1, 2020): [
            'Caramba! O Medidor de Bobagens est\xc3\xa1 ainda mais doido do que se esperava!',
            'Suas Ondas de Bobagem est\xc3\xa3o fazendo maravilhas...',
            'E Toontown fica mais animada a cada dia que passa!',
            'Continue fazendo um bom trabalho...',
            'E vejamos o qu\xc3\xa3o bobinha Toontown pode ficar!',
            'Voc\xc3\xaa sabe que os Cogs n\xc3\xa3o est\xc3\xa3o felizes com o que est\xc3\xa1 acontecendo...',
            'Mas com certeza os Toons est\xc3\xa3o!'] },
    EmceeDialoguePhase3_5Topic: {
        (1, 2020): [
            'VOC\xc3\x8aS CONSEGUIRAM, TOONS!',
            'Toontown est\xc3\xa1 cheia de vida! ',
            'As ruas est\xc3\xa3o repletas de bobagens!',
            'V\xc3\xa1 ver por si mesmo!'] },
    EmceeDialoguePhase4Topic: {
        (1, 2020): [
            'Aten\xc3\xa7\xc3\xa3o Toons!',
            'As s\xc3\xbabitas invas\xc3\xb5es de Cogs foram lastim\xc3\xa1veis.',
            'Como resultado, o n\xc3\xadvel de bobagem caiu drasticamente...',
            'E mais nenhum novo objeto ganhou vida.',
            'Mas os que ganharam est\xc3\xa3o muito agradecidos... ',
            'Ent\xc3\xa3o, talvez eles achem um jeito de mostrar sua gratid\xc3\xa3o!',
            'Fiquem Antenados!'] },
    EmceeDialoguePhase5Topic: {
        (1, 2020): [
            'Aten\xc3\xa7\xc3\xa3o Toons!',
            'As invas\xc3\xb5es de Cogs foram lastim\xc3\xa1veis.',
            'Como resultado, o n\xc3\xadvel de bobagem caiu drasticamente...',
            'E mais nenhum novo objeto ganhou vida.',
            'Mas os que ganharam est\xc3\xa3o muito agradecidos... ',
            'E est\xc3\xa3o demonstrando sua gratid\xc3\xa3o ajudando na batalha!',
            'J\xc3\xa1 podemos repelir os Cogs, portanto, continuem lutando!'] },
    EmceeDialoguePhase6Topic: {
        (1, 2020): [
            'Parab\xc3\xa9ns Toons!',
            'Voc\xc3\xaas eliminaram com sucesso as Invas\xc3\xb5es de Cogs...',
            'Com uma ajudinha de nossos novos amigos animados...',
            'E deixaram novamente Toontown t\xc3\xa3o bobinha como sempre!',
            'Esperamos que o Medidor de Bobagens volte a subir em breve...',
            'Enquanto isso, continuem enfrentando os Cogs...',
            'E aproveitem o lugar mais bobinho de todos, Toontown!'] } }
FriendsListPanelNewFriend = 'Novo amigo'
FriendsListPanelSecrets = 'Segredos'
FriendsListPanelOnlineFriends = 'AMIGOS\nON-LINE'
FriendsListPanelAllFriends = 'TODOS\nOS AMIGOS'
FriendsListPanelIgnoredFriends = 'TOONS\nIGNORADOS'
FriendsListPanelPets = 'BICHINHOS\nPR\xc3\x93XIMOS'
FriendsListPanelPlayers = 'TODOS OS AMIGOS\nDO JOGADOR'
FriendsListPanelOnlinePlayers = 'AMIGOS ONLINE\nDO JOGADOR'
FriendInviterClickToon = 'Clique no Toon com o qual voc\xc3\xaa quer fazer amizade.\n\n(Voc\xc3\xaa tem %s amigos)'
FriendInviterToon = 'Toon'
FriendInviterThatToon = 'Aquele Toon'
FriendInviterPlayer = 'Jogador'
FriendInviterThatPlayer = 'Aquele jogador'
FriendInviterBegin = 'Que tipo de amigo voc\xc3\xaa quer ter?'
FriendInviterToonFriendInfo = 'Um amigo somente em Toontown'
FriendInviterPlayerFriendInfo = 'Um amigo em toda a rede Disney.com'
FriendInviterToonTooMany = 'Voc\xc3\xaa tem amigos Toons demais para poder acrescentar um agora. Voc\xc3\xaa ter\xc3\xa1 de remover alguns amigos Toons se quiser fazer amizade com %s. Voc\xc3\xaa tamb\xc3\xa9m pode tentar fazer amizade com seu jogador.'
FriendInviterPlayerTooMany = 'Voc\xc3\xaa tem amigos jogadores demais para poder acrescentar um agora. Voc\xc3\xaa ter\xc3\xa1 de remover alguns amigos jogadores se quiser fazer amizade com %s. Voc\xc3\xaa tamb\xc3\xa9m pode tentar fazer amizade com seu Toon.'
FriendInviterToonAlready = '%s j\xc3\xa1 \xc3\xa9 seu amigo Toon.'
FriendInviterPlayerAlready = '%s j\xc3\xa1 \xc3\xa9 seu amigo jogador.'
FriendInviterStopBeingToonFriends = 'Romper amizade Toon'
FriendInviterStopBeingPlayerFriends = 'Romper amizade de jogador'
FriendInviterEndFriendshipToon = 'Tem certeza de que quer romper a amizade de Toon com %s?'
FriendInviterEndFriendshipPlayer = 'Tem certeza de que quer romper a amizade de jogador com %s?'
FriendInviterRemainToon = '\n(Voc\xc3\xaa vai continuar sendo amigo Toon de %s)'
FriendInviterRemainPlayer = '\n(Voc\xc3\xaa vai continuar sendo amigo jogador de %s)'
DownloadForceAcknowledgeVerbList = [
    'pintado',
    'desembalar',
    'desdobrado',
    'esticado',
    'inflado',
    'montar']
DownloadForceAcknowledgeMsg = 'Sinto muito, voc\xc3\xaa n\xc3\xa3o pode avan\xc3\xa7ar porque o download de %(phase)s est\xc3\xa1 apenas %(verb)s conclu\xc3\xaddo.\n\nTente novamente mais tarde.'
TeaserTop = ''
TeaserBottom = ''
TeaserDefault = ',\nVoc\xc3\xaa precisa ser um associado.\nUna-se!'
TeaserOtherHoods = 'Visite os 6 bairros exclusivos!'
TeaserTypeAName = 'Digite o seu nome favorito para o seu Toon!'
TeaserSixToons = 'Crie at\xc3\xa9 6 Toons em uma s\xc3\xb3 conta!'
TeaserClothing = 'Compre roupas exclusivas para personalizar o seu Toon!'
TeaserCogHQ = 'Infiltre-se nas\nperigosas \xc3\xa1reas avan\xc3\xa7adas dos Cogs!'
TeaserSecretChat = 'Troque segredos\ncom seus amigos conversando on-line com eles!'
TeaserSpecies = 'Crie e jogue com Toons Macacos, Cavalos e Ursos!'
TeaserFishing = 'Colecione todas as esp\xc3\xa9cies de peixes!'
TeaserGolf = 'Jogue em campos de golfe malucos!'
TeaserParties = ' Para planear Partes'
TeaserSubscribe = 'Assinar'
TeaserContinue = 'Continuar na vers\xc3\xa3o gratuita'
TeaserEmotions = 'Para fazer seu Toon mais expressivo'
TeaserKarting = 'Aposte corridas com outros Toons em karts maneiros!'
TeaserKartingAccessories = 'Personalize seu kart com acess\xc3\xb3rios incr\xc3\xadveis.'
TeaserGardening = 'Plante flores, construa est\xc3\xa1tuas e cultive \xc3\xa1rvores em seu terreno.'
TeaserHaveFun = 'Encontre mais divers\xc3\xa3o!'
TeaserJoinUs = 'Una-se!'
TeaserMinigames = TeaserOtherHoods
TeaserQuests = TeaserOtherHoods
TeaserOtherGags = TeaserOtherHoods
TeaserTricks = TeaserOtherHoods
DownloadWatcherUpdate = 'Fazendo download %s'
DownloadWatcherInitializing = 'Iniciando Download...'
LauncherPhaseNames = {
    0: 'Inicializa\xc3\xa7\xc3\xa3o',
    1: 'Panda',
    2: 'Motor',
    3: 'Fazer um Toon',
    3.5: 'Toontorial',
    4: 'Parque',
    5: 'Ruas',
    5.5: 'Estados',
    6: 'Bairros I',
    7: Cog + ' Edif\xc3\xadcios dos',
    8: 'Bairros II',
    9: Sellbot + ' Quartel dos',
    10: Cashbot + ' Quartel dos',
    11: Lawbot + ' Quartel dos',
    12: Bossbot + ' HQ',
    13: 'Festas' }
LauncherProgress = '%(name)s (%(current)s de %(total)s)'
LauncherStartingMessage = 'Iniciando Toontown On-line da Disney...'
LauncherDownloadFile = 'Fazendo download da atualiza\xc3\xa7\xc3\xa3o de ' + LauncherProgress + '...'
LauncherDownloadFileBytes = 'Fazendo download da atualiza\xc3\xa7\xc3\xa3o de ' + LauncherProgress + ': %(bytes)s'
LauncherDownloadFilePercent = 'Fazendo download da atualiza\xc3\xa7\xc3\xa3o de ' + LauncherProgress + ': %(percent)s%%'
LauncherDecompressingFile = 'Descompactando atualiza\xc3\xa7\xc3\xa3o de ' + LauncherProgress + '...'
LauncherDecompressingPercent = 'Descompactando atualiza\xc3\xa7\xc3\xa3o de ' + LauncherProgress + ': %(percent)s%%'
LauncherExtractingFile = 'Extraindo atualiza\xc3\xa7\xc3\xa3o de ' + LauncherProgress + '...'
LauncherExtractingPercent = 'Extraindo atualiza\xc3\xa7\xc3\xa3o de ' + LauncherProgress + ': %(percent)s%%'
LauncherPatchingFile = 'Aplicando atualiza\xc3\xa7\xc3\xa3o de ' + LauncherProgress + '...'
LauncherPatchingPercent = 'Aplicando atualiza\xc3\xa7\xc3\xa3o de ' + LauncherProgress + ': %(percent)s%%'
LauncherConnectProxyAttempt = 'Conectando-se a Toontown: %s (proxy: %s) tentativa: %s'
LauncherConnectAttempt = 'Conectando-se a Toontown: %s tentativa %s'
LauncherDownloadServerFileList = 'Atualizando Toontown...'
LauncherCreatingDownloadDb = 'Atualizando Toontown...'
LauncherDownloadClientFileList = 'Atualizando Toontown...'
LauncherFinishedDownloadDb = 'Atualizando Toontown...'
LauncherStartingGame = 'Iniciando Toontown...'
LauncherRecoverFiles = 'Atualizando Toontown. Recuperando arquivos...'
LauncherCheckUpdates = 'Verificando atualiza\xc3\xa7\xc3\xb5es de ' + LauncherProgress
LauncherVerifyPhase = 'Atualizando Toontown...'
LoadingDownloadWatcherUpdate = ' Carregando %s'
AvatarChoiceMakeAToon = 'Fazer um\nToon'
AvatarChoicePlayThisToon = 'Jogar com\neste Toon'
AvatarChoiceSubscribersOnly = 'Assinar\n\n\n\nAgora!'
AvatarChoiceDelete = 'Excluir'
AvatarChoiceDeleteConfirm = 'Isto far\xc3\xa1 que %s seja exclu\xc3\xaddo para sempre.'
AvatarChoiceNameRejected = 'Nome\nrejeitado'
AvatarChoiceNameApproved = 'Nome\naprovado!'
AvatarChoiceNameReview = 'Em\nrevis\xc3\xa3o'
AvatarChoiceNameYourToon = 'Dar um\nnome ao Toon!'
AvatarChoiceDeletePasswordText = 'Cuidado! Isto far\xc3\xa1 que %s seja exclu\xc3\xaddo para sempre. Para excluir este Toon, insira a sua senha.'
AvatarChoiceDeleteConfirmText = 'Cuidado! Isto excluir\xc3\xa1 %(name)s para sempre. Se voc\xc3\xaa tiver certeza de que \xc3\xa9 isso mesmo que deseja, digite "%(confirm)s" e clique em OK.'
AvatarChoiceDeleteConfirmUserTypes = 'excluir'
AvatarChoiceDeletePasswordTitle = 'Excluir Toon?'
AvatarChoicePassword = 'Senha'
AvatarChoiceDeletePasswordOK = lOK
AvatarChoiceDeletePasswordCancel = lCancel
AvatarChoiceDeleteWrongPassword = 'Esta senha n\xc3\xa3o parece ser a correta. Para excluir este Toon, insira a sua senha.'
AvatarChoiceDeleteWrongConfirm = 'Voc\xc3\xaa n\xc3\xa3o digitou corretamente. Para excluir %(name)s, digite "%(confirm)s" e clique em OK. N\xc3\xa3o digite as aspas. Clique em Cancelar se desistir.'
AvatarChooserPickAToon = 'Escolha um Toon para jogar'
AvatarChooserQuit = lQuit
DateOfBirthEntryMonths = [
    'Jan',
    'Fev',
    'Mar',
    'Abr',
    'Mai',
    'Jun',
    'Jul',
    'Ago',
    'Set',
    'Out',
    'Nov',
    'Dez']
DateOfBirthEntryDefaultLabel = 'Data de nascimento'
AchievePageTitle = 'Realiza\xc3\xa7\xc3\xb5es\n(em breve)'
PhotoPageTitle = 'Foto\n(em breve)'
BuildingPageTitle = 'Edif\xc3\xadcios\n(em breve)'
InventoryPageTitle = 'Piadas'
InventoryPageDeleteTitle = 'EXCLUIR PIADAS'
InventoryPageTrackFull = 'Voc\xc3\xaa possui todas as piadas do tipo %s.'
InventoryPagePluralPoints = 'Voc\xc3\xaa obter\xc3\xa1 uma nova piada de\n%(trackName)s quando\nganhar mais %(numPoints)s pontos de %(trackName)s.'
InventoryPageSinglePoint = 'Voc\xc3\xaa obter\xc3\xa1 uma nova piada de\n%(trackName)s quando\nganhar mais %(numPoints)s pontos de %(trackName)s.'
InventoryPageNoAccess = 'Voc\xc3\xaa ainda n\xc3\xa3o tem acesso ao tipo %s.'
NPCFriendPageTitle = 'SOS Toons'
PartyDateFormat = '%(mm)s %(dd)d, %(yyyy).4d'
PartyTimeFormat = '%d:%.2d %s'
PartyTimeFormatMeridiemAM = 'am'
PartyTimeFormatMeridiemPM = 'pm'
PartyCanStart = '\xc3\x89 Hora de Festejar! Clique em Iniciar Festa na sua p\xc3\xa1gina Hospedando do Livro de Brincadeiras!'
PartyHasStartedAcceptedInvite = '%s, a festa come\xc3\xa7ou!  Clique no anfitri\xc3\xa3o e em "Ir \xc3\xa0 Festa" na p\xc3\xa1gina Convites do Livro de Brincadeiras.'
PartyHasStartedNotAcceptedInvite = '%s, a festa come\xc3\xa7ou! Voc\xc3\xaa tamb\xc3\xa9m pode ir, teletransportando-se para o anfitri\xc3\xa3o.'
EventsPageName = 'Eventos'
EventsPageCalendarTabName = 'Calend\xc3\xa1rio'
EventsPageCalendarTabParty = 'Festa'
EventsPageToontownTimeIs = 'A HORA DE TOONTOWN \xc3\x89'
EventsPageConfirmCancel = 'Se cancelar, receber\xc3\xa1 uma devolu\xc3\xa7\xc3\xa3o de %d%%. Tem certeza de que quer cancelar sua festa?'
EventsPageCancelPartyResultOk = 'Sua festa foi cancelada e voc\xc3\xaa recebeu %d balinhas de volta!'
EventsPageCancelPartyResultError = 'Desculpe, sua festa n\xc3\xa3o foi cancelada.'
EventsPageTooLateToStart = 'Desculpe, tarde demais para come\xc3\xa7ar a sua festa. Voc\xc3\xaa pode cancel\xc3\xa1-la e planejar outra.'
EventsPagePublicPrivateChange = 'Alterando a sua configura\xc3\xa7\xc3\xa3o de privacidade de festa...'
EventsPagePublicPrivateNoGo = 'Desculpe, voc\xc3\xaa n\xc3\xa3o pode alterar a sua configura\xc3\xa7\xc3\xa3o de privacidade de festa agora.'
EventsPagePublicPrivateAlreadyStarted = 'Desculpe, a sua festa j\xc3\xa1 come\xc3\xa7ou, e voc\xc3\xaa n\xc3\xa3o pode alterar sua configura\xc3\xa7\xc3\xa3o de privacidade de festa.'
EventsPageHostTabName = 'Hospedando'
EventsPageHostTabTitle = 'Minha Pr\xc3\xb3xima Festa'
EventsPageHostTabTitleNoParties = 'Sem Festas'
EventsPageHostTabDateTimeLabel = 'Voc\xc3\xaa tem uma festa em %s \xc3\xa0s %s, Hora de Toontown.'
EventsPageHostingTabNoParty = 'V\xc3\xa1 ao Port\xc3\xa3o de Festa\nde um p\xc3\xa1tio para planejar\nsua festa!'
EventsPageHostTabPublicPrivateLabel = 'Esta festa \xc3\xa9:'
EventsPageHostTabToggleToPrivate = 'Particular'
EventsPageHostTabToggleToPublic = 'P\xc3\xbablica'
EventsPageHostingTabGuestListTitle = 'Convidados'
EventsPageHostingTabActivityListTitle = 'Atividades'
EventsPageHostingTabDecorationsListTitle = 'Decora\xc3\xa7\xc3\xb5es'
EventsPageHostingTabPartiesListTitle = 'Anfitri\xc3\xb5es'
EventsPageHostTabCancelButton = 'Cancelar Festa'
EventsPageGoButton = 'Iniciar\nFesta!'
EventsPageGoBackButton = 'Festa\nJ\xc3\xa1!'
EventsPageInviteGoButton = 'Ir para\\Festa!'
EventsPageUnknownToon = 'Toon Desconhecido'
EventsPageInvitedTabName = 'Convites'
EventsPageInvitedTabTitle = 'Convites de Festa'
EventsPageInvitedTabInvitationListTitle = 'Convites'
EventsPageInvitedTabActivityListTitle = 'Atividades'
EventsPageInvitedTabTime = '%s %s Hora de Toontown'
EventsPageNewsTabName = 'Not\xc3\xadcias'
EventsPageNewsTabTitle = 'Not\xc3\xadcias'
EventsPageNewsDownloading = 'Recuperando Not\xc3\xadcias...'
EventsPageNewsUnavailable = 'Tico e Teco brincando com a impressora da gr\xc3\xa1fica. Not\xc3\xadcias n\xc3\xa3o dispon\xc3\xadveis.'
EventsPageNewsPaperTitle = 'TOONTOWN TIMES (GAZETA DE TOONTOWN)'
EventsPageNewsLeftSubtitle = 'Ainda s\xc3\xb3 por 1 balinha'
EventsPageNewsRightSubtitle = 'Tiragem de nove mil toonplares'
NewsPageName = 'Not\xc3\xadcias'
NewsPageImportError = 'N\xc3\xa3o foi poss\xc3\xadvel abrir as not\xc3\xadcias sobre jogos.'
NewsPageDownloadingNewsSubstr = 'Please come back later. Downloading news'
NewsPageDownloadingNews0 = NewsPageDownloadingNewsSubstr + ' %s%%.'
NewsPageDownloadingNews1 = NewsPageDownloadingNewsSubstr + ' %s%%..'
NewsPageDownloadingNews2 = NewsPageDownloadingNewsSubstr + ' %s%%...'
NewsPageErrorDownloadingFile = 'Oops, there was a problem downloading\n%s.'
NewsPageErrorDownloadingFileCanStillRead = 'Oops, there was a problem downloading\n%s.\nYou can still read the other pages.'
NewsPageNoIssues = 'Could not find any issues in %s.'
IssueFrameThisWeek = 'this week'
IssueFrameLastWeek = 'last week'
IssueFrameWeeksAgo = '%d weeks ago'
SelectedInvitationInformation = '%s tem uma festa em %s \xc3\xa0s %s, Hora de Toontown.'
PartyPlannerNextButton = 'Continuar'
PartyPlannerPreviousButton = 'Voltar'
PartyPlannerWelcomeTitle = 'Planejador de Festas de Toontown'
PartyPlannerInstructions = 'Hospedar sua festa \xc3\xa9 muito divertido!\nComece a planejar com as setas na parte inferior!'
PartyPlannerDateTitle = 'Escolha o Dia de Sua Festa'
PartyPlannerTimeTitle = 'Escolha a Hora de Sua Festa'
PartyPlannerGuestTitle = 'Selecione os Convidados'
PartyPlannerEditorTitle = 'Crie Sua Festa\nInsira as Atividades e Decora\xc3\xa7\xc3\xb5es'
PartyPlannerConfirmTitle = 'Escolha os Convites para Enviar'
PartyPlannerConfirmTitleNoFriends = 'Reveja os Detalhes de Sua Festa'
PartyPlannerTimeToontown = 'Toontown'
PartyPlannerTimeTime = 'Hora'
PartyPlannerTimeRecap = 'Dia e Hora da Festa'
PartyPlannerPartyNow = 'O Mais Breve Poss\xc3\xadvel'
PartyPlannerTimeToontownTime = 'Hora de Toontown:'
PartyPlannerTimeLocalTime = 'Hora Local da Festa: '
PartyPlannerPublicPrivateLabel = 'A festa ser\xc3\xa1:'
PartyPlannerPublicDescription = 'Todos os Toons\npodem vir!'
PartyPlannerPrivateDescription = 'Apenas\nToons Convidados\npodem vir!'
PartyPlannerPublic = 'P\xc3\xbablica'
PartyPlannerPrivate = 'Particular'
PartyPlannerCheckAll = 'Selecionar\nTudo'
PartyPlannerUncheckAll = 'Desmarcar\nTudo'
PartyPlannerDateText = 'Data'
PartyPlannerTimeText = 'Hora'
PartyPlannerTTTimeText = 'Hora de Toontown'
PartyPlannerEditorInstructionsIdle = 'Clique na Atividade ou Decora\xc3\xa7\xc3\xa3o de Festa que deseja adquirir.'
PartyPlannerEditorInstructionsClickedElementActivity = 'Clique em Comprar ou Arraste o \xc3\x8dcone da Atividade para o Mapa da Festa'
PartyPlannerEditorInstructionsClickedElementDecoration = 'Clique em Comprar ou Arraste o \xc3\x8dcone da Decora\xc3\xa7\xc3\xa3o para o Mapa da Festa'
PartyPlannerEditorInstructionsDraggingActivity = 'Arraste a Atividade para o Mapa da Festa.'
PartyPlannerEditorInstructionsDraggingDecoration = 'Arraste a Decora\xc3\xa7\xc3\xa3o para o Mapa da Festa.'
PartyPlannerEditorInstructionsPartyGrounds = 'Clique e Arraste os itens para mov\xc3\xaa-los pelo Mapa da Festa'
PartyPlannerEditorInstructionsTrash = 'Arraste uma Atividade ou Decora\xc3\xa7\xc3\xa3o at\xc3\xa9 aqui para remov\xc3\xaa-la.'
PartyPlannerEditorInstructionsNoRoom = 'N\xc3\xa3o h\xc3\xa1 lugar para colocar essa atividade.'
PartyPlannerEditorInstructionsRemoved = '%(removed)s removidos(as) desde que %(added)s foram adicionados(as).'
PartyPlannerBeans = 'feij\xc3\xb5es'
PartyPlannerTotalCost = 'Custo Total:\n%d feij\xc3\xb5es'
PartyPlannerSoldOut = 'ESGOTADO'
PartyPlannerBuy = 'COMPRAR'
PartyPlannerPaidOnly = 'S\xc3\x93 ASSOCIADOS'
PartyPlannerPartyGrounds = 'MAPA DA FESTA'
PartyPlannerOkWithGroundsLayout = 'Voc\xc3\xaa j\xc3\xa1 terminou de mover suas Atividades e Decora\xc3\xa7\xc3\xb5es pelo Mapa da Festa?'
PartyPlannerChooseFutureTime = 'Por favor, selecione uma hora futura.'
PartyPlannerInviteButton = 'Enviar Convites'
PartyPlannerInviteButtonNoFriends = 'Planejar Festa'
PartyPlannerBirthdayTheme = 'Anivers\xc3\xa1rio'
PartyPlannerGenericMaleTheme = 'Estrelas'
PartyPlannerGenericFemaleTheme = 'Flores'
PartyPlannerRacingTheme = 'Corrida'
PartyPlannerValentoonsTheme = ' Dia dos namorados '
PartyPlannerVictoryPartyTheme = 'Vit\xc3\xb3ria'
PartyPlannerWinterPartyTheme = 'Inverno'
PartyPlannerGuestName = 'Nome do Convidado'
PartyPlannerClosePlanner = 'Fechar Planejador'
PartyPlannerConfirmationAllOkTitle = 'Parab\xc3\xa9ns!'
PartyPlannerConfirmationAllOkText = 'Sua festa foi criada e os convites enviados.\nObrigado!'
PartyPlannerConfirmationAllOkTextNoFriends = 'Sua festa foi criada!\nObrigado!'
PartyPlannerConfirmationErrorTitle = 'Opa.'
PartyPlannerConfirmationValidationErrorText = 'Desculpe, ocorreu um problema\ncom essa festa.\nPor favor, volte e tente novamente.'
PartyPlannerConfirmationDatabaseErrorText = 'Desculpe, n\xc3\xa3o foi poss\xc3\xadvel registrar todas as informa\xc3\xa7\xc3\xb5es.\nPor favor, tente novamente mais tarde.\nN\xc3\xa3o se preocupe, nenhum feij\xc3\xa3o foi perdido.'
PartyPlannerConfirmationTooManyText = 'Desculpe, voc\xc3\xaa j\xc3\xa1 est\xc3\xa1 dando uma festa.\nSe quiser planejar outra, por favor,\ncancele a atual.'
PartyPlannerInvitationThemeWhatSentence = 'Voc\xc3\xaa est\xc3\xa1 convidado(a) para minha festa de %s! %s!'
PartyPlannerInvitationThemeWhatSentenceNoFriends = 'Estou dando uma festa de %s! %s!'
PartyPlannerInvitationThemeWhatActivitiesBeginning = 'Ter\xc3\xa1 '
PartyPlannerInvitationWhoseSentence = 'Festa de %s'
PartyPlannerInvitationTheme = 'Tema'
PartyPlannerInvitationWhenSentence = 'Ser\xc3\xa1 em %s,\n\xc3\xa0s %s, Hora de Toontown.\nEspero que voc\xc3\xaa apare\xc3\xa7a!'
PartyPlannerInvitationWhenSentenceNoFriends = 'Ser\xc3\xa1 em %s,\n\xc3\xa0s %s, Hora de Toontown.\nToont\xc3\xa1stico!'
PartyPlannerComingSoon = 'Em Breve'
PartyPlannerCantBuy = 'N\xc3\xa3o Pode Comprar'
PartyPlannerGenericName = 'Planejador de Festa'
PartyJukeboxOccupied = 'Algu\xc3\xa9m est\xc3\xa1 usando a jukebox. Tente novamente mais tarde.'
PartyJukeboxNowPlaying = 'A m\xc3\xbasica que voc\xc3\xaa escolheu j\xc3\xa1 est\xc3\xa1 tocando na jukebox!'
MusicEncntrGeneralBg = 'Encontro Com Cogs'
MusicTcSzActivity = 'Mistureba de Toontorial'
MusicTcSz = 'Passeando Juntos'
MusicCreateAToon = 'Novo Toon na Cidade'
MusicTtTheme = 'O Tema de Toontown'
MusicMinigameRace = 'Devagar e Firme'
MusicMgPairing = 'Voc\xc3\xaa se lembra de Mim?'
MusicTcNbrhood = 'Centro de Toontown'
MusicMgDiving = 'Cantiga do Tesouro'
MusicMgCannonGame = 'Disparar os Canh\xc3\xb5es!'
MusicMgTwodgame = 'Toon Cont\xc3\xadnuo'
MusicMgCogthief = 'Pegue Aquele Cog!'
MusicMgTravel = 'M\xc3\xbasica para Viagem'
MusicMgTugOWar = 'Cabo de Guerra'
MusicMgVine = 'O Balan\xc3\xa7o da Selva'
MusicMgIcegame = 'Situa\xc3\xa7\xc3\xa3o Delicada'
MusicMgToontag = 'Mistureba de Minijogo'
MusicMMatchBg2 = 'Jazz da Minnie'
MusicMgTarget = 'Sobrevoando Toontown'
MusicFfSafezone = 'A Fazenda Divertida'
MusicDdSz = 'O Caminho Tortuoso'
MusicMmNbrhood = 'Melodil\xc3\xa2ndia da Minnie'
MusicGzPlaygolf = 'Vamos Jogar Golfe!'
MusicGsSz = 'Aut\xc3\xb3dromo do Pateta'
MusicOzSz = 'Terras do Tico e Teco'
MusicGsRaceCc = 'Dirigindo no Centro'
MusicGsRaceSs = 'Preparar, Acionar, Vai!'
MusicGsRaceRr = 'Rota 66'
MusicGzSz = 'A Polca Puf-Puf'
MusicMmSz = 'Dan\xc3\xa7ando nas Ruas'
MusicMmSzActivity = 'A\xc3\xad Vem o Soprano'
MusicDdNbrhood = 'O Porto do Donald'
MusicGsKartshop = 'Sr. Pateta M\xc3\xa3os \xc3\xa0 Obra'
MusicDdSzActivity = 'Cabana da Praia'
MusicEncntrGeneralBgIndoor = 'Botando pra Quebrar'
MusicTtElevator = 'Subindo?'
MusicEncntrToonWinningIndoor = 'Toons Unidos!'
MusicEncntrGeneralSuitWinningIndoor = 'Cogt\xc3\xa1strofe!'
MusicTbNbrhood = 'O Brrrgh'
MusicDlNbrhood = 'Sonhol\xc3\xa2ndia do Donald'
MusicDlSzActivity = 'Contando Ovelhas'
MusicDgSz = 'Valsa das Flores'
MusicDlSz = 'Son\xc3\xa2mbulo'
MusicTbSzActivity = 'Nevasca'
MusicTbSz = 'Tremendo e Vibrando'
MusicDgNbrhood = 'Jardim da Margarida'
MusicEncntrHallOfFame = 'A Galeria da Fama'
MusicEncntrSuitHqNbrhood = 'Reais e Centavos'
MusicChqFactBg = 'F\xc3\xa1brica de Cogs'
MusicCoghqFinale = 'Triunfo dos Toons'
MusicEncntrToonWinning = 'Pagando \xc3\xa0 Vista!'
MusicEncntrSuitWinning = 'Vendendo Seu Short'
MusicEncntrHeadSuitTheme = 'O Chef\xc3\xa3o'
MusicLbJurybg = 'O Julgamento Come\xc3\xa7ou'
MusicLbCourtyard = 'Balan\xc3\xa7ando'
MusicBossbotCeoV2 = 'O Gerente'
MusicBossbotFactoryV1 = 'Valsa do Cog'
MusicBossbotCeoV1 = 'Rodeado de Chefes'
MusicPartyOriginalTheme = 'Hora da Festa'
MusicPartyPolkaDance = 'Polca de Festa'
MusicPartySwingDance = 'Balan\xc3\xa7o de Festa'
MusicPartyWaltzDance = 'Valsa de Festa'
MusicPartyGenericThemeJazzy = 'Jazz de Festa'
MusicPartyGenericTheme = 'Jingle de Festa'
JukeboxAddSong = 'Adicionar\nM\xc3\xbasica'
JukeboxReplaceSong = 'Trocar\nM\xc3\xbasica'
JukeboxQueueLabel = 'Tocar a Seguir:'
JukeboxSongsLabel = 'Selecionar M\xc3\xbasica:'
JukeboxClose = 'Pronto'
JukeboxCurrentlyPlaying = 'Tocando Agora'
JukeboxCurrentlyPlayingNothing = 'Jukebox em pausa.'
JukeboxCurrentSongNothing = 'Adicionar uma m\xc3\xbasica \xc3\xa0 lista!'
PartyOverWarningNoName = 'A festa acabou! Obrigado por ter vindo!'
PartyOverWarningWithName = 'A festa %s de acabou! Obrigado por ter vindo!'
PartyCountdownClockText = 'Tempo\n\nRestante'
PartyTitleText = 'Festa de %s'
PartyActivityConjunction = ', e '
PartyActivityNameDict = {
    0: {
        'generic': 'Jukebox\n20 m\xc3\xbasicas',
        'invite': 'uma Jukebox de 20 m\xc3\xbasicas',
        'editor': 'Jukebox de 20',
        'description': 'Ou\xc3\xa7a m\xc3\xbasica com sua pr\xc3\xb3pria jukebox de 20 m\xc3\xbasicas!' },
    1: {
        'generic': 'Canh\xc3\xb5es de Festa',
        'invite': 'Canh\xc3\xb5es de Festa',
        'editor': 'Canh\xc3\xb5es',
        'description': 'Dispare voc\xc3\xaa mesmo os canh\xc3\xb5es e divirta-se!' },
    2: {
        'generic': 'Trampolim',
        'invite': 'Trampolim',
        'editor': 'Trampolim',
        'description': 'Pegue balinhas e salte o mais alto poss\xc3\xadvel!' },
    3: {
        'generic': 'Pescaria de Festa',
        'invite': 'Pescaria de Festa',
        'editor': 'Pescaria de Festa',
        'description': 'Pegue as frutas para ganhar feij\xc3\xb5es! Desvie-se das bigornas!' },
    4: {
        'generic': 'Pista de Dan\xc3\xa7a\n10 passos',
        'invite': 'uma Pista de Dan\xc3\xa7a com 10 passos',
        'editor': 'Pista de Dan\xc3\xa7a de 10',
        'description': 'Mostre seus 10 passos de dan\xc3\xa7a ao estilo toon!' },
    5: {
        'generic': 'Cabo de Guerra de Festa',
        'invite': 'Cabo de Guerra de Festa',
        'editor': 'Cabo de Guerra',
        'description': 'At\xc3\xa9 4 toons de cada lado puxando loucamente!' },
    6: {
        'generic': 'Fogos de Artif\xc3\xadcio de Festa',
        'invite': 'Fogos de Artif\xc3\xadcio de Festa',
        'editor': 'Fogos de Artif\xc3\xadcio',
        'description': 'Lance seu pr\xc3\xb3prio show de fogos de artif\xc3\xadcio!' },
    7: {
        'generic': 'Rel\xc3\xb3gio de Festa',
        'invite': 'um Rel\xc3\xb3gio de Festa',
        'editor': 'Rel\xc3\xb3gio de Festa',
        'description': 'Fa\xc3\xa7a a contagem regressiva do tempo que resta de sua festa.' },
    8: {
        'generic': 'Jukebox\n40 m\xc3\xbasicas',
        'invite': 'uma Jukebox de 40 m\xc3\xbasicas',
        'editor': 'Jukebox de 40',
        'description': 'Ou\xc3\xa7a m\xc3\xbasica com sua pr\xc3\xb3pria jukebox de 40 m\xc3\xbasicas!' },
    9: {
        'generic': 'Pista de Dan\xc3\xa7a\n20 passos',
        'invite': 'uma Pista de Dan\xc3\xa7a de 20 passos',
        'editor': 'Pista de Dan\xc3\xa7a de 20',
        'description': 'Mostre seus 20 passos de dan\xc3\xa7a ao estilo toon!' },
    10: {
        'generic': 'Cog-O-War',
        'invite': 'Cog-O-War',
        'editor': 'Cog-O-War',
        'description': 'O jogo de equipe versus equipe de acertar Cog!' },
    11: {
        'generic': 'Trampolim de Cog',
        'invite': 'Trampolim de Cog',
        'editor': 'Trampolim de Cog',
        'description': 'Pular na cara de um Cog!' },
    12: {
        'generic': 'Pegando Presentes',
        'invite': 'Pegando Presentes',
        'editor': 'Pegando Presentes',
        'description': 'Pegue presentes para ganhar balas! Esquive-se daquelas bigornas!' },
    13: {
        'generic': 'Trampolim de Inverno',
        'invite': 'Trampolim de Inverno',
        'editor': 'Trampolim de Inverno',
        'description': 'Pegue balinhas e salte o mais alto que puder!' },
    14: {
        'generic': 'Cog-O-War de Inverno',
        'invite': 'Cog-O-War de Inverno',
        'editor': 'Cog-O-War de Inverno',
        'description': 'O jogo de equipe versus equipe de acertar Cog!' } }
PartyDecorationNameDict = {
    0: {
        'editor': 'Bigorna de Bal\xc3\xb5es',
        'description': 'Tente evitar que a divers\xc3\xa3o acabe!' },
    1: {
        'editor': 'Palco de Festa',
        'description': 'Bal\xc3\xb5es, estrelas ou qualquer coisa que desejar' },
    2: {
        'editor': 'Arco de Festa',
        'description': 'Torne a divers\xc3\xa3o envolvente!' },
    3: {
        'editor': 'Bolo',
        'description': 'Delicioso.' },
    4: {
        'editor': 'Castelo de Festa',
        'description': 'A casa de um Toon \xc3\xa9 seu castelo.' },
    5: {
        'editor': 'Pilha de Presentes',
        'description': 'Presentes para todos os Toons!' },
    6: {
        'editor': 'L\xc3\xadngua de Sogra',
        'description': 'Esse apito \xc3\xa9 muito estridente! Serpenteante!' },
    7: {
        'editor': 'Port\xc3\xa3o de Festa',
        'description': 'Multicolorido e doidinho!' },
    8: {
        'editor': 'Itens Barulhentos',
        'description': 'Piiiiiiiiiiii!' },
    9: {
        'editor': 'Cata-vento',
        'description': 'Giros coloridos para todos!' },
    10: {
        'editor': 'Globo Engra\xc3\xa7ado',
        'description': 'Globo engra\xc3\xa7ado e de estrelas criado por Olivea' },
    11: {
        'editor': 'Faixa Feij\xc3\xa3o',
        'description': 'Uma faixa em forma de balinha criada por Cassidy' },
    12: {
        'editor': 'Bolo Engra\xc3\xa7ado',
        'description': 'Um bolo engra\xc3\xa7ado e Ca\xc3\xb3tico criado por Fel\xc3\xadcia' },
    13: {
        'editor': 'Cora\xc3\xa7\xc3\xb5es de Cupidos',
        'description': 'Voc\xc3\xaa na mira no Dia dos namorados, divirta-se!' },
    14: {
        'editor': 'Banner de Cora\xc3\xa7\xc3\xa3o',
        'description': 'Compartilhe a divers\xc3\xa3o neste dia dos namorados!' },
    15: {
        'editor': 'Cora\xc3\xa7\xc3\xa3o Voador',
        'description': 'Flutue com o esp\xc3\xadrito do dia dos namorados!' },
    16: {
        'editor': 'Suporte de palanque',
        'description': 'Todos os nossos novos amigos est\xc3\xa3o prontos para dan\xc3\xa7ar!' },
    17: {
        'editor': 'Faixa da vit\xc3\xb3ria',
        'description': 'N\xc3\xa3o \xc3\xa9 apenas uma faixa comum!' },
    18: {
        'editor': 'Canh\xc3\xb5es de confete',
        'description': 'BUM! Confete! Divers\xc3\xa3o!' },
    19: {
        'editor': 'Cog e Doodle',
        'description': 'Ui! Isso vai doer.' },
    20: {
        'editor': 'Cog Suspenso',
        'description': 'Um Cog cheio de ar quente, chocante!' },
    21: {
        'editor': 'Cog Sorvete',
        'description': 'Um Cog de boa apar\xc3\xaancia' },
    22: {
        'editor': 'Cog Sorvete',
        'description': 'Um Cog de boa apar\xc3\xaancia' },
    23: {
        'editor': 'Coreto de Natal',
        'description': 'Todos adoram uma Festa de Natal! ' },
    24: {
        'editor': 'Cog e Doodle',
        'description': 'Ai! Isso vai doer. ' },
    25: {
        'editor': 'Boneco de neve',
        'description': 'T\xc3\xa3o legal, ele \xc3\xa9 demais!' },
    26: {
        'editor': 'Doodle de neve',
        'description': 'Seu \xc3\xbanico truque est\xc3\xa1 esfriando!' } }
ActivityLabel = 'Custo \xe2\x80\x93 Nome da Atividade'
PartyDoYouWantToPlan = 'Deseja planejar uma nova festa agora?'
PartyPlannerOnYourWay = 'Divirta-se planejando a sua festa!'
PartyPlannerMaybeNextTime = 'Talvez da pr\xc3\xb3xima vez.  Tenha um bom-dia!'
PartyPlannerHostingTooMany = 'Desculpe, voc\xc3\xaa s\xc3\xb3 pode dar uma festa de cada vez.'
PartyPlannerOnlyPaid = 'Desculpe, s\xc3\xb3 toons assinantes podem dar uma festa.'
PartyPlannerNpcComingSoon = 'Em breve surgir\xc3\xa3o mais festas! Tente novamente mais tarde.'
PartyPlannerNpcMinCost = 'O custo m\xc3\xadnimo para planejar uma festa \xc3\xa9 de %d balinhas.'
PartyHatPublicPartyChoose = 'deseja ir para a primeira festa p\xc3\xbablica dispon\xc3\xadvel?'
PartyGateTitle = 'Festas P\xc3\xbablicas'
PartyGateGoToParty = 'Ir para\nFesta!'
PartyGatePartiesListTitle = 'Anfitri\xc3\xb5es'
PartyGatesPartiesListToons = 'Toons'
PartyGatesPartiesListActivities = 'Atividades'
PartyGatesPartiesListMinLeft = 'Minutos Restantes'
PartyGateLeftSign = 'Venha se Divertir!'
PartyGateRightSign = 'Festas P\xc3\xbablicas Aqui!'
PartyGateTitle = 'Festas P\xc3\xbablicas Aqui!'
PartyGatePartyUnavailable = 'Desculpe. Essa festa n\xc3\xa3o est\xc3\xa1 mais dispon\xc3\xadvel.'
PartyGatePartyFull = 'Desculpe. Essa festa est\xc3\xa1 lotada.'
PartyGateInstructions = 'Clique em um anfitri\xc3\xa3o e em "Ir para Festa"'
PartyActivityWaitingForOtherPlayers = 'Aguardando outros jogadores para se juntarem \xc3\xa0 festa...'
PartyActivityPleaseWait = 'Por favor, aguarde...'
DefaultPartyActivityTitle = 'T\xc3\xadtulo do Jogo de Festa'
DefaultPartyActivityInstructions = 'Instru\xc3\xa7\xc3\xb5es do Jogo de Festa'
PartyOnlyHostLeverPull = 'Apenas o anfitri\xc3\xa3o pode iniciar essa atividade. Desculpe.'
PartyActivityDefaultJoinDeny = 'Voc\xc3\xaa n\xc3\xa3o pode participar dessa atividade no momento. Desculpe.'
PartyActivityDefaultExitDeny = 'Voc\xc3\xaa n\xc3\xa3o pode sair dessa atividade no momento. Desculpe.'
PartyJellybeanRewardOK = 'OK'
PartyCatchActivityTitle = 'Atividade Pescaria de Festa'
PartyCatchActivityInstructions = "Pegue o m\xc3\xa1ximo de pe\xc3\xa7as de frutas que puder. Tente n\xc3\xa3o 'pescar' quaisquer %(badThing)s!"
PartyCatchActivityFinishPerfect = 'JOGO PERFEITO!'
PartyCatchActivityFinish = 'Bom Jogo!'
PartyCatchActivityExit = 'Sair'
PartyCatchActivityApples = 'ma\xc3\xa7\xc3\xa3s'
PartyCatchActivityOranges = 'laranjas'
PartyCatchActivityPears = 'peras'
PartyCatchActivityCoconuts = 'cocos'
PartyCatchActivityWatermelons = 'melancias'
PartyCatchActivityPineapples = 'abacaxis'
PartyCatchActivityAnvils = 'bigornas'
PartyCatchStarted = 'O jogo come\xc3\xa7ou. Divirta-se.'
PartyCatchCannotStart = 'O jogo n\xc3\xa3o pode ser iniciado no momento.'
PartyCatchRewardMessage = 'Pe\xc3\xa7as de frutas coletadas: %s\n\nBalinhas recebidas: %d'
WinterPartyCatchActivityInstructions = "Pegue o m\xc3\xa1ximo de presentes que puder. Tente n\xc3\xa3o 'pegar' nenhum %(badThing)s!"
WinterPartyCatchRewardMessage = 'Presentes pegos: %s\n\nBalinhas obtidas: %s'
PartyDanceActivityTitle = 'Pista de Dan\xc3\xa7a de Festa'
PartyDanceActivityInstructions = 'Combine 3 ou mais padr\xc3\xb5es de SETAS para fazer os passos de dan\xc3\xa7a! H\xc3\xa1 10 passos de dan\xc3\xa7a dispon\xc3\xadveis. Voc\xc3\xaa consegue obter todos?'
PartyDanceActivity20Title = 'Pista de Dan\xc3\xa7a de festa'
PartyDanceActivity20Instructions = 'Combine 3 ou mais padr\xc3\xb5es de SETAS para fazer os passos de dan\xc3\xa7a! H\xc3\xa1 20 passos de dan\xc3\xa7a dispon\xc3\xadveis. Voc\xc3\xaa consegue obter todos?'
DanceAnimRight = 'Direita'
DanceAnimReelNeutral = 'O Toonpescador'
DanceAnimConked = 'O Cabe\xc3\xa7amole'
DanceAnimHappyDance = 'A Dan\xc3\xa7a Feliz'
DanceAnimConfused = 'Vertigem Total'
DanceAnimWalk = 'Andando na Lua'
DanceAnimJump = 'O Salto!'
DanceAnimFirehose = 'O Toonbombeiro'
DanceAnimShrug = 'Quem Sabe?'
DanceAnimSlipForward = 'A Queda'
DanceAnimSadWalk = 'Exaust\xc3\xa3o'
DanceAnimWave = 'Ol\xc3\xa1, Tchauzinho'
DanceAnimStruggle = 'O Pulo Misto'
DanceAnimRunningJump = 'O Toon Fugitivo'
DanceAnimSlipBackward = 'A Queda de Costas'
DanceAnimDown = 'A Descida'
DanceAnimUp = 'A Subida'
DanceAnimGoodPutt = 'A Tacada'
DanceAnimVictory = 'A Dan\xc3\xa7a da Vit\xc3\xb3ria'
DanceAnimPush = 'O Toonm\xc3\xadmico'
DanceAnimAngry = "Rock'n'Roll"
DanceAnimLeft = 'Esquerda'
PartyCannonActivityTitle = 'Canh\xc3\xb5es de Festa'
PartyCannonActivityInstructions = 'Acerte as nuvens para mudar sua cor e ricochetear no ar! NO AR, voc\xc3\xaa pode USAR AS SETAS para DESLIZAR.'
PartyCannonResults = 'Voc\xc3\xaa recebeu %d balinhas!\n\nNuvens Atingidas: %d'
FireworksActivityInstructions = 'Pressione a tecla "Page Up" para visualizar melhor.'
FireworksActivityBeginning = 'Os fogos de artif\xc3\xadcio de festa v\xc3\xa3o ser lan\xc3\xa7ados! Curta o espet\xc3\xa1culo!'
FireworksActivityEnding = 'Espero que tenha gostado do espet\xc3\xa1culo!'
PartyFireworksAlreadyActive = 'O espet\xc3\xa1culo de fogos de artif\xc3\xadcio j\xc3\xa1 come\xc3\xa7ou.'
PartyFireworksAlreadyDone = 'O espet\xc3\xa1culo de fogos de artif\xc3\xadcio acabou.'
PartyTrampolineJellyBeanTitle = 'Trampolim de Balinhas'
PartyTrampolineTricksTitle = 'Trampolim de Acrobacias'
PartyTrampolineActivityInstructions = 'Use a tecla Control para saltar.\n\nSalte quando seu Toon estiver no ponto mais baixo do trampolim para ir bem alto.'
PartyTrampolineActivityOccupied = 'O trampolim est\xc3\xa1 sendo usado.'
PartyTrampolineQuitEarlyButton = 'Saltar'
PartyTrampolineBeanResults = 'Voc\xc3\xaa recebeu %d balinhas.'
PartyTrampolineBonusBeanResults = 'Voc\xc3\xaa recebeu %d balinhas, al\xc3\xa9m de mais %d por conseguir o Big Bean (Grande Feij\xc3\xa3o).'
PartyTrampolineTopHeightResults = 'Seu recorde de altura foi %d ft (mt).'
PartyTrampolineTimesUp = 'Acabou o Tempo'
PartyTrampolineReady = 'Preparar...'
PartyTrampolineGo = 'J\xc3\xa1!'
PartyTrampolineBestHeight = 'Recorde de Altura At\xc3\xa9 Agora:\n%s\n%d ft (mt)'
PartyTrampolineNoHeightYet = 'Qu\xc3\xa3o alto\nvoc\xc3\xaa pode saltar?'
PartyTrampolineGetHeight = '%d ft (mt)'
PartyTeamActivityForMorePlural = 'S'
PartyTeamActivityForMore = 'Aguardando %d jogadores%s\n\xc3\xa3o de cada lado...'
PartyTeamActivityForMoreWithBalance = 'Aguardando mais %d jogadores%s...'
PartyTeamActivityWaitingForOtherPlayers = 'Aguardando outros jogadores...'
PartyTeamActivityWaitingToStart = 'Come\xc3\xa7ando em...'
PartyTeamActivityExitButton = 'Pular Fora'
PartyTeamActivitySwitchTeamsButton = 'Mudar de\nEquipe'
PartyTeamActivityWins = 'A equipe %s venceu!'
PartyTeamActivityLocalAvatarTeamWins = 'Sua equipe venceu!'
PartyTeamActivityGameTie = 'Deu empate!'
PartyTeamActivityJoinDenied = 'Voc\xc3\xaa n\xc3\xa3o pode entrar para %s no momento.'
PartyTeamActivityExitDenied = 'Voc\xc3\xaa n\xc3\xa3o pode sair de %s no momento.'
PartyTeamActivitySwitchDenied = 'Voc\xc3\xaa n\xc3\xa3o pode mudar de equipe no momento.'
PartyTeamActivityTeamFull = 'Esta equipe j\xc3\xa1 est\xc3\xa1 completa!'
PartyTeamActivityRewardMessage = 'Voc\xc3\xaa tem %d balas de goma. Bom trabalho!'
PartyCogTeams = ('Azul', 'Laranja')
PartyCogRewardMessage = 'Sua Pontua\xc3\xa7\xc3\xa3o: %d\n'
PartyCogRewardBonus = '\nVoc\xc3\xaa tem %d balas de goma%s adicionais porque a sua equipe venceu!'
PartyCogJellybeanPlural = 'S'
PartyCogSignNote = 'RECORDE\n%s\n%d'
PartyCogTitle = 'Arremesso de Torta nos Cogs'
PartyCogInstructions = 'Jogue tortas nos cogs para afast\xc3\xa1-los de sua equipe. ' + 'Quando acabar o tempo, a equipe com menos cogs ganha!' + '\n\nArremesse com a TECLA CTRL. Movimente-se com as SETAS DIRECIONAIS.'
PartyCogDistance = '%d ft'
PartyCogTimeUp = 'O tempo acabou!'
PartyCogGuiScoreLabel = 'PONTOS'
PartyCogGuiPowerLabel = 'ENERGIA'
PartyCogGuiSpamWarning = 'Mantenha pressionada a tecla CONTROL para obter mais for\xc3\xa7a!'
PartyCogBalanceBar = 'EQUIL\xc3\x8dBRIO'
PartyTugOfWarJoinDenied = 'Desculpe. Voc\xc3\xaa n\xc3\xa3o pode participar do cabo de guerra no momento.'
PartyTugOfWarTeamFull = 'Desculpe. Essa equipe j\xc3\xa1 est\xc3\xa1 completa.'
PartyTrampolineQuitEarlyButton = 'Saltar'
PartyTugOfWarExitButton = 'Sair'
PartyTugOfWarWaitingForMore = 'Aguardando mais jogadores'
PartyTugOfWarWaitingToStart = 'Aguardando para come\xc3\xa7ar'
PartyTugOfWarWaitingForOtherPlayers = 'Aguardando outros jogadores'
PartyTugOfWarReady = 'Preparar...'
PartyTugOfWarGo = 'J\xc3\x81!'
PartyTugOfWarGameEnd = 'Bom jogo!'
PartyTugOfWarGameTie = 'Voc\xc3\xaa empatou!'
PartyTugOfWarRewardMessage = 'voc\xc3\xaa conseguiu %d balinhas. Bom trabalho!'
PartyTugOfWarTitle = 'Cabo de Guerra de Festa'
CalendarShowAll = 'Exibir Tudo'
CalendarShowOnlyHolidays = 'Exibir Apenas Feriados'
CalendarShowOnlyParties = 'Exibir Apenas Feriados'
CalendarEndsAt = 'Termina em '
CalendarStartedOn = 'Iniciada em '
CalendarEndDash = 'Final-'
CalendarEndOf = 'Final de '
CalendarPartyGetReady = 'Prepare-se!'
CalendarPartyGo = 'Festejar!'
CalendarPartyFinished = 'Acabou...'
CalendarPartyCancelled = 'Cancelado.'
CalendarPartyNeverStarted = 'Nunca Aconteceu.'
NPCFriendPanelRemaining = 'Restantes %s'
PartiesPageTitle = ''
PartiesPageHostTab = ''
PartiesPageInvitedTab = ''
PartiesPageTitleHost = ''
PartiesPageTitleInvited = ''
MapPageTitle = 'Mapa'
MapPageBackToPlayground = 'Voltar para o p\xc3\xa1tio'
MapPageBackToCogHQ = 'Voltar para o Quartel de Cogs'
MapPageGoHome = 'Ir para casa'
MapPageYouAreHere = 'Voc\xc3\xaa est\xc3\xa1 em: %s %s'
MapPageYouAreAtHome = 'Voc\xc3\xaa est\xc3\xa1 em\nsua propriedade'
MapPageYouAreAtSomeonesHome = 'Voc\xc3\xaa est\xc3\xa1 na propriedade de %s'
MapPageGoTo = 'Ir para\n%s'
OptionsPageTitle = 'Op\xc3\xa7\xc3\xb5es'
OptionsTabTitle = 'Op\xc3\xa7\xc3\xb5es\n& C\xc3\xb3digos'
OptionsPagePurchase = 'Assine j\xc3\xa1!'
OptionsPageLogout = 'Sair'
OptionsPageExitToontown = 'Sair de Toontown'
OptionsPageMusicOnLabel = 'A m\xc3\xbasica est\xc3\xa1 ligada.'
OptionsPageMusicOffLabel = 'A m\xc3\xbasica est\xc3\xa1 desligada.'
OptionsPageSFXOnLabel = 'Os efeitos sonoros est\xc3\xa3o ligados.'
OptionsPageSFXOffLabel = 'Os efeitos sonoros est\xc3\xa3o desligados.'
OptionsPageToonChatSoundsOnLabel = '   Type Chat Sounds are on.'
OptionsPageToonChatSoundsOffLabel = '   Type Chat Sounds are off.'
OptionsPageFriendsEnabledLabel = 'Aceito fazer novas amizades.'
OptionsPageFriendsDisabledLabel = 'N\xc3\xa3o aceito fazer amizades.'
OptionsPageSpeedChatStyleLabel = 'Cor do Chat r\xc3\xa1pido'
OptionsPageDisplayWindowed = 'com janela'
OptionsPageDisplayEmbedded = 'No navegador'
OptionsPageSelect = 'Selecionar'
OptionsPageToggleOn = 'Ligar'
OptionsPageToggleOff = 'Desligar'
OptionsPageChange = 'Alterar'
OptionsPageDisplaySettings = 'V\xc3\xaddeo: %(screensize)s, %(api)s'
OptionsPageDisplaySettingsNoApi = 'V\xc3\xaddeo: %(screensize)s'
OptionsPageExitConfirm = 'Sair de Toontown?'
DisplaySettingsTitle = 'Configura\xc3\xa7\xc3\xb5es de v\xc3\xaddeo'
DisplaySettingsIntro = 'As configura\xc3\xa7\xc3\xb5es a seguir s\xc3\xa3o usadas para determinar a maneira como Toontown \xc3\xa9 exibida em seu computador. Provavelmente, n\xc3\xa3o ser\xc3\xa1 necess\xc3\xa1rio ajust\xc3\xa1-las, a menos que voc\xc3\xaa esteja tendo algum problema.'
DisplaySettingsIntroSimple = 'Voc\xc3\xaa pode ajustar a resolu\xc3\xa7\xc3\xa3o da tela com um valor maior para melhorar o contraste do texto e dos gr\xc3\xa1ficos em Toontown, mas, dependendo da placa de v\xc3\xaddeo do seu computador, alguns valores mais altos podem fazer que o jogo fique lento ou trave.'
DisplaySettingsApi = 'API de gr\xc3\xa1fico:'
DisplaySettingsResolution = 'Resolu\xc3\xa7\xc3\xa3o:'
DisplaySettingsWindowed = 'Em uma janela'
DisplaySettingsFullscreen = 'Tela cheia'
DisplaySettingsEmbedded = 'No navegador'
DisplaySettingsApply = 'Aplicar'
DisplaySettingsCancel = lCancel
DisplaySettingsApplyWarning = 'Quando voc\xc3\xaa pressionar OK, as configura\xc3\xa7\xc3\xb5es de v\xc3\xaddeo ser\xc3\xa3o alteradas. Se a nova configura\xc3\xa7\xc3\xa3o n\xc3\xa3o ficar adequada em seu computador, o v\xc3\xaddeo retornar\xc3\xa1 \xc3\xa0 configura\xc3\xa7\xc3\xa3o original ap\xc3\xb3s %s segundos.'
DisplaySettingsAccept = 'Pressione em OK para manter as novas configura\xc3\xa7\xc3\xb5es, ou em Cancelar para voltar \xc3\xa0s anteriores. Se voc\xc3\xaa n\xc3\xa3o pressionar nada, as configura\xc3\xa7\xc3\xb5es voltar\xc3\xa3o em %s segundos automaticamente aos valores anteriores.'
DisplaySettingsRevertUser = 'As configura\xc3\xa7\xc3\xb5es de v\xc3\xaddeo anteriores foram restauradas.'
DisplaySettingsRevertFailed = 'As configura\xc3\xa7\xc3\xb5es de v\xc3\xaddeo selecionadas n\xc3\xa3o funcionam em seu computador. As configura\xc3\xa7\xc3\xb5es de v\xc3\xaddeo anteriores foram restauradas.'
OptionsPageCodesTab = 'Inserir C\xc3\xb3digo'
CdrPageTitle = 'Inserir um C\xc3\xb3digo'
CdrInstructions = 'Digite o seu c\xc3\xb3digo aqui para receber um pr\xc3\xaamio especial na sua caixa de entrada'
CdrResultSuccess = 'Parab\xc3\xa9ns! Verifique a sua caixa de correio para reivindicar o seu pr\xc3\xaamio!'
CdrResultInvalidCode = 'Voc\xc3\xaa inseriu um c\xc3\xb3digo inv\xc3\xa1lido. Por favor, confira a digita\xc3\xa7\xc3\xa3o e tente novamente'
CdrResultExpiredCode = 'Lamentamos. Esse c\xc3\xb3digo expirou'
CdrResultUnknownError = 'Lamentamos. Esse c\xc3\xb3digo n\xc3\xa3o pode ser aplicado ao seu Toon'
CdrResultMailboxFull = 'Sua caixa de correio est\xc3\xa1 cheia. Por favor, remova um item e, depois, insira o seu c\xc3\xb3digo novamente'
CdrResultAlreadyInMailbox = 'Voc\xc3\xaa j\xc3\xa1 recebeu esse item. Verifique a sua caixa de correio para confirmar'
CdrResultAlreadyInQueue = 'Seu pr\xc3\xaamio est\xc3\xa1 a caminho. Verifique a sua caixa de correio daqui a alguns minutos para receb\xc3\xaa-lo'
CdrResultAlreadyInCloset = 'Voc\xc3\xaa j\xc3\xa1 recebeu esse item. Verifique o seu arm\xc3\xa1rio para confirmar'
CdrResultAlreadyBeingWorn = 'Voc\xc3\xaa j\xc3\xa1 recebeu esse item e o est\xc3\xa1 usando!'
CdrResultAlreadyReceived = 'Voc\xc3\xaa j\xc3\xa1 recebeu esse item.'
CdrResultTooManyFails = 'Lamentamos. Voc\xc3\xaa tentou inserir um c\xc3\xb3digo errado repetidamente. Por favor, tente novamente daqui a 30 minutos'
CdrResultServiceUnavailable = 'Lamentamos. Esta caracter\xc3\xadstica \xc3\xa9 temporariamente n\xc3\xa3o dispon\xc3\xadvel. Tente por favor outra vez durante seu in\xc3\xadcio de uma sess\xc3\xa3o seguinte.'
TrackPageTitle = 'Treinamento de tipos de piadas'
TrackPageShortTitle = 'Treinamento de piadas'
TrackPageSubtitle = 'Execute as Tarefas Toon para aprender a usar novas piadas!'
TrackPageTraining = 'Voc\xc3\xaa est\xc3\xa1 treinando para usar as Piadas de %s.\nQuando executar todas as 16 tarefas,\nestar\xc3\xa1 apto a usar as Piadas de %s nas batalhas.'
TrackPageClear = 'Voc\xc3\xaa n\xc3\xa3o est\xc3\xa1 treinando nenhum tipo de piadas agora.'
TrackPageFilmTitle = 'Filme de\ntreinamento\nde %s'
TrackPageDone = 'FIM'
QuestPageToonTasks = 'Tarefas Toon'
QuestPageChoose = 'Escolha'
QuestPageLocked = 'Travado'
QuestPageDestination = '%s\n%s\n%s'
QuestPageNameAndDestination = '%s\n%s\n%s\n%s'
QuestPosterHQOfficer = lHQOfficerM
QuestPosterHQBuildingName = lToonHQ
QuestPosterHQStreetName = 'Qualquer rua'
QuestPosterHQLocationName = 'Qualquer bairro'
QuestPosterTailor = 'Costureiro'
QuestPosterTailorBuildingName = 'Loja de Roupas'
QuestPosterTailorStreetName = 'Qualquer p\xc3\xa1tio'
QuestPosterTailorLocationName = 'Qualquer bairro'
QuestPosterPlayground = 'No p\xc3\xa1tio'
QuestPosterAtHome = 'Na sua casa'
QuestPosterInHome = 'Em sua casa'
QuestPosterOnPhone = 'No seu telefone'
QuestPosterEstate = 'Na sua propriedade'
QuestPosterAnywhere = 'Qualquer lugar'
QuestPosterAuxTo = 'para:'
QuestPosterAuxFrom = 'de:'
QuestPosterAuxFor = 'para:'
QuestPosterAuxOr = 'ou:'
QuestPosterAuxReturnTo = 'Retornar\npara:'
QuestPosterLocationIn = ''
QuestPosterLocationOn = ''
QuestPosterFun = 'S\xc3\xb3 de brincadeira!'
QuestPosterFishing = 'IR PESCAR'
QuestPosterComplete = 'CONCLUIR'
QuestPosterConfirmDelete = 'Tem certeza de que quer excluir esta Tarefa de Toon?'
QuestPosterDeleteBtn = 'Excluir'
QuestPosterDialogYes = 'Excluir'
QuestPosterDialogNo = 'Cancelar'
ShardPageTitle = 'Regi\xc3\xb5es'
ShardPageHelpIntro = 'Cada Regi\xc3\xa3o \xc3\xa9 uma c\xc3\xb3pia do mundo de Toontown.'
ShardPageHelpWhere = ' Voc\xc3\xaa est\xc3\xa1 agora na Regi\xc3\xa3o "%s".'
ShardPageHelpWelcomeValley = ' Voc\xc3\xaa est\xc3\xa1 agora na Regi\xc3\xa3o "Vale Boas-vindas", em "%s".'
ShardPageHelpMove = ' Para ir at\xc3\xa9 uma nova Regi\xc3\xa3o, clique no nome dela.'
ShardPagePopulationTotal = 'Popula\xc3\xa7\xc3\xa3o Total de Toontown:\n%d'
ShardPageScrollTitle = 'Nome Popula\xc3\xa7\xc3\xa3o'
ShardPageLow = 'Tranquila'
ShardPageMed = 'Inteligente'
ShardPageHigh = 'Lotada'
ShardPageChoiceReject = 'Desculpe, essa Regi\xc3\xa3o est\xc3\xa1 lotada. Por favor, tente outra.'
SuitPageTitle = 'Galeria de Cogs'
SuitPageMystery = DialogQuestion + DialogQuestion + DialogQuestion
SuitPageQuota = '%s de %s'
SuitPageCogRadar = '%s presentes'
SuitPageBuildingRadarS = '%s edif\xc3\xadcio'
SuitPageBuildingRadarP = '%s edif\xc3\xadcios'
DisguisePageTitle = Cog + 'Disfarce'
DisguisePageMeritAlert = 'Pronto para a\npromo\xc3\xa7\xc3\xa3o!'
DisguisePageCogLevel = 'N\xc3\xadvel %s'
DisguisePageMeritFull = 'Completo'
FishPageTitle = 'Pescaria'
FishPageTitleTank = 'Balde de peixes'
FishPageTitleCollection = '\xc3\x81lbum de peixes'
FishPageTitleTrophy = 'Trof\xc3\xa9us de pesca'
FishPageWeightStr = 'Peso: '
FishPageWeightLargeS = '%d Kg '
FishPageWeightLargeP = '%d Kg '
FishPageWeightSmallS = '%d g'
FishPageWeightSmallP = '%d g'
FishPageWeightConversion = 16
FishPageValueS = 'Valor: %d balinha'
FishPageValueP = 'Valor: %d balinhas'
FishPageCollectedTotal = 'Esp\xc3\xa9cies de peixes recolhidas: %d de %d'
FishPageRodInfo = 'Vara %s\n%d - %d quilos'
FishPageTankTab = 'Balde'
FishPageCollectionTab = '\xc3\x81lbum'
FishPageTrophyTab = 'Trof\xc3\xa9us'
FishPickerTotalValue = 'Balde: %s / %s\nValor: %d balinhas'
UnknownFish = DialogQuestion + DialogQuestion + DialogQuestion
FishingRod = 'Vara %s'
FishingRodNameDict = {
    0: 'Vareta',
    1: 'Bambu',
    2: 'Madeira de lei',
    3: 'A\xc3\xa7o',
    4: 'Dourado' }
FishTrophyNameDict = {
    0: 'Peixinhozinho',
    1: 'Peixinho',
    2: 'Peixe',
    3: 'Peixe-voador',
    4: 'Tubar\xc3\xa3o',
    5: 'Peixe-espada',
    6: 'Baleia assassina' }
GardenPageTitle = 'Jardinagem'
GardenPageTitleBasket = 'Cesto de Flores'
GardenPageTitleCollection = '\xc3\x81lbum de Flores'
GardenPageTitleTrophy = 'Trof\xc3\xa9us de Jardinagem'
GardenPageTitleSpecials = 'Especiais de Jardinagem'
GardenPageBasketTab = 'Cesto'
GardenPageCollectionTab = '\xc3\x81lbum'
GardenPageTrophyTab = 'Trof\xc3\xa9us'
GardenPageSpecialsTab = 'Especiais'
GardenPageCollectedTotal = 'Variedades de Flores Colecionadas: %d de %d'
GardenPageValueS = 'Valor: %d balinha'
GardenPageValueP = 'Valor: %d balinhas'
FlowerPickerTotalValue = 'Cesto: %s / %s\nValor: %d balinhas'
GardenPageShovelInfo = '%s P\xc3\xa1: %d / %d\n'
GardenPageWateringCanInfo = '%s Regador: %d / %d'
FlowerPageWeightConversion = 1
FlowerPageWeightLargeP = ' Grande P '
FlowerPageWeightLargeS = ' GrandeS '
FlowerPageWeightSmallP = ' PequenoP '
FlowerPageWeightSmallS = ' PequenoS '
FlowerPageWeightStr = ' Peso: %s '
KartPageTitle = 'Karts'
KartPageTitleCustomize = 'Personalizador de karts'
KartPageTitleRecords = 'Melhores recordes pessoais'
KartPageTitleTrophy = 'Trof\xc3\xa9us de corridas'
KartPageCustomizeTab = 'Personalizar'
KartPageRecordsTab = 'Recordes'
KartPageTrophyTab = 'Trof\xc3\xa9us'
KartPageTrophyDetail = 'Trof\xc3\xa9us %s : %s'
KartPageTickets = 'Bilhetes :'
KartPageConfirmDelete = 'Excluir acess\xc3\xb3rio?'
KartShtikerDelete = 'Excluir'
KartShtikerSelect = 'Selecionar uma categoria'
KartShtikerNoAccessories = 'N\xc3\xa3o possui acess\xc3\xb3rios'
KartShtikerBodyColors = 'Cores de karts'
KartShtikerAccColors = 'Cores de acess\xc3\xb3rios'
KartShtikerEngineBlocks = 'Acess\xc3\xb3rios de cap\xc3\xb4'
KartShtikerSpoilers = 'Acess\xc3\xb3rios de mala'
KartShtikerFrontWheelWells = 'Acess\xc3\xb3rios de roda dianteira'
KartShtikerBackWheelWells = 'Acess\xc3\xb3rios de roda traseira'
KartShtikerRims = 'Acess\xc3\xb3rios de aro'
KartShtikerDecals = 'Acess\xc3\xb3rios de decalque'
KartShtikerBodyColor = 'Cor do kart'
KartShtikerAccColor = 'Cor do acess\xc3\xb3rio'
KartShtikerEngineBlock = 'Cap\xc3\xb4'
KartShtikerSpoiler = 'Mala'
KartShtikerFrontWheelWell = 'Roda dianteira'
KartShtikerBackWheelWell = 'Roda traseira'
KartShtikerRim = 'Aro'
KartShtikerDecal = 'Decalque'
KartShtikerDefault = 'Padr\xc3\xa3o %s'
KartShtikerNo = 'Nenhum acess\xc3\xb3rio %s'
QuestChoiceGuiCancel = lCancel
TrackChoiceGuiChoose = 'Escolher'
TrackChoiceGuiCancel = lCancel
TrackChoiceGuiHEAL = 'Toonar permite que voc\xc3\xaa cure outros Toons que est\xc3\xa3o na batalha.'
TrackChoiceGuiTRAP = 'Armadilhas s\xc3\xa3o piadas poderosas que devem ser usadas com Iscas.'
TrackChoiceGuiLURE = 'Use Iscas para abalar os Cogs ou fa\xc3\xa7a-os cair em armadilhas.'
TrackChoiceGuiSOUND = 'As piadas Sonoras afetam todos os Cogs, mas n\xc3\xa3o s\xc3\xa3o muito poderosas.'
TrackChoiceGuiDROP = 'As piadas Cadentes fazem muitos estragos, mas n\xc3\xa3o s\xc3\xa3o muito precisas.'
EmotePageTitle = 'Express\xc3\xb5es / Emo\xc3\xa7\xc3\xb5es'
EmotePageDance = 'Voc\xc3\xaa montou a seguinte sequ\xc3\xaancia de dan\xc3\xa7a:'
EmoteJump = 'Saltitante'
EmoteDance = 'Dan\xc3\xa7ante'
EmoteHappy = 'Feliz'
EmoteSad = 'Triste'
EmoteAnnoyed = 'Aborrecido'
EmoteSleep = 'Sonolento'
TIPPageTitle = 'DICA'
SuitBaseNameWithLevel = '%(name)s\n%(dept)s\nN\xc3\xadvel %(level)s'
HealthForceAcknowledgeMessage = 'Voc\xc3\xaa n\xc3\xa3o pode sair do parque at\xc3\xa9 que o seu Ris\xc3\xb4metro esteja sorrindo!'
InventoryTotalGags = 'Total de piadas\n%d / %d'
InventroyPinkSlips = '%s Bilhetes Azuis'
InventroyPinkSlip = '1 Bilhete Azul'
InventoryDelete = 'EXCLUIR'
InventoryDone = 'OK'
InventoryDeleteHelp = 'Clique em uma piada para EXCLUIR.'
InventorySkillCredit = 'Cr\xc3\xa9dito de habilidades:\n%s'
InventorySkillCreditNone = 'Cr\xc3\xa9dito de habilidades:\nNenhum'
InventoryDetailAmount = '%(numItems)s / %(maxItems)s'
InventoryDetailData = 'Precis\xc3\xa3o: %(accuracy)s\n%(damageString)s: %(damage)d\n%(singleOrGroup)s'
InventoryTrackExp = '%(curExp)s / %(nextExp)s'
InventoryUberTrackExp = 'Faltam %(nextExp)s!'
InventoryGuestExp = 'Limite de Visitantes'
GuestLostExp = ' Acima do Limite de Visitantes'
InventoryAffectsOneCog = 'Afeta: Um ' + Cog
InventoryAffectsOneToon = 'Afeta: Um Toon'
InventoryAffectsAllToons = 'Afeta: Todos os Toons'
InventoryAffectsAllCogs = 'Afeta: Todos os ' + Cogs
InventoryHealString = 'Toonar'
InventoryDamageString = 'Dano'
InventoryBattleMenu = 'MENU DE BATALHA'
InventoryRun = 'CORRER'
InventorySOS = 'SOS'
InventoryPass = 'PASSAR'
InventoryFire = 'Fogo'
InventoryClickToAttack = 'Clique em uma\npiada para\natacar'
InventoryDamageBonus = '(+%d)'
NPCForceAcknowledgeMessage = 'Voc\xc3\xaa deve pegar o bondinho antes de sair.\n\n\n\n\nVoc\xc3\xaa poder\xc3\xa1 encontrar o bondinho ao lado da Loja de Piadas do Pateta.'
NPCForceAcknowledgeMessage2 = 'Muito bem! Voc\xc3\xaa completou a busca pelo bondinho!\nVisite o Quartel dos Toons para solicitar a sua recompensa.\n\n\n\n\n\nO Quartel dos Toons localiza-se pr\xc3\xb3ximo ao centro do p\xc3\xa1tio.'
NPCForceAcknowledgeMessage3 = 'Lembre-se de pegar o bondinho.\n\n\n\nVoc\xc3\xaa pode encontrar o bondinho ao lado da Loja de Piadas do Pateta.'
NPCForceAcknowledgeMessage4 = 'Parab\xc3\xa9ns! Voc\xc3\xaa concluiu a sua primeira Tarefa Toon!\n\n\n\n\n\n\n\n\nVisite o Quartel dos Toons para solicitar a sua recompensa.'
NPCForceAcknowledgeMessage5 = 'N\xc3\xa3o se esque\xc3\xa7a de sua Tarefa Toon!\n\n\n\n\n\n\n\n\n\n\nVoc\xc3\xaa pode encontrar Cogs para serem derrotados do outro lado de t\xc3\xbaneis como este.'
NPCForceAcknowledgeMessage6 = 'Excelente trabalho derrotando esses Cogs!\n\n\n\n\n\n\n\n\nVolte para o Quartel dos Toons o mais r\xc3\xa1pido poss\xc3\xadvel.'
NPCForceAcknowledgeMessage7 = 'N\xc3\xa3o se esque\xc3\xa7a de fazer um amigo!\n\n\n\n\n\n\nClique em outro jogador e use o bot\xc3\xa3o Novo amigo.'
NPCForceAcknowledgeMessage8 = '\xc3\x93timo! Voc\xc3\xaa fez um novo amigo!\n\n\n\n\n\n\n\n\nAgora, voc\xc3\xaa deve voltar para o Quartel dos Toons.'
NPCForceAcknowledgeMessage9 = 'Bom trabalho usando o telefone!\n\n\n\n\n\n\n\n\nVolte para o Quartel dos Toons para pedir a sua recompensa.'
ToonSleepString = '. . . ZZZ . . .'
MovieTutorialReward1 = 'Voc\xc3\xaa recebeu 1 ponto de Lan\xc3\xa7amento! Quando voc\xc3\xaa obt\xc3\xa9m 10, ganha uma nova piada!'
MovieTutorialReward2 = 'Voc\xc3\xaa recebeu 1 ponto de Esguicho! Quando voc\xc3\xaa obt\xc3\xa9m 10, ganha uma nova piada!'
MovieTutorialReward3 = 'Muito bom! Voc\xc3\xaa concluiu a sua primeira Tarefa Toon!'
MovieTutorialReward4 = 'V\xc3\xa1 para o Quartel dos Toons para pegar a sua recompensa!'
MovieTutorialReward5 = 'Divirta-se!'
BattleGlobalTracks = [
    'toonar',
    'armadilha',
    'isca',
    'sonora',
    'lan\xc3\xa7amento',
    'esguicho',
    'cadente']
BattleGlobalNPCTracks = [
    'reabastecer',
    'toons atingidos',
    'cogs n\xc3\xa3o-atingidos']
BattleGlobalAvPropStrings = (('Pena', 'Megafone', 'Batom', 'Bengala', 'P\xc3\xb3 m\xc3\xa1gico', 'Bolinhas de malabarismo', 'Mergulho Elevado'), ('Casca de banana', 'Ancinho', 'Bolas de gude', 'Areia movedi\xc3\xa7a', 'Al\xc3\xa7ap\xc3\xa3o', 'TNT', 'Estrada De Ferro'), ('Nota de $1', '\xc3\x8dm\xc3\xa3 pequeno', 'Nota de $5', '\xc3\x8dm\xc3\xa3 grande', 'Nota de $10', '\xc3\x93culos hipn\xc3\xb3ticos', 'Presenta\xc3\xa7\xc3\xa3o'), ('Buzina de bicicleta', 'Apito', 'Trombeta', 'Foooonnnn!', 'Tromba de elefante', 'Buzina', 'Cantor de \xc3\x93pera'), ('Bolinho', 'Fatia de torta de frutas', 'Fatia de torta de creme', 'Torta de frutas inteira', 'Torta de creme inteira', 'Bolo de anivers\xc3\xa1rio', 'Bolo de Casamento'), ('Flor com esguicho', "Copo d'\xc3\xa1gua", 'Rev\xc3\xb3lver de \xc3\xa1gua', 'Garrafa de \xc3\xa1gua com g\xc3\xa1s', 'Mangueira de inc\xc3\xaandio', 'Nuvem de chuva', 'G\xc3\xaaiser'), ('Vaso de flor', 'Saco de areia', 'Bigorna', 'Peso pesado', 'Cofre', 'Piano de cauda', 'Toontanic'))
BattleGlobalAvPropStringsSingular = (('uma Pena', 'um Megafone', 'um Batom', 'uma Bengala', 'um P\xc3\xb3 m\xc3\xa1gico', 'um conjunto de Bolinhas de malabarismo', 'um Mergulho Elevado'), ('uma Casca de banana', 'um Ancinho', 'um conjunto de Bolas de gude', 'uma po\xc3\xa7a de Areia movedi\xc3\xa7a', 'um Al\xc3\xa7ap\xc3\xa3o', 'um TNT', 'uma Estrada de Ferro'), ('uma Nota de $1', 'um \xc3\x8dm\xc3\xa3 pequeno', 'uma Nota de $5', 'um \xc3\x8dm\xc3\xa3 grande', 'uma Nota de $10', 'um par de \xc3\x93culos hipn\xc3\xb3ticos', 'uma Presenta\xc3\xa7\xc3\xa3o'), ('uma Buzina de bicicleta', 'um Apito', 'uma Trombeta', 'um Foooonnnn!', 'uma Tromba de elefante', 'uma Buzina', 'um Cantor de \xc3\x93pera'), ('um Bolinho', 'uma Fatia de torta de frutas', 'uma Fatia de torta de creme', 'uma Torta de frutas inteira', 'uma Torta de creme inteira', 'um Bolo de Casamento'), ('uma Flor com esguicho', "um Copo d'\xc3\xa1gua", 'um Rev\xc3\xb3lver de \xc3\xa1gua', 'uma Garrafa de \xc3\xa1gua com g\xc3\xa1s', 'uma Mangueira de inc\xc3\xaandio', 'uma Nuvem de chuva', 'um G\xc3\xaaiser'), ('um Vaso de flor', 'um Saco de areia', 'uma Bigorna', 'um Peso pesado', 'um Cofre', 'um Piano de cauda', 'the Toontanic'))
BattleGlobalAvPropStringsPlural = (('Penas', 'Megafones', 'Batons', 'Bengalas', 'P\xc3\xb3s m\xc3\xa1gicos', 'conjuntos de Bolinhas de malabarismo', 'Mergulhos Elevados'), ('Cascas de banana', 'Ancinhos', 'conjuntos de Bolas de gude', 'po\xc3\xa7as de Areia movedi\xc3\xa7a', 'Al\xc3\xa7ap\xc3\xb5es', 'TNTs', 'Estradas de Ferro'), ('Notas de $1', '\xc3\x8dm\xc3\xa3s pequenos', 'Contas de $5', '\xc3\x8dm\xc3\xa3s grandes', 'Contas de $10', 'par de \xc3\x93culos hipn\xc3\xb3ticos', 'Presenta\xc3\xa7\xc3\xa3o'), ('Buzinas de bicicleta', 'Apitos', 'Trombetas', 'Foooonnnns!', 'Trombas de elefante', 'Buzinas', 'Cantor de \xc3\x93pera'), ('Bolinhos', 'Fatias de torta de frutas', 'Fatias de torta de creme', 'Tortas de frutas inteiras', 'Tortas de creme inteiras', 'Bolos de anivers\xc3\xa1rio', 'Bolo de Casamento'), ('Flores com esguicho', "Copos d'\xc3\xa1gua", 'Rev\xc3\xb3lveres de \xc3\xa1gua', 'Garrafas de \xc3\xa1gua com g\xc3\xa1s', 'Mangueiras de inc\xc3\xaandio', 'Nuvens de chuva', 'G\xc3\xaaiser'), ('Vasos de flor', 'Sacos de areia', 'Bigornas', 'Pesos pesados', 'Cofres', 'Pianos de cauda', 'Transatl\xc3\xa2nticos'))
BattleGlobalAvTrackAccStrings = ('M\xc3\xa9dio', 'Perfeito', 'Baixo', 'Alto', 'M\xc3\xa9dio', 'Alto', 'Baixo')
BattleGlobalLureAccLow = 'Baixo'
BattleGlobalLureAccMedium = 'M\xc3\xa9dio'
AttackMissed = 'PERDEU'
NPCCallButtonLabel = 'CHAMAR'
LoaderLabel = 'Carregando...'
HeadingToHood = 'Indo %(to)s %(hood)s...'
HeadingToYourEstate = 'Indo para a sua propriedade...'
HeadingToEstate = 'Indo para a propriedade de %s...'
HeadingToFriend = 'Indo para a propriedade do amigo de %s...'
HeadingToPlayground = 'Indo para o P\xc3\xa1tio...'
HeadingToStreet = 'Indo %(to)s %(street)s...'
TownBattleRun = 'Voltar correndo para o p\xc3\xa1tio?'
TownBattleChooseAvatarToonTitle = 'QUAL TOON?'
TownBattleChooseAvatarCogTitle = 'QUAL ' + string.upper(Cog) + '?'
TownBattleChooseAvatarBack = 'VOLTAR'
FireCogTitle = 'BILHETES AZUIS RESTANTES:%s\nQUAL COG DEMITIR?'
FireCogLowTitle = 'BILHETES AZUIS RESTANTES:%s\nSEM BILHETES SUFICIENTES!'
TownBattleSOSNoFriends = 'N\xc3\xa3o h\xc3\xa1 amigos para chamar!'
TownBattleSOSWhichFriend = 'Chamar qual amigo?'
TownBattleSOSNPCFriends = 'Toons resgatados'
TownBattleSOSBack = 'VOLTAR'
TownBattleToonSOS = 'SOS'
TownBattleToonFire = 'Disparar'
TownBattleUndecided = '?'
TownBattleHealthText = '%(hitPoints)s/%(maxHit)s'
TownBattleWaitTitle = 'Aguardando\noutros jogadores...'
TownSoloBattleWaitTitle = 'Aguarde...'
TownBattleWaitBack = 'VOLTAR'
TownBattleSOSPetSearchTitle = 'Procurando rabisco\n%s...'
TownBattleSOSPetInfoTitle = '%s est\xc3\xa1 %s'
TownBattleSOSPetInfoOK = lOK
TrolleyHFAMessage = 'Voc\xc3\xaa n\xc3\xa3o pode embarcar no bondinho at\xc3\xa9 que o seu Ris\xc3\xb4metro esteja sorrindo.'
TrolleyTFAMessage = '\\Voc\xc3\xaa n\xc3\xa3o pode embarcar no bondinho at\xc3\xa9 que o ' + Mickey + ' permita.'
TrolleyHopOff = 'Descer'
FishingExit = 'Sair'
FishingCast = 'Lan\xc3\xa7ar'
FishingAutoReel = 'Molinete autom\xc3\xa1tico'
FishingItemFound = 'Voc\xc3\xaa pegou:'
FishingCrankTooSlow = 'Muito\ndevagar'
FishingCrankTooFast = 'Muito\nr\xc3\xa1pido'
FishingFailure = 'Voc\xc3\xaa n\xc3\xa3o pegou nada!'
FishingFailureTooSoon = 'N\xc3\xa3o comece a rebobinar a linha at\xc3\xa9 que voc\xc3\xaa veja uma pequena mordida. Espere a b\xc3\xb3ia balan\xc3\xa7ar para cima e para baixo rapidamente!'
FishingFailureTooLate = 'Rebobine a linha enquanto o peixe ainda est\xc3\xa1 mordendo a isca!'
FishingFailureAutoReel = 'O molinete autom\xc3\xa1tico n\xc3\xa3o funcionou desta vez. Gire a manivela manualmente, na velocidade certa, para ter mais chance de pegar alguma coisa!'
FishingFailureTooSlow = 'Voc\xc3\xaa girou a manivela muito devagar. Alguns peixes s\xc3\xa3o mais r\xc3\xa1pidos do que outros. Tente manter a barra de velocidade centralizada!'
FishingFailureTooFast = 'Voc\xc3\xaa girou a manivela muito r\xc3\xa1pido. Alguns peixes s\xc3\xa3o mais lentos do que outros. Tente manter a barra de velocidade centralizada!'
FishingOverTankLimit = 'O seu balde de pesca est\xc3\xa1 cheio. V\xc3\xa1 vender os seus peixes para o Vendedor da Loja de Animais e volte.'
FishingBroke = 'Voc\xc3\xaa n\xc3\xa3o tem mais balinhas para as iscas! Para ganhar mais balinhas, pegue o bondinho ou venda os peixes para os Vendedores da Loja de Animais.'
FishingHowToFirstTime = 'Clique e arraste para baixo no bot\xc3\xa3o Lan\xc3\xa7ar. Quanto mais baixo voc\xc3\xaa arrastar, mais forte ser\xc3\xa1 o lan\xc3\xa7amento. Ajuste o \xc3\xa2ngulo para acertar os alvos dos peixes.\n\nTente agora!'
FishingHowToFailed = 'Clique e arraste para baixo no bot\xc3\xa3o Lan\xc3\xa7ar. Quanto mais baixo voc\xc3\xaa arrastar, mais forte ser\xc3\xa1 o lan\xc3\xa7amento. Ajuste o \xc3\xa2ngulo para acertar os alvos dos peixes.\n\nTente agora de novo!'
FishingBootItem = 'Bota velha'
FishingJellybeanItem = '%s balinhas'
FishingNewEntry = 'Novas esp\xc3\xa9cies!'
FishingNewRecord = 'Novo recorde!'
FishPokerCashIn = 'Morrer\n%s\n%s'
FishPokerLock = 'Bloquear'
FishPokerUnlock = 'Desbloquear'
FishPoker5OfKind = '5 de um naipe'
FishPoker4OfKind = '4 de um naipe'
FishPokerFullHouse = 'Full House'
FishPoker3OfKind = '3 de um naipe'
FishPoker2Pair = '2 pares'
FishPokerPair = 'Par'
TutorialGreeting1 = 'Oi %s!'
TutorialGreeting2 = 'Oi %s!\nVem c\xc3\xa1!'
TutorialGreeting3 = 'Oi %s!\nVem c\xc3\xa1!\nUse as teclas de seta!'
TutorialMickeyWelcome = 'Bem-vindo a Toontown!'
TutorialFlippyIntro = 'Deixe-me apresentar voc\xc3\xaa ao meu amigo ' + Flippy + '...'
TutorialFlippyHi = 'Oi, %s!'
TutorialQT1 = 'Voc\xc3\xaa pode conversar usando isto.'
TutorialQT2 = 'Voc\xc3\xaa pode conversar usando isto.\nClique no item e escolha "Oi".'
TutorialChat1 = 'Voc\xc3\xaa pode conversar usando qualquer um destes bot\xc3\xb5es.'
TutorialChat2 = 'O bot\xc3\xa3o azul permite que voc\xc3\xaa converse usando o teclado.'
TutorialChat3 = 'Cuidado! A maior parte dos outros jogadores n\xc3\xa3o entender\xc3\xa1 o que voc\xc3\xaa est\xc3\xa1 dizendo se usar o teclado.'
TutorialChat4 = 'O bot\xc3\xa3o verde abre o %s.'
TutorialChat5 = 'Todos entender\xc3\xa3o se voc\xc3\xaa usar o %s.'
TutorialChat6 = 'Tente dizer "Oi".'
TutorialBodyClick1 = 'Muito bem!'
TutorialBodyClick2 = 'Muito prazer! Quer ser meu amigo?'
TutorialBodyClick3 = 'Para fazer amizade com ' + Flippy + ', clique nele...'
TutorialHandleBodyClickSuccess = 'Muito bom!'
TutorialHandleBodyClickFail = 'N\xc3\xa3o \xc3\xa9 assim. Tente clicar em cima do ' + Flippy + '...'
TutorialFriendsButton = "Agora, clique no bot\xc3\xa3o 'Amigos' abaixo da figura do " + Flippy + ' no canto direito.'
TutorialHandleFriendsButton = "Em seguida, clique no bot\xc3\xa3o 'Sim'.."
TutorialOK = lOK
TutorialYes = lYes
TutorialNo = lNo
TutorialFriendsPrompt = 'Voc\xc3\xaa quer fazer amizade com o ' + Flippy + '?'
TutorialFriendsPanelMickeyChat = Flippy + " aceitou ser seu amigo. Clique em 'Ok' para concluir."
TutorialFriendsPanelYes = Flippy + ' disse sim!'
TutorialFriendsPanelNo = 'Isso n\xc3\xa3o foi muito simp\xc3\xa1tico!'
TutorialFriendsPanelCongrats = 'Parab\xc3\xa9ns! Voc\xc3\xaa fez seu primeiro amigo.'
TutorialFlippyChat1 = 'Venha me ver quando estiver pronto para a sua primeira Tarefa Toon!'
TutorialFlippyChat2 = 'Estarei na PrefeiToona!'
TutorialAllFriendsButton = 'Voc\xc3\xaa pode ver todos os seus amigos clicando no bot\xc3\xa3o Amigos. Experimente...'
TutorialEmptyFriendsList = 'No momento, a sua lista est\xc3\xa1 vazia porque o ' + Flippy + ' n\xc3\xa3o \xc3\xa9 um jogador real.'
TutorialCloseFriendsList = "Clique no bot\xc3\xa3o 'Fechar'\npara fazer que a\nlista desapare\xc3\xa7a"
TutorialShtickerButton = 'O bot\xc3\xa3o do canto direito inferior abre o seu \xc3\x81lbum Toon. Experimente...'
TutorialBook1 = 'O \xc3\xa1lbum cont\xc3\xa9m v\xc3\xa1rias informa\xc3\xa7\xc3\xb5es \xc3\xbateis, como este mapa de Toontown.'
TutorialBook2 = 'Voc\xc3\xaa tamb\xc3\xa9m pode verificar o andamento de suas Tarefas Toon.'
TutorialBook3 = 'Quando voc\xc3\xaa estiver pronto, clique no bot\xc3\xa3o do \xc3\xa1lbum novamente, para fech\xc3\xa1-lo'
TutorialLaffMeter1 = 'Voc\xc3\xaa tamb\xc3\xa9m precisar\xc3\xa1 disto...'
TutorialLaffMeter2 = 'Voc\xc3\xaa tamb\xc3\xa9m precisar\xc3\xa1 disto...\n\xc3\x89 o seu Ris\xc3\xb4metro.'
TutorialLaffMeter3 = 'Quando os ' + Cogs + ' atacarem voc\xc3\xaa, ele diminui.'
TutorialLaffMeter4 = 'Quando voc\xc3\xaa est\xc3\xa1 em p\xc3\xa1tios como este, ele volta a subir.'
TutorialLaffMeter5 = 'Quando concluir as Tarefas Toon, voc\xc3\xaa obter\xc3\xa1 recompensas, como o aumento do seu Limite de risadas.'
TutorialLaffMeter6 = 'Cuidado! Se os ' + Cogs + ' derrotarem voc\xc3\xaa, perder\xc3\xa1 todas as suas piadas.'
TutorialLaffMeter7 = 'Para obter mais piadas, divirta-se com os jogos no bondinho.'
TutorialTrolley1 = 'Siga-me at\xc3\xa9 o bondinho!'
TutorialTrolley2 = 'Pule nele!'
TutorialBye1 = 'Brinque com alguns jogos!'
TutorialBye2 = 'Divirta-se com alguns jogos!\nCompre algumas piadas!'
TutorialBye3 = '\\V\xc3\xa1 encontrar o  ' + Flippy + ' quando terminar!'
TutorialForceAcknowledgeMessage = '\\Voc\xc3\xaa est\xc3\xa1 indo na dire\xc3\xa7\xc3\xa3o errada! \\V\xc3\xa1 encontrar o  ' + Mickey + '!'
PetTutorialTitle1 = 'O Painel dos Rabiscos'
PetTutorialTitle2 = 'Chat r\xc3\xa1pido dos Rabiscos'
PetTutorialTitle3 = 'Gad\xc3\xa1logo dos Rabiscos'
PetTutorialNext = 'Pr\xc3\xb3xima P\xc3\xa1gina'
PetTutorialPrev = 'P\xc3\xa1gina Anterior'
PetTutorialDone = lOK
PetTutorialPage1 = 'Clique em um Rabisco para exibir o painel de Rabiscos. Daqui, voc\xc3\xaa pode alimentar, co\xc3\xa7ar e chamar o Rabisco.'
PetTutorialPage2 = "Use a nova \xc3\xa1rea 'Bichinhos' no menu Chat r\xc3\xa1pido para fazer com que um Rabisco fa\xc3\xa7a um truque. Se ele fizer, recompense-o para ele melhorar ainda mais!"
PetTutorialPage3 = 'Compre novos truques de Rabiscos no Gad\xc3\xa1logo da Clarabela. Truques melhores produzem Toonar melhores!'

def getPetGuiAlign():
    TextNode = TextNode
    import pandac.PandaModules
    return TextNode.ACenter

GardenTutorialTitle1 = 'Jardinagem'
GardenTutorialTitle2 = 'Flores'
GardenTutorialTitle3 = '\xc3\x81rvores'
GardenTutorialTitle4 = 'Instru\xc3\xa7\xc3\xb5es'
GardenTutorialTitle5 = 'Est\xc3\xa1tuas'
GardenTutorialNext = 'Pr\xc3\xb3xima P\xc3\xa1gina'
GardenTutorialPrev = 'P\xc3\xa1gina Anterior'
GardenTutorialDone = lOK
GardenTutorialPage1 = 'Crie o seu pr\xc3\xb3prio jardim bot\xc3\xa2nico!  Voc\xc3\xaa pode plantar flores e \xc3\xa1rvores, e at\xc3\xa9 erguer est\xc3\xa1tuas.'
GardenTutorialPage2 = 'As flores s\xc3\xa3o sens\xc3\xadveis, e voc\xc3\xaa precisa descobrir as suas receitas de balinhas.  Plante todos os tipos para melhorar as risadas, e venda as flores para ganhar balinhas.'
GardenTutorialPage3 = 'Use uma piada para plantar uma \xc3\xa1rvore.  Alguns dias depois, essa piada vai melhorar!!  Mas cuide bem da sa\xc3\xbade dela, ou a melhoria se vai.'
GardenTutorialPage4 = 'Para plantar, regar, cavar ou fazer a colheita no seu jardim, ande at\xc3\xa9 estes locais.'
GardenTutorialPage5 = 'Est\xc3\xa1tuas podem ser compradas no Cat\xc3\xa1logo da Clarabela. Aumenta suas habilidades para destravar as est\xc3\xa1tuas mais extravagantes.'
PlaygroundDeathAckMessage = 'Os' + Cogs + ' levaram todas as suas piadas!\n\nVoc\xc3\xaa est\xc3\xa1 triste. Voc\xc3\xaa n\xc3\xa3o pode sair do p\xc3\xa1tio at\xc3\xa9 ficar feliz.'
ForcedLeaveFactoryAckMsg = 'O Supervisor da f\xc3\xa1brica foi derrotado antes de voc\xc3\xaa alcan\xc3\xa7\xc3\xa1-lo. Voc\xc3\xaa n\xc3\xa3o recuperou nenhuma parte do Cog.'
ForcedLeaveMintAckMsg = 'O Supervisor do Andar da Casa da Moeda foi derrotado antes de voc\xc3\xaa alcan\xc3\xa7\xc3\xa1-lo. Voc\xc3\xaa n\xc3\xa3o recuperou nenhuma Grana Cog.'
HeadingToFactoryTitle = 'Dirigindo-se a %s...'
ForemanConfrontedMsg = '%s est\xc3\xa1 lutando com o Supervisor da f\xc3\xa1brica!'
MintBossConfrontedMsg = '%s est\xc3\xa1 lutando com o Supervisor!'
StageBossConfrontedMsg = '%s est\xc3\xa1 lutando com o Funcion\xc3\xa1rio!'
stageToonEnterElevator = '%s \nentrou no elevador'
ForcedLeaveStageAckMsg = 'O Funcion\xc3\xa1rio da Lei foi derrotado antes de voc\xc3\xaa alcan\xc3\xa7\xc3\xa1-lo. Voc\xc3\xaa n\xc3\xa3o recuperou nenhum Aviso de J\xc3\xbari.'
MinigameWaitingForOtherPlayers = 'Aguardando outros jogadores...'
MinigamePleaseWait = 'Aguarde...'
DefaultMinigameTitle = 'T\xc3\xadtulo do minijogo'
DefaultMinigameInstructions = 'Instru\xc3\xa7\xc3\xb5es do minijogo'
HeadingToMinigameTitle = 'Dirigindo-se a %s...'
MinigamePowerMeterLabel = 'Medidor de pot\xc3\xaancia'
MinigamePowerMeterTooSlow = 'Muito\ndevagar'
MinigamePowerMeterTooFast = 'Muito\nr\xc3\xa1pido'
MinigameTemplateTitle = 'Modelo de minijogo'
MinigameTemplateInstructions = 'Este \xc3\xa9 um modelo de minijogo. Use-o para criar novos minijogos.'
CannonGameTitle = 'Jogo do canh\xc3\xa3o'
CannonGameInstructions = 'Atire o seu Toon na torre de \xc3\xa1gua o mais r\xc3\xa1pido que puder. Use o mouse ou as teclas de seta para mirar o canh\xc3\xa3o. Seja r\xc3\xa1pido e ganhe uma grande recompensa para todos!'
CannonGameReward = 'RECOMPENSA'
TwoDGameTitle = 'Fuga dos Cartoons'
TwoDGameInstructions = 'Fuja dos ' + Cog + ' o mais r\xc3\xa1pido que voc\xc3\xaa puder. Use as setas para correr/pular e Ctrl para esguichar ' + Cog + '. Colete ' + Cog + ' tesouros para ganhar mais pontos.'
TwoDGameElevatorExit = 'SA\xc3\x8dDA'
TugOfWarGameTitle = 'Cabo de guerra'
TugOfWarInstructions = 'Toque alternadamente nas teclas de seta para a esquerda e para a direita r\xc3\xa1pido o suficiente para alinhar a barra verde com a linha vermelha. N\xc3\xa3o toque nelas muito devagar, ou voc\xc3\xaa acabar\xc3\xa1 na \xc3\xa1gua!'
TugOfWarGameGo = 'COME\xc3\x87AR!'
TugOfWarGameReady = 'Pronto...'
TugOfWarGameEnd = 'Bom jogo!'
TugOfWarGameTie = 'Voc\xc3\xaa empatou!'
TugOfWarPowerMeter = 'Medidor'
PatternGameTitle = 'Acompanhe a ' + Minnie
PatternGameInstructions = 'A ' + Minnie + ' mostrar\xc3\xa1 uma sequ\xc3\xaancia de dan\xc3\xa7a.' + 'Tente repetir a dan\xc3\xa7a da ' + Minnie + ' exatamente como voc\xc3\xaa v\xc3\xaa usando as teclas de seta!'
PatternGameWatch = 'Observe estes passos de dan\xc3\xa7a...'
PatternGameGo = 'COME\xc3\x87AR!'
PatternGameRight = 'Bom, %s!'
PatternGameWrong = 'Ops!'
PatternGamePerfect = 'Perfeito, %s!'
PatternGameBye = 'Obrigado por jogar!'
PatternGameWaitingOtherPlayers = 'Aguardando outros jogadores...'
PatternGamePleaseWait = 'Aguarde...'
PatternGameFaster = 'Voc\xc3\xaa foi\nmais r\xc3\xa1pido!'
PatternGameFastest = 'Voc\xc3\xaa foi o\nmais r\xc3\xa1pido!'
PatternGameYouCanDoIt = 'Deixa disso!\nVoc\xc3\xaa consegue!'
PatternGameOtherFaster = '\nfoi mais r\xc3\xa1pido!'
PatternGameOtherFastest = '\nfoi o mais r\xc3\xa1pido!'
PatternGameGreatJob = 'Muito bom!'
PatternGameRound = 'Rodada %s!'
PatternGameImprov = 'Voc\xc3\xaa foi muito bem!  Agora Melhore!'
RaceGameTitle = 'Jogo de corrida'
RaceGameInstructions = 'Clique em um n\xc3\xbamero. Escolha bem! Voc\xc3\xaa s\xc3\xb3 avan\xc3\xa7ar\xc3\xa1 se ningu\xc3\xa9m mais escolher o mesmo n\xc3\xbamero.'
RaceGameWaitingChoices = 'Esperando os outros jogadores escolherem...'
RaceGameCardText = '%(name)s aposta: %(reward)s'
RaceGameCardTextBeans = '%(name)s recebe: %(reward)s'
RaceGameCardTextHi1 = '%(name)s \xc3\xa9 um Toon fabuloso!'
RaceGameForwardOneSpace = ' avan\xc3\xa7a 1 espa\xc3\xa7o'
RaceGameForwardTwoSpaces = ' avan\xc3\xa7a 2 espa\xc3\xa7os'
RaceGameForwardThreeSpaces = ' avan\xc3\xa7a 3 espa\xc3\xa7os'
RaceGameBackOneSpace = ' recua 1 espa\xc3\xa7o'
RaceGameBackTwoSpaces = ' recua 2 espa\xc3\xa7os'
RaceGameBackThreeSpaces = ' recua 3 espa\xc3\xa7os'
RaceGameOthersForwardThree = ' todos os outros avan\xc3\xa7am \n3 espa\xc3\xa7os'
RaceGameOthersBackThree = 'todos os outros recuam \n3 espa\xc3\xa7os'
RaceGameInstantWinner = 'Vencedor imediato!'
RaceGameJellybeans2 = '2 balinhas'
RaceGameJellybeans4 = '4 balinhas'
RaceGameJellybeans10 = '10 balinhas!'
RingGameTitle = 'Jogo dos an\xc3\xa9is'
RingGameInstructionsSinglePlayer = 'Tente nadar atrav\xc3\xa9s do n\xc3\xbamero m\xc3\xa1ximo de an\xc3\xa9is %s que conseguir. Para nadar, use as teclas de seta.'
RingGameInstructionsMultiPlayer = 'Tente nadar atrav\xc3\xa9s dos an\xc3\xa9is %s. Os outros jogadores tentar\xc3\xa3o nadar atrav\xc3\xa9s dos outros an\xc3\xa9is coloridos. Para nadar, use as teclas de seta.'
RingGameMissed = 'PERDEU'
RingGameGroupPerfect = 'GRUPO\nPERFEITO!!'
RingGamePerfect = 'PERFEITO!'
RingGameGroupBonus = 'B\xc3\x94NUS DO GRUPO'
ColorRed = 'vermelhos'
ColorGreen = 'verdes'
ColorOrange = 'laranja'
ColorPurple = 'lilases'
ColorWhite = 'brancos'
ColorBlack = 'pretos'
ColorYellow = 'amarelos'
DivingGameTitle = 'Mergulho pro Tesouro'
DivingInstructionsSinglePlayer = 'Tesouros ir\xc3\xa3o aparecer no fundo do lago. Use as setas para nadar. Evite os peixes e leve os tesouros para o barco!'
DivingInstructionsMultiPlayer = ' Tesouros ir\xc3\xa3o aparecer no fundo do lago. Use as setas para nadar. Trabalhem juntos para levar os tesouros para o barco!'
DivingGameTreasuresRetrieved = 'Tesouros Recuperados'
TargetGameTitle = 'Estilingue do Toon'
TargetGameInstructionsSinglePlayer = 'Acerta na velocidade do alvo'
TargetGameInstructionsMultiPlayer = 'Acerta quantos alvos conseguir'
TargetGameBoard = 'Rodada %s - Mantendo o Melhor Placar'
TargetGameCountdown = 'Lan\xc3\xa7amento for\xc3\xa7ado em %s segundos'
TargetGameCountHelp = 'Bata nas setas esquerda e direita para conseguir pot\xc3\xaancia, pare para lan\xc3\xa7ar'
TargetGameFlyHelp = 'Aperte para baixo para abrir o guarda-chuva'
TargetGameFallHelp = 'Use as teclas de seta para aterrissar no alvo'
TargetGameBounceHelp = ' Bater e quicar pode tirar voc\xc3\xaa do alvo'
PhotoGameScoreTaken = '%s: %s\nVoc\xc3\xaa: %s'
PhotoGameScoreBlank = 'Placar: %s'
PhotoGameScoreOther = '\n%s'
PhotoGameScoreYou = '\nMelhor B\xc3\xb4nus!'
TagGameTitle = 'Jogo de pique'
TagGameInstructions = 'Pegue os tesouros. Voc\xc3\xaa n\xc3\xa3o pode pegar os tesouros se o pique estiver com voc\xc3\xaa!'
TagGameYouAreIt = 'Est\xc3\xa1 com voc\xc3\xaa!'
TagGameSomeoneElseIsIt = 'Est\xc3\xa1 com %s!'
MazeGameTitle = 'Jogo do labirinto'
MazeGameInstructions = 'Pegue os tesouros. Tente pegar todos, mas cuidado com os ' + Cogs + '!'
CatchGameTitle = 'Jogo de pegar'
CatchGameInstructions = 'Pegue o m\xc3\xa1ximo de %(fruit)s que conseguir. Cuidado com os ' + Cogs + " e tente n\xc3\xa3o 'pegar' nenhuma %(badThing)s!"
CatchGamePerfect = 'PERFEITO!'
CatchGameApples = 'ma\xc3\xa7\xc3\xa3s'
CatchGameOranges = 'laranjas'
CatchGamePears = 'p\xc3\xaaras'
CatchGameCoconuts = 'cocos'
CatchGameWatermelons = 'melancias'
CatchGamePineapples = 'abacaxis'
CatchGameAnvils = 'bigornas'
PieTossGameTitle = 'Jogo de lan\xc3\xa7amento de tortas'
PieTossGameInstructions = 'Lance as tortas nos alvos.'
PhotoGameInstructions = 'Tire fotos de acordo com os Toons mostrados na parte de baixo. Mire a c\xc3\xa2mera usando o mouse, e clique com o bot\xc3\xa3o esquerdo para tirar uma foto. Aperte Ctrl para aumentar ou reduzir o zoom, e olhe em sua volta com as teclas de seta. Fotos com notas maiores ganham mais pontos!'
PhotoGameTitle = 'Divers\xc3\xa3o Fotogr\xc3\xa1fica'
PhotoGameFilm = 'FILME'
PhotoGameScore = 'Placar da Equipe: %s\n\nMelhores Fotos: %s\n\nPlacar Total: %s'
CogThiefGameTitle = Cog + ' Ladr\xc3\xa3o'
CogThiefGameInstructions = 'Impe\xc3\xa7a que os ' + Cogs + ' roubem nossos barris! Aperte a tecla Ctrl para atirar uma torta. Use as teclas de seta para se mover. Dica: voc\xc3\xaa pode andar nas diagonais.'
CogThiefBarrelsSaved = '%(num)d Barris\nSalvos!'
CogThiefBarrelSaved = '%(num)d Barril\nSalvo!'
CogThiefNoBarrelsSaved = 'Nenhum Barril\nSalvo'
CogThiefPerfect = 'PERFEITO!!'
MinigameRulesPanelPlay = 'JOGAR'
GagShopName = 'Loja de Piadas do Pateta'
GagShopPlayAgain = 'JOGAR\nNOVAMENTE'
GagShopBackToPlayground = 'SAIR DE NOVO \nPARA O P\xc3\x81TIO'
GagShopYouHave = 'Voc\xc3\xaa tem %s balinhas para gastar'
GagShopYouHaveOne = 'Voc\xc3\xaa tem 1 balinha para gastar'
GagShopTooManyProps = 'Sinto muito, voc\xc3\xaa tem muitos acess\xc3\xb3rios'
GagShopDoneShopping = 'FIM DAS\nCOMPRAS'
GagShopTooManyOfThatGag = 'Sinto muito, voc\xc3\xaa j\xc3\xa1 tem %s o suficiente'
GagShopInsufficientSkill = 'Voc\xc3\xaa n\xc3\xa3o tem muita habilidade para isso ainda'
GagShopYouPurchased = 'Voc\xc3\xaa comprou %s'
GagShopOutOfJellybeans = 'Sinto muito, voc\xc3\xaa n\xc3\xa3o tem mais balinhas!'
GagShopWaitingOtherPlayers = 'Aguardando outros jogadores...'
GagShopPlayerDisconnected = '%s desconectou-se'
GagShopPlayerExited = '%s saiu'
GagShopPlayerPlayAgain = 'Jogar novamente'
GagShopPlayerBuying = 'Comprando'
GenderShopQuestionMickey = 'Para criar um Toon menino, clique em mim!'
GenderShopQuestionMinnie = 'Para criar um Toon menina, clique em mim!'
GenderShopFollow = 'Siga-me!'
GenderShopSeeYou = 'Vejo voc\xc3\xaa depois!'
GenderShopBoyButtonText = 'Menino'
GenderShopGirlButtonText = 'Menina'
BodyShopHead = 'Cabe\xc3\xa7a'
BodyShopBody = 'Corpo'
BodyShopLegs = 'Pernas'
ColorShopHead = 'Cabe\xc3\xa7a'
ColorShopBody = 'Corpo'
ColorShopLegs = 'Pernas'
ColorShopToon = 'Toon'
ColorShopParts = 'Partes'
ColorShopAll = 'Tudo'
ClothesShopShorts = 'Short'
ClothesShopShirt = 'Camisa'
ClothesShopBottoms = 'Parte de baixo'
PromptTutorial = 'Parab\xc3\xa9ns!\nVoc\xc3\xaa \xc3\xa9 o(a) mais recente morador(a) de Toontown!\n\nDeseja continuar com o Toontorial ou teletransportar-se diretamente para o Centro de Toontown?'
MakeAToonSkipTutorial = 'Pular Toontorial'
MakeAToonEnterTutorial = 'Acessar Toontorial'
MakeAToonDone = lOK
MakeAToonCancel = lCancel
MakeAToonNext = lNext
MakeAToonLast = 'Voltar'
CreateYourToon = 'Clique nas setas para criar o seu Toon.'
CreateYourToonTitle = 'Crie o seu Toon'
ShapeYourToonTitle = 'Selecione o Tipo'
PaintYourToonTitle = 'Selecione a Cor'
PickClothesTitle = 'Selecione as Roupas'
NameToonTitle = 'Selecione o Nome'
CreateYourToonHead = "Clique nas setas da 'cabe\xc3\xa7a' para escolher animais diferentes."
MakeAToonClickForNextScreen = 'Clique na seta abaixo para ir at\xc3\xa9 a pr\xc3\xb3xima tela.'
PickClothes = 'Clique nas setas para escolher roupas!'
PaintYourToon = 'Clique nas setas para pintar o seu toon!'
MakeAToonYouCanGoBack = 'Voc\xc3\xaa pode voltar para alterar o corpo tamb\xc3\xa9m!'
MakeAFunnyName = 'Escolha um nome engra\xc3\xa7ado para o seu Toon com o jogo Escolha um nome!'
MustHaveAFirstOrLast1 = 'O seu Toon deve ter um nome ou um sobrenome, n\xc3\xa3o \xc3\xa9?'
MustHaveAFirstOrLast2 = 'Voc\xc3\xaa n\xc3\xa3o quer que o seu Toon tenha um nome ou um sobrenome?'
ApprovalForName1 = '\xc3\x89 isso a\xc3\xad, o seu Toon merece um nome muito legal!'
ApprovalForName2 = 'Os nomes de Toons s\xc3\xa3o os nomes mais legais que existem!'
MakeAToonLastStep = '\xc3\x9altima etapa antes de ir para Toontown!'
PickANameYouLike = 'Escolha o nome que quiser!'
TitleCheckBox = 'T\xc3\xadtulo'
FirstCheckBox = 'Primeiro'
LastCheckBox = '\xc3\x9altimo'
RandomButton = 'Aleat\xc3\xb3rio'
ShuffleButton = 'Misturar'
NameShopSubmitButton = 'Enviar'
TypeANameButton = 'Digite um nome'
TypeAName = 'N\xc3\xa3o gostou destes nomes?\nClique aqui -->'
PickAName = 'Tente usar o jogo Escolha um nome!\nClique aqui -->'
PickANameButton = 'Escolha um nome'
RejectNameText = 'Este nome n\xc3\xa3o \xc3\xa9 permitido. Tente novamente.'
WaitingForNameSubmission = 'Enviando o seu nome...'
PetNameMaster = 'PetNameMaster_portuguese.txt'
PetshopUnknownName = 'Nome: ???'
PetshopDescGender = 'Sexo:\t%s'
PetshopDescCost = 'Custo:\t%s balinhas'
PetshopDescTrait = 'Caracter\xc3\xadsticas:\t%s'
PetshopDescStandard = 'Padr\xc3\xa3o'
PetshopCancel = lCancel
PetshopSell = 'Vender peixes'
PetshopAdoptAPet = 'Adotar um Rabisco'
PetshopReturnPet = 'Devolver o Rabisco'
PetshopAdoptConfirm = 'Adotar %s por %d balinhas?'
PetshopGoBack = 'Voltar'
PetshopAdopt = 'Adotar'
PetshopReturnConfirm = 'Devolver %s?'
PetshopReturn = 'Devolver'
PetshopChooserTitle = 'RABISCOS DE HOJE'
PetshopGoHomeText = 'Deseja ir \xc3\xa0 sua propriedade para brincar com seu novo Rabisco?'
NameShopNameMaster = 'NameMaster_portuguese.txt'
NameShopPay = 'Assine j\xc3\xa1!'
NameShopPlay = 'Avalia\xc3\xa7\xc3\xa3o gratuita'
NameShopOnlyPaid = 'Somente usu\xc3\xa1rios pagantes\npodem dar nomes aos seus Toons.\nAt\xc3\xa9 que voc\xc3\xaa se inscreva,\nseu nome ser\xc3\xa1\n'
NameShopContinueSubmission = 'Continuar envio'
NameShopChooseAnother = 'Escolha outro nome'
NameShopToonCouncil = 'O Conselho de Toons\nanalisar\xc3\xa1 o seu\nnome.' + 'A an\xc3\xa1lise pode\nlevar alguns dias.\nEnquanto voc\xc3\xaa espera,\nseu nome ser\xc3\xa1\n'
PleaseTypeName = 'Digite o seu nome:'
AllNewNames = 'Todos os novos nomes\ndevem ser aprovados\npelo Conselho de Toons.'
NameMessages = 'Use sua criatividade e lembre-se:\nnada de nomes relacionados com a Disney, por favor.'
NameShopNameRejected = 'O nome\nenviado foi\nrejeitado.'
NameShopNameAccepted = 'Parab\xc3\xa9ns!\nO nome\nenviado foi\naceito!'
NoPunctuation = 'N\xc3\xa3o \xc3\xa9 permitido usar caracteres de pontua\xc3\xa7\xc3\xa3o nos nomes!'
PeriodOnlyAfterLetter = 'Voc\xc3\xaa pode usar um ponto no nome, mas apenas depois de uma letra.'
ApostropheOnlyAfterLetter = 'Voc\xc3\xaa pode usar um ap\xc3\xb3strofo no nome, mas apenas depois de uma letra.'
NoNumbersInTheMiddle = 'D\xc3\xadgitos num\xc3\xa9ricos podem n\xc3\xa3o aparecer no meio da palavra.'
ThreeWordsOrLess = 'Seu nome deve ter tr\xc3\xaas palavras ou menos.'
CopyrightedNames = ('mickey', 'mickey mouse', 'mickeymouse', 'minnie', 'minnie mouse', 'minniemouse', 'donald', 'donald duck', 'donaldduck', 'pluto', 'goofy')
NumToColor = [
    'Branco',
    'P\xc3\xaassego',
    'Vermelho vivo',
    'Vermelho',
    'Castanho',
    'Siena',
    'Marrom',
    'Canela',
    'Coral',
    'Laranja',
    'Amarelo',
    'Creme',
    'C\xc3\xadtrico',
    'Lim\xc3\xa3o',
    'Verde-\xc3\xa1gua',
    'Verde',
    'Azul-claro',
    'Verde-azul',
    'Azul',
    'Verde-musgo',
    'Azul-turquesa',
    'Azul cinzento',
    'Lil\xc3\xa1s',
    'P\xc3\xbarpura',
    'Rosa',
    'Roxo',
    'Preto']
AnimalToSpecies = {
    'dog': 'Cachorro',
    'cat': 'Gato',
    'mouse': 'Rato',
    'horse': 'Cavalo',
    'rabbit': 'Coelho',
    'duck': 'Pato',
    'monkey': 'Macaco',
    'bear': 'Urso',
    'pig': 'Porco' }
NameTooLong = 'Este nome \xc3\xa9 muito longo. Tente novamente.'
ToonAlreadyExists = 'Voc\xc3\xaa j\xc3\xa1 tem um Toon com o nome %s!'
NameAlreadyInUse = 'Este nome j\xc3\xa1 foi usado!'
EmptyNameError = 'Voc\xc3\xaa deve primeiramente inserir um nome.'
NameError = 'Sinto muito. Este nome n\xc3\xa3o vai funcionar.'
NCTooShort = 'Este nome \xc3\xa9 muito curto.'
NCNoDigits = 'O nome n\xc3\xa3o pode conter n\xc3\xbameros.'
NCNeedLetters = 'Cada palavra do nome deve conter algumas letras.'
NCNeedVowels = 'Cada palavra do nome deve conter algumas vogais.'
NCAllCaps = 'O seu nome n\xc3\xa3o pode estar todo em mai\xc3\xbasculas.'
NCMixedCase = 'Este nome tem muitas letras em mai\xc3\xbasculas.'
NCBadCharacter = "O seu nome n\xc3\xa3o pode conter o caractere '%s'"
NCGeneric = 'Sinto muito, este nome n\xc3\xa3o vai funcionar.'
NCTooManyWords = 'O seu nome n\xc3\xa3o pode ter mais de quatro palavras.'
NCDashUsage = "H\xc3\xadfens podem ser usados apenas para ligar duas palavras(como em 'Bu-Bu')."
NCCommaEdge = 'O seu nome n\xc3\xa3o pode come\xc3\xa7ar ou terminar com v\xc3\xadrgula.'
NCCommaAfterWord = 'Voc\xc3\xaa n\xc3\xa3o pode come\xc3\xa7ar uma palavra com v\xc3\xadrgula.'
NCCommaUsage = 'Este nome n\xc3\xa3o usa v\xc3\xadrgulas corretamente. As v\xc3\xadrgulas devemjuntar duas palavras, como no nome "Dr. Quack, MD".As v\xc3\xadrgulas devem tamb\xc3\xa9m ser seguidas por um espa\xc3\xa7o.'
NCPeriodUsage = 'Este nome n\xc3\xa3o usa pontos corretamente. Os pontos s\xc3\xa3opermitidos somente em palavras como "Sr.", "Sra.", "J.P.", etc.'
NCApostrophes = 'Este nome tem excesso de ap\xc3\xb3strofos.'
RemoveTrophy = 'Quartel dos Toons: Os ' + Cogs + ' dominaram um dos edif\xc3\xadcios que voc\xc3\xaa salvou!'
STOREOWNER_TOOKTOOLONG = 'Precisa de mais tempo para pensar?'
STOREOWNER_GOODBYE = 'Vejo voc\xc3\xaa depois!'
STOREOWNER_NEEDJELLYBEANS = 'Voc\xc3\xaa precisa pegar o bondinho para conseguir algumas balinhas.'
STOREOWNER_GREETING = 'Escolha o que deseja comprar.'
STOREOWNER_BROWSING = 'Voc\xc3\xaa pode olhar, mas precisar\xc3\xa1 de um bilhete de roupas para comprar.'
STOREOWNER_NOCLOTHINGTICKET = 'Para comprar roupas, voc\xc3\xaa precisa de um bilhete de roupas.'
STOREOWNER_NOFISH = 'Volte aqui para vender peixes para a loja de animais e ganhar balinhas.'
STOREOWNER_THANKSFISH = 'Valeu! A loja de animais vai adorar estes aqui. Tchau!'
STOREOWNER_THANKSFISH_PETSHOP = 'Estes tipos s\xc3\xa3o raros! Valeu.'
STOREOWNER_PETRETURNED = 'N\xc3\xa3o se preocupe. Acharemos um bom lar para o seu Rabisco.'
STOREOWNER_PETADOPTED = 'Parab\xc3\xa9ns pelo novo Rabisco! Voc\xc3\xaa pode brincar com ele em sua propriedade.'
STOREOWNER_PETCANCELED = 'Lembre-se, caso veja um Rabisco de seu agrado, adote-o antes que algu\xc3\xa9m o fa\xc3\xa7a!'
STOREOWNER_NOROOM = 'Hmm... Voc\xc3\xaa pode precisar arranjar espa\xc3\xa7o no seu arm\xc3\xa1rio antes de comprar roupas novas.\n'
STOREOWNER_CONFIRM_LOSS = 'O seu arm\xc3\xa1rio est\xc3\xa1 cheio. Voc\xc3\xaa vai perder as roupas que estava vestindo.'
STOREOWNER_OK = lOK
STOREOWNER_CANCEL = lCancel
STOREOWNER_TROPHY = 'Uau! Voc\xc3\xaa pegou %s de %s peixe. Merece um trof\xc3\xa9u e um Acr\xc3\xa9scimo de risadas!'
SuitInvasionBegin1 = lToonHQ + ': Foi iniciada uma Invas\xc3\xa3o de Cogs!!!'
SuitInvasionBegin2 = lToonHQ + ': %s dominaram Toontown!!!'
SuitInvasionEnd1 = lToonHQ + ': A Invas\xc3\xa3o de %s terminou!!!'
SuitInvasionEnd2 = lToonHQ + ': Mais uma vez os Toons salvaram a p\xc3\xa1tria!!!'
SuitInvasionUpdate1 = lToonHQ + ': A Invas\xc3\xa3o de Cogs est\xc3\xa1 agora em %s Cogs!!!'
SuitInvasionUpdate2 = lToonHQ + ': Precisamos derrotar esses %s!!!'
SuitInvasionBulletin1 = lToonHQ + ': H\xc3\xa1 uma Invas\xc3\xa3o de Cogs em andamento!!!'
SuitInvasionBulletin2 = lToonHQ + ': %s dominaram Toontown!!!'
LeaderboardTitle = 'Pelot\xc3\xa3o Toon'
QuestScriptTutorialMickey_1 = 'Toontown ganhou um novo cidad\xc3\xa3o! Voc\xc3\xaa tem piadas de reserva?'
QuestScriptTutorialMickey_2 = 'Claro, %s!'
QuestScriptTutorialMickey_3 = 'O Tutorial Tom vai contar para voc\xc3\xaa tudo sobre os Cogs.\x7Tchauzinho!'
QuestScriptTutorialMickey_4 = 'Vem c\xc3\xa1! Use as teclas de seta para mover-se.'
QuestScriptTutorialMinnie_1 = 'Toontown ganhou um novo cidad\xc3\xa3o! Voc\xc3\xaa tem piadas de reserva?'
QuestScriptTutorialMinnie_2 = 'Claro, %s!'
QuestScriptTutorialMinnie_3 = 'O Tutorial Tom vai contar para voc\xc3\xaa tudo sobre os Cogs.\x7Tchauzinho!'
QuestScript101_1 = 'Estes s\xc3\xa3o os COGS. Eles s\xc3\xa3o rob\xc3\xb4s que est\xc3\xa3o tentando dominar Toontown.'
QuestScript101_2 = 'H\xc3\xa1 v\xc3\xa1rios tipos diferentes de COGS e...'
QuestScript101_3 = '...eles transformam os alegres edif\xc3\xadcios dos Toons...'
QuestScript101_4 = '...em horr\xc3\xadveis edif\xc3\xadcios de Cogs!'
QuestScript101_5 = 'Mas os COGS n\xc3\xa3o aguentam piadas!'
QuestScript101_6 = 'Uma boa piada os deter\xc3\xa1.'
QuestScript101_7 = 'H\xc3\xa1 milhares de piadas, mas, para come\xc3\xa7ar, use estas aqui.'
QuestScript101_8 = 'Ah! Voc\xc3\xaa tamb\xc3\xa9m vai precisar de um Ris\xc3\xb4metro!'
QuestScript101_9 = 'Se o seu Ris\xc3\xb4metro estiver baixo, \xc3\xa9 porque voc\xc3\xaa est\xc3\xa1 triste!'
QuestScript101_10 = 'Um Toon feliz \xc3\xa9 um Toon saud\xc3\xa1vel!'
QuestScript101_11 = 'OH N\xc3\x83O! H\xc3\xa1 um COG na porta da minha loja!'
QuestScript101_12 = 'AJUDE-ME, POR FAVOR! Derrote este COG!'
QuestScript101_13 = 'Esta \xc3\xa9 a sua primeira Tarefa Toon!'
QuestScript101_14 = 'Vamos nessa! V\xc3\xa1 derrotar aquele Puxa-saco!'
QuestScript110_1 = 'Bom trabalho; voc\xc3\xaa derrotou aquele Puxa-saco. Deixe-me dar a voc\xc3\xaa um \xc3\x81lbum Toon...'
QuestScript110_2 = 'O livro \xc3\xa9 cheio de coisas legais.'
QuestScript110_3 = 'Abra-o para eu mostrar a voc\xc3\xaa.'
QuestScript110_4 = 'O mapa mostra o local onde voc\xc3\xaa esteve.'
QuestScript110_5 = 'Vire a p\xc3\xa1gina para ver as suas piadas...'
QuestScript110_6 = '\xc3\x8apa! Voc\xc3\xaa n\xc3\xa3o tem nenhuma piada! Vou passar uma tarefa para voc\xc3\xaa.'
QuestScript110_7 = 'Vire a p\xc3\xa1gina para ver as suas tarefas.'
QuestScript110_8 = 'D\xc3\xaa uma volta no bondinho para ganhar balinhas e poder comprar piadas!'
QuestScript110_9 = 'Para ir at\xc3\xa9 o bondinho, saia pela porta logo atr\xc3\xa1s de mim e siga at\xc3\xa9 o p\xc3\xa1tio.'
QuestScript110_10 = 'Agora, feche o livro e encontre o bondinho!'
QuestScript110_11 = 'Volte para o Quartel dos Toons quando j\xc3\xa1 estiver pronto. Tchau!'
QuestScriptTutorialBlocker_1 = 'Oi, e a\xc3\xad, pessoal?'
QuestScriptTutorialBlocker_2 = 'Al\xc3\xb4?'
QuestScriptTutorialBlocker_3 = 'Ah! Voc\xc3\xaa n\xc3\xa3o sabe usar o Chat r\xc3\xa1pido!'
QuestScriptTutorialBlocker_4 = 'Clique no bot\xc3\xa3o para dizer algo.'
QuestScriptTutorialBlocker_5 = 'Muito bom!\x7O local para onde voc\xc3\xaa est\xc3\xa1 indo tem um monte de Toons para conversar.'
QuestScriptTutorialBlocker_6 = 'Se voc\xc3\xaa quiser conversar com seus amigos usando o teclado, h\xc3\xa1 um outro bot\xc3\xa3o que pode ser usado.'
QuestScriptTutorialBlocker_7 = 'Ele se chama bot\xc3\xa3o "Conversar". Voc\xc3\xaa precisa ser um cidad\xc3\xa3o oficial de Toontown para us\xc3\xa1-lo.'
QuestScriptTutorialBlocker_8 = 'Boa sorte! Vejo voc\xc3\xaa depois!'
QuestScriptGagShop_1 = 'Bem-vindo \xc3\xa0 Loja de Piadas!'
QuestScriptGagShop_1a = 'Aqui \xc3\xa9 o lugar onde os Toons v\xc3\xaam comprar piadas para usar contra os Cogs.'
QuestScriptGagShop_3 = 'Para comprar piadas, clique em bot\xc3\xb5es de piada. Tente pegar algumas agora!'
QuestScriptGagShop_4 = 'Bom! Voc\xc3\xaa pode usar estas piadas nas batalhas contra os Cogs.'
QuestScriptGagShop_5 = 'D\xc3\xaa uma olhada para ver como s\xc3\xa3o as piadas avan\xc3\xa7adas de jogar e de esguichar...'
QuestScriptGagShop_6 = 'Depois que terminar de comprar piadas, clique neste bot\xc3\xa3o para retornar ao P\xc3\xa1tio.'
QuestScriptGagShop_7 = 'Normalmente, voc\xc3\xaa pode usar este bot\xc3\xa3o para participar de outro Jogo no Bondinho...'
QuestScriptGagShop_8 = '...Mas n\xc3\xa3o h\xc3\xa1 tempo para outro jogo agora. Est\xc3\xa3o precisando de voc\xc3\xaa no Quartel dos Toons!'
QuestScript120_1 = 'Muito bem, voc\xc3\xaa encontrou o bondinho!\x7Por falar nisso, voc\xc3\xaa encontrou o Banqueiro Beto?\x7Ele \xc3\xa9 bem guloso por doces.\x7Por que voc\xc3\xaa n\xc3\xa3o se apresenta e leva para ele este chocolate de presente.'
QuestScript120_2 = 'O Banqueiro Beto est\xc3\xa1 l\xc3\xa1 no Banco de Toontown.'
QuestScript121_1 = 'Mmm, obrigado pelo chocolate.\x7Olha s\xc3\xb3, se voc\xc3\xaa me ajudar, eu dou a voc\xc3\xaa uma recompensa.\x7Esses Cogs roubaram as chaves do meu cofre. Derrote os Cogs para encontrar a chave roubada.\x7Quando voc\xc3\xaa encontra-la, traga-a para mim.'
QuestScript130_1 = 'Muito bem, voc\xc3\xaa encontrou o bondinho!\x7Por falar nisso, recebi hoje um pacote para o Professor Paulo.\x7Deve ser o novo giz que ele encomendou.\x7Voc\xc3\xaa pode, por favor, levar para ele?\x7Ele est\xc3\xa1 l\xc3\xa1 na escola.'
QuestScript131_1 = 'Ah, obrigado pelo giz.\x7O qu\xc3\xaa?\x7Esses Cogs roubaram meu quadro-negro. Derrote os Cogs para encontrar meu quadro-negro roubado.\x7Quando encontr\xc3\xa1-lo, traga de volta para mim.'
QuestScript140_1 = 'Muito bem, voc\xc3\xaa encontrou o bondinho!\x7Por falar nisso, tenho um amigo, o Bibliotec\xc3\xa1rio Bino, que \xc3\xa9 uma verdadeira tra\xc3\xa7a de livros.\x7Peguei este livro para ele da \xc3\xbaltima vez em que estive no Porto do Donald.\x7Voc\xc3\xaa podia levar para ele? Em geral, ele fica na Biblioteca.'
QuestScript141_1 = 'Ah, sim, este livro vai quase completar a minha cole\xc3\xa7\xc3\xa3o.\x7Deixe-me ver...\x7\xc3\x8apa...\x7Onde \xc3\xa9 que eu pus os meus \xc3\xb3culos agora?\x7Eu estava com eles um pouco antes de aqueles Cogs invadirem o meu edif\xc3\xadcio.\x7Derrote os Cogs para encontrar meus \xc3\xb3culos roubados.\x7aQuando encontr\xc3\xa1-los, traga de volta para mim para ganhar uma recompensa.'
QuestScript145_1 = 'Estou vendo que voc\xc3\xaa n\xc3\xa3o teve problemas com o bondinho!\x7 Olha s\xc3\xb3, os Cogs roubaram o apagador do nosso quadro-negro.\x7 V\xc3\xa1 para as ruas e lute com os Cogs at\xc3\xa9 recuperar o apagador.\x7 Para encontrar as ruas, passe por um dos t\xc3\xbaneis como este:'
QuestScript145_2 = 'Quando encontrar nosso apagador, traga-o de volta para c\xc3\xa1.\x7N\xc3\xa3o se esque\xc3\xa7a, se precisar de piadas, pegue o bondinho.\x7E se voc\xc3\xaa precisar recuperar Pontos de risadas, colete casquinhas de sorvete no P\xc3\xa1tio.'
QuestScript150_1 = 'Ah... Esta pr\xc3\xb3xima tarefa talvez seja muito dif\xc3\xadcil para voc\xc3\xaa executar sozinho!'
QuestScript150_2 = 'Para fazer amigos, encontre outro jogador e use o bot\xc3\xa3o Novo amigo.'
QuestScript150_3 = 'Depois que voc\xc3\xaa tiver arrumado um amigo, volte aqui.'
QuestScript150_4 = 'Algumas tarefas s\xc3\xa3o muito dif\xc3\xadceis de serem executadas sem ajuda!'
MissingKeySanityCheck = 'Ignore-me'
SellbotBossName = 'V. P. S\xc3\xaanior'
CashbotBossName = 'Diretor Financeiro'
LawbotBossName = 'Juiz-chefe'
BossCogNameWithDept = '%(name)s\n%(dept)s'
BossCogPromoteDoobers = 'Com isto, voc\xc3\xaa est\xc3\xa1 promovido a %s s\xc3\xaanior. Parab\xc3\xa9ns!'
BossCogDoobersAway = {
    's': 'Vai! E fa\xc3\xa7a essa venda!' }
BossCogWelcomeToons = 'Bem-vindos, novos Cogs!'
BossCogPromoteToons = 'Com isto, voc\xc3\xaa est\xc3\xa1 promovido a %s s\xc3\xaanior. Parab--'
CagedToonInterruptBoss = 'Oi! Uhuu! E a\xc3\xad pessoal!'
CagedToonRescueQuery = 'Ent\xc3\xa3o, galera de Toons, voc\xc3\xaas v\xc3\xaam me salvar?'
BossCogDiscoverToons = 'H\xc3\xa3? Toons! Disfar\xc3\xa7ar!'
BossCogAttackToons = 'Atacar!!'
CagedToonDrop = [
    'Bom trabalho! Ele est\xc3\xa1 ficando exausto!',
    'Fique atr\xc3\xa1s dele! Ele est\xc3\xa1 fugindo!',
    'Pessoal, voc\xc3\xaas est\xc3\xa3o se saindo muito bem!',
    'Fant\xc3\xa1stico! Voc\xc3\xaa quase o pegou agora!']
CagedToonPrepareBattleTwo = 'Cuidado, ele est\xc3\xa1 tentando escapar!\x7Ajudem-me todos! Levantem-se aqui e detenham-no!'
CagedToonPrepareBattleThree = 'Maneiro! Estou quase livre!\x7Agora, voc\xc3\xaa precisa atacar o Cog V. P. em pessoa.\x7Tenho um mont\xc3\xa3o de tortas que voc\xc3\xaa pode usar!\x7Pule e toque na parte inferior da minha cela para que eu lhe d\xc3\xaa algumas tortas.\x7Pressione a tecla Insert para jogar as tortas quando voc\xc3\xaa as pegar!'
BossBattleNeedMorePies = 'Voc\xc3\xaa precisa de mais tortas!'
BossBattleHowToGetPies = 'Pule para tocar na cela e pegar mais tortas.'
BossBattleHowToThrowPies = 'Pressione a tecla Insert para jogar tortas!'
CagedToonYippee = 'Iupii!!'
CagedToonThankYou = '\xc3\x89 \xc3\xb3timo estar livre!\x7Obrigado por toda a sua ajuda!\x7Te devo esta.\x7Se, por acaso, voc\xc3\xaa estiver em apuros em alguma batalha, \xc3\xa9 s\xc3\xb3 me chamar!\x7Basta clicar no bot\xc3\xa3o SOS para me chamar.'
CagedToonPromotion = '\x7Olha s\xc3\xb3! Aquele Cog V.P. acabou deixando aqui os seus documentos de promo\xc3\xa7\xc3\xa3o.\x7Vou arquiv\xc3\xa1-los para voc\xc3\xaa na sa\xc3\xadda, para que pegue a promo\xc3\xa7\xc3\xa3o!'
CagedToonLastPromotion = '\x7Uau, voc\xc3\xaa atingiu o n\xc3\xadvel %s no processo Cog!\x7Os Cogs n\xc3\xa3o t\xc3\xaam promo\xc3\xa7\xc3\xa3o maior do que esta.\x7Voc\xc3\xaa n\xc3\xa3o pode mais subir no processo Cog, mas certamente pode continuar salvando os Toons!'
CagedToonHPBoost = '\x7Voc\xc3\xaa salvou um monte de Toons neste quartel.\x7O Conselho de Toons decidiu dar a voc\xc3\xaa outro Ponto de risadas. Parab\xc3\xa9ns!'
CagedToonMaxed = '\x7Vi que voc\xc3\xaa tem o n\xc3\xadvel %s no processo Cog. Impressionante!\x7Em nome do Conselho de Toons, agrade\xc3\xa7o por retornar para salvar mais Toons!'
CagedToonGoodbye = 'Te vejo por a\xc3\xad!'
CagedToonBattleThree = {
    10: 'Belo salto, %(toon)s. Tome aqui algumas tortas!',
    11: 'Oi, %(toon)s! Pegue algumas tortas!',
    12: 'E a\xc3\xad, %(toon)s? Agora, voc\xc3\xaa tem algumas tortas!',
    20: 'Ol\xc3\xa1, %(toon)s! Pule at\xc3\xa9 a minha cela e pegue algumas tortas para jogar!',
    21: 'Oi, %(toon)s! Use a tecla Ctrl para pular e tocar a minha cela!',
    100: 'Pressione a tecla Insert para jogar uma torta.',
    101: 'O medidor de pot\xc3\xaancia azul mostra a altura que a sua torta atinge.',
    102: 'Primeiramente, tente jogar uma torta dentro da lataria dele para melecar seus mecanismos.',
    103: 'Espere at\xc3\xa9 que a porta se abra para jogar uma torta bem l\xc3\xa1 dentro.',
    104: 'Quando ele estiver tonto, bata na cara ou no peito dele para empurr\xc3\xa1-lo para tr\xc3\xa1s!',
    105: 'Voc\xc3\xaa saber\xc3\xa1 se o seu golpe foi bom quando vir o ch\xc3\xa3o colorido.',
    106: 'Se voc\xc3\xaa atingir um Toon com uma torta, ele ganhar\xc3\xa1 um Ponto de risadas!' }
CagedToonBattleThreeMaxGivePies = 12
CagedToonBattleThreeMaxTouchCage = 21
CagedToonBattleThreeMaxAdvice = 106
CashbotBossHadEnough = '\xc3\x89 isso a\xc3\xad! Chega desses Toons irritantes!'
CashbotBossOuttaHere = 'Tenho que pegar o trem!'
ResistanceToonName = 'Mata Rara'
ResistanceToonCongratulations = 'Voc\xc3\xaa conseguiu! Parab\xc3\xa9ns!\x7Voc\xc3\xaa \xc3\xa9 um orgulho para a Resist\xc3\xaancia!\x7Esta \xc3\xa9 uma frase especial que voc\xc3\xaa pode usar quando estiver em apuros:\x7%s\x7Quando voc\xc3\xaa a pronunciar, %s.\x7Mas s\xc3\xb3 pode usar uma vez, portanto, escolha a hora certa!'
ResistanceToonToonupInstructions = 'todos os Toons pr\xc3\xb3ximos a voc\xc3\xaa ganham %s pontos de risadas'
ResistanceToonToonupAllInstructions = 'todos os Toons pr\xc3\xb3ximos a voc\xc3\xaa ganham pontos de risadas completos'
ResistanceToonMoneyInstructions = 'todos os Toons pr\xc3\xb3ximos a voc\xc3\xaa ganham %s balinhas'
ResistanceToonMoneyAllInstructions = 'todos os Toons pr\xc3\xb3ximos a voc\xc3\xaa encher\xc3\xa3o suas jarras de balinhas'
ResistanceToonRestockInstructions = 'todos os Toons pr\xc3\xb3ximos a voc\xc3\xaa v\xc3\xa3o reabastecer suas "%s" piadas'
ResistanceToonRestockAllInstructions = 'todos os Toons pr\xc3\xb3ximos a voc\xc3\xaa v\xc3\xa3o reabastecer todas as suas piadas'
ResistanceToonLastPromotion = '\x7Uau, voc\xc3\xaa atingiu o n\xc3\xadvel %s no processo Cog!\x7Os Cogs n\xc3\xa3o t\xc3\xaam promo\xc3\xa7\xc3\xa3o maior do que esta.\x7Voc\xc3\xaa n\xc3\xa3o pode mais subir no processo Cog, mas, certamente, pode continuar trabalhando para a Resist\xc3\xaancia!'
ResistanceToonHPBoost = '\x7Voc\xc3\xaa trabalhou muito para a Resist\xc3\xaancia.\x7O Conselho de Toons decidiu dar a voc\xc3\xaa outro Ponto de risadas. Parab\xc3\xa9ns!'
ResistanceToonMaxed = '\x7Vejo que voc\xc3\xaa tem o n\xc3\xadvel %s no processo Cog. Impressionante!\x7Em nome do Conselho de Toons, agrade\xc3\xa7o por retornar para salvar mais Toons!'
CashbotBossCogAttack = 'Peguem-nos!!!'
ResistanceToonWelcome = 'Voc\xc3\xaa conseguiu! Siga-me at\xc3\xa9 o cofre-forte antes que o Diretor Financeiro nos ache!'
ResistanceToonTooLate = 'Droga! Estamos atrasados demais!'
CashbotBossDiscoverToons1 = 'Ah-HAH!'
CashbotBossDiscoverToons2 = 'Pensei ter farejado um tooninho por aqui! Impostores!'
ResistanceToonKeepHimBusy = 'Mantenha-o ocupado! Vou montar uma armadilha!'
ResistanceToonWatchThis = 'Olha isso!'
CashbotBossGetAwayFromThat = 'Ei! Afaste-se!'
ResistanceToonCraneInstructions1 = 'Controle um \xc3\xadm\xc3\xa3 subindo no p\xc3\xb3dio.'
ResistanceToonCraneInstructions2 = 'Use as teclas de setas para mover o guindaste e pressione a tecla Ctrl para pegar um objeto.'
ResistanceToonCraneInstructions3 = 'Pegue um cofre com o \xc3\xadm\xc3\xa3 e arranque o capacete de seguran\xc3\xa7a do Diretor Financeiro.'
ResistanceToonCraneInstructions4 = 'Depois de fazer zunir o capacete, pegue um brutamontes desativado e d\xc3\xaa uma pancada na cabe\xc3\xa7a dele!'
ResistanceToonGetaway = 'Ih! Tenho que correr!'
CashbotCraneLeave = 'Deixar o guindaste'
CashbotCraneAdvice = 'Use as teclas de setas para mover o guindaste de p\xc3\xb3rtico.'
CashbotMagnetAdvice = 'Mantenha pressionada a tecla Ctrl para pegar os objetos.'
CashbotCraneLeaving = 'Deixando o guindaste'
MintElevatorRejectMessage = 'N\xc3\xa3o ser\xc3\xa1 poss\xc3\xadvel entrar na Casa da Moeda at\xc3\xa9 que a vestimenta de Cog %s esteja completa.'
BossElevatorRejectMessage = 'Voc\xc3\xaa n\xc3\xa3o pode pegar este elevador at\xc3\xa9 que tenha recebido uma promo\xc3\xa7\xc3\xa3o.'
NotYetAvailable = 'Este elevador ainda n\xc3\xa3o est\xc3\xa1 dispon\xc3\xadvel.'
SellbotRentalSuitMessage = 'Use este Traje de Cog Alugado para que possa se aproximar o suficiente do VP para atac\xc3\xa1-lo.\n\nVoc\xc3\xaa n\xc3\xa3o receber\xc3\xa1 m\xc3\xa9ritos ou promo\xc3\xa7\xc3\xb5es, mas pode resgatar um Toon para uma recompensa SOS!'
SellbotCogSuitNoMeritsMessage = 'Seu disfarce de Rob\xc3\xb4 Vendedor o levar\xc3\xa1 para dentro, mas uma vez que n\xc3\xa3o tem m\xc3\xa9ritos suficientes, voc\xc3\xaa n\xc3\xa3o ser\xc3\xa1 promovido.\n\nSe resgatar o Toon encurralado, voc\xc3\xaa ganhar\xc3\xa1 uma recompensa SOS Toon!'
SellbotCogSuitHasMeritsMessage = '\xc3\x89 a Opera\xc3\xa7\xc3\xa3o: Rob\xc3\xb4 Vendedor Tempestade!\n\nTraga com voc\xc3\xaa 5 ou mais Toons com Trajes de Cog Alugados para derrotar o VP e ganhe cr\xc3\xa9dito para uma recompensa!'
FurnitureTypeName = 'Mob\xc3\xadlia'
PaintingTypeName = 'Pintura'
ClothingTypeName = 'Roupas'
ChatTypeName = 'Frase do Chat r\xc3\xa1pido'
EmoteTypeName = 'Aulas de representa\xc3\xa7\xc3\xa3o'
BeanTypeName = 'Balinhas'
PoleTypeName = 'Vara de pescar'
WindowViewTypeName = 'Vista da janela'
PetTrickTypeName = 'Treinamento de Rabiscos'
GardenTypeName = 'Materiais de Jardim'
RentalTypeName = 'Item de Aluguel'
GardenStarterTypeName = 'Kit de Jardinagem'
NametagTypeName = 'Crach\xc3\xa1'
CatalogItemTypeNames = {
    0: 'INVALID_ITEM',
    1: FurnitureTypeName,
    2: ChatTypeName,
    3: ClothingTypeName,
    4: EmoteTypeName,
    5: 'WALLPAPER_ITEM',
    6: 'WindowViewTypeName',
    7: 'FLOORING_ITEM',
    8: 'MOULDING_ITEM',
    9: 'WAINSCOTING_ITEM',
    10: PoleTypeName,
    11: PetTrickTypeName,
    12: BeanTypeName,
    13: GardenTypeName,
    14: RentalTypeName,
    15: GardenStarterTypeName,
    16: NametagTypeName,
    17: 'TOON_STATUE_ITEM',
    18: 'ANIMATED_FURNITURE_ITEM' }
ShirtStylesDescriptions = {
    'bss1': 'b\xc3\xa1sica',
    'bss2': 'uma listra',
    'bss3': 'colarinho',
    'bss4': 'duas listras',
    'bss5': 'listrada',
    'bss6': 'colarinho com bolso',
    'bss7': 'havaiana',
    'bss8': 'colarinho com 2 bolsos',
    'bss9': 'camisa de boliche',
    'bss10': 'colete (especial)',
    'bss11': 'colarinho com franzidos',
    'bss12': 'camiseta de futebol (especial)',
    'bss13': 'camiseta lightning bolt (especial)',
    'bss14': 'camiseta 19 (especial)',
    'bss15': 'camisa panam\xc3\xa1',
    'gss1': 'b\xc3\xa1sica',
    'gss2': 'uma listra',
    'gss3': 'colarinho',
    'gss4': 'duas listras',
    'gss5': 'colarinho com bolso',
    'gss6': 'estampa de flor',
    'gss7': 'bordado de flor (especial)',
    'gss8': 'colarinho feminino com 2 bolsos ',
    'gss9': 'colete de brim (especial)',
    'gss10': 'camponesa',
    'gss11': 'camponesa com meia listra',
    'gss12': 'camiseta de futebol (especial)',
    'gss13': 'com cora\xc3\xa7\xc3\xb5es',
    'gss14': 'com estrelas (especial)',
    'gss15': 'com flores',
    'c_ss1': 'amarela com capuz - S\xc3\xa9rie 1',
    'c_ss2': 'amarela com palmeira - S\xc3\xa9rie 1',
    'c_ss3': 'roxa com estrelas - S\xc3\xa9rie 2',
    'c_bss1': 'listras azuis (masculina) - S\xc3\xa9rie 1',
    'c_bss2': 'laranja (masculina) - S\xc3\xa9rie 1',
    'c_bss3': 'verde-lim\xc3\xa3o com listra (masculina) - S\xc3\xa9rie 2',
    'c_bss4': 'quimono vermelho com xadrez (masculina) - S\xc3\xa9rie 2',
    'c_gss1': 'azul com listras amarelas (feminina) - S\xc3\xa9rie 1',
    'c_gss2': 'rosa e bege com flor (feminina) - S\xc3\xa9rie 1',
    'c_gss3': 'azul e dourado com listras ondulantes (feminina) - S\xc3\xa9rie 2',
    'c_gss4': 'azul e rosa com arco (feminina) - S\xc3\xa9rie 2',
    'c_gss5': 'quimono azul-piscina com listra (feminina) \xe2\x80\x93 N\xc3\x83O USADO',
    'c_ss4': 'Camiseta tingida (unissex) - S\xc3\xa9rie 3',
    'c_ss5': 'azul-claro com azul e listra branca (masculina) - S\xc3\xa9rie 3',
    'c_ss6': 'camisa de vaqueiro 1 : S\xc3\xa9rie 4',
    'c_ss7': 'camisa de vaqueiro 2 : S\xc3\xa9rie 4',
    'c_ss8': 'camisa de vaqueiro 3 : S\xc3\xa9rie 4',
    'c_ss9': 'camisa de vaqueiro 4 : S\xc3\xa9rie 4',
    'c_ss10': 'camisa de vaqueiro 5 : S\xc3\xa9rie 4',
    'c_ss11': 'camisa de vaqueiro 6 : S\xc3\xa9rie 4',
    'hw_ss1': 'Fantasma de Halloween',
    'hw_ss2': 'Ab\xc3\xb3bora de Halloween',
    'hw_ss3': 'Vampiro de Halloween',
    'hw_ss4': 'Tartaruga de Halloween',
    'wh_ss1': 'Feriado de Inverno 1',
    'wh_ss2': 'Feriado de Inverno 2',
    'wh_ss3': 'Feriado de Inverno 3',
    'wh_ss4': 'Feriado de Inverno 4',
    'vd_ss1': 'Dia dos namorados, rosa com cora\xc3\xa7\xc3\xb5es vermelhos (feminina)',
    'vd_ss2': 'Dia dos namorados, vermelha com cora\xc3\xa7\xc3\xb5es brancos',
    'vd_ss3': 'Dia dos namorados, branca com cora\xc3\xa7\xc3\xb5es alados (masculina)',
    'vd_ss4': 'Dia dos namorados, rosa com cora\xc3\xa7\xc3\xb5es flamejantes',
    'vd_ss5': 'Dia dos namorados 2009, branca com cupido vermelho',
    'vd_ss6': 'Dia dos namorados 2009, azul com verde e cora\xc3\xa7\xc3\xb5es vermelhos',
    'vd_ss7': '2010 Dia dos namorados, red with white wings',
    'sd_ss1': 'Dia de S\xc3\xa3o Patr\xc3\xadcio, camisa com trevo-de-quatro-folhas',
    'sd_ss2': 'Dia de S\xc3\xa3o Patr\xc3\xadcio, camisa com pote de ouro',
    'tc_ss1': 'Concurso de Camiseta, Colete de Pesca',
    'tc_ss2': 'Concurso de Camiseta, Aqu\xc3\xa1rio',
    'tc_ss3': 'Concurso de Camiseta, Pegada 1',
    'tc_ss4': 'Concurso de Camiseta, Pegada 2',
    'tc_ss5': 'Concurso de Camiseta, Shorts de Couro',
    'tc_ss6': 'Concurso de Camiseta, Melancia',
    'tc_ss7': 'Concurso de Camiseta, Camisa de Corrida',
    'tc_ss8': 'T-Shirt Contest, Most Cogs Defeated Shirt',
    'j4_ss1': 'Bandeira de 4 de julho',
    'j4_ss2': 'Fogos de Artif\xc3\xadcio de 4 de julho',
    'c_ss12': 'Cat\xc3\xa1logo s\xc3\xa9rie 7, Verde com bot\xc3\xb5es de amarelos',
    'c_ss13': 'Cat\xc3\xa1logo s\xc3\xa9rie 7, Roxo com flor grande',
    'pj_ss1': 'Camisa de Pijama de banana azul',
    'pj_ss2': 'Camisa de Pijama de chifre vermelho',
    'pj_ss3': 'Camisa de Pijama de \xc3\xb3culos roxos',
    'sa_ss1': 'Camisa Listrada',
    'sa_ss2': 'Camisa de Pesca 1',
    'sa_ss3': 'Camisa de Pesca 2',
    'sa_ss4': 'Camisa de Jardinagem 1',
    'sa_ss5': 'Camisa de Jardinagem 2',
    'sa_ss6': 'Camisa de Festa 1',
    'sa_ss7': 'Camisa de Festa 2',
    'sa_ss8': 'Camisa de Corrida 1',
    'sa_ss9': 'Camisa de Corrida 2',
    'sa_ss10': 'Camisa de Ver\xc3\xa3o 1',
    'sa_ss11': 'Camisa de Ver\xc3\xa3o 2',
    'sa_ss12': 'Camiseta de Golfe 1',
    'sa_ss13': 'Camiseta de Golfe 2',
    'sa_ss14': 'Camiseta de Fantasia de Halloween 1',
    'sa_ss15': 'Camiseta de Fantasia de Halloween 2',
    'sa_ss16': 'Camiseta de Maratona 1',
    'sa_ss17': 'Camiseta de Salvador de Edif\xc3\xadcios 1',
    'sa_ss18': 'Camiseta de Salvador de Edif\xc3\xadcios 2',
    'sa_ss19': 'Camiseta de Tarefa de Toon 1',
    'sa_ss20': 'Camiseta de Tarefa de Toon 2',
    'sa_ss21': 'Camiseta de Bonde 1',
    'sa_ss22': 'Camiseta de Bonde 2',
    'sa_ss23': 'Camiseta de Inverno 1',
    'sa_ss24': 'Camiseta de Fantasia de Halloween 3',
    'sa_ss25': 'Camiseta de Fantasia de Halloween 4',
    'sa_ss26': 'Pr\xc3\xaamio Camiseta Maioria de Cogs Derrotados',
    'sa_ss27': 'Pr\xc3\xaamio Camiseta Maioria de V.P.s Derrotados',
    'sa_ss28': 'Pr\xc3\xaamio Camiseta de Esmagador do Rob\xc3\xb4 Vendedor',
    'sc_1': ' O 1\xc2\xba melhor Cientista ',
    'sc_2': ' O 2\xc2\xba melhor Cientista ',
    'sc_3': ' O 3\xc2\xba melhor Cientista ',
    'sil_1': 'Camiseta Caixa de Correio Engra\xc3\xa7adinha',
    'sil_2': 'Camiseta Lixeira Engra\xc3\xa7adinha',
    'sil_3': 'Camiseta Laborat\xc3\xb3rio Maluco Engra\xc3\xa7adinho',
    'sil_4': 'Camiseta Hidrante Engra\xc3\xa7adinho',
    'sil_5': 'Camiseta Buzina Engra\xc3\xa7adinha',
    'sil_6': 'Camiseta Esmaga Cog Engra\xc3\xa7adinho',
    'sil_7': 'Blusa Festa da Vit\xc3\xb3ria 1',
    'sil_8': 'Blusa Festa da Vit\xc3\xb3ria 2',
    'sb_1': 'Camiseta \xc3\x8dcone do Rob\xc3\xb4 Vendedor ',
    'jb_1': 'Camiseta Balinha',
    'jb_2': 'Camiseta Doodle',
    'emb_us1': 'placeholder emblem shirt 1',
    'emb_us2': 'placeholder emblem shirt 2',
    'emb_us3': 'placeholder emblem shirt 3',
    'cr_1': 'Mailbox Shirt',
    'cr_2': 'Trashcan Shirt',
    'cr_3': 'Loony Labs Shirt',
    'cr_4': 'Hydrant Shirt' }
BottomStylesDescriptions = {
    'bbs1': 'b\xc3\xa1sico com bolsos',
    'bbs2': 'cinto',
    'bbs3': 'cargo',
    'bbs4': 'havaiano',
    'bbs5': 'listras laterais (especial)',
    'bbs6': 'shorts de futebol',
    'bbs7': 'chamas laterais (especial)',
    'bbs8': 'brim',
    'vd_bs1': 'Shorts de dia dos namorados',
    'vd_bs2': 'Verde com cora\xc3\xa7\xc3\xa3o vermelho',
    'vd_bs3': 'Brim azul com cora\xc3\xa7\xc3\xa3o verde e vermelho',
    'c_bs1': 'Laranja com listras laterais azuis',
    'c_bs2': 'Azul com listras e pregas douradas',
    'c_bs5': 'Listras verdes - s\xc3\xa9rie 7',
    'sd_bs1': 'Shorts de Duende de S\xc3\xa3o Patr\xc3\xadcio',
    'pj_bs1': 'Cal\xc3\xa7a de Pijama de banana azul',
    'pj_bs2': 'Cal\xc3\xa7a de Pijama de chifre vermelho',
    'pj_bs3': 'Cal\xc3\xa7a de Pijama de \xc3\xb3culos roxos',
    'wh_bs1': 'Shorts de Feriado de Inverno Estilo 1',
    'wh_bs2': 'Shorts de Feriado de Inverno Estilo 2',
    'wh_bs3': 'Shorts de Feriado de Inverno Estilo 3',
    'wh_bs4': 'Shorts de Feriado de Inverno Estilo 4',
    'sil_bs1': 'Short Esmaga Cog Engra\xc3\xa7adinho',
    'gsk1': 'b\xc3\xa1sica',
    'gsk2': 'bolinhas (especial)',
    'gsk3': 'listras verticais',
    'gsk4': 'listra horizontal',
    'gsk5': 'estampa de flor',
    'gsk6': '2 bolsos (especial)',
    'gsk7': 'saia de brim',
    'gsh1': 'b\xc3\xa1sico com bolsos',
    'gsh2': 'florido',
    'gsh3': 'shorts de brim',
    'c_gsk1': 'saia azul com borda bege e bot\xc3\xa3o ',
    'c_gsk2': 'saia roxa com rosa e fita',
    'c_gsk3': 'saia violeta com amarelo e estrela',
    'vd_gs1': 'Saia vermelha com cora\xc3\xa7\xc3\xb5es',
    'vd_gs2': 'Saia rosa com cora\xc3\xa7\xc3\xb5es',
    'vd_gs3': 'Saia de brim azul com cora\xc3\xa7\xc3\xa3o verde e vermelho',
    'c_gsk4': 'Saia de arco-\xc3\xadris - S\xc3\xa9rie 3',
    'sd_gs1': 'Shorts de dia de S\xc3\xa3o Patr\xc3\xadcio',
    'c_gsk5': 'Saias de vaqueira 1',
    'c_gsk6': 'Saias de vaqueira 2',
    'c_bs3': 'Shorts de caub\xc3\xb3i 1',
    'c_bs4': 'Shorts de caub\xc3\xb3i 2',
    'j4_bs1': 'Shorts de 4 de julho',
    'j4_gs1': 'Saia de 4 de julho',
    'c_gsk7': 'Azul com flor - s\xc3\xa9rie 7',
    'pj_gs1': 'Cal\xc3\xa7a de Pijama de banana azul',
    'pj_gs2': 'Cal\xc3\xa7a de Pijama de chifre vermelho',
    'pj_gs3': 'Cal\xc3\xa7a de Pijama de \xc3\xb3culos roxos',
    'wh_gsk1': 'Saia de Feriado de Inverno Estilo 1',
    'wh_gsk2': 'Saia de Feriado de Inverno Estilo 2',
    'wh_gsk3': 'Saia de Feriado de Inverno Estilo 3',
    'wh_gsk4': 'Saia de Feriado de Inverno Estilo 4',
    'sa_bs1': 'Shorts de Pesca',
    'sa_bs2': 'Shorts de Jardinagem',
    'sa_bs3': 'Shorts de Festa',
    'sa_bs4': 'Shorts de Corrida',
    'sa_bs5': 'Shorts de Ver\xc3\xa3o',
    'sa_bs6': 'Shorts de Golfe 1',
    'sa_bs7': 'Shorts de Fantasia de Halloween 1',
    'sa_bs8': 'Shorts de Fantasia de Halloween 2',
    'sa_bs9': 'Shorts de Salvador de Edif\xc3\xadcios 1',
    'sa_bs10': 'Shorts de Bonde 1',
    'sa_bs11': 'Shorts de Halloween 3',
    'sa_bs12': 'Shorts de Halloween 4',
    'sa_bs13': 'Pr\xc3\xaamio Shorts Destruidor de Sellbot masculino',
    'sa_gs1': 'Saia de Pesca',
    'sa_gs2': 'Saia de Jardinagem',
    'sa_gs3': 'Saia de Festa',
    'sa_gs4': 'Saia de Corrida',
    'sa_gs5': 'Saia de Ver\xc3\xa3o',
    'sa_gs6': 'Saia de Golfe 1',
    'sa_gs7': 'Saia de Fantasia de Halloween 1',
    'sa_gs8': 'Saia de Fantasia de Halloween 2',
    'sa_gs9': 'Saia de Salvadora de Edif\xc3\xadcios 1',
    'sa_gs10': 'Saia de Bonde 1',
    'sa_gs11': 'Saia de Halloween 3',
    'sa_gs12': 'Saia de Halloween 4',
    'sa_gs13': 'Pr\xc3\xaamio Shorts Destruidor de Sellbot feminino',
    'sc_bs1': ' O 1\xc2\xba cientista masculino ',
    'sc_bs2': ' O 2\xc2\xba cientista masculino ',
    'sc_bs3': ' O 3\xc2\xba cientista masculino ',
    'sc_gs1': ' O 1\xc2\xba cientista feminino ',
    'sc_gs2': ' O 2\xc2\xba cientista feminino ',
    'sc_gs3': ' O 3\xc2\xba cientista feminino ',
    'sil_bs1': 'Short masculino Esmaga Cog Engra\xc3\xa7adinho',
    'sil_gs1': 'Short feminino Esmaga Cog Engra\xc3\xa7adinho',
    'hw_bs3': 'Shorts Vampiro de Halloween masculino',
    'hw_gs3': 'Shorts Vampiro de Halloween feminino',
    'hw_bs4': 'Shorts Tartaruga de Halloween masculino',
    'hw_gs4': 'Shorts Tartaruga de Halloween feminino' }
AwardMgrBoy = 'masculino'
AwardMgrGirl = 'feminino'
AwardMgrUnisex = 'unissex'
AwardMgrShorts = 'shorts'
AwardMgrSkirt = 'saia'
AwardMgrShirt = 'camisa'
SpecialEventMailboxStrings = {
    1: 'Um item especial do conselho Toon',
    2: 'Pr\xc3\xaamio do Torneio de Pesca de Melville',
    3: 'Pr\xc3\xaamio do Torneio de Pesca de Billy Bud',
    4: 'Aqui est\xc3\xa1 seu pr\xc3\xaamio pelo Convite de Abril do Bosque de Bolotas! Parab\xc3\xa9ns!',
    5: 'Aqui est\xc3\xa1 seu pr\xc3\xaamio do Campeonato no Bosque de Bolotas! Parab\xc3\xa9ns!',
    6: 'Aqui est\xc3\xa1 seu pr\xc3\xaamio do Festival de Presentes! Parab\xc3\xa9ns!',
    7: 'Aqui est\xc3\xa1 seu pr\xc3\xaamio da Maratona de Ano-Novo dos Toons! Parab\xc3\xa9ns!',
    8: 'Aqui est\xc3\xa1 seu pr\xc3\xaamio do Fim de Semana de Jogos no Bonde! Parab\xc3\xa9ns!',
    9: 'Aqui est\xc3\xa1 seu pr\xc3\xaamio do Festival de Jogos no Bonde! Parab\xc3\xa9ns!',
    10: 'Aqui est\xc3\xa1 seu pr\xc3\xaamio do Fim de Semana Premiado! Parab\xc3\xa9ns!',
    11: 'Aqui est\xc3\xa1 seu pr\xc3\xaamio da Corrida de Cavalos dos Toons!  Parab\xc3\xa9ns!',
    12: 'Aqui est\xc3\xa1 seu pr\xc3\xaamio da Maratona de Salvamento de Edif\xc3\xadcios! Parab\xc3\xa9ns!',
    13: "A\xc3\xad est\xc3\xa1 seu pr\xc3\xaamio do torneio de 'Maioria dos Cogs Derrotados'! Parab\xc3\xa9ns!",
    14: 'Aqui est\xc3\xa1 seu pr\xc3\xaamio do Torneio de Maioria de V.P.s Derrotados! Parab\xc3\xa9ns!',
    15: 'Aqui est\xc3\xa1 seu pr\xc3\xaamio Opera\xc3\xa7\xc3\xa3o: Rob\xc3\xb4 Vendedor Tempestade! Parab\xc3\xa9ns!' }
RentalHours = 'Horas de'
RentalOf = 'De'
RentalCannon = 'Canh\xc3\xb5es!'
RentalTime = 'Horas de'
RentalGameTable = 'Mesa de Jogo!'
EstateCannonGameEnd = 'O aluguel do Jogo de Canh\xc3\xa3o acabou.'
GameTableRentalEnd = 'O per\xc3\xadodo de aluguel do Jogo de Tabuleiro acabou.'
MessageConfirmRent = 'Iniciar o aluguel? Cancele para guardar o aluguel para depois'
MessageConfirmGarden = 'Voc\xc3\xaa quer mesmo iniciar um jardim?'
NametagPaid = 'Crach\xc3\xa1 de Cidad\xc3\xa3o'
NametagAction = 'Crach\xc3\xa1 de A\xc3\xa7\xc3\xa3o'
NametagFrilly = 'Crach\xc3\xa1 Chique'
FurnitureYourOldCloset = 'seu arm\xc3\xa1rio velho'
FurnitureYourOldBank = 'seu banco velho'
ChatItemQuotes = '"%s"'
FurnitureNames = {
    100: 'Poltrona',
    105: 'Poltrona',
    110: 'Cadeira',
    120: 'Cadeira de escrivaninha',
    130: 'Cadeira de jardim',
    140: 'Cadeira lagosta',
    145: 'Cadeira salva-vidas',
    150: 'Banco de sela',
    160: 'Cadeira nativa',
    170: 'Cadeira-bolinho',
    200: 'Cama',
    205: 'Cama',
    210: 'Cama',
    220: 'Cama banheira',
    230: 'Cama de folhas',
    240: 'Cama-barco',
    250: 'Rede de c\xc3\xa1ctus',
    260: 'Cama de sorvete',
    270: "Olivia Erin & Cat's Bed",
    300: 'Pianola',
    310: '\xc3\x93rg\xc3\xa3o de tubo',
    400: 'Lareira',
    410: 'Lareira',
    420: 'Lareira redonda',
    430: 'Lareira',
    440: 'Lareira-ma\xc3\xa7\xc3\xa3',
    450: 'Lareira Irlandesa',
    460: 'Lareira Irlandesa Acesa',
    470: 'Lareira Acesa',
    480: 'Lareira Circular Acesa',
    490: 'Lareira Acesa',
    491: 'Lareira Acesa',
    492: 'Lareira em Forma de Ma\xc3\xa7\xc3\xa3 Acesa',
    500: 'Arm\xc3\xa1rio',
    502: 'Arm\xc3\xa1rio com 15 itens',
    504: 'Arm\xc3\xa1rio com 20 itens',
    506: 'Arm\xc3\xa1rio com 25 itens',
    510: 'Arm\xc3\xa1rio',
    512: 'Arm\xc3\xa1rio com 15 itens',
    514: 'Arm\xc3\xa1rio com 20 itens',
    516: 'Arm\xc3\xa1rio com 25 itens',
    600: 'Abajur pequeno',
    610: 'Abajur grande',
    620: 'Abajur de mesa',
    625: 'Abajur de mesa',
    630: 'Abajur da Margarida',
    640: 'Abajur da Margarida',
    650: 'Abajur da \xc3\x81gua-viva',
    660: 'Abajur da \xc3\x81gua-viva',
    670: 'Abajur do vaqueiro',
    680: 'Vela',
    681: 'Vela Acesa',
    700: 'Cadeira estofada',
    705: 'Cadeira estofada',
    710: 'Sof\xc3\xa1',
    715: 'Sof\xc3\xa1',
    720: 'Sof\xc3\xa1 de feno',
    730: 'Sof\xc3\xa1-torta',
    800: 'Escrivaninha',
    810: 'Mesinha',
    900: 'Porta-guarda-chuva',
    910: 'Cabideiro',
    920: 'Lata de lixo',
    930: 'Cogumelo vermelho',
    940: 'Cogumelo amarelo',
    950: 'Cabideiro',
    960: 'Mesinha-barril',
    970: 'Planta c\xc3\xa1ctus',
    980: 'Tenda',
    990: 'O Fan (Leque) de Julieta',
    1000: 'Tapete grande',
    1010: 'Tapete redondo',
    1015: 'Tapete redondo',
    1020: 'Tapete pequeno',
    1030: 'Capacho de folha',
    1040: 'Presentes',
    1050: 'Tren\xc3\xb3',
    1100: 'Vitrina',
    1110: 'Vitrina',
    1120: 'Estante alta',
    1130: 'Estante baixa',
    1140: 'Arca-sundae',
    1200: 'Mesinha lateral',
    1210: 'Mesa pequena',
    1215: 'Mesa pequena',
    1220: 'Mesinha de centro',
    1230: 'Mesinha de centro',
    1240: 'Mesa Snorkel',
    1250: 'Mesa-biscoito',
    1260: 'Mesa do quarto',
    1300: 'Banco 1.000 Balas',
    1310: 'Banco 2.500 Balas',
    1320: 'Banco 5.000 Balas',
    1330: 'Banco 7.500 Balas',
    1340: 'Banco 10.000 Balas',
    1350: 'Banco 12.000 Balas',
    1399: 'Telefone',
    1400: 'Toon Cezanne',
    1410: 'Flores',
    1420: 'Mickey Moderno',
    1430: 'Toon Rembrandt',
    1440: 'Toonescape',
    1441: 'Cavalo Assobiador',
    1442: 'Estrela Toon',
    1443: 'N\xc3\xa3o \xc3\xa9 Torta',
    1450: 'Mickey \xc3\xa9 Minnie',
    1500: 'R\xc3\xa1dio',
    1510: 'R\xc3\xa1dio',
    1520: 'R\xc3\xa1dio',
    1530: 'Televis\xc3\xa3o',
    1600: 'Vasinho',
    1610: 'Vaso alto',
    1620: 'Vasinho',
    1630: 'Vaso alto',
    1640: 'Vasinho',
    1650: 'Vasinho',
    1660: 'Vaso Coral',
    1661: 'Vaso de concha',
    1670: 'Vaso Rosa',
    1680: 'Regador Rosa',
    1700: 'Carrocinha de pipoca',
    1710: 'Joaninha',
    1720: 'Chafariz',
    1725: 'Lavadora de roupa',
    1800: 'Aqu\xc3\xa1rio',
    1810: 'Aqu\xc3\xa1rio',
    1900: 'Peixe-espada',
    1910: 'Tubar\xc3\xa3o-martelo',
    1920: 'Chifres de pendurar',
    1930: 'Sombreiro simples',
    1940: 'Sombreiro elegante',
    1950: 'Apanhador de sonhos',
    1960: 'Ferradura',
    1970: 'Retrato de b\xc3\xbafalo',
    2000: 'Balan\xc3\xa7o de doces',
    2010: 'Escorregada de torta',
    3000: 'Banheira banana split',
    10000: 'Moranga',
    10010: 'Ab\xc3\xb3bora',
    10020: '\xc3\x81rvore de Natal',
    10030: 'Guirlanda de Natal' }
AwardManagerFurnitureNames = {
    100: 'Poltrona A \xe2\x80\x93 S\xc3\xa9rie 1',
    105: 'Poltrona A \xe2\x80\x93 S\xc3\xa9rie 7',
    110: 'Cadeira \xe2\x80\x93 S\xc3\xa9rie 1',
    120: 'Cadeira de Escrit\xc3\xb3rio \xe2\x80\x93 S\xc3\xa9rie 2',
    130: 'Cadeira de Madeira \xe2\x80\x93 S\xc3\xa9rie 2',
    140: 'Cadeira de Lagosta \xe2\x80\x93 S\xc3\xa9rie 3',
    145: 'Cadeira Salva-vidas \xe2\x80\x93 S\xc3\xa9rie 3',
    150: 'Banco de Sela - S\xc3\xa9rie 4',
    160: 'Cadeira Nativa \xe2\x80\x93 S\xc3\xa9rie 4',
    170: 'Cadeira-Bolinho \xe2\x80\x93 S\xc3\xa9rie 6',
    200: 'Cama de Menino Sonolento \xe2\x80\x93 Mob\xc3\xadlia Inicial',
    205: 'Cama de Menino Sonolento S\xc3\xa9rie \xe2\x80\x93 7',
    210: 'Cama de Menina Sonolenta \xe2\x80\x93 S\xc3\xa9rie 1',
    220: 'Cama-Banheira',
    230: 'Cama-Folha',
    240: 'Cama-Barco',
    250: 'Rede-Cacto',
    260: 'Cama-Sorvete',
    270: 'Cama de Olivia Erin e Gato \xe2\x80\x93 Cama-Bonde',
    300: 'Piano de Jogador',
    310: '\xc3\x93rg\xc3\xa3o',
    400: 'Lareira \xe2\x80\x93 Lareira Quadrada Mob\xc3\xadlia Inicial',
    410: 'Lareira \xe2\x80\x93 Lareira Feminina S\xc3\xa9rie 1',
    420: 'Lareira Redonda',
    430: 'Lareira \xe2\x80\x93 sala de insetos s\xc3\xa9rie 2',
    440: 'Lareira-Ma\xc3\xa7\xc3\xa3',
    450: 'Lareira de Erin \xe2\x80\x93 coral',
    460: 'Lareira Acesa de Erin - coral',
    470: 'Lareira Acesa \xe2\x80\x93 lareira quadrada com fogo',
    480: 'Lareira Redonda Acesa',
    490: 'Lareira Acesa \xe2\x80\x93 lareira de menina com fogo',
    491: 'Lareira Acesa \xe2\x80\x93 lareira da sala de insetos',
    492: 'Lareira Ma\xc3\xa7\xc3\xa3 Acesa',
    500: 'Guarda-roupa de menino \xe2\x80\x93 10 itens iniciais',
    502: 'Guarda-roupa de menino com 15 itens',
    504: 'Guarda-roupa de menino com 20 itens',
    506: 'Guarda-roupa de menino com 25 itens',
    510: 'Guarda-roupa de menina \xe2\x80\x93 10 itens iniciais',
    512: 'Guarda-roupa de menina com 15 itens',
    514: 'Guarda-roupa de menina com 20 itens',
    516: 'Guarda-roupa de menina com 25 itens',
    600: 'L\xc3\xa2mpada Baixa',
    610: 'L\xc3\xa2mpada Alta',
    620: 'L\xc3\xa2mpada de Mesa \xe2\x80\x93 S\xc3\xa9rie 1',
    625: 'L\xc3\xa2mpada de Mesa \xe2\x80\x93 S\xc3\xa9rie 7',
    630: 'L\xc3\xa2mpada da Margarida 1',
    640: 'L\xc3\xa2mpada da Margarida 2',
    650: 'L\xc3\xa2mpada-\xc3\x81gua-viva 1',
    660: 'L\xc3\xa2mpada-\xc3\x81gua-viva 2',
    670: 'L\xc3\xa2mpada de Cowboy',
    680: 'Vela',
    681: 'Vela Acesa',
    700: 'Cadeira com Almofada \xe2\x80\x93 S\xc3\xa9rie 1',
    705: 'Cadeira com Almofada \xe2\x80\x93 S\xc3\xa9rie 7',
    710: 'Sof\xc3\xa1 \xe2\x80\x93 s\xc3\xa9rie 1',
    715: 'Sof\xc3\xa1 \xe2\x80\x93 s\xc3\xa9rie 7',
    720: 'Sof\xc3\xa1 de Feno',
    730: 'Sof\xc3\xa1 Bolinho',
    800: 'Escrivaninha',
    810: 'Escrivaninha de Madeira',
    900: 'Suporte para Guarda-chuva',
    910: 'Porta-casaco \xe2\x80\x93 S\xc3\xa9rie 1',
    920: 'Lata de Lixo',
    930: 'Cogumelo Vermelho',
    940: 'Cogumelo Amarelo',
    950: 'Porta-casaco - aqu\xc3\xa1tico',
    960: 'Suporte para Barril',
    970: 'Cacto',
    980: 'Tenda',
    990: 'F\xc3\xa3 de Juliette \xe2\x80\x93 f\xc3\xa3 de brincadeira',
    1000: 'Tapete Grande',
    1010: 'Tapete Redondo \xe2\x80\x93 S\xc3\xa9rie 1',
    1015: 'Tapete Redondo \xe2\x80\x93 S\xc3\xa9rie 7',
    1020: 'Tapete Pequeno',
    1030: 'Tapete-Folha',
    1040: 'Presentes',
    1050: 'Tren\xc3\xb3',
    1100: 'Vitrine \xe2\x80\x93 Vermelha',
    1110: 'Vitrine \xe2\x80\x93 Amarela',
    1120: 'Estante Alta',
    1130: 'Estante Baixa',
    1140: 'Ba\xc3\xba-Sorvete',
    1200: 'Mesinha',
    1210: 'Mesa Pequena \xe2\x80\x93 s\xc3\xa9rie 1 ',
    1215: 'Mesa Pequena \xe2\x80\x93 s\xc3\xa9rie 7',
    1220: 'Mesa de Caf\xc3\xa9 quadrada',
    1230: 'Mesa de Caf\xc3\xa9 bw',
    1240: 'Mesa-Mergulhador',
    1250: 'Mesa-Biscoito',
    1260: 'Mesa de Quarto',
    1300: 'Banco de 1.000 Balas',
    1310: 'Banco de 2.500 Balas',
    1320: 'Banco de 5.000 Balas',
    1330: 'Banco de 7.500 Balas',
    1340: 'Banco de 10.000 Balas',
    1350: 'Banco de 12.000 Balas',
    1399: 'Telefone',
    1400: 'Toon Cezanne',
    1410: 'Flores',
    1420: 'Mickey Moderno',
    1430: 'Toon Rembrandt',
    1440: 'Fuga dos Toons',
    1441: 'Cavalo do Apitador',
    1442: 'Estrela Toon',
    1443: 'N\xc3\xa3o \xc3\xa9 uma Torta',
    1450: 'Mickey e Minnie',
    1500: 'R\xc3\xa1dio A s\xc3\xa9rie 2',
    1510: 'R\xc3\xa1dio B s\xc3\xa9rie 1',
    1520: 'R\xc3\xa1dio C s\xc3\xa9rie 2',
    1530: 'Televis\xc3\xa3o',
    1600: 'Vaso Baixo A',
    1610: 'Vaso Alto A',
    1620: 'Vaso Baixo B',
    1630: 'Vaso Alto B',
    1640: 'Vaso Baixo C',
    1650: 'Vaso Baixo D',
    1660: 'Vaso Coral',
    1661: 'Vaso-Concha',
    1670: 'Vaso Rosa',
    1680: 'Regador Rosa',
    1700: 'Carrinho de Pipoca',
    1710: 'Joaninha',
    1720: 'Fonte',
    1725: 'M\xc3\xa1quina de Lavar',
    1800: 'Caveira de Aqu\xc3\xa1rio',
    1810: 'Lagarto de Aqu\xc3\xa1rio',
    1900: 'Peixe-espada',
    1910: 'Tubar\xc3\xa3o-martelo',
    1920: 'Chifres Empalhados',
    1930: 'Sombreiro Simples',
    1940: 'Sobreiro Chique',
    1950: 'Apanhador de Sonhos',
    1960: 'Ferradura',
    1970: 'Retrato de Bis\xc3\xa3o',
    2000: 'Balan\xc3\xa7o de Doce',
    2010: 'Escorregador-Bolo',
    3000: 'Banheira-Banana Split',
    10000: 'Ab\xc3\xb3bora Pequena',
    10010: 'Ab\xc3\xb3bora Grande',
    10020: '\xc3\x81rvore de Inverno',
    10030: 'Guirlanda de Inverno' }
ClothingArticleNames = ('Camisa', 'Camisa', 'Camisa', 'Bermuda', 'Bermuda', 'Saia', 'Bermuda')
ClothingTypeNames = {
    1001: 'Camiseta de Fantasma',
    1002: 'Camiseta de Ab\xc3\xb3bora',
    1400: 'Camisa do Mateus',
    1401: 'Camisa da J\xc3\xa9ssica',
    1402: 'Camisa da Marisa',
    1600: 'Traje de Armadilha',
    1601: 'Traje de Som',
    1602: 'Traje de Isca',
    1603: 'Traje de Armadilha',
    1604: 'Traje de Som',
    1605: 'Traje de Isca',
    1606: 'Traje de Armadilha',
    1607: 'Traje de Som',
    1608: 'Traje de Isca',
    1723: 'Camiseta de Abelha',
    1724: 'Camiseta de SuperToon',
    1734: 'Shorts de Abelha',
    1735: 'Shorts de SuperToon',
    1739: 'Saia de Abelha',
    1740: 'Saia de SuperToon',
    1743: 'Camiseta de Esqueleto',
    1744: 'Saia de Aranha',
    1745: 'Shorts de Aranha',
    1746: 'Shorts de Esqueleto',
    1747: 'Saia de Esqueleto',
    1748: 'Saia de Aranha',
    1749: 'Camiseta Caixa de Correio Engra\xc3\xa7adinha',
    1750: 'Camiseta Lixeira Engra\xc3\xa7adinha',
    1751: 'Camiseta Laborat\xc3\xb3rio Maluco Engra\xc3\xa7adinho',
    1752: 'Camiseta Hidrante Engra\xc3\xa7adinho',
    1753: 'Camiseta Medidor de bobagens',
    1754: 'Camiseta Esmaga Cog Engra\xc3\xa7adinho',
    1755: 'Short Esmaga Cog Engra\xc3\xa7adinho',
    1756: 'Short Esmaga Cog Engra\xc3\xa7adinho',
    1757: 'Camiseta Festa da Vit\xc3\xb3ria',
    1758: 'Camiseta Festa da Vit\xc3\xb3ria',
    1763: 'Camiseta Rob\xc3\xb4 Vendedor Destru\xc3\xaddo',
    1764: 'Camiseta Maioria de V.P.s Derrotados',
    1765: 'Camiseta Destruidor do Rob\xc3\xb4 Vendedor',
    1766: 'Shorts Destruidor do Rob\xc3\xb4 Vendedor ',
    1767: 'Shorts Destruidor do Rob\xc3\xb4 Vendedor ',
    1768: 'Camiseta Banco de Balinha',
    1769: 'Camiseta Doodle',
    1770: 'Camiseta de Vampiro',
    1771: 'Camiseta de Tartaruga',
    1772: 'Shorts de Vampiro',
    1773: 'Shorts de Vampiro',
    1774: 'Shorts de Tartaruga',
    1775: 'Shorts de Tartaruga' }
SurfaceNames = ('Papel de parede', 'Moldura do teto', 'Piso', 'Lambri', 'Moldura')
WallpaperNames = {
    1000: 'Pergaminho',
    1100: 'Mil\xc3\xa3o',
    1200: 'Dover',
    1300: 'Vit\xc3\xb3ria',
    1400: 'Newport',
    1500: 'Pastoral',
    1600: 'Arlequim',
    1700: 'Lua',
    1800: 'Estrelas',
    1900: 'Flores',
    2000: 'Jardim de primavera',
    2100: 'Jardim formal',
    2200: 'Dia de corrida',
    2300: 'Gol!',
    2400: 'Nuvem 9',
    2500: 'Trepadeira',
    2600: 'Primavera',
    2700: 'Boneca japonesa',
    2800: 'Arranjo de flores',
    2900: 'Peixe-anjo',
    3000: 'Bolhas',
    3100: 'Bolhas',
    3200: 'Ir pescar',
    3300: 'Parar de pescar',
    3400: 'Cavalo-marinho',
    3500: 'Conchinhas do mar',
    3600: "Debaixo d'\xc3\xa1gua",
    3700: 'Botinas',
    3800: 'C\xc3\xa1ctus',
    3900: 'Chap\xc3\xa9u de vaqueiro',
    10100: 'Gatos',
    10200: 'Morcegos',
    11000: 'Flocos de neve',
    11100: 'Folhas de Natal',
    11200: 'Boneco de neve',
    12000: 'Cart\xc3\xa3o do Dia dos Namorados',
    12100: 'Cart\xc3\xa3o do Dia dos Namorados',
    12200: 'Cart\xc3\xa3o do Dia dos Namorados',
    12300: 'Cart\xc3\xa3o do Dia dos Namorados',
    13000: 'Trevo',
    13100: 'Trevo',
    13200: 'Arco-\xc3\xadris',
    13300: 'Trevo' }
FlooringNames = {
    1000: 'T\xc3\xa1bua-corrida',
    1010: 'Carpete',
    1020: 'Piso em losangos',
    1030: 'Piso em losangos',
    1040: 'Grama',
    1050: 'Tijolinho bege',
    1060: 'Tijolinho vermelho',
    1070: 'Piso quadrado',
    1080: 'Pedra',
    1090: 'Cal\xc3\xa7ada',
    1100: 'Terra',
    1110: 'Sinteco',
    1120: 'Lajota',
    1130: 'Favo',
    1140: '\xc3\x81gua',
    1150: 'Piso praiano',
    1160: 'Piso praiano',
    1170: 'Piso praiano',
    1180: 'Piso praiano',
    1190: 'Areia',
    10000: 'Cubo de gelo',
    10010: 'Iglu',
    11000: 'Trevo',
    11010: 'Trevo' }
MouldingNames = {
    1000: 'N\xc3\xb3s',
    1010: 'Pintado',
    1020: 'Dental',
    1030: 'Flores',
    1040: 'Flores',
    1050: 'Joaninha',
    1060: 'Cart\xc3\xb5es do Dia dos Namorados ',
    1070: 'Praia',
    1080: 'Luzes de Inverno 1',
    1085: 'Luzes de Inverno 2',
    1090: 'Luzes de Inverno 3',
    1100: 'Cupido do Dia dos Namorados',
    1110: 'Cora\xc3\xa7\xc3\xa3o do Dia dos Namorados 1',
    1120: 'Cora\xc3\xa7\xc3\xa3o do Dia dos Namorados 2' }
WainscotingNames = {
    1000: 'Pintado',
    1010: 'Painel de madeira',
    1020: 'Madeira',
    1030: 'Cart\xc3\xb5es do Dia dos Namorados ',
    1040: 'Subaqu\xc3\xa1tico' }
WindowViewNames = {
    10: 'Jardim amplo',
    20: 'Jardim selvagem',
    30: 'Jardim grego',
    40: 'Paisagem urbana',
    50: 'Velho Oeste',
    60: 'Fundo do mar',
    70: 'Ilha tropical',
    80: 'Noite estrelada',
    90: 'Piscina Tiki',
    100: 'Fronteira congelada',
    110: 'Fazenda',
    120: 'Campo Nativo',
    130: 'Rua Principal' }
SpecialEventNames = {
    1: 'Pr\xc3\xaamio Geral',
    2: 'Torneio de Pesca de Melville',
    3: 'Torneio de Pesca de Billy Bud',
    4: 'Convite de Abril do Bosque de Bolotas',
    5: 'Campeonato no Bosque de Bolotas',
    6: 'Festival de Presentes',
    7: 'Maratona de Ano-Novo dos Toons',
    8: 'Fim de Semana de Jogos no Bonde',
    9: 'Festival de Jogos no Bonde',
    10: 'Fim de Semana Premiado',
    11: 'Corrida de Cavalos dos Toons',
    12: 'Maratona de Salvamento de Edif\xc3\xadcios',
    13: 'Maioria dos Cogs Derrotados',
    14: 'Maioria dos V.P.s Derrotados',
    15: 'Opera\xc3\xa7\xc3\xa3o Evento Rob\xc3\xb4 Vendedor Tempestade' }
NewCatalogNotify = 'H\xc3\xa1 novos itens dispon\xc3\xadveis para serem encomendados por telefone!'
NewDeliveryNotify = 'Chegou correspond\xc3\xaancia nova em sua caixa de correio!'
CatalogNotifyFirstCatalog = 'Seu primeiro cat\xc3\xa1logo chegou! Voc\xc3\xaa pode us\xc3\xa1-lo para encomendar novos itens para uso pessoal ou para casa.'
CatalogNotifyNewCatalog = 'O seu cat\xc3\xa1logo No. %s chegou! Voc\xc3\xaa pode fazer os pedidos dos itens do cat\xc3\xa1logo pelo telefone.'
CatalogNotifyNewCatalogNewDelivery = 'Chegou correspond\xc3\xaancia nova em sua caixa de correio! Al\xc3\xa9m disso, o seu cat\xc3\xa1logo No. %s chegou!'
CatalogNotifyNewDelivery = 'Chegou correspond\xc3\xaancia nova em sua caixa de correio!'
CatalogNotifyNewCatalogOldDelivery = 'O seu cat\xc3\xa1logo No. %s chegou, e ainda h\xc3\xa1 itens aguardando por voc\xc3\xaa em sua caixa de correio!'
CatalogNotifyOldDelivery = 'Ainda h\xc3\xa1 itens aguardando por voc\xc3\xaa em sua caixa de correio!'
CatalogNotifyInstructions = 'Clique no bot\xc3\xa3o "Ir para casa" na P\xc3\xa1gina do mapa em seu \xc3\x81lbum Toon e v\xc3\xa1 at\xc3\xa9 o telefone que h\xc3\xa1 dentro da sua casa.'
CatalogNewDeliveryButton = 'Nova\nentrega!'
CatalogNewCatalogButton = 'Novo\ncat\xc3\xa1logo'
CatalogSaleItem = '\xc3\x80 venda!'
DistributedMailboxEmpty = 'A sua caixa de correio est\xc3\xa1 vazia no momento. Volte aqui para procurar entregas depois que voc\xc3\xaa fizer um pedido pelo telefone!'
DistributedMailboxWaiting = 'A sua caixa de correio est\xc3\xa1 vazia no momento, mas o pacote que voc\xc3\xaa encomendou est\xc3\xa1 a caminho. Verifique mais tarde!'
DistributedMailboxReady = 'Sua encomenda chegou!'
DistributedMailboxNotOwner = 'Sinto muito, esta n\xc3\xa3o \xc3\xa9 a sua caixa de correio.'
DistributedPhoneEmpty = 'Voc\xc3\xaa pode usar qualquer telefone para encomendar itens especiais para uso pessoal ou para sua casa. Em breve, haver\xc3\xa1 novos itens dispon\xc3\xadveis para pedidos.\n\nN\xc3\xa3o h\xc3\xa1 nenhum item dispon\xc3\xadvel para pedidos no momento, mas verifique novamente mais tarde!'
Clarabelle = 'Clarabela'
MailboxExitButton = 'Fechar caixa\nde correio'
MailboxAcceptButton = 'Pegar este item'
MailBoxDiscard = 'Remover este item'
MailboxAcceptInvite = 'Aceitar convite'
MailBoxRejectInvite = 'Recusar convite'
MailBoxDiscardVerify = 'Voc\xc3\xaa quer mesmo Remover %s?'
MailBoxRejectVerify = 'Voc\xc3\xaa quer mesmo Recusar %s?'
MailboxOneItem = 'Sua caixa postal cont\xc3\xa9m 1 item.'
MailboxNumberOfItems = 'Sua caixa postal cont\xc3\xa9m %s itens.'
MailboxGettingItem = 'Pegando %s da caixa postal.'
MailboxGiftTag = 'Presente De: %s'
MailboxGiftTagAnonymous = 'An\xc3\xb4nimo'
MailboxItemNext = 'Pr\xc3\xb3ximo\nitem'
MailboxItemPrev = 'Item\nanterior'
MailboxDiscard = 'Remover'
MailboxReject = 'Recusar'
MailboxLeave = 'Guardar'
CatalogCurrency = 'balas'
CatalogHangUp = 'Desligar'
CatalogNew = 'NOVA'
CatalogBackorder = 'ENCOMENDA'
CatalogLoyalty = 'ESPECIAL'
CatalogEmblem = 'EMBLEMA'
CatalogPagePrefix = 'P\xc3\xa1gina'
CatalogGreeting = 'Ol\xc3\xa1! Agradecemos sua liga\xc3\xa7\xc3\xa3o para o Cat\xc3\xa1logo da Clarabela. Posso ajudar?'
CatalogGoodbyeList = [
    'Agora tchau!',
    'Ligue novamente em breve!',
    'Agradecemos sua liga\xc3\xa7\xc3\xa3o!',
    'Ok, agora tchau!',
    'Tchau!']
CatalogHelpText1 = 'Vire a p\xc3\xa1gina para ver os itens \xc3\xa0 venda.'
CatalogSeriesLabel = 'S\xc3\xa9rie %s'
CatalogGiftFor = 'Comprar Presente para:'
CatalogGiftTo = 'Para: %s'
CatalogGiftToggleOn = 'Parar de\nPresentear'
CatalogGiftToggleOff = 'Comprar\nPresentes'
CatalogGiftToggleWait = 'Tentando!...'
CatalogGiftToggleNoAck = 'N\xc3\xa3o Dispon\xc3\xadvel'
CatalogPurchaseItemAvailable = 'Parab\xc3\xa9ns pela nova compra! Voc\xc3\xaa j\xc3\xa1 pode usar o seu produto imediatamente.'
CatalogPurchaseGiftItemAvailable = '\xc3\x93timo!  %s pode come\xc3\xa7ar a usar o seu presente agora mesmo.'
CatalogPurchaseItemOnOrder = 'Parab\xc3\xa9ns! O produto ser\xc3\xa1 entregue em sua caixa de correio em breve.'
CatalogPurchaseGiftItemOnOrder = '\xc3\x93timo! O seu presente para %s ser\xc3\xa1 entregue na caixa de correio dele.'
CatalogAnythingElse = 'Deseja mais alguma coisa hoje?'
CatalogPurchaseClosetFull = 'O seu arm\xc3\xa1rio est\xc3\xa1 cheio. Apesar disso, voc\xc3\xaa pode comprar este item, mas se comprar, ter\xc3\xa1 que excluir alguma coisa do seu arm\xc3\xa1rio para liberar espa\xc3\xa7o para o novo item, quando ele chegar.\n\nQuer comprar este item mesmo assim?'
CatalogAcceptClosetFull = 'O seu arm\xc3\xa1rio est\xc3\xa1 cheio. Entre em casa e exclua alguma coisa do seu arm\xc3\xa1rio para liberar espa\xc3\xa7o para o item antes de retir\xc3\xa1-lo da caixa de correio.'
CatalogAcceptShirt = 'Voc\xc3\xaa est\xc3\xa1 vestindo agora a sua nova camisa. O que voc\xc3\xaa estava vestindo antes foi transferido para o seu arm\xc3\xa1rio.'
CatalogAcceptShorts = 'Voc\xc3\xaa est\xc3\xa1 vestindo agora o seu novo short. O que voc\xc3\xaa estava vestindo antes foi transferido para o seu arm\xc3\xa1rio.'
CatalogAcceptSkirt = 'Voc\xc3\xaa est\xc3\xa1 vestindo agora a sua nova saia. A que voc\xc3\xaa estava vestindo antes foi transferida para o seu arm\xc3\xa1rio.'
CatalogAcceptPole = 'Agora, voc\xc3\xaa est\xc3\xa1 pronto para pescar uns peixes maiores com sua nova vara!'
CatalogAcceptPoleUnneeded = 'Voc\xc3\xaa j\xc3\xa1 tem uma vara de pescar melhor do que esta!'
CatalogAcceptChat = 'Voc\xc3\xaa ganhou uma nova frase de Chat r\xc3\xa1pido!'
CatalogAcceptEmote = 'Voc\xc3\xaa ganhou uma nova Emo\xc3\xa7\xc3\xa3o!'
CatalogAcceptBeans = 'Voc\xc3\xaa recebeu algumas balinhas!'
CatalogAcceptRATBeans = 'A sua recompensa de recruta Toon chegou!'
CatalogAcceptNametag = 'Seu novo crach\xc3\xa1 chegou!'
CatalogAcceptGarden = 'Os seus materiais de jardim chegaram!'
CatalogAcceptPet = 'Voc\xc3\xaa ganhou um novo Truque de Rabisco!'
CatalogPurchaseHouseFull = 'Sua casa est\xc3\xa1 cheia. Apesar disso, voc\xc3\xaa pode comprar este item, mas se comprar, ter\xc3\xa1 que excluir alguma coisa da sua casa para liberar espa\xc3\xa7o para o novo item, quando ele chegar.\n\nQuer comprar este item mesmo assim?'
CatalogAcceptHouseFull = 'Sua casa est\xc3\xa1 cheia. Entre em casa e exclua alguma coisa de l\xc3\xa1 para liberar espa\xc3\xa7o para o item antes de retir\xc3\xa1-lo da caixa de correio.'
CatalogAcceptInAttic = 'O seu novo item est\xc3\xa1 agora no s\xc3\xb3t\xc3\xa3o. Voc\xc3\xaa pode coloc\xc3\xa1-lo em casa entrando l\xc3\xa1 e clicando no bot\xc3\xa3o "Mover mob\xc3\xadlia".'
CatalogAcceptInAtticP = 'Os seus novos itens est\xc3\xa3o agora no s\xc3\xb3t\xc3\xa3o. Voc\xc3\xaa pode coloc\xc3\xa1-los em casa entrando l\xc3\xa1 e clicando no bot\xc3\xa3o "Mover mob\xc3\xadlia".'
CatalogPurchaseMailboxFull = 'Sua caixa de correio est\xc3\xa1 cheia! Voc\xc3\xaa n\xc3\xa3o poder\xc3\xa1 comprar este item at\xc3\xa9 retirar alguns itens da caixa de correio para liberar espa\xc3\xa7o.'
CatalogPurchaseGiftMailboxFull = 'A caixa de correio de %s est\xc3\xa1 cheia!  Voc\xc3\xaa n\xc3\xa3o pode comprar este item.'
CatalogPurchaseOnOrderListFull = 'Voc\xc3\xaa tem itens demais encomendados no momento. Voc\xc3\xaa n\xc3\xa3o poder\xc3\xa1 encomendar mais nenhum item at\xc3\xa9 que cheguem alguns j\xc3\xa1 encomendados.'
CatalogPurchaseGiftOnOrderListFull = '%s tem \xc3\xadtens demais encomendados.'
CatalogPurchaseGeneralError = 'N\xc3\xa3o foi poss\xc3\xadvel encomendar o item devido a um erro interno no jogo: c\xc3\xb3digo de erro %s.'
CatalogPurchaseGiftGeneralError = 'N\xc3\xa3o foi poss\xc3\xadvel dar o item de presente a %(friend)s por causa de algum erro interno de jogo: c\xc3\xb3digo de erro %(error)s.'
CatalogPurchaseGiftNotAGift = 'Este item n\xc3\xa3o p\xc3\xb4de ser enviado para %s porque seria uma vantagem injusta.'
CatalogPurchaseGiftWillNotFit = 'Este item n\xc3\xa3o p\xc3\xb4de ser enviado para %s porque n\xc3\xa3o vai servir.'
CatalogPurchaseGiftLimitReached = 'Este item n\xc3\xa3o p\xc3\xb4de ser enviado para %s porque ele j\xc3\xa1 o possui.'
CatalogPurchaseGiftNotEnoughMoney = 'Este item n\xc3\xa3o p\xc3\xb4de ser enviado para %s porque ele n\xc3\xa3o pode pagar.'
CatalogAcceptGeneralError = 'Este item n\xc3\xa3o p\xc3\xb4de ser exclu\xc3\xaddo da sua caixa de correio por causa de um erro interno do jogo: c\xc3\xb3digo do erro %s.'
CatalogAcceptRoomError = 'Voc\xc3\xaa n\xc3\xa3o tem espa\xc3\xa7o para isto. Voc\xc3\xaa vai ter que se livrar de alguma coisa.'
CatalogAcceptLimitError = 'Voc\xc3\xaa j\xc3\xa1 tem o n\xc3\xbamero m\xc3\xa1ximo poss\xc3\xadvel disto. Voc\xc3\xaa vai ter que se livrar de alguma coisa.'
CatalogAcceptFitError = 'Isto n\xc3\xa3o serve em voc\xc3\xaa! Voc\xc3\xaa o doa para Toons que precisam.'
CatalogAcceptInvalidError = 'Este item saiu da moda! Voc\xc3\xaa o doa para Toons que precisam.'
MailboxOverflowButtonDicard = 'Remover'
MailboxOverflowButtonLeave = 'Sair'
HDMoveFurnitureButton = 'Mover\nmob\xc3\xadlia'
HDStopMoveFurnitureButton = 'Mudan\xc3\xa7a\nconclu\xc3\xadda'
HDAtticPickerLabel = 'No s\xc3\xb3t\xc3\xa3o'
HDInRoomPickerLabel = 'Na sala'
HDInTrashPickerLabel = 'Na lixeira'
HDDeletePickerLabel = 'Excluir?'
HDInAtticLabel = 'S\xc3\xb3t\xc3\xa3o'
HDInRoomLabel = 'Sala'
HDInTrashLabel = 'Lixo'
HDToAtticLabel = 'Enviar\npara o s\xc3\xb3t\xc3\xa3o'
HDMoveLabel = 'Mover'
HDRotateCWLabel = 'Girar para a direita'
HDRotateCCWLabel = 'Girar para a esquerda'
HDReturnVerify = 'Retornar este item para o s\xc3\xb3t\xc3\xa3o?'
HDReturnFromTrashVerify = 'Retornar este item para o s\xc3\xb3t\xc3\xa3o, da lixeira?'
HDDeleteItem = 'Clique em OK para enviar este item para a lixeira ou em Cancelar para mant\xc3\xaa-lo.'
HDNonDeletableItem = 'Voc\xc3\xaa n\xc3\xa3o pode excluir itens deste tipo!'
HDNonDeletableBank = 'Voc\xc3\xaa n\xc3\xa3o pode excluir o seu banco!'
HDNonDeletableCloset = 'Voc\xc3\xaa n\xc3\xa3o pode excluir o seu arm\xc3\xa1rio!'
HDNonDeletablePhone = 'Voc\xc3\xaa n\xc3\xa3o pode excluir o seu telefone!'
HDNonDeletableNotOwner = "Voc\xc3\xaa n\xc3\xa3o pode excluir as coisas de %s's!"
HDHouseFull = 'Sua casa est\xc3\xa1 cheia. Voc\xc3\xaa precisa excluir algo mais de sua casa ou do s\xc3\xb3t\xc3\xa3o antes de recuperar este item da lixeira.'
HDHelpDict = {
    'DoneMoving': 'Decora\xc3\xa7\xc3\xa3o da sala conclu\xc3\xadda.',
    'Attic': 'Mostrar lista de itens do s\xc3\xb3t\xc3\xa3o. O s\xc3\xb3t\xc3\xa3o armazena itens que n\xc3\xa3o est\xc3\xa3o na sala.',
    'Room': 'Mostrar lista de itens da sala. \xc3\x9atil para encontrar itens perdidos.',
    'Trash': 'Mostrar itens da lixeira. Os itens mais antigos s\xc3\xa3o exclu\xc3\xaddos ap\xc3\xb3s um tempo ou quando a lixeira fica cheia demais.',
    'ZoomIn': 'Tenha uma vis\xc3\xa3o ampliada da sala.',
    'ZoomOut': 'Tenha uma vis\xc3\xa3o reduzida da sala.',
    'SendToAttic': 'Envie o item de mob\xc3\xadlia atual para o s\xc3\xb3t\xc3\xa3o, para armazen\xc3\xa1-lo.',
    'RotateLeft': 'Vire para a esquerda.',
    'RotateRight': 'Vire para a direita.',
    'DeleteEnter': 'Alterne para o modo de exclus\xc3\xa3o.',
    'DeleteExit': 'Saia do modo de exclus\xc3\xa3o.',
    'FurnitureItemPanelDelete': 'Envie o item %s para a lixeira.',
    'FurnitureItemPanelAttic': 'Coloque o item %s na sala.',
    'FurnitureItemPanelRoom': 'Voltar o item %s para o s\xc3\xb3t\xc3\xa3o.',
    'FurnitureItemPanelTrash': 'Voltar o item %s para o s\xc3\xb3t\xc3\xa3o.' }
MessagePickerTitle = 'Voc\xc3\xaa tem frases demais. Para comprar o item\n"%s"\n voc\xc3\xaa precisa escolher um deles para ser removido:'
MessagePickerCancel = lCancel
MessageConfirmDelete = 'Tem certeza de que quer remover "%s" do menu de Chat r\xc3\xa1pido?'
CatalogBuyText = 'Comprar'
CatalogRentText = 'Alugar'
CatalogGiftText = 'Presente'
CatalogOnOrderText = 'Encomendado'
CatalogPurchasedText = 'J\xc3\xa1\ncomprado'
CatalogCurrent = 'Atual'
CatalogGiftedText = 'Presenteado\nPara Voc\xc3\xaa'
CatalogPurchasedGiftText = 'J\xc3\xa1\nRecebido'
CatalogMailboxFull = 'Sem Espa\xc3\xa7o'
CatalogNotAGift = 'N\xc3\xa3o \xc3\xa9 um Presente'
CatalogNoFit = 'N\xc3\xa3o\nServe'
CatalogMembersOnly = 'Somente para\nUsu\xc3\xa1rios!'
CatalogSndOnText = 'Som Ligado'
CatalogSndOffText = 'Som Desligado'
CatalogPurchasedMaxText = 'J\xc3\xa1\ncomprado o m\xc3\xa1x.'
CatalogVerifyPurchase = 'Comprar o item %(item)s por %(price)s balinhas?'
CatalogVerifyPurchaseBeanSilverGold = 'Comprar %(item)s por %(price)s balinhas, %(silver)s s\xc3\xadmbolos de prata e %(gold)s s\xc3\xadmbolos de ouro?'
CatalogVerifyPurchaseBeanGold = 'Comprar %(item)s por %(price)s balinhas e %(gold)s s\xc3\xadmbolos de ouro?'
CatalogVerifyPurchaseBeanSilver = 'Comprar %(item)s por %(price)s balinhas e %(silver)s s\xc3\xadmbolos de prata?'
CatalogVerifyPurchaseSilverGold = 'Comprar %(item)s por %(silver)s s\xc3\xadmbolos de prata e %(gold)s s\xc3\xadmbolos de ouro?'
CatalogVerifyPurchaseSilver = 'Comprar %(item)s por %(silver)s s\xc3\xadmbolos de prata?'
CatalogVerifyPurchaseGold = 'Comprar %(item)s por %(gold)s s\xc3\xadmbolos de ouro?'
CatalogVerifyRent = 'Alugar %(item)s por %(price)s balinhas?'
CatalogVerifyGift = 'Comprar %(item)s por %(price)s balinhas de presente para %(friend)s?'
CatalogOnlyOnePurchase = 'Voc\xc3\xaa s\xc3\xb3 pode ter um destes itens de cada vez. Se comprar este aqui, ele substituir\xc3\xa1 os itens %(old)s.\n\nTem certeza de que quer comprar o item %(item)s por %(price)s balinhas?'
CatalogExitButtonText = 'Desligar'
CatalogCurrentButtonText = 'Para itens atuais'
CatalogPastButtonText = 'Para itens antigos'
TutorialHQOfficerName = 'Haroldo do Quartel'
NPCToonNames = {
    20000: 'Tom Tutorial',
    999: 'Costureiro Toon',
    1000: lToonHQ,
    20001: Flippy,
    2001: Flippy,
    2002: 'Banqueiro Beto',
    2003: 'Professor Paulo',
    2004: 'Cora, a Costureira',
    2005: 'Bibliotec\xc3\xa1rio Bino',
    2006: 'Vendedor Alaor',
    2011: 'Vendedora Isadora',
    2007: lHQOfficerM,
    2008: lHQOfficerM,
    2009: lHQOfficerF,
    2010: lHQOfficerF,
    2012: 'Vendedor da Loja de Animais',
    2018: 'Est\xc3\xbapi...doo... Homem-DICA',
    2013: 'Vendedor Pop',
    2014: 'Vendedora El\xc3\xa9trica',
    2015: 'Vendedor Molenga',
    2016: 'Planejador de Festa Ab\xc3\xb3bora',
    2017: 'Planejadora de Festa Polly',
    2018: 'Doutor Surlee',
    2019: 'Doutor Dimm',
    2020: 'Professor Prepostera',
    2101: 'Dentista Daniel',
    2102: 'Delegada D\xc3\xa9lis',
    2103: 'Gatinho Funga-funga',
    2104: lHQOfficerM,
    2105: lHQOfficerM,
    2106: lHQOfficerF,
    2107: lHQOfficerF,
    2108: 'Can\xc3\xa1ria Mina de carv\xc3\xa3o',
    2109: 'Gugu Bolha',
    2110: "Otto D'or",
    2111: 'Diego Dan\xc3\xa7ante',
    2112: 'Dr. Tom',
    2113: 'Rolo, o Incr\xc3\xadvel',
    2114: 'Rosabela',
    2115: 'Pati Papel',
    2116: 'Brutus Crespo',
    2117: 'Dona Putrefata',
    2118: 'Bob Bobo',
    2119: 'Renata R\xc3\xa1 R\xc3\xa1',
    2120: 'Professor Pimp\xc3\xa3o',
    2121: 'Madame Risadinha',
    2122: 'Toni Macacada',
    2123: 'Lat\xc3\xb4nia Lata',
    2124: 'Massinha Mode Lar',
    2125: 'Ralf Desocupado',
    2126: 'Professora Gargalhada',
    2127: 'Nico N\xc3\xadquel',
    2128: 'Duda Doidinho',
    2129: 'Franco Furtado',
    2130: 'Fel\xc3\xadcia Ding-dong',
    2131: 'Espanadora Penas',
    2132: 'Joe Tromundo',
    2133: 'Dr. F\xc3\xb3rico',
    2134: 'Simone Sil\xc3\xaancio',
    2135: 'Karla Rossel',
    2136: 'Saulo Risadinha',
    2137: 'Alegria Alegre',
    2138: 'Jo\xc3\xa3o',
    2139: 'Beb\xc3\xaa Bab\xc3\xa1',
    2140: 'Gui Pescador',
    2201: 'Gerente Gil',
    2202: 'Shirley Vocezomba',
    2203: lHQOfficerM,
    2204: lHQOfficerM,
    2205: lHQOfficerF,
    2206: lHQOfficerF,
    2207: 'Saulo Sabich\xc3\xa3o',
    2208: 'Lucas Grude',
    2209: 'Rico Risada',
    2210: 'Chazinha',
    2211: 'Cl\xc3\xa1udia Cuspinho',
    2212: 'Est\xc3\xaav\xc3\xa3o Estranho',
    2213: 'Luciana da Roda',
    2214: 'Mano da Mancha',
    2215: 'Bob Buj\xc3\xa3o',
    2216: 'K\xc3\xaania Teviu',
    2217: 'Jo\xc3\xa3o Tubar\xc3\xa3o',
    2218: 'Hil\xc3\xa1ria Folha',
    2219: 'Chef Cabe\xc3\xa7a de Vento',
    2220: 'Carlos Cabe\xc3\xa7a de Ferro',
    2221: 'Flora Canudinho',
    2222: 'Fus\xc3\xadvel Mirim',
    2223: 'Gl\xc3\xa1ucia Gargalhada',
    2224: 'F\xc3\xa1bio Fumacinha',
    2225: 'Corcunda Pescador',
    2301: 'Dr. Puxaperna',
    2302: 'Professor Balan\xc3\xa7o',
    2303: 'Enfermeira Enferma',
    2304: lHQOfficerM,
    2305: lHQOfficerM,
    2306: lHQOfficerF,
    2307: lHQOfficerF,
    2308: 'Nancy Veneno',
    2309: 'Jo\xc3\xa3o Grand\xc3\xa3o',
    2311: 'Francisco da Gra\xc3\xa7a',
    2312: 'Dra. Sens\xc3\xadvel',
    2313: 'Lucinda Pinta',
    2314: 'L\xc3\xbacio Lan\xc3\xa7ador',
    2315: 'Tat\xc3\xa1 Tasco',
    2316: 'B\xc3\xa1rbara Bola',
    2318: 'Ronaldo Engra\xc3\xa7aldo',
    2319: 'Tiraldo',
    2320: 'Alfredo Nham',
    2321: 'Bart\xc3\xb4 Pescador',
    1001: 'Vendedor Willy',
    1002: 'Vendedor Billy',
    1003: lHQOfficerM,
    1004: lHQOfficerF,
    1005: lHQOfficerM,
    1006: lHQOfficerF,
    1007: 'Bet\xc3\xa3o Cal\xc3\xa7alongas',
    1008: 'Vendedor da Loja de Animais',
    1009: 'Vendedor Dur\xc3\xa3o',
    1010: 'Vendedora Ron-ron',
    1011: 'Vendedora Blup',
    1012: 'Planejador de Festa Pickles',
    1013: 'Planejador de Festa Patty',
    1101: 'Levi Legal',
    1102: 'Capit\xc3\xa3o Carl\xc3\xa3o',
    1103: 'Pedro Peixe',
    1104: 'Doutor Al\xc3\xa1',
    1105: 'Almirante Gancho',
    1106: 'Dona Goma',
    1107: 'Carlo Caiado',
    1108: lHQOfficerM,
    1109: lHQOfficerF,
    1110: lHQOfficerM,
    1111: lHQOfficerF,
    1112: 'Gl\xc3\xa1ucio Glubglub',
    1113: 'Adele Adernada',
    1114: 'Carlos Camarada',
    1115: 'L\xc3\xbacia Lula',
    1116: 'Carla Craca',
    1117: 'Capit\xc3\xa3o Blargh',
    1118: 'Marinho Crespo',
    1121: 'Linda Terra Firme',
    1122: 'Salgado Pescado',
    1123: 'Enguia El\xc3\xa9trica',
    1124: 'Jo\xc3\xa3o Farpa do Cais',
    1125: 'Arlene Al\xc3\xa9m-mar',
    1126: 'Z\xc3\xa9 Silva Pescador',
    1201: 'Craca B\xc3\xa1rbara',
    1202: 'M\xc3\xa1rio',
    1203: 'Salgado',
    1204: 'Marco Quebra-mar',
    1205: lHQOfficerM,
    1206: lHQOfficerF,
    1207: lHQOfficerM,
    1208: lHQOfficerF,
    1209: 'Professora Pranchinha',
    1210: 'Aiki Sopa',
    1211: 'Malo Mala',
    1212: 'Tom\xc3\xa1s L\xc3\xadngua de Trapo',
    1213: 'Bob Botinho',
    1214: 'K\xc3\xa1tia Furac\xc3\xa3o',
    1215: 'Paula Profundeza',
    1216: 'Otto Ostra',
    1217: 'Ci\xc3\xa7a Cani\xc3\xa7o',
    1218: 'Toni Pac\xc3\xadfico',
    1219: 'Carlos Encalhado',
    1220: 'Carla Canal',
    1221: 'Alan Abrolhos',
    1222: 'Bob Abordo',
    1223: 'Lula Lulu',
    1224: 'Em\xc3\xadlia Enguia',
    1225: 'Est\xc3\xaav\xc3\xa3o Estivador',
    1226: 'Pedro P\xc3\xa9 na T\xc3\xa1bua',
    1227: 'Coral do Recife',
    1228: 'Junqueira Pescador',
    1301: 'Alice',
    1302: 'Moby',
    1303: 'M\xc3\xa1rio',
    1304: 'Martina',
    1305: lHQOfficerM,
    1306: lHQOfficerF,
    1307: lHQOfficerM,
    1308: lHQOfficerF,
    1309: 'Esponja do Mar',
    1310: 'Fernando Ferramenta',
    1311: 'Paulinha Ponta Cabe\xc3\xa7a',
    1312: 'H\xc3\xa9lio H\xc3\xa9lice',
    1313: 'Wilson N\xc3\xb3',
    1314: 'Fernando Enferrujado',
    1315: 'Doutora Correnteza',
    1316: 'Beth Rodopio',
    1317: 'Paula Poste',
    1318: 'Te\xc3\xb3filo Bote',
    1319: 'Est\xc3\xa1cio Estaleiro',
    1320: 'Caio Calmaria',
    1321: 'Camila Cais',
    1322: 'Rachel Recheio',
    1323: 'Fred Fedido',
    1324: 'P\xc3\xa9rola Profunda',
    1325: 'S\xc3\xa9rgio Vira-latas',
    1326: 'Fel\xc3\xadcia Batatinha',
    1327: 'C\xc3\xadntia T\xc3\xa1bua',
    1328: 'Lucas Linguado',
    1329: 'Conchita Alga Marina',
    1330: 'Porta Dor',
    1331: 'Rudy Rid\xc3\xadquilhas',
    1332: 'Polar Pescador',
    3001: 'Frida Freezer',
    3002: lHQOfficerM,
    3003: lHQOfficerF,
    3004: lHQOfficerM,
    3005: lHQOfficerM,
    3006: 'Vendedor Breno',
    3007: 'Vendedora Brenda',
    3008: 'Paco Pacote',
    3009: 'Vendedor da Loja de Animais',
    3010: 'Vendedor Saltitante',
    3011: 'Vendedora Glub',
    3012: 'Vendedor Kiko',
    3013: 'Planejador de Festa Pedro',
    3014: 'Planejador de Festa Penny',
    3101: 'Seu Le\xc3\xa3o',
    3102: 'Tia Freezer',
    3103: 'Chic\xc3\xb3',
    3104: 'Gorrete',
    3105: 'Fred Cavanhaque',
    3106: 'Pio Arrepio',
    3107: 'Patty Passaporte',
    3108: 'Tobi Tobog\xc3\xa3',
    3109: 'Kate',
    3110: 'Franguinho',
    3111: 'C\xc3\xa3o de Bico',
    3112: 'Pequeno Grande Anci\xc3\xa3o',
    3113: 'Am\xc3\xa9rico Hist\xc3\xa9rico',
    3114: 'Rico Arriscado',
    3115: lHQOfficerM,
    3116: lHQOfficerF,
    3117: lHQOfficerM,
    3118: lHQOfficerM,
    3119: 'Carlos K. B. Loemp\xc3\xa9',
    3120: 'Kiko Quiproc\xc3\xb3',
    3121: 'Jo\xc3\xa3o Eletrochoque',
    3122: 'Luci Lugar',
    3123: 'Francis Quebra Gelo',
    3124: 'Estileto Iceberg',
    3125: 'Coronel Mastiga',
    3126: 'Jo\xc3\xa3o Jornada',
    3127: 'A\xc3\xa9rea Inflada',
    3128: 'Jorge Palitinho',
    3129: 'F\xc3\xa1tima F\xc3\xb4rma',
    3130: 'Sandy',
    3131: 'Patr\xc3\xadcio Pregui\xc3\xa7a',
    3132: 'Maria Cinza',
    3133: 'Dr. Congelado',
    3134: 'V\xc3\xadtor Vest\xc3\xadbulo',
    3135: '\xc3\x8ania Sopada',
    3136: 'Susana Nimada',
    3137: 'Sr. Freezer',
    3138: 'Chefe Sopa Rala',
    3139: 'Vov\xc3\xb3 Ceroulas',
    3140: 'Luci Pescadora',
    3201: 'Tia \xc3\x81rtica',
    3202: 'Tremend\xc3\xa3o',
    3203: 'Walter',
    3204: 'Dra. Vai C. V.',
    3205: 'Cabe\xc3\xa7\xc3\xa3o Kika',
    3206: 'Vid\xc3\xa1lia VaVum',
    3207: 'Dr. Ban Guela',
    3208: 'Felipe Nervosinho',
    3209: 'Marcos Cem Gra\xc3\xa7a',
    3210: '\xc3\x81lvaro Asno',
    3211: 'Hil\xc3\xa1ria Freezer',
    3212: 'Rog\xc3\xa9rio G\xc3\xa9lido',
    3213: lHQOfficerM,
    3214: lHQOfficerF,
    3215: lHQOfficerM,
    3216: lHQOfficerM,
    3217: 'Consuelo Suada',
    3218: 'Lu Lazul',
    3219: 'Bob BikeDupla',
    3220: 'Sr. Espirro',
    3221: 'Neli Neve',
    3222: 'Vera Vento Cortante',
    3223: 'Chapa',
    3224: 'Rita Raspadinha',
    3225: 'Foca Fofoca',
    3226: 'Papai N\xc3\xb3 El',
    3227: 'Raiomundo de Sol',
    3228: 'Frida Calafrio',
    3229: 'Herm\xc3\xadnia Cinta',
    3230: 'Pedro Pedreira',
    3231: 'G. Lopicado',
    3232: 'Pescador Alberto',
    3301: 'Remendo Tecidos',
    3302: 'Pedro Urso',
    3303: 'Dr. Olhadelas',
    3304: 'Abr\xc3\xa3o o Abomin\xc3\xa1vel',
    3305: 'Mick Eimei',
    3306: 'Paula \xc3\x9arsula',
    3307: 'Pescadora Frederica',
    3308: 'Roberto Injustus',
    3309: 'Botinha',
    3310: 'Professor Floco',
    3311: 'Connie Feras',
    3312: 'Haroldo Marcha',
    3313: lHQOfficerM,
    3314: lHQOfficerF,
    3315: lHQOfficerM,
    3316: lHQOfficerF,
    3317: 'Bete Beijoqueira',
    3318: 'Jo\xc3\xa3o Caxemira',
    3319: 'Reinaldo Retifica',
    3320: 'Ester Espuma',
    3321: 'Paulo Picareta',
    3322: 'Luis Fluis',
    3323: 'Aurora Borealis',
    3324: 'Otto Dentetorto',
    3325: 'Dercy Balan\xc3\xa7alves',
    3326: 'Blanche',
    3327: 'Cac\xc3\xa1 Sado',
    3328: 'S\xc3\xb4nia Sombria',
    3329: 'Edu Pisada',
    4001: 'Mel Odia',
    4002: lHQOfficerM,
    4003: lHQOfficerF,
    4004: lHQOfficerF,
    4005: lHQOfficerF,
    4006: 'Vendedora Do-r\xc3\xa9-mi',
    4007: 'Vendedor F\xc3\xa1-sol-l\xc3\xa1-si',
    4008: 'Costureira Harmonia',
    4009: 'Vendedor da Loja de Animais',
    4010: 'Vendedor Caco',
    4011: 'Vendedor Nilton',
    4012: 'Vendedora Flor do Nordeste',
    4013: 'Planejador de Festa Preston',
    4014: 'Planejadora de Festa Pen\xc3\xa9lope',
    4101: 'Tom',
    4102: 'Fifi',
    4103: 'Dr. Triturador',
    4104: lHQOfficerM,
    4105: lHQOfficerF,
    4106: lHQOfficerF,
    4107: lHQOfficerF,
    4108: 'Clave',
    4109: 'Carlos',
    4110: 'M\xc3\xa9trica An\xc3\xa3',
    4111: 'Tom Tum',
    4112: 'F\xc3\xa1',
    4113: 'Madame Boa Maneira',
    4114: 'Bino Desafino',
    4115: 'B\xc3\xa1rbara de Sevilha',
    4116: 'Fl\xc3\xa1vio Flautim',
    4117: 'Banda Lyn',
    4118: 'Faxineiro Abel',
    4119: 'Moz Arte',
    4120: 'Violante Almofada',
    4121: 'Geg\xc3\xaa Menor',
    4122: 'Mentolada do Baixo',
    4123: 'Andr\xc3\xa9 Raio',
    4124: 'Renato Refr\xc3\xa3o',
    4125: 'Ondina Musical',
    4126: 'Mel\xc3\xb4 Canto',
    4127: 'Fel\xc3\xadcia Podos',
    4128: 'Luciano Furo',
    4129: 'Carla Cad\xc3\xaancia',
    4130: 'Miguel Metal',
    4131: 'Abra\xc3\xa3o Arm\xc3\xa1rio',
    4132: 'Marta Marrom',
    4133: 'Paulo Popeline',
    4134: 'Davi Disco',
    4135: 'Carlo Canoro',
    4136: 'Patr\xc3\xadcia Pausa',
    4137: 'Toni Surdo',
    4138: 'Agudo Clave',
    4139: 'Harmonia Decrescente',
    4140: 'Daniel Desajeitado',
    4141: 'Pet Pescador',
    4201: 'Tina',
    4202: 'Barry',
    4203: 'Al\xc3\xaa Nhador',
    4204: lHQOfficerM,
    4205: lHQOfficerF,
    4206: lHQOfficerF,
    4207: lHQOfficerF,
    4208: 'Heidi',
    4209: 'Brega Galopante',
    4211: 'Carlo Concerto',
    4212: 'Detetive Marcha F\xc3\xbanebre',
    4213: 'Franca Foley',
    4214: 'Paula Meia-ponta',
    4215: 'M\xc3\xa1rio Marcha a r\xc3\xa9',
    4216: 'Bob Buzina',
    4217: 'Toni Bonit\xc3\xa3o',
    4218: 'S\xc3\xb4nia Soprano',
    4219: 'Bruno Bar\xc3\xadtono',
    4220: 'D\xc3\xaanis Dedus',
    4221: 'Marcos Madrigal',
    4222: 'Jo\xc3\xa3o da Silva',
    4223: 'P\xc3\xa2mela Ponto',
    4224: 'Jim das Selvas',
    4225: 'V\xc3\xa2nia Vaia',
    4226: 'Samantha Garganta',
    4227: 'Cl\xc3\xa1udia Calada',
    4228: 'Augusto de Sopro',
    4229: 'J\xc3\xbania Bombom',
    4230: 'Marcelo Martelo',
    4231: 'Stefanie Acordes',
    4232: 'Helder Hino',
    4233: 'Enzo Enjoado',
    4234: 'Mestre Guitarra',
    4235: 'Lauro Pescador',
    4301: 'Cavaca',
    4302: 'Ana',
    4303: 'L\xc3\xa9o',
    4304: lHQOfficerM,
    4305: lHQOfficerF,
    4306: lHQOfficerF,
    4307: lHQOfficerF,
    4308: 'T\xc3\xa1bata',
    4309: 'Punk Ecas',
    4310: 'Mezza Soprana',
    4311: 'Chica Shake',
    4312: 'Paulo Palheta',
    4313: 'M\xc3\xa1rio Mudo',
    4314: 'Danuza Uza',
    4315: 'Maritza Tique Ataque',
    4316: 'Toni Tango',
    4317: 'Dedo Curto',
    4318: 'Bob Marlin',
    4319: 'C\xc3\xa1tia Zuza',
    4320: 'Roberta P. Rock',
    4321: 'Edinho Verde',
    4322: 'Antoniota Musical',
    4323: 'B\xc3\xa1rbara Balado',
    4324: 'Elen',
    4325: 'Ralf R\xc3\xa1dio',
    4326: 'K\xc3\xadria Irrita',
    4327: 'Arm\xc3\xadnia Arranca Pele',
    4328: 'Wagner',
    4329: 'Teles Prompter',
    4330: 'Quarentino',
    4331: 'Mello Costello',
    4332: 'Ziggy',
    4333: 'Ubaldo',
    4334: 'Est\xc3\xaav\xc3\xa3o Expresso',
    4335: 'S\xc3\xadlvia Pescadora',
    5001: lHQOfficerM,
    5002: lHQOfficerM,
    5003: lHQOfficerF,
    5004: lHQOfficerF,
    5005: 'Vendedora Moranguinho',
    5006: 'Vendedor Herbal',
    5007: 'Florinda Flores',
    5008: 'Vendedor da Loja de Animais',
    5009: 'Vendedora Buba T\xc3\xa2nica',
    5010: 'Vendedor Tony Grana',
    5011: 'Vendedor Duda Madeira',
    5012: 'Planejador de Festa Pierce',
    5013: 'Planejadora de Festa Peggy',
    5101: 'S\xc3\xa9rgio',
    5102: 'Susana',
    5103: 'Flor\xc3\xaancio',
    5104: 'Borba Oleta',
    5105: 'Jo\xc3\xa3o',
    5106: 'Barbeiro Tosque Ador',
    5107: 'Carteiro Felipe',
    5108: 'Funcion\xc3\xa1ria Janete',
    5109: lHQOfficerM,
    5110: lHQOfficerM,
    5111: lHQOfficerF,
    5112: lHQOfficerF,
    5113: 'Dra. \xc3\x81lia e \xc3\x93lea',
    5114: 'Al F\xc3\xa1cio Murcho',
    5115: 'Lua de Mel\xc3\xa3o',
    5116: 'V\xc3\xadtor Vegetal',
    5117: 'P\xc3\xa9tala',
    5118: 'Pipo K.',
    5119: 'Jo\xc3\xa3o Medalh\xc3\xa3o',
    5120: 'Toupeira',
    5121: 'Em\xc3\xadlia Ervilha',
    5122: 'J. Jardim',
    5123: 'Diana Uva',
    5124: 'Olavo Orvalho',
    5125: 'Chu Chu\xc3\xa1',
    5126: 'Madame Calado',
    5127: 'Poliana P\xc3\xb3len',
    5128: 'Suzana Seiva',
    5129: 'Salgueira Pescadora',
    5201: 'Jo\xc3\xa3ozinho',
    5202: 'C\xc3\xadntia',
    5203: 'Lisa',
    5204: 'Ubaldo',
    5205: 'Maur\xc3\xadcio Le\xc3\xa3o',
    5206: 'Branco Vinho',
    5207: 'Sofia Seiva',
    5208: 'Samanta P\xc3\xa1',
    5209: lHQOfficerM,
    5210: lHQOfficerM,
    5211: lHQOfficerF,
    5212: lHQOfficerF,
    5213: 'Nabo Bobo',
    5214: 'Empolada Al\xc3\xa9rgica',
    5215: 'Clara Caules',
    5216: 'Fernando Fedido',
    5217: 'V\xc3\xadtor do Dedo Verde',
    5218: 'Francisco Framboesa',
    5219: 'Bi Ceps',
    5220: 'Luci Cal\xc3\xa7ola',
    5221: 'Rosinha Flamingo',
    5222: 'Sandra Samambaia',
    5223: 'Paulo Ensopado',
    5224: 'Tio Campon\xc3\xaas',
    5225: 'P\xc3\xa2mela P\xc3\xa2ntana',
    5226: 'Mauro Musgo',
    5227: 'Beg\xc3\xb4nia Malte',
    5228: 'Drago Di Lama',
    5229: 'Lili Pescadora',
    5301: lHQOfficerM,
    5302: lHQOfficerM,
    5303: lHQOfficerM,
    5304: lHQOfficerM,
    5305: 'Cristal',
    5306: 'C. Postal',
    5307: 'Mo Fus',
    5308: 'Nely Nervo',
    5309: 'R\xc3\xb4 Mann',
    5310: 'Tim\xc3\xb3teo',
    5311: 'Ju\xc3\xadza Gala',
    5312: 'Eug\xc3\xaanio',
    5313: 'Treinador Abobrinha',
    5314: 'Tia Miga',
    5315: 'Tio Lama',
    5316: 'Tio Batatinha',
    5317: 'Detetive Linda',
    5318: 'C\xc3\xa9sar',
    5319: 'Rose',
    5320: 'M\xc3\xa1rcia',
    5321: 'Professora Uva',
    5322: 'Rose Pescadora',
    8001: 'Grandep R\xc3\xaamio',
    8002: 'Keruk Orr\xc3\xaa',
    8003: 'Precisuv Encer',
    8004: 'En Chaela',
    9001: 'Susana Pestana',
    9002: 'Dor Minhoco',
    9003: 'Sono Lento',
    9004: lHQOfficerF,
    9005: lHQOfficerF,
    9006: lHQOfficerM,
    9007: lHQOfficerM,
    9008: 'Vendedora Resona',
    9009: 'Vendedor Kisono',
    9010: 'Ultraje Velho',
    9011: 'Vendedor da Loja de Animais',
    9012: 'Vendedora Sara Soneca',
    9013: 'Vendedora Gata na Lata',
    9014: 'Vendedor Cara Mujo',
    9015: 'Planejador de Festa Pedregulho',
    9016: 'Planejadora de Festa P\xc3\xa9rola',
    9101: 'Marcelo',
    9102: 'Mama',
    9103: 'Py Jama',
    9104: 'Dulce Lombra',
    9105: 'Professor Bocejo',
    9106: 'M\xc3\xa1ximo',
    9107: 'Aurora Ninho',
    9108: 'Pedro Pestana',
    9109: 'Dafne Sonolinda',
    9110: 'Gat\xc3\xa1ria Soneca',
    9111: 'Elle \xc3\x89trica',
    9112: 'Denis Nar',
    9113: 'Tique Eust\xc3\xa1quio',
    9114: 'M\xc3\xa1ki Agem',
    9115: 'Nen\xc3\xaa Crespo',
    9116: 'Dan\xc3\xa7a com Carneirinhos',
    9117: 'Aurora Extra',
    9118: 'Celeste Estrelada',
    9119: 'Pedro',
    9120: 'L\xc3\xbacia Lenta',
    9121: 'Serena Len\xc3\xa7ol Curto',
    9122: 'Paulo Pregado',
    9123: 'Ursolino de P. L\xc3\xbacia',
    9124: 'Nana de Nina',
    9125: 'Dr. Turvo',
    9126: 'Jatha Cordada',
    9127: 'Tati U. Nidos',
    9128: 'Pedro Fuso',
    9129: 'C\xc3\xa1tia Colcha',
    9130: 'Nico Penico',
    9131: 'C\xc3\xa9lia Sesta',
    9132: lHQOfficerF,
    9133: lHQOfficerF,
    9134: lHQOfficerF,
    9135: lHQOfficerF,
    9136: 'Tainha Pescador',
    9201: 'Bernardo',
    9202: 'Carneiro',
    9203: 'Zez\xc3\xa9',
    9204: 'Clara da Lua',
    9205: 'Bob Boc\xc3\xa3o',
    9206: 'Petra P\xc3\xa9tala',
    9207: 'Denise Dreno',
    9208: 'Solano Sonolento',
    9209: 'Dr. Sedoso',
    9210: 'Mestre M\xc3\xa1rio',
    9211: 'Aurora',
    9212: 'Raio de Lua',
    9213: 'Gustavo Galo',
    9214: 'Dr. Soneca',
    9215: 'Ded\xc3\xa9 Descanso',
    9216: 'Cuca',
    9217: 'Linda Legal',
    9218: 'Matilda Madruga',
    9219: 'Condessa',
    9220: 'Ney Nervoso',
    9221: 'Z\xc3\xa9firo',
    9222: 'Vaqueiro George',
    9223: 'Vado Levado',
    9224: 'Cuca P. Gol',
    9225: 'Henriqueta Inquieta',
    9226: 'Guilherme Sonoleve',
    9227: 'Carlos Cabeceira',
    9228: 'Samuel Suspiro',
    9229: 'Rosa Sonada',
    9230: 'Lel\xc3\xaa',
    9231: 'R\xc3\xa9gis Rede',
    9232: 'Lua de Mel',
    9233: lHQOfficerM,
    9234: lHQOfficerM,
    9235: lHQOfficerM,
    9236: lHQOfficerM,
    9237: 'Jung Pescador' }
zone2TitleDict = {
    2513: ('PrefeiToona', ''),
    2514: ('Banco de Toontown', ''),
    2516: ('Escola de Toontown', ''),
    2518: ('Biblioteca de Toontown', ''),
    2519: ('Loja de Piadas', ''),
    2520: (lToonHQ, ''),
    2521: ('Loja de Roupas', ''),
    2522: ('Loja de Animais', ''),
    2601: ('Restaura\xc3\xa7\xc3\xb5es Dent\xc3\xa1rias Todo Sorrisos', ''),
    2602: ('', ''),
    2603: ('Mineradores Espirituosos', ''),
    2604: ('Lavanderia Lavou est\xc3\xa1 Novo', ''),
    2605: ('F\xc3\xa1brica de Sinaliza\xc3\xa7\xc3\xa3o de Toontown', ''),
    2606: ('', ''),
    2607: ('Feij\xc3\xb5es Saltadores', ''),
    2610: ('Dr. Tom Besteira', ''),
    2611: ('', ''),
    2616: ('Loja de Disfarces Bigode Bizarro', ''),
    2617: ('Feitos Idiotas', ''),
    2618: ('A Encarna\xc3\xa7\xc3\xa3o Deve Continuar', ''),
    2621: ('Avi\xc3\xb5es de Papel', ''),
    2624: ('Brutamontes Felizes', ''),
    2625: ('Casa da Torta Azeda', ''),
    2626: ('Restaura\xc3\xa7\xc3\xa3o de Piadas do Bob', ''),
    2629: ('A Casa da Risada', ''),
    2632: ('Curso de Palha\xc3\xa7os', ''),
    2633: ('Casa de Ch\xc3\xa1 Chapinha', ''),
    2638: ('Casa de Brinquedos de Toontown', ''),
    2639: ('Truques e Macaquices', ''),
    2643: ('Conservas Conservadas', ''),
    2644: ('Pregadinhas de Pe\xc3\xa7a', ''),
    2649: ('Loja de Divers\xc3\xb5es e Jogos', ''),
    2652: ('', ''),
    2653: ('', ''),
    2654: ('Curso de Risada', ''),
    2655: ('Financeira Dinheiro Feliz', ''),
    2656: ('Carros de Palha\xc3\xa7o Usados', ''),
    2657: ('Pegadinhas do Franco', ''),
    2659: ('Campainhas Ding-dong para o Mundo', ''),
    2660: ('M\xc3\xa1quinas de Cosquinhas', ''),
    2661: ('Doces Joe', ''),
    2662: ('Dr. E. U. F\xc3\xb3rico', ''),
    2663: ('Cinerama de Toontown', ''),
    2664: ('M\xc3\xadmicas Divertidas', ''),
    2665: ('Ag\xc3\xaancia de Viagens K. Rossel', ''),
    2666: ('Posto de G\xc3\xa1s Hilariante', ''),
    2667: ('A Folha da Alegria', ''),
    2669: ('Bal\xc3\xb5es do Jo\xc3\xa3o', ''),
    2670: ('Sopa no Garfo', ''),
    2671: ('', ''),
    2701: ('', ''),
    2704: ('Cinemas Multiplex', ''),
    2705: ('Instrumentos Barulhentos do Sabich\xc3\xa3o', ''),
    2708: ('Cola Azul', ''),
    2711: ('Correio de Toontown', ''),
    2712: ('Caf\xc3\xa9 do Risada', ''),
    2713: ('Caf\xc3\xa9 da Madrugargalhada', ''),
    2714: ('CinePlex Lesado', ''),
    2716: ('Sopas e Surtos', ''),
    2717: ('Latas engarrafadas', ''),
    2720: ('Oficina do Chilique', ''),
    2725: ('', ''),
    2727: ('Garrafas e Conservas do Gasoso', ''),
    2728: ('Sorvete Sumi\xc3\xa7o', ''),
    2729: ('Peixinhos Dourados Ki-late', ''),
    2730: ('Not\xc3\xadcias Divertidas', ''),
    2731: ('', ''),
    2732: ('Espaguete Maluquete', ''),
    2733: ('Pipas de Ferro', ''),
    2734: ('Copos de Leite Chupa-chupa', ''),
    2735: ('Casa do Cabum', ''),
    2739: ('Restaura\xc3\xa7\xc3\xa3o de Gargalhadas', ''),
    2740: ('Roj\xc3\xb5es Usados', ''),
    2741: ('', ''),
    2742: ('', ''),
    2743: ('Lavagem a Seco Beca', ''),
    2744: ('', ''),
    2747: ('Tinta Vis\xc3\xadvel', ''),
    2748: ('Zombarias para Gargalhadas', ''),
    2801: ('Estofados Iupii', ''),
    2802: ('Bolas de Ferro Infl\xc3\xa1veis', ''),
    2803: ('Karnaval Kid', ''),
    2804: ('Dr. Puxaperna, Ortopedista', ''),
    2805: ('', ''),
    2809: ('Academia Gra\xc3\xa7a da Piada', ''),
    2814: ('Teatro de Toontown', ''),
    2818: ('A Torta Voadora', ''),
    2821: ('', ''),
    2822: ('Sandu\xc3\xadches de Frango de Borracha', ''),
    2823: ('Sorvetes e Sundaes Divertidos', ''),
    2824: ('Cinema Pal\xc3\xa1cio do Auge da Gra\xc3\xa7a', ''),
    2829: ('Truques e Trocadilhos', ''),
    2830: ('Tiradas R\xc3\xa1pidas', ''),
    2831: ('Casa do Sorriso Amarelo do Professor Balan\xc3\xa7o', ''),
    2832: ('', ''),
    2833: ('', ''),
    2834: ('Sala de Emerg\xc3\xaancia Osso Bom', ''),
    2836: ('', ''),
    2837: ('Centro de Estudos R\xc3\xa1 R\xc3\xa1 R\xc3\xa1', ''),
    2839: ('Grude Massas', ''),
    2841: ('', ''),
    1506: ('Loja de Piadas', ''),
    1507: (lToonHQ, ''),
    1508: ('Loja de Roupas', ''),
    1510: ('Loja de Animais', ''),
    1602: ('Salva-vidas Usados', ''),
    1604: ('Lavagem a Seco Roupa de Mergulho', ''),
    1606: ('Conserto de Rel\xc3\xb3gios do Gancho', ''),
    1608: ('Bugigangas a Vela', ''),
    1609: ('Iscas e Petiscos', ''),
    1612: ('Banco Moedinha no Conv\xc3\xa9s', ''),
    1613: ('Lula Ki Pro Quo, Advogados', ''),
    1614: ('Butique Unha Afiada', ''),
    1615: ('E a\xc3\xad, Galera?', ''),
    1616: ('Sal\xc3\xa3o de Beleza Barba Azul', ''),
    1617: ('\xc3\x93tica Olha L\xc3\xa1', ''),
    1619: ('Arboristas Desembarcar!', ''),
    1620: ('Da Proa \xc3\xa0 Popa', ''),
    1621: ('Academia Castelo de Popa', ''),
    1622: ('Artigos El\xc3\xa9tricos Isca Interruptora', ''),
    1624: ('Reparos de Pescadas na Hora', ''),
    1626: ('Roupas de Gala Salm\xc3\xa3o Encantado', ''),
    1627: ('Atacado de B\xc3\xbassolas do Levi Legal', ''),
    1628: ('Pianos Atum', ''),
    1629: ('', ''),
    1701: ('Creche Peixinho Feliz', ''),
    1703: ('Restaurante China Prancha', ''),
    1705: ('Velas \xc3\xa0 Venda', ''),
    1706: ('Pasta de Amendoim e \xc3\x81gua-viva', ''),
    1707: ('Presentes Golfinho Fofinho', ''),
    1709: ('Veleiros e Gelatinas', ''),
    1710: ('Liquida\xc3\xa7\xc3\xa3o das Cracas', ''),
    1711: ('Restaurante Fundo do Mar', ''),
    1712: ('Academia da Gera\xc3\xa7\xc3\xa3o Sa\xc3\xbade', ''),
    1713: ('Mercado Carta Marinha do M\xc3\xa1rio', ''),
    1714: ('Hotel do Otto', ''),
    1716: ('Roupas de Banho Sereias', ''),
    1717: ('Curso de Navega\xc3\xa7\xc3\xa3o \xc3\x81guas do Pac\xc3\xadfico', ''),
    1718: ('Servi\xc3\xa7os de T\xc3\xa1xi Banco de Areia', ''),
    1719: ('Empresas Correntes do Sul', ''),
    1720: ('A Loja do Molinete', ''),
    1721: ('Armarinho Marinho', ''),
    1723: ('Alga Marinha do Lula', ''),
    1724: ('A Enguia Moderna', ''),
    1725: ('Centro de Caranguejos Pr\xc3\xa9-fabricados do Salgado', ''),
    1726: ('Cerveja Preta Flutuante', ''),
    1727: ('Rema aqui, Rema l\xc3\xa1', ''),
    1728: ('Caranguejos-ferradura Boa Sorte', ''),
    1729: ('', ''),
    1802: ('Nada como N\xc3\xa1utica', ''),
    1804: ('Gin\xc3\xa1sio Mexilh\xc3\xa3o da Praia', ''),
    1805: ('Caixa de Ferramentas Lanches', ''),
    1806: ('Loja de Chap\xc3\xa9us Emborcado', ''),
    1807: ('Loja do H\xc3\xa9lice', ''),
    1808: ('N\xc3\xb3s Sam\xc3\xa3e', ''),
    1809: ('Balde Enferrujado', ''),
    1810: ('Administra\xc3\xa7\xc3\xa3o de \xc3\x82ncoras', ''),
    1811: ('Canoa para L\xc3\xa1, Canoa para C\xc3\xa1?', ''),
    1813: ('Press\xc3\xa3o do Pier Consultoria', ''),
    1814: ('Parada do \xc3\x93', ''),
    1815: ('Qual \xc3\xa9, galerinha?', ''),
    1818: ('Caf\xc3\xa9 dos Sete Mares', ''),
    1819: ('Restaurante Cais', ''),
    1820: ('Loja de Pegadinhas Linha e Anzol', ''),
    1821: ('Conservas Rei Netuno', ''),
    1823: ('Assados Ostra', ''),
    1824: ('Remo Cachorrinho', ''),
    1825: ('Mercado de Peixes Cavala Trotante!', ''),
    1826: ('Arm\xc3\xa1rios Embutidos do M\xc3\xa1rio Metido', ''),
    1828: ('Mans\xc3\xa3o da Alice Cascalh\xc3\xa3o', ''),
    1829: ('Loja de Esculturas Piscicultura', ''),
    1830: ('Linguados e Perdidos', ''),
    1831: ('Alga Mais em sua Casa', ''),
    1832: ('Hipermercado Mastro do Moby', ''),
    1833: ('Alfaiataria sob Medida Seu Mastro', ''),
    1834: ('Rid\xc3\xadquilhas!', ''),
    1835: ('', ''),
    4503: ('Loja de Piadas', ''),
    4504: (lToonHQ, ''),
    4506: ('Loja de Roupas', ''),
    4508: ('Loja de Animais', ''),
    4603: ('Baterias do Tomtom', ''),
    4604: ('A Quatro M\xc3\xa3os', ''),
    4605: ('Violinos da Fifi', ''),
    4606: ('Casa da Castanhola', ''),
    4607: ('Trajes de Gala Toon', ''),
    4609: ('Teclas de Piano D\xc3\xb3-r\xc3\xa9-mi', ''),
    4610: ('O Bom Refr\xc3\xa3o', ''),
    4611: ('Faqueiros Diapas\xc3\xa3o', ''),
    4612: ('Cl\xc3\xadnica Dent\xc3\xa1ria Dr. Triturador', ''),
    4614: ('Barbearia Musical', ''),
    4615: ('Pizza do Flautim', ''),
    4617: ('Bandolins Animados', ''),
    4618: ('Banheiros P\xc3\xbablicos', ''),
    4619: ('Mar Ca\xc3\xa7\xc3\xa3o', ''),
    4622: ('Travesseiros Descanso de Queixo', ''),
    4623: ('Afia\xc3\xa7\xc3\xa3o Bemol', ''),
    4625: ('Pasta de Dente Tuba', ''),
    4626: ('Notas Musicais', ''),
    4628: ('Seguradora Acidental', ''),
    4629: ('Pratos de Papel Refr\xc3\xa3o', ''),
    4630: ('A M\xc3\xbasica \xc3\xa9 o nosso Forte', ''),
    4631: ('Aux\xc3\xadlio Canto Neiras', ''),
    4632: ('Loja do Rock', ''),
    4635: ('Not\xc3\xadcias do Tenor', ''),
    4637: ('A Boa Escala', ''),
    4638: ('Loja do Heavy Metal', ''),
    4639: ('Antiguidades Oitenta', ''),
    4641: ('Jornal dos Blues', ''),
    4642: ('Lavagem a Seco Beca', ''),
    4645: ('Clube 88', ''),
    4646: ('', ''),
    4648: ('Mudan\xc3\xa7as Carregando Toons', ''),
    4649: ('', ''),
    4652: ('Loja de Conveni\xc3\xaancia Ponto Final', ''),
    4653: ('', ''),
    4654: ('Telhados Volume Perfeito', ''),
    4655: ('Escola de Culin\xc3\xa1ria do Terr\xc3\xadvel Chef Agudo', ''),
    4656: ('', ''),
    4657: ('Barbearia Quarteto', ''),
    4658: ('Pianos Submersos', ''),
    4659: ('', ''),
    4701: ('Escola de Dan\xc3\xa7a Jumento Sentimento', ''),
    4702: ('Timbre! Artigos para Lenhadores', ''),
    4703: ('A Mala Madeus', ''),
    4704: ('Concertos de Concertina da Tina', ''),
    4705: ('Zarpou fora', ''),
    4707: ('Est\xc3\xbadio de Efeitos Sonoros Doppler', ''),
    4709: ('Artigos de Montanhismo Pli\xc3\xaa', ''),
    4710: ('Auto-escola Pouca Polca', ''),
    4712: ('Borracharia D\xc3\xb3 do Murcho', ''),
    4713: ('Moda Fina Masculina Desafina', ''),
    4716: ('Gaitas de Quatro Segmentos', ''),
    4717: ('Seguradora de Autom\xc3\xb3veis Barateira Bar\xc3\xadtono', ''),
    4718: ('Pe\xc3\xa7as para Chopp-in e Outros Artigos para Cozinha', ''),
    4719: ('Casas-m\xc3\xb3veis Madrigal', ''),
    4720: ('D\xc3\xaa um Nome a este Toon', ''),
    4722: ('Substitutos Abertura', ''),
    4723: ('Artigos para Parquinhos Infantis Ex-condesconde', ''),
    4724: ('Moda Infantil Inci Dental', ''),
    4725: ('O Barbeiro Bar\xc3\xadtono', ''),
    4727: ('Bordados Corda Vocal', ''),
    4728: ('Solo Vocal N\xc3\xa3o d\xc3\xa1 pra Ouvir', ''),
    4729: ('Livraria Obo\xc3\xa9', ''),
    4730: ('Sebo de Letras de M\xc3\xbasicas', ''),
    4731: ('Tons dos Toons', ''),
    4732: ('Companhia Teatral Prega Pe\xc3\xa7a', ''),
    4733: ('', ''),
    4734: ('', ''),
    4735: ('Acorde N\xc3\xa3o!', ''),
    4736: ('Planejamento Matrimonial Casal Hino Esperado', ''),
    4737: ('Lonas Harpa', ''),
    4738: ('Presentes Cantata do Tat\xc3\xa1', ''),
    4739: ('', ''),
    4801: ('Ponto do Punk', ''),
    4803: ('Servi\xc3\xa7os de Governan\xc3\xa7a Que Mezza!', ''),
    4804: ('Curso de Barman Shake Shake Shake', ''),
    4807: ('N\xc3\xa3o Quebre o Bra\xc3\xa7o', ''),
    4809: ('N\xc3\xa3o Com Verso!', ''),
    4812: ('', ''),
    4817: ('Loja de Animais Trin Can\xc3\xa1rio', ''),
    4819: ('Cavaquinhos da Cavaca', ''),
    4820: ('', ''),
    4821: ('Cruzeiros da Ana', ''),
    4827: ('Rel\xc3\xb3gios Ritmo Cadente', ''),
    4828: ('Sapatos Masculinos Rima', ''),
    4829: ('Bolas de Canh\xc3\xa3o Vaga Ner', ''),
    4835: ('Fundamentos Musicais para Felinos Felizes', ''),
    4836: ('Regalias do Reggae', ''),
    4838: ('Escola de M\xc3\xbasica K. Zuza', ''),
    4840: ('Bebidas Musicais Pop Rock', ''),
    4841: ('Bandoleiro Bandolins!', ''),
    4842: ('Corpora\xc3\xa7\xc3\xa3o Sincopa\xc3\xa7\xc3\xa3o', ''),
    4843: ('', ''),
    4844: ('Motocicletas Com Nota\xc3\xa7\xc3\xa3o', ''),
    4845: ('Elegias Elegantes da Elen', ''),
    4848: ('Financeira Cordas de Dinheiro', ''),
    4849: ('', ''),
    4850: ('Hipoteca Cordas Emprestadas', ''),
    4852: ('Arranca-peles Flauta Florida', ''),
    4853: ('Para-choques do L\xc3\xa9o Guitarra', ''),
    4854: ('V\xc3\xaddeos de Violinos Vocacionais Wagner', ''),
    4855: ('Rede de Televis\xc3\xa3o Teleouvisa', ''),
    4856: ('', ''),
    4862: ('Quatrilhos Quintessenciais do Quarentino', ''),
    4867: ('Celos Amarelos do Costello', ''),
    4868: ('', ''),
    4870: ('Zool\xc3\xb3gico de Ziriguidum do Ziggy', ''),
    4871: ('Humbuckers \xc3\x9anicos do Ubaldo', ''),
    4872: ('Bra\xc3\xa7os sem Estresse do Estev\xc3\xa3o Expresso', ''),
    4873: ('', ''),
    5501: ('Loja de Piadas', ''),
    5502: (lToonHQ, ''),
    5503: ('Loja de Roupas', ''),
    5505: ('Loja de Animais', ''),
    5601: ('Exames de Vista Olho do Alho', ''),
    5602: ('Gravatas do S\xc3\xa9rgio Sufocado', ''),
    5603: ('Verde que te Quero Verdura', ''),
    5604: ('Loja de Noivas Mel e L\xc3\xa3o', ''),
    5605: ('Sobre Mesas e Cadeiras', ''),
    5606: ('P\xc3\xa9talas', ''),
    5607: ('Correios Adubo Expresso', ''),
    5608: ('Toca da Pipoca', ''),
    5609: ('Tesouro dos Dentes de Alho de Ouro', ''),
    5610: ('Aulas de Boxe da Susana Olhos Negros', ''),
    5611: ('Piadas do Toupeira', ''),
    5613: ('Barbeiros Tosa Completa', ''),
    5615: ('Ra\xc3\xa7\xc3\xa3o para P\xc3\xa1ssaros do Flor\xc3\xaancio', ''),
    5616: ('Pousada Pouso da Coruja', ''),
    5617: ('Borboletas do Borba Oleta', ''),
    5618: ('Ervilhas e Milhas', ''),
    5619: ('P\xc3\xa9s de feij\xc3\xa3o do Jo\xc3\xa3o', ''),
    5620: ('Pousada P\xc3\xa1 de Coisa', ''),
    5621: ('Uvinhas da Ira', ''),
    5622: ('Loja de Bicicletas Bem-me-quer', ''),
    5623: ('Banheiras para P\xc3\xa1ssaros Bolhinhas Aladas', ''),
    5624: ('Bico Calado', ''),
    5625: ('Os Abelhudos', ''),
    5626: ('Artesanato P\xc3\xadnus', ''),
    5627: ('', ''),
    5701: ('Do In\xc3\xadcio ao Figo', ''),
    5702: ('Ancinho do Jo\xc3\xa3ozinho', ''),
    5703: ('Fotos C\xc3\xadntia', ''),
    5704: ('Carros Usados Lisa Lima', ''),
    5705: ('M\xc3\xb3veis Urtigas', ''),
    5706: ('Joalheiros 14 Ki Latas', ''),
    5707: ('Fruta Musical', ''),
    5708: ('Ag\xc3\xaancia de Viagens Erva da Ninha', ''),
    5709: ('Cortadores de Grama R\xc3\xa9 U. Vassint\xc3\xa9tica', ''),
    5710: ('Academia Dur\xc3\xa3o', ''),
    5711: ('Roupas \xc3\x8dntimas Jardim de Inverno', ''),
    5712: ('Est\xc3\xa1tuas Idiotas', ''),
    5713: ('M\xc3\xa3os \xc3\xa0 Obra', ''),
    5714: ('\xc3\x81gua Mineral Chuva de Ver\xc3\xa3o', ''),
    5715: ('Not\xc3\xadcias do Campo', ''),
    5716: ('Hipotecas Folhas Ca\xc3\xaddas', ''),
    5717: ('Seivas Florais', ''),
    5718: ('Animais Ex\xc3\xb3ticos Mauricinho Le\xc3\xa3o', ''),
    5719: ('Investigadores Particulares Cara que Manch\xc3\xa3o!', ''),
    5720: ('Moda Masculina Bran Covinho', ''),
    5721: ('Restaurante Rota 66', ''),
    5725: ('Cervejaria da Cevada', ''),
    5726: ('Terra Adubada do Ubaldo', ''),
    5727: ('Financeira Toupeira Encurralada', ''),
    5728: ('', ''),
    5802: (lToonHQ, ''),
    5804: ('Vazar ou n\xc3\xa3o Vazar?', ''),
    5805: ('Correio da Lesma', ''),
    5809: ('Escola de Palha\xc3\xa7os Fungos', ''),
    5810: ('Mela o Melado', ''),
    5811: ('Pousada Al Face a Face', ''),
    5815: ('Rural', ''),
    5817: ('Ma\xc3\xa7\xc3\xa3s e Laranjas', ''),
    5819: ('Jeans Vagem Verde', ''),
    5821: ('Academia Amassado e Esticado', ''),
    5826: ('Artigos para o Cultivo de Formigas', ''),
    5827: ('Promo\xc3\xa7\xc3\xa3o de Aterrar', ''),
    5828: ('M\xc3\xb3veis Batatinha Quando Nasce', ''),
    5830: ('Espalhado o Babado', ''),
    5833: ('Restaurante Saladas', ''),
    5835: ('Caf\xc3\xa9 Colonial Flores do Campo', ''),
    5836: ('Tubula\xc3\xa7\xc3\xb5es e \xc3\x81guas de M\xc3\xa1rcia', ''),
    5837: ('Curso de En\xc3\xb3logo', ''),
    9501: ('Biblioteca da Can\xc3\xa7\xc3\xa3o de Ninar', ''),
    9503: ('O Bar da Soneca', ''),
    9504: ('Loja de Piadas', ''),
    9505: (lToonHQ, ''),
    9506: ('Loja de Roupas', ''),
    9508: ('Loja de Animais', ''),
    9601: ('Pousada A. Ninho', ''),
    9602: ('Dois Dedos de Prosa com Morfeu pelo Pre\xc3\xa7o de Um', ''),
    9604: ('Sof\xc3\xa1-cama Amarelo do Marcelo', ''),
    9605: ('Travessa da Can\xc3\xa7\xc3\xa3o de Ninar, 323', ''),
    9607: ('Pijamas Bahamas da Mama', ''),
    9608: ('Erva-de-gato para Tirar um Cochilo', ''),
    9609: ('Sono de Pedra por uma Bagatela', ''),
    9613: ('Relojoeiros das Alturas', ''),
    9616: ('Companhia El\xc3\xa9trica Luzes Apagadas', ''),
    9617: ('Travessa da Can\xc3\xa7\xc3\xa3o de Ninar, 212', ''),
    9619: ('Relaxe ao M\xc3\xa1ximo', ''),
    9620: ('Servi\xc3\xa7os de T\xc3\xa1xi Py Jama', ''),
    9622: ('Rel\xc3\xb3gios Sono Atrasado', ''),
    9625: ('Sal\xc3\xa3o de Beleza Enrolado Crespo', ''),
    9626: ('Travessa da Can\xc3\xa7\xc3\xa3o de Ninar, 818', ''),
    9627: ('A Tenda dos Sonhos', ''),
    9628: ('Calend\xc3\xa1rios J\xc3\xa1 Chega por Hoje', ''),
    9629: ('Travessa da Can\xc3\xa7\xc3\xa3o de Ninar, 310', ''),
    9630: ('Pedreira Sono de Pedra', ''),
    9631: ('Conserto de Rel\xc3\xb3gios Inatividade', ''),
    9633: ('Sala de Proje\xc3\xa7\xc3\xa3o da Sonhol\xc3\xa2ndia', ''),
    9634: ('Colch\xc3\xb5es Descanso da Mente', ''),
    9636: ('Seguradora Ins\xc3\xb4nia', ''),
    9639: ('Casa de Hiberna\xc3\xa7\xc3\xa3o', ''),
    9640: ('Travessa da Can\xc3\xa7\xc3\xa3o de Ninar, 805', ''),
    9642: ('Serraria Lombeira da Madeira', ''),
    9643: ('Exames de Vista Olho Fechado', ''),
    9644: ('Guerras de Travesseiro Noturnas', ''),
    9645: ('Pousada Unidos Venceremos', ''),
    9647: ('Loja de Ferragens Fa\xc3\xa7a a sua Cama', ''),
    9649: ('Ranking do Ronco', ''),
    9650: ('Travessa da Can\xc3\xa7\xc3\xa3o de Ninar, 714', ''),
    9651: ('Com Muito ou com Ronco', ''),
    9652: ('', ''),
    9703: ('Ag\xc3\xaancia de Viagens V\xc3\xb4o Noturno', ''),
    9704: ('Loja de Animais Coruja Noturna', ''),
    9705: ('Oficina Dormindo ao Volante', ''),
    9706: ('Cl\xc3\xadnica Dent\xc3\xa1ria Fada do Dente', ''),
    9707: ('Centro de Jardinagem Bocejo Matutino', ''),
    9708: ('Floricultura Leito de Rosas', ''),
    9709: ('Encanamentos Sonho do Bombeiro', ''),
    9710: ('Exames de Vista REM', ''),
    9711: ('Companhia Telef\xc3\xb4nica Despertador', ''),
    9712: ('Contagem de Ovelhas - N\xc3\xb3s Contamos para Voc\xc3\xaa!', ''),
    9713: ('Pisca-duro, Pestana e Cabe\xc3\xa7ada, Advogados', ''),
    9714: ('Artigos Mar\xc3\xadtimos Barco dos Sonhos', ''),
    9715: ('Banco A Fraldinha de Dormir', ''),
    9716: ('Pipi na Cama Festas', ''),
    9717: ('Padaria Sonho \xc3\xa0 D\xc3\xbazia', ''),
    9718: ('Sandu\xc3\xadches A Cuca Vai Pegar', ''),
    9719: ('F\xc3\xa1brica de Travesseiros Tatu', ''),
    9720: ('Treinamento de Voz Fale Dormindo', ''),
    9721: ('Tapetes Aconchego', ''),
    9722: ('Ag\xc3\xaancia de Talentos Sonho de Menina', ''),
    9725: ('Pijamas Saco de Gato', ''),
    9727: ('Cochilou, Dan\xc3\xa7ou', ''),
    9736: ('Ag\xc3\xaancia de Empregos Trabalho dos Sonhos', ''),
    9737: ('Escola de Dan\xc3\xa7a Matilda Madruga', ''),
    9738: ('Casa de Zzzzzs', ''),
    9740: ('Escola de Esgrima Nan\xc3\xa1', ''),
    9741: ('Deu Pulga na Cama Exterm\xc3\xadnio de Insetos', ''),
    9744: ('Creme para Rugas Chega de Ins\xc3\xb4nia', ''),
    9752: ('Petroleira Meia-Noite', ''),
    9753: ('Sorveteria Luar Gelado', ''),
    9754: ('Passeios de P\xc3\xb4nei Cavalgada Noturna', ''),
    9755: ('Cinemas Cama Voadora', ''),
    9756: ('', ''),
    9759: ('Sal\xc3\xa3o de Beleza Bela Adormecida', ''),
    3507: ('Loja de Piadas', ''),
    3508: (lToonHQ, ''),
    3509: ('Loja de Roupas', ''),
    3511: ('Loja de Animais', ''),
    3601: ('Companhia El\xc3\xa9trica Esplendor do Norte', ''),
    3602: ('Gorros do P\xc3\xb3lo Norte', ''),
    3605: ('', ''),
    3607: ('Mago do Lago Congelado', ''),
    3608: ('Existe um Lugar', ''),
    3610: ('Hipermercado de Sapatos de Esquim\xc3\xb3 Quiproc\xc3\xb3', ''),
    3611: ('Rodinho do Le\xc3\xa3o Marinho', ''),
    3612: ('Design de Iglus', ''),
    3613: ('Cicle Geloso', ''),
    3614: ('Ind\xc3\xbastria de Cereais Flocos de Neve', ''),
    3615: ('Past\xc3\xa9is de Forno Lindo Alasca', ''),
    3617: ('Passeios de Bal\xc3\xa3o Vento Frio', ''),
    3618: ('Consultoria de Gest\xc3\xa3o de Crises Grande Coisa!', ''),
    3620: ('Cl\xc3\xadnica do Esqui', ''),
    3621: ('Sorveteria Gelo Derretido', ''),
    3622: ('', ''),
    3623: ('Ind\xc3\xbastria de P\xc3\xa3es Torradinha', ''),
    3624: ('Sanduicheria Abaixo de Zero', ''),
    3625: ('Aquecedores Tia Freezer', ''),
    3627: ('Canil S\xc3\xa3o Bernardo', ''),
    3629: ('Restaurante Sopa de Ervilhas', ''),
    3630: ('Ag\xc3\xaancia de Viagens Com Gelo em Londres, Com Gelo na Fran\xc3\xa7a', ''),
    3634: ('Telef\xc3\xa9rico Boa Vista', ''),
    3635: ('Lenha Usada', ''),
    3636: ('Promo\xc3\xa7\xc3\xa3o de Arrepios', ''),
    3637: ('Skates da Kate', ''),
    3638: ('Tobog\xc3\xa3 da L\xc3\xa3', ''),
    3641: ('Tren\xc3\xb3 do Chic\xc3\xb3', ''),
    3642: ('\xc3\x93tica Olho do Furac\xc3\xa3o', ''),
    3643: ('Sal\xc3\xa3o Bola de Neve', ''),
    3644: ('Cubos de Gelo Derretidos', ''),
    3647: ('Loja de Smokings Pinguim Animado', ''),
    3648: ('Sorvete Instant\xc3\xa2neo', ''),
    3649: ('Hambrrrgers', ''),
    3650: ('Antiguidades Ant\xc3\xa1rctica', ''),
    3651: ('Salsichas Congeladas do Fred Barbicha', ''),
    3653: ('Joalheria Cristal do Gelo', ''),
    3654: ('', ''),
    3702: ('Armaz\xc3\xa9m do Inverno', ''),
    3703: ('', ''),
    3705: ('Cicle Pingo Congelado para Dois', ''),
    3706: ('F\xc3\xa1brica de Refrigerantes Treme-treme', ''),
    3707: ('Neve Doce Neve', ''),
    3708: ('Loja do Pluto', ''),
    3710: ('Temperatura em Queda Refei\xc3\xa7\xc3\xb5es', ''),
    3711: ('', ''),
    3712: ('Vai por Gelo Abaixo', ''),
    3713: ('Dentista Abaixo de Zero Tiritante', ''),
    3715: ('Casa de Sopas Tia \xc3\x81rtica', ''),
    3716: ('Estrada de Sal e Pimenta', ''),
    3717: ('A Lasca Verbal', ''),
    3718: ('Designer de C\xc3\xa2maras de Ar', ''),
    3719: ('Cubo de Gelo no Palitinho', ''),
    3721: ('Liquida\xc3\xa7\xc3\xa3o de Tobog\xc3\xa3s Cabe\xc3\xa7\xc3\xa3o', ''),
    3722: ('Loja de Esquis Coelhinho de Neve', ''),
    3723: ('Bolas de Neve Tremend\xc3\xa3o', ''),
    3724: ('Fatos e Fofocas', ''),
    3725: ('O N\xc3\xb3 do Tren\xc3\xb3', ''),
    3726: ('Cobertores com Energia Solar', ''),
    3728: ('Tratores de Neve Anta Lenta', ''),
    3729: ('', ''),
    3730: ('Compra e Venda de Bonecos de Neve', ''),
    3731: ('Lareiras Port\xc3\xa1teis', ''),
    3732: ('O Nariz Congelado', ''),
    3734: ('Exames de Vista C. V. Gelo', ''),
    3735: ('Capas de Gelo Polar', ''),
    3736: ('Cubos de Gelo com Zelo', ''),
    3737: ('Restaurante Montanha Abaixo', ''),
    3738: ('Aquecimento - Aproveite Enquanto est\xc3\xa1 Quente', ''),
    3739: ('', ''),
    3801: (lToonHQ, ''),
    3806: ('Linha de Comida Alpina', ''),
    3807: ('Sombras de Marmota Usadas', ''),
    3808: ('A Cabana Suadoura', ''),
    3809: ('Elvira T\xc3\xa3o Bem', ''),
    3810: ('O Bom Edredom', ''),
    3811: ('Seu Anjo de Neve', ''),
    3812: ('Gatinhos de Luvas', ''),
    3813: ('Botas de Neve Essenciais', ''),
    3814: ('Banca de Refrigerantes G\xc3\xa1s-na-Boca', ''),
    3815: ('O Chal\xc3\xa9 da Peruca', ''),
    3816: ('Viste o Visco', ''),
    3817: ('Clube de Trilha de Inverno do Pa\xc3\xads das Maravilhas', ''),
    3818: ('A Barraca das P\xc3\xa1s', ''),
    3819: ('Servi\xc3\xa7o de Chamin\xc3\xa9s Sopro Limpo', ''),
    3820: ('Brancura de Neve', ''),
    3821: ('F\xc3\xa9rias Hibernantes', ''),
    3823: ('Funda\xc3\xa7\xc3\xb5es e Precipita\xc3\xa7\xc3\xb5es', ''),
    3824: ('Nozes Assadas na Fogueira', ''),
    3825: ('Chap\xc3\xa9us do Gato Legal', ''),
    3826: ('Ai, Minhas Galochas!', ''),
    3827: ('Grinaldas Corais', ''),
    3828: ('Terra do Homem de Neve', ''),
    3829: ('\xc3\x81rea dos Pinheiros', ''),
    3830: ('Desemba\xc3\xa7amento de \xc3\x93culos Espere-e-Veja', '') }
ClosetTimeoutMessage = 'Sinto muito, o tempo\n acabou.'
ClosetNotOwnerMessage = 'Este n\xc3\xa3o \xc3\xa9 o seu arm\xc3\xa1rio, mas voc\xc3\xaa pode experimentar as roupas.'
ClosetPopupOK = lOK
ClosetPopupCancel = lCancel
ClosetDiscardButton = 'Remover'
ClosetAreYouSureMessage = 'Voc\xc3\xaa excluiu algumas roupas. Deseja mesmo exclu\xc3\xad-las?'
ClosetYes = lYes
ClosetNo = lNo
ClosetVerifyDelete = 'Excluir mesmo %s?'
ClosetShirt = 'esta camisa'
ClosetShorts = 'este short'
ClosetSkirt = 'esta saia'
ClosetDeleteShirt = 'Excluir\ncamisa'
ClosetDeleteShorts = 'Excluir\nshort'
ClosetDeleteSkirt = 'Excluir\nsaia'
EstateOwnerLeftMessage = 'Sinto muito, o dono desta propriedade saiu. Voc\xc3\xaa ser\xc3\xa1 enviado ao p\xc3\xa1tio em %s segundos'
EstatePopupOK = lOK
EstateTeleportFailed = 'N\xc3\xa3o foi poss\xc3\xadvel ir para casa. Tente novamente!'
EstateTeleportFailedNotFriends = 'Sinto muito, %s fica na propriedade de um toon com o qual voc\xc3\xaa n\xc3\xa3o fez amizade.'
EstateTargetGameStart = 'O jogo do Alvo de Toonar come\xc3\xa7ou!'
EstateTargetGameInst = 'Quanto mais acertar no alvo vermelho, mais Toonar voc\xc3\xaa vai receber.'
EstateTargetGameEnd = 'O jogo de Alvo de Toonar acabou...'
AvatarsHouse = 'Casa de\n %s'
BankGuiCancel = lCancel
BankGuiOk = lOK
DistributedBankNoOwner = 'Sinto muito, este n\xc3\xa3o \xc3\xa9 o seu banco.'
DistributedBankNotOwner = 'Sinto muito, este n\xc3\xa3o \xc3\xa9 o seu banco.'
FishGuiCancel = lCancel
FishGuiOk = 'Vender tudo'
FishTankValue = 'Oi, %(name)s! Voc\xc3\xaa tem %(num)s peixe(s) em seu balde, que vale(m) o total de %(value)s balinhas. Deseja vender todos eles?'
FlowerGuiCancel = lCancel
FlowerGuiOk = 'Vender Tudo'
FlowerBasketValue = '%(name)s, voc\xc3\xaa tem %(num)s flores no seu cesto que valem um total de %(value)s balinhas. Voc\xc3\xaa quer vender todas?'

def GetPossesive(name):
    if name[-1:] == 'de':
        possesive = name + "'"
    else:
        possesive = name + ''
    return possesive

PetTrait2descriptions = {
    'hungerThreshold': ('Sempre faminto', 'Muito faminto', '\xc3\x80s vezes faminto', 'Raramente faminto'),
    'boredomThreshold': ('Sempre chateado', 'Muito chateado', '\xc3\x80s vezes chateado', 'Raramente chateado'),
    'angerThreshold': ('Sempre irritado', 'Muito irritado', '\xc3\x80s vezes irritado', 'Raramente irritado'),
    'forgetfulness': ('Sempre esquecido', 'Muito esquecido', '\xc3\x80s vezes esquecido', 'Raramente esquecido'),
    'excitementThreshold': ('Muito calmo', 'Bem calmo', 'Bem animado', 'Muito animado'),
    'sadnessThreshold': ('Sempre triste', 'Muitas vezes triste', '\xc3\x80s vezes triste', 'Raramente triste'),
    'restlessnessThreshold': ('Sempre inquieto', 'Muito inquieto', '\xc3\x80s vezes inquieto', 'Raramente inquieto'),
    'playfulnessThreshold': ('Raramente brincalh\xc3\xa3o', '\xc3\x80s vezes brincalh\xc3\xa3o', 'Muito brincalh\xc3\xa3o', 'Sempre brincalh\xc3\xa3o'),
    'lonelinessThreshold': ('Sempre solit\xc3\xa1rio', 'Muito solit\xc3\xa1rio', '\xc3\x80s vezes solit\xc3\xa1rio', 'Raramente solit\xc3\xa1rio'),
    'fatigueThreshold': ('Sempre cansado', 'Muito cansado', '\xc3\x80s vezes cansado', 'Raramente cansado'),
    'confusionThreshold': ('Sempre confuso', 'Muito confuso', '\xc3\x80s vezes confuso', 'Raramente confuso'),
    'surpriseThreshold': ('Sempre surpreso', 'Muito surpreso', '\xc3\x80s vezes surpreso', 'Raramente surpreso'),
    'affectionThreshold': ('Raramente carinhoso', '\xc3\x80s vezes carinhoso', 'Muito carinhoso', 'Sempre carinhoso') }
FireworksInstructions = lToonHQ + ': Pressione a tecla "Page Up" para ver melhor.'
startFireworksResponse = "Usage: startFireworksShow ['num']\n                                         'num' = %s - New Years\n                                         %s - Party Summer \n                                         %s - 4th of July"
FireworksValentinesBeginning = ''
FireworksValentinesEnding = ''
FireworksJuly4Beginning = lToonHQ + ': Bem-vindo \xc3\xa0 queima de fogos de ver\xc3\xa3o! Divirta-se com o show!'
FireworksJuly4Ending = lToonHQ + ': Espero que tenha gostado do show! Um \xc3\xb3timo ver\xc3\xa3o para voc\xc3\xaa!'
FireworksJuly14Beginning = lToonHQ + ''
FireworksJuly14Ending = lToonHQ + ''
FireworksOctober31Beginning = ''
FireworksOctober31Ending = ''
FireworksNewYearsEveBeginning = lToonHQ + ': Feliz Ano Novo!!!!'
FireworksNewYearsEveEnding = lToonHQ + ': Gostou dos Fogos? Logo tem mais!'
FireworksBeginning = lToonHQ + ': Bem-vindo \xc3\xa0 queima de fogos de ver\xc3\xa3o! Divirta-se com o show!'
FireworksEnding = lToonHQ + ': Espero que tenha gostado do show! Um \xc3\xb3timo ver\xc3\xa3o para voc\xc3\xaa!'
BlockerTitle = 'CARREGANDO TOONTOWN...'
BlockerLoadingTexts = [
    'Esfregando latas de torta',
    'Assando crostas de torta',
    'Aquecendo recheio de torta',
    'Carregando Doodle chow',
    'Alinhando Jungle Vines',
    'Soltando as aranhas que rastejam pelas jungle vines',
    'Plantando sementes de flores que esguicham',
    'Esticando trampolins',
    'Reunindo porcos',
    "Ajustando sons de 'SPLAT'",
    'Limpando \xc3\xb3culos de hipnose',
    'Desengarrafando tinta para as Not\xc3\xadcias Toon',
    'Cortando estopins de TNT',
    "Colocando a placa 'Em constru\xc3\xa7\xc3\xa3o' no Bosque de Bolotas",
    'Andando como o Pato Donald',
    'Ensinando novos passos a hidrantes dan\xc3\xa7antes',
    'Amarrando Shticker Books',
    'Analyzing quacks',
    'Colhendo balinhas',
    'Esvaziando baldes de peixe',
    'Encurralando lixo de lixeira',
    'Espalhando graxa de Cog',
    'Polindo trof\xc3\xa9us de kart',
    'Balan\xc3\xa7a para pesar uma tonelada',
    'Praticando Dan\xc3\xa7as da Vit\xc3\xb3ria',
    'Preparando maluquices',
    "Mostrando a placa de 'cinco minutos' ao Mickey Mouse",
    'Testando luvas brancas',
    'Tocando sinos submersos',
    'Bobinando fita vermelha',
    'Congelando, brrr, gelo',
    'Afiando pianos que caem']
TIP_NONE = 0
TIP_GENERAL = 1
TIP_STREET = 2
TIP_MINIGAME = 3
TIP_COGHQ = 4
TIP_ESTATE = 5
TIP_KARTING = 6
TIP_GOLF = 7
TipTitle = 'DICA TOON:'
TipDict = {
    TIP_NONE: ('',),
    TIP_GENERAL: ('Verifique com rapidez o andamento da Tarefa Toon mantendo pressionada a tecla "End".', 'Verifique com rapidez a sua P\xc3\xa1gina de piadas mantendo pressionada a tecla "Home".', 'Abra a sua Lista de amigos pressionando a tecla "F7".', 'Abra ou feche o seu \xc3\x81lbum Toon pressionando a tecla "F8".', 'Voc\xc3\xaa pode procurar acima pressionando a tecla "Page Up" e abaixo pressionando a tecla "Page Down".', 'Pressione a tecla "Control" para pular.', 'Pressione a tecla "F9" para capturar a tela, que ser\xc3\xa1 salva na pasta Toontown do seu computador.', 'Voc\xc3\xaa pode alterar a resolu\xc3\xa7\xc3\xa3o de seu v\xc3\xaddeo, ajustar o \xc3\xa1udio e controlar outras op\xc3\xa7\xc3\xb5es na P\xc3\xa1gina de op\xc3\xa7\xc3\xb5es do \xc3\x81lbum Toon.', 'Experimente as roupas de seus amigos no arm\xc3\xa1rio da casa deles.', 'Voc\xc3\xaa pode ir para casa usando o bot\xc3\xa3o "Ir para casa" em seu mapa.', 'Toda vez que voc\xc3\xaa conclui uma Tarefa Toon, seus Pontos de risadas s\xc3\xa3o automaticamente recarregados.', 'Voc\xc3\xaa pode procurar a sele\xc3\xa7\xc3\xa3o nas lojas de roupas mesmo sem ter um bilhete de roupas.', 'As recompensas para algumas Tarefas Toon permitem que voc\xc3\xaa carregue mais piadas e balinhas.', 'Voc\xc3\xaa pode ter at\xc3\xa9 50 amigos na sua Lista de amigos.', 'Algumas recompensas das Tarefas Toon permitem que voc\xc3\xaa se teletransporte para os p\xc3\xa1tios de Toontown usando a P\xc3\xa1gina do mapa do \xc3\x81lbum Toon.', 'Aumente os seus Pontos de risadas nos p\xc3\xa1tios, catando tesouros como estrelas e casquinhas de sorvete.', 'Se voc\xc3\xaa precisar se recuperar r\xc3\xa1pido ap\xc3\xb3s uma batalha dif\xc3\xadcil, v\xc3\xa1 para a sua propriedade e recolha casquinhas de sorvete.', 'Alterne entre os diversos modos de exibi\xc3\xa7\xc3\xa3o de seu Toon pressionando a tecla Tab.', 'Algumas vezes, voc\xc3\xaa poder\xc3\xa1 encontrar v\xc3\xa1rias Tarefas Toon diferentes com a mesma recompensa. Fa\xc3\xa7a sua pesquisa de mercado!', 'Encontrar amigos com Tarefas Toon semelhantes \xc3\xa9 uma maneira divertida de progredir no jogo.', 'Voc\xc3\xaa nunca precisa salvar o seu progresso em Toontown. Os servidores de Toontown salvam continuamente todas as informa\xc3\xa7\xc3\xb5es necess\xc3\xa1rias.', 'Voc\xc3\xaa pode cochichar com outros Toons clicando neles ou selecionando-os em sua Lista de amigos.', 'Algumas frases do Chat r\xc3\xa1pido t\xc3\xaam anima\xc3\xa7\xc3\xb5es para indicar o estado de esp\xc3\xadrito do seu Toon.', 'Se a \xc3\xa1rea em que voc\xc3\xaa est\xc3\xa1 se encontra lotada, tente mudar de regi\xc3\xa3o. V\xc3\xa1 para a P\xc3\xa1gina de regi\xc3\xa3o do \xc3\x81lbum Toon e selecione uma diferente.', 'Se voc\xc3\xaa estiver em plena atividade de salvamento de edif\xc3\xadcios, ganhar\xc3\xa1 uma estrela de bronze, prata ou ouro, que ficar\xc3\xa1 acima de seu Toon.', 'Se voc\xc3\xaa salvar um n\xc3\xbamero suficiente de edif\xc3\xadcios para obter uma estrela acima da cabe\xc3\xa7a, seu nome pode estar no quadro-negro de um Quartel Toon.', 'Os edif\xc3\xadcios salvos, \xc3\xa0s vezes, s\xc3\xa3o recuperados pelos Cogs. A \xc3\xbanica maneira de manter a sua estrela \xc3\xa9 sair em campo e salvar mais edif\xc3\xadcios!', 'Os nomes dos seus Amigos secretos aparecer\xc3\xa3o na cor azul.', 'Veja se voc\xc3\xaa consegue pegar todos os peixes de Toontown!', 'H\xc3\xa1 peixes diferentes nos diversos lagos. Tente todos!', 'Quando o seu balde de pesca estiver cheio, venda os peixes para os pescadores dos p\xc3\xa1tios.', 'Venda os peixes para o pescador ou dentro das Lojas de Animais.', 'As varas de pescar mais fortes conseguem pegar peixes mais pesados, mas custam mais balinhas.', 'Voc\xc3\xaa pode comprar varas de pescar mais fortes no Gad\xc3\xa1logo.', 'Os peixes mais pesados valem mais balinhas na Loja de animais.', 'Os peixes raros valem mais balinhas na Loja de animais.', '\xc3\x80s vezes, voc\xc3\xaa consegue encontrar bolsas de balinhas durante a pesca.', 'Algumas Tarefas Toon exigem que voc\xc3\xaa pesque itens fora dos lagos.', 'Os lagos de pesca dos p\xc3\xa1tios possuem peixes diferentes dos lagos das ruas.', 'Alguns peixes s\xc3\xa3o realmente raros. Continue pescando at\xc3\xa9 pegar todos!', 'O lago da sua propriedade possui peixes que s\xc3\xb3 podem ser encontrados l\xc3\xa1.', 'Para cada dez esp\xc3\xa9cies pescadas, voc\xc3\xaa ganhar\xc3\xa1 um trof\xc3\xa9u de pesca!', 'Voc\xc3\xaa pode ver qual peixe pescou no \xc3\x81lbum Toon.', 'Alguns trof\xc3\xa9us de pesca o recompensam com um Acr\xc3\xa9scimo de risadas.', 'A pesca \xc3\xa9 uma boa maneira de ganhar mais balinhas.', 'Adote um Rabisco na Loja de Animais!', 'As lojas de animais t\xc3\xaam Rabiscos novos para vender todos os dias.', 'Visite as lojas de animais todos os dias para ver que Rabiscos novos elas t\xc3\xaam.', 'H\xc3\xa1 diferentes Rabiscos para ado\xc3\xa7\xc3\xa3o nos diferentes bairros.', 'Mostre o seu carr\xc3\xa3o e d\xc3\xaa uma turbinada no seu limite de Risadas no Aut\xc3\xb3dromo do Pateta. ', 'Entre no Aut\xc3\xb3dromo do Pateta pelo t\xc3\xbanel em forma de pneu no p\xc3\xa1tio do Centro de Toontown.', 'Ganhe pontos de Risada no Aut\xc3\xb3dromo do Pateta.', 'O Aut\xc3\xb3dromo do Pateta tem seis pistas de corrida diferentes. '),
    TIP_STREET: ('H\xc3\xa1 quatro tipos de Cogs: Rob\xc3\xb4s da Lei, Rob\xc3\xb4s Mercen\xc3\xa1rios, Rob\xc3\xb4s Vendedores e Rob\xc3\xb4s-chefe.', 'Cada M\xc3\xa9todo de piadas possui diferentes intensidades de precis\xc3\xa3o e dano.', 'As piadas sonoras afetam todos os Cogs, mas acordam qualquer Cog iscado.', 'Derrotar os Cogs em ordem estrat\xc3\xa9gica pode aumentar bastante as suas chances de vencer as batalhas.', 'O M\xc3\xa9todo de piadas Toonar permite que voc\xc3\xaa atinja outros Toons na batalha.', 'Os pontos de experi\xc3\xaancia das piadas s\xc3\xa3o dobrados durante uma Invas\xc3\xa3o de Cogs!', 'V\xc3\xa1rios Toons podem se reunir em equipes e usar o mesmo M\xc3\xa9todo de piadas na batalha para conseguir danos extras aos Cogs.', 'Na batalha, as piadas s\xc3\xa3o usadas na ordem de cima para baixo, conforme exibido no Menu de piadas.', 'A fileira de luzes circulares sobre os elevadores do Edif\xc3\xadcio dos Cogs mostram quantos andares haver\xc3\xa1 l\xc3\xa1 dentro.', 'Clique em um Cog para ver mais detalhes.', 'Usar piadas de alto n\xc3\xadvel contra Cogs de baixo n\xc3\xadvel n\xc3\xa3o lhe render\xc3\xa1 nenhum ponto de experi\xc3\xaancia.', 'As piadas que rendem experi\xc3\xaancia possuem um fundo azul no Menu de piadas da batalha.', 'A experi\xc3\xaancia de piadas \xc3\xa9 multiplicada quando usada dentro dos Edif\xc3\xadcios dos Cogs. Os andares mais altos t\xc3\xaam multiplicadores maiores.', 'Quando um Cog \xc3\xa9 derrotado, cada Toon daquela rodada recebe cr\xc3\xa9ditos de Cogs depois que a batalha termina.', 'Cada rua de Toontown possui n\xc3\xadveis e tipos diferentes de Cogs.', 'As cal\xc3\xa7adas s\xc3\xa3o locais seguros, sem Cogs.', 'Nas ruas, as portas laterais contam piadas do tipo toc-toc quando voc\xc3\xaa se aproxima delas.', 'Algumas Tarefas Toon treinam voc\xc3\xaa em novos M\xc3\xa9todos de piadas. Voc\xc3\xaa s\xc3\xb3 pode escolher seis dos sete m\xc3\xa9todos, portanto, escolha direito!', 'As armadilhas s\xc3\xb3 ter\xc3\xa3o utilidade se voc\xc3\xaa ou seus amigos coordenarem o uso de iscas na batalha.', 'As iscas de alto n\xc3\xadvel t\xc3\xaam menos probabilidade de falhar.', 'As piadas de n\xc3\xadvel baixo oferecem menor precis\xc3\xa3o contra os Cogs de alto n\xc3\xadvel.', 'Os Cogs n\xc3\xa3o podem atacar depois que forem "iscados" para a batalha.', 'Quando voc\xc3\xaa e seus amigos dominam um Edif\xc3\xadcio de Cogs, voc\xc3\xaas s\xc3\xa3o recompensados com retratos dentro do Edif\xc3\xadcio dos Toons recuperado.', 'Usar uma piada Toonar em um Toon que possua um Ris\xc3\xb4metro cheio n\xc3\xa3o render\xc3\xa1 nenhuma experi\xc3\xaancia de Toonar.', 'Os Cogs ficar\xc3\xa3o atordoados por uns momentos quando atingidos por alguma. Assim, aumentam as chances de outras piadas da mesma rodada os atingirem.', 'As Piadas cadentes t\xc3\xaam menos chance de atingir algu\xc3\xa9m, mas sua precis\xc3\xa3o aumenta quando os Cogs j\xc3\xa1 tiverem sido atingidos por outra piada na mesma rodada.', 'Quando voc\xc3\xaa j\xc3\xa1 tiver derrotado um n\xc3\xbamero suficiente de Cogs, use o "Radar de Cogs" clicando nos \xc3\xadcones de Cogs da p\xc3\xa1gina Galeria de Cogs do seu \xc3\x81lbum Toon.', 'Durante uma batalha, voc\xc3\xaa tem como saber qual Cog os seus companheiros de equipe est\xc3\xa3o atacando; basta olhar para os travess\xc3\xb5es (-) e para os X.', 'Durante uma batalha, os Cogs carregam uma luz que mostra sua sa\xc3\xbade: o verde significa saud\xc3\xa1vel e o vermelho, quase destru\xc3\xaddo.', 'No m\xc3\xa1ximo, quatro Toons podem guerrear ao mesmo tempo.', 'Na rua, os Cogs t\xc3\xaam mais probabilidade de entrar em uma briga contra v\xc3\xa1rios Toons do que contra apenas um Toon.', 'Os dois tipos de Cogs mais dif\xc3\xadceis de cada tipo s\xc3\xb3 s\xc3\xa3o encontrados nos edif\xc3\xadcios.', 'As Piadas cadentes nunca funcionam contra Cogs iscados.', 'Os Cogs tendem a atacar o Toon que lhes causou danos maiores.', 'As piadas sonoras n\xc3\xa3o rendem danos extras contra Cogs iscados.', 'Se voc\xc3\xaa esperar muito para atacar um Cog iscado, ele acordar\xc3\xa1. As iscas de n\xc3\xadvel mais alto t\xc3\xaam dura\xc3\xa7\xc3\xa3o maior.', 'H\xc3\xa1 lagos de pesca em cada rua de Toontown. Algumas ruas possuem peixes exclusivos.'),
    TIP_MINIGAME: ('Depois que voc\xc3\xaa preenche a sua jarra de balinhas, qualquer balinha que ganhar nos Jogos no bondinho cair\xc3\xa3o direto no seu banco.', 'Voc\xc3\xaa pode usar as teclas de seta em vez de o mouse no Jogo no bondinho "Acompanhe a Minnie".', 'No Jogo do canh\xc3\xa3o, voc\xc3\xaa pode usar as teclas de seta para mover o seu canh\xc3\xa3o e pressionar a tecla "Control" para atirar.', 'No Jogo dos an\xc3\xa9is, voc\xc3\xaa ganha pontos extras quando todo o grupo consegue nadar com sucesso atrav\xc3\xa9s dos an\xc3\xa9is.', 'Um jogo perfeito de Acompanhe a Minnie dobrar\xc3\xa1 seus pontos.', 'No Cabo de guerra, voc\xc3\xaa ganha mais balinhas se jogar contra um Cog forte.', 'A dificuldade dos Jogos no bondinho varia conforme o bairro; os do Centro de Toontown s\xc3\xa3o os mais f\xc3\xa1ceis, e os da Sonhol\xc3\xa2ndia do Donald s\xc3\xa3o os mais dif\xc3\xadceis.', 'Certos Jogos no bondinho s\xc3\xb3 podem ser em grupo.'),
    TIP_COGHQ: ('Voc\xc3\xaa deve completar o seu Disfarce de Rob\xc3\xb4 Vendedor antes de visitar o VP.', 'Voc\xc3\xaa deve completar o seu Disfarce de Rob\xc3\xb4 Mercen\xc3\xa1rio antes de visitar o Diretor Financeiro.', 'Voc\xc3\xaa deve completar o seu Disfarce de Rob\xc3\xb4 da Lei antes de visitar o Juiz-chefe.', 'Voc\xc3\xaa pode pular em cima de cogs Brutamontes para desativ\xc3\xa1-los por um tempo.', 'Ganhe M\xc3\xa9ritos de cogs ao derrotar Rob\xc3\xb4s Vendedores em batalha.', 'Ganhe Cograna ao derrotar Rob\xc3\xb4s Mercen\xc3\xa1rios em batalha.', 'Ganhe Avisos de J\xc3\xbari ao derrotar Rob\xc3\xb4s da Lei em batalha.', 'Voc\xc3\xaa ganha mais M\xc3\xa9ritos, Cogranas ou Avisos de J\xc3\xbari de Cogs de n\xc3\xadvel maior.', 'Quando conseguir juntar M\xc3\xa9ritos o suficiente para merecer uma promo\xc3\xa7\xc3\xa3o, v\xc3\xa1 ver o VP dos Rob\xc3\xb4s Vendedores!', 'Quando conseguir juntar Cogranas o suficiente para merecer uma promo\xc3\xa7\xc3\xa3o, v\xc3\xa1 ver o Diretor Financeiro dos Rob\xc3\xb4s Mercen\xc3\xa1rios!', 'Quando conseguir juntar Avisos de J\xc3\xbari o suficiente para merecer uma promo\xc3\xa7\xc3\xa3o, v\xc3\xa1 ver o Juiz-chefe dos Rob\xc3\xb4s da Lei!', 'Voc\xc3\xaa pode falar como um Cog quando estiver usando o seu Disfarce de Cog.', 'At\xc3\xa9 oito Toons podem lutar juntos contra o VP dos Rob\xc3\xb4s Vendedores', 'At\xc3\xa9 oito Toons podem lutar juntos contra o Diretor Financeiro dos Rob\xc3\xb4s Mercen\xc3\xa1rios', 'At\xc3\xa9 oito Toons podem lutar juntos contra o Juiz-chefe dos Rob\xc3\xb4s da Lei', 'Dentro do Quartel dos Cogs, o caminho \xc3\xa9 subindo as escadas.', 'Cada vez que lutar numa f\xc3\xa1brica do Quartel dos Rob\xc3\xb4s Vendedores, voc\xc3\xaa vai ganhar uma pe\xc3\xa7a do seu Disfarce de Rob\xc3\xb4 Vendedor.', 'Voc\xc3\xaa pode verificar o progresso do seu Disfarce no seu \xc3\x81lbum Toon.', 'Voc\xc3\xaa pode verificar o progresso da sua promo\xc3\xa7\xc3\xa3o na P\xc3\xa1gina de Disfarce do seu \xc3\x81lbum Toon.', 'Certifique-se de estar com as piadas cheias e com o Ris\xc3\xb4metro cheio antes de ir at\xc3\xa9 um Quartel dos Cogs.', 'Quando for promovido, seu disfarce de Cog ser\xc3\xa1 atualizado.', 'Voc\xc3\xaa ter\xc3\xa1 que derrotar o ' + Foreman + ' para recuperar uma pe\xc3\xa7a do Disfarce de Rob\xc3\xb4 Vendedor.', 'Ganhe pe\xc3\xa7as de disfarce de Rob\xc3\xb4 Mercen\xc3\xa1rio como recompensa de Tarefas Toon na Sonhol\xc3\xa2ndia do Donald.', 'Os Rob\xc3\xb4s Mercen\xc3\xa1rios produzem e distribuem o seu pr\xc3\xb3prio dinheiro, as Cogranas, de tr\xc3\xaas maneiras - Moeda, D\xc3\xb3lar e Barra.', 'Espere at\xc3\xa9 que o Diretor Financeiro esteja tonto para lan\xc3\xa7ar um cofre, sen\xc3\xa3o ele vai us\xc3\xa1-lo como capacete! Acerte o capacete com outro cofre para derrub\xc3\xa1-lo.', 'Ganhe pe\xc3\xa7as de disfarce de Rob\xc3\xb4 da Lei como recompensa de Tarefas Toon pelo Professor Floco.', 'Vale a pena a confus\xc3\xa3o: os Cogs virtuais no Quartel dos Rob\xc3\xb4s da Lei n\xc3\xa3o d\xc3\xa3o Avisos de J\xc3\xbari de recompensa.', ' Rob\xc3\xb4 Mercen\xc3\xa1rio produz e distribui a sua pr\xc3\xb3pia moeda, Cogbucks, em tr\xc3\xaas formas diferentes: Moedas, D\xc3\xb3lar, e lingotes.', ' Aguarde at\xc3\xa9 que o Diretor Financeiro fique doido para lan\xc3\xa7ar um seguro ou o utilize-o como um capacete! Acerte no capacete com outro seguro para peg\xc3\xa1-lo.', 'O Rob\xc3\xb4 da Lei obt\xc3\xa9m as partes do traje como recompensa ao concluir a TarefaToon para o Professor Floco.'),
    TIP_ESTATE: ('Os Rabiscos entendem algumas frases do Chat r\xc3\xa1pido. Experimente!', 'Use o menu "Bichinho" do Chat r\xc3\xa1pido para pedir a seu Rabisco que fa\xc3\xa7a truques.', 'Voc\xc3\xaa pode ensinar aos Rabiscos truques com as li\xc3\xa7\xc3\xb5es de treinamento do Gad\xc3\xa1logo da Clarabela.', 'Recompense o seu Rabisco pelos truques.', 'Se voc\xc3\xaa visitar a propriedade de um amigo, o seu Rabisco lhe far\xc3\xa1 companhia.', 'Alimente o seu Rabisco com uma balinha quando ele estiver com fome.', 'Clique em um Rabisco para ver um menu no qual voc\xc3\xaa poder\xc3\xa1 Alimentar, Co\xc3\xa7ar e Cham\xc3\xa1-lo.', 'Os Rabiscos adoram companhia. Convide os amigos para brincar!', 'Todos os Rabiscos possuem personalidades pr\xc3\xb3prias.', 'Voc\xc3\xaa pode devolver o seu Rabisco e adotar outro nas Lojas de Animais.', 'Quando um Rabisco faz um truque, os Toons que o cercam se recuperam.', 'Os Rabiscos ficam ainda melhores nos truques com a pr\xc3\xa1tica. Continue assim!', 'Os truques mais avan\xc3\xa7ados dos Rabiscos recuperam os Toons com mais rapidez.', 'Rabiscos com mais experi\xc3\xaancia podem fazer mais truques sem ficar t\xc3\xa3o cansados.', 'Veja uma lista de Rabiscos pr\xc3\xb3ximos em sua Lista de amigos.', 'Compre m\xc3\xb3veis usando o Gad\xc3\xa1logo da Clarabela e decore a sua casa.', 'O banco da casa tem mais balinhas.', 'O arm\xc3\xa1rio da casa tem mais roupas.', 'V\xc3\xa1 at\xc3\xa9 a casa do seu amigo e experimente as roupas dele.', 'Compre varas de pescar melhores no Gad\xc3\xa1logo da Clarabela.', 'Ligue para a Clarabela usando o telefone da casa.', 'A Clarabela vende um arm\xc3\xa1rio maior em que cabem mais roupas.', 'Reserve espa\xc3\xa7o no seu arm\xc3\xa1rio antes de usar o bilhete de roupas.', 'A Clarabela vende tudo o que \xc3\xa9 preciso para decorar a sua casa.', 'Verifique a sua caixa de correio para ver se h\xc3\xa1 entregas antes de fazer seus pedidos com a Clarabela.', 'As roupas do Gad\xc3\xa1logo da Clarabela levam uma hora para serem entregues.', 'Os pap\xc3\xa9is de parede e pisos do Gad\xc3\xa1logo da Clarabela levam uma hora para serem entregues.', 'Os m\xc3\xb3veis do Gad\xc3\xa1logo da Clarabela levam um dia inteiro para serem entregues.', 'Armazene m\xc3\xb3veis de reserva no s\xc3\xb3t\xc3\xa3o.', 'Voc\xc3\xaa ser\xc3\xa1 avisado pela Clarabela quando um novo Gad\xc3\xa1logo estiver dispon\xc3\xadvel.', 'Voc\xc3\xaa ser\xc3\xa1 avisado pela Clarabela quando uma entrega do Gad\xc3\xa1logo chegar.', 'Novos Gad\xc3\xa1logos s\xc3\xa3o entregues toda semana.', 'Procure os produtos promocionais de estoque limitado no Gad\xc3\xa1logo.', 'Mova os m\xc3\xb3veis indesejados para a lata de lixo.', 'Alguns peixes, como a Cavala Trotante, s\xc3\xa3o mais comuns nas propriedades de Toons.', 'Voc\xc3\xaa pode convidar os seus amigos para a sua propriedade usando o Chat r\xc3\xa1pido.', 'Voc\xc3\xaa sabia que a cor da sua casa combina com a cor do seu painel Pegar um Toon?'),
    TIP_KARTING: ('Compre um Convers\xc3\xadvel, Utilit\xc3\xa1rio Toon ou Cruzeiro na Loja do Kart do Pateta.', 'Personalize o seu kart com decalques, calotas e muito mais na Loja do Kart do Pateta.', 'Ganhe bilhetes correndo de kart no Aut\xc3\xb3dromo do Pateta.', 'Os bilhetes s\xc3\xa3o a \xc3\xbanica moeda aceita na Loja do Kart do Pateta.', 'S\xc3\xa3o necess\xc3\xa1rios bilhetes como dep\xc3\xb3sito antes das corridas.', 'Uma p\xc3\xa1gina especial do seu \xc3\x81lbum Toon permite que voc\xc3\xaa personalize o seu kart.', 'Uma p\xc3\xa1gina especial do seu \xc3\x81lbum Toon permite que voc\xc3\xaa veja os recordes de cada pista.', 'Uma p\xc3\xa1gina especial do seu \xc3\x81lbum Toon permite que voc\xc3\xaa veja seus trof\xc3\xa9us.', 'O Est\xc3\xa1dio dos Nerds \xc3\xa9 a pista mais f\xc3\xa1cil do Aut\xc3\xb3dromo do Pateta.', 'A Pista de Pulos tem o maior n\xc3\xbamero de inclina\xc3\xa7\xc3\xb5es e rampas do Aut\xc3\xb3dromo do Pateta.', 'A Avenida da Neve \xc3\xa9 a pista mais dif\xc3\xadcil do Aut\xc3\xb3dromo do Pateta.'),
    TIP_GOLF: ('Aperte a tecla Tab para ver de cima o percurso de golfe.', 'Aperte a tecla de Seta para Cima para se colocar na dire\xc3\xa7\xc3\xa3o do buraco de golfe.', 'Balan\xc3\xa7ar o taco \xc3\xa9 como atirar uma torta.') }
FishGenusNames = {
    0: 'Baiacu',
    2: 'Peixe-gato',
    4: 'Peixe-palha\xc3\xa7o',
    6: 'Peixe congelado',
    8: 'Estrela-do-mar',
    10: 'Cavala Trotante!',
    12: 'Cachorra',
    14: 'Enguia Amore',
    16: 'Tubar\xc3\xa3o-enfermeira',
    18: 'Caranguejo-rei',
    20: 'Peixe-lua',
    22: 'Cavalo-marinho',
    24: 'Tubar\xc3\xa3o Fera',
    26: 'Barra Cursa',
    28: 'Truta Cicuta',
    30: 'Piano Atum',
    32: 'Manteiga de Amendoim e \xc3\x81gua-viva',
    34: 'Raia Jamanta' }
FishSpeciesNames = {
    0: ('Baiacu', 'Baiacu Bal\xc3\xa3o de Ar', 'Baiacu Bal\xc3\xa3o Meteorol\xc3\xb3gico', 'Baiacu Bal\xc3\xa3o de \xc3\x81gua', 'Baiacu Bal\xc3\xa3o Vermelho'),
    2: ('Peixe-gato', 'Peixe-gato Siam\xc3\xaas', 'Peixe-gato de Rua', 'Peixe-gato Rajado', 'Peixe-gato Tonto'),
    4: ('Peixe-palha\xc3\xa7o', 'Peixe-palha\xc3\xa7o Triste', 'Peixe-palha\xc3\xa7o de Festa', 'Peixe-palha\xc3\xa7o de Circo'),
    6: ('Peixe congelado',),
    8: ('Estrela-do-mar', 'Cinco Estrelas-do-mar', 'Estrela-do-mar do Rock', 'Estrela-do-mar Cintilante', 'Estrela-do-mar All Star'),
    10: ('Cavala Trotante!',),
    12: ('Cachorra', 'Cachorra Buldogue', 'Cachorra-quente', 'Cachorra D\xc3\xa1lmata', 'Cachorrinha'),
    14: ('Enguia Amore', 'Enguia Amore El\xc3\xa9trica'),
    16: ('Tubar\xc3\xa3o-enfermeira', 'Tubar\xc3\xa3o-enfermeira Clara', 'Tubar\xc3\xa3o-enfermeira Flora'),
    18: ('Caranguejo-rei', 'Caranguejo-rei do Alasca', 'Caranguejo-rei Velho'),
    20: ('Peixe-lua', 'Peixe-lua Cheia', 'Peixe Meia-lua', 'Peixe-lua Nova', 'Peixe-lua Crescente', 'Peixe-lua da Colheita'),
    22: ('Cavalo-marinho', 'Cavalo-marinho de Pau', 'Cavalo-marinho Clydesdale', 'Cavalo-marinho \xc3\x81rabe'),
    24: ('Tubar\xc3\xa3o-Fera', 'Tubar\xc3\xa3ozinho Fera', 'Tubar\xc3\xa3o-Fera da Piscina', 'Tubar\xc3\xa3o-Fera da Piscina Ol\xc3\xadmpica'),
    26: ('Barra Cursa Marrom', 'Barra Cursa Preto', 'Barra Cursa Coala', 'Barra Cursa de Mel', 'Barra Cursa Polar', 'Barra Cursa Panda', 'Barra Cursa Kodiac', 'Barra Cursa Grizzly'),
    28: ('Truta', 'Capit\xc3\xa3o Truta Cicuta', 'Truta Cicuta Escorbuta'),
    30: ('Piano Atum', 'Grande Piano Atum', 'Grande Piano Atum Baby', 'Piano Atum Ereto', 'M\xc3\xbasico de Piano Atum'),
    32: ('Manteiga de Amendoim e \xc3\x81gua-viva', 'MA & \xc3\x81gua-viva de Uva', 'MA & \xc3\x81gua-viva Crocante', 'MA & \xc3\x81gua-viva de Morango', 'Concord Grape PB&J Fish'),
    34: ('Raia Jamanta',) }
CogPartNames = ('Perna superior esquerda', 'Perna inferior esquerda', 'P\xc3\xa9 esquerdo', 'Perna superior direita', 'Perna inferior direita', 'P\xc3\xa9 direito', 'Ombro esquerdo', 'Ombro direito', 'Peito', 'Medidor de sa\xc3\xbade', 'Quadril', 'Bra\xc3\xa7o superior esquerdo', 'Bra\xc3\xa7o inferior esquerdo', 'M\xc3\xa3o esquerda', 'Bra\xc3\xa7o superior direito', 'Bra\xc3\xa7o inferior direito', 'M\xc3\xa3o direita')
CogPartNamesSimple = ('Busto superior',)
SellbotLegFactorySpecMainEntrance = 'Entrada principal'
SellbotLegFactorySpecLobby = 'Sal\xc3\xa3o'
SellbotLegFactorySpecLobbyHallway = 'Corredor do sal\xc3\xa3o'
SellbotLegFactorySpecGearRoom = 'Sala de engrenagens'
SellbotLegFactorySpecBoilerRoom = 'Sala da caldeira'
SellbotLegFactorySpecEastCatwalk = 'Passarela leste'
SellbotLegFactorySpecPaintMixer = 'Misturador de tinta'
SellbotLegFactorySpecPaintMixerStorageRoom = 'Dep\xc3\xb3sito do Misturador de tinta'
SellbotLegFactorySpecWestSiloCatwalk = 'Passarela do Silo Oeste'
SellbotLegFactorySpecPipeRoom = 'Sala de tubula\xc3\xa7\xc3\xb5es'
SellbotLegFactorySpecDuctRoom = 'Sala de dutos'
SellbotLegFactorySpecSideEntrance = 'Entrada lateral'
SellbotLegFactorySpecStomperAlley = 'Beco sinistro'
SellbotLegFactorySpecLavaRoomFoyer = 'Antec\xc3\xa2mara do Sal\xc3\xa3o de lava'
SellbotLegFactorySpecLavaRoom = 'Sal\xc3\xa3o de lava'
SellbotLegFactorySpecLavaStorageRoom = 'Dep\xc3\xb3sito de lava'
SellbotLegFactorySpecWestCatwalk = 'Passarela oeste'
SellbotLegFactorySpecOilRoom = 'Sala de \xc3\xb3leo'
SellbotLegFactorySpecLookout = 'Vigil\xc3\xa2ncia'
SellbotLegFactorySpecWarehouse = 'Armaz\xc3\xa9m'
SellbotLegFactorySpecOilRoomHallway = 'Corredor da Sala de \xc3\xb3leo'
SellbotLegFactorySpecEastSiloControlRoom = 'Sala de controle do Silo Leste'
SellbotLegFactorySpecWestSiloControlRoom = 'Sala de controle do Silo Oeste'
SellbotLegFactorySpecCenterSiloControlRoom = 'Sala de controle do Silo Central'
SellbotLegFactorySpecEastSilo = 'Silo Leste'
SellbotLegFactorySpecWestSilo = 'Silo Oeste'
SellbotLegFactorySpecCenterSilo = 'Silo Central'
SellbotLegFactorySpecEastSiloCatwalk = 'Passarela do Silo Leste'
SellbotLegFactorySpecWestElevatorShaft = 'Eixo do Elevador Oeste'
SellbotLegFactorySpecEastElevatorShaft = 'Eixo do Elevador Leste'
FishBingoBingo = 'BINGO!'
FishBingoVictory = 'VIT\xc3\x93RIA!!'
FishBingoJackpot = 'Ganhe %s balinhas!'
FishBingoGameOver = 'FIM DO JOGO'
FishBingoIntermission = 'Intervalo\nTermina em:'
FishBingoNextGame = 'Pr\xc3\xb3ximo jogo\nCome\xc3\xa7a em:'
FishBingoTypeNormal = 'Cl\xc3\xa1ssico'
FishBingoTypeCorners = 'Quatro cantos'
FishBingoTypeDiagonal = 'Diagonais'
FishBingoTypeThreeway = 'Tr\xc3\xaas vias'
FishBingoTypeBlockout = 'BLOQUEADO!'
FishBingoStart = 'Est\xc3\xa1 na hora do Bingo dos Peixes! V\xc3\xa1 para qualquer p\xc3\xader dispon\xc3\xadvel para jogar!'
FishBingoOngoing = 'Bem-vindo! O Bingo dos Peixes j\xc3\xa1 est\xc3\xa1 rolando.'
FishBingoEnd = 'Espero que tenha se divertido no jogo Bingo dos Peixes.'
FishBingoHelpMain = 'Bem-vindo ao Bingo dos Peixes de Toontown! Todo mundo trabalha em conjunto no lago para preencher a cartela antes de acabar o tempo.'
FishBingoHelpFlash = 'Quando voc\xc3\xaa pegar um peixe, clique em um dos quadrados piscantes para marcar a cartela.'
FishBingoHelpNormal = '\xc3\x89 uma cartela de Bingo Cl\xc3\xa1ssico. Para ganhar, complete qualquer linha vertical, horizontal ou na diagonal.'
FishBingoHelpDiagonals = 'Complete as duas diagonais para ganhar.'
FishBingoHelpCorners = 'Uma cartela de Cantos f\xc3\xa1cil. Complete todos os quatro cantos para ganhar.'
FishBingoHelpThreeway = 'Tr\xc3\xaas vias. Complete ambas as diagonais e a linha do meio para ganhar. Esta n\xc3\xa3o \xc3\xa9 f\xc3\xa1cil n\xc3\xa3o!'
FishBingoHelpBingo = ''
FishBingoHelpBlockout = 'Bloqueado! Complete a cartela inteira para ganhar. Voc\xc3\xaa est\xc3\xa1 competindo contra todos os outros lagos e a bolada \xc3\xa9 grande!'
FishBingoOfferToSellFish = 'O seu balde de pesca est\xc3\xa1 cheio. Quer vender os seus peixes?'
FishBingoJackpotWin = 'Ganhe %s balinhas!'
ResistanceToonupMenu = 'Toonar'
ResistanceToonupItem = '%s toonar'
ResistanceToonupItemMax = 'M\xc3\xa1x.'
ResistanceToonupChat = 'Toons de todo o mundo: vamos toonar!'
ResistanceRestockMenu = 'Doar Piadas'
ResistanceRestockItem = 'Doar Piadas %s'
ResistanceRestockItemAll = 'Tudo'
ResistanceRestockChat = 'Toons de todo o mundo: vamos piadar!'
ResistanceMoneyMenu = 'Balinhas'
ResistanceMoneyItem = '%s balinhas'
ResistanceMoneyChat = 'Toons de todo o mundo: gastem com consci\xc3\xaancia!'
ResistanceEmote1 = NPCToonNames[9228] + ': Bem-vindo \xc3\xa0 Resist\xc3\xaancia!'
ResistanceEmote2 = NPCToonNames[9228] + ': Use a sua nova express\xc3\xa3o para se identificar com outros membros.'
ResistanceEmote3 = NPCToonNames[9228] + ': Boa sorte!'
KartUIExit = 'Deixar o kart'
KartShop_Cancel = lCancel
KartShop_BuyKart = 'Comprar kart'
KartShop_BuyAccessories = 'Comprar acess\xc3\xb3rios'
KartShop_BuyAccessory = 'Comprar acess\xc3\xb3rio'
KartShop_Cost = 'Custo: %d bilhetes'
KartShop_ConfirmBuy = 'Comprar %s por %d bilhetes?'
KartShop_NoAvailableAcc = 'N\xc3\xa3o h\xc3\xa1 acess\xc3\xb3rios deste tipo'
KartShop_FullTrunk = 'A mala est\xc3\xa1 cheia.'
KartShop_ConfirmReturnKart = 'Tem certeza de que quer devolver o seu kart atual?'
KartShop_ConfirmBoughtTitle = 'Parab\xc3\xa9ns!'
KartShop_NotEnoughTickets = 'N\xc3\xa3o h\xc3\xa1 bilhetes suficientes!'
KartView_Rotate = 'Girar'
KartView_Right = 'Direita'
KartView_Left = 'Esquerda'
StartingBlock_NotEnoughTickets = 'Voc\xc3\xaa n\xc3\xa3o tem bilhetes suficientes! Experimente participar de um treino.'
StartingBlock_NoBoard = 'O embarque para esta corrida terminou. Espere o in\xc3\xadcio da pr\xc3\xb3xima corrida.'
StartingBlock_NoKart = 'Primeiramente, voc\xc3\xaa precisa de um kart! Por que voc\xc3\xaa n\xc3\xa3o pergunta a um dos funcion\xc3\xa1rios da Loja do kart?'
StartingBlock_Occupied = 'Este bloco j\xc3\xa1 est\xc3\xa1 ocupado! Procure outro ponto.'
StartingBlock_TrackClosed = 'Desculpe, esta pista est\xc3\xa1 fechada para reformas.'
StartingBlock_EnterPractice = 'Deseja participar do treino?'
StartingBlock_EnterNonPractice = 'Deseja participar de uma corrida %s por %s bilhetes?'
StartingBlock_EnterShowPad = 'Deseja estacionar o seu carro aqui?'
StartingBlock_KickSoloRacer = 'As corridas Batalha dos Toons e Grande Pr\xc3\xaamio requerem dois ou mais participantes.'
StartingBlock_Loading = 'Indo para a corrida!'
LeaderBoard_Time = 'Tempo'
LeaderBoard_Name = 'Nome do piloto'
LeaderBoard_Daily = 'Pontua\xc3\xa7\xc3\xa3o di\xc3\xa1ria'
LeaderBoard_Weekly = 'Pontua\xc3\xa7\xc3\xa3o semanal'
LeaderBoard_AllTime = 'Melhor pontua\xc3\xa7\xc3\xa3o de todos os tempos'
RecordPeriodStrings = [
    LeaderBoard_Daily,
    LeaderBoard_Weekly,
    LeaderBoard_AllTime]
KartRace_RaceNames = [
    'Treino',
    'Batalha dos Toons',
    'Torneio']
from toontown.racing import RaceGlobals
KartRace_Go = 'Largar!'
KartRace_Reverse = ' Rev'
KartRace_TrackNames = {
    RaceGlobals.RT_Speedway_1: 'Est\xc3\xa1dio dos Nerds',
    RaceGlobals.RT_Speedway_1_rev: 'Est\xc3\xa1dio dos Nerds' + KartRace_Reverse,
    RaceGlobals.RT_Rural_1: 'Aut\xc3\xb3dromo R\xc3\xbastico',
    RaceGlobals.RT_Rural_1_rev: 'Aut\xc3\xb3dromo R\xc3\xbastico' + KartRace_Reverse,
    RaceGlobals.RT_Urban_1: 'Circuito da Cidade',
    RaceGlobals.RT_Urban_1_rev: 'Circuito da Cidade' + KartRace_Reverse,
    RaceGlobals.RT_Speedway_2: 'Coliseu Saca-Rolhas',
    RaceGlobals.RT_Speedway_2_rev: 'Coliseu Saca-Rolhas' + KartRace_Reverse,
    RaceGlobals.RT_Rural_2: 'Pista de Pulos',
    RaceGlobals.RT_Rural_2_rev: 'Pista de Pulos' + KartRace_Reverse,
    RaceGlobals.RT_Urban_2: 'Avenida da Neve',
    RaceGlobals.RT_Urban_2_rev: 'Avenida da Neve' + KartRace_Reverse }
KartRace_Unraced = 'N/D'
KartDNA_KartNames = {
    0: 'Cruzeiro',
    1: 'Convers\xc3\xadvel',
    2: 'Utilit\xc3\xa1rio Toon' }
KartDNA_AccNames = {
    1000: 'Filtro de ar',
    1001: 'Carburador qu\xc3\xa1druplo',
    1002: '\xc3\x81guia',
    1003: 'Chifres',
    1004: 'Seis cilindros',
    1005: 'Aerof\xc3\xb3lio pequeno',
    1006: 'V\xc3\xa1lvulas simples',
    1007: 'Aerof\xc3\xb3lio m\xc3\xa9dio',
    1008: 'Carburador simples',
    1009: 'Corneta',
    1010: 'Aerof\xc3\xb3lio sim\xc3\xa9trico',
    2000: 'Asa',
    2001: 'Pe\xc3\xa7a recondicionada',
    2002: 'Gaiola',
    2003: 'Aleta',
    2004: 'Asa dupla',
    2005: 'Asa simples',
    2006: 'Pe\xc3\xa7a sobressalente padr\xc3\xa3o',
    2007: 'Aleta',
    2008: 'ps9',
    2009: 'ps10',
    3000: 'Buzina dupla',
    3001: 'Para-choques do Joe',
    3002: 'Estribos de cobalto',
    3003: 'Descarga lateral cobra',
    3004: 'Descarga lateral reta',
    3005: 'Para-choques vazados',
    3006: 'Estribos de carbono',
    3007: 'Estribos de madeira',
    3008: 'fw9',
    3009: 'fw10',
    4000: 'Canos de descarga traseiros curvos',
    4001: 'Para-lamas',
    4002: 'Escapamento duplo',
    4003: 'Aletas duplas lisas',
    4004: 'Para-lamas lisos',
    4005: 'Escapamento quadrado',
    4006: 'Acabamento duplo',
    4007: 'Megaescapamento',
    4008: 'Aletas duplas sim\xc3\xa9tricas',
    4009: 'Aletas duplas redondas',
    4010: 'Para-lamas sim\xc3\xa9tricos',
    4011: 'Para-lamas do Mickey',
    4012: 'Para-lamas vazados',
    5000: 'Turbo',
    5001: 'Lua',
    5002: 'Emendado',
    5003: 'Tr\xc3\xaas raios',
    5004: 'Pintura da tampa',
    5005: 'Cora\xc3\xa7\xc3\xa3o',
    5006: 'Mickey',
    5007: 'Cinco raios',
    5008: 'Margarida',
    5009: 'Basquete',
    5010: 'Hipn\xc3\xb3tico',
    5011: 'Tribal',
    5012: 'Diamante',
    5013: 'Cinco raios',
    5014: 'Roda',
    6000: 'N\xc3\xbamero cinco',
    6001: 'Respingo',
    6002: 'Quadriculado',
    6003: 'Chamas',
    6004: 'Cora\xc3\xa7\xc3\xb5es',
    6005: 'Bolhas',
    6006: 'Tigre',
    6007: 'Flores',
    6008: 'Raio',
    6009: 'Anjo',
    7000: 'Verde-lim\xc3\xa3o',
    7001: 'P\xc3\xaassego',
    7002: 'Vermelho vivo',
    7003: 'Vermelho',
    7004: 'Castanho',
    7005: 'Siena',
    7006: 'Marrom',
    7007: 'Canela',
    7008: 'Coral',
    7009: 'Laranja',
    7010: 'Amarelo',
    7011: 'Creme',
    7012: 'C\xc3\xadtrico',
    7013: 'Lim\xc3\xa3o',
    7014: 'Verde-\xc3\xa1gua',
    7015: 'Verde',
    7016: 'Azul-claro',
    7017: 'Verde-azulado',
    7018: 'Azul',
    7019: 'Verde-musgo',
    7020: 'Azul-turquesa',
    7021: 'Azul-cinzento',
    7022: 'Lil\xc3\xa1s',
    7023: 'P\xc3\xbarpura',
    7024: 'Rosa',
    7025: 'Ameixa',
    7026: 'Preto' }
RaceHoodSpeedway = 'Aut\xc3\xb3dromo'
RaceHoodRural = 'Rural'
RaceHoodUrban = 'Urbano'
RaceTypeCircuit = 'Torneio'
RaceQualified = 'classificado'
RaceSwept = 'varrido'
RaceWon = 'venceu'
Race = 'corrida'
Races = 'corridas'
Total = 'total'
GrandTouring = 'Gran Turismo'

def getTrackGenreString(genreId):
    genreStrings = [
        'Aut\xc3\xb3dromo',
        'Pa\xc3\xads',
        'Cidade']
    return genreStrings[genreId].lower()


def getTunnelSignName(trackId, padId):
    if trackId == 2 and padId == 0:
        return 'tunne1l_citysign'
    elif trackId == 1 and padId == 0:
        return 'tunnel_countrysign1'
    else:
        genreId = RaceGlobals.getTrackGenre(trackId)
        return 'tunnel%s_%ssign' % (padId + 1, RaceGlobals.getTrackGenreString(genreId))

KartTrophyDescriptions = [
    RaceHoodSpeedway + ' ' + str(RaceGlobals.QualifiedRaces[0]) + ' ' + Race + ' ' + RaceQualified,
    RaceHoodSpeedway + ' ' + str(RaceGlobals.QualifiedRaces[1]) + ' ' + Races + ' ' + RaceQualified,
    RaceHoodSpeedway + ' ' + str(RaceGlobals.QualifiedRaces[2]) + ' ' + Races + ' ' + RaceQualified,
    RaceHoodRural + ' ' + str(RaceGlobals.QualifiedRaces[0]) + ' ' + Race + ' ' + RaceQualified,
    RaceHoodRural + ' ' + str(RaceGlobals.QualifiedRaces[1]) + ' ' + Races + ' ' + RaceQualified,
    RaceHoodRural + ' ' + str(RaceGlobals.QualifiedRaces[2]) + ' ' + Races + ' ' + RaceQualified,
    RaceHoodUrban + ' ' + str(RaceGlobals.QualifiedRaces[0]) + ' ' + Race + ' ' + RaceQualified,
    RaceHoodUrban + ' ' + str(RaceGlobals.QualifiedRaces[1]) + ' ' + Races + ' ' + RaceQualified,
    RaceHoodUrban + ' ' + str(RaceGlobals.QualifiedRaces[2]) + ' ' + Races + ' ' + RaceQualified,
    str(RaceGlobals.TotalQualifiedRaces) + ' ' + Total + ' ' + Races + ' ' + RaceQualified,
    RaceHoodSpeedway + ' ' + str(RaceGlobals.WonRaces[0]) + ' ' + Race + ' ' + RaceWon,
    RaceHoodSpeedway + ' ' + str(RaceGlobals.WonRaces[1]) + ' ' + Races + ' ' + RaceWon,
    RaceHoodSpeedway + ' ' + str(RaceGlobals.WonRaces[2]) + ' ' + Races + ' ' + RaceWon,
    RaceHoodSpeedway + ' ' + str(RaceGlobals.WonRaces[0]) + ' ' + Race + ' ' + RaceWon,
    RaceHoodRural + ' ' + str(RaceGlobals.WonRaces[1]) + ' ' + Races + ' ' + RaceWon,
    RaceHoodRural + ' ' + str(RaceGlobals.WonRaces[2]) + ' ' + Races + ' ' + RaceWon,
    RaceHoodUrban + ' ' + str(RaceGlobals.WonRaces[0]) + ' ' + Race + ' ' + RaceWon,
    RaceHoodUrban + ' ' + str(RaceGlobals.WonRaces[1]) + ' ' + Races + ' ' + RaceWon,
    RaceHoodUrban + ' ' + str(RaceGlobals.WonRaces[2]) + ' ' + Races + ' ' + RaceWon,
    str(RaceGlobals.TotalWonRaces) + ' ' + Total + ' ' + Races + ' ' + RaceWon,
    str(RaceGlobals.WonCircuitRaces[0]) + ' ' + RaceTypeCircuit + ' ' + Race + ' ' + RaceQualified,
    str(RaceGlobals.WonCircuitRaces[1]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceQualified,
    str(RaceGlobals.WonCircuitRaces[2]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceQualified,
    str(RaceGlobals.WonCircuitRaces[0]) + ' ' + RaceTypeCircuit + ' ' + Race + ' ' + RaceWon,
    str(RaceGlobals.WonCircuitRaces[1]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceWon,
    str(RaceGlobals.WonCircuitRaces[2]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceWon,
    str(RaceGlobals.SweptCircuitRaces[0]) + ' ' + RaceTypeCircuit + ' ' + Race + ' ' + RaceSwept,
    str(RaceGlobals.SweptCircuitRaces[1]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceSwept,
    str(RaceGlobals.SweptCircuitRaces[2]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceSwept,
    GrandTouring,
    str(RaceGlobals.TrophiesPerCup) + ' Trof\xc3\xa9us de corrida de kart recebidos! Mais acr\xc3\xa9scimo de pontos de risada!',
    str(RaceGlobals.TrophiesPerCup * 2) + ' Trof\xc3\xa9us de corrida de kart recebidos! Mais acr\xc3\xa9scimo de pontos de risada!',
    str(RaceGlobals.TrophiesPerCup * 3) + ' Trof\xc3\xa9us de corrida de kart recebidos! Mais acr\xc3\xa9scimo de pontos de risada!']
KartRace_TitleInfo = 'Preparar para a corrida'
KartRace_SSInfo = 'Bem-vindo ao Est\xc3\xa1dio dos Nerds!\nP\xc3\xa9 na t\xc3\xa1bua e segure firme!'
KartRace_CoCoInfo = 'Bem-vindo ao Coliseu Saca-Rolhas!\nUse as curvas inclinadas para manter a velocidade!\n'
KartRace_RRInfo = 'Bem-vindo ao Aut\xc3\xb3dromo R\xc3\xbastico!\nPreserve os animais e permane\xc3\xa7a na pista!\n'
KartRace_AAInfo = 'Bem-vindo \xc3\xa0 Pista de Pulos!\nSegure firme! O caminho parece acidentado...\n'
KartRace_CCInfo = 'Bem-vindo ao Circuito da Cidade!\nCuidado com os pedestres quando passar pelo centro da cidade!\n'
KartRace_BBInfo = 'Bem-vindo \xc3\xa0 Avenida da Neve!\nCuidado com a velocidade. Pode ter gelo na pista.\n'
KartRace_GeneralInfo = 'Use Ctrl para lan\xc3\xa7ar as piadas que pegar na pista, e as teclas de setas, para controlar o kart.'
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
    RaceGlobals.RT_Urban_2_rev: KartRace_BBInfo + KartRace_GeneralInfo }
KartRecordStrings = {
    RaceGlobals.Daily: 'diariamente',
    RaceGlobals.Weekly: 'semanalmente',
    RaceGlobals.AllTime: 'o tempo todo' }
KartRace_FirstSuffix = 'o'
KartRace_SecondSuffix = ' o'
KartRace_ThirdSuffix = ' o'
KartRace_FourthSuffix = ' o'
KartRace_WrongWay = 'Dire\xc3\xa7\xc3\xa3o\nerrada!'
KartRace_LapText = 'Volta %s'
KartRace_FinalLapText = 'Volta final!'
KartRace_Exit = 'Sair da corrida'
KartRace_NextRace = 'Pr\xc3\xb3xima Corrida'
KartRace_Leave = 'Deixar a corrida'
KartRace_Qualified = 'Classificado!'
KartRace_Record = 'Recorde!'
KartRace_RecordString = 'Voc\xc3\xaa bateu um novo recorde %s para %s! Seu b\xc3\xb4nus \xc3\xa9 %s bilhetes.'
KartRace_Tickets = 'Bilhetes'
KartRace_Exclamations = '!'
KartRace_Deposit = 'Dep\xc3\xb3sito'
KartRace_Winnings = 'Vit\xc3\xb3rias'
KartRace_Bonus = 'B\xc3\xb4nus'
KartRace_RaceTotal = 'Total da corrida'
KartRace_CircuitTotal = 'Total do Circuito'
KartRace_Trophies = 'Trof\xc3\xa9us'
KartRace_Zero = '0'
KartRace_Colon = ':'
KartRace_TicketPhrase = '%s' + KartRace_Tickets
KartRace_DepositPhrase = KartRace_Deposit + KartRace_Colon + '\n' + KartRace_Tickets
KartRace_QualifyPhrase = 'Classificar:\n'
KartRace_RaceTimeout = 'Tempo esgotado nesta corrida. Seus bilhetes foram reembolsados. Continue tentando!'
KartRace_RaceTimeoutNoRefund = 'O tempo da corrida esgotou.  Seus bilhetes n\xc3\xa3o foram reembolsados porque o Grande Pr\xc3\xaamio j\xc3\xa1 come\xc3\xa7ou.  Continue tentando!'
KartRace_RacerTooSlow = 'Voc\xc3\xaa demorou demais para terminar a corrida.  Seus bilhetes n\xc3\xa3o foram reembolsados.  Continue tentando!'
KartRace_PhotoFinish = 'Foto da chegada!'
KartRace_CircuitPoints = 'Pontos do Circuito'
CircuitRaceStart = 'O Grande Pr\xc3\xaamio de Toontown est\xc3\xa1 prestes a come\xc3\xa7ar!  Para vencer, ganhe o maior n\xc3\xbamero de pontos em tr\xc3\xaas corridas consecutivas!'
CircuitRaceOngoing = 'Ol\xc3\xa1! O Grande Pr\xc3\xaamio de Toontown est\xc3\xa1 acontecendo agora.'
CircuitRaceEnd = 'E por hoje \xc3\xa9 s\xc3\xb3 do Grande Pr\xc3\xaamio de Toontown no Aut\xc3\xb3dromo do Pateta.  Vejo voc\xc3\xaa na pr\xc3\xb3xima segunda-feira!'
TrickOrTreatMsg = 'Voc\xc3\xaa j\xc3\xa1 encontrou\nesta gostosura!'
WinterCarolingMsg = 'Voc\xc3\xaa j\xc3\xa1 cantou aqui!'
LawbotBossTempIntro0 = 'Humm, o que temos na pauta de casos hoje?'
LawbotBossTempIntro1 = 'Arr\xc3\xa1, temos o julgamento de um Toon!'
LawbotBossTempIntro2 = 'O caso da promotoria \xc3\xa9 forte.'
LawbotBossTempIntro3 = 'E aqui est\xc3\xa3o os defensores p\xc3\xbablicos.'
LawbotBossTempIntro4 = 'Espere um pouco... Voc\xc3\xaas s\xc3\xa3o Toons!'
LawbotBossTempJury1 = 'A sele\xc3\xa7\xc3\xa3o do j\xc3\xbari vai come\xc3\xa7ar agora.'
LawbotBossHowToGetEvidence = 'Toque na tribuna da testemunha para pegar a evid\xc3\xaancia.'
LawbotBossTrialChat1 = 'A sess\xc3\xa3o da Corte est\xc3\xa1 aberta'
LawbotBossHowToThrowPies = 'Aperte a tecla Insert para arremessar a evid\xc3\xaancia\n nos advogados ou na balan\xc3\xa7a!'
LawbotBossNeedMoreEvidence = 'Voc\xc3\xaa precisa de mais evid\xc3\xaancias!'
LawbotBossDefenseWins1 = 'Imposs\xc3\xadvel! A defesa venceu?'
LawbotBossDefenseWins2 = 'N\xc3\xa3o. Eu declaro este julgamento nulo! Um novo julgamento ser\xc3\xa1 agendado.'
LawbotBossDefenseWins3 = 'Humpf. Estarei na minha sala.'
LawbotBossProsecutionWins = 'Eu julgo em favor do querelante'
LawbotBossReward = 'O pr\xc3\xaamio \xc3\xa9 uma promo\xc3\xa7\xc3\xa3o e a habilidade de evocar Cogs'
LawbotBossLeaveCannon = 'Deixar canh\xc3\xa3o'
LawbotBossPassExam = 'Bah, e da\xc3\xad que voc\xc3\xaa passou no exame da ordem dos advogados?'
LawbotBossTaunts = [
    '%s, eu julgo voc\xc3\xaa em desacato desta corte!',
    'Obje\xc3\xa7\xc3\xa3o aceita!',
    'Apague isso dos registros.',
    'Sua apela\xc3\xa7\xc3\xa3o foi rejeitada. A sua senten\xc3\xa7a \xc3\xa9 a tristeza!',
    'Ordem na corte!']
LawbotBossAreaAttackTaunt = 'Voc\xc3\xaas todos est\xc3\xa3o em desacato da corte!'
WitnessToonName = 'Abel Abelhudo'
WitnessToonPrepareBattleTwo = 'Oh, n\xc3\xa3o! Eles est\xc3\xa3o colocando apenas Cogs no j\xc3\xbari!\x7R\xc3\xa1pido, use os canh\xc3\xb5es e atire alguns jurados Toons nas cadeiras do j\xc3\xbari.\x7Precisamos de %d para ter uma balan\xc3\xa7a justa.'
WitnessToonNoJuror = 'Oh-oh, sem jurados Toons. Vai ser um julgamento dif\xc3\xadcil.'
WitnessToonOneJuror = 'Legal! Tem 1 Toon no j\xc3\xbari!'
WitnessToonSomeJurors = 'Legal! Tem %d Toons no j\xc3\xbari!'
WitnessToonAllJurors = 'Irado! Todos os jurados s\xc3\xa3o Toons!'
WitnessToonPrepareBattleThree = 'R\xc3\xa1pido, toque na tribuna da testemunha para pegar evid\xc3\xaancias.\x7Aperte a tecla Insert para arremessar a evid\xc3\xaancia nos advogados, ou no prato da defesa.'
WitnessToonCongratulations = 'Voc\xc3\xaa conseguiu!  Obrigado por uma defesa espetacular!\x7Aqui ,fique com estes pap\xc3\xa9is deixados pelo Juiz-chefe.\x7Com isto voc\xc3\xaa ser\xc3\xa1 capaz de evocar Cogs da sua p\xc3\xa1gina Galeria de Cogs.'
WitnessToonLastPromotion = '\x7Uau, voc\xc3\xaa atingiu o n\xc3\xadvel %s do seu Disfarce de Cog!\x7Os Cogs n\xc3\xa3o s\xc3\xa3o promovidos mais que isso.\x7Voc\xc3\xaa n\xc3\xa3o pode mais atualizar o seu Disfarce de Cog, mas ainda pode continuar trabalhando pela Resist\xc3\xaancia!'
WitnessToonHPBoost = '\x7Voc\xc3\xaa fez muito pela Resist\xc3\xaancia.\x7O Conselho de Toons decidiu lhe dar mais um ponto de Risada. Parab\xc3\xa9ns!'
WitnessToonMaxed = '\x7Vejo que tem um Disfarce de Cog n\xc3\xadvel %s. Impressionante!\x7Em nome de todo o Conselho de Toons, obrigado por voltar para defender mais Toons!'
WitnessToonBonus = 'Maravilhoso! Todos os advogados est\xc3\xa3o atordoados. O peso da sua evid\xc3\xaancia foi %s vezes mais denso por %s segundos'
WitnessToonJuryWeightBonusSingular = {
    6: 'Este caso \xc3\xa9 dif\xc3\xadcil. Voc\xc3\xaa sentou %d jurado Toon, ent\xc3\xa3o a sua evid\xc3\xaancia tem um peso-b\xc3\xb4nus de %d.',
    7: 'Este caso \xc3\xa9 muito dif\xc3\xadcil. Voc\xc3\xaa sentou %d jurado Toon, ent\xc3\xa3o a sua evid\xc3\xaancia tem um peso-b\xc3\xb4nus de %d.',
    8: 'Este caso \xc3\xa9 o mais dif\xc3\xadcil. Voc\xc3\xaa sentou %d jurado Toon, ent\xc3\xa3o a sua evid\xc3\xaancia tem um peso-b\xc3\xb4nus de %d.' }
WitnessToonJuryWeightBonusPlural = {
    6: 'Este caso \xc3\xa9 dif\xc3\xadcil. Voc\xc3\xaa sentou %d jurados Toon, ent\xc3\xa3o a sua evid\xc3\xaancia tem um peso-b\xc3\xb4nus de %d.',
    7: 'Este caso \xc3\xa9 muito dif\xc3\xadcil. Voc\xc3\xaa sentou %d jurados Toon, ent\xc3\xa3o a sua evid\xc3\xaancia tem um peso-b\xc3\xb4nus de %d.',
    8: 'Este caso \xc3\xa9 o mais dif\xc3\xadcil. Voc\xc3\xaa sentou %d jurados Toon, ent\xc3\xa3o a sua evid\xc3\xaancia tem um peso-b\xc3\xb4nus de %d.' }
IssueSummons = 'Evocar'
SummonDlgTitle = 'Evocar um Cog'
SummonDlgButton1 = 'Evocar um Cog'
SummonDlgButton2 = 'Evocar um Pr\xc3\xa9dio Cog'
SummonDlgButton3 = 'Evocar uma Invas\xc3\xa3o Cog'
SummonDlgSingleConf = 'Gostaria de evocar um %s?'
SummonDlgBuildingConf = 'Gostaria de evocar um %s para um pr\xc3\xa9dio Toon pr\xc3\xb3ximo?'
SummonDlgInvasionConf = 'Gostaria de evocar uma invas\xc3\xa3o de %s?'
SummonDlgNumLeft = 'Voc\xc3\xaa tem %s sobrando.'
SummonDlgDelivering = 'Evocando...'
SummonDlgSingleSuccess = 'Voc\xc3\xaa evocou o Cog com sucesso.'
SummonDlgSingleBadLoc = 'Desculpe, mas cogs s\xc3\xa3o proibidos aqui.  Tente em outro lugar.'
SummonDlgBldgSuccess = 'Voc\xc3\xaa evocou os Cogs com sucesso. %s concordou em deix\xc3\xa1-los tomar %s por um tempo!'
SummonDlgBldgSuccess2 = 'Voc\xc3\xaa evocou os Cogs com sucesso. Um Dono de Loja concordou em deix\xc3\xa1-los tomar o pr\xc3\xa9dio dele por um tempo!'
SummonDlgBldgBadLoc = 'Desculpe, n\xc3\xa3o h\xc3\xa1 pr\xc3\xa9dios Toon por perto para os Cogs tomarem.'
SummonDlgInvasionSuccess = 'Voc\xc3\xaa evocou os Cogs com sucesso. \xc3\x89 uma invas\xc3\xa3o!'
SummonDlgInvasionBusy = 'Um %s n\xc3\xa3o p\xc3\xb4de ser encontrado.  Tente novamente quando a invas\xc3\xa3o dos Cogs terminar.'
SummonDlgInvasionFail = 'Desculpe, a invas\xc3\xa3o dos Cogs fracassou.'
SummonDlgShopkeeper = 'O Dono da Loja '
PolarPlaceEffect1 = NPCToonNames[3306] + ': Bem-vindo ao Lugar Polar!'
PolarPlaceEffect2 = NPCToonNames[3306] + ': Tente isto.'
PolarPlaceEffect3 = NPCToonNames[3306] + ': A sua nova apar\xc3\xaancia s\xc3\xb3 vai funcionar em ' + lTheBrrrgh + '.'
LaserGameMine = 'Ca\xc3\xa7a-Caveiras!'
LaserGameRoll = 'Combinando'
LaserGameAvoid = 'Evite as Caveiras'
LaserGameDrag = 'Arraste tr\xc3\xaas da mesma cor em uma fileira'
LaserGameDefault = 'Jogo Desconhecido'
PinballHiScore = 'Maior Pontua\xc3\xa7\xc3\xa3o: %s\n'
PinballHiScoreAbbrev = '...'
PinballYourBestScore = 'Sua Melhor Pontua\xc3\xa7\xc3\xa3o:\n'
PinballScore = 'Pontua\xc3\xa7\xc3\xa3o:        %d x %d = '
PinballScoreHolder = '%s\n'
GagTreeFeather = '\xc3\x81rvore de Piada de Pena'
GagTreeJugglingBalls = '\xc3\x81rvore de Piada de Bolinhas de Malabarismo'
StatuaryFountain = 'Fonte'
StatuaryToonStatue = 'Est\xc3\xa1tua de Toon'
StatuaryDonald = 'Est\xc3\xa1tua do Donald'
StatuaryMinnie = 'Est\xc3\xa1tua da Minnie'
StatuaryMickey1 = 'Est\xc3\xa1tua do Mickey'
StatuaryMickey2 = 'Fonte do Mickey'
StatuaryToon = 'Est\xc3\xa1tua de Toon'
StatuaryToonWave = 'Est\xc3\xa1tua da Onda Toon'
StatuaryToonVictory = 'Est\xc3\xa1tua da Vit\xc3\xb3ria Toon'
StatuaryToonCrossedArms = 'Est\xc3\xa1tua da Autoridade Toon'
StatuaryToonThinking = 'Est\xc3\xa1tua do Abra\xc3\xa7o Toon'
StatuaryMeltingSnowman = ' Boneco de neve Derretendo'
StatuaryMeltingSnowDoodle = 'Est\xc3\xa1tua de Doodle de neve'
StatuaryGardenAccelerator = 'Fertilizante Instant\xc3\xa2neo'
AnimatedStatuaryFlappyCog = 'Cog Suspenso'
FlowerColorStrings = [
    'Vermelha',
    'Laranja',
    'Violeta',
    'Azul',
    'Rosa',
    'Amarela',
    'Branca',
    'Verde']
FlowerSpeciesNames = {
    49: 'Margarida',
    50: 'Tulipa',
    51: 'Cravo',
    52: 'L\xc3\xadrio',
    53: 'Narciso',
    54: 'Til\xc3\xa1pia',
    55: 'Pet\xc3\xbania',
    56: 'Rosa' }
FlowerFunnyNames = {
    49: ('Margarida Lida', 'Margarida Sumida', 'Margarida Querida', 'Margarida Lambida', 'Margarida Ca\xc3\xadda', 'Margarida Subida', 'Margarida Enlouquecida', 'Margarida Esclarecida'),
    50: ('Eulipa', 'Tulipas', 'Elelipa'),
    51: ('Encravou', 'Cravado', 'Cravo H\xc3\xadbrido', 'Cravo de Lado', 'Cravo Modelo'),
    52: ('De L\xc3\xadrio', 'Co L\xc3\xadrio', 'L\xc3\xadrio Selvagem', 'L\xc3\xadrio Figueiro', 'L\xc3\xadrio Pimenta', 'L\xc3\xadrio Bobo', 'Ecl\xc3\xadrio', 'L\xc3\xadrio D\xc3\xadlio'),
    53: ('Nar-sorriso', 'Nariz Ciso', 'Narcisudo', 'Ante Narciso'),
    54: ('Til\xc3\xa1pia Pudo', 'Ene-A-O-Til\xc3\xa1pia', 'Tilapiano', 'Tilapiada', 'Til\xc3\xa1pia S\xc3\xa1bia'),
    55: ('Car Pet\xc3\xbania', 'Plat\xc3\xbania'),
    56: ('\xc3\x9altima Rosa do Ver\xc3\xa3o', 'Choque de Rosa', 'Rosa Tinta', 'Rosa Fedida', 'Rosa Aindarrosa') }
FlowerVarietyNameFormat = '%s %s'
FlowerUnknown = '????'
FloweringNewEntry = 'Nova Entrada'
ShovelNameDict = {
    0: 'Lat\xc3\xa3o',
    1: 'Bronze',
    2: 'Prata',
    3: 'Ouro' }
WateringCanNameDict = {
    0: 'Pequeno',
    1: 'M\xc3\xa9dio',
    2: 'Grande',
    3: 'Enorme' }
GardeningPlant = 'Plantar'
GardeningWater = 'Regar'
GardeningRemove = 'Remover'
GardeningPick = 'Colher'
GardeningFull = 'Encher'
GardeningSkill = 'Habilidade'
GardeningWaterSkill = 'Habilidade na \xc3\x81gua'
GardeningShovelSkill = 'Habilidade com a P\xc3\xa1'
GardeningNoSkill = 'Nenhuma Habilidade'
GardeningPlantFlower = 'Plantar\nFlor'
GardeningPlantTree = 'Plantar\n\xc3\x81rvore'
GardeningPlantItem = 'Plantar\nItem'
PlantingGuiOk = 'Plantar'
PlantingGuiCancel = lCancel
PlantingGuiReset = 'Restaurar'
GardeningChooseBeans = 'Escolha as balinhas que deseja plantar.'
GardeningChooseBeansItem = 'Escolha as balinhas / item que deseja plantar.'
GardeningChooseToonStatue = 'Escolha o Toon do qual deseja criar uma est\xc3\xa1tua.'
GardenShovelLevelUp = 'Parab\xc3\xa9ns, voc\xc3\xaa ganhou uma nova p\xc3\xa1!'
GardenShovelSkillLevelUp = 'Parab\xc3\xa9ns! Voc\xc3\xaa atingiu %(oldbeans)d violetas! Para progredir, voc\xc3\xaa deve coletar %(newbeans)d violetas.'
GardenShovelSkillMaxed = 'Incr\xc3\xadvel! Voc\xc3\xaa superou sua habilidade com a p\xc3\xa1!'
GardenWateringCanLevelUp = 'Parab\xc3\xa9ns, voc\xc3\xaa ganhou um novo regador!'
GardenMiniGameWon = 'Parab\xc3\xa9ns, voc\xc3\xaa regou a planta!'
ShovelTin = 'P\xc3\xa1 de Lat\xc3\xa3o'
ShovelSteel = 'P\xc3\xa1 de A\xc3\xa7o'
ShovelSilver = 'P\xc3\xa1 de Prata'
ShovelGold = 'P\xc3\xa1 de Ouro'
WateringCanSmall = 'Regador Pequeno'
WateringCanMedium = 'Regador M\xc3\xa9dio'
WateringCanLarge = 'Regador Grande'
WateringCanHuge = 'Regador Enorme'
BeanColorWords = ('vermelha', 'verde', 'laranja', 'lil\xc3\xa1s', 'azul', 'rosa', 'amarela', 'ciano', 'prata')
PlantItWith = ' Plante com %s.'
MakeSureWatered = ' Primeiramente, certifique-se de que todas as plantas foram regadas.'
UseFromSpecialsTab = 'Use por meio da guia de especiais na p\xc3\xa1gina do jardim.'
UseSpecial = 'Usar Especial'
UseSpecialBadLocation = 'Voc\xc3\xaa s\xc3\xb3 pode usar isso no seu jardim.'
UseSpecialSuccess = 'Sucesso! Suas plantas regadas acabaram de crescer.'
ConfirmWiltedFlower = '%(plant)s murchou.  Tem certeza de que quer remov\xc3\xaa-la?  Ela n\xc3\xa3o ir\xc3\xa1 para o seu cesto de flores, e voc\xc3\xaa tamb\xc3\xa9m n\xc3\xa3o receber\xc3\xa1 aumento na sua habilidade.'
ConfirmUnbloomingFlower = '%(plant)s n\xc3\xa3o est\xc3\xa1 desabrochando.  Tem certeza de que quer remov\xc3\xaa-la?  Ela n\xc3\xa3o ir\xc3\xa1 para o seu cesto de flores, e voc\xc3\xaa tamb\xc3\xa9m n\xc3\xa3o receber\xc3\xa1 aumento na sua habilidade.'
ConfirmNoSkillupFlower = 'Tem certeza de que quer remover %(plant)s? Ela n\xc3\xa3o ir\xc3\xa1 para o seu cesto de flores, e voc\xc3\xaa tamb\xc3\xa9m n\xc3\xa3o receber\xc3\xa1 aumento na sua habilidade.'
ConfirmSkillupFlower = 'Tem certeza de que quer colher %(plant)s?  Ela ir\xc3\xa1 para o seu cesto de flores. Voc\xc3\xaa vai receber um aumento de habilidade.'
ConfirmMaxedSkillFlower = 'Tem certeza que quer colher as %(plant)s?  Elas ir\xc3\xa3o para sua cesta de flores. Suas habilidades N\xc3\x83O aumentar\xc3\xa3o pois voc\xc3\xaa j\xc3\xa1 atingiu o m\xc3\xa1ximo.'
ConfirmBasketFull = 'Seu cesto de flores est\xc3\xa1 cheio. Venda algumas flores primeiro.'
ConfirmRemoveTree = 'Tem certeza de que quer remover %(tree)s?'
ConfirmWontBeAbleToHarvest = ' Se voc\xc3\xaa remover esta \xc3\xa1rvore, voc\xc3\xaa n\xc3\xa3o colher\xc3\xa1 piadas das \xc3\xa1rvores mais altas.'
ConfirmRemoveStatuary = 'Tem certeza de que quer apagar para sempre %(item)s?'
ResultPlantedSomething = 'Parab\xc3\xa9ns! Voc\xc3\xaa acaba de plantar %s.'
ResultPlantedSomethingAn = 'Parab\xc3\xa9ns! Voc\xc3\xaa acaba de plantar %s.'
ResultPlantedNothing = 'Isso n\xc3\xa3o funcionou.  Por favor, tente uma combina\xc3\xa7\xc3\xa3o diferente de balinhas.'
GardenGagTree = '\xc3\x81rvore de Brincadeira'
GardenUberGag = 'Brincadeira de Uber'

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
            retval = '%d %s balinhas' % (len(beanTuple), BeanColorWords[beanTuple[0]])
        else:
            retval = 'uma balinha %s' % BeanColorWords[beanTuple[0]]
    else:
        retval += 'a'
        maxBeans = len(beanTuple)
        for index in range(maxBeans):
            if index == maxBeans - 1:
                retval += ' e balinha %s' % BeanColorWords[beanTuple[index]]
                continue
            if index == 0:
                retval += ' %s' % BeanColorWords[beanTuple[index]]
                continue
            retval += ', %s' % BeanColorWords[beanTuple[index]]
        
    return retval

GardenTextMagicBeans = 'Balas M\xc3\xa1gicas'
GardenTextMagicBeansB = 'Outras Balas'
GardenSpecialDiscription = 'Este texto deveria explicar como usar certo especial do jardim'
GardenSpecialDiscriptionB = 'Este texto deveria explicar como usar certo especial do jardim, podicr\xc3\xaa!'
GardenTrophyAwarded = 'Uau! Voc\xc3\xaa tem %s de %s flores. Isso merece um trof\xc3\xa9u e uma melhora na Risada!'
GardenTrophyNameDict = {
    0: 'Carrinho de M\xc3\xa3o',
    1: 'P\xc3\xa1s',
    2: 'Flor',
    3: 'Regador',
    4: 'Tubar\xc3\xa3o',
    5: 'Peixe-Espada',
    6: 'Baleia Assassina' }
SkillTooLow = 'Habilidade\nBaixa Demais'
NoGarden = 'Nenhum \nJardim'

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

TravelGameTitle = 'Trilhos de Bonde'
TravelGameInstructions = 'Clique para cima ou para baixo para definir seu n\xc3\xbamero de votos.  Clique no bot\xc3\xa3o votar para lan\xc3\xa7ar os votos. Chegue ao seu objetivo secreto para conseguir balinhas extras. Ganhe mais votos quando se der bem nos outros jogos.'
TravelGameRemainingVotes = 'Votos Restantes:'
TravelGameUse = 'Usar'
TravelGameVotesWithPeriod = 'votos.'
TravelGameVotesToGo = 'votos restantes'
TravelGameVoteToGo = 'voto restante'
TravelGameUp = 'PARA CIMA.'
TravelGameDown = 'PARA BAIXO.'
TravelGameVoteWithExclamation = 'Vote!'
TravelGameWaitingChoices = 'Esperando que outros jogadores votem...'
TravelGameDirections = [
    'PARA CIMA',
    'PARA BAIXO']
TravelGameTotals = 'Totais '
TravelGameReasonVotes = 'O bonde est\xc3\xa1 indo para %(dir)s, vencendo por %(numVotes)de votos.'
TravelGameReasonVotesPlural = 'O bonde est\xc3\xa1 indo para %(dir)s, vencendo por %(numVotes)de votos.'
TravelGameReasonVotesSingular = 'O bonde est\xc3\xa1 indo para %(dir)s, vencendo por %(numVotes)de voto.'
TravelGameReasonPlace = '%(name)s desempatou. O bonde est\xc3\xa1 indo para %(dir)s.'
TravelGameReasonRandom = 'O bonde est\xc3\xa1 indo aleatoriamente para %(dir)s.'
TravelGameOneToonVote = '%(name)s usou %(numVotes)s votos para ir para %(dir)s\n'
TravelGameBonusBeans = '%(numBeans)de Balinhas'
TravelGamePlaying = 'A seguir, o jogo do bonde de %(game)s.'
TravelGameGotBonus = '%(name)s ganhou um b\xc3\xb4nus de %(numBeans)s balinhas!'
TravelGameNoOneGotBonus = 'Ningu\xc3\xa9m chegou ao seu objetivo secreto.  Todos ganham 1 balinha.'
TravelGameConvertingVotesToBeans = 'Convertendo alguns votos em balinhas...'
TravelGameGoingBackToShop = 'S\xc3\xb3 resta 1 jogador. Indo para a Loja de Piadas do Pateta.'
PairingGameTitle = 'Jogo de Mem\xc3\xb3ria Toon'
PairingGameInstructions = 'Aperte Delete para virar uma carta. Combine 2 cartas iguais para marcar um ponto. Combine cartas com o brilho de b\xc3\xb4nus e ganhe um ponto extra. Ganhe mais pontos virando poucas vezes.'
PairingGameInstructionsMulti = 'Aperte Delete para virar uma carta. Aperte Ctrl para fazer o sinal para outro jogador virar uma carta. Combine 2 cartas iguais para marcar um ponto. Combine cartas com o brilho de b\xc3\xb4nus e ganhe um ponto extra. Ganhe mais pontos virando poucas vezes.'
PairingGamePerfect = 'PERFEITO!!'
PairingGameFlips = 'Viradas:'
PairingGamePoints = 'Pontos:'
TrolleyHolidayStart = 'Vamos come\xc3\xa7ar com os Trilhos de Bonde!  Para jogar, embarque em qualquer bonde com 2 ou mais Toons.'
TrolleyHolidayOngoing = ''
TrolleyHolidayEnd = 'Isso \xc3\xa9 tudo nos Trilhos de Bonde por hoje.  At\xc3\xa9 a pr\xc3\xb3xima semana!'
TrolleyWeekendStart = 'O Fim de Semana dos Trilhos de Bonde vai come\xc3\xa7ar!  Para jogar, embarque em qualquer bonde com 2 ou mais Toons.'
TrolleyWeekendEnd = 'Terminamos com o Fim de Semana dos Trilhos de Bonde.'
VineGameTitle = 'Cip\xc3\xb3s da Selva'
VineGameInstructions = 'Chegue ao cip\xc3\xb3 mais \xc3\xa0 direita a tempo. Aperte para Cima ou para Baixo para escalar o cip\xc3\xb3.  Aperte para Esquerda ou Direita para mudar de dire\xc3\xa7\xc3\xa3o e pular.  Quanto mais baixo voc\xc3\xaa estiver no cip\xc3\xb3, mais r\xc3\xa1pido poder\xc3\xa1 saltar dele. Colete as bananas se puder, mas evite os morcegos e aranhas.'
ValentinesDayStart = 'Feliz Dia dos namorados!'
ValentinesDayEnd = ' Aquele \xc3\xa9 todo para Dia dos namorados!'
GolfCourseNames = {
    0: 'Tacada e Caminhada',
    1: 'Tacadas Divertidas',
    2: 'Todas as Tacadas' }
GolfHoleNames = {
    0: 'Vit\xc3\xb3ria-em-Uma',
    1: 'Sem D\xc3\xbavida at\xc3\xa9 o Buraco',
    2: 'S\xc3\xb3 na Descida',
    3: 'S\xc3\xb3 Vejo Verde',
    4: 'Tacadas Quentes',
    5: '\xc3\x89 na Manteiga',
    6: 'Balan\xc3\xa7o do Taco',
    7: 'Na Tacada das Cinco Horas',
    8: 'Divers\xc3\xa3o no Gramad\xc3\xa3o',
    9: 'A Bola Cai e a Gente Vibra',
    10: 'Nada de Bogey',
    11: 'Hora do Taco',
    12: 'Santa Tacada!',
    13: 'S\xc3\xb3 um Birdie, Vai',
    14: 'Correndo para o Buraco',
    15: 'Hora da Tacada',
    16: 'Buraco ao Alcance',
    17: 'Mais um Vento e Chega',
    18: 'Vit\xc3\xb3ria-em-Uma-2',
    19: 'Sem D\xc3\xbavida, at\xc3\xa9 o Buraco-2',
    20: 'S\xc3\xb3 na Descida-2',
    21: 'S\xc3\xb3 Vejo Verde-2',
    22: 'Tacadas Quentes-2',
    23: '\xc3\x89 na Manteiga-2',
    24: 'Balan\xc3\xa7o do Taco-2',
    25: 'Na Tacada das Cinco Horas-2',
    26: 'Divers\xc3\xa3o no Gramad\xc3\xa3o-2',
    27: 'A Bola Cai e a Gente Vibra-2',
    28: 'Nada de Bogey-2',
    29: 'Hora do Taco-2',
    30: 'Santa Tacada!-2',
    31: 'S\xc3\xb3 um Birdie, Vai-2',
    32: 'Correndo para o Buraco-2',
    33: 'Hora da Tacada-2',
    34: 'Buraco ao Alcance-2',
    35: 'Mais um Vento e Chega-2' }
GolfHoleInOne = 'Buraco-em-Uma'
GolfCondor = 'Condor'
GolfAlbatross = 'Albatroz'
GolfEagle = '\xc3\x81guia'
GolfBirdie = 'Passarinho'
GolfPar = 'Par'
GolfBogey = 'Bogey'
GolfDoubleBogey = 'Bogey Duplo'
GolfTripleBogey = 'Bogey Triplo'
GolfShotDesc = {
    -4: GolfCondor,
    -3: GolfAlbatross,
    -2: GolfEagle,
    -1: GolfBirdie,
    0: GolfPar,
    1: GolfBogey,
    2: GolfDoubleBogey,
    3: GolfTripleBogey }
from toontown.golf import GolfGlobals
CoursesCompleted = 'Percursos Conclu\xc3\xaddos'
CoursesUnderPar = 'Percursos Abaixo do Par'
HoleInOneShots = 'Jogadas de Buraco-em-Uma'
EagleOrBetterShots = 'Jogadas de Eagle ou Melhor'
BirdieOrBetterShots = 'Jogadas de Birdie ou Melhor'
ParOrBetterShots = 'Jogadas de Par ou Melhor'
MultiPlayerCoursesCompleted = 'Concursos Multiplayer Conclu\xc3\xaddos'
TwoPlayerWins = 'Vit\xc3\xb3rias com Dois Jogadores'
ThreePlayerWins = 'Jogadas com Tr\xc3\xaas Jogadores'
FourPlayerWins = 'Jogadas com Quatro Jogadores'
CourseZeroWins = GolfCourseNames[0] + ' Vit\xc3\xb3rias'
CourseOneWins = GolfCourseNames[1] + ' Vit\xc3\xb3rias'
CourseTwoWins = GolfCourseNames[2] + ' Vit\xc3\xb3rias'
GolfHistoryDescriptions = [
    CoursesCompleted,
    CoursesUnderPar,
    HoleInOneShots,
    EagleOrBetterShots,
    BirdieOrBetterShots,
    ParOrBetterShots,
    MultiPlayerCoursesCompleted,
    CourseZeroWins,
    CourseOneWins,
    CourseTwoWins]
GolfTrophyDescriptions = [
    str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesCompleted][0]) + ' ' + CoursesCompleted,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesCompleted][1]) + ' ' + CoursesCompleted,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesCompleted][2]) + ' ' + CoursesCompleted,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesUnderPar][0]) + ' ' + CoursesUnderPar,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesUnderPar][1]) + ' ' + CoursesUnderPar,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesUnderPar][2]) + ' ' + CoursesUnderPar,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.HoleInOneShots][0]) + ' ' + HoleInOneShots,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.HoleInOneShots][1]) + ' ' + HoleInOneShots,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.HoleInOneShots][2]) + ' ' + HoleInOneShots,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.EagleOrBetterShots][0]) + ' ' + EagleOrBetterShots,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.EagleOrBetterShots][1]) + ' ' + EagleOrBetterShots,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.EagleOrBetterShots][2]) + ' ' + EagleOrBetterShots,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.BirdieOrBetterShots][0]) + ' ' + BirdieOrBetterShots,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.BirdieOrBetterShots][1]) + ' ' + BirdieOrBetterShots,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.BirdieOrBetterShots][2]) + ' ' + BirdieOrBetterShots,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.ParOrBetterShots][0]) + ' ' + ParOrBetterShots,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.ParOrBetterShots][1]) + ' ' + ParOrBetterShots,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.ParOrBetterShots][2]) + ' ' + ParOrBetterShots,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.MultiPlayerCoursesCompleted][0]) + ' ' + MultiPlayerCoursesCompleted,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.MultiPlayerCoursesCompleted][1]) + ' ' + MultiPlayerCoursesCompleted,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.MultiPlayerCoursesCompleted][2]) + ' ' + MultiPlayerCoursesCompleted,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseZeroWins][0]) + ' ' + CourseZeroWins,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseZeroWins][1]) + ' ' + CourseZeroWins,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseZeroWins][2]) + ' ' + CourseZeroWins,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseOneWins][0]) + ' ' + CourseOneWins,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseOneWins][1]) + ' ' + CourseOneWins,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseOneWins][2]) + ' ' + CourseOneWins,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseTwoWins][0]) + ' ' + CourseTwoWins,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseTwoWins][1]) + ' ' + CourseTwoWins,
    str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseTwoWins][2]) + ' ' + CourseTwoWins]
GolfCupDescriptions = [
    str(GolfGlobals.TrophiesPerCup) + ' Trof\xc3\xa9us ganhos',
    str(GolfGlobals.TrophiesPerCup * 2) + ' Trof\xc3\xa9us ganhos',
    str(GolfGlobals.TrophiesPerCup * 3) + ' Trof\xc3\xa9us ganhos']
GolfAvReceivesHoleBest = '%(name)s marcou um novo recorde de tacadas em %(hole)s!'
GolfAvReceivesCourseBest = '%(name)s marcou um novo recorde de percurso em %(course)s!!'
GolfAvReceivesCup = '%(name)s ganhou a ta\xc3\xa7a %(cup)s!!  B\xc3\xb4nus em pontos de risada!'
GolfAvReceivesTrophy = '%(name)s ganhou o trof\xc3\xa9u %(award)s!!'
GolfRanking = 'Posi\xc3\xa7\xc3\xa3o: \n'
GolfPowerBarText = '%(power)s%%'
GolfChooseTeeInstructions = 'Aperte para Esquerda ou Direita para mudar a posi\xc3\xa7\xc3\xa3o do taco.\nAperte Ctrl para selecionar.'
GolfWarningMustSwing = 'Aten\xc3\xa7\xc3\xa3o: voc\xc3\xaa precisa apertar Ctrl na sua pr\xc3\xb3xima tacada.'
GolfAimInstructions = 'Aperte para a Esquerda ou Direita para mirar.\nAperte e segure Ctrl para balan\xc3\xa7ar o taco.'
GolferExited = '%s saiu do percurso de golfe.'
GolfPowerReminder = 'Segure Ctrl por Mais Tempo para\nMandar a Bola Mais Longe'
GolfPar = 'Par'
GolfHole = 'Buraco'
GolfTotal = 'Total'
GolfExitCourse = 'Sair do Percurso'
GolfUnknownPlayer = '???'
GolfPageTitle = 'Golfe'
GolfPageTitleCustomize = 'Personalizador de Golfe'
GolfPageTitleRecords = 'Recordes Pessoais'
GolfPageTitleTrophy = 'Trof\xc3\xa9us de Golfe'
GolfPageCustomizeTab = 'Personalizar'
GolfPageRecordsTab = 'Recordes'
GolfPageTrophyTab = 'Trof\xc3\xa9u'
GolfPageTickets = 'Bilhetes: '
GolfPageConfirmDelete = 'Apagar Acess\xc3\xb3rio?'
GolfTrophyTextDisplay = 'Trof\xc3\xa9u %(number)s : %(desc)s'
GolfCupTextDisplay = 'Ta\xc3\xa7a %(number)s : %(desc)s'
GolfCurrentHistory = '%(historyDesc)s Atual: %(num)s'
GolfTieBreakWinner = '%(name)s venceu o desempate aleat\xc3\xb3rio!'
GolfSeconds = ' -  %(time).2f segundos'
GolfTimeTieBreakWinner = '%(name)s venceu o desempate por tempo total de mira!!!'
RoamingTrialerWeekendStart = 'Est\xc3\xa1 come\xc3\xa7ando a Tour por Toontown! Jogadores podem entrar em qualquer vizinhan\xc3\xa7a de gra\xc3\xa7a!'
RoamingTrialerWeekendOngoing = 'Boas-vindas ao Tour por Toontown! Jogadores podem entrar gratuitamente em qualquer vizinhan\xc3\xa7a!'
RoamingTrialerWeekendEnd = 'Terminamos com o Tour por Toontown.'
MoreXpHolidayStart = 'Boas novas! Come\xc3\xa7ou o per\xc3\xadodo de Teste Toon, com o dobro de experi\xc3\xaancia em piadas.'
MoreXpHolidayOngoing = 'Ol\xc3\xa1! Estamos no per\xc3\xadodo de Teste Toon, com o dobro de experi\xc3\xaancia em piadas.'
MoreXpHolidayEnd = 'Terminou o per\xc3\xadodo exclusivo de Teste Toon, com o dobro de experi\xc3\xaancia em piadas. Obrigado por nos ajudar a Testar!'
JellybeanDayHolidayStart = '\xc3\x89 Dia das Balinhas! Ganhe pr\xc3\xaamios de Balinhas em dobro nas Festas!'
JellybeanDayHolidayEnd = 'Acabou o Dia das Balinhas. Vejo voc\xc3\xaa no ano que vem.'
PartyRewardDoubledJellybean = 'Balinhas em Dobro!'
GrandPrixWeekendHolidayStart = '\xc3\x89 o Fim de Semana do Grande Pr\xc3\xaamio no Aut\xc3\xb3dromo do Pateta! Quem jogar gratuitamente ou pagando pode obter a maioria dos pontos em tr\xc3\xaas corridas consecutivas.'
GrandPrixWeekendHolidayEnd = 'O Fim de Semana do Grande Pr\xc3\xaamio acabou. Vejo voc\xc3\xaa no ano que vem.'
SellbotNerfHolidayStart = 'A Opera\xc3\xa7\xc3\xa3o: Rob\xc3\xb4 Vendedor Tempestade est\xc3\xa1 acontecendo agora! Batalhe contra o VP hoje!'
SellbotNerfHolidayEnd = 'A Opera\xc3\xa7\xc3\xa3o: Rob\xc3\xb4 Vendedor Tempestade terminou. \xc3\x93timo trabalho, Toons!'
JellybeanTrolleyHolidayStart = 'Os Dias de Balinha em Dobro para Jogos de Bonde come\xc3\xa7aram!'
JellybeanTrolleyHolidayEnd = 'Os Dias de Balinha em Dobro para Jogos de Bonde terminaram!'
JellybeanFishingHolidayStart = 'Os Dias de Balinha em Dobro para Pescaria come\xc3\xa7aram!'
JellybeanFishingHolidayEnd = 'Os Dias de Balinha em Dobro para Pescaria terminaram!'
JellybeanPartiesHolidayStart = 'Os Dias de Balinha em Dobro para Jogos de Grupo come\xc3\xa7aram!'
JellybeanPartiesHolidayEnd = 'Os Dias de Balinha em Dobro para Jogos de Grupo terminaram!'
BankUpgradeHolidayStart = 'Aconteceu Algo Toont\xc3\xa1stico com seu Banco de Balinha!'
HalloweenPropsHolidayStart = '\xc3\x89 Halloween em Toontown!'
HalloweenPropsHolidayEnd = 'O Halloween terminou. Bu!'
BlackCatHolidayStart = 'Crie um Gato Preto - S\xc3\xb3 Hoje!'
BlackCatHolidayEnd = 'O Dia do Gato Preto terminou!'
TopToonsMarathonStart = 'A Maratona de Ano-Novo dos Toons come\xc3\xa7ou!'
TopToonsMarathonEnd = 'A Maratona de Ano-Novo dos Toons terminou!'
WinterDecorationsStart = '\xc3\x89 hora da Festa de Natal em Toontown!'
WinterDecorationsEnd = 'A Festa de Natal acabou - Feliz Ano-Novo!'
WinterCarolingStart = 'As Can\xc3\xa7\xc3\xb5es de Natal come\xc3\xa7aram em Toontown. Cante para a sua Cabe\xc3\xa7a de Boneco de Neve!\xe2\x80\x9d.'
LogoutForced = 'Voc\xc3\xaa fez algo errado\n e estamos fazendo seu logout automaticamente,\n sua conta tamb\xc3\xa9m pode estar congelada.\n Experimente dar uma volta l\xc3\xa1 fora, \xc3\xa9 divertido.'
CountryClubToonEnterElevator = '%s \nentrou no carrinho de golfe.'
CountryClubBossConfrontedMsg = '%s est\xc3\xa1 lutando com o Presidente do Clube!'
ElevatorBlockedRoom = 'Todos os desafios devem ser vencidos antes disso.'
MolesLeft = 'Toupeiras Restantes: %d'
MolesInstruction = 'Pis\xc3\xa3o nas Toupeiras!\nPule nas toupeiras vermelhas!'
MolesFinished = 'Pis\xc3\xa3o nas Toupeiras vencido!'
MolesPityWin = 'Erro ao Pisotear! Mas as toupeiras sa\xc3\xadram.'
MolesRestarted = 'Perdeu no Pis\xc3\xa3o! Recome\xc3\xa7ando...'
BustACogInstruction = 'Remova a bola Cog!'
BustACogExit = 'Sair por Enquanto'
BustACogHowto = 'Como Jogar'
BustACogFailure = 'Acabou o Tempo!'
BustACogSuccess = 'Sucesso!'
GolfGreenGameScoreString = 'Quebra-Cabe\xc3\xa7as Restantes: %s'
GolfGreenGamePlayerScore = 'Resolveu %s'
GolfGreenGameBonusGag = 'Voc\xc3\xaa ganhou %s!'
GolfGreenGameGotHelp = '%s resolveu um Quebra-Cabe\xc3\xa7a!'
GolfGreenGameDirections = 'D\xc3\xaa tacadas nas bolas usando o mouse\n\n\nCombinar tr\xc3\xaas bolas de uma mesma cor as faz cair\n\n\nRemova todas as bolas Cog da tela'
enterHedgeMaze = 'Corra pela Sebe-Labirinto\n para ganhar b\xc3\xb4nus de risadas!'
toonFinishedHedgeMaze = '%s \n  terminou em %s lugar!'
hedgeMazePlaces = [
    'primeiro',
    'segundo',
    'terceiro',
    'quarto']
mazeLabel = 'Corrida no Labirinto!'
BoardingPartyReadme = 'Grupo de Abordagem?'
BoardingGroupHide = 'Ocultar'
BoardingGroupShow = 'Exibir Grupo de Abordagem'
BoardingPartyInform = 'Crie um Grupo de Abordagem para o elevador clicando em outro Toon e fazendo um convite.\nNessa \xc3\xa1rea, os Grupos de Abordagem n\xc3\xa3o podem ter mais de %s Toons.'
BoardingPartyTitle = 'Grupo de Abordagem'
QuitBoardingPartyLeader = 'Dispensar'
QuitBoardingPartyNonLeader = 'Deixar'
QuitBoardingPartyConfirm = 'Tem certeza de que quer sair desse Grupo de Abordagem?'
BoardcodeMissing = 'Aconteceu algum erro; tente mais tarde.'
BoardcodeMinLaffLeader = 'N\xc3\xa3o \xc3\xa9 poss\xc3\xadvel fazer abordagem com seu grupo porque voc\xc3\xaa tem menos de %s pontos de risada.'
BoardcodeMinLaffNonLeaderSingular = 'Seu grupo n\xc3\xa3o pode fazer abordagem porque %s tem menos de %s pontos de risada.'
BoardcodeMinLaffNonLeaderPlural = 'Seu grupo n\xc3\xa3o pode fazer abordagem porque %s tem menos de %s pontos de risada.'
BoardcodePromotionLeader = 'Seu grupo n\xc3\xa3o pode fazer abordagem porque voc\xc3\xaa n\xc3\xa3o tem m\xc3\xa9ritos de promo\xc3\xa7\xc3\xa3o suficientes.'
BoardcodePromotionNonLeaderSingular = 'Seu grupo n\xc3\xa3o pode fazer abordagem porque %s n\xc3\xa3o tem m\xc3\xa9ritos de promo\xc3\xa7\xc3\xa3o suficientes.'
BoardcodePromotionNonLeaderPlural = 'Seu grupo n\xc3\xa3o pode fazer abordagem porque %s n\xc3\xa3o tem m\xc3\xa9ritos de promo\xc3\xa7\xc3\xa3o suficientes.'
BoardcodeSpace = 'Seu grupo n\xc3\xa3o pode fazer abordagem porque n\xc3\xa3o tem espa\xc3\xa7o suficiente.'
BoardcodeBattleLeader = 'Seu grupo n\xc3\xa3o pode fazer abordagem porque voc\xc3\xaa est\xc3\xa1 combatendo.'
BoardcodeBattleNonLeaderSingular = 'Seu grupo n\xc3\xa3o pode fazer abordagem porque %s est\xc3\xa1 combatendo.'
BoardcodeBattleNonLeaderPlural = 'Seu grupo n\xc3\xa3o pode fazer abordagem porque %s est\xc3\xa1 combatendo.'
BoardingInviteMinLaffInviter = 'Voc\xc3\xaa precisa de %s Pontos de Risada antes de se tornar associado desse Grupo de Abordagem.'
BoardingInviteMinLaffInvitee = '%s precisa de %s Pontos de Risada antes de se tornar associado desse Grupo de Abordagem.'
BoardingInvitePromotionInviter = 'Voc\xc3\xaa precisa receber uma promo\xc3\xa7\xc3\xa3o antes de se tornar associado desse Grupo de Abordagem.'
BoardingInvitePromotionInvitee = '%s precisa receber uma promo\xc3\xa7\xc3\xa3o antes de se tornar associado desse Grupo de Abordagem.'
BoardingInviteNotPaidInvitee = '%s precisa ser um Assinante para fazer parte do seu Grupo de Abordagem.'
BoardingInviteeInDiffGroup = '%s j\xc3\xa1 est\xc3\xa1 em outro Grupo de Abordagem.'
BoardingInviteeInKickOutList = '%s foi removido por seu l\xc3\xadder. Apenas o l\xc3\xadder pode reconvidar associados removidos.'
BoardingInviteePendingIvite = '%s tem um convite pendente; tente novamente mais tarde.'
BoardingInviteeInElevator = '%s est\xc3\xa1 ocupado(a) no momento; tente novamente mais tarde.'
BoardingInviteGroupFull = 'Seu Grupo de Abordagem j\xc3\xa1 est\xc3\xa1 completo'
BoardingAlreadyInGroup = 'Voc\xc3\xaa n\xc3\xa3o pode aceitar esse convite porque j\xc3\xa1 est\xc3\xa1 em outro Grupo de Abordagem.'
BoardingGroupAlreadyFull = 'Voc\xc3\xaa n\xc3\xa3o pode aceitar esse convite porque o grupo j\xc3\xa1 est\xc3\xa1 completo.'
BoardingKickOutConfirm = 'Tem certeza de que quer remover %s?'
BoardingPendingInvite = 'Primeiro voc\xc3\xaa tem de resolver\n o convite pendente.'
BoardingCannotLeaveZone = 'Voc\xc3\xaa n\xc3\xa3o pode deixar essa \xc3\xa1rea porque voc\xc3\xaa faz parte de um Grupo de Abordagem.'
BoardingInviteeMessage = '%s gostaria de se juntar ao seu Grupo de Abordagem.'
BoardingInvitingMessage = 'Convidando %s para seu Grupo de Abordagem.'
BoardingInvitationRejected = '%s recusou se juntar ao seu Grupo de Abordagem.'
BoardingMessageKickedOut = 'Voc\xc3\xaa foi removido do Grupo de Abordagem.'
BoardingMessageInvited = '%s convidou %s para o Grupo de Abordagem.'
BoardingMessageLeftGroup = '%s deixou o Grupo de Abordagem.'
BoardingMessageGroupDissolved = 'Seu Grupo de Abordagem foi dispensado pelo l\xc3\xadder do grupo.'
BoardingMessageGroupDisbandedGeneric = 'Seu Grupo de Abordagem foi dispensado.'
BoardingMessageInvitationFailed = '%s tentou convidar voc\xc3\xaa para seu Grupo de Abordagem.'
BoardingMessageGroupFull = '%s tentou aceitar seu convite, mas seu grupo estava completo.'
BoardingGo = 'IR'
BoardingCancelGo = 'Clique Novamente para\nCancelar o comando Ir'
And = 'e'
BoardingGoingTo = 'Indo Para:'
BoardingTimeWarning = 'Abordando o elevador em '
BoardingMore = 'mais'
BoardingGoShow = 'Indo para\n%s em '
BoardingGoPreShow = 'Confirmando...'
BossbotBossName = 'Presidente'
BossbotRTWelcome = 'Seus Toons v\xc3\xa3o precisar de disfarces diferentes.'
BossbotRTRemoveSuit = 'Primeiramente, tire suas roupas de Cog...'
BossbotRTFightWaiter = 'e, ent\xc3\xa3o, lute com estes gar\xc3\xa7ons.'
BossbotRTWearWaiter = 'Bom Trabalho! Agora, coloque as roupas de gar\xc3\xa7om.'
BossbotBossPreTwo1 = 'Por que est\xc3\xa1 demorando tanto? '
BossbotBossPreTwo2 = 'Vamos, sirva meu banquete!'
BossbotRTServeFood1 = 'Hehe, sirva a comida que eu coloco nestas esteiras.'
BossbotRTServeFood2 = 'Se voc\xc3\xaa servir um Cog tr\xc3\xaas vezes seguidas, ele vai explodir.'
BossbotResistanceToonName = 'A velha e boa Risada'
BossbotPhase3Speech1 = 'O que est\xc3\xa1 acontecendo aqui?!'
BossbotPhase3Speech2 = 'Esses gar\xc3\xa7ons s\xc3\xa3o Toons!'
BossbotPhase3Speech3 = 'Peguem-nos!!!'
BossbotPhase4Speech1 = 'Humpf. Se quero um trabalho bem feito...'
BossbotPhase4Speech2 = 'tenho de fazer eu mesmo.'
BossbotRTPhase4Speech1 = 'Bom Trabalho! Agora, esguiche \xc3\xa1gua no Presidente nas mesas...'
BossbotRTPhase4Speech2 = 'ou use bolas de golfe para atras\xc3\xa1-lo.'
BossbotPitcherLeave = 'Deixar Garrafa'
BossbotPitcherLeaving = 'Deixando Garrafa'
BossbotPitcherAdvice = 'Use as teclas para esquerda e direita se quiser girar.\nSegure Ctrl para aumentar a for\xc3\xa7a.\nSolte Ctrl para disparar.'
BossbotGolfSpotLeave = 'Deixar Bola de Golfe'
BossbotGolfSpotLeaving = 'Deixando Bola de Golfe'
BossbotGolfSpotAdvice = 'Use as teclas para esquerda e direita se quiser girar.\nCtrl dispara.'
BossbotRewardSpeech1 = 'N\xc3\xa3o! O Presidente do Conselho n\xc3\xa3o vai gostar disso.'
BossbotRewardSpeech2 = 'Arrrggghhh!!!!'
BossbotRTCongratulations = 'Voc\xc3\xaa conseguiu!  Voc\xc3\xaa rebaixou o Presidente!\x7Pegue estes bilhetes azuis que o Presidente deixou para tr\xc3\xa1s.\x7Com eles, voc\xc3\xaa vai poder disparar contra Cogs em batalha.'
BossbotRTLastPromotion = '\x7Uau, voc\xc3\xaa chegou ao n\xc3\xadvel %s com sua Roupa de Cog!\x7Os Cogs n\xc3\xa3o conseguem promo\xc3\xa7\xc3\xb5es maiores do que essa.\x7Voc\xc3\xaa n\xc3\xa3o pode mais atualizar sua Roupa de Cog, mas, certamente, poder\xc3\xa1 continuar trabalhando para a Resist\xc3\xaancia!'
BossbotRTHPBoost = '\x7Voc\xc3\xaa trabalhou bastante para a Resist\xc3\xaancia.\x7O Conselho Toon decidiu lhe dar mais um ponto de Risada. Parab\xc3\xa9ns!'
BossbotRTMaxed = '\x7Vejo que voc\xc3\xaa tem uma Roupa de Cog de n\xc3\xadvel %s. Impressionante!\x7Em nome do Conselho Toon, agrade\xc3\xa7o por voltar para defender mais Toons!'
GolfAreaAttackTaunt = 'Bola!'
OvertimeAttackTaunts = [
    '\xc3\x89 hora de reorganizar.',
    'Temos gente para demitir.']
ElevatorBossBotBoss = 'Batalha do C.E.O.'
ElevatorBossBotCourse = 'Campo de Golfe Cog'
ElevatorBossBotCourse0 = 'O Front Three (Tr\xc3\xaas da Frente)'
ElevatorBossBotCourse1 = 'O Middle Six (Seis do Meio)'
ElevatorBossBotCourse2 = 'O Back Nine (Nove dos Fundos)'
ElevatorCashBotBoss = 'Batalha do C.F.O'
ElevatorCashBotMint0 = 'Coin Mint (a Mina de Moedas)'
ElevatorCashBotMint1 = 'Dollar Mint (a Mina de Dinheiro)'
ElevatorCashBotMint2 = 'Bullion Mint (a Mina de Ouro)'
ElevatorSellBotBoss = 'Batalha do Rob\xc3\xb4 Vendedor '
ElevatorSellBotFactory0 = 'Entrada Principal'
ElevatorSellBotFactory1 = 'Entrada dos Fundos'
ElevatorLawBotBoss = 'Batalha do Juiz-Chefe'
ElevatorLawBotCourse0 = 'Escrit\xc3\xb3rio A'
ElevatorLawBotCourse1 = 'Escrit\xc3\xb3rio B'
ElevatorLawBotCourse2 = 'Escrit\xc3\xb3rio C'
ElevatorLawBotCourse3 = 'Escrit\xc3\xb3rio D'
DaysToGo = 'Espere\n%s Dias'
IceGameTitle = 'Escorregador de Gelo'
IceGameInstructions = 'Chegue o mais perto do centro ao final da segunda rodada. Use as teclas de seta para mudar a dire\xc3\xa7\xc3\xa3o e a for\xc3\xa7a. Aperte Ctrl para lan\xc3\xa7ar seu Toon. Acerte os barris para ganhar mais pontos, e evite a dinamite!'
IceGameInstructionsNoTnt = 'Chegue o mais perto do centro ao final da segunda rodada. Use as teclas de seta para mudar a dire\xc3\xa7\xc3\xa3o e a for\xc3\xa7a. Aperte Ctrl para lan\xc3\xa7ar seu Toon. Acerte os barris para ganhar mais pontos.'
IceGameWaitingForPlayersToFinishMove = 'Esperando outros jogadores...'
IceGameWaitingForAISync = 'Esperando outros jogadores...'
IceGameInfo = 'Partida %(curMatch)d/%(numMatch)d, Rodada %(curRound)d/%(numRound)d'
IceGameControlKeyWarning = 'Lembre-se de apertar a tecla Ctrl!'
PicnicTableJoinButton = 'Entrar'
PicnicTableObserveButton = 'Observar'
PicnicTableCancelButton = 'Cancelar'
PicnicTableTutorial = 'Como Jogar'
PicnicTableMenuTutorial = 'Qual jogo voc\xc3\xaa quer aprender?'
PicnicTableMenuSelect = 'Qual jogo voc\xc3\xaa quer jogar?'
ChineseCheckersGetUpButton = 'Levantar-se'
ChineseCheckersStartButton = 'Iniciar Jogo'
ChineseCheckersQuitButton = 'Sair do Jogo'
ChineseCheckersIts = '\xc3\x89 a '
ChineseCheckersYourTurn = 'Sua Vez'
ChineseCheckersGreenTurn = 'Vez do Verde'
ChineseCheckersYellowTurn = 'Vez do Amarelo'
ChineseCheckersPurpleTurn = 'Vez do Roxo'
ChineseCheckersBlueTurn = 'Vez do Azul'
ChineseCheckersPinkTurn = 'Vez do Rosa'
ChineseCheckersRedTurn = 'Vez do Vermelho'
ChineseCheckersColorG = 'Voc\xc3\xaa \xc3\xa9 o Verde'
ChineseCheckersColorY = 'Voc\xc3\xaa \xc3\xa9 o Amarelo'
ChineseCheckersColorP = 'Voc\xc3\xaa \xc3\xa9 o Roxo'
ChineseCheckersColorB = 'Voc\xc3\xaa \xc3\xa9 o Azul'
ChineseCheckersColorPink = 'Voc\xc3\xaa \xc3\xa9 o Rosa'
ChineseCheckersColorR = 'Voc\xc3\xaa \xc3\xa9 o Vermelho'
ChineseCheckersColorO = 'Voc\xc3\xaa est\xc3\xa1 Observando'
ChineseCheckersYouWon = 'Voc\xc3\xaa acaba de ganhar uma partida de Xadrez Chin\xc3\xaas!'
ChineseCheckers = 'Xadrez Chin\xc3\xaas.'
ChineseCheckersGameOf = ' acaba de ganhar uma partida de '
ChineseTutorialTitle1 = 'Objetivo'
ChineseTutorialTitle2 = 'Como Jogar'
ChineseTutorialPrev = 'P\xc3\xa1gina Anterior'
ChineseTutorialNext = 'Pr\xc3\xb3xima P\xc3\xa1gina'
ChineseTutorialDone = 'Pronto'
ChinesePage1 = 'O objetivo do Xadrez Chin\xc3\xaas \xc3\xa9 ser o primeiro jogador a mover todas as suas pe\xc3\xa7as do tri\xc3\xa2ngulo de baixo do tabuleiro at\xc3\xa9 o tri\xc3\xa2ngulo do outro lado. O primeiro jogador a conseguir isso vence!'
ChinesePage2 = 'Os jogadores se alternam movendo qualquer pedra de sua pr\xc3\xb3pria cor.  Uma pedra pode se mover para um buraco ao lado, ou pode saltar por outras pedras. Os saltos devem passar por um m\xc3\xa1rmore e cair em um buraco livre. \xc3\x89 poss\xc3\xadvel combinar saltos para andar mais longe!'
CheckersPage1 = 'O objetivo das Damas \xc3\xa9 deixar o oponente sem poder fazer jogadas. Para isso, voc\xc3\xaa pode capturar todas as suas pe\xc3\xa7as, ou bloque\xc3\xa1-las para que n\xc3\xa3o ele n\xc3\xa3o possa mov\xc3\xaa-las.'
CheckersPage2 = 'Os jogadores se alternam movendo qualquer pedra de sua pr\xc3\xb3pria cor. Uma pe\xc3\xa7a pode se mover para um quadrado diagonal \xc3\xa0 frente. Uma pe\xc3\xa7a s\xc3\xb3 pode se mover para um quadrado que n\xc3\xa3o esteja ocupado por outra pe\xc3\xa7a. As damas seguem as mesmas regras, mas podem se mover para tr\xc3\xa1s.'
CheckersPage3 = 'Para capturar uma pe\xc3\xa7a do oponente, voc\xc3\xaa deve saltar sobre ela diagonalmente para o quadrado vazio depois dela. Se voc\xc3\xaa puder fazer alguma captura em sua vez, ter\xc3\xa1 de faz\xc3\xaa-la. Voc\xc3\xaa pode combinar capturas, desde que seja com a mesma pe\xc3\xa7a.'
CheckersPage4 = 'Uma pe\xc3\xa7a se torna dama quando chegar \xc3\xa0 \xc3\xbaltima linha do tabuleiro. Uma pe\xc3\xa7a que acaba de se tornar dama n\xc3\xa3o pode saltar de novo at\xc3\xa9 o pr\xc3\xb3ximo turno. Al\xc3\xa9m disso, damas podem se mover para todas as dire\xc3\xa7\xc3\xb5es e podem mudar de dire\xc3\xa7\xc3\xa3o ao saltar.'
CheckersGetUpButton = 'Levantar-se'
CheckersStartButton = 'Iniciar Jogo'
CheckersQuitButton = 'Sair do Jogo'
CheckersIts = '\xc3\x89 a '
CheckersYourTurn = 'Sua Vez'
CheckersWhiteTurn = 'Vez do Branco'
CheckersBlackTurn = 'Vez do Preto'
CheckersColorWhite = 'Voc\xc3\xaa \xc3\xa9 o Branco'
CheckersColorBlack = 'Voc\xc3\xaa \xc3\xa9 o Preto'
CheckersObserver = 'Voc\xc3\xaa est\xc3\xa1 Observando'
RegularCheckers = 'Damas.'
RegularCheckersGameOf = ' acaba de ganhar uma partida de '
RegularCheckersYouWon = 'Voc\xc3\xaa acaba de ganhar uma partida de Damas!'
MailNotifyNewItems = 'Chegou correio para voc\xc3\xaa!'
MailNewMailButton = 'Correio'
MailSimpleMail = 'Bilhete'
MailFromTag = 'Bilhete de: %s'
AwardNotifyNewItems = 'Voc\xc3\xaa tem um novo pr\xc3\xaamio na sua caixa de correio!'
AwardNotifyOldItems = 'Voc\xc3\xaa ainda tem pr\xc3\xaamios na sua caixa de correio para ser recolhidos!'
InviteInvitation = 'o convite'
InviteAcceptInvalidError = 'O convite n\xc3\xa3o \xc3\xa9 mais v\xc3\xa1lido.'
InviteAcceptPartyInvalid = 'Sua festa foi cancelada.'
InviteAcceptAllOk = 'O anfitri\xc3\xa3o recebeu sua resposta.'
InviteRejectAllOk = 'O anfitri\xc3\xa3o recebeu sua recusa do convite.'
Months = {
    1: 'JANEIRO',
    2: 'FEVEREIRO',
    3: 'MAR\xc3\x87O',
    4: 'ABRIL',
    5: 'MAIO',
    6: 'JUNHO',
    7: 'JULHO',
    8: 'AGOSTO',
    9: 'SETEMBRO',
    10: 'OUTUBRO',
    11: 'NOVEMBRO',
    12: 'DEZEMBRO' }
DayNames = ('Segunda-feira', 'Ter\xc3\xa7a-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'S\xc3\xa1bado', 'Domingo')
DayNamesAbbrev = ('SEG', 'TER', 'QUA', 'QUI', 'SEX', 'S\xc3\x81B', 'DOM')
HolidayNamesInCalendar = {
    1: ('Fogos de Artif\xc3\xadcio de Ver\xc3\xa3o', 'Comemore o Ver\xc3\xa3o com um espet\xc3\xa1culo de fogos de artif\xc3\xadcio a cada hora em cada p\xc3\xa1tio!'),
    2: ('Fogos de Artif\xc3\xadcio de Ano Novo', 'Feliz Ano Novo! Curta um espet\xc3\xa1culo de fogos de artif\xc3\xadcio a cada hora em cada p\xc3\xa1tio!'),
    3: ('Invas\xc3\xa3o Sanguessuga', 'Feliz Halloween! Impe\xc3\xa7a que os Cogs Sanguessugas invadam Toontown!'),
    4: ('Decora\xc3\xa7\xc3\xa3o de Feriados de Inverno', 'Comemore os Feriados de Inverno com \xc3\xa1rvores e postes de ilumina\xc3\xa7\xc3\xa3o Toont\xc3\xa1sticos!'),
    5: ('Invas\xc3\xa3o Skelecog', 'Impe\xc3\xa7a que os Skelecogs invadam Toontown!'),
    6: ('Invas\xc3\xa3o Dr. Celebridade ', 'Impe\xc3\xa7a que os Cogs  do Dr. Celebridade invadam Toontown!'),
    7: ('Bingo de Peixe', 'Quarta-feira do Bingo de Peixe! Todos no lago trabalhando juntos para completar a cartela antes de o tempo esgotar.'),
    8: ('Elei\xc3\xa7\xc3\xa3o de Esp\xc3\xa9cie de Toon', 'Vote na nova esp\xc3\xa9cie de Toon! Ser\xc3\xa1 uma Cabra? Ser\xc3\xa1 um Porco?'),
    9: ('Dia do Gato Preto', 'Feliz Halloween! Crie um Toon Gato Preto Toont\xc3\xa1stico \xe2\x80\x93 S\xc3\xb3 Hoje!'),
    13: ('Doces ou Travessuras', 'Feliz Halloween! V\xc3\xa1 atr\xc3\xa1s das guloseimas por toda Toontown para ganhar uma linda cabe\xc3\xa7a de ab\xc3\xb3bora de pr\xc3\xaamio!'),
    14: ('Grande Pr\xc3\xaamio', 'Segunda-feira do Grande Pr\xc3\xaamio no aut\xc3\xb3dromo do Pateta! Para vencer, conquiste o maior n\xc3\xbamero de pontos em tr\xc3\xaas corridas consecutivas!'),
    16: ('Fim de Semana do Grande Pr\xc3\xaamio', 'Quem jogar gratuitamente ou pagando compete nas corridas do Aut\xc3\xb3dromo do Pateta!'),
    17: ('Trilhas do Bondinho', 'Quinta-feira das Trilhas do Bondinho! Embarque em qualquer Bondinho para jogar com dois ou mais Toons.'),
    19: ('S\xc3\xa1bados Engra\xc3\xa7ados', 'Os s\xc3\xa1bados s\xc3\xa3o engra\xc3\xa7ados com o Bingo de Peixe, Grande Pr\xc3\xaamio e  Trilhas do Bondinho o dia todo!'),
    24: ('Idos de Mar\xc3\xa7o', 'Cuidado com os Idos de Mar\xc3\xa7o! Impe\xc3\xa7a que os Cogs Golpe Sujo invadam Toontown!'),
    26: ('Decora\xc3\xa7\xc3\xa3o de Halloween', 'Comemore o Halloween deixando as \xc3\xa1rvores e  postes de ilumina\xc3\xa7\xc3\xa3o de Toontown assustadores!'),
    28: ('Invas\xc3\xa3o de Inverno', 'Os Rob\xc3\xb4 Vendedor est\xc3\xa3o \xc3\xa0 solta espalhando suas t\xc3\xa1ticas de vendas frias!'),
    29: ('Semana Abril Toons', ' Comemore o Semana Abril Toons - um feriado construido por Toons para Toons!'),
    33: ('Surpresa de Rob\xc3\xb4 Vendedor 1', 'Surpresa de Rob\xc3\xb4 Vendedor! Impe\xc3\xa7a que os Cogs Reis da Incerta invadam Toontown!'),
    34: ('Surpresa de Rob\xc3\xb4 Vendedor 2', 'Surpresa de Rob\xc3\xb4 Vendedor! Impe\xc3\xa7a que os Cogs Sabe-com-quem-est\xc3\xa1-falando invadam Toontown!'),
    35: ('Surpresa de Rob\xc3\xb4 Vendedor 3', 'Surpresa de Rob\xc3\xb4 Vendedor! Impe\xc3\xa7a que os Cogs Amigos da On\xc3\xa7a invadam Toontown!'),
    36: ('Surpresa de Rob\xc3\xb4 Vendedor 4', 'Surpresa de Rob\xc3\xb4 Vendedor! Impe\xc3\xa7a que os Cogs Agitadores invadam Toontown!'),
    37: ('Enigma de Rob\xc3\xb4 Mercen\xc3\xa1rio 1', 'Enigma de Rob\xc3\xb4 Mercen\xc3\xa1rio. Impe\xc3\xa7a que os Cogs Farsantes invadam Toontown!'),
    38: ('Enigma de Rob\xc3\xb4 Mercen\xc3\xa1rio 2', 'Enigma de Rob\xc3\xb4 Mercen\xc3\xa1rio. Impe\xc3\xa7a que os Cogs M\xc3\xa3o de Vaca invadam Toontown!'),
    39: ('Enigma de Rob\xc3\xb4 Mercen\xc3\xa1rio 3', 'Enigma de Rob\xc3\xb4 Mercen\xc3\xa1rio. Impe\xc3\xa7a que os Cogs Conta-moedinhas invadam Toontown!'),
    40: ('Enigma de Rob\xc3\xb4 Mercen\xc3\xa1rio 4', 'Enigma de Rob\xc3\xb4 Mercen\xc3\xa1rio. Impe\xc3\xa7a que os Cogs Destruidores de N\xc3\xbameros invadam Toontown!'),
    41: ('A Estrat\xc3\xa9gia do Rob\xc3\xb4 da Lei 1', 'A Estrat\xc3\xa9gia do Rob\xc3\xb4 da Lei. Impe\xc3\xa7a que os Cogs Comensais invadam Toontown!'),
    42: ('A Estrat\xc3\xa9gia do Rob\xc3\xb4 da Lei 2', 'A Estrat\xc3\xa9gia do Rob\xc3\xb4 da Lei. Impe\xc3\xa7a que os Cogs Duplo Sentido invadam Toontown!'),
    43: ('A Estrat\xc3\xa9gia do Rob\xc3\xb4 da Lei 3', 'A Estrat\xc3\xa9gia do Rob\xc3\xb4 da Lei. Impe\xc3\xa7a que os Cogs Perseguidores de Ambul\xc3\xa2ncia invadam Toontown!'),
    44: ('A Estrat\xc3\xa9gia do Rob\xc3\xb4 da Lei 4', 'A Estrat\xc3\xa9gia do Rob\xc3\xb4 da Lei. Impe\xc3\xa7a que os Cogs Golpe Sujo invadam Toontown!'),
    45: ('O Problema Com Rob\xc3\xb4s Chefes 1', 'O Problema Com Rob\xc3\xb4s Chefes. Impe\xc3\xa7a que os Cogs Puxa-sacos invadam Toontown!'),
    46: ('O Problema Com Rob\xc3\xb4s Chefes 2', 'O Problema Com Rob\xc3\xb4s Chefes. Impe\xc3\xa7a que os Cogs Ratos de Escrit\xc3\xb3rio invadam Toontown!'),
    47: ('O Problema Com Rob\xc3\xb4s Chefes 3', 'O Problema Com Rob\xc3\xb4s Chefes. Impe\xc3\xa7a que os Cogs Microempres\xc3\xa1rios invadam Toontown!'),
    48: ('O Problema Com Rob\xc3\xb4s Chefes 4', 'O Problema Com Rob\xc3\xb4s Chefes. Impe\xc3\xa7a que os Cogs Fac\xc3\xb5es invadam Toontown!'),
    49: ('Dia da Balinha', 'Comemore o Dia da Balinha ganhando Balinhas em dobro nas festas!'),
    53: ('Invas\xc3\xa3o Reis da Incerta', 'Impe\xc3\xa7a que os Cogs  Reis da Incerta invadam Toontown!'),
    54: ('Invas\xc3\xa3o Conta-moedinha', 'Impe\xc3\xa7a que os Cogs  Conta-moedinhas invadam Toontown!'),
    55: ('Invas\xc3\xa3o Duplo Sentido', 'Impe\xc3\xa7a que os Cogs  Duplo Sentido invadam Toontown!'),
    56: ('Invas\xc3\xa3o de Fac\xc3\xa3o', 'Impe\xc3\xa7a que os Cogs Fac\xc3\xb5es invadam Toontown!'),
    57: ('Toon Caroling', 'Celebrate Winter Holiday by caroling around Toontown for a "cool" reward!'),
    59: ('Dia dos namorados ', ' Dia dos namorados de Junho 05 a Junho 14!'),
    72: ('Invas\xc3\xa3o de Sim', 'Impe\xc3\xa7a que os Cogs Sim invadam Toontown!'),
    73: ('Invas\xc3\xa3o de Mesquinhos', 'Impe\xc3\xa7a que os Cogs Mesquinhos invadam Toontown!'),
    74: ('Invas\xc3\xa3o de Telemarqueteiros', 'Impe\xc3\xa7a que os Cogs Telemarqueteiros invadam Toontown!'),
    75: ('Invas\xc3\xa3o de Ca\xc3\xa7adores de Talentos', 'Impe\xc3\xa7a que os Cogs Ca\xc3\xa7adores de Talentos invadam Toontown!'),
    76: ('Invas\xc3\xa3o de Rela\xc3\xa7\xc3\xb5es P\xc3\xbablicas', 'Impe\xc3\xa7a que os Cogs Rela\xc3\xa7\xc3\xb5es P\xc3\xbablicas invadam Toontown!'),
    77: ('Invas\xc3\xa3o de Sacos de Dinheiro', 'Impe\xc3\xa7a que os Cogs Sacos de Dinheiro invadam Toontown!'),
    78: ('Invas\xc3\xa3o de Duas Caras', 'Impe\xc3\xa7a que os Cogs Duas Caras invadam Toontown!'),
    79: ('Invas\xc3\xa3o de Soci\xc3\xa1veis', 'Impe\xc3\xa7a que os Cogs Soci\xc3\xa1veis invadam Toontown!'),
    80: ('Invas\xc3\xa3o de Agiotas', 'Impe\xc3\xa7a que os Cogs Agiotas invadam Toontown!'),
    81: ('Invas\xc3\xa3o de Especuladores', 'Impe\xc3\xa7a que os Cogs Especuladores invadam Toontown!'),
    82: ('Invas\xc3\xa3o de Industriais', 'Impe\xc3\xa7a que os Cogs Industriais invadam Toontown!'),
    83: ('Invas\xc3\xa3o de Juristas', 'Impe\xc3\xa7a que os Cogs Juristas invadam Toontown!'),
    84: ('Invas\xc3\xa3o de Peruc\xc3\xb5es', 'Impe\xc3\xa7a que os Cogs Peruc\xc3\xb5es invadam Toontown!'),
    85: ('Invas\xc3\xa3o de Queij\xc3\xb5es', 'Impe\xc3\xa7a que os Cogs Queij\xc3\xb5es invadam Toontown!'),
    86: ('Invas\xc3\xa3o de Diminuidores', 'Impe\xc3\xa7a que os Cogs Diminuidores invadam Toontown!'),
    87: ('Invas\xc3\xa3o de Agitadores', 'Impe\xc3\xa7a que os Cogs Agitadores invadam Toontown!'),
    88: ('Invas\xc3\xa3o de Incoerentes', 'Impe\xc3\xa7a que os Cogs Incoerentes invadam Toontown!'),
    89: ('Invas\xc3\xa3o de Sovinas', 'Impe\xc3\xa7a que os Cogs Sovinas invadam Toontown!'),
    90: ('Invas\xc3\xa3o de Fanfarr\xc3\xb5es', 'Impe\xc3\xa7a que os Cogs Fanfarr\xc3\xb5es invadam Toontown!'),
    91: ('Invas\xc3\xa3o de Perseguidores de Ambul\xc3\xa2ncia', 'Impe\xc3\xa7a que os Cogs Perseguidores de Ambul\xc3\xa2ncia invadam Toontown!'),
    92: ('Invas\xc3\xa3o de Microgerentes', 'Impe\xc3\xa7a que os Cogs Microgerentes invadam Toontown!'),
    93: ('Invas\xc3\xa3o de Contadores', 'Impe\xc3\xa7a que os Cogs Contadores invadam Toontown!'),
    95: ('Festas da vit\xc3\xb3ria', 'Comemore nosso triunfo hist\xc3\xb3rico contra os Cogs!'),
    96: ('Opera\xc3\xa7\xc3\xa3o: Tormenta Sellbot', 'Sellbot HQ est\xc3\xa1 aberto para todos. Vamos lutar com o Presidente!'),
    97: ('Dias de Balinha em Dobro - Jogos de Bonde', ''),
    98: ('Dias de Balinha em Dobro - Jogos de Bonde', ''),
    99: ('Dias de Balinha em Dobro - Jogos de Grupo', ''),
    101: ('Maratona de Ano-Novo dos Toons', 'Chances de vencer a toda hora! ') }
UnknownHoliday = 'Feriado Desconhecido %d'
HolidayFormat = '%m/%d '
TimeZone = 'Brazil/West'
CogdoMemoGuiTitle = 'Memos:'
CogdoMemoNames = 'Barrel-Destruction Memos'
CogdoStomperName = 'Stomp-O-Matic'
BoardroomGameTitle = 'Boardroom Hijinks'
BoardroomGameInstructions = 'The COGS are having a meeting to decide what to do with stolen gags. Slide on through and grab as many gag-destruction memos as you can!'
CogdoCraneGameTitle = 'Vend-A-Stomper'
CogdoCraneGameInstructions = 'The COGS are using a coin-operated machine to destroy laff barrels. Use the cranes to pick up and throw money bags, in order to prevent barrel destruction!'
CogdoGamePickupCount = 'Memos Collected: %i'
CogdoMazeGameTitle = 'Moving & Shaking Dept.'
CogdoMazeGameInstructions = 'The big Mover & Shaker Cogs have the code to open the door. Defeat them with your water balloons in order to get it!'
CogdoMazeIntroMovieDialogue = (("This should give you Toons a shiver! We're powering our offices with your Laff, and you're powerless to stop us!", "This will make you Toons quake! We're destroying barrels of your Laff, and you cannot stop us!", "This may come as an aftershock, but we're crushing barrels of Toon Laff in our %s, and there's nothing you can do about it!" % CogdoStomperName), ("Don't get rattled, Toons! Fill your water balloons, splash the BIG Cogs, and retrieve the PASS CODE that opens the exit! Good luck from the Toon Resistance!", 'Are you ready to rumble, Toons? Go to the water coolers and fill up balloons to throw at Cogs. Hit the BIG Cogs to get the pass code for the exit! Toon Resistance out!', 'Want some good vibrations?  Fill your balloons at the water coolers, splash the BIG Movers & Shakers, complete the PASS CODE, and find the way out! Good luck, Toons!'), ("Hmph!  I'm a Silver Sprocket Award winner, I don't need this!", "You're on shaky ground, Toons!", "Before you know it, you'll all be trembling!"))
CogdoMazeGameDoorOpens = "The Pass Code opened the Exit!\nGet there before it's too late!"
CogdoMazeGameLocalToonFoundExit = 'This Exit will open when\nyou get the Pass Code from the Big Cogs!'
CogdoMazeGameWaitingForToons = 'Waiting for %d other Toons...'
CogdoMazeGameTimeOut = 'Oh No! Time ran out!\nYou lost your Memos!'
CogdoMazeGameBossGuiTitle = 'Pass Code:'
CogdoMazeFindHint = 'Find a Water Cooler!'
CogdoMazeThrowHint = "Press 'Ctrl' to throw your water balloon!"
CogdoMazeSquashHint = 'Careful! Falling objects pop your balloon!'
CogdoMazeBossHint = 'Big Cogs take %i hits to take them down!'
CogdoMazeMinionHint = 'Minions will drop bonus Memos!'
CogdoFlyingGameTitle = 'Legal Eagle Offices'
CogdoFlyingGameInstructions = "Fly through the Legal Eagles' lair. Watch out for obstacles and cogs along the way, and don't forget to refuel your helicopter!"
CogdoFlyingIntroMovieDialogue = (("You won't ruffle our feathers, Toons! We're destroying barrels of your Laff, and you cannot stop us!", "A flock of Toons! We're crushing barrels of your Laff in our %s, and there's nothing you can do about it!" % CogdoStomperName, "You can't egg us on, Toons! We're powering our offices with your Laff, and you're powerless to stop us!"), ('This is the Toon Resistance! A little bird told me you can use propellers to fly around, grab Barrel Destruction Memos, and keep Laff from being destroyed! Good luck, Toons!', 'Attention Toons! Wing it with a propeller and collect Barrel Destruction Memos to keep our Laff from being stomped! Toon Resistance out!', 'Toon Resistance here! Cause a flap by finding propellers, flying to the Barrel Destruction Memos, and keeping our Laff from being smashed! Have fun!'), ("Squawk! I'm a Silver Sprocket Award winner, I don't need this!", 'Do your best, Toons! You will find us to be quite talon-ted!', "We'll teach you to obey the pecking order, Toons!"))
CogdoFlyingGameWaiting = 'Waiting for other Toons%s'
CogdoFlyingGameFuelLabel = 'Fuel'
CogdoFlyingGameLegalEagleTargeting = 'A Legal Eagle has noticed you!'
CogdoFlyingGameLegalEagleAttacking = 'Incoming Eagle!'
CogdoFlyingGamePickUpAPropeller = 'You need a propeller to fly!'
CogdoFlyingGamePressCtrlToFly = "Press 'Ctrl' to fly up!"
CogdoFlyingGameYouAreInvincible = 'Red Tape protects you!'
CogdoFlyingGameTimeIsRunningOut = 'Time is running out!'
CogdoFlyingGameMinimapIntro = 'This meter shows your progress!\nX marks the finish line.'
CogdoFlyingGameMemoIntro = 'Memos prevent Laff Barrels in\nthe Stomper Room from being destroyed!'
CogdoFlyingGameOutOfTime = 'Oh No! You ran out of time!'
CogdoFlyingGameYouMadeIt = 'You made it on time!'
CogdoFlyingGameYouMadeIt = 'Good work, you made it on time!'
CogdoFlyingGameTakingMemos = 'The legal eagles took all your memos!'
CogdoElevatorRewardLaff = 'Great job, Toons! You get a Laff Boost from the jokes you saved!'
CogdoExecutiveSuiteTitle = 'Executive Suite'
CogdoExecutiveSuiteIntroMessage = "Oh no, they've got the shop keeper! Defeat the Cogs and free the captive!"
CogdoExecutiveSuiteToonThankYou = 'Thanks for the rescue!\x7If you need help in a fight, use this SOS card to call my friend %s!'
CogdoExecutiveSuiteToonBye = 'Bye now!'
SillySurgeTerms = {
    1: 'Ascens\xc3\xa3o Divertida! ',
    2: 'Onda de Bobagem! ',
    3: 'Aumento Rid\xc3\xadculo! ',
    4: 'Crescimento de Risadinha! ',
    5: 'Est\xc3\xadmulo Engra\xc3\xa7ado! ',
    6: 'Impulso Raro!',
    7: 'Escalada Doida!',
    8: 'Salto Feliz!',
    9: 'Levantamento Insano!',
    10: 'Caminhada Alegre! ',
    11: 'Aumento Insano!',
    12: 'Aumento For\xc3\xa7ado! ' }
InteractivePropTrackBonusTerms = {
    0: 'Super Toon-Up',
    1: '',
    2: '',
    3: '',
    4: 'Superarremesso',
    5: 'Superesguicho!',
    6: '' }
PlayingCardUnknown = 'Nome de Cart\xc3\xa3o desconhecido'
AllTrickOrTreatFounded = 'Doces ou travessuras'
TrickOrTreatScavengerHuntCompleted = 'Doces ou travessuras'

