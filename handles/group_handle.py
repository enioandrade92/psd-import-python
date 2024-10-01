from layers.layer_handle import layerHandle
from handles.clips_handle import clipsHandle

def process_layer(layer):
    if layer.clipping_layer or not layer.is_visible(): return None
    
    if layer.is_group(): return groupHandle(layer)
    
    if layer.has_clip_layers():
        baseLayer = layerHandle(layer)
        if baseLayer is None: return None
        
        if layer.kind == 'pixel' or layer.kind == 'smartobject': return baseLayer
        
        childLayers = clipsHandle(layer.clip_layers)
        baseLayer['props']['children'] = childLayers
        
        return baseLayer
    
    else:
        if layer.clipping_layer: return None
        
        baseLayer = layerHandle(layer)
        return baseLayer


def groupHandle(layers):
    elements = []
    for child in layers:
        processed_layer = process_layer(child)

        if isinstance(processed_layer, list):
            elements.extend(processed_layer)

        elif processed_layer is not None:
            elements.append(processed_layer)

    return elements