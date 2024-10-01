import uuid
from utils.opacity_util import check_opacity
from utils.stroke_util import stroke_rgb, stroke_width, stroke_is_enable
from effects.effect_handle import effectHandle

def line_build(layer):
    format = layer.origination[0]

    return {
        "id": f'line:{uuid.uuid4()}',
        "type": "line",
        "name": layer.name,
        "props": {
            "width": layer.width,
            "height": layer.height,
            "x": layer.left, 
            "y": layer.top,
            "opacity": check_opacity(layer),
            "visible": layer.visible,
            "stroke": stroke_rgb(layer),
            "strokeWidth": stroke_width(layer),
            "strokeEnabled": stroke_is_enable(layer),
            "arrowStart": format.arrow_start,
            "arrowEnd": format.arrow_end,
            "arrowWidth": format.arrow_width,
            "arrowConc": format.arrow_conc,
            "arrowLength": format.arrow_length,
            "lineStart": format.line_start,
            "lineEnd": format.line_end,
            "lineWeight": format.line_weight,
            "resolution": format.resolution,
            "index": int(format.index),
            "effects": effectHandle(layer),
            "children": [],
        }
    }

    