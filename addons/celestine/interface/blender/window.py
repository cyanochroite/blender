from celestine.window.window import Window as master

from celestine.window.collection import Rectangle
from .package import data

import bpy

from . import package
from .page import Page
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
        rectangle = Rectangle(0, 0, 20, 10, 0, 0)
        page = Page(self, rectangle, name)
        document(page)
        self.item_set(name, page)

        self.frame = page.frame

    def turn(self, page):
        self.frame.hide()
        self.frame = self.item_get(page).frame
        self.frame.show()

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

        camera = data.camera.make("camera")
        camera.location = (+16.0, -08.5, +60.0)
        camera.ortho_scale = +35.0
        camera.type = 'ORTHO'

        light = data.light.sun.make("light")
        light.location = (0, 0, 1)

        collection = data.collection.make("window")
        collection.link(camera)
        collection.link(light)

        self.mouse = Mouse(Rectangle())

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
