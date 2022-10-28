# <pep8-80 compliant>
# <pep8-80 compliant>
import bpy


class _imaginary():
    type_ = ""
    data = None

    @classmethod
    def new(cls, *args):
        if cls.type_:
            return cls.data.new(cls.type_, *args)
        return cls.data.new(*args)

    @classmethod
    def remove(cls, item):
        cls.data.remove(
            item,
            do_unlink=True,
            do_id_user=True,
            do_ui_user=True
        )


class _real(_imaginary):
    @classmethod
    def make(cls, name, item=None):
        return cls.object_(name, item or cls.new(name))

    @classmethod
    def object_(cls, name, object_data):
        object_ = bpy.data.objects.new(name, object_data)
        bpy.context.scene.collection.objects.link(object_)
        return object_


