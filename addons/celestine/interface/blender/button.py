from .package.data import mesh as make_mesh
from .package import mesh as _mesh

from .widget import Widget


class Button(Widget):
    def __init__(self, collection, text, action, rectangle):
        width = len(text) / 4
        height = 1 / 20

        mesh = make_mesh.bind(collection, text, _mesh.plane(text))
        mesh.scale = (width, height, 1)

        word = _mesh.text(collection, text, text)
        word.scale = (1 / width, 1 / height, 1)
        word.location = (- width / 4, - height, 0.1)

        word.parent = mesh
        super().__init__(
            mesh,
            rectangle,
        )
        self.action = action
