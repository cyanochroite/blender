from .element import Element

from .package import data
from .package import UV
from .package.data import mesh as make_mesh
from .package import mesh as _mesh


class Image(Element):
    def __init__(self, collection, name, **kwargs):
        self.collection = collection
        self.name = name
        super().__init__(**kwargs)

    def draw(self):
        image = data.image.load(self.name)
        material = UV.material("pretty", image)
        plane = _mesh.image(image)
        mesh = make_mesh.bind(self.collection, self.name, plane)
        mesh.body.data.materials.append(material)
        self.mesh = mesh
        super().draw()
