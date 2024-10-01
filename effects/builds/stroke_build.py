import uuid
from utils.color_util import rgb
from utils.opacity_util import calculation_opacity

def strokeBuild(effect, layer):
    red = effect.color[b'Rd  ']
    green = effect.color[b'Grn ']
    blue = effect.color[b'Bl  ']

    return {
        "id": f'stroke:{uuid.uuid4()}',
        "type": 'stroke',
        "stroke": rgb(red, green, blue),
        "strokeWidth": effect.size,
        "strokeEnabled": effect.enabled,
        "strokeOpacity": calculation_opacity(effect.opacity),
    }
