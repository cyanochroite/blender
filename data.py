import bpy


class all():
    data = None

    @classmethod
    def new(cls, name, type=None):
        if type:
            return cls.data.new(name, type)
        return cls.data.new(name)

    @classmethod
    def remove(cls, item):
        cls.data.remove(
            item,
            do_unlink=True,
            do_id_user=True,
            do_ui_user=True
        )

    @classmethod
    def unregister(cls):
        cls.data = None


class camera(all):
    @classmethod
    def register(cls):
        cls.data = bpy.data.cameras


class image(all):  # incomplete
    @classmethod
    def register(cls):
        cls.data = bpy.data.images

    @staticmethod
    def new(name, width, height):
        return bpy.data.images.new(name, width, height)

    @staticmethod
    def load(name, width, height):
        return bpy.data.images.load(filepath, check_existing)
#    return bpy.data.images.load(filepath, check_existing=check_existing)


class light(all):
    @classmethod
    def register(cls):
        cls.data = bpy.data.lights

    @classmethod
    def area(cls, name):
        return cls.new(name, 'AREA')

    @classmethod
    def point(cls, name):
        return cls.new(name, 'POINT')

    @classmethod
    def spot(cls, name):
        return cls.new(name, 'SPOT')

    @classmethod
    def sun(cls, name):
        return cls.new(name, 'SUN')


class material(all):
    @classmethod
    def register(cls):
        cls.data = bpy.data.materials


class mesh(all):
    @classmethod
    def register(cls):
        cls.data = bpy.data.meshes

    def mesh(name, vertices, edges, faces):
        mesh = data(bpy.data.meshes, name)
        mesh.from_pydata(vertices, edges, faces)
        return empty_object(name, mesh)


class object(all):
    @classmethod
    def register(cls):
        cls.data = bpy.data.objects


class texture(all):
    @classmethod
    def register(cls):
        cls.data = bpy.data.textures

    @classmethod
    def blend(cls, name):
        return cls.new(name, 'BLEND')

    @classmethod
    def clouds(cls, name):
        return cls.new(name, 'CLOUDS')

    @classmethod
    def distorted_noise(cls, name):
        return cls.new(name, 'DISTORTED_NOISE')

    @classmethod
    def image(cls, name):
        return cls.new(name, 'IMAGE')

    @classmethod
    def magic(cls, name):
        return cls.new(name, 'MAGIC')

    @classmethod
    def marble(cls, name):
        return cls.new(name, 'MARBLE')

    @classmethod
    def musgrave(cls, name):
        return cls.new(name, 'MUSGRAVE')

    @classmethod
    def noise(cls, name):
        return cls.new(name, 'NOISE')

    @classmethod
    def none(cls, name):
        return cls.new(name, 'NONE')

    @classmethod
    def stucci(cls, name):
        return cls.new(name, 'STUCCI')

    @classmethod
    def voronoi(cls, name):
        return cls.new(name, 'VORONOI')

    @classmethod
    def wood(cls, name):
        return cls.new(name, 'WOOD')


def register():
    camera.register()
    image.register()
    material.register()
    mesh.register()
    object.register()
    texture.register()


def unregister():
    camera.unregister()
    image.unregister()
    material.unregister()
    mesh.unregister()
    object.unregister()
    texture.unregister()




