from .package.data import mesh as make_mesh
from .package import mesh as _mesh

from .widget import Widget

from .package import data

from math import radians

from .widget import Widget


class Mouse(Widget):
    def __init__(self, rectangle):
        text = "mouse"
        collection = data.collection.scene()
        mesh = make_mesh.bind(collection, text, _mesh.plane(text))

        super().__init__(
            mesh,
            rectangle,
        )
        self.mesh.location = (1, 1, 1)
        self.mesh.rotation_euler = (0, 0, radians(45))
        self.mesh.scale = (0.5, 0.5, 0.5)
