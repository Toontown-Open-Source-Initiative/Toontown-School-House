import string
from otp.otpbase.OTPLocalizer_portuguese_Property import *
from OTPGlobals import *

lTheBrrrgh = 'O Brrrgh'
lDaisyGardens = 'Jardim da Margarida'
lDonaldsDock = 'Porto do Donald'
lDonaldsDreamland = 'Sonhol\xc3\xa2ndia do Donald'
lMinniesMelodyland = 'Melodil\xc3\xa2ndia da Minnie'
lToontownCentral = 'Centro de Toontown'
lGoofySpeedway = 'Aut\xc3\xb3dromo do Pateta'
lOutdoorZone = 'Bosque de Bolotas de Tico e Teco'
lGolfZone = 'Minigolfe de Tico e Teco'
lCancel = 'Cancelar'
lClose = 'Fechar'
lOK = 'OK'
lNext = 'Pr\xc3\xb3ximo'
lNo = 'N\xc3\xa3o'
lQuit = 'Sair'
lYes = 'Sim'
Cog = 'Cog'
Cogs = 'Cogs'
DialogOK = lOK
DialogCancel = lCancel
DialogYes = lYes
DialogNo = lNo
DialogDoNotShowAgain = 'N\xc3\xa3o\nExibir de Novo'
WhisperNoLongerFriend = '%s saiu da sua lista de amigos.'
WhisperNowSpecialFriend = '%s agora \xc3\xa9 seu amigo secreto!'
WhisperComingToVisit = '%s est\xc3\xa1 vindo visitar voc\xc3\xaa.'
WhisperFailedVisit = '%s tentou visitar voc\xc3\xaa.'
WhisperTargetLeftVisit = '%s foi para algum outro lugar. Tente novamente!'
WhisperGiveupVisit = '%s n\xc3\xa3o conseguiu encontr\xc3\xa1-lo porque voc\xc3\xaa est\xc3\xa1 se movendo!'
WhisperIgnored = '%s est\xc3\xa1 ignorando voc\xc3\xaa!'
TeleportGreeting = 'Oi, %s.'
WhisperFriendComingOnline = '%s est\xc3\xa1 entrando on-line!'
WhisperFriendLoggedOut = '%s fez logout.'
WhisperPlayerOnline = '%s on-line em %s'
WhisperPlayerOffline = '%s est\xc3\xa1 off-line.'
WhisperUnavailable = 'Aquele jogador j\xc3\xa1 n\xc3\xa3o est\xc3\xa1 dispon\xc3\xadvel para cochichos.'
DialogSpecial = 'ooo'
DialogExclamation = '!'
DialogQuestion = '?'
ChatInputNormalSayIt = 'Dizer'
ChatInputNormalCancel = lCancel
ChatInputNormalWhisper = 'Cochichar'
ChatInputWhisperLabel = 'Com %s'
SCEmoteNoAccessMsg = 'Voc\xc3\xaa n\xc3\xa3o tem acesso\na esta emo\xc3\xa7\xc3\xa3o ainda.'
SCEmoteNoAccessOK = lOK
ParentLogin = 'Login de Pais'
ParentPassword = 'Senha conta de pais'
ChatGarblerDefault = ['bl\xc3\xa1']
ChatManagerChat = 'Chat'
ChatManagerWhisperTo = 'Cochichar com:'
ChatManagerWhisperToName = 'Cochichar com:\n%s'
ChatManagerCancel = lCancel
ChatManagerWhisperOffline = '%s est\xc3\xa1 off-line.'
OpenChatWarning = 'Para se tornar Amigo secreto de algu\xc3\xa9m, clique na pessoa e selecione "Amigos Secretos" no painel de detalhes.\n\nO recurso Chat r\xc3\xa1pido Plus pode tamb\xc3\xa9m estar ativado, qual permite us\xc3\xa1rios para bater um papo por digitando palavras encontrado no Dicion\xc3\xa1rio Chat R\xc3\xa1pido Plus.\n\nPara ativar este recurso ou para aprender mais sobre ele, saia de Toontown e clique em "Op\xc3\xa7\xc3\xb5es da conta" na p\xc3\xa1gina da web de Toontown.  '
OpenChatWarningOK = lOK
UnpaidChatWarning = 'Depois que voc\xc3\xaa assinar o servi\xc3\xa7o, poder\xc3\xa1 ativar este bot\xc3\xa3o para conversar com seus amigos usando o teclado. At\xc3\xa9 l\xc3\xa1, voc\xc3\xaa deve conversar com os outros Toons usando o Chat r\xc3\xa1pido.'
UnpaidChatWarningPay = 'Assine j\xc3\xa1!'
UnpaidChatWarningContinue = 'Continuar avalia\xc3\xa7\xc3\xa3o gratuita'
PaidNoParentPasswordWarning = 'Use este bot\xc3\xa3o para conversar com seus amigos usando o teclado, ative-o atrav\xc3\xa9s das suas Op\xc3\xa7\xc3\xb5es de Contas no site de Toontown. At\xc3\xa9 l\xc3\xa1, voc\xc3\xaa pode conversar por usando o Chat r\xc3\xa1pido '
UnpaidNoParentPasswordWarning = 'Este \xc3\xa9 para o recurso Chat R\xc3\xa1pido Plus, qual permite us\xc3\xa1rios para bater um papo por digitando palavras encontradas no Dicion\xc3\xa1rio Chat R\xc3\xa1pido Plus da Disney. Para ativar este recurso ou para aprender mais sobre ele, saia de Toontown e clique em "Op\xc3\xa7\xc3\xb5es da conta" na p\xc3\xa1gina da web de Toontown.'
PaidNoParentPasswordWarningSet = 'Atualizar Op\xc3\xa7\xc3\xb5es de Chat'
PaidNoParentPasswordWarningContinue = 'Continuar jogando'
PaidParentPasswordUKWarning = 'Depois que o Chat estiver ativado, voc\xc3\xaa poder\xc3\xa1 usar este bot\xc3\xa3o para conversar com seus amigos usando o teclado. At\xc3\xa9 l\xc3\xa1, voc\xc3\xaa deve conversar com os outros Toons usando o Chat r\xc3\xa1pido.'
PaidParentPasswordUKWarningSet = 'Ativar Chat agora!'
PaidParentPasswordUKWarningContinue = 'Continuar jogando'
NoSecretChatWarningTitle = 'Controles dispon\xc3\xadveis aos pais'
NoSecretChatWarning = 'Para conversar com um amigo, o recurso Amigos secretos deve estar ativado. As crian\xc3\xa7as precisam que seus pais visitem o site de Toontown para conhecer o recurso Amigos Secretos.'
RestrictedSecretChatWarning = 'Para pegar ou digitar um c\xc3\xb3digo secreto, fa\xc3\xa7a login com a conta de pais. Voc\xc3\xaa pode desativar esta solicita\xc3\xa7\xc3\xa3o alterando as suas op\xc3\xa7\xc3\xb5es de Amigos secretos.'
NoSecretChatWarningOK = lOK
NoSecretChatWarningCancel = lCancel
NoSecretChatWarningWrongPassword = 'Esta n\xc3\xa3o \xc3\xa9 a conta de pais. Fa\xc3\xa7a login com a conta de pais que \xc3\xa9 vinculada para esta conta.'
NoSecretChatAtAllTitle = 'Abrir Chat com Amigos Secretos'
NoSecretChatAtAll = 'O recurso Abrir Chat com Amigos Secretos permite amigos da vida-real para conversar abertamente com uns aos outros por meio de um c\xc3\xb3digo secreto que deve ser compartilhado fora do jogo\n\nPara ativar este recurso ou para aprender mais sobre ele, saia de Toontown e clique em "Op\xc3\xa7\xc3\xb5es da conta" na p\xc3\xa1gina da web de Toontown.'
NoSecretChatAtAllAndNoWhitelistTitle = 'Bot\xc3\xa3o de Chat'
NoSecretChatAtAllAndNoWhitelist = 'Voc\xc3\xaa pode usar o bot\xc3\xa3o azul de chat para se comunicar com outros Toons usando o recurso Chat R\xc3\xa1pido Plus ou o recurso Abrir Chat com Amigos Secretos.\n\nO recurso Chat r\xc3\xa1pido Plus \xc3\xa9 uma forma de tipo de chat que permitem usu\xc3\xa1rios para comunicarem por usar o dicion\xc3\xa1rio Disney Chat R\xc3\xa1pido Plus.\n\nO recurso Abrir Chat com Amigos Secretos \xc3\xa9 uma forma de tipo de chat que permite amigos da vida-real para conversar abertamente com uns aos outros por meio de um c\xc3\xb3digo secreto que deve ser compartilhado fora do jogo.\n\nPara ativar estes recursos ou para aprender mais sobre ele, saia de Toontown e clique em "Op\xc3\xa7\xc3\xb5es da conta" na p\xc3\xa1gina da web de Toontown.'
NoSecretChatAtAllOK = lOK
ChangeSecretFriendsOptions = 'Alterar op\xc3\xa7\xc3\xb5es de Amigos Secretos'
ChangeSecretFriendsOptionsWarning = '\nInsira a senha conta de pais para alterar suas op\xc3\xa7\xc3\xb5es de Amigos secretos.'
ActivateChatTitle = 'Op\xc3\xa7\xc3\xb5es de Amigos secretos'
WhisperToFormat = 'Para %s %s'
WhisperToFormatName = 'Para %s'
WhisperFromFormatName = '%s cochichos'
ThoughtOhterFormatName = '%s pensa'
ThoughtSelfFormatName = 'Voc\xc3\xaa pensa'
from panda3d.core import TextProperties
from panda3d.core import TextPropertiesManager
shadow = TextProperties()
shadow.setShadow(-0.025, -0.025)
shadow.setShadowColor(0, 0, 0, 1)
TextPropertiesManager.getGlobalPtr().setProperties('sombra', shadow)
red = TextProperties()
red.setTextColor(1, 0, 0, 1)
TextPropertiesManager.getGlobalPtr().setProperties('vermelho', red)
green = TextProperties()
green.setTextColor(0, 1, 0, 1)
TextPropertiesManager.getGlobalPtr().setProperties('verde', green)
yellow = TextProperties()
yellow.setTextColor(1, 1, 0, 1)
TextPropertiesManager.getGlobalPtr().setProperties('amarelo', yellow)
midgreen = TextProperties()
midgreen.setTextColor(0.2, 1, 0.2, 1)
TextPropertiesManager.getGlobalPtr().setProperties('verde-\xc3\xa1gua', midgreen)
blue = TextProperties()
blue.setTextColor(0, 0, 1, 1)
TextPropertiesManager.getGlobalPtr().setProperties('azul', blue)
white = TextProperties()
white.setTextColor(1, 1, 1, 1)
TextPropertiesManager.getGlobalPtr().setProperties('branco', white)
black = TextProperties()
black.setTextColor(0, 0, 0, 1)
TextPropertiesManager.getGlobalPtr().setProperties('preto', black)
grey = TextProperties()
grey.setTextColor(0.5, 0.5, 0.5, 1)
TextPropertiesManager.getGlobalPtr().setProperties('cinza', grey)
ActivateChat = 'O recurso Amigos Secretos permite que um membro converse com outro membro apenas por meio de um c\xc3\xb3digo secreto que deve ser comunicado fora do jogo. O recurso Amigos Secretos n\xc3\xa3o \xc3\xa9 moderado ou supervisionado.\n\nPor favor, escolha uma das op\xc3\xa7\xc3\xb5es do recurso Amigos Secretos de Toontown:\n\n      \x01shadow\x01Sem O recurso Amigos Secretos\x02 - Capacidade para fazer o recurso Amigos Secretos \xc3\xa9 desativado.\n      Isso oferece o mais alto n\xc3\xadvel de controle.\n      \x01shadow\x01O recurso Amigos Secretos restritos\x02 - Requer a senha conta de pais para fazer\n      cada novo recurso Amigo Secreto.\n\n      \x01shadow\x01O recurso Amigos Secretos irrestritos\x02 - Depois de habilitado com a senha conta de pais,\n      n\xc3\xa3o \xc3\xa9 necess\xc3\xa1rio fornecer a senha de pais para fazer cada novo\n      o recurso Amigos Secretos . \x01red\x01Esta op\xc3\xa7\xc3\xa3o n\xc3\xa3o \xc3\xa9 recomendada para menores de 13 anos.\x02\n\n\n\n\n\n\nAo ativar o recurso Amigos secretos, voc\xc3\xaa reconhece que, apesar de haver alguns riscos inerentes a ele, voc\xc3\xaa foi informado de todos os riscos mencionados aqui, concordando em aceit\xc3\xa1-los.'
ActivateChatYes = 'Atualizar'
ActivateChatNo = lCancel
ActivateChatMoreInfo = 'Mais informa\xc3\xa7\xc3\xb5es'
ActivateChatPrivacyPolicy = 'Pol\xc3\xadtica de Privacidade'
ActivateChatPrivacyPolicy_Button1A = 'Version 1'
ActivateChatPrivacyPolicy_Button1K = 'Version 1'
ActivateChatPrivacyPolicy_Button2A = 'Version 2'
ActivateChatPrivacyPolicy_Button2K = 'Version 2'
PrivacyPolicyText_1A = [' ']
PrivacyPolicyText_1K = [' ']
PrivacyPolicyText_2A = [' ']
PrivacyPolicyText_2K = [' ']
PrivacyPolicyText_Intro = [' ']
PrivacyPolicyClose = lClose
SecretFriendsInfoPanelOk = lOK
SecretFriendsInfoPanelClose = lClose
SecretFriendsInfoPanelText = ['\nO recurso Abrir chat com Amigos secretos\n\nO recurso Abrir chat com Amigos secretos ativa um membro para conversar diretamente com outro no Toontown On-line da Disney (o "Servi\xc3\xa7o") depois que os membros estabelecerem uma conex\xc3\xa3o de Amigos secretos. Quando o seu filho tentar usar o recurso Abrir chat com Amigos secretos, solicitaremos que voc\xc3\xaa insira a sua Senha conta de pais para indicar seu consentimento para que a crian\xc3\xa7a use o recurso. Esta \xc3\xa9 uma descri\xc3\xa7\xc3\xa3o detalhada do processo de cria\xc3\xa7\xc3\xa3o de uma conex\xc3\xa3o de Abrir chat com Amigos secretos entre os membros fict\xc3\xadcios chamados "Tails" e "Perninha". \n1. O respons\xc3\xa1vel por Tails e o respons\xc3\xa1vel por Perninha ativam o recurso Abrir chat com Amigos secretos inserindo suas respectivas Senhas conta de pais (a) nas \xc3\xa1reas de Op\xc3\xa7\xc3\xb5es da conta do Servi\xc3\xa7o ou (b) quando for solicitado no jogo, em uma janela pop-up de Controles dispon\xc3\xadveis aos pais.\n2. Tails pede um c\xc3\xb3digo secreto (descrito abaixo) no Servi\xc3\xa7o.', 
 '\n3. O c\xc3\xb3digo secreto de Tails \xc3\xa9 comunicado a Perninha fora do Servi\xc3\xa7o. (O c\xc3\xb3digo secreto de Tails pode ser comunicado a Perninha diretamente por Tails ou indiretamente, se Tails revelar o c\xc3\xb3digo secreto a outra pessoa.)\n4. Perninha envia o c\xc3\xb3digo secreto de Tails ao Servi\xc3\xa7o dentro de 48 horas a partir da hora em que Tails solicitou o c\xc3\xb3digo secreto ao Servi\xc3\xa7o.\n5. Em seguida, o Servi\xc3\xa7o notifica Perninha de que Tails tornou-se sua Amiga verdadeira. Da mesma forma, o Servi\xc3\xa7o notifica Tails de que Perninha tornou-se seu Amigo secreto. \n6. Tails e Perninha podem agora bater um papo aberto diretamente um com o outro at\xc3\xa9 um deles escolher cancelar o seu relacionamento como Amigo secreto, ou at\xc3\xa9 que o recurso Abrir Chat com Amigos secretos seja desativado para Tails ou Perninha por um dos respons\xc3\xa1veis. Ent\xc3\xa3o, a conex\xc3\xa3o de Amigos secretos pode ser desativada a qualquer momento: (a) por um membro, que remove o Amigo secreto de sua lista de amigos (conforme descrito no Servi\xc3\xa7o), ou (b) pelo respons\xc3\xa1vel pelo membro, que desativa o recurso Abrir chat com ', 
 '\nAmigos secretos na \xc3\xa1rea Op\xc3\xa7\xc3\xb5es da conta do Servi\xc3\xa7o, seguindo as etapas definidas no recurso.\n\nUm c\xc3\xb3digo secreto \xc3\xa9 um c\xc3\xb3digo aleat\xc3\xb3rio, gerado por computador, que \xc3\xa9 atribu\xc3\xaddo a um membro espec\xc3\xadfico. O c\xc3\xb3digo secreto precisa ser usado para ativar a conex\xc3\xa3o de Amigo secreto dentro de 48 horas a partir da hora em que o membro solicitou o c\xc3\xb3digo secreto; caso contr\xc3\xa1rio, o c\xc3\xb3digo secreto expirar\xc3\xa1 e n\xc3\xa3o poder\xc3\xa1 ser usado. Al\xc3\xa9m disso, s\xc3\xb3 se pode usar um simples c\xc3\xb3digo secreto para estabelecer uma conex\xc3\xa3o de Amigo secreto. Para fazer conex\xc3\xb5es adicionais de Amigos secretos, o membro precisar\xc3\xa1 solicitar mais c\xc3\xb3digos de Amigo secretos, um para cada Amigo secreto que quiser incluir.\n\nAs Amizades verdadeiras n\xc3\xa3o podem ser transferidas. Por exemplo, se Tails se tornar Amiga verdadeira de Perninha, e Perninha se tornar Amigo secreto de J\xc3\xa9ssica, Tails n\xc3\xa3o se tornar\xc3\xa1 automaticamente Amiga verdadeira de J\xc3\xa9ssica. Para que Tails e J\xc3\xa9ssica\n',
 "\nse tornem Amigas verdadeiras, uma delas ter\xc3\xa1 que solicitar um novo c\xc3\xb3digo secreto ao Servi\xc3\xa7o e comunicar \xc3\xa0 outra.\n\nOs Amigos secretos se comunicam entre si por meio de uma conversa interativa em formato livre. O conte\xc3\xbado da conversa \xc3\xa9 inserido diretamente pelo membro participante e \xc3\xa9 processado pelo Servi\xc3\xa7o, cuja opera\xc3\xa7\xc3\xa3o \xc3\xa9 realizada pelo Walt Disney Internet Group ('WDIG'), 500 S. Buena Vista St., Burbank, CA 91521-7691.  Embora aconselhamos os membros n\xc3\xa3o trocarem informa\xc3\xa7\xc3\xb5es pessoais como nome e sobrenome, e-mails, endere\xc3\xa7o postal ou n\xc3\xbameros de telefone ao usarem o recurso Abrir Chat com Amigos secretos, n\xc3\xa3o podemos garantir que os membros seguir\xc3\xa3o a recomenda\xc3\xa7\xc3\xa3o e que tais informa\xc3\xa7\xc3\xb5es sejam preservadas. Embora o chat Amigos secretos seja automaticamente filtrado para maioria dos palavr\xc3\xb5es, Abrir chat com amigos secretos pode ser moderado e a Disney reserva-se o direito de moderar qualquer parte do Servi\xc3\xa7o que a Disney,\n",
 '\na seu exclusivo e absoluto crit\xc3\xa9rio, julgar necess\xc3\xa1rio. No entanto, como Abrir chat com Amigos secretos nem sempre ser\xc3\xa1 moderado, se a conta de pais deixarem seus filhos usarem a conta com o recurso Abrir chat com Amigos secretos ativado no Servi\xc3\xa7o, aconselhamos que eles mesmos supervisionem os filhos durante a brincadeira. Ao ativar o recurso Abrir chat com Amigos secretos, a conta de pais reconhece que, apesar de haver alguns riscos inerentes ao recurso Abrir chat com amigos secretos, a conta de pais foi informada de todos os riscos mencionados aqui, concordando em aceit\xc3\xa1-los, seja previs\xc3\xadvel ou n\xc3\xa3o. \n\nO WDIG n\xc3\xa3o usa o conte\xc3\xbado do chat Amigos secretos para nenhum fim que n\xc3\xa3o seja a comunica\xc3\xa7\xc3\xa3o do conte\xc3\xbado ao amigo secreto do membro, e n\xc3\xa3o revela tal conte\xc3\xbado a terceiros, exceto: (1) se exigido por lei; por exemplo, para cumprir uma ordem ',
 "\nou intima\xc3\xa7\xc3\xa3o judicial; (2) para fazer com que os Termos de Uso aplic\xc3\xa1veis ao Servi\xc3\xa7o (que podem ser acessados na p\xc3\xa1gina principal do Servi\xc3\xa7o) sejam respeitados; ou (3) para proteger a seguran\xc3\xa7a dos Membros do Servi\xc3\xa7o e o Servi\xc3\xa7o propriamente dito. Mediante solicita\xc3\xa7\xc3\xa3o ao WDIG, o respons\xc3\xa1vel por uma crian\xc3\xa7a-membro pode analisar e mandar apagar qualquer conte\xc3\xbado do recurso de chat Amigos secretos fornecidos pela crian\xc3\xa7a em quest\xc3\xa3o, desde que tal conte\xc3\xbado j\xc3\xa1 n\xc3\xa3o tenha sido exclu\xc3\xaddo dos registros pelo WDIG. Obedecendo \xc3\xa0 Children's Online Privacy Protection Act, uma lei americana de prote\xc3\xa7\xc3\xa3o \xc3\xa0 privacidade on-line para as crian\xc3\xa7as, estamos proibidos de condicionar a participa\xc3\xa7\xc3\xa3o da crian\xc3\xa7a em qualquer tipo de atividade (inclusive o recurso Abrir chat com Amigos secretos) ao fornecimento, por parte da crian\xc3\xa7a, de mais informa\xc3\xa7\xc3\xb5es pessoais do que o estritamente necess\xc3\xa1rio para que ela participe de tais atividades.\n\nAl\xc3\xa9m disso, conforme observado acima, reconhecemos o direito do respons\xc3\xa1vel pela crian\xc3\xa7a de n\xc3\xa3o permitir que continuemos a deixar que a crian\xc3\xa7a use o recurso Amigos secretos. Ao ativar o recurso Abrir chat com Amigos secretos, voc\xc3\xaa reconhece que h\xc3\xa1 alguns riscos inerentes ao chat aberto, no qual os membros podem conversar uns com os outros usando o recurso Abrir chat com Amigos secretos, sendo que voc\xc3\xaa foi informado de todos os riscos mencionados aqui, concordando em aceit\xc3\xa1-los, seja previs\xc3\xadvel ou n\xc3\xa3o.\n"]
