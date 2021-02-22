import bpy


def area_light(name):
    return light(name, 'AREA')


def blend_texture(name):
    return texture(name, 'BLEND')


def camera(name):
    return object(bpy.data.cameras, name)


def clouds_texture(name):
    return texture(name, 'CLOUDS')


def distorted_noise_texture(name):
    return texture(name, 'DISTORTED_NOISE')


def image(name):
    # width
    return bpy.data.images.new(name, 64, 64)


def image_load(filepath, check_existing=False):
    return bpy.data.images.load(filepath, check_existing=check_existing)


def image_texture(name):
    return texture(name, 'IMAGE')


def light(name, type):
    return object(bpy.data.lights, name, type)


def link(object):
    bpy.context.scene.collection.objects.link(object)


def magic_texture(name):
    return texture(name, 'MAGIC')


def marble_texture(name):
    return texture(name, 'MARBLE')


def material(name):
    return object_data(bpy.data.materials, name)


def musgrave_texture(name):
    return texture(name, 'MUSGRAVE')


def noise_texture(name):
    return texture(name, 'NOISE')


def none_texture(name):
    return texture(name, 'NONE')


def mesh(name):
    return object(bpy.data.meshes, name)


def object(data, name, type=None):
    item = object_data(data, name, type)
    object = object_data(bpy.data.objects, name, item)
    link(object)
    return object


def object_data(data, name, type=None):
    if type:
        return data.new(name, type)
    return data.new(name)


def point_light(name):
    return light(name, 'POINT')


def spot_light(name):
    return light(name, 'SPOT')


def stucci_texture(name):
    return texture(name, 'STUCCI')


def sun_light(name):
    return light(name, 'SUN')


def texture(name, type):
    return object_data(bpy.data.textures, name, type)


def voronoi_texture(name):
    return texture(name, 'VORONOI')


def wood_texture(name):
    return texture(name, 'WOOD')
