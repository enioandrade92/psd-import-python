import uuid
from utils.opacity_util import check_opacity
from utils.stroke_util import stroke_rgb, stroke_width, stroke_is_enable
from utils.fill_util import fill_rgb
from effects.effect_handle import effectHandle

def invalidated_build(layer):
    format = layer.origination[0]

    return {
        "id": f'shape:{uuid.uuid4()}',
        "type": 'shape',
        "name": layer.name,
        "props": {
            "width": layer.width,
            "height": layer.height,
            "x": layer.left, 
            "y": layer.top,
            "opacity": check_opacity(layer),
            "visible": layer.visible,
            "fill": fill_rgb(layer, True),
            "stroke": stroke_rgb(layer),
            "strokeWidth": stroke_width(layer),
            "strokeEnabled": stroke_is_enable(layer),
            "origination": str(layer.origination),
            "effects": effectHandle(layer),
            "children": []
        }
    }