from celestine.window.window import Window as master

from celestine.window.collection import Rectangle
from .package import data

import bpy

from . import package
from .container import Drop
from .mouse import Mouse


def context():
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            override = bpy.context.copy()
            override['area'] = area
            return override
    return None


class Window(master):
    def page(self, name, document):
        collection = data.collection.make(name)
        collection.hide()
        page = Drop(
            self.session,
            collection,
            name,
            self.turn,
            x_min=0,
            y_min=0,
            x_max=20,
            y_max=20,
            offset_x=0,
            offset_y=-2.5,
        )
        document(page)
        self.item_set(name, page)

        self.frame = page.collection

    def turn(self, name):
        """"""
        page = self.item_get(name)

        self.frame.hide()
        self.frame = page.collection
        self.frame.show()

        bpy.context.scene.celestine.page = page.tag

    def __enter__(self):
        super().__enter__()
        for camera in bpy.data.cameras:
            data.camera.remove(camera)
        for collection in bpy.data.collections:
            data.collection.remove(collection)
        for curve in bpy.data.curves:
            data.curve.remove(curve)
        for image in bpy.data.images:
            data.image.remove(image)
        for light in bpy.data.lights:
            data.light.remove(light)
        for material in bpy.data.materials:
            data.material.remove(material)
        for mesh in bpy.data.meshes:
            data.mesh.remove(mesh)
        for texture in bpy.data.textures:
            data.texture.remove(texture)

        collection = data.collection.make("window")

        camera = data.camera.make(collection, "camera")
        camera.location = (+16.0, -08.5, +60.0)
        camera.ortho_scale = +35.0
        camera.type = 'ORTHO'

        light = data.light.sun.make(collection, "light")
        light.location = (0, 0, 1)

        self.mouse = Mouse()

        override = context()
        bpy.ops.view3d.toggle_shading(override, type='RENDERED')
        bpy.ops.view3d.view_camera(override)

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)
        return False

    def __init__(self, session, **kwargs):
        super().__init__(session, **kwargs)
        self.frame = None
        self.width = 20
        self.height = 10
        self.mouse = None
