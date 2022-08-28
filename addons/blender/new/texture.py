# <pep8-80 compliant>
"""Texture data-block used by materials, lights, worlds and brushes."""
from blender import data


def none(name):
    """None."""
    return data.texture.new(name, 'NONE')


def blend(name):
    """Blend – Procedural - create a ramp texture."""
    return data.texture.new(name, 'BLEND')


def clouds(name):
    """Clouds – Procedural - create a cloud-like fractal noise texture."""
    return data.texture.new(name, 'CLOUDS')


def distorted_noise(name):
    """
    Distorted Noise – Procedural - noise texture distorted by two noise
    algorithms.
    """
    return data.texture.new(name, 'DISTORTED_NOISE')


def image(name):
    """Image or Movie – Allow for images or movies to be used as textures."""
    return data.texture.new(name, 'IMAGE')


def magic(name):
    """Magic – Procedural - color texture based on trigonometric functions."""
    return data.texture.new(name, 'MAGIC')


def marble(name):
    """
    Marble – Procedural - marble-like noise texture with wave generated bands.
    """
    return data.texture.new(name, 'MARBLE')


def musgrave(name):
    """Musgrave – Procedural - highly flexible fractal noise texture."""
    return data.texture.new(name, 'MUSGRAVE')


def noise(name):
    """
    Noise – Procedural - random noise, gives a different result every time, for
    every frame, for every pixel.
    """
    return data.texture.new(name, 'NOISE')


def stucci(name):
    """Stucci – Procedural - create a fractal noise texture."""
    return data.texture.new(name, 'STUCCI')


def voronoi(name):
    """
    Voronoi – Procedural - create cell-like patterns based on Worley noise.
    """
    return data.texture.new(name, 'VORONOI')


def wood(name):
    """
    Wood – Procedural - wave generated bands or rings, with optional noise.
    """
    return data.texture.new(name, 'WOOD')
