# <pep8-80 compliant>
"""Light data-block for lighting a scene."""
import bpy


class all():
    @staticmethod
    def new(data, *args):
        print("eat")
        return data.new(*args)

    @staticmethod
    def object_(name, object_data):
        object = bpy.data.objects.new(name, object_data)
        bpy.context.scene.collection.objects.link(object)
        return object


class lighter(all):
    @classmethod
    def new(cls, *args):
        print("you")
        return super().new(bpy.data.lights, *args)

    @classmethod
    def make(cls, name):
        print("hi")
        return cls.object_(name, cls.new(name))


class sun(lighter):
    @classmethod
    def new(cls, name):
        print("cow")
        return super().new(name, 'SUN')
