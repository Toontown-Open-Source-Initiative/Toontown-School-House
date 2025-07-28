from panda3d.core import *
from direct.showbase import DConfig
import string
import types
try:
    language = DConfig.GetString('language', 'portuguese')
    checkLanguage = DConfig.GetBool('check-language', 0)
except:
    language = simbase.config.GetString('language', 'portuguese')
    checkLanguage = simbase.config.GetBool('check-language', 0)

def getLanguage():
    return language


print 'TTLocalizer: Running in language: %s' % language
if language == 'english':
    _languageModule = 'toontown.toonbase.TTLocalizer' + string.capitalize(language)
else:
    checkLanguage = 1
    _languageModule = 'toontown.toonbase.TTLocalizer_' + language
print 'from ' + _languageModule + ' import *'
from toontown.toonbase.TTLocalizer_portuguese import *
if checkLanguage:
    l = {}
    g = {}
    portugueseModule = __import__('toontown.toonbase.TTLocalizer_portuguese', g, l)
    foreignModule = __import__(_languageModule, g, l)
    for key, val in portugueseModule.__dict__.items():
        if key not in foreignModule.__dict__:
            print 'WARNING: Foreign module: %s missing key: %s' % (_languageModule, key)
            locals()[key] = val
        elif isinstance(val, types.DictType):
            fval = foreignModule.__dict__.get(key)
            for dkey, dval in val.items():
                if dkey not in fval:
                    print 'WARNING: Foreign module: %s missing key: %s.%s' % (_languageModule, key, dkey)
                    fval[dkey] = dval

            for dkey in fval.keys():
                if dkey not in val:
                    print 'WARNING: Foreign module: %s extra key: %s.%s' % (_languageModule, key, dkey)

    for key in foreignModule.__dict__.keys():
        if key not in portugueseModule.__dict__:
            print 'WARNING: Foreign module: %s extra key: %s' % (_languageModule, key)