LeaveToPay = 'Clica comprar para sair do jogo e compra um Seja um Super Toon no site Toontown.com.br'
LeaveToPayYes = 'Comprar'
LeaveToPayNo = lCancel
LeaveToSetParentPassword = 'Para configurar a Senha conta de pais, o jogo sair\xc3\xa1 para Toontown.com.br'
LeaveToSetParentPasswordYes = 'Definir senha'
LeaveToSetParentPasswordNo = lCancel
LeaveToEnableChatUK = 'Para ativar o chat, o jogo sair\xc3\xa1 para o site Toontown.'
LeaveToEnableChatUKYes = 'Ativar chat'
LeaveToEnableChatUKNo = lCancel
ChatMoreInfoOK = lOK
SecretChatDeactivated = 'O recurso "Amigos secretos" foi desativado.'
RestrictedSecretChatActivated = 'O recurso "Amigos secretos restritos" foi ativado!'
SecretChatActivated = 'O recurso "Amigos secretos irrestritos" foi ativado!\n\nSe voc\xc3\xaa mudar de id\xc3\xa9ia e decidir desativar este recurso mais tarde, clique em "Op\xc3\xa7\xc3\xb5es da conta" na p\xc3\xa1gina da web de Toontown.'
SecretChatActivatedOK = lOK
SecretChatActivatedChange = 'Alterar Op\xc3\xa7\xc3\xb5es'
ProblemActivatingChat = 'Ops! N\xc3\xa3o foi poss\xc3\xadvel ativar o recurso de chat "Amigos secretos".\n\n%s\n\nTente novamente mais tarde.'
ProblemActivatingChatOK = lOK
MultiPageTextFrameNext = lNext
MultiPageTextFramePrev = 'Anterior'
MultiPageTextFramePage = 'P\xc3\xa1gina %s/%s'
GuiScreenToontownUnavailable = 'O servidor parece estar temporariamente indispon\xc3\xadvel, ainda tentando...'
GuiScreenCancel = lCancel
CreateAccountScreenUserName = 'Nome da conta'
CreateAccountScreenPassword = 'Senha'
CreateAccountScreenConfirmPassword = 'Confirmar senha'
CreateAccountScreenCancel = lCancel
CreateAccountScreenSubmit = 'Enviar'
CreateAccountScreenConnectionErrorSuffix = '.\n\nTente novamente mais tarde.'
CreateAccountScreenNoAccountName = 'Insira o nome da conta.'
CreateAccountScreenAccountNameTooShort = 'O nome da conta deve ter, pelo menos, %s caracteres. Tente novamente.'
CreateAccountScreenPasswordTooShort = 'A senha deve ter, pelo menos, %s caracteres. Tente novamente.'
CreateAccountScreenPasswordMismatch = 'As senhas inseridas n\xc3\xa3o combinam. Tente novamente.'
CreateAccountScreenUserNameTaken = 'Este nome de usu\xc3\xa1rio j\xc3\xa1 existe. Tente novamente.'
CreateAccountScreenInvalidUserName = 'Nome de usu\xc3\xa1rio inv\xc3\xa1lido.\nTente novamente.'
CreateAccountScreenUserNameNotFound = 'Nome de usu\xc3\xa1rio n\xc3\xa3o encontrado.\nTente novamente ou crie uma nova conta.'
CRConnecting = 'Conectando...'
CRNoConnectTryAgain = 'N\xc3\xa3o foi poss\xc3\xadvel conectar-se a %s:%s. Tentar novamente?'
CRNoConnectProxyNoPort = 'N\xc3\xa3o foi poss\xc3\xadvel conectar-se a %s:%s.\n\nVoc\xc3\xaa est\xc3\xa1 se comunicando com a Internet por via proxy, mas o seu proxy n\xc3\xa3o permite conex\xc3\xb5es na porta %s.\n\nVoc\xc3\xaa deve abrir esta porta, ou desativar o proxy, para poder jogar na Toontown. Se o proxy foi fornecido pelo seu provedor, \xc3\xa9 preciso entrar em contato com ele para abrir esta porta.'
CRMissingGameRootObject = 'H\xc3\xa1 alguns objetos do jogo raiz ausentes. (A causa pode ser uma conex\xc3\xa3o de rede com falhas). Saindo do jogo.'
CRNoDistrictsTryAgain = 'N\xc3\xa3o h\xc3\xa1 Regi\xc3\xb5es de Toontown dispon\xc3\xadveis. Tentar novamente?'
CRRejectRemoveAvatar = 'O Toon n\xc3\xa3o p\xc3\xb4de ser exclu\xc3\xaddo, tente novamente mais tarde.'
CRLostConnection = 'A sua conex\xc3\xa3o de Internet \xc3\xa0 Toontown foi interrompida inesperadamente.'
CRBootedReasons = {
 BootedUnexpectedProblem: 'Houve um problema inesperado. A conex\xc3\xa3o falhou, mas voc\xc3\xaa ainda deve conseguir se conectar novamente e voltar ao jogo.',
 BootedLoggedInElsewhere: 'Voc\xc3\xaa foi desconectado porque outra pessoa acabou de fazer login usando sua conta em outro computador.',
 BootedKeyboardChatAuth: 'Voc\xc3\xaa foi desconectado porque houve um problema com sua autoriza\xc3\xa7\xc3\xa3o para usar o chat de teclado.',
 BootedConnectionKilled: 'Houve um problema inesperado ao fazer login na Toontown. Entre em contato com o suporte ao Cliente da Toontown.',
 BootedVersionMismatch: 'Voc\xc3\xaa est\xc3\xa1 executando uma vers\xc3\xa3o do jogo diferente da vers\xc3\xa3o do host do servidor. Se voc\xc3\xaa acabou de atualizar seu jogo, pe\xc3\xa7a ao host do servidor para atualizar e reiniciar o servidor.',
 BootedFileMismatch: 'Os arquivos da Toontown que voc\xc3\xaa tem instalados parecem ser inv\xc3\xa1lidos. Se voc\xc3\xaa receber esse erro repetidamente, o host do servidor provavelmente est\xc3\xa1 executando uma vers\xc3\xa3o diferente do jogo.',
 BootedNoAdminPrivileges: 'Voc\xc3\xaa n\xc3\xa3o est\xc3\xa1 autorizado a usar privil\xc3\xa9gios de administrador.',
 BootedToonIssue: 'Ocorreu um problema com seu Toon. Entre em contato com o suporte do Toontown Online.',
 BootedKickedForMaintenance: 'Voc\xc3\xaa foi desconectado por um administrador que trabalha nos servidores.',
 BootedBanned: "Foi relatada uma viola\xc3\xa7\xc3\xa3o das regras deste servidor conectada a '%(name)s'. Voc\xc3\xaa foi banido.",
 BootedDistrictReset: 'A regi\xc3\xa3o de Toontown em que voc\xc3\xaa estava jogando foi reiniciada. Todos as pessoas que estavam jogando nesta regi\xc3\xa3o foram desconectadas. Entretanto, voc\xc3\xaa poder\xc3\xa1 conectar-se novamente e voltar direto ao jogo.',
 BootedOutOfTime: 'Desculpe, voc\xc3\xaa ficou sem tempo para jogar.'
}
CRBootedReasonUnknownCode = 'Houve um problema inesperado (c\xc3\xb3digo de erro %s). A conex\xc3\xa3o falhou, mas voc\xc3\xaa ainda deve conseguir conectar-se novamente para voltar ao jogo.'
CRBootedAdditionalInfo = '\n\nInforma\xc3\xa7\xc3\xb5es adicionais\n{}'
CRTryConnectAgain = '\n\nTentar conectar-se novamente?'
CRToontownUnavailable = 'O servidor parece estar temporariamente indispon\xc3\xadvel, ainda tentando...'
CRToontownUnavailableCancel = lCancel
CRNameCongratulations = 'PARAB\xc3\x89NS!!'
CRNameAccepted = 'O seu nome foi\naprovado pelo Conselho de Toons.\n\nA partir de agora,\nvoc\xc3\xaa ter\xc3\xa1 o nome\n\'%s\''
CRServerConstantsProxyNoPort = 'N\xc3\xa3o foi poss\xc3\xadvel contatar %s.\n\nVoc\xc3\xaa est\xc3\xa1 se comunicando com a Internet por via proxy, mas o seu proxy n\xc3\xa3o permite conex\xc3\xb5es na porta %s.\n\nVoc\xc3\xaa deve abrir esta porta, ou desativar o proxy, para poder jogar na Toontown. Se o proxy foi fornecido pelo seu provedor, \xc3\xa9 preciso entrar em contato com ele para abrir esta porta.'
CRServerConstantsProxyNoCONNECT = 'N\xc3\xa3o foi poss\xc3\xadvel contatar %s.\n\nVoc\xc3\xaa est\xc3\xa1 se comunicando com a Internet por via proxy, mas o seu proxy n\xc3\xa3o permite o m\xc3\xa9todo CONECTAR.\n\nVoc\xc3\xaa deve ativar este recurso, ou desativar o proxy, para poder jogar na Toontown. Se o proxy foi fornecido pelo seu provedor, \xc3\xa9 preciso entrar em contato com ele para abrir esta porta.'
CRServerConstantsTryAgain = 'N\xc3\xa3o foi poss\xc3\xadvel contatar %s.\n\nO servidor de contas da Toontown deve estar temporariamente fora do ar ou deve haver algum problema na conex\xc3\xa3o de Internet.\n\nTentar novamente?'
CRServerDateTryAgain = 'N\xc3\xa3o foi poss\xc3\xadvel obter a data do servidor de %s. Tentar novamente?'
AfkForceAcknowledgeMessage = 'O seu Toon ficou com sono e foi para a cama.'
PeriodTimerWarning = 'O seu limite de tempo em Toontown neste m\xc3\xaas est\xc3\xa1 quase no fim!'
PeriodForceAcknowledgeMessage = 'Desculpe, voc\xc3\xaa usou todo o seu tempo dispon\xc3\xadvel. Por favor, saia para comprar mais.'
CREnteringToontown = 'Entrando em Toontown...'
DownloadWatcherUpdate = 'Fazendo o download de %s'
DownloadWatcherInitializing = 'Inicializando Download...'
LoginScreenUserName = 'Nome da Conta'
LoginScreenPassword = 'Senha'
LoginScreenLogin = 'Login'
LoginScreenCreateAccount = 'Criar Conta'
LoginScreenQuit = lQuit
LoginScreenLoginPrompt = 'Por favor, digite um nome de usu\xc3\xa1rio e uma senha.'
LoginScreenBadPassword = 'Senha errada.\nTente novamente.'
LoginScreenInvalidUserName = 'Nome de usu\xc3\xa1rio inv\xc3\xa1lido.\nTente novamente.'
LoginScreenUserNameNotFound = 'Nome de usu\xc3\xa1rio n\xc3\xa3o encontrado.\nTente novamente ou crie uma nova conta.'
LoginScreenPeriodTimeExpired = 'Sinto muito, mas voc\xc3\xaa j\xc3\xa1 usou todos os seus minutos dispon\xc3\xadveis deste m\xc3\xaas. Volte no in\xc3\xadcio do pr\xc3\xb3ximo m\xc3\xaas.'
LoginScreenNoNewAccounts = 'Sinto muito, no momento n\xc3\xa3o estamos aceitando novas contas.'
LoginScreenTryAgain = 'Tente novamente'
DialogSpecial = 'ooo'
DialogExclamation = '!'
DialogQuestion = '?'
DialogLength1 = 6
DialogLength2 = 12
DialogLength3 = 20
GlobalSpeedChatName = 'Chat r\xc3\xa1pido'
SCMenuPromotion = 'PROMOCIONAL'
SCMenuElection = 'ESCOLHA'
SCMenuEmotions = 'EMO\xc3\x87\xc3\x95ES'
SCMenuCustom = 'MINHAS FRASES'
SCMenuResistance = 'UNIR!'
SCMenuPets = 'BICHINHOS'
SCMenuPetTricks = 'TRUQUES'
SCMenuCog = 'FALAS DE COGS'
SCMenuHello = 'OL\xc3\x81'
SCMenuBye = 'TCHAU'
SCMenuHappy = 'FELIZ'
SCMenuSad = 'TRISTE'
SCMenuFriendly = 'AMIG\xc3\x81VEL'
SCMenuSorry = 'DESCULPE'
SCMenuStinky = 'FEDIDO'
SCMenuPlaces = 'LUGARES'
SCMenuToontasks = 'TAREFAS TOON'
SCMenuBattle = 'BATALHA'
SCMenuGagShop = 'LOJA DE PIADAS'
SCMenuFactory = 'F\xc3\x81BRICA'
SCMenuKartRacing = 'CORRIDA'
SCMenuFactoryMeet = 'ENCONTRO'
SCMenuCFOBattle = 'DIRETOR FINANCEIRO'
SCMenuCFOBattleCranes = 'GUINDASTES'
SCMenuCFOBattleGoons = 'BRUTAMONTES'
SCMenuCJBattle = 'JUIZ-CHEFE'
SCMenuCEOBattle = 'PRESIDENTE'
SCMenuGolf = 'GOLFE'
SCMenuWhiteList = 'LISTA DE PERMISS\xc3\x95ES'
SCMenuPlacesPlayground = 'P\xc3\x81TIO'
SCMenuPlacesEstate = 'PROPRIEDADE'
SCMenuPlacesCogs = 'COGS'
SCMenuPlacesWait = 'ESPERE'
SCMenuFriendlyYou = 'Voc\xc3\xaa...'
SCMenuFriendlyILike = 'Eu gosto de...'
SCMenuPlacesLetsGo = 'Vamos...'
SCMenuToontasksMyTasks = 'MINHAS TAREFAS'
SCMenuToontasksYouShouldChoose = 'Eu acho que voc\xc3\xaa deveria escolher...'
SCMenuToontasksINeedMore = 'Preciso de mais...'
SCMenuBattleGags = 'PIADAS'
SCMenuBattleTaunts = 'PROVOCA\xc3\x87\xc3\x95ES'
SCMenuBattleStrategy = 'ESTRAT\xc3\x89GIA'
SCMenuBoardingGroup = 'ABORDAGEM'
SCMenuParties = 'FESTAS'
SCMenuAprilToons = 'DIA DA MENTIRA TOONS'
SCMenuSingingGroup = 'CANTORIA'
SCMenuCarol = 'CANTANDO'
SCMenuSillyHoliday = 'MEDIDOR DE BOBAGEM'
SCMenuVictoryParties = 'FESTAS DA VIT\xc3\x93RIAS'
SCMenuSellbotNerf = 'TEMPESTADE DOS R\xc3\x94BOS VENDEDORES'
SCMenuJellybeanJam = 'SEMANA DAS BALINHAS'
SCMenuHalloween = 'DIAS DAS BRUXAS'
SCMenuWinter = 'INVERNO'
SCMenuSellbotInvasion = 'INVAS\xc3\x83O DOS R\xc3\x94BOS VENDEDORES'
SCMenuFieldOffice = 'ESCRIT\xc3\x93RIOS DE CAMPO'
SCMenuIdesOfMarch = 'VERDE'
FriendSecretNeedsPasswordWarningTitle = 'Controles dispon\xc3\xadveis aos pais'
FriendSecretNeedsParentLoginWarning = 'Para conseguir ou digitar um c\xc3\xb3digo secreto, um dos seus pais ou respons\xc3\xa1veis precisa fazer o login. Voc\xc3\xaa pode desativar esta pergunta alterando suas op\xc3\xa7\xc3\xb5es de Amigos Secretos.'
FriendSecretNeedsPasswordWarning = 'Para pegar ou digitar um c\xc3\xb3digo secreto, voc\xc3\xaa deve inserir a Senha conta de pais. Voc\xc3\xaa pode desativar esta solicita\xc3\xa7\xc3\xa3o alterando as suas op\xc3\xa7\xc3\xb5es de Amigos verdadadeiros.'
FriendSecretNeedsPasswordWarningOK = lOK
FriendSecretNeedsPasswordWarningCancel = lCancel
FriendSecretNeedsPasswordWarningWrongUsername = 'Esse n\xc3\xa3o \xc3\xa9 o nome de usu\xc3\xa1rio correto. Digite o nome de usu\xc3\xa1rio da conta de pais. Esse n\xc3\xa3o \xc3\xa9 o mesmo nome de usu\xc3\xa1rio que \xc3\xa9 usado para jogar.'''
FriendSecretNeedsPasswordWarningWrongPassword = 'Esta n\xc3\xa3o \xc3\xa9 a senha correta. Insira a Senha conta de pais criada na compra desta conta. N\xc3\xa3o \xc3\xa9 a mesma senha usada para os jogos.'''
FriendSecretIntro = 'Se voc\xc3\xaa estiver jogando Toontown Online da Disney com algu\xc3\xa9m que conhece no mundo real, poder\xc3\xa1 tornar-se Amigo secreto dessa pessoa. Voc\xc3\xaa pode conversar com seus Amigos secretos usando o teclado. Os outros Toons n\xc3\xa3o entender\xc3\xa3o o que voc\xc3\xaas estiverem falando.\n\nVoc\xc3\xaa pode conseguir isto obtendo um c\xc3\xb3digo secreto. Conte o c\xc3\xb3digo secreto s\xc3\xb3 ao seu amigo, e a mais ningu\xc3\xa9m. Quando o seu amigo digitar o seu c\xc3\xb3digo secreto na tela, voc\xc3\xaas dois ser\xc3\xa3o Amigos secretos em Toontown!'
FriendSecretGetSecret = 'Obter um c\xc3\xb3digo secreto'
FriendSecretEnterSecret = 'Se voc\xc3\xaa tiver um c\xc3\xb3digo secreto de algu\xc3\xa9m conhecido, digite-o aqui.'
FriendSecretOK = lOK
FriendSecretEnter = 'Inserir c\xc3\xb3digo secreto'
FriendSecretCancel = lCancel
FriendSecretGettingSecret = 'Obtendo c\xc3\xb3digo secreto. . .'
FriendSecretGotSecret = 'Este \xc3\xa9 o seu novo c\xc3\xb3digo secreto. N\xc3\xa3o deixe de anot\xc3\xa1-lo em algum lugar!\n\nVoc\xc3\xaa s\xc3\xb3 pode dar este c\xc3\xb3digo secreto a uma pessoa. Depois que algu\xc3\xa9m digitar o seu c\xc3\xb3digo secreto, ele n\xc3\xa3o funcionar\xc3\xa1 para nenhuma outra pessoa. Se voc\xc3\xaa quiser dar um c\xc3\xb3digo secreto para mais de uma pessoa, obtenha outro.\n\nO c\xc3\xb3digo secreto s\xc3\xb3 funcionar\xc3\xa1 nos pr\xc3\xb3ximos dois dias. O seu amigo ter\xc3\xa1 que digit\xc3\xa1-lo antes que expire, caso contr\xc3\xa1rio, n\xc3\xa3o funcionar\xc3\xa1.\n\nO c\xc3\xb3digo secreto \xc3\xa9:'
FriendSecretTooMany = 'Sinto muito, voc\xc3\xaa n\xc3\xa3o pode ter mais c\xc3\xb3digo secreto hoje. Voc\xc3\xaa j\xc3\xa1 obteve mais do que a parte que lhe cabia!\n\nTente novamente amanh\xc3\xa3.'
FriendSecretTryingSecret = 'Tentando usar c\xc3\xb3digo secreto. . .'
FriendSecretEnteredSecretSuccess = 'Agora, voc\xc3\xaa \xc3\xa9 Amigo secreto de %s!'
FriendSecretTimeOut = 'Sinto muitos, c\xc3\xb3digo secreto n\xc3\xa3o est\xc3\xa3o funcionando agora.'
FriendSecretTimeOutRetro = 'Sinto muitos, segredos n\xc3\xa3o est\xc3\xa3o funcionando agora.'
FriendSecretEnteredSecretUnknown = 'Este c\xc3\xb3digo secreto n\xc3\xa3o existe. Tem certeza de que digitou certo?\n\nSe voc\xc3\xaa tiver digitado certo, ele pode ter expirado. Pe\xc3\xa7a ao seu amigo para pegar outro c\xc3\xb3digo secreto para voc\xc3\xaa (ou pegue um novo voc\xc3\xaa mesmo e d\xc3\xaa ao seu amigo).'
FriendSecretEnteredSecretFull = 'Voc\xc3\xaa n\xc3\xa3o pode fazer amizade com %s porque um de voc\xc3\xaas dois possui amigos demais na lista.'
FriendSecretEnteredSecretFullNoName = 'Voc\xc3\xaas n\xc3\xa3o podem fazer amizade porque um de voc\xc3\xaas dois possui amigos demais na lista.'
FriendSecretEnteredSecretSelf = 'Voc\xc3\xaa acabou de digitar seu pr\xc3\xb3prio c\xc3\xb3digo secreto! Agora, ningu\xc3\xa9m mais poder\xc3\xa1 usar este c\xc3\xb3digo secreto.'
FriendSecretEnteredSecretWrongProduct = "Voc\xc3\xaa digitou o tipo errado de c\xc3\xb3digo secreto.\nEste jogo utiliza c\xc3\xb3digos que come\xc3\xa7am com '%s'."
FriendSecretNowFriends = 'Agora, voc\xc3\xaa \xc3\xa9 Amigo Verdadeiro de %s!'
FriendSecretNowFriendsNoName = 'Agora, voc\xc3\xaas s\xc3\xa3o Amigos secretos!'
FriendSecretDetermineSecret = 'Que tipo de Amigo Verdadeiro voc\xc3\xaa quer ter?'
FriendSecretDetermineSecretAvatar = 'Avatar'
FriendSecretDetermineSecretAvatarRollover = 'Um amigo somente neste jogo'
FriendSecretDetermineSecretAccount = 'Conta'
FriendSecretDetermineSecretAccountRollover = 'Um amigo em toda a rede Disney.com.br'
GuildMemberTitle = 'Op\xc3\xa7\xc3\xb5es de Membros'
GuildMemberPromote = 'Fazer Oficial'
GuildMemberPromoteInvite = 'Fazer Veterano'
GuildMemberDemoteInvite = 'Rebaixar para Veterano'
GuildMemberGM = 'Fazer Mestre da Guilda'
GuildMemberGMConfirm = 'Confirmado'
GuildMemberDemote = 'Rebaixar para Membro'
GuildMemberKick = 'Ejeitar Membro'
GuildMemberCancel = lCancel
GuildMemberOnline = 'tem entrado online.'
GuildMemberOffline = 'tem indo off-line.'
GuildPrefix = '(G):'
GuildNewMember = 'Novo Membro da Guilda'
GuildMemberUnknown = 'Desconhecido'
GuildMemberGMMessage = 'Aviso! Voc\xc3\xaa gostaria de desistir da lideran\xc3\xa7a da sua guilda e tornar %s seu mestre da guilda?\n\nVoc\xc3\xaa se tornar\xc3\xa1 um oficial'
GuildInviteeOK = lOK
GuildInviteeNo = lNo
GuildInviteeInvitation = '%s est\xc3\xa1 convidando voc\xc3\xaa para se juntar a %s.'
GuildRedeemErrorInvalidToken = 'Sinto muito, que o c\xc3\xb3digo est\xc3\xa1 invalido. Por Favor tente novamente.'
GuildRedeemErrorGuildFull = 'Sinto muito, esta guilda j\xc3\xa1 tem muitos membros.'
FriendInviteeTooManyFriends = '%s quer fazer amizade com voc\xc3\xaa, mas voc\xc3\xaa j\xc3\xa1 tem muitos amigos em sua lista!'
FriendInviteeInvitation = '%s quer fazer amizade com voc\xc3\xaa.'
FriendInviteeInvitationPlayer = 'O jogador de %s gostaria de ser seu amigo.'
FriendNotifictation = '%s \xc3\xa9 agora seu amigo.'
FriendInviteeOK = lYes
FriendInviteeNo = lNo
GuildInviterWentAway = '%s n\xc3\xa3o est\xc3\xa1 mais presente.'
GuildInviterAlready = '%s j\xc3\xa1 est\xc3\xa1 em uma guilda.'
GuildInviterBusy = '%s est\xc3\xa1 ocupado agora certo.'
GuildInviterNotYet = 'Convidar %s para entrar na sua guilda?'
GuildInviterCheckAvailability = 'Convidando %s para ingressar na sua guilda.'
GuildInviterOK = lOK
GuildInviterNo = lNo
GuildInviterCancel = lCancel
GuildInviterYes = lYes
GuildInviterTooFull = 'A guilda atingiu o tamanho m\xc3\xa1ximo.'
GuildInviterClickToon = 'Clique no pirata que voc\xc3\xaa deseja convidar.'
GuildInviterTooMany = 'Isto \xc3\xa9 um bug'
GuildInviterNotAvailable = '%s est\xc3\xa1 ocupado agora correto; tente novamente mais tarde.'
GuildInviterGuildSaidNo = '%s n\xc3\xa3o deseja para se juntar.'
GuildInviterAlreadyInvited = '%s j\xc3\xa1 foi convidado.'
GuildInviterEndGuildship = 'Ejetar %s da guilda?'
GuildInviterFriendsNoMore = '%s tenha sa\xc3\xaddo da guilda.'
GuildInviterSelf = 'Voc\xc3\xaa j\xc3\xa1 est\xc3\xa1 na guilda!'
GuildInviterIgnored = '%s est\xc3\xa1 ignorando voc\xc3\xaa.'
GuildInviterAsking = 'Pedindo para %s entrar na guilda.'
GuildInviterGuildSaidYes = '%s ir\xc3\xa1 participar!'
GuildInviterFriendKickedOut = '%s tenha expulsado %s da Guilda.'
GuildInviterFriendKickedOutP = '%s tenham expulsado %s da Guilda.'
GuildInviterFriendInvited = '%s tenha convidando %s para a Guilda.'
GuildInviterFriendInvitedP = '%s tenham convidados %s para a Guilda.'
GuildInviterFriendPromoted = '%s tenha promovido o %s  para o ranque de %s.'
GuildInviterFriendPromotedP = '%s tenham promovidos o %s para o ranque de %s.'
GuildInviterFriendDemoted = '%s tenha rebaixado o %s para o rank de %s.'
GuildInviterFriendDemotedP = '%s tenham rebaixado o %s para o rank de %s.'
GuildInviterFriendPromotedGM = '%s tenha nomeado o %s como o novo %s'
GuildInviterFriendPromotedGMP = '%s tenham nomearam o %s como o novo %s'
GuildInviterFriendDemotedGM = '%s foi nomeado por %s como o novo Mestre da Guilda que se tornou o ranque de %s'
GuildInviterFriendDemotedGMP = '%s foram nomeados por %s como o novo Mestre da Guilda que alcan\xc3\xa7ou o ranque de %s'
FriendOnline = 'entrou on-line.'
FriendOffline = 'saiu e est\xc3\xa1 off-line.'
FriendInviterOK = lOK
FriendInviterCancel = lCancel
FriendInviterStopBeingFriends = 'Interromper amizade'
FriendInviterConfirmRemove = 'Remova'
FriendInviterYes = lYes
FriendInviterNo = lNo
FriendInviterClickToon = 'Clique no Toon com o qual deseja fazer amizade.'
FriendInviterTooMany = 'Voc\xc3\xaa tem amigos demais na lista e n\xc3\xa3o pode adicionar mais nenhum agora. Voc\xc3\xaa ter\xc3\xa1 que remover alguns amigos se desejar fazer amizade com %s.'
FriendInviterToonTooMany = 'Voc\xc3\xaa tem amigos Tonns demais em sua lista para poder acrescentar um agora. Remova alguns amigos Tonns se quiser fazer amizade com %s.'
FriendInviterPlayerTooMany = 'Voc\xc3\xaa tem amigos jogadores demais em sua lista para poder acrescentar um agora. Remova alguns amigos jogadores se quiser fazer amizade com %s.'
FriendInviterNotYet = 'Deseja fazer amizade com %s?'
FriendInviterCheckAvailability = 'Verificando se %s est\xc3\xa1 dispon\xc3\xadvel.'
FriendInviterNotAvailable = '%s est\xc3\xa1 ocupado(a) agora; tente novamente mais tarde.'
FriendInviterCantSee = 'Isso s\xc3\xb3 funciona se voc\xc3\xaa puder ver %s.'
FriendInviterNotOnline = 'Isso s\xc3\xb3 funciona se %s estiver online'
FriendInviterNotOpen = '%s n\xc3\xa3o tem um bate-papo aberto, use segredos para fazer amigos'
FriendInviterWentAway = '%s saiu.'
FriendInviterAlready = '%s j\xc3\xa1 \xc3\xa9 seu(sua) amigo(a).'
FriendInviterAlreadyInvited = '%s j\xc3\xa1 recebeu o convite.'
FriendInviterAskingCog = 'Pedindo a %s para fazer amizade com voc\xc3\xaa.'
FriendInviterAskingPet = '%s pula \xc3\xa0 sua volta, corre em c\xc3\xadrculos e lambe seu rosto.'
FriendInviterAskingMyPet = '%s j\xc3\xa1 \xc3\xa9 seu(sua) MELHOR amigo(a).'
FriendInviterEndFriendship = 'Tem certeza de que voc\xc3\xaa deseja interromper a amizade com %s?'
FriendInviterFriendsNoMore = '%s n\xc3\xa3o \xc3\xa9 mais seu(sua) amigo(a).'
FriendInviterSelf = 'Voc\xc3\xaa j\xc3\xa1 tem amizade com voc\xc3\xaa mesmo(a)!'
FriendInviterIgnored = '%s est\xc3\xa1 ignorando voc\xc3\xaa.'
FriendInviterAsking = 'Pedindo a %s para fazer amizade com voc\xc3\xaa.'
FriendInviterFriendSaidYes = 'Agora voc\xc3\xaa \xc3\xa9 amigo de %s!'
FriendInviterPlayerFriendSaidYes = 'Agora, voc\xc3\xaa fez amizade com o jogador de %s, %s!'
FriendInviterFriendSaidNo = '%s agradece, mas disse n\xc3\xa3o.'
FriendInviterFriendSaidNoNewFriends = '%s n\xc3\xa3o est\xc3\xa1 procurando novos amigos no momento.'
FriendInviterOtherTooMany = '%s j\xc3\xa1 tem amigos demais!'
FriendInviterMaybe = '%s n\xc3\xa3o conseguiu responder.'
FriendInviterDown = 'N\xc3\xa3o foi poss\xc3\xadvel fazer amizade agora.'
TalkGuild = 'G'
TalkParty = 'P'
TalkPVP = 'PVP'
AntiSpamInChat = '***Spamming***'
IgnoreConfirmOK = lOK
IgnoreConfirmCancel = lCancel
IgnoreConfirmYes = lYes
IgnoreConfirmNo = lNo
IgnoreConfirmNotYet = 'Deseja continuar a Ignorar %s?'
IgnoreConfirmAlready = 'Voc\xc3\xaa j\xc3\xa1 est\xc3\xa1 ignorando %s.'
IgnoreConfirmSelf = 'Voc\xc3\xaa n\xc3\xa3o pode ignorar a si mesmo(a)!'
IgnoreConfirmNewIgnore = 'Voc\xc3\xaa est\xc3\xa1 ignorando %s.'
IgnoreConfirmEndIgnore = 'Voc\xc3\xaa n\xc3\xa3o est\xc3\xa1 mais ignorando %s.'
IgnoreConfirmRemoveIgnore = 'Parar de ignorar %s?'
EmoteList = ['Aceno',
 'Feliz',
 'Triste',
 'Raivoso',
 'Sonolento',
 'Dar de ombros',
 'Dan\xc3\xa7ante',
 'Piscar',
 'Entediado',
 'Palmas',
 'Surpreso',
 'Confuso',
 'Casca de Banana',
 'Saudar',
 'Muito triste',
 'Sorris\xc3\xa3o',
 'Risada',
 lYes,
 lNo,
 lOK,
 'Surpresa',
 'Choro',
 'Alegre',
 'Raiva',
 'Risada']
