import uuid
import math
from utils.color_util import rgb

def fillColorStopsHandle(items):
    fillColorStops = []

    for item in items:
       fillColorStops.append(float(item[b'Lctn'] / 4096))
       fillColorStops.append(rgb(item[b'Clr '][b'Rd  '], item[b'Clr '][b'Grn '], item[b'Clr '][b'Bl  ']))
    
    return fillColorStops

def gradientLinearBuild(effect, layer):
    angle = math.radians(effect.value[b'Angl'])
    fillColorStops = fillColorStopsHandle(effect.value[b'Grad'][b'Clrs'])

    return {
        "id": f'linearGradient:{uuid.uuid4()}',
        "type": 'linearGradient',
        "fillLinearGradientEndPoint":{ 
            "x": float(effect.offset[b'Hrzn']),
            "y": float(effect.offset[b'Vrtc']),
        },
        "fillLinearGradientStartPoint":{ 
            "x" : float(effect.offset[b'Hrzn']) + math.cos(angle) * layer.width,
            "y" : float(effect.offset[b'Vrtc']) + math.sin(angle) * layer.height,
        },
        "fillLinearGradientColorStops": fillColorStops,
        "fillLinearGradientEnabled": effect.enabled,
    }

def gradientRadialBuild(effect, layer):
    fillColorStops = fillColorStopsHandle(effect.value[b'Grad'][b'Clrs'])

    return {
        "id": f'radialGradient:{uuid.uuid4()}',
        "type": 'radialGradient',
        "fillRadialGradientStartPoint":{ 
            "x": float(effect.offset[b'Hrzn']),
            "y": float(effect.offset[b'Vrtc']),
        },
        "fillRadialGradientEndPoint":{ 
            "x": float(effect.offset[b'Vrtc']),
            "y": float(effect.offset[b'Hrzn']),
        },
        "fillRadialGradientStartRadius": 0,
        "fillRadialGradientEndRadius": effect.scale,
        "fillRadialGradientColorStops": fillColorStops,
        "fillRadialGradientEnabled": effect.enabled,
    }

def gradientOverlayBuild(effect, layer):
    if effect.type == b'Lnr ':
        return gradientLinearBuild(effect, layer)
    
    if effect.type == b'Rdl ':
        return gradientRadialBuild(effect, layer)
    
    return None