import sys
if sys.version.startswith('3.6'):
    from .py36.libpandadna import *
else:
    if sys.platform == "darwin":
        # Create folder in /Library/Developer/Panda3D and call it pandaMac and drop libpandadna.so in there
        from pandaMac.libpandadna import *
    else:
        from .libpandadna import *