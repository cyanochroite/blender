from .package.data import mesh as make_mesh
from .package import mesh as _mesh

from .element import Element


class Label(Element):
    def __init__(self, collection, text, rectangle):
        self.collection = collection
        self.text = text
        super().__init__(rectangle)
        self.draw()

    def draw(self):
        mesh = _mesh.text(self.collection, self.text, self.text)
        super().draw(mesh)

