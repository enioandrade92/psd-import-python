import json
import uuid
from layers.layer_handle import layerHandle
from psd_tools import PSDImage
from utils.file_util import file_name
from handles.group_handle import groupHandle
from handles.clips_handle import clipsHandle

file = file_name()
input_path = f'./psd/{file}.psd'
output_path = f'./json/{file}.json'

psd = PSDImage.open(input_path)

elements = []
for layer in psd:
    if not layer.is_visible() or layer.clipping_layer:
        continue

    if layer.is_group():
        layersGroup = groupHandle(layer)
        elements.extend(layersGroup)
        continue

    if layer.has_clip_layers():
        baseLayer = layerHandle(layer)
        if baseLayer == None: continue
        if layer.kind == 'pixel' or layer.kind == 'smartobject':
            elements.append(baseLayer)
            continue

        childLayers = clipsHandle(layer.clip_layers)
        baseLayer['props']['children'] = childLayers

        elements.append(baseLayer)
        continue

    baseLayer = layerHandle(layer)
    if baseLayer == None: continue
    elements.append(baseLayer)

page = {
    "width": psd.width,
    "height": psd.height,
    "pages": [
        {
            "id": f'page:{uuid.uuid4()}',
            "name": "Page 1",
            "elements": elements,
        }
    ]
}

with open(output_path, 'w') as file:
    json.dump(page, file, indent=4)
