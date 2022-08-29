# <pep8-80 compliant>
import bpy

from blender.data.most import most


class texture(most):
    """Light data-block for lighting a scene."""
    data = bpy.data.lights


class none(texture):
    """None."""
    type_ = 'NONE'


class blend(texture):
    """Blend – Procedural - create a ramp texture."""
    type_ = 'BLEND'


class clouds(texture):
    """Clouds – Procedural - create a cloud-like fractal noise texture."""
    type_ = 'CLOUDS'


class distorted_noise(texture):
    """
    Distorted Noise – Procedural - noise texture distorted by two noise
    algorithms.
    """
    type_ = 'DISTORTED_NOISE'


class image(texture):
    """Image or Movie – Allow for images or movies to be used as textures."""
    type_ = 'IMAGE'


class magic(texture):
    """Magic – Procedural - color texture based on trigonometric functions."""
    type_ = 'MAGIC'


class marble(texture):
    """
    Marble – Procedural - marble-like noise texture with wave generated bands.
    """
    type_ = 'MARBLE'


class musgrave(texture):
    """Musgrave – Procedural - highly flexible fractal noise texture."""
    type_ = 'MUSGRAVE'


class noise(texture):
    """
    Noise – Procedural - random noise, gives a different result every time, for
    every frame, for every pixel.
    """
    type_ = 'NOISE'


class stucci(texture):
    """Stucci – Procedural - create a fractal noise texture."""
    type_ = 'STUCCI'


class voronoi(texture):
    """
    Voronoi – Procedural - create cell-like patterns based on Worley noise.
    """
    type_ = 'VORONOI'


class wood(texture):
    """
    Wood – Procedural - wave generated bands or rings, with optional noise.
    """
    type_ = 'WOOD'


texture.none = none
texture.blend = blend
texture.clouds = clouds
texture.distorted_noise = distorted_noise
texture.image = image
texture.magic = magic
texture.marble = marble
texture.musgrave = musgrave
texture.noise = noise
texture.stucci = stucci
texture.voronoi = voronoi
texture.wood = wood