EmoteWhispers = ['%s acena.',
 '%s est\xc3\xa1 feliz.',
 '%s est\xc3\xa1 triste.',
 '%s est\xc3\xa1 furioso.',
 '%s est\xc3\xa1 sonolento.',
 '%s d\xc3\xa1 de ombros.',
 '%s dan\xc3\xa7a.',
 '%s pisca.',
 '%s est\xc3\xa1 entediado.',
 '%s aplaude.',
 '%s est\xc3\xa1 surpreso.',
 '%s est\xc3\xa1 confuso.',
 '%s escorregou numa casca de banana.',
 '%s sa\xc3\xbada voc\xc3\xaa.',
 '%s est\xc3\xa1 muito triste.',
 '%s sorriu.',
 '%s d\xc3\xa1 risada.',
 "%s diz '" + lYes + "'.",
 "%s diz '" + lNo + "'.",
 "%s diz '" + lOK + "'.",
 '%s se surpreende.',
 '%s est\xc3\xa1 chorando.',
 '%s est\xc3\xa1 alegre.',
 '%s est\xc3\xa1 com raiva.',
 '%s est\xc3\xa1 rindo.']
EmoteFuncDict = {'Wave': 0,
 'Happy': 1,
 'Sad': 2,
 'Angry': 3,
 'Sleepy': 4,
 'Shrug': 5,
 'Dance': 6,
 'Think': 7,
 'Bored': 8,
 'Applause': 9,
 'Cringe': 10,
 'Confused': 11,
 'Belly Flop': 12,
 'Bow': 13,
 'Banana Peel': 14,
 'Resistance Salute': 15,
 'Laugh': 16,
 lYes: 17,
 lNo: 18,
 lOK: 19,
 'Surprise': 20,
 'Cry': 21,
 'Delighted': 22,
 'Furious': 23,
 'Laugh': 24,
 'Sing Note G1': 25,
 'Sing Note A': 26,
 'Sing Note B': 27,
 'Sing Note C': 28,
 'Sing Note D': 29,
 'Sing Note E': 30,
 'Sing Note F': 31,
 'Sing Note G2': 32}
SuitBrushOffs = {'f': ['Estou atrasado para uma reuni\xc3\xa3o.'],
 'p': ['Sai fora.'],
 'ym': ['As vaquinhas de pres\xc3\xa9pio dizem N\xc3\x83O.'],
 None: ['\xc3\x89 o meu dia de folga.',
        'Acho que voc\xc3\xaa est\xc3\xa1 no escrit\xc3\xb3rio errado.',
        'Fale para o seu pessoal falar com o meu.',
        'Voc\xc3\xaa n\xc3\xa3o tem cacife para se encontrar comigo.',
        'Fale com o meu assistente.']}
SuitFaceoffTaunts = {'b': ['Voc\xc3\xaa tem uma doa\xc3\xa7\xc3\xa3o para mim?',
       'Voc\xc3\xaa vai detestar perder a parada.',
       'Voc\xc3\xaa n\xc3\xa3o vai ter salva\xc3\xa7\xc3\xa3o.',
       'Sou "A Positivo", portanto, vou ganhar.',
       '"O" n\xc3\xa3o seja t\xc3\xa3o "Negativo".',
       '\xc3\x89 uma surpresa voc\xc3\xaa ter me achado; n\xc3\xa3o tenho parada.',
       'Vou precisar fazer uma r\xc3\xa1pida contagem em voc\xc3\xaa.',
       'Em breve, voc\xc3\xaa vai precisar comer biscoito e tomar um suco.',
       'Quando eu terminar, voc\xc3\xaa vai precisar dar uma descansada.',
       'S\xc3\xb3 vai doer um pouquinho.',
       'Vou deixar voc\xc3\xaa tonto.',
       'Na hora certa, s\xc3\xb3 estou um pouquinho abaixo.'],
 'm': ['Voc\xc3\xaa n\xc3\xa3o sabe com quem est\xc3\xa1 se metendo.',
       'Nunca se meteu com algu\xc3\xa9m da minha turma?',
       'Isso \xc3\xa9 bom, quando um n\xc3\xa3o quer dois n\xc3\xa3o se misturam.',
       'Vamos fazer amizade.',
       'Parece um bom lugar para confraternizar.',
       'N\xc3\xa3o \xc3\xa9 confort\xc3\xa1vel?',
       'Voc\xc3\xaas est\xc3\xa3o se unindo com a derrota.',
       'Vou me juntar a voc\xc3\xaa no neg\xc3\xb3cio.',
       'Tem certeza de que est\xc3\xa1 pronto para a uni\xc3\xa3o?'],
 'ms': ['Prepare-se para uma sacudida.',
        'Melhor voc\xc3\xaa sair do caminho.',
        'Olha a frente.',
        'Acho que \xc3\xa9 minha vez.',
        'Isso deve agitar voc\xc3\xaa.',
        'Prepare-se para ser movido.',
        'Estou pronto para dar o meu passo.',
        'Cuidado Toon, voc\xc3\xaa est\xc3\xa1 em terreno inst\xc3\xa1vel.',
        'Este deve ser um momento de movimento.',
        'Sinto um impulso de derrotar voc\xc3\xaa.',
        'Voc\xc3\xaa ainda est\xc3\xa1 tremendo?'],
 'hh': ['Estou na sua frente nesta ca\xc3\xa7ada.',
        'Voc\xc3\xaa est\xc3\xa1 ca\xc3\xa7ando encrenca da grande.',
        'A sua cabe\xc3\xa7a est\xc3\xa1 na mira do ca\xc3\xa7ador de cabe\xc3\xa7as.',
        'Que bom, estava atr\xc3\xa1s de voc\xc3\xaa.',
        'Vou perseguir voc\xc3\xaa por isto.',
        'Fique de olho!',
        'Parece que voc\xc3\xaa est\xc3\xa1 perdido nesta ca\xc3\xa7ada.',
        'Est\xc3\xa1 indo pela mesma trilha que eu?',
        'Um trof\xc3\xa9u perfeito para a minha cole\xc3\xa7\xc3\xa3o.',
        'Voc\xc3\xaa vai ter uma dor de cabe\xc3\xa7a...',
        'N\xc3\xa3o perca o rumo comigo.'],
 'tbc': ['Cuidado, vou ado\xc3\xa7ar voc\xc3\xaa.',
         'Pode me chamar de Coquinho.',
         'Tem certeza? \xc3\x80s vezes ajo como um C\xc3\xa3ocad\xc3\xa3o.',
         'Finalmente, estava achando que voc\xc3\xaa ia me deixar aqui \xc3\xa0 merc\xc3\xaa das formigas.',
         'Vou queimar o seu coco.',
         'N\xc3\xa3o acha que eu sou um docinho de coco?',
         'Voc\xc3\xaa vai virar cocada comigo.',
         'As pessoas me acham dur\xc3\xa3o.',
         'Cuidado, eu sei a sua data de validade.',
         'Cuidado, sou uma fera neste jogo.',
         'Bater voc\xc3\xaa vai ser mole.'],
 'cr': ['ATAQUE!',
        'Voc\xc3\xaa n\xc3\xa3o \xc3\xa9 adequado para a minha corpora\xc3\xa7\xc3\xa3o.',
        'Prepare-se para ser atacado.',
        'Parece que voc\xc3\xaa est\xc3\xa1 preparado para assumir o comando da aventura.',
        'Esta roupa n\xc3\xa3o \xc3\xa9 apropriada para ambientes corporativos.',
        'Voc\xc3\xaa parece estar bem vulner\xc3\xa1vel.',
        '\xc3\x89 hora de botar os bens em seu nome.',
        'Estou em uma cruzada a favor da elimina\xc3\xa7\xc3\xa3o dos Toons.',
        'Voc\xc3\xaa fica sem defesa contra as minhas id\xc3\xa9ias.',
        'Relaxa, voc\xc3\xaa vai ver que vai ser melhor assim.'],
 'mh': ['Est\xc3\xa1 preparado para a minha tomada?',
        'Luz, c\xc3\xa2mera, a\xc3\xa7\xc3\xa3o!',
        'Vai come\xc3\xa7ar a rodar.',
        'Hoje o papel do Toon derrotado ser\xc3\xa1 feito por - VOC\xc3\x8a!',
        'Esta cena vai ser cortada.',
        'J\xc3\xa1 sei qual vai ser a minha motiva\xc3\xa7\xc3\xa3o para esta cena.',
        'Est\xc3\xa1 preparado para a sua cena final?',
        'Estou pronto para passar os seus cr\xc3\xa9ditos no final.',
        'Eu disse para voc\xc3\xaa n\xc3\xa3o me chamar.',
        'O show tem que continuar.',
        'N\xc3\xa3o tem neg\xc3\xb3cio igual a este!',
        'Espero que voc\xc3\xaa n\xc3\xa3o se esque\xc3\xa7a das suas falas.'],
 'nc': ['Parece que o seu n\xc3\xbamero est\xc3\xa1 em alta.',
        'Prefere ser destru\xc3\xaddo com ou sem cobertura crocante?',
        'Agora, voc\xc3\xaa est\xc3\xa1 destru\xc3\xaddo.',
        'J\xc3\xa1 est\xc3\xa1 na hora de dizimar todos estes n\xc3\xbameros?',
        'Vamos fazer uma matem\xc3\xa1tica.',
        'Onde voc\xc3\xaa gostaria de fazer uma subtra\xc3\xa7\xc3\xa3o hoje?',
        'Voc\xc3\xaa me deu uma coisa para calcular!',
        'N\xc3\xa3o vai ser f\xc3\xa1cil.',
        'Vai em frente, pegue um n\xc3\xbamero qualquer.',
        'Vou destruir voc\xc3\xaa com os meus c\xc3\xa1lculos.'],
 'ls': ['\xc3\x89 hora de recolher o seu empr\xc3\xa9stimo.',
        'Voc\xc3\xaa tem estado na pior.',
        'O empr\xc3\xa9stimo agora tem que ser pago.',
        'Hora de liquidar a d\xc3\xadvida.',
        'Bom, voc\xc3\xaa queria um adiantamento e conseguiu.',
        'Voc\xc3\xaa ter\xc3\xa1 que pagar por isso.',
        '\xc3\x89 hora de devolver o que pegou.',
        'Pode me dar uma m\xc3\xa3ozinha?',
        'Ainda bem que voc\xc3\xaa est\xc3\xa1 aqui, isto est\xc3\xa1 uma loucura.',
        'Podemos fazer um lanchinho?',
        'Deixe-me dar um tasco.'],
 'mb': ['Est\xc3\xa1 na hora de trazer os sacos.',
        'Posso ensacar isso.',
        'Papel ou pl\xc3\xa1stico?',
        'Voc\xc3\xaa tem o t\xc3\xadquete da bagagem?',
        'Lembre-se de que o dinheiro n\xc3\xa3o vai fazer voc\xc3\xaa feliz.',
        'Cuidado, tenho muita bagagem.',
        'Voc\xc3\xaa est\xc3\xa1 prestes a ficar no vermelho.',
        'O dinheiro vai fazer o seu mundo girar.',
        'Sou muito rico para o seu bico.',
        'Voc\xc3\xaa nunca poder\xc3\xa1 ter tanto dinheiro!'],
 'rb': ['Voc\xc3\xaa foi roubado.',
        'Vou roubar esta vit\xc3\xb3ria de voc\xc3\xaa.',
        'Sou um chato de galochas!',
        'Espero que voc\xc3\xaa ainda possa sorrir para o bar\xc3\xa3o.',
        'Voc\xc3\xaa ter\xc3\xa1 que denunciar este roubo.',
        'M\xc3\xa3os ao alto.',
        'Sou um advers\xc3\xa1rio nobre.',
        'Vou levar tudo o que voc\xc3\xaa tem.',
        'Voc\xc3\xaa pode chamar isto de roubo no bairro.',
        'Voc\xc3\xaa j\xc3\xa1 devia saber que n\xc3\xa3o se fala com estranhos.'],
 'bs': ['Nunca vire as costas para mim.',
        'Voc\xc3\xaa n\xc3\xa3o vai voltar mesmo.',
        'Retire o que disse, ou ent\xc3\xa3o...!',
        'Sou bom em cortar custos.',
        'Tenho as costas quentes.',
        'Agora, n\xc3\xa3o d\xc3\xa1 mais para voltar atr\xc3\xa1s.',
        'Sou o melhor e posso provar.',
        '\xc3\x94\xc3\xb4\xc3\xb4, parado a\xc3\xad, Toon.',
        'Deixe-me dar cobertura a voc\xc3\xaa.',
        'Voc\xc3\xaa vai ter uma dor de cabe\xc3\xa7a infernal.',
        'Tenho um golpe perfeito.'],
 'bw': ['Quero sair bem na foto.',
        'Voc\xc3\xaa me arrepia os cabelos.',
        'Posso deixar assim para sempre, se quiser.',
        'Parece que voc\xc3\xaa vai ficar com a cara boa.',
        'Voc\xc3\xaa n\xc3\xa3o consegue encarar a verdade.',
        'Acho que \xc3\xa9 sua vez de mudar de cor.',
        'Estou t\xc3\xa3o feliz que voc\xc3\xaa chegou na hora de mudar o visual.',
        'Voc\xc3\xaa est\xc3\xa1 encrencado.',
        'Vou deixar voc\xc3\xaa doid\xc3\xa3o.',
        'Sou um baita de um Toonzinho.'],
 'le': ['Cuidado, sou legal mas nem tanto.',
        'Eu pulo de galho em galho, mas alguns quebram.',
        'Vou fazer a lei chegar at\xc3\xa9 voc\xc3\xaa.',
        'Voc\xc3\xaa j\xc3\xa1 devia saber que tenho instintos criminosos.',
        'Vou fazer voc\xc3\xaa ter pesadelos jur\xc3\xaddicos.',
        'Voc\xc3\xaa n\xc3\xa3o vai ganhar esta batalha.',
        'Isto \xc3\xa9 t\xc3\xa3o divertido que deveria ser proibido por lei.',
        'Legalmente falando, voc\xc3\xaa \xc3\xa9 muito pequeno para lutar comigo.',
        'N\xc3\xa3o h\xc3\xa1 limites para os meus botes.',
        'Chamo isso de pris\xc3\xa3o de cidad\xc3\xa3o.'],
 'sd': ['Voc\xc3\xaa nunca saber\xc3\xa1 quando vou parar.',
        'Deixe-me levar voc\xc3\xaa para uma volta.',
        'Vida social \xc3\xa9 comigo mesmo.',
        'Vou colocar voc\xc3\xaa em um agito.',
        'Voc\xc3\xaa parece precisar de anima\xc3\xa7\xc3\xa3o.',
        'A festa est\xc3\xa1 rolando, mas Toons n\xc3\xa3o entram.',
        'Voc\xc3\xaa n\xc3\xa3o vai gostar do meu pitaco nisto.',
        'Voc\xc3\xaa vai ficar fora de controle.',
        'Voc\xc3\xaa se importa de dar umas voltinhas comigo?',
        'Tenho minha pr\xc3\xb3pria teoria sobre o assunto.'],
 'f': ['Vou falar sobre voc\xc3\xaa com o chefe!',
       'Posso ser apenas um puxa-saco, mas sou demais.',
       'Estou usando voc\xc3\xaa para subir os v\xc3\xa1rios degraus dentro da empresa.',
       'Voc\xc3\xaa n\xc3\xa3o vai gostar do jeito como eu trabalho.',
       'O chefe est\xc3\xa1 contando comigo para deter voc\xc3\xaa.',
       'Voc\xc3\xaa vai ficar bonito no meu curr\xc3\xadculo.',
       'Voc\xc3\xaa ter\xc3\xa1 que passar por cima de mim primeiro.',
       'Vamos ver como voc\xc3\xaa classifica meu desempenho funcional.',
       'Eu me sobressaio na elimina\xc3\xa7\xc3\xa3o de Toons.',
       'Voc\xc3\xaa jamais conhecer\xc3\xa1 o meu chefe.',
       'Vou mandar voc\xc3\xaa de volta para o P\xc3\xa1tio.'],
 'p': ['Eu vou apagar voc\xc3\xaa!',
       'Ei, voc\xc3\xaa n\xc3\xa3o pode ficar mandando em mim.',
       'Sou o n\xc3\xbamero 2!',
       'Vou cortar voc\xc3\xaa.',
       'Vou ter que me fazer mais claro.',
       'Deixe-me ir direto ao ponto.',
       'R\xc3\xa1pido, eu fico irritado com facilidade.',
       'Odeio quando as coisas ficam bobas.',
       'Ent\xc3\xa3o, voc\xc3\xaa quer arriscar a pr\xc3\xb3pria sorte?',
       'Voc\xc3\xaa me passou o l\xc3\xa1pis?',
       'Cuidado, posso deixar uma marca.'],
 'ym': ['Concordo com tudo.',
        'N\xc3\xa3o sei o que significa n\xc3\xa3o.',
        'Quer me conhecer? Eu digo sim sempre.',
        'Voc\xc3\xaa precisa de uma for\xc3\xa7a positiva.',
        'Vou deixar uma impress\xc3\xa3o positiva.',
        'Ainda n\xc3\xa3o me enganei.',
        'Sim, estou pronto para voc\xc3\xaa.',
        'Acha mesmo que quer fazer isto?',
        'Voc\xc3\xaa certamente terminar\xc3\xa1 com saldo positivo nessa.',
        'Confirmando a hora da sua reuni\xc3\xa3o.',
        'N\xc3\xa3o aceito n\xc3\xa3o como resposta.'],
 'mm': ['Vou entrar neste neg\xc3\xb3cio.',
        '\xc3\x80s vezes, os piores venenos v\xc3\xaam em pequenos frascos.',
        'Nenhum trabalho \xc3\xa9 insignificante para mim.',
        'Quero o trabalho feito direito, por isso eu mesmo o fa\xc3\xa7o.',
        'Voc\xc3\xaa precisa de algu\xc3\xa9m para gerenciar os seus bens.',
        'Que bom, um projeto.',
        'Bem, voc\xc3\xaa conseguiu me achar.',
        'Acho que voc\xc3\xaa precisa de alguma organiza\xc3\xa7\xc3\xa3o.',
        'Vou cuidar de voc\xc3\xaa em dois tempos.',
        'Estou observando tudo que voc\xc3\xaa faz.',
        'Tem certeza de que deseja fazer isto?',
        'Vamos fazer da minha maneira.',
        'Vou estar na sua cola.',
        'Posso ser bem intimidador.'],
 'ds': ['Voc\xc3\xaa est\xc3\xa1 caindo no meu golpe!',
        'Voc\xc3\xaa vai encolher com meu ataque.',
        'Espere retornos min\xc3\xbasculos.',
        'Voc\xc3\xaa vai deixar de existir.',
        'N\xc3\xa3o me pe\xc3\xa7a nenhuma dispensa.',
        'Vou precisar fazer alguns cortes.',
        'As coisas parecem estar despeda\xc3\xa7adas para voc\xc3\xaa.',
        'Por que voc\xc3\xaa parece t\xc3\xa3o machucado?'],
 'cc': ['Surpreso de saber de mim?',
        'Voc\xc3\xaa ligou?',
        'Est\xc3\xa1 pronto para aceitar as minhas tarifas?',
        'Este aqui sempre recolhe alguma coisa.',
        'Eu opero bem as linhas.',
        'Espere um segundo, estou aqui.',
        'Estava esperando a minha liga\xc3\xa7\xc3\xa3o?',
        'Estava torcendo para voc\xc3\xaa atender a minha liga\xc3\xa7\xc3\xa3o.',
        'Vou deixar uma sensa\xc3\xa7\xc3\xa3o tocante.',
        'Sempre fa\xc3\xa7o liga\xc3\xa7\xc3\xb5es diretas.',
        'Cara, tem boi na linha.',
        'Esta liga\xc3\xa7\xc3\xa3o ter\xc3\xa1 um custo para voc\xc3\xaa.',
        'Voc\xc3\xaa tem um pepino nesta linha.'],
 'tm': ['Meu plano \xc3\xa9 tornar isto inconveniente para voc\xc3\xaa.',
        'Posso incluir voc\xc3\xaa em um seguro?',
        'Voc\xc3\xaa n\xc3\xa3o deveria ter me atendido.',
        'Voc\xc3\xaa n\xc3\xa3o vai conseguir se livrar de mim agora.',
        'T\xc3\xa1 chateado? Que bom.',
        'Estava pensando em atropelar voc\xc3\xaa.',
        'Vou inverter as cobran\xc3\xa7as desta liga\xc3\xa7\xc3\xa3o.',
        'Tenho alguns itens bem caros para voc\xc3\xaa hoje.',
        'Se deu mal, eu fa\xc3\xa7o liga\xc3\xa7\xc3\xb5es locais.',
        'Estou preparado para fechar este neg\xc3\xb3cio rapidinho.',
        'Vou usar um monte de recursos seus.'],
 'nd': ['Na minha opini\xc3\xa3o, seu nome est\xc3\xa1 na lama.',
        'Espero que n\xc3\xa3o se importe se eu jogar o seu nome na boca das matildes.',
        'A gente j\xc3\xa1 n\xc3\xa3o se conhece?',
        'Depressa, vou almo\xc3\xa7ar com o Dr. Celebridade.',
        'Eu falei que conhe\xc3\xa7o o Amizade F\xc3\xa1cil?',
        'Voc\xc3\xaa nunca vai me esquecer.',
        'Conhe\xc3\xa7o todas as pessoas certas para detonar voc\xc3\xaa.',
        'Acho que vou passar a\xc3\xad.',
        'Estou a fim de detonar alguns Toons.',
        'Eu te disse, detonei.'],
 'gh': ['Diz a\xc3\xad, Toon.',
        'O bicho vai pegar.',
        'Vou gostar disso.',
        'Voc\xc3\xaa vai acabar vendo as minhas garras.',
        'Vamos assinar embaixo.',
        'Vamos direto ao que interessa.',
        'N\xc3\xa3o cutuca a on\xc3\xa7a com vara curta, ou voc\xc3\xaa vai acabar mal.',
        'Voc\xc3\xaa vai acabar gostando da minha pinta.',
        'Olha que eu viro uma on\xc3\xa7a.',
        'Voc\xc3\xaa n\xc3\xa3o vai escapar das minhas garras.',
        'Voc\xc3\xaa quer que eu safe a on\xc3\xa7a?',
        'Se ficar o bicho come, se correr o bicho pega.',
        'As marcas das minhas unhas afiadas est\xc3\xa3o na parede.'],
 'sc': ['Vamos logo acabar com esta farsa.',
        'Voc\xc3\xaa est\xc3\xa1 prestes a ficar no vermelho.',
        'Voc\xc3\xaa est\xc3\xa1 prestes a pagar taxas abusivas.',
        'O projeto vai ser de fachada.',
        'Esta fraude vai ser moleza.',
        'Logo, logo voc\xc3\xaa vai cair na minha arapuca.',
        'Vamos embromar um pouquinho.',
        'Veio cedo para ver o meu truque, n\xc3\xa9?',
        'Tenho pavio curto com Toons.',
        'Logo vou armar minha armadilha para voc\xc3\xaa.',
        'Voc\xc3\xaa est\xc3\xa1 prestes a cair na minha l\xc3\xa1bia.'],
 'pp': ['Meu aperto de m\xc3\xa3o \xc3\xa9 forte.',
        'Minha m\xc3\xa3o \xc3\xa9 de ferro.',
        'Voc\xc3\xaa n\xc3\xa3o quer que a vaca v\xc3\xa1 pro brejo, ou quer?',
        'Seu sorriso vai ficar p\xc3\xa1lido como leite.',
        'Tenho um lugar para voc\xc3\xaa, mas n\xc3\xa3o pense que sou m\xc3\xa3o-aberta.',
        'Deixe e pagar na mesma moeda.',
        'Dou tchau com a m\xc3\xa3o fechada.',
        'Vou provar que voc\xc3\xaa n\xc3\xa3o est\xc3\xa1 sonhando.',
        'Cabe\xc3\xa7as v\xc3\xa3o rolar, e eu vou ganhar.',
        'Dou uma moedinha pelas suas piadas.'],
 'tw': ['Vamos ter que dar duro.',
        '\xc3\x89 o P\xc3\xa3o-duro.',
        'Vou ter que cortar a sua verba.',
        '\xc3\x89 a melhor oferta que voc\xc3\xaa pode fazer?',
        'Vamos logo. Tempo \xc3\xa9 dinheiro.',
        'Voc\xc3\xaa vai descobrir como dou duro.',
        'Voc\xc3\xaa est\xc3\xa1 na corda bamba.',
        'Prepare-se para a dureza.',
        'Voc\xc3\xaa n\xc3\xa3o conhece o p\xc3\xa3o que o diabo amassou.',
        'Vou ter que apertar o cinto.',
        'Vou fazer um rombo no seu or\xc3\xa7amento.'],
 'bc': ['Adoro subtrair Toons.',
        'Pode contar comigo para fazer voc\xc3\xaa pagar.',
        'O neg\xc3\xb3cio \xc3\xa9 contar as moedinhas.',
        'Contar \xc3\xa9 comigo mesmo.',
        'Sou um contador de balinhas.',
        'Sua planilha de gastos est\xc3\xa1 excedendo o limite.',
        '\xc3\x89 hora de fazer uma auditoria.',
        'Vamos entrar no meu escrit\xc3\xb3rio.',
        'Onde voc\xc3\xaa estava? Eu contava com voc\xc3\xaa.',
        'Estou esperando por voc\xc3\xaa h\xc3\xa1 um milh\xc3\xa3o de horas.',
        'Voc\xc3\xaa n\xc3\xa3o vale um n\xc3\xadquel.'],
 'bf': ['Parece que voc\xc3\xaa chegou na hora do lanche.',
        'Estou pronto para o banquete.',
        'Sou um comedor de Toons.',
        '\xc3\x8aba, hora do almo\xc3\xa7o.',
        'Na hora certa! Preciso de um lanchinho.',
        'Gostaria de alguma opini\xc3\xa3o sobre o meu desempenho.',
        'Vamos falar sobre o que interessa.',
        'Voc\xc3\xaa vai descobrir que tenho um talento imensur\xc3\xa1vel.',
        'Bom, preciso de um pequeno est\xc3\xadmulo.',
        'Adoraria se voc\xc3\xaa almo\xc3\xa7asse comigo.'],
 'tf': ['Est\xc3\xa1 na hora de nosso duelo!',
        'Melhor encarar a derrota.',
        'Prepare-se para enfrentar o seu pior pesadelo!',
        'Encare os fatos: eu sou melhor que voc\xc3\xaa.',
        'Duas cabe\xc3\xa7as pensam melhor que uma.',
        'Se um n\xc3\xa3o quer, dois n\xc3\xa3o brigam. Quer brigar?',
        'Voc\xc3\xaa est\xc3\xa1 duplamente encrencado.',
        'Qual face voc\xc3\xaa quer que o derrote?',
        'Eu sou demais para voc\xc3\xaa.',
        'Voc\xc3\xaa n\xc3\xa3o sabe com quem est\xc3\xa1 se metendo.',
        'Voc\xc3\xaa est\xc3\xa1 preparado para encarar sua derrota?'],
 'dt': ['Voc\xc3\xaa ter\xc3\xa1 trabalho em dobro comigo.',
        'Veja se voc\xc3\xaa consegue enfrentar meu golpe duplo.',
        'Trabalho para um ARM\xc3\x81RIO 4x4 muito mau.',
        'Est\xc3\xa1 na hora de um golpe duplo.',
        'Meu plano \xc3\xa9 ter duas FONTES.',
        'Voc\xc3\xaa n\xc3\xa3o vai gostar do meu jogo duplo.',
        'Talvez queira pensar duas vezes nisso.',
        'Prepare-se para uma LIGA\xc3\x87\xc3\x83O dupla.',
        'Talvez queira aplicar uma dose dupla contra mim.',
        'Duplas, algu\xc3\xa9m??'],
 'ac': ['Eu vou botar voc\xc3\xaa pr\xc3\xa1 correr desta cidade!',
        'Est\xc3\xa1 ouvindo uma sirene?',
        'Vou gostar disso.',
        'Adoro a emo\xc3\xa7\xc3\xa3o da persegui\xc3\xa7\xc3\xa3o.',
        'Vou dar um passa-fora.',
        'Voc\xc3\xaa tem seguro?',
        'Espero que tenha trazido uma maca.',
        'Duvido que voc\xc3\xaa possa comigo.',
        '\xc3\x89 s\xc3\xb3 rala\xc3\xa7\xc3\xa3o a partir daqui.',
        'Em breve voc\xc3\xaa vai precisar de uma ambul\xc3\xa2ncia.',
        'N\xc3\xa3o \xc3\xa9 piada.',
        'Vou passar a parada para voc\xc3\xaa.']}
