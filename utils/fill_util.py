from utils.color_util import rgb
from psd_tools.constants import Tag

def fill_rgb(layer, orStroke = False):
    if orStroke:
        color = layer.tagged_blocks.get_data(Tag.SOLID_COLOR_SHEET_SETTING) or layer.tagged_blocks.get_data(Tag.VECTOR_STROKE_CONTENT_DATA)
    else:
        color = layer.tagged_blocks.get_data(Tag.SOLID_COLOR_SHEET_SETTING)

    if color == None or b'Clr ' not in color:
        return None

    return rgb(
        red = color[b'Clr '][b'Rd  '],
        green = color[b'Clr '][b'Grn '],
        blue = color[b'Clr '][b'Bl  '],
    )

