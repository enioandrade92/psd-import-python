from utils.opacity_util import check_opacity
from utils.stroke_util import stroke_rgb, stroke_width, stroke_is_enable

def mask_build(layer): 
    if layer.mask == None:
        return layer.mask
    
    return {
        "backgroundColor": layer.mask.background_color,
        "left-top-right-bottom": layer.mask.bbox,
        "flags": str(layer.mask.flags),
        "realFlags": str(layer.mask.real_flags),
        "width": layer.width,
        "height": layer.height,
        "x": layer.left, 
        "y": layer.top,
        "opacity": check_opacity(layer),
        "visible": layer.visible,
        "stroke": stroke_rgb(layer),
        "strokeWidth": stroke_width(layer),
        "strokeEnabled": stroke_is_enable(layer),

    }
    