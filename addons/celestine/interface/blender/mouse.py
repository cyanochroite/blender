""""""
from math import radians

from celestine.typed import N

from .element import Abstract
from .package import mesh as _mesh
from .package.data import mesh as make_mesh

from .package.data.collection import _collection

from .package import data


COLLECTION = _collection


class Mouse(Abstract):
    """"""

    def __init__(self) -> N:
        self.text = "mouse"
        super().__init__("mouse")

    def draw(self, view: COLLECTION) -> N:
        """"""
        plane = _mesh.plane(self.text)
        self.item = make_mesh.bind(view, self.text, plane)

        self.render()

        mesh = data.mesh.make(view, self.text)
        mesh.location = (0, 0, -1)
        mesh.rotation_euler = (0, 0, radians(45))
        mesh.scale = (0.5, 0.5, 0.5)
        self.item = mesh

