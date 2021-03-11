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


# new data
def camera(name):
    return data.camera(name)


class data():
    @staticmethod
    def camera(name):
        return bpy.data.cameras.new(name)

    @staticmethod
    def light(name, type):
        return bpy.data.lights.new(name, type)

    @staticmethod
    def material(name):
        return bpy.data.materials.new(name)

    @staticmethod
    def mesh(name):
        return bpy.data.meshes.new(name)

    @staticmethod
    def texture(name, type):
        return bpy.data.textures.new(name, type)


class light():
    @staticmethod
    def area(name):
        return data.light(name, 'AREA')

    @staticmethod
    def point(name):
        return data.light(name, 'POINT')

    @staticmethod
    def spot(name):
        return data.light(name, 'SPOT')

    @staticmethod
    def sun(name):
        return data.light(name, 'SUN')


def material(name):
    return data.material(name)


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
        return data.texture(name, 'BLEND')

    @staticmethod
    def clouds(name):
        return data.texture(name, 'CLOUDS')

    @staticmethod
    def distorted_noise(name):
        return data.texture(name, 'DISTORTED_NOISE')

    @staticmethod
    def image(name):
        return data.texture(name, 'IMAGE')

    @staticmethod
    def magic(name):
        return data.texture(name, 'MAGIC')

    @staticmethod
    def marble(name):
        return data.texture(name, 'MARBLE')

    @staticmethod
    def musgrave(name):
        return data.texture(name, 'MUSGRAVE')

    def noise(name):
        return data.texture(name, 'NOISE')

    @staticmethod
    def none(name):
        return data.texture(name, 'NONE')

    @staticmethod
    def stucci(name):
        return data.texture(name, 'STUCCI')

    @staticmethod
    def voronoi(name):
        return data.texture(name, 'VORONOI')

    @staticmethod
    def wood(name):
        return data.texture(name, 'WOOD')


# new spawn
def camera(name):
    return data.camera(name)


class light():
    @staticmethod
    def area(name):
        return data.light(name, 'AREA')

    @staticmethod
    def point(name):
        return data.light(name, 'POINT')

    @staticmethod
    def spot(name):
        return data.light(name, 'SPOT')

    @staticmethod
    def sun(name):
        return data.light(name, 'SUN')


class mesh():  # invalid data
    @staticmethod
    def data(name):
        return object(bpy.data.meshes, name)

    def mesh(name, vertices, edges, faces):
        mesh = data(bpy.data.meshes, name)
        mesh.from_pydata(vertices, edges, faces)
        return empty_object(name, mesh)

