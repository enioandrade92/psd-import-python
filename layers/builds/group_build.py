import uuid
from utils.opacity_util import check_opacity
from utils.stroke_util import stroke_rgb, stroke_width, stroke_is_enable
from effects.effect_handle import effectHandle

def group_build(group):

    return {
        "id": f'group:{uuid.uuid4()}',
        "type": 'group',
        "name": group.name,
        "props": {
            "width": group.width,
            "height": group.height,
            "x": group.left, 
            "y": group.top,
            "opacity": check_opacity(group),
            "visible": group.visible,
            "stroke": stroke_rgb(group),
            "strokeWidth": stroke_width(group),
            "strokeEnabled": stroke_is_enable(group),
            "origination": str(group.origination),
            "effects": effectHandle(group),
            "children": []
        }
    }
    