from panda3d.core import *
from panda3d.physics import *
from direct.particles import ParticleEffect
from direct.directnotify import DirectNotifyGlobal
from toontown.battle import BattleParticles

class Sparks(NodePath):
    def __init__(self, parent, renderParent):
        # Initialize the superclass
        NodePath.__init__(self)

        notify = DirectNotifyGlobal.directNotify.newCategory('SparkParticles')

        self.renderParent = renderParent.attachNewNode("sparkRenderParent")
        self.renderParent.setBin("fixed", 0)
        self.renderParent.setDepthWrite(0)
        self.assign(parent.attachNewNode('sparks'))
        self.effect = BattleParticles.loadParticleFile('sparks.ptf')
        ren = self.effect.getParticlesNamed('particles-1').getRenderer()
        ren.setTextureFromNode('phase_6/models/karting/particleSpark','**/*')
        
    def start(self):
        self.effect.start(self, self.renderParent)

    def stop(self):
        try:
            self.effect.disable()
        except AttributeError:
            pass

    def destroy(self):
        self.stop()
        self.effect.cleanup()
        self.renderParent.removeNode()
        del self.effect
        del self.renderParent
