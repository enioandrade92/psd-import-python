import uuid
from utils.opacity_util import check_opacity
from utils.stroke_util import stroke_rgb, stroke_width, stroke_is_enable
from utils.fill_util import fill_rgb
from effects.effect_handle import effectHandle

def ellipse_build(layer):
    format = layer.origination[0]
    radiusX = float(layer.width) / 2
    radiusY = float(layer.height) / 2

    return {
        "id": f'ellipse:{uuid.uuid4()}',
        "type": 'ellipse',
        "name": layer.name,
        "props": {
            "radiusX": radiusX,
            "radiusY": radiusY,
            "x": layer.left + radiusX,
            "y": layer.top + radiusY,
            "resolution": format.resolution,
            "index": int(format.index),
            "opacity": check_opacity(layer),
            "visible": layer.visible,
            "fill": fill_rgb(layer, True),
            "stroke": stroke_rgb(layer),
            "strokeWidth": stroke_width(layer),
            "strokeEnabled": stroke_is_enable(layer),
            "effects": effectHandle(layer),
            "children": []
        }
    }
