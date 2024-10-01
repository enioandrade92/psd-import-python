from effects.builds.drop_shadow_build import dropShadowBuild
from effects.builds.gradient_overlay_build import gradientOverlayBuild
from effects.builds.stroke_build import strokeBuild
from effects.deep_layer_effect_handle import deepLayerEffectHandle

def effectHandle(layer):
    effects = []

    deepEffect = deepLayerEffectHandle(layer)
    if deepEffect != None:
        effects.append(deepEffect)

    if layer.has_effects():
        for effect in layer.effects:
            name = effect.__class__.__name__

            if name == 'GradientOverlay':
                gradientEffect = gradientOverlayBuild(effect, layer)
                if gradientEffect != None:
                    effects.append(gradientEffect)
                continue
            
            if name == 'DropShadow':
                dropShadowEffect = dropShadowBuild(effect, layer)
                if dropShadowEffect != None:
                    effects.append(dropShadowEffect)
                continue

            if name == 'Stroke':
                strokeEffect = strokeBuild(effect, layer)
                if strokeEffect != None:
                    effects.append(strokeEffect)
                continue
            
        return effects
   
    return effects