SpeedChatStaticText = {1: lYes,
 2: lNo,
 3: lOK,
 4: 'CHAT R\xc3\x81PIDO PLUS'}
SpeedChatStaticTextToontown = {100: 'Oi!',
 101: 'Ol\xc3\xa1!',
 102: 'E a\xc3\xad?',
 103: '\xc3\x94pa!',
 104: 'Tudo certo?',
 105: 'Oi, pessoal!',
 106: 'Bem-vindo a Toontown!',
 107: 'Tudo em cima?',
 108: 'Tudo bem?',
 109: 'Al\xc3\xb4?',
 200: 'Tchau!',
 201: 'At\xc3\xa9 mais!',
 202: 'Te vejo por a\xc3\xad!',
 203: 'Bom dia pra voc\xc3\xaa!',
 204: 'Divirta-se!',
 205: 'Boa sorte!',
 206: 'J\xc3\xa1 volto.',
 207: 'Tenho que ir.',
 208: 'Eu volto j\xc3\xa1!',
 209: 'Eu s\xc3\xb3 tenho alguns minutos.',
 300: ':-)',
 301: 'Valeu!',
 302: 'Maneiro!',
 303: 'Legal!',
 304: 'Iuhuu!',
 305: '\xc3\x89 isso a\xc3\xad!',
 306: 'Ah, ah!',
 307: 'He, he!',
 308: 'Uau!',
 309: 'Demais!',
 310: 'Iahuuuuu!',
 311: 'Nossa!',
 312: 'Uhuu!',
 313: 'Iupii!!',
 314: 'Dez!',
 315: 'Toont\xc3\xa1stico!',
 400: ':-(',
 401: 'Ah, n\xc3\xa3o!',
 402: '\xc3\x8apa!',
 403: 'Droga!',
 404: 'Ai, ai, ai!',
 405: 'Ahhh!',
 406: 'Puxa!',
 407: 'N\xc3\xa3o!!!',
 408: 'P\xc3\xb4xa vida!',
 409: 'H\xc3\xa3?',
 410: 'Preciso de mais pontos de Risadas.',
 500: 'Valeu!',
 501: 'Sem problemas.',
 502: 'De nada!',
 503: 'Sempre que quiser!',
 504: 'N\xc3\xa3o, obrigado.',
 505: 'Bom trabalho de equipe!',
 506: 'Isso foi divertido!',
 507: 'Vamos ser amigos!',
 508: 'Vamos trabalhar juntos!',
 509: 'Voc\xc3\xaas s\xc3\xa3o demais!',
 510: 'Voc\xc3\xaa \xc3\xa9 novo aqui?',
 511: 'Ganhou?',
 512: 'Acho arriscado pr\xc3\xa1 voc\xc3\xaa.',
 513: 'Quer ajuda?',
 514: 'Voc\xc3\xaa me ajuda?',
 515: 'Voc\xc3\xaa j\xc3\xa1 veio aqui antes?',
 600: 'Voc\xc3\xaa parece legal.',
 601: 'Voc\xc3\xaa \xc3\xa9 incr\xc3\xadvel!',
 602: 'Voc\xc3\xaa \xc3\xa9 maneiro!',
 603: 'Voc\xc3\xaa \xc3\xa9 um g\xc3\xaanio!',
 700: 'Gosto do seu nome.',
 701: 'Gosto do seu jeito.',
 702: 'Gosto da sua camisa.',
 703: 'Gosto da sua saia.',
 704: 'Gosto do seu short.',
 705: 'Gosto deste jogo!',
 800: 'Desculpe!',
 801: 'Ops!',
 802: 'Desculpe, agora estou lutando com Cogs!',
 803: 'Desculpe, agora estou conseguindo balinhas!',
 804: 'Desculpe, agora estou completando uma Tarefa Toon!',
 805: 'Desculpe, tive que sair de repente.',
 806: 'Desculpe, fiquei preso.',
 807: 'Desculpe, n\xc3\xa3o posso.',
 808: 'N\xc3\xa3o pude esperar mais.',
 809: 'N\xc3\xa3o entendi.',
 810: 'Use o %s.' % GlobalSpeedChatName,
 811: 'Desculpe, estou ocupado pescando!',
 812: 'Desculpe, estou dentro de um pr\xc3\xa9dio!',
 813: 'Desculpe, estou ajudando um amigo!',
 814: 'Desculpe, estou ocupado numa corrida de kart!',
 815: 'Desculpe, estou fazendo jardinagem agora!',
 816: 'N\xc3\xa3o posso entrar no elevador agora.',
 817: 'Desculpe, estou jogando golfe agora!',
 818: 'Desculpe, minha Lista de Amigos est\xc3\xa1 cheia.',
 900: '\xc3\x94pa!',
 901: 'V\xc3\xa1 embora!!',
 902: 'Pare com isso!',
 903: 'Isso n\xc3\xa3o foi legal!',
 904: 'N\xc3\xa3o seja mau!',
 905: 'Voc\xc3\xaa \xc3\xa9 nojento!',
 906: 'Envie um relat\xc3\xb3rio de problemas.',
 907: 'Estou atolado.',
 1000: 'Vamos!',
 1001: 'Voc\xc3\xaa pode se teletransportar at\xc3\xa9 a mim?',
 1002: 'Podemos ir?',
 1003: 'Para onde devemos ir?',
 1004: 'Em que dire\xc3\xa7\xc3\xa3o?',
 1005: 'Esta dire\xc3\xa7\xc3\xa3o.',
 1006: 'Siga-me.',
 1007: 'Espere por mim!',
 1008: 'Vamos esperar pelo meu amigo.',
 1009: 'Vamos encontrar outros Toons.',
 1010: 'Espere aqui.',
 1011: 'Espere um minuto.',
 1012: 'Vamos nos encontrar aqui.',
 1013: 'Voc\xc3\xaa pode ir at\xc3\xa9 a minha casa?',
 1014: 'N\xc3\xa3o espere por mim.',
 1015: 'Espere!',
 1016: 'Venha dar uma olhada no meu jardim.',
 1017: 'Vamos pegar o pr\xc3\xb3ximo.',
 1100: 'Vamos pegar o bondinho!',
 1101: 'Vamos voltar para o p\xc3\xa1tio!',
 1102: 'Vamos lutar com %s!' % Cogs,
 1103: 'Vamos tomar um edif\xc3\xadcio %s!' % Cog,
 1104: 'Vamos entrar no elevador!',
 1105: 'Vamos para o %s!' % lToontownCentral,
 1106: 'Vamos para o %s!' % lDonaldsDock,
 1107: 'Vamos para a %s!' % lMinniesMelodyland,
 1108: 'Vamos para o %s!' % lDaisyGardens,
 1109: 'Vamos para %s!' % lTheBrrrgh,
 1110: 'Vamos para a %s!' % lDonaldsDreamland,
 1111: 'Vamos para o %s!' % lGoofySpeedway,
 1112: 'Vamos para a minha casa!',
 1113: 'Vamos para a sua casa!',
 1114: 'Vamos para o Quartel do Rob\xc3\xb4 Vendedor!',
 1115: 'Vamos lutar com o VP!',
 1116: 'Vamos entrar na F\xc3\xa1brica!',
 1117: 'Vamos pescar!',
 1118: 'Vamos pescar na minha casa!',
 1119: 'Vamos para o Quartel do Rob\xc3\xb4 Mercen\xc3\xa1rio!',
 1120: 'Vamos lutar com o Diretor Financeiro!',
 1121: 'Vamos entrar na Casa da Moeda!',
 1122: 'Vamos para o Quartel do Rob\xc3\xb4 da Lei!',
 1123: 'Vamos lutar com o Juiz Chefe!',
 1124: 'Vamos para o Escrit\xc3\xb3rio do Promotor P\xc3\xbablico!',
 1125: 'Vamos para %s!' % lOutdoorZone,
 1126: 'Vamos para %s!' % lGolfZone,
 1127: 'Vamos para o Quartel do Rob\xc3\xb4 Chefe!',
 1128: 'Vamos lutar com o Presidente!',
 1129: 'Vamos para o Campo de Golfe Cog!',
 1130: 'Vamos assumir um Escrit\xc3\xb3rio de Campo!',
 1200: 'Em que Tarefa Toon voc\xc3\xaa est\xc3\xa1 trabalhando?',
 1201: 'Vamos trabalhar nisto.',
 1202: 'Isto n\xc3\xa3o \xc3\xa9 o que estou procurando.',
 1203: 'Vou procurar isto.',
 1204: 'N\xc3\xa3o est\xc3\xa1 nesta rua.',
 1205: 'N\xc3\xa3o encontrei ainda.',
 1206: 'Preciso de mais M\xc3\xa9ritos por Cogs.',
 1207: 'Preciso de mais pe\xc3\xa7as de vestimentas de Cogs.',
 1208: 'N\xc3\xa3o \xc3\xa9 disso que voc\xc3\xaa precisa.',
 1209: 'Achei o que voc\xc3\xaa precisa.',
 1210: 'Eu preciso de mais d\xc3\xb3aleres de Cog.',
 1211: 'Eu preciso de mais Avisos ao J\xc3\xbari.',
 1212: 'Eu preciso de mais O\xc3\xa7\xc3\xb5es de Estoque.',
 1213: 'Eu preciso de mais Pe\xc3\xa7as de Vestimenta de Rob\xc3\xb4 Mercen\xc3\xa1rio.',
 1214: 'Eu preciso de mais Pe\xc3\xa7as de Vestimenta de Rob\xc3\xb4 da Lei.',
 1215: 'Preciso de mais Pe\xc3\xa7as de Rob\xc3\xb4 Chefe.',
 1299: 'Preciso pegar uma Tarefa Toon.',
 1300: 'Acho que voc\xc3\xaa devia escolher Toonar.',
 1301: 'Acho que voc\xc3\xaa devia escolher Sonora.',
 1302: 'Acho que voc\xc3\xaa devia escolher Cadente.',
 1303: 'Acho que voc\xc3\xaa devia escolher Armadilha.',
 1304: 'Acho que voc\xc3\xaa devia escolher Isca.',
 1400: 'Anda!',
 1401: 'Que tiro!',
 1402: 'Que piada!',
 1403: 'N\xc3\xa3o me acertou!',
 1404: 'Conseguiu!',
 1405: 'Conseguimos!',
 1406: 'Ataque!',
 1407: 'Moleza!',
 1408: 'Esta foi f\xc3\xa1cil!',
 1409: 'Corre!',
 1410: 'Socorro!',
 1411: 'Ufa!',
 1412: 'Estamos em apuros.',
 1413: 'Preciso de mais piadas.',
 1414: 'Preciso de uma Toonar.',
 1415: 'Voc\xc3\xaa deve passar.',
 1416: 'Vamos conseguir!',
 1500: 'Vamos usar toonar!',
 1501: 'Vamos usar armadilha!',
 1502: 'Vamos usar isca!',
 1503: 'Vamos usar sonora!',
 1504: 'Vamos usar lan\xc3\xa7amento!',
 1505: 'Vamos usar esguicho!',
 1506: 'Vamos usar cadente!',
 1520: '\xc3\x89 hora do Rock!',
 1521: 'Isso deve doer.',
 1522: 'Pegue!',
 1523: 'Entrega especial!',
 1524: 'Voc\xc3\xaa ainda est\xc3\xa1 aqui?',
 1525: 'Ai, que medo!',
 1526: 'Esta vai deixar cicatriz!',
 1550: 'Vou usar uma armadilha.',
 1551: 'Vou usar uma isca.',
 1552: 'Vou usar uma cadente.',
 1553: 'Voc\xc3\xaa devia usar uma piada diferente.',
 1554: 'Vamos todos no mesmo Cog.',
 1555: 'Voc\xc3\xaa devia escolher um Cog diferente.',
 1556: 'V\xc3\xa1 no Cog mais fraco primeiro.',
 1557: 'V\xc3\xa1 no Cog mais forte primeiro.',
 1558: 'Economize as piadas mais poderosas.',
 1559: 'N\xc3\xa3o use som em Cogs dominados por iscas.',
 1600: 'Tenho piadas suficientes.',
 1601: 'Preciso de mais balinhas.',
 1602: 'Eu tamb\xc3\xa9m.',
 1603: 'Vamos nessa!',
 1604: 'Mais um?',
 1605: 'Jogar de novo?',
 1606: 'Vamos jogar de novo.',
 1700: 'Vamos nos separar.',
 1701: 'Vamos ficar juntos.',
 1702: 'Vamos lutar com os Cogs.',
 1703: 'Pise no interruptor.',
 1704: 'Passe pela porta.',
 1803: 'Estou na Entrada principal.',
 1804: 'Estou no Sal\xc3\xa3o.',
 1805: 'Estou no corredor fora do Sal\xc3\xa3o.',
 1806: 'Estou no corredor fora do Sal\xc3\xa3o.',
 1807: 'Estou na Sala de cogs.',
 1808: 'Estou na Sala da caldeira.',
 1809: 'Estou na Passarela leste.',
 1810: 'Estou no Misturador de tinta.',
 1811: 'Estou no Dep\xc3\xb3sito do Misturador de tinta.',
 1812: 'Estou na Passarela do Silo Oeste.',
 1813: 'Estou na Sala de tubula\xc3\xa7\xc3\xb5es.',
 1814: 'Estou nas escadas da Sala de tubula\xc3\xa7\xc3\xb5es.',
 1815: 'Estou na Sala de dutos.',
 1816: 'Estou na Entrada lateral.',
 1817: 'Estou no Beco sinistro.',
 1818: 'Estou fora do Sal\xc3\xa3o de lava.',
 1819: 'Estou no Sal\xc3\xa3o de lava.',
 1820: 'Estou no Dep\xc3\xb3sito de lava.',
 1821: 'Estou na Passarela oeste.',
 1822: 'Estou na Sala de \xc3\xb3leo.',
 1823: 'Estou na Vigil\xc3\xa2ncia do Armaz\xc3\xa9m.',
 1824: 'Estou no Armaz\xc3\xa9m.',
 1825: 'Estou fora do Misturador de tinta.',
 1827: 'Estou fora da Sala de \xc3\xb3leo.',
 1830: 'Estou na Sala de controle do Silo Leste.',
 1831: 'Estou na Sala de controle do Silo Oeste.',
 1832: 'Estou na Sala de controle do Silo Central.',
 1833: 'Estou no Silo Leste.',
 1834: 'Estou no Silo Oeste.',
 1835: 'Estou no Silo Central.',
 1836: 'Estou no Silo Oeste.',
 1837: 'Estou no Silo Leste.',
 1838: 'Estou na Passarela do Silo Leste.',
 1840: 'Estou no topo do Silo Oeste.',
 1841: 'Estou no topo do Silo Leste.',
 1860: 'Estou no Elevador do Silo Oeste.',
 1861: 'Estou no Elevador do Silo Leste.',
 1903: 'Vamos nos encontrar na Entrada principal.',
 1904: 'Vamos nos encontrar no Sal\xc3\xa3o.',
 1905: 'Vamos nos encontrar no corredor fora do sal\xc3\xa3o.',
 1906: 'Vamos nos encontrar no corredor fora do sal\xc3\xa3o.',
 1907: 'Vamos nos encontrar na Sala de Cogs.',
 1908: 'Vamos nos encontrar na Sala da caldeira.',
 1909: 'Vamos nos encontrar na Passarela leste.',
 1910: 'Vamos nos encontrar no Misturador de tinta.',
 1911: 'Vamos nos encontrar no Dep\xc3\xb3sito do Misturador de tinta.',
 1912: 'Vamos nos encontrar na Passarela do Silo Oeste.',
 1913: 'Vamos nos encontrar na Sala de tubula\xc3\xa7\xc3\xb5es.',
 1914: 'Vamos nos encontrar nas escadas da Sala de tubula\xc3\xa7\xc3\xb5es.',
 1915: 'Vamos nos encontrar na Sala de dutos.',
 1916: 'Vamos nos encontrar na Entrada lateral.',
 1917: 'Vamos nos encontrar no Beco sinistro.',
 1918: 'Vamos nos encontrar fora do Sal\xc3\xa3o de lava.',
 1919: 'Vamos nos encontrar no Sal\xc3\xa3o de lava.',
 1920: 'Vamos nos encontrar no Dep\xc3\xb3sito de lava.',
 1921: 'Vamos nos encontrar na Passarela oeste.',
 1922: 'Vamos nos encontrar na Sala de \xc3\xb3leo.',
 1923: 'Vamos nos encontrar na Vigil\xc3\xa2ncia do Armaz\xc3\xa9m.',
 1924: 'Vamos nos encontrar no Armaz\xc3\xa9m.',
 1925: 'Vamos nos encontrar fora do Misturador de tinta.',
 1927: 'Vamos nos encontrar fora da Sala de \xc3\xb3leo.',
 1930: 'Vamos nos encontrar na Sala de controle do Silo Leste.',
 1931: 'Vamos nos encontrar na Sala de controle do Silo Oeste.',
 1932: 'Vamos nos encontrar na Sala de controle do Silo Central.',
 1933: 'Vamos nos encontrar no Silo Leste.',
 1934: 'Vamos nos encontrar no Silo Oeste.',
 1935: 'Vamos nos encontrar no Silo Central.',
 1936: 'Vamos nos encontrar no Silo Oeste.',
 1937: 'Vamos nos encontrar no Silo Leste.',
 1938: 'Vamos nos encontrar na Passarela do Silo Leste.',
 1940: 'Vamos nos encontrar no topo do Silo Oeste.',
 1941: 'Vamos nos encontrar no topo do Silo Leste.',
 1960: 'Vamos nos encontrar no Elevador do Silo Oeste.',
 1961: 'Vamos nos encontrar no Elevador do Silo Leste.',
 2000: 'Lil\xc3\xa1s',
 2001: 'Azul',
 2002: 'Ciano',
 2003: 'Azul petr\xc3\xb3leo',
 2004: 'Verde',
 2005: 'Amarelo',
 2006: 'Laranja',
 2007: 'Vermelho',
 2008: 'Rosa',
 2009: 'Marrom',
 2100: 'Opere o guindaste.',
 2101: 'Posso operar o guindaste?',
 2102: 'Preciso de pr\xc3\xa1tica para operar o guindaste.',
 2103: 'Escolha um brutamontes desativado.',
 2104: 'Jogue o brutamontes no Diretor Financeiro.',
 2105: 'Agora jogue um cofre!',
 2106: 'N\xc3\xa3o jogue o cofre agora!',
 2107: 'O cofre vai derrubar o capacete dele.',
 2108: 'O cofre vai virar o novo capacete dele.',
 2109: 'N\xc3\xa3o consigo chegar a nenhum cofre.',
 2110: 'N\xc3\xa3o consigo chegar a nenhum brutamontes.',
 2120: 'Desative os brutamontes.',
 2121: 'Prefiro desativar os brutamontes.',
 2122: 'Preciso de pr\xc3\xa1tica para desativar brutamontes.',
 2123: 'Fique por perto.',
 2124: 'Fique circulando.',
 2125: 'Preciso circular.',
 2126: 'Procure algu\xc3\xa9m que precise de ajuda.',
 2130: 'Guarde os tesouros.',
 2131: 'Pegue os tesouros.',
 2132: 'Preciso de tesouros!',
 2133: 'Cuidado!',
 2200: 'Voc\xc3\xaa precisa acertar a balan\xc3\xa7a.',
 2201: 'Eu vou acertar a balan\xc3\xa7a.',
 2202: 'Eu preciso de ajuda com a balan\xc3\xa7a!',
 2203: 'Voc\xc3\xaa precisa atordoar os Cogs.',
 2204: 'Eu vou atordoar os Cogs.',
 2205: 'Eu preciso de ajuda com os Cogs!',
 2206: 'Eu preciso de mais evid\xc3\xaancias.',
 2207: 'Eu fico com as cadeiras da fileira de cima.',
 2208: 'Eu fico com as cadeiras da fileira de baixo.',
 2209: 'Saia da frente! N\xc3\xa3o podemos atingir o prato.',
 2210: 'Eu fa\xc3\xa7o as piadas Toonar.',
 2211: 'Eu n\xc3\xa3o tenho peso b\xc3\xb4nus.',
 2212: 'Eu tenho peso b\xc3\xb4nus de 1.',
 2213: 'Eu tenho peso b\xc3\xb4nus de 2.',
 2214: 'Eu tenho peso b\xc3\xb4nus de 3.',
 2215: 'Eu tenho peso b\xc3\xb4nus de 4.',
 2216: 'Eu tenho peso b\xc3\xb4nus de 5.',
 2217: 'Eu tenho peso b\xc3\xb4nus de 6.',
 2218: 'Eu tenho peso b\xc3\xb4nus de 7.',
 2219: 'Eu tenho peso b\xc3\xb4nus de 8.',
 2220: 'Eu tenho peso b\xc3\xb4nus de 9.',
 2221: 'Eu tenho peso b\xc3\xb4nus de 10.',
 2222: 'Eu tenho peso b\xc3\xb4nus de 11.',
 2223: 'Eu tenho peso b\xc3\xb4nus de 12.',
 2300: 'Voc\xc3\xaa alimenta os Cogs \xc3\xa0 esquerda.',
 2301: 'Vou alimentar os Cogs \xc3\xa0 esquerda.',
 2302: 'Voc\xc3\xaa alimenta os Cogs \xc3\xa0 direita.',
 2303: 'Vou alimentar os Cogs \xc3\xa0 direita.',
 2304: 'Voc\xc3\xaa alimenta os Cogs \xc3\xa0 frente.',
 2305: 'Vou alimentar os Cogs \xc3\xa0 frente.',
 2306: 'Voc\xc3\xaa alimenta os Cogs de tr\xc3\xa1s.',
 2307: 'Vou alimentar os Cogs de tr\xc3\xa1s.',
 2308: 'Voc\xc3\xaa usa a garrafa de \xc3\xa1gua com g\xc3\xa1s.',
 2309: 'Vou usar a garrafa de \xc3\xa1gua com g\xc3\xa1s.',
 2310: 'Voc\xc3\xaa usa o taco de golfe.',
 2311: 'Vou usar o taco de golfe.',
 2312: 'Vou servir esta mesa.',
 2313: 'Pode servir esta mesa?',
 2314: 'Alimente o mesmo Cog de novo.',
 2315: 'Depressa, seu Cog est\xc3\xa1 com fome!',
 2316: 'Reserve os lanches para Toons mais tristes.',
 2317: 'Pegue os lanches antes que eles caiam.',
 3010: 'Algu\xc3\xa9m quer apostar corrida?',
 3020: 'Vamos apostar corrida!',
 3030: 'Quer apostar corrida?',
 3040: 'Vamos mostrar nossos karts!',
 3050: 'N\xc3\xa3o tenho t\xc3\xadquetes suficientes.',
 3060: 'Vamos apostar outra corrida!',
 3061: 'Quer apostar outra corrida?',
 3150: 'Preciso ir \xc3\xa0 Loja do kart.',
 3160: 'Vamos para a pista de corrida!',
 3170: 'Vamos para a largada para mostrar nossos karts!',
 3180: 'Vou para a largada mostrar meu kart!',
 3190: 'A gente se encontra na pista de corrida!',
 3110: 'O ponto de encontro \xc3\xa9 a Loja do kart!',
 3130: 'Onde a gente se encontra?',
 3200: 'Onde voc\xc3\xaa quer correr?',
 3201: 'Vamos escolher uma corrida diferente.',  
 3210: 'Vamos fazer uma corrida de aquecimento.',
 3211: 'Vamos fazer um campeonato de corrida.',
 3220: 'Eu gosto da corrida do Est\xc3\xa1dio dos Nerds!',
 3221: 'Eu gosto da corrida do Aut\xc3\xb3dromo R\xc3\xbastico!',
 3222: 'Eu gosto da corrida do Circuito da Cidade!',
 3223: 'Eu gosto da corrida do Coliseu Saca-Rolhas!',
 3224: 'Eu gosto da corrida da Pista de Pulos!',
 3222: 'Eu gosto da corrida do Circuito da Cidade!',
 3230: 'Vamos correr no Est\xc3\xa1dio dos Nerds!',
 3231: 'Vamos correr no Aut\xc3\xb3dromo R\xc3\xbastico!',
 3232: 'Vamos correr no Circuito da Cidade!',
 3233: 'Vamos correr no Coliseu Saca-Rolhas!',
 3234: 'Vamos correr na Pista de Pulos!',
 3235: 'Vamos correr na Avenida da Neve!',
 3600: 'Em que pista voc\xc3\xaa quer correr?',
 3601: 'Escolha uma pista!',
 3602: 'A gente pode correr em uma pista diferente?',
 3603: 'Vamos escolher uma pista diferente!',
 3640: 'Quero correr na primeira pista!',
 3641: 'Quero correr na segunda pista!',
 3642: 'Quero correr na terceira pista!',
 3643: 'Quero correr na quarta pista!',
 3660: 'N\xc3\xa3o quero correr na primeira pista!',
 3661: 'N\xc3\xa3o quero correr na segunda pista!',
 3662: 'N\xc3\xa3o quero correr na terceira pista!',
 3663: 'N\xc3\xa3o quero correr na quarta pista!',
 3300: 'Uau! Voc\xc3\xaa \xc3\xa9 R\xc3\x81PIDO!',
 3301: 'Voc\xc3\xaa \xc3\xa9 muito r\xc3\xa1pido para mim!',
 3310: 'Boa corrida!',
 3320: 'Eu me amarrei no seu kart!',
 3330: 'Uma corrida maravilhosa!',
 3340: 'Seu kart \xc3\xa9 muito maneiro!',
 3350: 'Seu kart \xc3\xa9 incr\xc3\xadvel!',
 3360: 'Seu kart \xc3\xa9 maravilhoso!',
 3400: 'T\xc3\xa1 com medo de me enfrentar?',
 3410: 'Vejo voc\xc3\xaa na linha de chegada!',
 3430: 'Sou r\xc3\xa1pido como um raio!',
 3450: 'Voc\xc3\xaa nunca vai me alcan\xc3\xa7ar!',
 3451: 'Voc\xc3\xaa nunca vai me derrotar!',
 3452: 'Ningu\xc3\xa9m consegue bater o meu tempo!',
 3453: 'Vamos embora, molenga!',
 3460: 'Me d\xc3\xa1 outra chance!',
 3461: 'Foi sorte a sua!',
 3462: 'Uh-huu! Essa foi perto!',
 3470: 'Uau, pensei que voc\xc3\xaa tinha me vencido!',
 4000: 'Vamos jogar minigolfe!',
 4001: 'Vamos jogar de novo!',
 4002: 'Quer jogar golfe?',
 4100: 'Vamos jogar no "Tacada e Caminhada".',
 4101: 'Vamos jogar no "Tacadas Divertidas".',
 4102: 'Vamos jogar no "Todas as Tacadas".',
 4103: 'Esse percurso \xc3\xa9 f\xc3\xa1cil demais.',
 4104: 'Esse percurso \xc3\xa9 dif\xc3\xadcil demais.',
 4105: 'Esse percurso est\xc3\xa1 \xc3\xb3timo.',
 4200: 'Tente ficar mais para a esquerda.',
 4201: 'Tente ficar mais para a direita.',
 4202: 'Tente ficar bem no meio.',
 4203: 'Tente bater mais forte.',
 4204: 'Tente bater mais fraco.',
 4205: 'Tente mirar mais para a esquerda.',
 4206: 'Tente mirar mais para a direita.',
 4207: 'Tente mirar bem no meio.',
 4300: 'Por pouco!',
 4301: 'Que tacada sensacional!',
 4302: 'Essa foi uma tacada de sorte.',
 4303: 'Quero mais uma chance...',
 4304: 'Essa \xc3\xa9 muito f\xc3\xa1cil.',
 4305: 'Bola!',
 4306: 'Shhhh!',
 4307: 'Grande jogo!',
 5000: 'Vamos formar um Grupo de Abordagem.',
 5001: 'Junte-se ao meu Grupo de Abordagem.',
 5002: 'Voc\xc3\xaa pode me convidar para o seu Grupo de Abordagem',
 5003: 'Eu j\xc3\xa1 estou em um Grupo de Embarque.',
 5004: 'Deixar o seu Grupo de Abordagem.',
 5005: 'Estamos embarcando agora.',
 5006: 'Onde estamos indo?',
 5007: 'Estamos prontos?',
 5008: 'Vamos!',
 5009: 'N\xc3\xa3o saia desta \xc3\xa1rea ou sair\xc3\xa1 do Grupo de Abordagem.',
 5100: 'Vamos para o Tr\xc3\xaas da Frente.',
 5101: 'Vamos para o Seis do Meio.',
 5102: 'Vamos para o Nove de Tr\xc3\xa1s.',
 5103: 'Vamos para a Batalha do Presidente',
 5104: 'Vamos para a Batalha do S\xc3\xaanior V.P..',
 5105: 'Vamos para a Entrada Principal.',
 5106: 'Vamos para a Entrada dos Fundos.',
 5107: 'Vamos para a Mina de Moedas.',
 5108: 'Vamos para a Mina de Dinheiro',
 5109: 'Vamos para a Mina de Ouro.',
 5110: 'Vamos para a Batalha do C.F.O.',
 5111: 'Vamos para a Batalha do Juiz-Chefe.',
 5112: 'Vamos para o Escrit\xc3\xb3rio dos Rob\xc3\xb4s da Lei A.',
 5113: 'Vamos para o Escrit\xc3\xb3rio dos Rob\xc3\xb4s da Lei B.',
 5114: 'Vamos para o Escrit\xc3\xb3rio dos Rob\xc3\xb4s da Lei C.',
 5115: 'Vamos para o Escrit\xc3\xb3rio dos R\xc3\xb4bos da Lei D',
 5200: 'Estamos indo para o Tr\xc3\xaas da Frente.',
 5201: 'Estamos indo para o Seis do Meio.',
 5202: 'Estamos indo para o Nove de Tr\xc3\xa1s.',
 5203: 'Estamos indo para a Batalha do Presidente.',
 5204: 'Estamos indo para a Batalha do S\xc3\xaanior V.P..',
 5205: 'Estamos indo para a Entrada Principal.',
 5206: 'Estamos indo para a Entrada dos Fundos.',
 5207: 'Estamos indo para a Mina de Moedas.',
 5208: 'Estamos indo para a Mina de Dinheiro.',
 5209: 'Estamos indo para a Mina de Ouro',
 5210: 'Estamos indo para a Batalha do C.F.O.',
 5211: 'Estamos indo para a Batalha do Juiz-Chefe.',
 5212: 'Estamos indo para o Escrit\xc3\xb3rio do R\xc3\xb4bos da Lei A.',
 5213: 'Estamos indo para o Escrit\xc3\xb3rio do R\xc3\xb4bos da Lei B.',
 5214: 'Estamos indo para o Escrit\xc3\xb3rio do R\xc3\xb4bos da Lei C.',
 5215: 'Estamos indo para o Escrit\xc3\xb3rio do R\xc3\xb4bos da Lei D.',
 5300: 'Vamos para uma festa.',
 5301: 'Vejo voc\xc3\xaa na festa!',
 5302: 'Minha festa come\xc3\xa7ou!',
 5303: 'Venha para a minha festa!',
 5304: 'Bem-vindo \xc3\xa0 minha festa!',
 5305: 'Esta festa tem regras!',
 5306: 'Sua festa \xc3\xa9 divertida!',
 5307: '\xc3\x89 hora da festa!',
 5308: 'O tempo est\xc3\xa1 ficando para fora!',
 5309: 'Nenhum Cogs s\xc3\xa3o permitidos!',
 5310: 'Eu gosto dessa m\xc3\xbasica!',
 5311: 'Esta m\xc3\xbasica \xc3\xa9 \xc3\xb3tima!',
 5312: 'Canh\xc3\xb5es s\xc3\xa3o uma explos\xc3\xa3o!',
 5313: 'V\xc3\xaa-me salto!',
 5314: 'Trampolines s\xc3\xa3o divertidos!',
 5315: 'Deixe-nos Pegar jogo!',
 5316: 'Vamos dan\xc3\xa7ar!',
 5317: 'Para a pista de dan\xc3\xa7a!',
 5318: 'Vamos brincar de Cabo de guerra!',
 5319: 'Comece os fogos de artif\xc3\xadcio!',
 5320: 'Estes fogos de artif\xc3\xadcio s\xc3\xa3o lindos',
 5321: 'Decora\xc3\xa7\xc3\xb5es agrad\xc3\xa1veis.',
 5322: 'Eu gostaria de poder comer este bolo!',
 10000: 'A escolha \xc3\xa9 sua!',
 10001: 'Voc\xc3\xaa vai votar em quem?',
 10002: 'A minha candidata \xc3\xa9 a Galinha!',
 10003: 'Nada de caca! Vote na Vaca!',
 10004: 'N\xc3\xa3o fique no v\xc3\xa1cuo! Vote no Macaco!',
 10005: 'Mantenha o curso! Vote no Urso!',
 10006: 'Pense gordo! Vote no Porco!',
 10007: 'Vote no Bode - com ele a gente pode!',
 20000: SuitBrushOffs[None][0],
 20001: SuitBrushOffs[None][1],
 20002: SuitBrushOffs[None][2],
 20003: SuitBrushOffs[None][3],
 20004: SuitBrushOffs[None][4],
 20005: SuitFaceoffTaunts['bf'][0],
 20006: SuitFaceoffTaunts['bf'][1],
 20007: SuitFaceoffTaunts['bf'][2],
 20008: SuitFaceoffTaunts['bf'][3],
 20009: SuitFaceoffTaunts['bf'][4],
 20010: SuitFaceoffTaunts['bf'][5],
 20011: SuitFaceoffTaunts['bf'][6],
 20012: SuitFaceoffTaunts['bf'][7],
 20013: SuitFaceoffTaunts['bf'][8],
 20014: SuitFaceoffTaunts['bf'][9],
 20015: SuitFaceoffTaunts['nc'][0],
 20016: SuitFaceoffTaunts['nc'][1],
 20017: SuitFaceoffTaunts['nc'][2],
 20018: SuitFaceoffTaunts['nc'][3],
 20019: SuitFaceoffTaunts['nc'][4],
 20020: SuitFaceoffTaunts['nc'][5],
 20021: SuitFaceoffTaunts['nc'][6],
 20022: SuitFaceoffTaunts['nc'][7],
 20023: SuitFaceoffTaunts['nc'][8],
 20024: SuitFaceoffTaunts['nc'][9],
 20025: SuitFaceoffTaunts['ym'][0],
 20026: SuitFaceoffTaunts['ym'][1],
 20027: SuitFaceoffTaunts['ym'][2],
 20028: SuitFaceoffTaunts['ym'][3],
 20029: SuitFaceoffTaunts['ym'][4],
 20030: SuitFaceoffTaunts['ym'][5],
 20031: SuitFaceoffTaunts['ym'][6],
 20032: SuitFaceoffTaunts['ym'][7],
 20033: SuitFaceoffTaunts['ym'][8],
 20034: SuitFaceoffTaunts['ym'][9],
 20035: SuitFaceoffTaunts['ym'][10],
 20036: SuitFaceoffTaunts['ms'][0],
 20037: SuitFaceoffTaunts['ms'][1],
 20038: SuitFaceoffTaunts['ms'][2],
 20039: SuitFaceoffTaunts['ms'][3],
 20040: SuitFaceoffTaunts['ms'][4],
 20041: SuitFaceoffTaunts['ms'][5],
 20042: SuitFaceoffTaunts['ms'][6],
 20043: SuitFaceoffTaunts['ms'][7],
 20044: SuitFaceoffTaunts['ms'][8],
 20045: SuitFaceoffTaunts['ms'][9],
 20046: SuitFaceoffTaunts['ms'][10],
 20047: SuitFaceoffTaunts['bc'][0],
 20048: SuitFaceoffTaunts['bc'][1],
 20049: SuitFaceoffTaunts['bc'][2],
 20050: SuitFaceoffTaunts['bc'][3],
 20051: SuitFaceoffTaunts['bc'][4],
 20052: SuitFaceoffTaunts['bc'][5],
 20053: SuitFaceoffTaunts['bc'][6],
 20054: SuitFaceoffTaunts['bc'][7],
 20055: SuitFaceoffTaunts['bc'][8],
 20056: SuitFaceoffTaunts['bc'][9],
 20057: SuitFaceoffTaunts['bc'][10],
 20058: SuitFaceoffTaunts['cc'][0],
 20059: SuitFaceoffTaunts['cc'][1],
 20060: SuitFaceoffTaunts['cc'][2],
 20061: SuitFaceoffTaunts['cc'][3],
 20062: SuitFaceoffTaunts['cc'][4],
 20063: SuitFaceoffTaunts['cc'][5],
 20064: SuitFaceoffTaunts['cc'][6],
 20065: SuitFaceoffTaunts['cc'][7],
 20066: SuitFaceoffTaunts['cc'][8],
 20067: SuitFaceoffTaunts['cc'][9],
 20068: SuitFaceoffTaunts['cc'][10],
 20069: SuitFaceoffTaunts['cc'][11],
 20070: SuitFaceoffTaunts['cc'][12],
 20071: SuitFaceoffTaunts['nd'][0],
 20072: SuitFaceoffTaunts['nd'][1],
 20073: SuitFaceoffTaunts['nd'][2],
 20074: SuitFaceoffTaunts['nd'][3],
 20075: SuitFaceoffTaunts['nd'][4],
 20076: SuitFaceoffTaunts['nd'][5],
 20077: SuitFaceoffTaunts['nd'][6],
 20078: SuitFaceoffTaunts['nd'][7],
 20079: SuitFaceoffTaunts['nd'][8],
 20080: SuitFaceoffTaunts['nd'][9],
 20081: SuitFaceoffTaunts['ac'][0],
 20082: SuitFaceoffTaunts['ac'][1],
 20083: SuitFaceoffTaunts['ac'][2],
 20084: SuitFaceoffTaunts['ac'][3],
 20085: SuitFaceoffTaunts['ac'][4],
 20086: SuitFaceoffTaunts['ac'][5],
 20087: SuitFaceoffTaunts['ac'][6],
 20088: SuitFaceoffTaunts['ac'][7],
 20089: SuitFaceoffTaunts['ac'][8],
 20090: SuitFaceoffTaunts['ac'][9],
 20091: SuitFaceoffTaunts['ac'][10],
 20092: SuitFaceoffTaunts['ac'][11],
 20093: SuitFaceoffTaunts['tf'][0],
 20094: SuitFaceoffTaunts['tf'][1],
 20095: SuitFaceoffTaunts['tf'][2],
 20096: SuitFaceoffTaunts['tf'][3],
 20097: SuitFaceoffTaunts['tf'][4],
 20098: SuitFaceoffTaunts['tf'][5],
 20099: SuitFaceoffTaunts['tf'][6],
 20100: SuitFaceoffTaunts['tf'][7],
 20101: SuitFaceoffTaunts['tf'][8],
 20102: SuitFaceoffTaunts['tf'][9],
 20103: SuitFaceoffTaunts['tf'][10],
 20104: SuitFaceoffTaunts['hh'][0],
 20105: SuitFaceoffTaunts['hh'][1],
 20106: SuitFaceoffTaunts['hh'][2],
 20107: SuitFaceoffTaunts['hh'][3],
 20108: SuitFaceoffTaunts['hh'][4],
 20109: SuitFaceoffTaunts['hh'][5],
 20110: SuitFaceoffTaunts['hh'][6],
 20111: SuitFaceoffTaunts['hh'][7],
 20112: SuitFaceoffTaunts['hh'][8],
 20113: SuitFaceoffTaunts['hh'][9],
 20114: SuitFaceoffTaunts['hh'][10],
 20115: SuitFaceoffTaunts['le'][0],
 20116: SuitFaceoffTaunts['le'][1],
 20117: SuitFaceoffTaunts['le'][2],
 20118: SuitFaceoffTaunts['le'][3],
 20119: SuitFaceoffTaunts['le'][4],
 20120: SuitFaceoffTaunts['le'][5],
 20121: SuitFaceoffTaunts['le'][6],
 20122: SuitFaceoffTaunts['le'][7],
 20123: SuitFaceoffTaunts['le'][8],
 20124: SuitFaceoffTaunts['le'][9],
 20125: SuitFaceoffTaunts['bs'][0],
 20126: SuitFaceoffTaunts['bs'][1],
 20127: SuitFaceoffTaunts['bs'][2],
 20128: SuitFaceoffTaunts['bs'][3],
 20129: SuitFaceoffTaunts['bs'][4],
 20130: SuitFaceoffTaunts['bs'][5],
 20131: SuitFaceoffTaunts['bs'][6],
 20132: SuitFaceoffTaunts['bs'][7],
 20133: SuitFaceoffTaunts['bs'][8],
 20134: SuitFaceoffTaunts['bs'][9],
 20135: SuitFaceoffTaunts['bs'][10],
 20136: SuitFaceoffTaunts['cr'][0],
 20137: SuitFaceoffTaunts['cr'][1],
 20138: SuitFaceoffTaunts['cr'][2],
 20139: SuitFaceoffTaunts['cr'][3],
 20140: SuitFaceoffTaunts['cr'][4],
 20141: SuitFaceoffTaunts['cr'][5],
 20142: SuitFaceoffTaunts['cr'][6],
 20143: SuitFaceoffTaunts['cr'][7],
 20144: SuitFaceoffTaunts['cr'][8],
 20145: SuitFaceoffTaunts['cr'][9],
 20146: SuitFaceoffTaunts['tbc'][0],
 20147: SuitFaceoffTaunts['tbc'][1],
 20148: SuitFaceoffTaunts['tbc'][2],
 20149: SuitFaceoffTaunts['tbc'][3],
 20150: SuitFaceoffTaunts['tbc'][4],
 20151: SuitFaceoffTaunts['tbc'][5],
 20152: SuitFaceoffTaunts['tbc'][6],
 20153: SuitFaceoffTaunts['tbc'][7],
 20154: SuitFaceoffTaunts['tbc'][8],
 20155: SuitFaceoffTaunts['tbc'][9],
 20156: SuitFaceoffTaunts['tbc'][10],
 20157: SuitFaceoffTaunts['ds'][0],
 20158: SuitFaceoffTaunts['ds'][1],
 20159: SuitFaceoffTaunts['ds'][2],
 20160: SuitFaceoffTaunts['ds'][3],
 20161: SuitFaceoffTaunts['ds'][4],
 20162: SuitFaceoffTaunts['ds'][5],
 20163: SuitFaceoffTaunts['ds'][6],
 20164: SuitFaceoffTaunts['ds'][7],
 20165: SuitFaceoffTaunts['gh'][0],
 20166: SuitFaceoffTaunts['gh'][1],
 20167: SuitFaceoffTaunts['gh'][2],
 20168: SuitFaceoffTaunts['gh'][3],
 20169: SuitFaceoffTaunts['gh'][4],
 20170: SuitFaceoffTaunts['gh'][5],
 20171: SuitFaceoffTaunts['gh'][6],
 20172: SuitFaceoffTaunts['gh'][7],
 20173: SuitFaceoffTaunts['gh'][8],
 20174: SuitFaceoffTaunts['gh'][9],
 20175: SuitFaceoffTaunts['gh'][10],
 20176: SuitFaceoffTaunts['gh'][11],
 20177: SuitFaceoffTaunts['gh'][12],
 20178: SuitFaceoffTaunts['pp'][0],
 20179: SuitFaceoffTaunts['pp'][1],
 20180: SuitFaceoffTaunts['pp'][2],
 20181: SuitFaceoffTaunts['pp'][3],
 20182: SuitFaceoffTaunts['pp'][4],
 20183: SuitFaceoffTaunts['pp'][5],
 20184: SuitFaceoffTaunts['pp'][6],
 20185: SuitFaceoffTaunts['pp'][7],
 20186: SuitFaceoffTaunts['pp'][8],
 20187: SuitFaceoffTaunts['pp'][9],
 20188: SuitFaceoffTaunts['b'][0],
 20189: SuitFaceoffTaunts['b'][1],
 20190: SuitFaceoffTaunts['b'][2],
 20191: SuitFaceoffTaunts['b'][3],
 20192: SuitFaceoffTaunts['b'][4],
 20193: SuitFaceoffTaunts['b'][5],
 20194: SuitFaceoffTaunts['b'][6],
 20195: SuitFaceoffTaunts['b'][7],
 20196: SuitFaceoffTaunts['b'][8],
 20197: SuitFaceoffTaunts['b'][9],
 20198: SuitFaceoffTaunts['b'][10],
 20199: SuitFaceoffTaunts['b'][11],
 20200: SuitFaceoffTaunts['f'][0],
 20201: SuitFaceoffTaunts['f'][1],
 20202: SuitFaceoffTaunts['f'][2],
 20203: SuitFaceoffTaunts['f'][3],
 20204: SuitFaceoffTaunts['f'][4],
 20205: SuitFaceoffTaunts['f'][5],
 20206: SuitFaceoffTaunts['f'][6],
 20207: SuitFaceoffTaunts['f'][7],
 20208: SuitFaceoffTaunts['f'][8],
 20209: SuitFaceoffTaunts['f'][9],
 20210: SuitFaceoffTaunts['f'][10],
 20211: SuitFaceoffTaunts['mm'][0],
 20212: SuitFaceoffTaunts['mm'][1],
 20213: SuitFaceoffTaunts['mm'][2],
 20214: SuitFaceoffTaunts['mm'][3],
 20215: SuitFaceoffTaunts['mm'][4],
 20216: SuitFaceoffTaunts['mm'][5],
 20217: SuitFaceoffTaunts['mm'][6],
 20218: SuitFaceoffTaunts['mm'][7],
 20219: SuitFaceoffTaunts['mm'][8],
 20220: SuitFaceoffTaunts['mm'][9],
 20221: SuitFaceoffTaunts['mm'][10],
 20222: SuitFaceoffTaunts['mm'][11],
 20223: SuitFaceoffTaunts['mm'][12],
 20224: SuitFaceoffTaunts['mm'][13],
 20225: SuitFaceoffTaunts['tw'][0],
 20226: SuitFaceoffTaunts['tw'][1],
 20227: SuitFaceoffTaunts['tw'][2],
 20228: SuitFaceoffTaunts['tw'][3],
 20229: SuitFaceoffTaunts['tw'][4],
 20230: SuitFaceoffTaunts['tw'][5],
 20231: SuitFaceoffTaunts['tw'][6],
 20232: SuitFaceoffTaunts['tw'][7],
 20233: SuitFaceoffTaunts['tw'][8],
 20234: SuitFaceoffTaunts['tw'][9],
 20235: SuitFaceoffTaunts['tw'][10],
 20236: SuitFaceoffTaunts['mb'][0],
 20237: SuitFaceoffTaunts['mb'][1],
 20238: SuitFaceoffTaunts['mb'][2],
 20239: SuitFaceoffTaunts['mb'][3],
 20240: SuitFaceoffTaunts['mb'][4],
 20241: SuitFaceoffTaunts['mb'][5],
 20242: SuitFaceoffTaunts['mb'][6],
 20243: SuitFaceoffTaunts['mb'][7],
 20244: SuitFaceoffTaunts['mb'][8],
 20245: SuitFaceoffTaunts['mb'][9],
 20246: SuitFaceoffTaunts['m'][0],
 20247: SuitFaceoffTaunts['m'][1],
 20248: SuitFaceoffTaunts['m'][2],
 20249: SuitFaceoffTaunts['m'][3],
 20250: SuitFaceoffTaunts['m'][4],
 20251: SuitFaceoffTaunts['m'][5],
 20252: SuitFaceoffTaunts['m'][6],
 20253: SuitFaceoffTaunts['m'][7],
 20254: SuitFaceoffTaunts['m'][8],
 20255: SuitFaceoffTaunts['mh'][0],
 20256: SuitFaceoffTaunts['mh'][1],
 20257: SuitFaceoffTaunts['mh'][2],
 20258: SuitFaceoffTaunts['mh'][3],
 20259: SuitFaceoffTaunts['mh'][4],
 20260: SuitFaceoffTaunts['mh'][5],
 20261: SuitFaceoffTaunts['mh'][6],
 20262: SuitFaceoffTaunts['mh'][7],
 20263: SuitFaceoffTaunts['mh'][8],
 20264: SuitFaceoffTaunts['mh'][9],
 20265: SuitFaceoffTaunts['mh'][10],
 20266: SuitFaceoffTaunts['mh'][11],
 20267: SuitFaceoffTaunts['dt'][0],
 20268: SuitFaceoffTaunts['dt'][1],
 20269: SuitFaceoffTaunts['dt'][2],
 20270: SuitFaceoffTaunts['dt'][3],
 20271: SuitFaceoffTaunts['dt'][4],
 20272: SuitFaceoffTaunts['dt'][5],
 20273: SuitFaceoffTaunts['dt'][6],
 20274: SuitFaceoffTaunts['dt'][7],
 20275: SuitFaceoffTaunts['dt'][8],
 20276: SuitFaceoffTaunts['dt'][9],
 20277: SuitFaceoffTaunts['p'][0],
 20278: SuitFaceoffTaunts['p'][1],
 20279: SuitFaceoffTaunts['p'][2],
 20280: SuitFaceoffTaunts['p'][3],
 20281: SuitFaceoffTaunts['p'][4],
 20282: SuitFaceoffTaunts['p'][5],
 20283: SuitFaceoffTaunts['p'][6],
 20284: SuitFaceoffTaunts['p'][7],
 20285: SuitFaceoffTaunts['p'][8],
 20286: SuitFaceoffTaunts['p'][9],
 20287: SuitFaceoffTaunts['p'][10],
 20288: SuitFaceoffTaunts['tm'][0],
 20289: SuitFaceoffTaunts['tm'][1],
 20290: SuitFaceoffTaunts['tm'][2],
 20291: SuitFaceoffTaunts['tm'][3],
 20292: SuitFaceoffTaunts['tm'][4],
 20293: SuitFaceoffTaunts['tm'][5],
 20294: SuitFaceoffTaunts['tm'][6],
 20295: SuitFaceoffTaunts['tm'][7],
 20296: SuitFaceoffTaunts['tm'][8],
 20297: SuitFaceoffTaunts['tm'][9],
 20298: SuitFaceoffTaunts['tm'][10],
 20299: SuitFaceoffTaunts['bw'][0],
 20300: SuitFaceoffTaunts['bw'][1],
 20301: SuitFaceoffTaunts['bw'][2],
 20302: SuitFaceoffTaunts['bw'][3],
 20303: SuitFaceoffTaunts['bw'][4],
 20304: SuitFaceoffTaunts['bw'][5],
 20305: SuitFaceoffTaunts['bw'][6],
 20306: SuitFaceoffTaunts['bw'][7],
 20307: SuitFaceoffTaunts['bw'][8],
 20308: SuitFaceoffTaunts['bw'][9],
 20309: SuitFaceoffTaunts['ls'][0],
 20310: SuitFaceoffTaunts['ls'][1],
 20311: SuitFaceoffTaunts['ls'][2],
 20312: SuitFaceoffTaunts['ls'][3],
 20313: SuitFaceoffTaunts['ls'][4],
 20314: SuitFaceoffTaunts['ls'][5],
 20315: SuitFaceoffTaunts['ls'][6],
 20316: SuitFaceoffTaunts['ls'][7],
 20317: SuitFaceoffTaunts['ls'][8],
 20318: SuitFaceoffTaunts['ls'][9],
 20319: SuitFaceoffTaunts['ls'][10],
 20320: SuitFaceoffTaunts['rb'][0],
 20321: SuitFaceoffTaunts['rb'][1],
 20322: SuitFaceoffTaunts['rb'][2],
 20323: SuitFaceoffTaunts['rb'][3],
 20324: SuitFaceoffTaunts['rb'][4],
 20325: SuitFaceoffTaunts['rb'][5],
 20326: SuitFaceoffTaunts['rb'][6],
 20327: SuitFaceoffTaunts['rb'][7],
 20328: SuitFaceoffTaunts['rb'][8],
 20329: SuitFaceoffTaunts['rb'][9],
 20330: SuitFaceoffTaunts['sc'][0],
 20331: SuitFaceoffTaunts['sc'][1],
 20332: SuitFaceoffTaunts['sc'][2],
 20333: SuitFaceoffTaunts['sc'][3],
 20334: SuitFaceoffTaunts['sc'][4],
 20335: SuitFaceoffTaunts['sc'][5],
 20336: SuitFaceoffTaunts['sc'][6],
 20337: SuitFaceoffTaunts['sc'][7],
 20338: SuitFaceoffTaunts['sc'][8],
 20339: SuitFaceoffTaunts['sc'][9],
 20340: SuitFaceoffTaunts['sc'][10],
 20341: SuitFaceoffTaunts['sd'][0],
 20342: SuitFaceoffTaunts['sd'][1],
 20343: SuitFaceoffTaunts['sd'][2],
 20344: SuitFaceoffTaunts['sd'][3],
 20345: SuitFaceoffTaunts['sd'][4],
 20346: SuitFaceoffTaunts['sd'][5],
 20347: SuitFaceoffTaunts['sd'][6],
 20348: SuitFaceoffTaunts['sd'][7],
 20349: SuitFaceoffTaunts['sd'][8],
 20350: SuitFaceoffTaunts['sd'][9],
 21000: 'Aqui, amig\xc3\xa3o!',
 21001: 'Aqui, amigona!',
 21002: 'Parado.',
 21003: 'Bom garoto!',
 21004: 'Boa menina!',
 21005: 'Rabisco bonzinho.',
 21006: 'Por favor, n\xc3\xa3o me chateie.',
 21200: 'Pula!',
 21201: 'D\xc3\xa1 a pata!',
 21202: 'Finge de morto!',
 21203: 'Rola!',
 21204: 'Faz cambalhota!',
 21205: 'Dan\xc3\xa7a!',
 21206: 'Fala!',
 30100: 'Feliz Semana da mentira Toons!',
 30101: 'Bem-vindo \xc3\xa0 minha festa da Semana da mentira dos Toons!',
 30102: 'O Medidor de Bobagem est\xc3\xa1 de volta ao Prefeitoona!',
 30110: 'Mickey est\xc3\xa1 no Jardim da Margarida.',
 30111: 'Margarida est\xc3\xa1 em Centro de Toontown.',
 30112: 'Minnie est\xc3\xa1 no Brrrgh.',
 30113: 'Pluto est\xc3\xa1 na Melodil\xc3\xa2ndia.',
 30114: 'Donald est\xc3\xa1 son\xc3\xa2mbulo no aut\xc3\xb3dromo.',
 30115: 'O Pateta est\xc3\xa1 na Sonhol\xc3\xa2ndia.',
 30120: 'Mickey est\xc3\xa1 agindo como Margarida!',
 30121: 'Margarida est\xc3\xa1 agindo como Mickey!',
 30122: 'Minnie est\xc3\xa1 agindo como Pluto!',
 30123: 'Pluto est\xc3\xa1 agindo como Minnie!',
 30124: 'Pluto est\xc3\xa1 falando!',
 30125: 'Pateta est\xc3\xa1 agindo como Donald!',
 30126: 'Donald est\xc3\xa1 sonhando que \xc3\xa9 o Pateta!',
 30130: 'Observe at\xc3\xa9 onde consigo pular.',
 30131: 'Nossa, voc\xc3\xaa pulou muito longe!',
 30132: 'Ei, Rabiscos podem, falar!',
 30133: 'Seu Rabisco acabou de falar?',
 30140: 'As coisas com certeza s\xc3\xa3o bobas por aqui!',
 30141: 'Qu\xc3\xa3o mais bobas as coisas poderiam ficar?',
 30150: 'Opera\xc3\xa7\xc3\xa3o: Tempestade dos Rob\xc3\xb4s Vendedores est\xc3\xa1 aqui!',
 30151: 'Torres dos Rob\xc3\xb4s Vendedores teve sua energia drenada por Rabiscos!',
 30152: 'O S\xc3\xaanior VP teve seu poder drenado por Rabiscos!',
 30153: 'Todos podem lutar contra o  S\xc3\xaanior VP agora mesmo!',
 30154: 'Voc\xc3\xaa n\xc3\xa3o precisa de um disfarce de Rob\xc3\xb4 Vendedores para lutar contra o VP!',
 30155: 'Voc\xc3\xaa ganha um Terno Alugado quando entra nas Torres dos Rob\xc3\xb4s Vendedores.',
 30156: 'Voc\xc3\xaa gostou do meu traje de aluguel? Desculpe pelos alfinetes de seguran\xc3\xa7a!',
 30157: '\xc3\x89 melhor ter oito Toons para lutar contra o s\xc3\xaanior VP.',
 30158: 'Voc\xc3\xaa vai me ajudar a lutar contra o s\xc3\xaanior VP?',
 30159: 'Voc\xc3\xaa quer lutar contra o s\xc3\xaanior VP comigo?',
 30160: 'Voc\xc3\xaa gostaria de se juntar ao meu grupo Rob\xc3\xb4s Vendedores s\xc3\xaanior VP?',
 30161: 'Estou procurando um Toon com Traje Alugado para lutar contra o s\xc3\xaanior VP.',
 30162: 'Eu tenho um traje de aluguel e estou querendo lutar contra o  s\xc3\xaanior VP.',
 30163: 'Basta passar pelas portas para pegar seu traje de aluguel.',
 30164: 'Guarde suas piadas para os Cogs l\xc3\xa1 dentro!',
 30165: 'Temos que derrotar esses Cogs primeiro!',
 30166: 'Bata nos barris para piada subir.',
 30167: 'Bata no cano para conseguir um Toonar.',
 30168: 'Agora temos que lutar contra alguns EsqueletosCogs!',
 30169: 'Salte e toque na gaiola do Toon para pegar tortas!',
 30170: 'Agora lutamos contra o s\xc3\xaanior VP!',
 30171: 'Mire suas tortas pressionando o bot\xc3\xa3o Delete.',
 30172: 'Dois Toons deveriam jogar tortas pelas portas abertas do VP!',
 30173: 'Vou atordoar o s\xc3\xaanior VP pela frente.',
 30174: 'Vou atordoar o s\xc3\xaanior VP pelas costas.',
 30175: 'Pule quando o s\xc3\xaanior VP pular!',
 30180: 'Tenho balinhas duplas no carrinho!',
 30181: 'Ganhei balinhas duplas na pesca!',
 30182: 'Ganhei Balinhas duplas em uma festa!',
 30183: 'Balinhas  balinhas balinhas!',
 30184: 'Estou com muita vontade de ganhar uma bala!',
 30185: 'N\xc3\xa3o seja fedorento, pegue balinha!',
 30186: 'Vou adotar um Rasbico com todas essas balinhas!',
 30187: 'Em que vou gastar todas essas balinhas?',
 30188: 'Vou dar uma grande festa!',
 30189: 'Vou decorar toda a minha propriedade!',
 30190: 'Vou comprar um guarda-roupa totalmente novo!',
 30191: 'Balinhas, por favor!',
 30192: 'N\xc3\xa3o seja mau, d\xc3\xaa um feij\xc3\xa3o!',
 30193: 'Quem quer balinhas?',
 30194: 'Dance para balinhas!',
 30200: 'Hoje \xc3\xa9 dia de Alegria...',
 30201: 'Coloque algumas tortas...',
 30202: 'Toons alegres...',
 30203: 'Cabe\xc3\xa7as de boneco de neve...',
 30204: 'Toontown \xc3\xa9 alegre...',
 30205: 'Isca bom \xc3\xa2nimo...',
 30220: 'Hoje \xc3\xa9 dia de Alegria com spray de \xc3\xa1gua com g\xc3\xa1s!\nBoas festas de inverno!',
 30221: 'Coloque algumas tortas em seu tren\xc3\xb3!\nBoas festas de inverno!',
 30222: 'Toons alegres trazem consterna\xc3\xa7\xc3\xa3o aos Cogs!\nBoas festas de inverno!',
 30223: 'As cabe\xc3\xa7as dos bonecos de neve est\xc3\xa3o quentes hoje!\nBoas f\xc3\xa9rias de inverno!',
 30224: 'Toontown \xc3\xa9 alegre, aconte\xc3\xa7a o que acontecer!\nBoas festas de inverno!',
 30225: 'Isca a alegria do jeito Toontown!\nBoas f\xc3\xa9rias de inverno!',
 30250: 'Buu!',
 30251: 'Feliz Dia das Bruxas!',
 30252: 'Assustador!',
 30275: 'Boas festas!',
 30276: 'Cumprimentos de temporada!',
 30277: 'Tenha um inverno maravilhoso!',
 30301: 'Voc\xc3\xaa viu o Medidor de Bobagem?',
 30302: 'O medidor de bobagem est\xc3\xa1 na Prefeitoona.',
 30303: 'As coisas com certeza est\xc3\xa3o ficando bobas por aqui!',
 30304: 'Eu vi um hidrante se mexendo!',
 30305: 'Toontown est\xc3\xa1 ganhando vida!',
 30306: 'Voc\xc3\xaa j\xc3\xa1 esteve no novo escrit\xc3\xb3rio do Flippy?',
 30307: 'Eu causei um Surto Bobo em batalha!',
 30308: 'Vamos derrotar alguns Cogs para deixar Toontown mais boba!',
 30309: 'O Medidor de Bobagem est\xc3\xa1 maior e mais louco do que nunca!',
 30310: 'Muitos hidrantes ganharam vida!',
 30311: 'Vi uma caixa de correio se mexendo!',
 30312: 'Eu vi uma lata de lixo acordar!',
 30313: 'Qu\xc3\xa3o bobo isso pode ser?',
 30314: 'O que vai acontecer a seguir?',
 30315: 'Algo bobo, aposto!',
 30316: 'Voc\xc3\xaa j\xc3\xa1 causou um Surto Bobo?',
 30317: 'Vamos derrotar alguns Cogs para deixar Toontown mais boba!',
 30318: 'Invas\xc3\xa3o da cog!',
 30319: 'Chegando!',
 30320: 'Vamos parar esses cogs!',
 30321: 'Sinto falta dos Surtos Bobos!',
 30322: 'Vamos impedir uma invas\xc3\xa3o!',
 30323: 'Toontown est\xc3\xa1 mais bobo do que nunca!',
 30324: 'Voc\xc3\xaa viu algo ganhar vida?',
 30325: 'Meus favoritos s\xc3\xa3o os hidrantes!',
 30326: 'Minhas favoritas s\xc3\xa3o as caixas de correio!',
 30327: 'Meus favoritos s\xc3\xa3o as latas de lixo!',
 30328: 'Viva! Paramos as invas\xc3\xb5es dos Cogs!',
 30329: 'Um hidrante me ajudou na batalha!',
 30330: 'Um hidrante impulsionou minhas Piadas de Esguicho!',
 30331: 'Uma lata de lixo impulsionou minhas Piadas de Toonar!',
 30332: 'Uma caixa de correio ajudou minhas Piadas de Lan\xc3\xa7amento!',
 30350: 'Bem-vindo \xc3\xa0 minha Festa da Vit\xc3\xb3ria!',
 30351: 'Esta \xc3\xa9 uma grande Festa da Vit\xc3\xb3ria!',
 30352: 'Mostramos \xc3\xa0queles Cogs quem \xc3\xa9 que manda!',
 30353: 'Bom trabalho ajudando a acabar com as invas\xc3\xb5es Cog!',
 30354: 'Aposto que isso est\xc3\xa1 deixando os Cogs loucos!',
 30355: 'Vamos jogar Cog-De-Guerra!',
 30356: 'Meu time venceu no Cog-De-Guerra!',
 30357: '\xc3\x89 bom ter hidrantes, latas de lixo, e caixas de correio aqui!',
 30358: 'Gosto do bal\xc3\xa3o do Rabisco mordendo o cog!',
 30359: 'Gosto do bal\xc3\xa3o do Cog coberto de sorvete!',
 30360: 'Gosto do cog ondulado que bate os bra\xc3\xa7os!',
 30361: 'Eu pulei na cara de um Cog!',
 30400: 'Os Rob\xc3\xb4s Vendedores est\xc3\xa3o invadindo!',
 30401: 'O s\xc3\xaanior VP estava louco com a Opera\xc3\xa7\xc3\xa3o: Storm Sellbot ...',
 30402: 'Ele est\xc3\xa1 enviando os Rob\xc3\xb4s Vendedores para invadir Toontown!',
 30403: 'Vamos lutar contra alguns Rob\xc3\xb4s Vendedores!',
 30404: 'H\xc3\xa1 um novo tipo de constru\xc3\xa7\xc3\xa3o em Toontown!',
 30405: 'Voc\xc3\xaa viu os escrit\xc3\xb3rios de campo dos Agitadores?',
 30406: 'O s\xc3\xaanior VP os criou como uma recompensa para os Agitadores.',
 30407: 'Vamos derrotar um Escrit\xc3\xb3rio de Campo!',
 30408: 'Recebi um cart\xc3\xa3o SOS por derrotar um Escrit\xc3\xb3rio de Campo!',
 30409: 'Limpe o mapa explorando o labirinto.',
 30410: 'Destrua os cogs acertando-as com bal\xc3\xb5es de \xc3\xa1gua!',
 30411: 'Agitadores levam dois bal\xc3\xb5es para destruir.',
 30412: 'Cuidado com a queda de objetos!',
 30413: 'Cuidado com as cogs!',
 30414: 'Colete piadas para obter um Toonar no final!',
 30415: 'Quando a sala treme, um Agitador est\xc3\xa1 por perto.',
 30416: 'Derrote todos os quatros Agitadores para abrir a sa\xc3\xadda!',
 30417: 'A sa\xc3\xadda est\xc3\xa1 aberta!',
 30418: '\xc3\x89 o chefe!',
 30450: '\xc3\x89 f\xc3\xa1cil ser verde!',
 30451: 'Visite Jeans Feij\xc3\xa3o Verde e voc\xc3\xaa tamb\xc3\xa9m pode ser verde!',
 30452: 'Fica na Rua dos Carvalhos em Jardins da Margarida.'}
