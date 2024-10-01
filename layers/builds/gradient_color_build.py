import uuid
from utils.opacity_util import check_opacity
from utils.color_util import rgb
from effects.effect_handle import effectHandle

def gradientHandle(data):
    gradient = {
        "gradient_type": str(data[b'GrdF']),
        "colorStops": []
    }

    for color in data[b'Clrs']:
        red = color[b'Clr '][b'Rd  ']
        green = color[b'Clr '][b'Grn ']
        blue = color[b'Clr '][b'Bl  ']

        gradient['colorStops'].append({
            "location": float(color[b'Lctn']) / float(data[b'Intr']), 
            "fill": rgb(red, green, blue)
        })

    return gradient



def gradient_color_build(layer):
    # url_image = save_image(layer)
    return {
        "id": f'gradientfill:{uuid.uuid4()}',
        "type": 'gradientfill',
        "name": layer.name,
        "props": {
            "width": layer.width,
            "height": layer.height,
            "x": layer.left, 
            "y": layer.top,
            "opacity": check_opacity(layer),
            "visible": layer.visible,
            "gradient": gradientHandle(layer.data),
            "origination": str(layer.origination),
            "effects": effectHandle(layer),
            "children": []
        }
    }