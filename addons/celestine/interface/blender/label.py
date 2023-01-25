from .package.data import mesh as make_mesh
from .package import mesh as _mesh

from .widget import Widget


class Label(Widget):
    def __init__(self, text, rectangle):
        _mesh.text()
        mesh = make_mesh.make(text, _mesh.plane(text))
        super().__init__(
            mesh,
            rectangle,
        )

