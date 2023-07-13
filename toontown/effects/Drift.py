from panda3d.core import *
from panda3d.physics import *
from direct.directnotify import DirectNotifyGlobal
from toontown.battle import BattleParticles

class Drift(NodePath):
    def __init__(self, parent, renderParent):
        # Initialize the superclass
        NodePath.__init__(self)

        notify = DirectNotifyGlobal.directNotify.newCategory('DriftParticles')

        self.renderParent = renderParent.attachNewNode("driftRenderParent")
        self.renderParent.setBin("fixed", 0)
        self.renderParent.setDepthWrite(0)
        self.assign(parent.attachNewNode('drift'))
        self.effect = BattleParticles.loadParticleFile('drift.ptf')
        ren = self.effect.getParticlesNamed('particles-1').getRenderer()
        ren.setTextureFromNode('phase_6/models/karting/driftSmoke','**/*')

    def start(self):
        self.effect.start(self, self.renderParent)

    def stop(self):
        self.effect.disable()

    def destroy(self):
        self.stop()
        self.effect.cleanup()
        self.renderParent.removeNode()
        del self.effect
        del self.renderParent