import uuid
import math
from utils.color_util import rgb
from psd_tools.constants import Tag
from effects.builds.gradient_overlay_build import fillColorStopsHandle

def deepGradientLinearBuild(effectData, layer):
    angle = math.radians(effectData[b'Angl'])
    fillColorStops = fillColorStopsHandle(effectData[b'Grad'][b'Clrs'])
    enabled = bool(effectData[b'Dthr']) if b'Dthr' in effectData else True

    return {
        "id": f'linearGradient:{uuid.uuid4()}',
        "type": 'linearGradient',
        "fillLinearGradientEndPoint":{ 
            "x": 0.0,
            "y": 0.0,
        },
        "fillLinearGradientStartPoint":{ 
            "x" : float(math.cos(angle) * layer.width),
            "y" : float(math.sin(angle) * layer.height),
        },
        "fillLinearGradientColorStops": fillColorStops,
        "fillLinearGradientEnabled": enabled,
    }

def deepGradientRadialBuild(effectData, layer):
    fillColorStops = fillColorStopsHandle(effectData[b'Grad'][b'Clrs'])
    length = len(effectData[b'Grad'][b'Clrs'])
    scale = float(effectData[b'Grad'][b'Clrs'][length -1][b'Lctn'] / 4096)
    centerX = float(layer.width / 2)
    centerY = float(layer.height / 2)
    enabled = bool(effectData[b'Dthr']) if b'Dthr' in effectData else True

    return {
        "id": f'radialGradient:{uuid.uuid4()}',
        "type": 'radialGradient',
        "fillRadialGradientStartPoint":{ 
            "x": centerX,
            "y": centerY,
        },
        "fillRadialGradientEndPoint":{ 
            "x": centerX + float(layer.width * scale / 2),
            "y": centerY + float(layer.height * scale / 2),
        },
        "fillRadialGradientStartRadius": scale,
        "fillRadialGradientColorStops": fillColorStops,
        "fillRadialGradientEnabled": enabled,
    }
