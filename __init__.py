# <pep8-80 compliant>

bl_info = {
    "name": "Blender Booru Builder",
    "description": "Add, tag, and browse images on your computer.",
    "author": "Mem Dixy",
    "version": (0, 0, 1),
    "blender": (2, 91, 0),
    "location": "View 3D > Sidebar > Viewer",
    "warning": "Does not work. Work in progress. Not ready for publication.",
    "wiki_url": "https://mem-dixy.ch/",
    "tracker_url": "https://github.com/Mem-Dixy/Blender-Booru-Builder",
    "support": "COMMUNITY",
    "category": "3D View",
}

# 234567890123456789012345678901234567890123456789012345678901234567890123456789

# {'RUNNING_MODAL', 'CANCELLED', 'FINISHED', 'PASS_THROUGH'}
import bpy
import bmesh
from . import new
from . import remove
from . import preferences
from . import UV


class BOORU_mesh_make(bpy.types.Operator):
    bl_label = "Plane"
    bl_idname = "blenderbooru.mesh_make"

    def _new_object(self, context):
        bpy.ops.mesh.primitive_plane_add(
            enter_editmode=False,
            align='WORLD',
            location=(0, 0, 0),
            scale=(1, 1, 1)
        )
        object = bpy.data.objects[-1]
        return object

    def _bmesh_magic(self, object, image):
        mesh = bmesh.new()
        mesh.from_mesh(object.data)
        mesh.faces.ensure_lookup_table()
        UV.image_offset(image, mesh)
        mesh.to_mesh(object.data)
        mesh.free()

    def execute(self, context):
        ##
        print("start")
        from . import OS
        content = preferences.content()
        (path, file) = OS.walk_directory(content.root)
        images = []
        for (filenames) in file:
            (dirpath, name) = filenames
            ext = OS.file_extension(name)
            if ext in Image_Formats:
                merge = OS.join(dirpath, name)
                images.append(merge)
        for item in images:
            print("convert " + item)
        print("done")

        ##

        for file in images:
            object = self._new_object(context)
            image = new.image_load(file)
            material = UV.material("pretty", image)
            object.data.materials.append(material)
            self._bmesh_magic(object, image)

        # finish
        return {'FINISHED'}


class BOORU_mesh_delete(bpy.types.Operator):
    bl_label = "Delete Me Now"
    bl_idname = "blenderbooru.mesh_delete"

    def execute(self, context):
        # currently selected at the momnet
        object = bpy.context.object
        if object:
            remove.material(object.active_material)
        remove.object(object)
        return {'FINISHED'}


class BOORU_clear_all(bpy.types.Operator):
    bl_label = "Clear all data"
    bl_idname = "blenderbooru.clear_all"

    def execute(self, context):
        # this probably highly unoptimized.
        # try doing this backwarks
        for camera in bpy.data.cameras:
            remove.camera(camera)
        for light in bpy.data.lights:
            remove.light(light)
        for material in bpy.data.materials:
            remove.material(material)
        for mesh in bpy.data.meshes:
            remove.mesh(mesh)
        for image in bpy.data.images:
            remove.image(image)
        for texture in bpy.data.textures:
            remove.texture(texture)
        camera = new.camera("cool cat")
        camera.location = (0, 0, 10)
        light = new.sun_light("lili")
        light.location = (0, 0, 1)
        new.camera("b")
        new.mesh("e")
        #bpy_data.make(new.object, "f")
        new.point_light("g")
        new.spot_light("h")
        new.sun_light("i")
        new.area_light("a")
        return {'FINISHED'}


class BOORU_PT_main(bpy.types.Panel):
    bl_category = "Tab Name"
    bl_context = ""
    bl_idname = "BOORU_PT_main_panel2"
    bl_label = "Main Panel"
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 0
    bl_owner_id = ""
    bl_parent_id = ""
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_translation_context = "*"
    bl_ui_units_x = 0

    bl_label = "Select a TAG"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    #bl_context = 'object'
    # bl_context = "OBJECT"
    bl_options = {'DEFAULT_CLOSED'}
    ###
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "bbb"
    bl_label = "Landmarks yay"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        self.layout.label(text="Hello World")
        self.layout.operator("blenderbooru.mesh_make")
        self.layout.operator("blenderbooru.mesh_delete")
        self.layout.operator("blenderbooru.clear_all")

        content = preferences.content()
        self.layout.prop(content, "boolean")
        if content.boolean:
            self.layout.label(text="checkbox is on")
        else:
            self.layout.label(text="checkbox is off")


def register():
    bpy.utils.register_class(BOORU_PT_main)
    bpy.utils.register_class(BOORU_mesh_make)
    bpy.utils.register_class(BOORU_mesh_delete)
    bpy.utils.register_class(BOORU_clear_all)
    preferences.register()


def unregister():
    bpy.utils.unregister_class(BOORU_mesh_delete)
    bpy.utils.unregister_class(BOORU_mesh_make)
    bpy.utils.unregister_class(BOORU_clear_all)
    bpy.utils.unregister_class(BOORU_PT_main)
    preferences.unregister()


Image_Formats = [
    ".bmp",
    ".sgi",
    ".rgb",
    ".bw",
    ".png",
    ".jpg",
    "jpeg",
    ".jp2",
    ".jp2",
    ".j2c",
    ".tga",
    ".cin",
    ".dpx",
    ".exr",
    ".hdr",
    ".tif",
    ".tiff"
]
