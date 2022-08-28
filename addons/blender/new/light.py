# <pep8-80 compliant>
"""Light data-block for lighting a scene."""
from blender import data


def area(name):
    """Directional area Light."""
    return data.light.new(name, 'AREA')


def point(name):
    """Omnidirectional point Light."""
    return data.light.new(name, 'POINT')


def spot(name):
    """Directional cone Light."""
    return data.light.new(name, 'SPOT')


def sun(name):
    """Constant direction parallel ray Light."""
    return data.light.new(name, 'SUN')
