import bpy


def remove(type, data):
    if not type:
        return
    if not data:
        return
    type.remove(
        data,
        do_unlink=True,
        do_id_user=True,
        do_ui_user=True
    )


def camera(camera):
    remove(bpy.data.cameras, camera)


def image(image):
    remove(bpy.data.images, image)


def light(light):
    remove(bpy.data.lights, light)


def material(material):
    remove(bpy.data.materials, material)


def mesh(mesh):
    remove(bpy.data.meshes, mesh)


def object(object):
    remove(bpy.data.objects, object)


def texture(texture):
    remove(bpy.data.textures, texture)

