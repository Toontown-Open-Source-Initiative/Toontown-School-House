from otp.level import EntityCreator
from . import FactoryLevelMgr
from . import PlatformEntity
from . import ConveyorBelt
from . import GearEntity
from . import PaintMixer
from . import GoonClipPlane
from . import MintProduct
from . import MintProductPallet
from . import MintShelf
from . import PathMasterEntity
from . import RenderingEntity

class FactoryEntityCreator(EntityCreator.EntityCreator):

    def __init__(self, level):
        EntityCreator.EntityCreator.__init__(self, level)
        nothing = EntityCreator.nothing
        _nonlocal = EntityCreator._nonlocal
        self.privRegisterTypes({'activeCell': _nonlocal,
         'crusherCell': _nonlocal,
         'battleBlocker': _nonlocal,
         'beanBarrel': _nonlocal,
         'button': _nonlocal,
         'conveyorBelt': ConveyorBelt.ConveyorBelt,
         'crate': _nonlocal,
         'door': _nonlocal,
         'directionalCell': _nonlocal,
         'gagBarrel': _nonlocal,
         'gear': GearEntity.GearEntity,
         'goon': _nonlocal,
         'gridGoon': _nonlocal,
         'golfGreenGame': _nonlocal,
         'goonClipPlane': GoonClipPlane.GoonClipPlane,
         'grid': _nonlocal,
         'healBarrel': _nonlocal,
         'levelMgr': FactoryLevelMgr.FactoryLevelMgr,
         'lift': _nonlocal,
         'mintProduct': MintProduct.MintProduct,
         'mintProductPallet': MintProductPallet.MintProductPallet,
         'mintShelf': MintShelf.MintShelf,
         'mover': _nonlocal,
         'paintMixer': PaintMixer.PaintMixer,
         'pathMaster': PathMasterEntity.PathMasterEntity,
         'rendering': RenderingEntity.RenderingEntity,
         'platform': PlatformEntity.PlatformEntity,
         'sinkingPlatform': _nonlocal,
         'stomper': _nonlocal,
         'stomperPair': _nonlocal,
         'laserField': _nonlocal,
         'securityCamera': _nonlocal,
         'elevatorMarker': _nonlocal,
         'trigger': _nonlocal,
         'moleField': _nonlocal,
         'maze': _nonlocal})
