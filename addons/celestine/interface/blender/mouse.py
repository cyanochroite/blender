from .package.data import mesh as make_mesh
from .package import mesh as _mesh

from .element import Element

from .package import data

from math import radians


class Mouse(Element):
    def __init__(self):
        self.collection = data.collection.scene()
        self.text = "mouse"
        super().__init__()
        self.draw()

    def draw(self):
        plane = _mesh.plane(self.text)
        mesh = make_mesh.bind(self.collection, self.text, plane)
        super().draw(mesh)
        mesh.location = (1, 1, 1)
        mesh.rotation_euler = (0, 0, radians(45))
        mesh.scale = (0.5, 0.5, 0.5)

