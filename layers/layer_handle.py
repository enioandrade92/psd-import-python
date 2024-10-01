from layers.builds.text_build import text_build
from layers.builds.solid_color_build import solid_color_build
from layers.builds.pixel_build import pixel_build
from layers.builds.smart_object_build import smart_object_build
from layers.builds.group_build import group_build
from layers.builds.gradient_color_build import gradient_color_build
from shapes.shape_handle import shape_handle
from utils.string_util import normalize_string

# Build our data structure from the library data structure
def layerHandle(layer):
    layer.name = normalize_string(layer.name)

    if layer.kind == 'solidcolorfill':
        return solid_color_build(layer)
    
    if layer.kind == 'gradientfill':
        return gradient_color_build(layer)
    
    if layer.kind == 'pixel':
        return pixel_build(layer)

    if layer.kind == 'smartobject':
        return smart_object_build(layer)

    if layer.kind == 'type':
        return text_build(layer)

    if layer.kind == 'shape':
        return shape_handle(layer)
    
    if layer.kind == 'huesaturation':
        return None
    
    return None