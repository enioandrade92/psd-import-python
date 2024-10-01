
from effects.builds.deep_gradient_build import deepGradientLinearBuild, deepGradientRadialBuild
from psd_tools.constants import Tag

def typeHandle(effectData, layer):
    if b'Type' in effectData:
        if effectData[b'Type'].enum == b'Lnr ':
            effect = deepGradientLinearBuild(effectData, layer)
            return effect
        
        if effectData[b'Type'].enum == b'Rdl ':
            return deepGradientRadialBuild(effectData, layer)

    return None

def deepLayerEffectHandle(layer):
    vectorData = layer.tagged_blocks.get_data(Tag.VECTOR_STROKE_CONTENT_DATA)
    fillData = layer.tagged_blocks.get_data(Tag.GRADIENT_FILL_SETTING)

    if vectorData != None:
        return typeHandle(vectorData,layer)

    if fillData != None:
        return typeHandle(fillData, layer)

    return None