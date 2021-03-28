import bpy


class all():
    data = None

    @classmethod
    def new(cls, name, type=None):
        if type:
            cls.data.new(name, type)
        else:
            cls.data.new(name)

    @classmethod
    def remove(cls, item):
        cls.data.remove(
            item,
            do_unlink=True,
            do_id_user=True,
            do_ui_user=True
        )


class camera(all):
    data = bpy.data.cameras


class image():
    @staticmethod
    def new(name, width, height):
        return bpy.data.images.new(name, width, height)

    @staticmethod
    def load(name, width, height):
        return bpy.data.images.load(filepath, check_existing)
#    return bpy.data.images.load(filepath, check_existing=check_existing)


class light():
    data = bpy.data.lights


class material():
    data = bpy.data.materials


class mesh():
    data = bpy.data.meshes


class object():
    data = bpy.data.objects


class texture():
    data = bpy.data.textures


class mesh():  # invalid data
    def mesh(name, vertices, edges, faces):
        mesh = data(bpy.data.meshes, name)
        mesh.from_pydata(vertices, edges, faces)
        return empty_object(name, mesh)
