def clips_order(psd):
    isClip = []
    isNotClip = []
    for layer in psd:
        if layer.has_clip_layers() or layer.is_group():
            isClip.append(layer)
        else:
            isNotClip.append(layer)

    orderedPsd = isClip + isNotClip
    return orderedPsd