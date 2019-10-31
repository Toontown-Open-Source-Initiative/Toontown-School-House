from SCTerminal import SCTerminal
from otp.otpbase.OTPLocalizer import SpeedChatStaticText
SCStaticTextMsgEvent = 'SCStaticTextMsg'

def decodeSCStaticTextMsg(textId):
    return SpeedChatStaticText.get(textId, None)


class SCStaticTextTerminal(SCTerminal):

    def __init__(self, textId):
        SCTerminal.__init__(self)
        self.textId = textId
        self.text = SpeedChatStaticText[self.textId]

    def handleSelect(self, displayType=0):
        SCTerminal.handleSelect(self, displayType)
        messenger.send(self.getEventName(SCStaticTextMsgEvent), [self.textId, displayType])
