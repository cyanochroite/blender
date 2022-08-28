# <pep8-80 compliant>
"""Light data-block for lighting a scene."""
from blender import data


def area(name):
    """Area – Directional area light source."""
    return data.light.new(name, 'AREA')


def point(name):
    """Point – Omnidirectional point light source."""
    return data.light.new(name, 'POINT')


def spot(name):
    """Spot – Directional cone light source."""
    return data.light.new(name, 'SPOT')


def sun(name):
    """Sun – Constant direction parallel ray light source."""
    return data.light.new(name, 'SUN')
