# <pep8-80 compliant>
from . import new


def camera(name):
    return new.object(name, new.camera(name))


class image():  # incomplete
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



def mesh(name, mesh=None):
    if not mesh:
        mesh = new.mesh(name)
    return new.object(name, mesh)