SpeedChatStaticTextPirates = {50001: 'Sim',
 50002: 'N\xc3\xa3o',
 50003: 'Arrr!',
 50004: 'Sim, sim, Capit\xc3\xa3o!',
 50005: 'Ok',
 50100: 'Todos a bordo!',
 50101: 'Ei, marujo!',
 50102: 'Alto l\xc3\xa1!',
 50103: 'Abram caminho!',
 50104: 'Caramba!',
 50105: 'Me explodiram!',
 50106: 'Ei, voc\xc3\xaa!',
 50107: 'Claro, claro, Capit\xc3\xa3o!',
 50108: 'Ande na prancha!',
 50700: 'Ah!',
 50701: 'Ah, amigo!',
 50702: 'Yo-Ho-Ho',
 50703: 'Avast!',
 50704: 'Ei, Bucko.',
 50800: 'At\xc3\xa9 a pr\xc3\xb3xima.',
 50801: 'Que bons ventos encontrem voc\xc3\xaa.',
 50802: 'Boa velocidade.',
 50900: 'Como vai, amigo?',
 50901: '',
 51000: '\xc3\x89 como se o c\xc3\xa9u estivesse chovendo dobr\xc3\xb5es de ouro!',
 51001: 'Que o vento sopre forte, o sol aque\xc3\xa7a nossas faces e os canh\xc3\xb5es disparem certeiros!',
 51100: 'Eu estive navegando em \xc3\xa1guas agitadas neste dia.',
 51200: 'Minhas desculpas, cara.',
 51201: 'Desculpe.',
 51202: 'Desculpe, eu estava ocupado antes.',
 51203: 'Desculpe, j\xc3\xa1 tenho planos.',
 51204: 'Desculpe, n\xc3\xa3o preciso fazer isso.',
 51300: 'Ataque o mais fraco!',
 51301: 'Ataque o mais forte!',
 51302: 'Ataque meu alvo!',
 51303: 'Preciso de ajuda!',
 51304: 'N\xc3\xa3o posso causar nenhum dano!',
 51305: 'Acho que estamos com problemas.',
 51306: 'Cerque o mais poderoso.',
 51307: 'Dev\xc3\xadamos recuar.',
 51308: 'Corra!',
 51400: 'Dispare um Broadside!',
 51401: 'Bombordo! (esquerda)',
 51402: 'Lado de estibordo! (direita)',
 51403: 'Chegando!',
 51404: 'Vamos l\xc3\xa1!',
 51405: 'Broadside! Proteja-se!',
 51406: 'Para os Canh\xc3\xb5es!',
 51407: 'Abra fogo!',
 51408: 'Segure o fogo!',
 51409: 'Mire nos mastros!',
 51410: 'Mire no casco!',
 51411: 'Prepare-se para embarcar!',
 51412: 'Ela est\xc3\xa1 chegando.',
 51413: 'Velocidade de for\xc3\xa7a!',
 51414: 'N\xc3\xb3s a temos em fuga.',
 51415: 'Estamos entrando na \xc3\xa1gua.',
 51416: 'N\xc3\xa3o aguentamos mais.',
 51417: 'N\xc3\xa3o tenho chance!',
 51418: 'Vamos encontrar uma porta para reparo.',
 51419: 'Homem ao mar!',
 51420: 'Inimigo avistado.',
 51421: 'Bonito agora, homens!',
 50400: 'Vamos zarpar.',
 50401: 'Vamos sair daqui.',
 51500: 'Vamos navegar para Port Royal.',
 51501: 'Vamos navegar para Tortuga.',
 51502: 'Vamos navegar para Padres Del Fuego.',
 51503: "Vamos navegar para Devil's Anvil.",
 51504: 'Vamos navegar para Kingshead.',
 51505: 'Vamos navegar para Isla Perdida.',
 51506: 'Vamos navegar para Cuba.',
 51507: 'Vamos navegar para Tormenta.',
 51508: 'Vamos navegar para Outcast Isle.',
 51509: 'Vamos navegar para Driftwood.',
 51510: 'Vamos navegar para Cutthroat.',
 51511: "Vamos navegar para Rumrunner's Isle.",
 51512: 'Vamos navegar para Isla Cangrejos.',
 51600: 'Vamos para a cidade.',
 51601: 'Vamos para as docas.',
 51602: 'Vamos para o bar.',
 51800: 'Vamos para o Forte Charles.',
 51801: 'Vamos para a Mans\xc3\xa3o do Governador.',
 52500: 'Onde estou?',
 51700: 'Voc\xc3\xaa j\xc3\xa1 est\xc3\xa1 l\xc3\xa1.',
 51701: 'N\xc3\xa3o sei.',
 51702: 'Voc\xc3\xaa est\xc3\xa1 na ilha errada.',
 51703: 'Isso \xc3\xa9 na cidade.',
 51704: 'Olhe fora da cidade.',
 51705: 'Voc\xc3\xaa ter\xc3\xa1 que procurar na selva.',
 51706: 'Mais fundo no interior.',
 51707: 'Ah, isso \xc3\xa9 perto da costa.',
 50200: 'Seu rato de por\xc3\xa3o!',
 50201: 'Seu c\xc3\xa3o sarnento!',
 50202: 'Te vejo no fundo do mar!',
 50203: 'Patife!',
 50204: 'Marujo de terra firme!',
 50205: 'Tolo confuso',
 50206: 'Voc\xc3\xaa precisa de uma espada afiada e intelig\xc3\xaancia mais afiada.',
 50207: 'Voc\xc3\xaa est\xc3\xa1 a um dobr\xc3\xa3o de um companheiro de casco completo!',
 50208: 'Cuidado com sua l\xc3\xadngua ou vou conserv\xc3\xa1-la com sal marinho!',
 50209: 'Toca-me e saqueie e voc\xc3\xaa ganha a bota!',
 50210: 'O horizonte est\xc3\xa1 t\xc3\xa3o vazio quanto sua cabe\xc3\xa7a.',
 50211: 'Voc\xc3\xaa \xc3\xa9 uma lona t\xc3\xadmida de uma vela cheia, n\xc3\xa3o \xc3\xa9, companheiro?',
 50300: 'Bom tiro, amigo!',
 50301: 'Um golpe bem dado!',
 50302: 'Belo tiro!',
 50303: 'Muito bem!',
 50304: 'N\xc3\xb3s mostramos a eles!',
 50305: 'Voc\xc3\xaa n\xc3\xa3o \xc3\xa9 t\xc3\xa3o ruim assim!',
 50306: 'Uma bela pilhagem!',
 52400: 'Que a sorte esteja minha senhora.',
 52401: 'Acho que essas cartas est\xc3\xa3o marcadas!',
 52402: 'Caramba, trapaceiro!',
 51900: 'Isso \xc3\xa9 um fracasso terr\xc3\xadvel!',
 51901: 'Tentando comprar a m\xc3\xa3o, n\xc3\xa3o \xc3\xa9?',
 51902: 'Voc\xc3\xaa est\xc3\xa1 blefando.',
 51903: 'Acho que voc\xc3\xaa n\xc3\xa3o entendeu.',
 51904: 'Salvo pelo rio.',
 52600: 'Bata em mim.',
 52601: 'Posso contratar outro revendedor?',
 53101: 'Peguei um peixe!',
 53102: 'Vi um peixe lend\xc3\xa1rio!',
 53103: 'O que voc\xc3\xaa pescou?',
 53104: 'Isso vai virar uma hist\xc3\xb3ria de baleia!',
 53105: 'Foi uma beleza!',
 53106: 'Arr, o mar est\xc3\xa1 trai\xc3\xa7oeiro hoje.',
 53107: 'Que farta pesca!', 
 53110: 'Voc\xc3\xaa tem a isca lend\xc3\xa1ria?',
 53111: 'Voc\xc3\xaa j\xc3\xa1 pescou um peixe lend\xc3\xa1rio?',
 53112: 'Voc\xc3\xaa sabe navegar em um barco de pesca?',
 53113: 'Onde est\xc3\xa1 o Mestre da Pesca?',
 53114: 'Voc\xc3\xaa completou sua cole\xc3\xa7\xc3\xa3o de peixes?',
 53120: 'Atire no meu alvo!',
 53121: 'Atire no navio mais pr\xc3\xb3ximo da costa!',
 53122: 'Tem um navio fugindo!',
 53123: 'Atire nos navios grandes!',
 53124: 'Atire nos navios pequenos!',
 53125: 'Mais est\xc3\xa3o chegando!',
 53126: 'N\xc3\xa3o vamos durar muito mais!',
 53127: 'Atire nos barris!',
 53128: 'Temos muni\xc3\xa7\xc3\xa3o nova!',
 53129: 'Defesa resistente, companheiros!',
 53141: 'Olhe a po\xc3\xa7\xc3\xa3o que eu fiz!',
 53142: 'Voc\xc3\xaa completou sua cole\xc3\xa7\xc3\xa3o de po\xc3\xa7\xc3\xb5es?',
 53143: 'Onde est\xc3\xa1 o cigano?',
 53144: 'Que po\xc3\xa7\xc3\xa3o \xc3\xa9 essa?',
 53145: 'Esta po\xc3\xa7\xc3\xa3o foi f\xc3\xa1cil o suficiente.',
 53146: 'Esta po\xc3\xa7\xc3\xa3o foi dif\xc3\xadcil de preparar, eu te digo!',
 53160: 'Precisamos de algu\xc3\xa9m para bombear o por\xc3\xa3o!',
 53161: 'Precisamos de algu\xc3\xa9m para esfregar!',
 53162: 'Precisamos de algu\xc3\xa9m para serrar!',
 53163: 'Precisamos de algu\xc3\xa9m para refor\xc3\xa7ar!',
 53164: 'Precisamos de algu\xc3\xa9m para martelar!',
 53165: 'Precisamos de algu\xc3\xa9m para remendar!',
 53166: 'Eu fa\xc3\xa7o isso!',
 53167: 'Continue assim, este navio n\xc3\xa3o vai se consertar sozinho!',
 53168: '\xc3\x93timo trabalho consertando o navio!',
 52100: 'Quer se agrupar?',
 52101: 'Juntar-se \xc3\xa0 minha tripula\xc3\xa7\xc3\xa3o?',
 52200: 'Lute contra alguns esqueletos?',
 52201: 'Lute contra alguns caranguejos?',
 52300: 'Que tal um jogo de Mayhem?',
 52301: 'Junte-se ao meu jogo Mayhem.',
 52302: 'Quer iniciar um jogo Mayhem?',
 52303: 'Quer iniciar um jogo de batalha em equipe?',
 52304: 'Junte-se ao meu jogo de batalha em equipe.',
 52350: 'Junte-se \xc3\xa0 minha Defesa de Canh\xc3\xa3o.',
 52351: 'Quer come\xc3\xa7ar uma Defesa de Canh\xc3\xa3o?',
 52352: 'Voc\xc3\xaa pode me dar uma m\xc3\xa3o com o Reparo?',
 52353: 'Precisamos consertar o navio agora!',
 52354: 'Quer pescar?',
 52355: 'Quer ir pescar comigo?',
 52356: 'Junte-se \xc3\xa0 minha tripula\xc3\xa7\xc3\xa3o para pescar?',
 52357: 'Hora de preparar algumas po\xc3\xa7\xc3\xb5es!',
 52358: 'Voc\xc3\xaa deveria tentar preparar po\xc3\xa7\xc3\xb5es.',
 52000: '',
 52000: '',
 52700: '',
 53000: '',
 52800: '',
 52900: '',
 50500: '',
 50600: '',
 60100: 'Oi',
 60101: 'Ol\xc3\xa1!',
 60102: 'Oi!',
 60103: 'Ei!',
 60104: 'Oi pessoal!',
 60105: 'Como \xc3\xa9 que t\xc3\xa1?',
 60106: 'Qual \xc3\xa9?',
 60200: 'Tchau!',
 60201: 'At\xc3\xa9 mais!',
 60202: 'Te vejo por a\xc3\xad!',
 60203: 'Volto j\xc3\xa1!',
 60204: 'Tenho que ir.',
 60300: ':-)',
 60301: 'Legal!',
 60302: '\xc3\x89 isso a\xc3\xad!',
 60303: 'Ha ha!',
 60304: 'Que fofo!',
 60305: '\xc3\x89 isso a\xc3\xad!',
 60306: 'Que maneiro!',
 60307: 'Irado!',
 60308: 'Incr\xc3\xadvel!',
 60309: 'Uau!',
 60400: ':-(',
 60401: 'Aahh!',
 60402: 'P\xc3\xb4xa, cara!',
 60403: 'Ai!',
 60404: 'P\xc3\xb4xa!',
 60500: 'Cad\xc3\xaa voc\xc3\xaa?',
 60501: 'Vamos para a Loja da Entrada!',
 60502: 'Vamos para a Discoteca!',
 60503: 'Vamos para Toontown.',
 60504: 'Vamos para os Piratas do Caribe!',
 60505: 'Girar moeda',
 60506: 'Dan\xc3\xa7ar',
 60507: 'Canto 1',
 60508: 'Canto 2',
 60509: 'Dan\xc3\xa7ar animado',
 60510: 'Dormir',
 60511: 'Flexionar',
 60512: 'Tocar Ala\xc3\xbade',
 60513: 'Tocar Flauta',
 60514: 'Frustra\xc3\xa7\xc3\xa3o',
 60515: 'Procurando',
 60516: 'Bocejar',
 60517: 'Ajoelhar',
 60518: 'Varrer',
 60519: 'Enfeitar',
 60520: 'Bocejar',
 60521: 'Dan\xc3\xa7ar',
 60522: 'N\xc3\xa3o',
 60523: 'Sim',
 60524: 'Rir',
 60525: 'Aplaudir',
 60526: 'Sorrir',
 60527: 'Raiva',
 60528: 'Medo',
 60529: 'Triste',
 60530: 'Comemorar',
 60668: 'Comemorar',
 60669: 'Dormir',
 60602: 'Furioso',
 60614: 'Aplaudir',
 60622: 'Assustado',
 60640: 'Rir',
 60652: 'Triste',
 60657: 'Sorrir',
 60664: 'Acenar',
 60665: 'Piscar',
 60666: 'Bocejar',
 60669: 'Dormir',
 60670: 'Dan\xc3\xa7ar',
 60676: 'Flertar',
 60677: 'Dan\xc3\xa7a do Zumbi',
 60678: 'Barulhento',
 60671: 'Ol\xc3\xa1, sou um Pirata e estou aqui para roubar seu cora\xc3\xa7\xc3\xa3o.',
 60672: 'Acabo de encontrar o tesouro que procurava.',
 60673: 'Se voc\xc3\xaa fosse uma meleca te pegava primeiro.',
 60674: 'Vem sempre aqui em Tortuga?',
 60675: 'Voc\xc3\xaa tem um mapa? Acabo de me perder em seu olhar.',
 65000: 'Sim',
 65001: 'N\xc3\xa3o',
 60909: 'Verifique a m\xc3\xa3o'}
