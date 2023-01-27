from .widget import Widget

from .package import data
from .package import UV
from .package.data import mesh as make_mesh
from .package import mesh as _mesh


class Image(Widget):
    def __init__(self, collection, name, rectangle):
        image = data.image.load(name)
        material = UV.material("pretty", image)
        mesh = make_mesh.bind(collection, name, _mesh.image(image))
        mesh.body.data.materials.append(material)
        super().__init__(
            mesh,
            rectangle,
        )
