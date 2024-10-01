import os
import base64
from io import BytesIO
from utils.file_util import file_name

def generate_image(layer):
    if layer.topil() == None:
        return None
    
    if layer.has_mask():
        image = layer.composite()
    else:
        image = layer.topil()

    # -- save image --
    # file = file_name()
    # directory = f'./images/{file}/'
    # image_name = f'{layer.name}.{layer.kind}.png'
    # output_path = directory + image_name
    # os.makedirs(directory, exist_ok=True)
    # image.save(output_path)

    buffer = BytesIO()
    image.save(buffer, format="PNG")

    base64_string = base64.b64encode(buffer.getvalue()).decode('utf-8')

    return f'data:image/png;base64,{base64_string}'