# <pep8-80 compliant>
from blender import data

import blender.new.light
import blender.new.texture


def camera(name):
    """Camera data-block for storing camera settings."""
    return data.camera.new(name)


def image(
    name,
    width,
    height,
    alpha=False,
    float_buffer=False,
    stereo3d=False,
    is_data=False,
    tiled=False,
):
    """Image data-block referencing an external or packed image."""
    return data.image.new(
        name,
        width,
        height,
        alpha,
        float_buffer,
        stereo3d,
        is_data,
        tiled,
    )


def material(name):
    """
    Material data-block to define the appearance of geometric objects for
    rendering.
    """
    return data.material.new(name)


def mesh(name):
    """Mesh data-block defining geometric surfaces."""
    return data.mesh.new(name)


def object(name, object_data):
    """Object data-block defining an object in a scene."""
    return data.object.new(name, object_data)
