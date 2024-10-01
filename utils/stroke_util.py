from utils.color_util import rgb

def stroke_rgb(layer):
    if layer.has_stroke(): 
        stroke = layer.stroke._data

        return rgb(
            stroke[b'strokeStyleContent'][b'Clr '][b'Rd  '],
            stroke[b'strokeStyleContent'][b'Clr '][b'Grn '],
            stroke[b'strokeStyleContent'][b'Clr '][b'Bl  '],
        )

    return None

def stroke_width(layer):
    if layer.has_stroke(): 
        stroke = layer.stroke._data
        return float(stroke[b'strokeStyleLineWidth'])
    
    return None

def stroke_is_enable(layer):
    if layer.has_stroke(): 
        return layer.stroke.enabled
    
    return False