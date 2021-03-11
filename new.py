import bpy


def image(name):
    # width
    return bpy.data.images.new(name, 64, 64)


def image_load(filepath, check_existing=False):
    return bpy.data.images.load(filepath, check_existing=check_existing)


def link(object):
    bpy.context.scene.collection.objects.link(object)


def object(data, name, type=None):
    # got to rethink the idea of not returning the sub item generated
    # maybe make a seperate spawning class for scenes
    item = object_data(data, name, type)
    object = empty_object(name, item)
    link(object)
    return object


def empty_object(name, item):
    object = object_data(bpy.data.objects, name, item)
    link(object)
    return object


def object_data(data, name, type=None):
    if type:
        return data.new(name, type)
    return data.new(name)


###
def camera(name):
    return object(bpy.data.cameras, name)


def data(data, name, type=None):
    if type:
        return data.new(name, type)
    return data.new(name)


class light():  # invalid data
    @staticmethod
    def area(name):
        return light.data(name, 'AREA')

    @staticmethod
    def data(name, type):
        return object(bpy.data.lights, name, type)

    @staticmethod
    def point(name):
        return light.data(name, 'POINT')

    @staticmethod
    def spot(name):
        return light.data(name, 'SPOT')

    @staticmethod
    def sun(name):
        return light.data(name, 'SUN')


def material(name):
    return data(bpy.data.materials, name)


class mesh():  # invalid data
    @staticmethod
    def data(name):
        return object(bpy.data.meshes, name)

    def mesh(name, vertices, edges, faces):
        mesh = data(bpy.data.meshes, name)
        mesh.from_pydata(vertices, edges, faces)
        return empty_object(name, mesh)


class texture():
    @staticmethod
    def blend(name):
        return texture.data(name, 'BLEND')

    @staticmethod
    def clouds(name):
        return texture.data(name, 'CLOUDS')

    @staticmethod
    def data(name, type):
        return data(bpy.data.textures, name, type)

    @staticmethod
    def distorted_noise(name):
        return texture.data(name, 'DISTORTED_NOISE')

    @staticmethod
    def image(name):
        return texture.data(name, 'IMAGE')

    @staticmethod
    def magic(name):
        return texture.data(name, 'MAGIC')

    @staticmethod
    def marble(name):
        return texture.data(name, 'MARBLE')

    @staticmethod
    def musgrave(name):
        return texture.data(name, 'MUSGRAVE')

    def noise(name):
        return texture.data(name, 'NOISE')

    @staticmethod
    def none(name):
        return texture.data(name, 'NONE')

    @staticmethod
    def stucci(name):
        return texture.data(name, 'STUCCI')

    @staticmethod
    def voronoi(name):
        return texture.data(name, 'VORONOI')

    @staticmethod
    def wood(name):
        return texture.data(name, 'WOOD')
