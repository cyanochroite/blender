# <pep8-80 compliant>
import bpy

from blender.data.most import most


class light(most):
    """Light data-block for lighting a scene."""
    data = bpy.data.lights


class area(light):
    """Area – Directional area light source."""
    type_ = 'AREA'


class point(light):
    """Point – Omnidirectional point light source."""
    type_ = 'POINT'


class spot(light):
    """Spot – Directional cone light source."""
    type_ = 'SPOT'


class sun(light):
    """Sun – Constant direction parallel ray light source."""
    type_ = 'SUN'


light.area = area
light.point = point
light.spot = spot
light.sun = sun