SpeedChatStaticText = SpeedChatStaticTextCommon
Emotes_Root = 'EMO\xc3\x87\xc3\x95ES'
Emotes_Dances = 'Dan\xc3\xa7as'
Emotes_General = 'Geral'
Emotes_Music = 'M\xc3\xbasica'
Emotes_Expressions = 'Emo\xc3\xa7\xc3\xb5es'
Emote_ShipDenied = 'N\xc3\xa3o \xc3\xa9 poss\xc3\xadvel se emocionar ao navegar.'
Emote_MoveDenied = 'N\xc3\xa3o \xc3\xa9 poss\xc3\xadvel se emocionar ao mover-se.'
Emote_CombatDenied = 'N\xc3\xa3o \xc3\xa9 poss\xc3\xadvel se emocionar ao lutar.'
Emote_CannonDenied = 'N\xc3\xa3o \xc3\xa9 poss\xc3\xadvel se emocionar ao usar um canh\xc3\xa3o.'
Emote_SwimDenied = 'N\xc3\xa3o \xc3\xa9 poss\xc3\xadvel se emocionar ao nadar.'
Emote_ParlorGameDenied = 'N\xc3\xa3o \xc3\xa9 poss\xc3\xadvel se emocionar durante um jogo de sal\xc3\xa3o.'
Emotes = (60505,
 60506,
 60509,
 60510,
 60511,
 60516,
 60519,
 60520,
 60521,
 60522,
 60523,
 60524,
 60525,
 60526,
 60527,
 60528,
 60529,
 60530,
 60602,
 60607,
 60611,
 60614,
 60615,
 60622,
 60627,
 60629,
 60632,
 60636,
 60638,
 60640,
 60644,
 60652,
 60654,
 60657,
 60658,
 60663,
 60664,
 60665,
 60666,
 60668,
 60669,
 60612,
 60661,
 60645,
 60629,
 60641,
 60654,
 60630,
 60670,
 60633,
 60676,
 60677,
 65000,
 65001,
 60517,
 60678,
 60909)
