from otp.otpbase import OTPLocalizer
from otp.speedchat import SCStaticTextTerminal


DestIdsToMsgs = {0: [[5105], [5205]],
                 1: [[5106], [5206]],
                 2: [[5107], [5207]],
                 3: [[5108], [5208]],
                 4: [[5109], [5209]],
                 5: [[5112], [5212]],
                 6: [[5113], [5213]],
                 7: [[5114], [5214]],
                 8: [[5115], [5215]],
                 9: [[5100], [5200]],
                 10: [[5101], [5201]],
                 11: [[5102], [5202]],
                 12: [[5104], [5204]],
                 13: [[5110], [5210]],
                 14: [[5111], [5211]],
                 15: [[5103], [5203]]}


def boardingMessagesChanged(destId, parent):
    menu = None
    for scElement in parent:
        if hasattr(scElement, 'title') and scElement.title == OTPLocalizer.SCMenuBoardingGroup:
            menu = scElement.getMenu()
            break
    if hasattr(base, 'localAvatar') and base.localAvatar:
        if destId in DestIdsToMsgs.keys():
            for subMenu in DestIdsToMsgs[destId]:
                for phrase in subMenu:
                    if phrase not in OTPLocalizer.SpeedChatStaticText:
                        print 'warning: tried to link boarding phrase %s which does not seem to exist' % phrase
                        break
                    else:
                        if not menu:
                            print 'warning: no menu found'
                            break
                        menuIndex = DestIdsToMsgs[destId].index(subMenu)
                        menu[menuIndex + 1].getMenu().append(SCStaticTextTerminal.SCStaticTextTerminal(phrase))
        elif destId == -1:
            if not menu:
                print 'warning: no menu found'
                return
            for i in range(2):
                menu[i + 1].getMenu().clearMenu()
