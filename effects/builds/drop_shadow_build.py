import uuid
import math
from utils.color_util import rgb

def dropShadowBuild(effect, layer):
    red = effect.color[b'Rd  ']
    green = effect.color[b'Grn ']
    blue = effect.color[b'Bl  ']

    return {
        "id": f'dropShadow:{uuid.uuid4()}',
        "type": 'dropShadow',
        "shadowOpacity": effect.opacity / 100,
        "shadowBlur": effect.size,
        "shadowColor": rgb(red, green, blue),
        "shadowEnabled": effect.enabled,
        "shadowOffset": {
            "x": effect.distance * math.sin(effect.angle),
            "y": effect.distance * math.cos(effect.angle),
        }
    }
