from panda3d.core import *
from panda3d.physics import *
from direct.directnotify import DirectNotifyGlobal
from toontown.battle import BattleParticles

class CarSmoke(NodePath):
    def __init__(self, parent):
        # Initialize the superclass
        NodePath.__init__(self)

        notify = DirectNotifyGlobal.directNotify.newCategory('CarSmokeParticles')

        self.effectNode = parent.attachNewNode('carSmoke')
        self.effectNode.setBin("fixed", 1)
        self.effectNode.setDepthWrite(0)     
        self.effect = BattleParticles.loadParticleFile('smokeTest4.ptf')
        ren = self.effect.getParticlesNamed('particles-1').getRenderer()
        ren.setTextureFromNode('phase_4/models/props/tt_m_efx_ext_smoke','**/*')        

    def start(self):
        self.effect.start(parent = self.effectNode)

    def stop(self):
        try:
            self.effect.disable()
        except AttributeError:
            pass

    def destroy(self):
        self.stop()
        self.effect.cleanup()
        self.effectNode.removeNode()
        del self.effect
        del self.effectNode
