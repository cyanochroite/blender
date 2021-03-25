import bpy
from . import new

# new spawn


def camera(name):
    return object(name, new.camera(name))


class light():
    @staticmethod
    def area(name):
        return object(name, new.light.area(name))

    @staticmethod
    def point(name):
        return object(name, new.light.point(name))

    @staticmethod
    def spot(name):
        return object(name, new.light.spot(name))

    @staticmethod
    def sun(name):
        return object(name, new.light.sun(name))


class mesh():  # invalid data
    def mesh(name, vertices, edges, faces):
        mesh = data(bpy.data.meshes, name)
        mesh.from_pydata(vertices, edges, faces)
        return empty_object(name, mesh)


def object(name, object_data):
    object = bpy.data.objects.new(name, object_data)
    bpy.context.scene.collection.objects.link(object)
    return object

