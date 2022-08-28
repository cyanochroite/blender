# <pep8-80 compliant>
"""Point – Omnidirectional point light source."""
import bpy


def object(name, object_data):
    object = bpy.data.objects.new(name, object_data)
    bpy.context.scene.collection.objects.link(object)
    return object


def all_remove(data, item):
    data.remove(
        item,
        do_unlink=True,
        do_id_user=True,
        do_ui_user=True
    )


def all_new(data, *args):
    return data.new(*args)


def light_new(*args):
    return all_new(bpy.data.lights, *args)


def new(name):
    return light_new(name, 'POINT')


def make(name):
    return object(name, new(name))
