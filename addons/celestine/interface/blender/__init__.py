from .package import preferences
from .package import UV
from .package import mesh
from .package import data

import bpy  # pylint: disable=import-error
import bpy

from .window import Window

import celestine


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
        x_dot = round(location.x / 2.5) * 2.5
        y_dot = round(location.y / 2.5) * 2.5
        z_dot = 1
        mouse.location = (x_dot, y_dot, z_dot)

        page = bpy.context.scene.celestine.page
        collection = find_collection(page)

        task = "poke"
        celestine.blender(task, x_dot, y_dot)

        for item in collection.all_objects:
            print(item.location)

        print("done")
        return {'FINISHED'}


class celestine_main(bpy.types.Panel):
    bl_category = "celestine"
    bl_context = "object"
    bl_description = "Celestine Tab"
    bl_idname = "OBJECT_PT_celestine"
    bl_label = "Célestine"
    bl_options = {"HEADER_LAYOUT_EXPAND"}
    bl_order = 0
    bl_owner_id = ""
    bl_parent_id = ""
    bl_region_type = "WINDOW"
    bl_space_type = "PROPERTIES"
    bl_translation_context = "*"
    bl_ui_units_x = 0

    text = ""
    use_pin = False

    def draw(self, context):
        self.layout.operator(SimpleOperator.bl_idname)
        self.layout.label(text=str(SimpleOperator.run))

        content = preferences.content()
        if content.ready:
            self.layout.operator("celestine.start")
            self.layout.operator("celestine.click")
        else:
            self.layout.operator("celestine.finish")

    def draw_header(self, context):
        pass

    def draw_header_preset(self, context):
        pass


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


class HelloWorldPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Hello World Panel"
    bl_idname = "OBJECT_PT_hello"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout

        layout.operator(SimpleOperator.bl_idname)
        layout.label(text=str(SimpleOperator.run))


class SimpleOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_operator"
    bl_label = "Simple Object Operator"

    run = 0

    def execute(self, context):
        self.__class__.run += 1
        self.report({'INFO'}, str(self.__class__.run))
        return {'FINISHED'}


def register():
    bpy.utils.register_class(HelloWorldPanel)
    bpy.utils.register_class(SimpleOperator)

    preferences.register()
    bpy.utils.register_class(celestine_start)
    bpy.utils.register_class(celestine_finish)
    bpy.utils.register_class(celestine_click)
    bpy.utils.register_class(celestine_main)


def unregister():
    bpy.utils.unregister_class(SimpleOperator)
    bpy.utils.unregister_class(HelloWorldPanel)

    bpy.utils.unregister_class(celestine_main)
    bpy.utils.unregister_class(celestine_click)
    bpy.utils.unregister_class(celestine_finish)
    bpy.utils.unregister_class(celestine_start)
    preferences.unregister()
