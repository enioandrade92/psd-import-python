import uuid
from utils.opacity_util import check_opacity
from utils.color_util import rgb
from effects.effect_handle import effectHandle

def solid_color_build(layer):
    # url_image = save_image(layer)
    red = layer._data[b'Clr '][b'Rd  ']
    green = layer._data[b'Clr '][b'Grn ']
    blue = layer._data[b'Clr '][b'Bl  ']
    return {
        "id": f'solidcolorfill:{uuid.uuid4()}',
        "type": 'solidcolorfill',
        "name": layer.name,
        "props": {
            "width": layer.width,
            "height": layer.height,
            "x": layer.left, 
            "y": layer.top,
            "fill": rgb(red, green, blue),
            # "src": url_image,
            "opacity": check_opacity(layer),
            "visible": layer.visible,
            "origination": str(layer.origination),
            "effects": effectHandle(layer),
            "children": []
        }
    }