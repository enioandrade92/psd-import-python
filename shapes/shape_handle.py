from shapes.builds.invalidated_build import invalidated_build
from shapes.builds.rectangle_build import rectangle_build
from shapes.builds.rounded_rectangle_build import rounded_rectangle_build
from shapes.builds.line_build import line_build
from shapes.builds.ellipse_build import ellipse_build
from shapes.builds.basic_format import basic_format_build

originType = {
        'Rectangle': 1, 
        'RoundedRectangle': 2, 
        'Line': 4, 
        'Ellipse': 5, 
    }

def shape_handle(layer):
    if layer.has_origination() == False:
        return basic_format_build(layer)
    
    format = layer.origination[0]

    if format.invalidated:
        return invalidated_build(layer)

    elif format.origin_type == originType['Rectangle']:
        return rectangle_build(layer)

    elif format.origin_type == originType['RoundedRectangle']:
        return rounded_rectangle_build(layer)

    elif format.origin_type == originType['Line']:
        return line_build(layer)

    elif format.origin_type == originType['Ellipse']:
        return ellipse_build(layer)

    return None
