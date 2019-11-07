from direct.directnotify import DirectNotifyGlobal
from panda3d.core import loadPrcFileData

from otp.settings.Settings import Settings


class ToontownSettings(Settings):
    notify = DirectNotifyGlobal.directNotify.newCategory('ToontownSettings')

    def loadFromSettings(self):
        # Setting for toggling stretched screen.
        # Stretched screen forces the aspect ratio to be 4:3, or 1.333.
        stretchedScreen = self.getBool('game', 'stretched-screen', False)
        if stretchedScreen:
            loadPrcFileData('toonBase Settings Stretched Screen', 'aspect-ratio 1.333')
        else:
            self.updateSetting('game', 'stretched-screen', stretchedScreen)

        # Setting for a semi-custom Magic Word activator.
        # We will give players a list of which activators will work, and which will not.
        magicWordActivator = self.getInt('game', 'magic-word-activator', 0)
        loadPrcFileData('toonBase Settings Magic Word Activator', 'magic-word-activator %d' % magicWordActivator)
        self.updateSetting('game', 'magic-word-activator', magicWordActivator)
