import uuid
from utils.image_util import generate_image
from utils.opacity_util import check_opacity
from utils.stroke_util import stroke_rgb, stroke_width, stroke_is_enable
from effects.effect_handle import effectHandle

def pixel_build(layer):
    url_image = generate_image(layer)

    return {
        "id": f'image:{uuid.uuid4()}',
        "type": 'image',
        "name": layer.name,
        "props": {
            "width": layer.width,
            "height": layer.height,
            "x": layer.left, 
            "y": layer.top,
            "opacity": calculation_opacity(layer.opacity),
            # "mask": mask_build(layer),
            "src": url_image,
            "opacity": check_opacity(layer),
            "visible": layer.visible,
            "stroke": stroke_rgb(layer),
            "strokeWidth": stroke_width(layer),
            "strokeEnabled": stroke_is_enable(layer),
            "origination": str(layer.origination),
            "effects": effectHandle(layer),
            "children": []
        }
    }