SCFactoryMeetMenuIndexes = (1903,
 1904,
 1906,
 1907,
 1908, 
 1910,
 1913,
 1915,
 1916, 
 1917,
 1919,
 1922, 
 1923,
 1924,
 1932,
 1940, 
 1941)
CustomSCStrings = {10: 'Bom...',
 20: 'Por que n\xc3\xa3o?',
 30: 'Claro!',
 40: '\xc3\x89 assim que se faz isso.',
 50: 'Maravilha!',
 60: 'E a\xc3\xad?',
 70: 'Mas claro!',
 80: 'Bingo!',
 90: 'Voc\xc3\xaa s\xc3\xb3 pode estar brincando...',
 100: 'Parece legal.',
 110: 'Que loucura!',
 120: 'Caramba!',
 130: 'Que confus\xc3\xa3o!',
 140: 'N\xc3\xa3o se preocupe.',
 150: 'Grrrr!',
 160: 'Qual \xc3\xa9 a boa?',
 170: 'Ei, ei, ei!',
 180: 'Vejo voc\xc3\xaa amanh\xc3\xa3.',
 190: 'At\xc3\xa9 a pr\xc3\xb3xima.',
 200: 'Tchau-tchau, pica-pau.',
 210: "At\xc3\xa9 outra hora, galinha d'angola.",
 220: 'Vou precisar ir daqui a pouco.',
 230: 'N\xc3\xa3o conhe\xc3\xa7o isso!',
 240: 'Voc\xc3\xaa est\xc3\xa1 fora daqui!',
 250: 'Ai, isso d\xc3\xb3i!',
 260: 'Peguei voc\xc3\xaa!',
 270: 'Por favor!',
 280: 'Obrigad\xc3\xadssimo!',
 290: 'Voc\xc3\xaa est\xc3\xa1 ditando moda!',
 300: 'D\xc3\xa1 licen\xc3\xa7a!',
 310: 'Posso ajudar?',
 320: '\xc3\x89 o que eu estou falando!',
 330: 'Jabuti perde tempo querendo aprender li\xc3\xa7\xc3\xa3o de \xc3\xa1guia.',
 340: 'Macacos me mordam!',
 350: 'Isso \xc3\xa9 especial!',
 360: 'Vamos parar de fazer bagun\xc3\xa7a!',
 370: 'O gato comeu sua l\xc3\xadngua?',
 380: 'Agora \xc3\xa9 com voc\xc3\xaa!',
 390: 'Feio que d\xc3\xb3i.',
 400: 'Preciso ver um Toon.',
 410: 'N\xc3\xa3o dei a m\xc3\xadnima!',
 420: 'N\xc3\xa3o vai amarelar!',
 430: 'Voc\xc3\xaa \xc3\xa9 uma isca f\xc3\xa1cil.',
 440: 'Sei l\xc3\xa1!',
 450: 'Tudo a ver!',
 460: 'Gracinha!',
 470: 'Voc\xc3\xaa que manda!',
 480: '\xc3\x89 isso a\xc3\xad, garoto!',
 490: 'Vem me pegar, se voc\xc3\xaa conseguir!',
 500: 'Voc\xc3\xaa precisa se recuperar antes.',
 510: 'Voc\xc3\xaa precisa de mais Pontos de risadas.',
 520: 'Estou de volta em um minuto.',
 530: 'Estou com fome.',
 540: 'Isso mesmo!',
 550: 'Estou com sono.',
 560: 'Estou pronto!',
 570: 'Estou de aborrecido.',
 580: 'Amo isso!',
 590: 'Isso foi muito legal!',
 600: 'Pule!',
 610: 'Ganhou piadas?',
 620: 'O que houve?',
 630: 'Vai devagar.',
 640: 'Devagar e sempre.',
 650: 'Gol!',
 660: 'Pronto?',
 670: 'Tudo OK!',
 680: 'Vai!',
 690: 'Vamos por aqui!',
 700: 'Voc\xc3\xaa ganhou!',
 710: 'Meu voto \xc3\xa9 sim.',
 720: 'Meu voto \xc3\xa9 n\xc3\xa3o.',
 730: 'Me inclui nessa.',
 740: 'Me inclui fora dessa.',
 750: 'Fica aqui, eu volto.',
 760: 'Rapidinho!',
 770: 'Voc\xc3\xaa viu aquilo?',
 780: 'O que foi isso?',
 790: 'Nojento!',
 800: 'N\xc3\xa3o ligo.',
 810: 'Justo o que eu precisava.',
 820: 'Vamos botar lenha na fogueira!',
 830: 'Por aqui, galera!',
 840: 'Que coisa \xc3\xa9 essa?',
 850: 'A sorte est\xc3\xa1 lan\xc3\xa7ada.',
 860: 'Eu ouvi isso!',
 870: 'Voc\xc3\xaa est\xc3\xa1 falando comigo?',
 880: 'Valeu, vou estar por aqui por uma semana.',
 890: 'Hmm.',
 900: 'Eu pego este.',
 910: 'Peguei!',
 920: '\xc3\x89 meu!',
 930: 'Toma pra voc\xc3\xaa.',
 940: 'Afaste-se, pode ser perigoso.',
 950: 'N\xc3\xa3o esquenta!',
 960: 'Minha nossa!',
 970: 'Puxa!',
 980: 'Uuuuhuuu!',
 990: 'Todos a bordo!',
 1000: 'Caramba!',
 1010: 'A curiosidade matou o gato.',
 2000: 'Tome ju\xc3\xadzo!',
 2010: 'Que bom ver voc\xc3\xaa!',
 2020: 'Voc\xc3\xaa que sabe.',
 2030: 'Est\xc3\xa1 se saindo bem?',
 2040: 'Antes tarde do que nunca!',
 2050: 'Bravo!',
 2060: 'Mas, falando s\xc3\xa9rio, pessoal...',
 2070: 'Est\xc3\xa1 a fim de se juntar a n\xc3\xb3s?',
 2080: 'Te pego depois!',
 2090: 'Mudou de id\xc3\xa9ia?',
 2100: 'Vem pegar!',
 2110: 'Ai, meu Deus!',
 2120: 'Prazer em conhecer.',
 2130: 'N\xc3\xa3o fa\xc3\xa7a nada que eu n\xc3\xa3o faria!',
 2140: 'Nem pense nisso!',
 2150: 'N\xc3\xa3o abandone o barco!',
 2160: 'N\xc3\xa3o segura a respira\xc3\xa7\xc3\xa3o.',
 2170: 'Nem me fale.',
 2180: '\xc3\x89 f\xc3\xa1cil falar.',
 2190: 'J\xc3\xa1 chega!',
 2200: 'Excelente!',
 2210: 'Incr\xc3\xadvel encontrar voc\xc3\xaa aqui!',
 2220: 'D\xc3\xa1 um tempo.',
 2230: 'Gostei de saber.',
 2240: 'Vai em frente que eu quero ver!',
 2250: 'Vai em frente!',
 2260: 'Muito bom!',
 2270: 'Legal ver voc\xc3\xaa!',
 2280: 'Tenho que me mandar.',
 2290: 'Tenho que ir embora.',
 2300: 'Aguenta firme.',
 2310: 'Espera um segundo.',
 2320: 'Curta bastante!',
 2330: 'Divirta-se!',
 2340: 'N\xc3\xa3o tenho o dia todo!',
 2350: 'Segura a onda!',
 2360: 'Viajou!',
 2370: 'N\xc3\xa3o acredito!',
 2380: 'Duvido.',
 2390: 'Devo essa a voc\xc3\xaa.',
 2400: 'Estou lendo sua mente, voc\xc3\xaa \xc3\xa9 claro como \xc3\xa1gua.',
 2410: 'Eu acho isso.',
 2420: 'Acho que voc\xc3\xaa devia passar.',
 2430: 'Quem dera ter dito isso.',
 2440: 'Se eu fosse voc\xc3\xaa n\xc3\xa3o faria isso.',
 2450: 'Seria \xc3\xb3timo!',
 2460: 'Estou ajudando meu amigo.',
 2470: 'Estou aqui a semana toda.',
 2480: 'Imagina s\xc3\xb3!',
 2490: 'Na hora H...',
 2500: 'O que tiver de ser, ser\xc3\xa1.',
 2510: 'S\xc3\xb3 estou pensando alto.',
 2520: 'Mantenha o contato.',
 2530: 'Depois da tempestade vem o lama\xc3\xa7al!',
 2540: 'Rapidinho!',
 2550: 'Sinta-se em casa.',
 2560: 'Talvez outra hora.',
 2570: 'Posso me juntar a voc\xc3\xaas?',
 2580: 'Que lugar legal, o seu.',
 2590: 'Foi \xc3\xb3timo falar com voc\xc3\xaa.',
 2600: 'Sem d\xc3\xbavida.',
 2610: 'Sem brincadeira!',
 2620: 'Nem por um decreto.',
 2630: 'Tenha a santa paci\xc3\xaancia!',
 2640: 'Por mim tudo bem.',
 2650: 'T\xc3\xa1 legal.',
 2660: 'Sorria!',
 2670: 'O que voc\xc3\xaa disse?',
 2680: 'Tchaaaan!',
 2690: 'Calma a\xc3\xad.',
 2700: 'At\xc3\xa9 pr\xc3\xa1 voc\xc3\xaas!',
 2710: 'Quem desdenha quer comprar.',
 2720: 'Muito maneiro!',
 2730: 'Muito engra\xc3\xa7ado.',
 2740: 'O truque \xc3\xa9 esse!',
 2750: 'Est\xc3\xa1 acontecendo uma invas\xc3\xa3o de Cogs!',
 2760: 'Vacilo.',
 2770: 'Cuidado!',
 2780: 'Bem feito!',
 2790: 'O que est\xc3\xa1 acontecendo?',
 2800: 'O que est\xc3\xa1 havendo?',
 2810: 'Para mim est\xc3\xa1 certo.',
 2820: 'Certo, chefe.',
 2830: 'Pode apostar.',
 2840: 'Fa\xc3\xa7a as contas.',
 2850: 'Por que est\xc3\xa1 saindo t\xc3\xa3o cedo?',
 2860: 'Voc\xc3\xaa me faz rir!',
 2870: 'Vai direto.',
 2880: 'Voc\xc3\xaa est\xc3\xa1 decaindo!',
 3000: 'O que quiser.',
 3010: 'Voc\xc3\xaa se importa se eu me juntar a voc\xc3\xaas?',
 3020: 'Verifique, OK?',
 3030: 'N\xc3\xa3o esteja t\xc3\xa3o certo disso.',
 3040: 'N\xc3\xa3o liga se eu fizer isso.',
 3050: 'N\xc3\xa3o sacrifica!',
 3060: 'Voc\xc3\xaa n\xc3\xa3o conhece?',
 3070: 'N\xc3\xa3o liga para mim.',
 3080: 'Descobri!',
 3090: 'Imagine s\xc3\xb3!',
 3100: 'Pode esquecer!',
 3110: 'Est\xc3\xa1 indo para o mesmo lugar que eu?',
 3120: 'Melhor para voc\xc3\xaa!',
 3130: 'Que coisa.',
 3140: 'Aproveita!',
 3150: 'Fica de olho!',
 3160: 'E l\xc3\xa1 vamos n\xc3\xb3s de novo.',
 3170: 'Que tal essa!',
 3180: 'Que voc\xc3\xaa acha?',
 3190: 'Eu acho que sim.',
 3200: 'Acho que n\xc3\xa3o.',
 3210: 'Dou uma resposta mais tarde.',
 3220: 'Sou todo ouvidos.',
 3230: 'Agora n\xc3\xa3o d\xc3\xa1.',
 3240: 'N\xc3\xa3o estou brincando!',
 3250: 'Estou de queixo ca\xc3\xaddo.',
 3260: 'Continue sorrindo.',
 3270: 'Depois me fala!',
 3280: 'Deixa a torta voar!',
 3290: 'Eu tamb\xc3\xa9m tenho certeza.',
 3300: 'Pare de demorar!',
 3310: 'Caramba, o tempo voou.',
 3320: 'Sem coment\xc3\xa1rios.',
 3330: 'Agora voc\xc3\xaa est\xc3\xa1 falando minha l\xc3\xadngua!',
 3340: 'Por mim tudo bem.',
 3350: 'Bom conhecer voc\xc3\xaa.',
 3360: 'T\xc3\xa1 legal.',
 3370: 'Com certeza.',
 3380: 'Valeu mesmo.',
 3390: '\xc3\x89 por a\xc3\xad.',
 3400: '\xc3\x89 isso!',
 3410: 'Hora de dormir.',
 3420: 'Confie em mim!',
 3430: 'At\xc3\xa9 a pr\xc3\xb3xima.',
 3440: 'Espere acordado!',
 3450: 'Muito bem!',
 3460: 'O que traz voc\xc3\xaa aqui?',
 3470: 'O que aconteceu?',
 3480: 'E agora?',
 3490: 'Voc\xc3\xaa primeiro.',
 3500: 'Pegue a esquerda.',
 3510: 'Bem que voc\xc3\xaa queria!',
 3520: 'Voc\xc3\xaa est\xc3\xa1 com problemas!',
 3530: 'Voc\xc3\xaa \xc3\xa9 demais!',
 4000: 'Os Tonns mandam na \xc3\xa1rea!',
 4010: 'Besteirol de Cog!',
 4020: 'Toons de todo o mundo, uni-vos!',
 4030: 'E a\xc3\xad, parceiro!',
 4040: 'Muit\xc3\xadssimo obrigado.',
 4050: 'Vamos l\xc3\xa1, novato.',
 4060: 'T\xc3\xb4 indo pra caminha.',
 4070: 'T\xc3\xb4 doido pra ir!',
 4080: 'Esta cidade \xc3\xa9 pequena demais para n\xc3\xb3s dois!',
 4090: 'V\xc3\xa1 embora!',
 4100: 'Puxa!!!',
 4110: '\xc3\x89 ouro!',
 4120: 'Boa viagem!',
 4130: 'T\xc3\xa1 na hora de sumir...',
 4140: 'Debandar!',
 4150: 'Ficou com a pulga atr\xc3\xa1s da orelha?',
 4160: 'Me poupe!',
 4170: 'Perfeito.',
 4180: 'Aposto.',
 4190: 'P\xc3\xa9 na estrada!',
 4200: 'Ent\xc3\xa3o, adivinha!',
 4210: 'T\xc3\xb4 de novo na ativa!',
 4220: 'Procure os suspeitos de sempre.',
 4230: 'Vamos agitar!',
 4240: 'O c\xc3\xa9u \xc3\xa9 o limite.',
 4250: 'Estou me preparando.',
 4260: 'Segura a onda!',
 4270: 'N\xc3\xa3o acerto uma.',
 4280: 'Voltem todos agora.',
 4290: '\xc3\x89 uma verdadeira lavada!',
 4300: 'N\xc3\xa3o vai amarelar.',
 4310: 'T\xc3\xa1 se achando?',
 4320: 'Que bagun\xc3\xa7a \xc3\xa9 essa aqui?',
 4330: 'Vamos parar com esta pregui\xc3\xa7a!',
 4340: 'S\xc3\xb3 n\xc3\xa3o v\xc3\xaa quem n\xc3\xa3o quer.',
 4350: '\xc3\x89 um col\xc3\xadrio para os olhos!',
 4360: 'Nossas op\xc3\xa7\xc3\xb5es est\xc3\xa3o acabando.',
 4370: 'Tire esse peso das costas.',
 4380: 'Que paisagem maravilhosa!',
 4390: 'Voc\xc3\xaa vai ver s\xc3\xb3!',
 6000: 'Quero doce!',
 6010: 'Sou que nem formiga com doce.',
 6020: 'Foi feito no grito.',
 6030: 'F\xc3\xa1cil como tirar doce de crian\xc3\xa7a!',
 6040: 'Leve tr\xc3\xaas e pague um.',
 6050: 'Eles v\xc3\xa3o sentir o gostinho!',
 6060: '\xc3\x89 a parte ruim da hist\xc3\xb3ria.',
 6070: 'Voc\xc3\xaa n\xc3\xa3o pode assobiar e chupar cana.',
 6080: 'T\xc3\xb4 me sentindo como uma crian\xc3\xa7a em uma loja de doces.',
 6090: 'Seis deste, meia d\xc3\xbazia do outro...',
 6100: 'Rapadura \xc3\xa9 doce mas n\xc3\xa3o \xc3\xa9 mole n\xc3\xa3o.',
 6110: 'Tem que fritar o peixe de olho no gato.',
 6120: '\xc3\x89 sopa no mel.',
 6130: 'Mas temos que pisar em ovos.',
 6140: 'Vamos melar os trabalhos!',
 6150: 'Voc\xc3\xaa \xc3\xa9 um coco duro de quebrar!',
 6160: '\xc3\x89 assim que o bolo desanda.',
 6170: 'Caf\xc3\xa9 com leite.',
 6180: 'T\xc3\xa1 tentando ado\xc3\xa7ar a minha boca?',
 6190: 'Tem que tomar \xc3\xa1gua pra ajudar a descer.',
 6200: 'Voc\xc3\xaa \xc3\xa9 o que voc\xc3\xaa come!',
 6210: '\xc3\x89 mam\xc3\xa3o com a\xc3\xa7\xc3\xbacar!',
 6220: 'Deixa de ser banan\xc3\xa3o!',
 6230: 'Azedinho doce.',
 6240: 'Molezinha!',
 6250: 'Olha o bicho-pap\xc3\xa3o!',
 6260: 'Olha o sorvete a\xc3\xad, gente!',
 6270: 'N\xc3\xa3o vamos enfeitar o bolo n\xc3\xa3o.',
 6280: 'Toc, toc, toc...',
 6290: 'Quem \xc3\xa9?',
 7000: 'P\xc3\xa1ra de macaquice!',
 7010: 'Entrou areia.',
 7020: 'Macaco de imita\xc3\xa7\xc3\xa3o.',
 7030: 'Eles te passaram a perna.',
 7040: 'Parece hist\xc3\xb3ria pra boi dormir.',
 7050: 'S\xc3\xb3 t\xc3\xb4 de palha\xc3\xa7ada contigo.',
 7060: 'Quem quer ser a bola da vez?',
 7070: '\xc3\x89 papagaio de pirata...',
 7080: 'Uma macacada s\xc3\xb3!',
 7090: 'Macacos me mordam!',
 7100: 'Cada macaco no seu galho.',
 7110: 'E a beca?',
 7120: 'N\xc3\xa3o ou\xc3\xa7o.',
 7130: 'N\xc3\xa3o vejo.',
 7140: 'N\xc3\xa3o falo.',
 7150: 'Cada um para um lado, macacada.',
 7160: 'L\xc3\xa1 fora \xc3\xa9 uma selva.',
 7170: 'Voc\xc3\xaa \xc3\xa9 o rei da selva!',
 7180: 'Tudo \xc3\xb3timo!',
 7190: 'T\xc3\xb4 enlouquecendo!',
 7200: 'Vamos entrar no ritmo!',
 7210: 'Este lugar est\xc3\xa1 muito cheio!',
 7220: 'Adeus, vida cruel.',
 7230: 'Acabei numa furada.',
 7230: 'P\xc3\xa9 na t\xc3\xa1bua.',
 7240: 'Balinhas n\xc3\xa3o crescem em \xc3\xa1rvores!',
 10000: 'Este lugar \xc3\xa9 uma cidade-fantasma.',
 10001: 'Bonita roupa!',
 10002: 'Acho que este lugar \xc3\xa9 assombrado.',
 10003: 'Gostosuras ou travessuras!',
 10004: 'Buuuuu!',
 10005: 'Feliz Assombra\xc3\xa7\xc3\xa3o!',
 10006: 'Feliz Dia das Bruxas!',
 10007: 'Est\xc3\xa1 na hora de eu virar uma ab\xc3\xb3bora.',
 10008: 'Fantasm\xc3\xa1tico!',
 10009: 'Sinistro!',
 10010: 'Isso \xc3\xa9 horripilante!',
 10011: 'Detesto aranhas!',
 10012: 'Voc\xc3\xaa ouviu?',
 10013: 'Voc\xc3\xaa n\xc3\xa3o tem nem uma sombra de chance!',
 10014: 'Me assustou!',
 10015: 'Horr\xc3\xadvel!',
 10016: 'Bizarro!',
 10017: 'Isso foi muito estranho....',
 10018: 'Esqueletos no seu arm\xc3\xa1rio?',
 10019: 'Assustei voc\xc3\xaa?',
 11000: 'Ah! Marmelada!',
 11001: 'Melhor desamarrar a cara!',
 11002: 'Brrr!',
 11003: 'Fica calmo!',
 11004: 'Vem pegar!',
 11005: 'N\xc3\xa3o d\xc3\xa1 uma de peru, para morrer de v\xc3\xa9spera.',
 11006: 'Glu-glu-glu!',
 11007: 'Boas Festas!',
 11008: 'Feliz Ano Novo!',
 11009: 'Um bom feriado para voc\xc3\xaa!',
 11010: 'Feliz Dia do Peru!',
 11011: 'Ho! Ho! Ho!',
 11012: "\'Noel\' problema.",
 11013: "\'Noel\' surpresa nenhuma.",
 11014: 'Deixa bater o sino, pequenino!',
 11015: 'Raspa o tacho.',
 11016: 'Feliz Natal!',
 11017: 'Com \'nataleza\'!',
 11018: 'At\xc3\xa9 o Natal, tudo bem!',
 11019: "Voc\xc3\xaa vai se \'arrenapender\'!",
 11020: 'Tenha um inverno maravilhoso!',
 11021: 'As decora\xc3\xa7\xc3\xb5es da festa de fim de ano s\xc3\xa3o Toontastico!',
 11022: 'Soldados Toons est\xc3\xa3o organizando festas de fim de ano!',
 12000: 'Fica comigo!',
 12001: 'Vem ser meu amorzinho!',
 12002: 'Feliz Dia dos Namorados!',
 12003: 'Ahhh, que bonitinho.',
 12004: 'Estou apaixonado por voc\xc3\xaa.',
 12005: 'Amor de pombinhos.',
 12006: 'Te amo!',
 12007: 'Quer ser meu amor?',
 12008: 'Voc\xc3\xaa \xc3\xa9 uma gra\xc3\xa7a.',
 12009: 'Voc\xc3\xaa \xc3\xa9 doce como mel.',
 12010: 'Fofura.',
 12011: 'Voc\xc3\xaa precisa de um abra\xc3\xa7o.',
 12012: 'Muito fofo!',
 12013: 'Que fofo!',
 12014: 'Batatinha quando nasce...',
 12015: 'Esparrama pelo ch\xc3\xa3o...',
 12016: 'Que gracinha!',
 12050: 'EU AMO acabar com Cogs!',
 12051: 'Voc\xc3\xaa \xc3\xa9 um estouro!',
 12052: 'S\xc3\xb3 tenho olhos para voc\xc3\xaa!',
 12053: 'Voc\xc3\xaa \xc3\xa9 mais doce do que uma bala!',
 12054: 'Eu ADORARIA ter voc\xc3\xaa em minha Festa Dia dos namorados!',
 13000: 'Tenho voc\xc3\xaa no cora\xc3\xa7\xc3\xa3o!',
 13001: 'Feliz P\xc3\xa1scoa!',
 13002: 'Voc\xc3\xaa n\xc3\xa3o est\xc3\xa1 vestindo marrom-chocolate!',
 13003: 'Sorte de iniciante marrom-chocolate.',
 13004: 'Estou chocolate de inveja.',
 13005: 'Seu sortudo!',
 13006: 'Voc\xc3\xaa \xc3\xa9 o meu trevo de quatro folhas!',
 13007: 'Voc\xc3\xaa \xc3\xa9 o meu talism\xc3\xa3!',
 14000: 'Vamos dar uma festa de ver\xc3\xa3o na Propriedade!',
 14001: '\xc3\x89 hora da festa!',
 14002: 'O \xc3\xbaltimo a chegar ao lago \xc3\xa9 um Cog do padre!',
 14003: 'Hora de treinar Rabisco em Grupo!',
 14004: 'Hora de treinar Rabisco!',
 14005: 'Seu Rabisco \xc3\xa9 legal!',
 14006: 'Que truques seu Rabisco pode fazer?',
 14007: 'Hora do Pinball de Canh\xc3\xa3o!',
 14008: 'O Pinball de Canh\xc3\xa3o \xc3\xa9 demais!',
 14009: 'Sua Propriedade \xc3\xa9 demais!',
 14010: 'Seu Jardim \xc3\xa9 legal!',
 14011: 'Sua Propriedade \xc3\xa9 legal!'}
