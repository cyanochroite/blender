from .package.data import mesh as make_mesh
from .package import mesh as _mesh

from .widget import Widget


class Button(Widget):
    def __init__(self, collection, text, action, rectangle):
        self.collection = collection
        self.text = text

        super().__init__(rectangle)

        self.action = action

        self.draw()

    def draw(self):
        width = len(self.text) / 4
        height = 1 / 20

        plane = _mesh.plane(self.text)
        mesh = make_mesh.bind(self.collection, self.text, plane)
        mesh.scale = (width, height, 1)

        word = _mesh.text(self.collection, self.text, self.text)
        word.scale = (1 / width, 1 / height, 1)
        word.location = (- width / 4, - height, 0.1)

        word.parent = mesh

        super().draw(mesh)

