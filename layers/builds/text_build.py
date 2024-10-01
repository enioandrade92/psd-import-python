import uuid
from utils.opacity_util import check_opacity
from utils.stroke_util import stroke_rgb, stroke_width, stroke_is_enable
from utils.color_util import rgba
from effects.effect_handle import effectHandle

def process_color(color_values):
    return rgba(color_values[1] * 255, color_values[2] * 255, color_values[3] * 255, color_values[0])

def text_build(layer):
    text = layer.engine_dict['Editor']['Text'].value
    fontset = layer.resource_dict['FontSet']
    runlength = layer.engine_dict['StyleRun']['RunLengthArray']
    rundata = layer.engine_dict['StyleRun']['RunArray']
    gridInfo = layer.engine_dict['GridInfo']
    red, green, blue, alpha = gridInfo['GridColor']['Values']

    texts = []
    index = 0

    for length, style in zip(runlength, rundata):
        stylesheet = style['StyleSheet']['StyleSheetData']
        font_index = stylesheet['Font']
        
        # Acesso direto ao dicionário de fontes na lista
        font = fontset[font_index]['Name'].value if font_index < len(fontset) else 'default-font-name'
        substring = text[index:index + length]

        text_props = {
            "text": substring,
            "fontFamily": font,
            "fontSize": float(stylesheet['FontSize']),
            "fontBold": bool(stylesheet['FauxBold']),
            "fontItalic": bool(stylesheet['FauxItalic']),
            "fontUnderline": bool(stylesheet['Underline']),
            "fill": process_color(stylesheet['FillColor']['Values']),
            "stroke": process_color(stylesheet['StrokeColor']['Values']),
            "AutoLeading": bool(stylesheet['AutoLeading']),
            "Leading": str(stylesheet['Leading']),
            "HorizontalScale": str(stylesheet['HorizontalScale']),
            "VerticalScale": str(stylesheet['VerticalScale']),
            "Tracking": str(stylesheet['Tracking']),
            "AutoKerning": str(stylesheet['AutoKerning']),
            "Kerning": str(stylesheet['Kerning']),
            "BaselineShift": str(stylesheet['BaselineShift']),
            "FontCaps": str(stylesheet['FontCaps']),
            "FontBaseline": str(stylesheet['FontBaseline']),
            "Strikethrough": str(stylesheet['Strikethrough']),
            "Ligatures": str(stylesheet['Ligatures']),
            "DLigatures": str(stylesheet['DLigatures']),
            "BaselineDirection": str(stylesheet['BaselineDirection']),
            "Tsume": str(stylesheet['Tsume']),
            "StyleRunAlignment": str(stylesheet['StyleRunAlignment']),
            "Language": str(stylesheet['Language']),
            "NoBreak": str(stylesheet['NoBreak']),
            "YUnderline": str(stylesheet['YUnderline']),
            "HindiNumbers": str(stylesheet['HindiNumbers']),
            "Kashida": str(stylesheet['Kashida']),
        }

        texts.append(text_props)
        index += length

    return {
        "id": f'text:{uuid.uuid4()}',
        "type": 'text',
        "name": layer.name,
        "props": {
            "width": layer.width,
            "height": layer.height,
            "x": layer.left, 
            "y": layer.top, 
            "texts": texts,
            "opacity": check_opacity(layer),
            "visible": layer.visible,
            "stroke": stroke_rgb(layer),
            "strokeWidth": stroke_width(layer),
            "strokeEnabled": stroke_is_enable(layer),
            "fill": rgba(red, green, blue, alpha),
            "origination": str(layer.origination),
            "effects": effectHandle(layer),
            "children": []
        }
    }