SCMenuCommonCogIndices = (20000, 20004)
SCMenuCustomCogIndices = {'bf': (20005, 20014),
 'nc': (20015, 20024),
 'ym': (20025, 20035),
 'ms': (20036, 20046),
 'bc': (20047, 20057),
 'cc': (20058, 20070),
 'nd': (20071, 20080),
 'ac': (20081, 20092),
 'tf': (20093, 20103),
 'hh': (20104, 20114),
 'le': (20115, 20124),
 'bs': (20125, 20135),
 'cr': (20136, 20145),
 'tbc': (20146, 20156),
 'ds': (20157, 20164),
 'gh': (20165, 20177),
 'pp': (20178, 20187),
 'b': (20188, 20199),
 'f': (20200, 20210),
 'mm': (20211, 20224),
 'tw': (20225, 20235),
 'mb': (20236, 20245),
 'm': (20246, 20254),
 'mh': (20255, 20266),
 'dt': (20267, 20276),
 'p': (20277, 20287),
 'tm': (20288, 20298),
 'bw': (20299, 20308),
 'ls': (20309, 20319),
 'rb': (20320, 20329),
 'sc': (20330, 20331),
 'sd': (20341, 20350)}
PSCMenuExpressions = 'EXPRESS\xc3\x95ES'
PSCMenuGreetings = 'CUMPRIMENTOS'
PSCMenuGoodbyes = 'DESPEDIDAS'
PSCMenuFriendly = 'AMIG\xc3\x81VEL'
PSCMenuHappy = 'FELIZ'
PSCMenuSad = 'TRISTE'
PSCMenuSorry = 'DESCULPA'
PSCMenuCombat = 'COMBATE'
PSCMenuSeaCombat = 'COMBATE NO MAR'
PSCMenuPlaces = 'LUGARES'
PSCMenuLetsSail = 'VAMOS\\NAVEGAR...'
PSCMenuLetsHeadTo = 'VAMOS\\PARA...'
PSCMenuHeadToPortRoyal = 'PORT ROYAL'
PSCMenuWhereIs = 'ONDE EST\xc3\x81 ..?'
PSCMenuWhereIsPortRoyal = 'PORT ROYAL'
PSCMenuWhereIsTortuga = 'TORTUGA'
PSCMenuWhereIsPadresDelFuego = 'PADRES DEL FUEGO'
PSCMenuWhereIsLasPulgas = 'LAS PULGAS'
PSCMenuWhereIsLosPadres = 'LOS PADRES'
PSCMenuDirections = 'DIRE\xc3\x87\xc3\x95ES'
PSCMenuInsults = 'INSULTOS'
PSCMenuCompliments = 'ELOGIOS'
PSCMenuCardGames = 'JOGOS DE CARTAS'
PSCMenuPoker = 'P\xc3\x94QUER'
PSCMenuBlackjack = 'O JOGO DE VINTE-E-UM'
PSCMenuMinigames = 'MINIGAMES'
PSCMenuFishing = 'FISHING'
PSCMenuCannonDefense = 'CANH\xc3\x83O DE DEFESA'
PSCMenuPotions = 'PO\xc3\x87\xc3\x83O DE FERMENTA\xc3\x87\xc3\x83O'
PSCMenuRepair = 'REPARAR'
PSCMenuInvitations = 'CONVITES'
PSCMenuVersusPlayer = 'VERSUS'
PSCMenuHunting = 'CA\xc3\x87ANDO'
PSCMenuQuests = 'MISS\xc3\x95ES'
PSCMenuGM = 'GM'
PSCMenuShips = 'NAVIOS'
PSCMenuAdventures = 'AVENTURA'
GWSCMenuHello = 'CUMPRIMENTOS'
GWSCMenuBye = 'DESPEDIDAS'
GWSCMenuHappy = 'FELIZ'
GWSCMenuSad = 'TRISTE'
GWSCMenuPlaces = 'LUGARES'
RandomButton = 'Aleat\xc3\xb3rio'
TypeANameButton = 'Digite um nome'
PickANameButton = 'Escolha um nome'
NameShopSubmitButton = 'Enviar'
RejectNameText = 'Este nome n\xc3\xa3o \xc3\xa9 permitido. Tente novamente.'
WaitingForNameSubmission = 'Enviando o seu nome...'
NameShopNameMaster = 'NameMaster_portuguese.txt'
NameShopPay = 'Assine j\xc3\xa1!'
NameShopPlay = 'Avalia\xc3\xa7\xc3\xa3o gratuita'
NameShopOnlyPaid = 'Somente usu\xc3\xa1rios pagantes\npodem dar nomes aos seus Toons.\nAt\xc3\xa9 que voc\xc3\xaa se inscreva\nseu nome ser\xc3\xa1\n'
NameShopContinueSubmission = 'Continuar envio'
NameShopChooseAnother = 'Escolha outro nome'
NameShopToonCouncil = 'O Conselho de Toons\nanalisar\xc3\xa1 o seu\nnome.' + 'A an\xc3\xa1lise pode\nlevar alguns dias.\nEnquanto voc\xc3\xaa espera\nseu nome ser\xc3\xa1\n'
PleaseTypeName = 'Digite o seu nome:'
ToonAlreadyExists = '%s j\xc3\xa1 existe'
AllNewNames = 'Todos os novos nomes\ndevem ser aprovados\npelo Conselho de Toons.'
NameShopNameRejected = 'O nome\nenviado foi\nrejeitado.'
NameShopNameAccepted = 'Parab\xc3\xa9ns!\nO nome\nenviado foi\naceito!'
NoPunctuation = 'N\xc3\xa3o \xc3\xa9 permitido usar caracteres de pontua\xc3\xa7\xc3\xa3o nos nomes!'
PeriodOnlyAfterLetter = 'Voc\xc3\xaa pode usar um ponto no nome, mas apenas depois de uma letra.'
ApostropheOnlyAfterLetter = 'Voc\xc3\xaa pode usar um ap\xc3\xb3strofo no nome, mas apenas depois de uma letra.'
NoNumbersInTheMiddle = 'D\xc3\xadgitos num\xc3\xa9ricos podem n\xc3\xa3o aparecer no meio da palavra.'
ThreeWordsOrLess = 'Seu nome deve ter tr\xc3\xaas palavras ou menos.'
CopyrightedNames = ('mickey',
 'mickey mouse',
 'mickeymouse',
 'minnie',
 'minnie mouse',
 'minniemouse',
 'donald',
 'pato donald',
 'donaldduck',
 'pluto',
 'pateta')
NCTooShort = 'Este nome \xc3\xa9 muito curto.'
NCNoDigits = 'O nome n\xc3\xa3o pode conter n\xc3\xbameros.'
NCNeedLetters = 'Cada palavra do nome deve conter algumas letras.'
NCNeedVowels = 'Cada palavra do nome deve conter algumas vogais.'
NCAllCaps = 'O seu nome n\xc3\xa3o pode estar todo em mai\xc3\xbascula.'
NCMixedCase = 'Este nome tem muitas letras em min\xc3\xbascula.'
NCBadCharacter = "O seu nome n\xc3\xa3o pode conter o caractere '%s'"
NCRepeatedChar = "Seu nome tem muitos caracteres '%s'"
NCGeneric = 'Sinto muito, este nome n\xc3\xa3o vai funcionar.'
NCTooManyWords = 'O seu nome n\xc3\xa3o pode ter mais de quatro palavras.'
NCDashUsage = "H\xc3\xadfens podem ser usados apenas para ligar duas palavras (como em 'Bu-Bu')."
NCCommaEdge = 'O seu nome n\xc3\xa3o pode come\xc3\xa7ar ou terminar com v\xc3\xadrgula.'
NCCommaAfterWord = 'Voc\xc3\xaa n\xc3\xa3o pode come\xc3\xa7ar uma palavra com v\xc3\xadrgula.'
NCCommaUsage = 'Este nome n\xc3\xa3o usa v\xc3\xadrgulas corretamente. As v\xc3\xadrgulas devem juntar duas palavras, como no nome "Dr. Quack, MD". As v\xc3\xadrgulas devem tamb\xc3\xa9m ser seguidas por um espa\xc3\xa7o.'
NCPeriodUsage = 'Este nome n\xc3\xa3o usa pontos corretamente. Os pontos s\xc3\xa3o permitidos somente em palavras como "Sr.", "Sra.", "J.P." etc.'
NCApostrophes = 'Este nome tem muitos ap\xc3\xb3strofos.'
AvatarDetailPanelOK = lOK
AvatarDetailPanelCancel = lCancel
AvatarDetailPanelClose = 'Fechar'
AvatarDetailPanelLookup = 'Procurando detalhes de %s.'
AvatarDetailPanelFailedLookup = 'N\xc3\xa3o foi poss\xc3\xadvel obter detalhes de %s.'
AvatarDetailPanelPlayer = 'Jogador: %(player)s\Mundo: %(world)s\nLocal: %(location)s'
AvatarDetailPanelOnline = 'Regi\xc3\xa3o: %(district)s\nLocation: %(location)s'
AvatarDetailPanelOffline = 'Regi\xc3\xa3o: off-line\nLocal: off-line'
AvatarPanelFriends = 'Amigos'
AvatarPanelWhisper = 'Cochichar'
AvatarPanelSecrets = 'Amigos Secretos'
AvatarPanelGoTo = 'Ir para'
AvatarPanelIgnore = 'Ignorar'
AvatarPanelStopIgnore = 'Parar de Ignorar'
AvatarPanelEndIgnore = 'Encerrar Ignorar'
AvatarPanelTrade = 'Trocar'
AvatarPanelCogLevel = 'N\xc3\xadvel: %s'
AvatarPanelCogDetailClose = 'Fechar'
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
KartRacingMenuSections = [-1,
 'LUGARES',
 'CORRIDAS',
 'PISTAS',
 'ELOGIOS',
 'PROVOCA\xc3\x87\xc3\x95ES']
AprilToonsMenuSections = [-1,
 'CUMPRIMENTOS',
 'PARQUES',
 'PERSONAGENS',
 'PROPRIEDADES']
SillyHolidayMenuSections = [-1, 'MUNDO', 'BATALHA']
CarolMenuSections = [-1]
VictoryPartiesMenuSections = [-1, 'FESTA', 'ITENS']
GolfMenuSections = [-1, 
 'PERCURSOS',
 'DICAS',
 'COMENT\xc3\x81RIOS']
BoardingMenuSections = ['GRUPO',
 'Vamos para...',
 'Estava indo para...',
 -1]
SellbotNerfMenuSections = [-1, 'REUNINDO', 'TORRES/VP Rob\xc3\xb4 Vendedor']
JellybeanJamMenuSections = ['OBTER BALINHAS', 'GASTAR BALINHAS']
WinterMenuSections = ['CANTANDO', -1]
HalloweenMenuSections = [-1]
SingingMenuSections = [-1]
WhiteListMenu = [-1, 'LISTA DE PERMISS\xc3\x95ES']
SellbotInvasionMenuSections = [-1]
SellbotFieldOfficeMenuSections = [-1, 'ESTRAT\xc3\x89GIA']
IdesOfMarchMenuSections = [-1]
TTAccountCallCustomerService = 'Favor entrar em contato com o Atendimento ao Consumidor em %s.'
TTAccountCustomerServiceHelp = '\nSe precisar de ajuda, favor entrar em contato com o Atendimento ao Comsumidor em %s.'
TTAccountIntractibleError = 'Um erro ocorreu.'

def timeElapsedString(timeDelta):
    timeDelta = abs(timeDelta)
    if timeDelta.days > 0:
        if timeDelta.days == 1:
            return '1 dia atr\xc3\xa1s'
        else:
            return '%s dias atr\xc3\xa1s' % timeDelta.days
    elif timeDelta.seconds / 3600 > 0:
        if timeDelta.seconds / 3600 == 1:
            return '1 hora atr\xc3\xa1s'
        else:
            return '%s horas atr\xc3\xa1s' % (timeDelta.seconds / 3600)
    elif timeDelta.seconds / 60 < 2:
        return '1 minuto atr\xc3\xa1s'
    else:
        return '%s minutos atr\xc3\xa1s' % (timeDelta.seconds / 60)
