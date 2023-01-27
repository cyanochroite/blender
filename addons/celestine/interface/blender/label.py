from .package.data import mesh as make_mesh
from .package import mesh as _mesh

from .widget import Widget


class Label(Widget):
    def __init__(self, collection, text, rectangle):
        mesh = _mesh.text(collection, text, text)
        super().__init__(
            mesh,
            rectangle,
        )

