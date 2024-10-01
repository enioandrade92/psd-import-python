from psd_tools.constants import Tag

def calculation_opacity(input_number):    
    is_number = isinstance(input_number, (int, float))
    if is_number == False:
        return 1

    handled_number = input_number / 255
    rounded_number = round(handled_number, 1)

    return rounded_number

def check_opacity(layer):
    opacity = layer.tagged_blocks.get_data(Tag.BLEND_FILL_OPACITY) if layer.tagged_blocks.get_data(Tag.BLEND_FILL_OPACITY) else layer.opacity
    return calculation_opacity(opacity)





