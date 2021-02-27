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

    def _uv_offset(self, numerator, denominator):
        ratio = numerator / denominator
        unit = 1
        maximum = max(ratio, unit)
        normalization = maximum - unit
        half = 1 / 2
        halving = normalization * half
        return halving

    def _uv_image_offset(self, image):
        size = image.size
        x = size[0]
        y = size[1]
        y_to_x = self._uv_offset(y, x)
        x_to_y = self._uv_offset(x, y)
        offset = (y_to_x, x_to_y)
        return offset

    def _shader_image(self, nodes, image):
        # inputs
        # "Vector"
        # outputs
        # "Color"
        # "Alpha"
        node = nodes.new('ShaderNodeTexImage')
        node.image = image
        node.interpolation = 'Cubic'
        node.projection = 'FLAT'
        node.extension = 'CLIP'
        return node

    def _shader_diffuse(self, nodes):
        # inputs
        # "Color"
        # "Roughness"
        # "Normal"
        # outputs
        # "BSDF"
        node = nodes.new('ShaderNodeBsdfDiffuse')
        return node

    def _shader_output(self, nodes):
        # inputs
        # "Surface"
        # "Volume"
        # "Displacement"
        # outputs
        node = nodes.new('ShaderNodeOutputMaterial')
        node.target = 'ALL'
        return node

    def execute(self, context):
        preferences = bpy.context.preferences.addons[__name__].preferences
        path = preferences.fluffypath
        file = path + "test.jpg"
        object = self._new_object(context)
        image = new.image_load(file)
        material = new.material("pretty")
        material.use_nodes = True

        tree = material.node_tree
        nodes = tree.nodes
        nodes.clear()

        aa = self._shader_image(nodes, image)
        aa.location = (000, 000)

        bb = self._shader_diffuse(nodes)
        bb.location = (300, 000)

        cc = self._shader_output(nodes)
        cc.location = (500, 000)

        tree.links.new(aa.outputs["Color"], bb.inputs["Color"])
        tree.links.new(bb.outputs["BSDF"], cc.inputs["Surface"])

        # material
        object.data.materials.append(material)

        mesh = bmesh.new()
        mesh.from_mesh(object.data)
        mesh.faces.ensure_lookup_table()
        loops = mesh.faces[0].loops
        uv = mesh.loops.layers.uv.verify()
        (x, y) = self._uv_image_offset(image)
        loops[0][uv].uv = (0 - x, 0 - y)
        loops[1][uv].uv = (1 + x, 0 - y)
        loops[2][uv].uv = (1 + x, 1 + y)
        loops[3][uv].uv = (0 - x, 1 + y)
        mesh.to_mesh(object.data)
        mesh.free()

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

        addon_prefs = bpy.context.preferences.addons[__name__].preferences
        self.layout.prop(addon_prefs, "boolean")
        if addon_prefs.boolean:
            self.layout.label(text="checkbox is on")
        else:
            self.layout.label(text="checkbox is off")


class BooruAddonPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    fluffypath: bpy.props.StringProperty(
        name="Root Image Folder",
        description="Location of your image collection.",
        subtype='DIR_PATH'
    )

    filepath: bpy.props.StringProperty(
        name="Example File Path",
        description="Location of your image collection.",
        subtype='FILE_PATH',
    )

    number: bpy.props.IntProperty(
        name="Example Number",
        description="Location of your image collection.",
        default=4
    )

    boolean: bpy.props.BoolProperty(
        name="Example Boolean",
        description="Location of your image collection.",
        default=False
    )

    def draw(self, context):
        layout = self.layout
        layout.label(text="This is a preferences view for our add-on")
        layout.prop(self, "fluffypath")
        layout.prop(self, "filepath")
        layout.prop(self, "number")
        layout.prop(self, "boolean")


def register():
    bpy.utils.register_class(BOORU_PT_main)
    bpy.utils.register_class(BOORU_mesh_make)
    bpy.utils.register_class(BOORU_mesh_delete)
    bpy.utils.register_class(BOORU_clear_all)
    bpy.utils.register_class(BooruAddonPreferences)


def unregister():
    bpy.utils.unregister_class(BOORU_mesh_delete)
    bpy.utils.unregister_class(BOORU_mesh_make)
    bpy.utils.unregister_class(BOORU_clear_all)
    bpy.utils.unregister_class(BOORU_PT_main)
    bpy.utils.unregister_class(BooruAddonPreferences)
