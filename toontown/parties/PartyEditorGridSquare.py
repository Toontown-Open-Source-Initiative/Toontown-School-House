#-------------------------------------------------------------------------------
# Contact: Shawn Patton
# Created: Oct 2008
#
# Purpose: PartyEditorGridSquares can have PartyEditorGridElements dragged on
#          top of them.
#-------------------------------------------------------------------------------

from panda3d.core import Vec3, Vec4, Point3, TextNode, VBase4

from direct.gui.DirectGui import DirectFrame, DirectButton, DirectLabel, DirectScrolledList, DirectCheckButton
from direct.gui import DirectGuiGlobals
from direct.showbase.DirectObject import DirectObject
from direct.showbase import PythonUtil

from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from toontown.parties import PartyGlobals
from toontown.parties.PartyInfo import PartyInfo
from toontown.parties import PartyUtils

class PartyEditorGridSquare(DirectObject):
    """
    PartyEditorGridSquares can have PartyEditorGridElements dragged onto them
    """
    notify = directNotify.newCategory("PartyEditorGridSquare")

    def __init__(self, partyEditor, x, y):
        self.partyEditor = partyEditor
        self.x = x
        self.y = y
        self.gridElement = None

    def getPos(self):
        aspectRatio = base.camLens.getAspectRatio()
        if aspectRatio >= 1.6:
            bounds = PartyGlobals.PartyEditorGridBoundsWidescreen
            squareSize = PartyGlobals.PartyEditorGridSquareSizeWidescreen
        else:
            bounds = PartyGlobals.PartyEditorGridBounds
            squareSize = PartyGlobals.PartyEditorGridSquareSize

        return Point3(
            bounds[0][0] + self.x*squareSize[0] + squareSize[0]/2.0,
            0.0,
            bounds[1][1] + (PartyGlobals.PartyEditorGridSize[1]-1-self.y)*squareSize[1] + squareSize[1]/2.0,
        )

    def destroy(self):
        # Grid elements get destroyed by their list element
        del self.gridElement
