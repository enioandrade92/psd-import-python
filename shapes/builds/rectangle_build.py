import uuid
from utils.opacity_util import check_opacity
from utils.stroke_util import stroke_rgb, stroke_width, stroke_is_enable
from utils.fill_util import fill_rgb
from psd_tools.constants import Tag
from effects.effect_handle import effectHandle

def rectangle_build(layer):
    format = layer.origination[0]

    return {
        "id": f'rect:{uuid.uuid4()}',
        "type": "rect",
        "name": layer.name,
        "props": {
            "width": layer.width,
            "height": layer.height,
            "x": layer.left,
            "y": layer.top,
            "cornerRadius": [0, 0, 0, 0],
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