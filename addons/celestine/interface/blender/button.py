from .package.data import mesh as make_mesh
from .package import mesh as _mesh

from .widget import Widget


class Button(Widget):
    def __init__(self, text, action, rectangle):
        mesh = make_mesh.make(text, _mesh.plane(text))
        super().__init__(
            mesh,
            rectangle,
        )
        self.action = action
