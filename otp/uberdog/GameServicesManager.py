from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal

from otp.distributed.PotentialAvatar import PotentialAvatar


class GameServicesManager(DistributedObjectGlobal):
    notify = DirectNotifyGlobal.directNotify.newCategory('GameServicesManager')

    def __init__(self, cr):
        DistributedObjectGlobal.__init__(self, cr)
        self.doneEvent = None
        self._callback = None

    def login(self, doneEvent):
        self.doneEvent = doneEvent

        playToken = self.cr.playToken or 'dev'

        self.d_login(playToken)

    def d_login(self, playToken):
        self.sendUpdate('login', [playToken])

    def acceptLogin(self):
        messenger.send(self.doneEvent, [{'mode': 'success'}])

    def requestAvatarList(self):
        self.sendUpdate('requestAvatarList')

    def avatarListResponse(self, avatarList):
        avList = []
        for avNum, avName, avDNA, avPosition, nameState in avatarList:
            nameOpen = int(nameState == 1)
            names = [avName, '', '', '']
            if nameState == 2:  # Pending
                names[1] = avName
            elif nameState == 3:  # Approved
                names[2] = avName
            elif nameState == 4:  # Rejected
                names[3] = avName

            avList.append(PotentialAvatar(avNum, names, avDNA, avPosition, nameOpen))

        self.cr.handleAvatarsList(avList)

    def requestRemoveAvatar(self, avId):
        self.sendUpdate('requestRemoveAvatar', [avId])

    def requestPlayAvatar(self, avId):
        self.sendUpdate('requestPlayAvatar', [avId])

    def receiveAccountDays(self, accountDays):
        base.cr.accountDays = accountDays
