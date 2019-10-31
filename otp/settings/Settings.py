import json
import os

from direct.directnotify import DirectNotifyGlobal


class Settings:
    """
    The Settings class is responsible for reading our JSON formatted settings files
    and returning the values from that settings file back to whatever requested them.

    This class can either be inherited by another settings class, or instantiated directly.
    Either way, an ideal setup would have some form of this class instantiated in whatever ShowBase
    class you are using, and accessible via base.settings.
    """
    notify = DirectNotifyGlobal.directNotify.newCategory('Settings')

    def __init__(self, fileName='settings.json'):
        # The name of the settings file.
        self.fileName = fileName

        # The settings file might be located inside of another directory. If it doesn't already exist, we want
        # to create that directory, otherwise the file won't be able to be saved.
        if os.path.dirname(self.fileName) and not os.path.exists(os.path.dirname(self.fileName)):
            os.makedirs(os.path.dirname(self.fileName))

        # Let's attempt to load the settings file.
        try:
            with open(self.fileName, 'r') as f:
                self.settings = json.load(f)
        except:
            # If we got here, then that means that we weren't able to load the settings file, for whatever reason.
            # In this case, we will just define an empty settings dictionary.
            self.settings = {}

    def getOption(self, category, attribute, default):
        """
        This is a generic function used to fetch the saved configuration settings.
        This should probably be used by a more sane helper function, but you could
        use this by itself if you wanted to...
        """
        return self.settings.get(category, {}).get(attribute, default)

    def getBool(self, category, attribute, default=False):
        """
        Given a category and an attribute, will attempt to fetch the boolean value corresponding
        to the attribute in the given category. If an incorrect type is fetched, or there doesn't
        exist a result at all, return the default.
        """
        value = self.getOption(category, attribute, default)
        if isinstance(value, bool):
            return value
        else:
            return default

    def getFloat(self, category, attribute, default=1.0):
        """
        Given a category and an attribute, will attempt to fetch the float value corresponding
        to the attribute in the given category. If an incorrect type is fetched, or there doesn't
        exist a result at all, return the default.
        """
        value = self.getOption(category, attribute, default)
        if isinstance(value, float):
            return value
        else:
            return default

    def getList(self, category, attribute, default=[], expectedLength=2):
        """
        Given a category and an attribute, will attempt to fetch the list value corresponding
        to the attribute in the given category. If an incorrect type is fetched, or there doesn't
        exist a result at all, return the default.
        """
        value = self.getOption(category, attribute, default)
        if isinstance(value, list) and len(value) == expectedLength:
            return value
        else:
            return default

    def getInt(self, category, attribute, default=0):
        """
        Given a category and an argument, will attempt to fetch the int value corresponding
        to the attribute in the given category. If an incorrect type is fetched, or there doesn't
        exist a result at all, return the default.
        """
        value = self.getOption(category, attribute, default)
        if isinstance(value, (int, long)):
            return int(value)
        else:
            return default

    def doSavedSettingsExist(self):
        return os.path.exists(self.fileName)

    def writeSettings(self):
        """
        Attempts to write the data from the settings dictionary to the settings file.
        """
        with open(self.fileName, 'w+') as f:
            json.dump(self.settings, f, indent=4)

    def updateSetting(self, category, attribute, value):
        """
        Given a category, an attribute, and a value, will attempt to update the settings
        dictionary with the given data.
        """
        if not self.settings.get(category):
            self.settings[category] = {}

        self.settings[category][attribute] = value
        self.writeSettings()
