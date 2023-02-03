from .package import preferences
from .package import UV
from .package import mesh
from .package import data

import bpy  # pylint: disable=import-error
import bpy

from .window import Window


def image_format():
    return [
        ".bmp",
        ".sgi",
        ".rgb",
        ".bw",
        ".png",
        ".jpg",
        ".jpeg",
        ".jp2",
        ".j2c",
        ".tga",
        ".cin",
        ".dpx",
        ".exr",
        ".hdr",
        ".tif",
        ".tiff",
        ".webp",
    ]


def window(session):
    return Window(session)


# <pep8-80 compliant>

def find_object(name):
    return next(obj for obj in bpy.data.objects if obj.name == name)


def find_collection(name):
    for collection in bpy.data.collections:
        if collection.name == name:
            return collection
    return None


def find_in_collection(collection, name):
    for item in collection.all_objects:
        if item.name == name:
            return item
    return None


class celestine_click(bpy.types.Operator):
    bl_label = "Mouse Click"
    bl_idname = "celestine.click"

    def execute(self, context):
        print("click")
        mouse = find_object("mouse")
        location = mouse.location
        x = round(location.x / 2.5) * 2.5
        y = round(location.y / 2.5) * 2.5
        z = 1
        mouse.location = (x, y, z)

        page = bpy.context.scene.celestine.page
        collection = find_collection(page)

        for item in collection.all_objects:
            print(item.location)

        print("done")
        return {'FINISHED'}


class celestine_main(bpy.types.Panel):
    bl_category = "Celestine"
    bl_context = ""
    bl_idname = "CELESTINE_PT_main"
    bl_label = "Main Panel"
    bl_options = {"HEADER_LAYOUT_EXPAND"}
    bl_order = 0
    bl_owner_id = ""
    bl_parent_id = ""
    bl_region_type = "UI"
    bl_space_type = "VIEW_3D"
    bl_translation_context = "*"
    bl_ui_units_x = 0

    def draw(self, _):
        content = preferences.content()
        if content.ready:
            self.layout.operator("celestine.start")
            self.layout.operator("celestine.click")
        else:
            self.layout.operator("celestine.finish")


class celestine_start(bpy.types.Operator):

    bl_description = "whati ti do"

    bl_label = "Startup"
    bl_idname = "celestine.start"

    def execute(self, _):
        print("start")
        car = bpy.context.preferences.addons["celestine"].preferences
        print(car)
        print(car.ready)
        data.start()
        preferences.start()
        print(car.ready)
        car.ready = True
        print(car.ready)
        print("dane")
        return {'FINISHED'}


class celestine_finish(bpy.types.Operator):
    bl_label = "Shutdown"
    bl_idname = "celestine.finish"

    def execute(self, _):
        print("finish")
        preferences.finish()
        data.finish()
        return {'FINISHED'}


def register():
    preferences.register()
    bpy.utils.register_class(celestine_start)
    bpy.utils.register_class(celestine_finish)
    bpy.utils.register_class(celestine_click)
    bpy.utils.register_class(celestine_main)


def unregister():
    bpy.utils.unregister_class(celestine_main)
    bpy.utils.unregister_class(celestine_click)
    bpy.utils.unregister_class(celestine_finish)
    bpy.utils.unregister_class(celestine_start)
    preferences.unregister()
