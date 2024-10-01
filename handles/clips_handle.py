from layers.layer_handle import layerHandle

def clipsHandle(clips):
    elements = []

    for clip in clips:
        if not clip.is_visible(): continue
            
        childLayer = layerHandle(clip)
        if childLayer == None: continue
        elements.append(childLayer)

    return elements
