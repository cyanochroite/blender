# <pep8-80 compliant>
import bpy


class _imaginary():
    type_ = ""
    data = None

    @classmethod
    def new(cls, name):
        if cls.type_:
            return cls.data.new(name, cls.type_)
        return cls.data.new(name)

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
        soul = item or cls.new(name)
        body = cls.object_(name, soul)
        return _real(body, soul)

    @classmethod
    def object_(cls, name, object_data):
        object_ = bpy.data.objects.new(name, object_data)
        bpy.context.scene.collection.objects.link(object_)
        return object_

    def __init__(self, body, soul):
        self.__dict__["body"] = body
        self.__dict__["soul"] = soul

    def __getattr__(self, name):
        match name:
            case "location":
                getattr(self.body, name)
            case "parent":
                getattr(self.body, name)
            case "rotation_euler":
                getattr(self.body, name)
            case "scale":
                getattr(self.body, name)
            case _:
                getattr(self.soul, name)

    def __setattr__(self, name, value):
        match name:
            case "location":
                setattr(self.body, name, value)
            case "parent":
                setattr(self.body, name, value.body)
            case "rotation_euler":
                setattr(self.body, name, value)
            case "scale":
                setattr(self.body, name, value)
            case _:
                setattr(self.soul, name, value)


class _text(_real):
    @classmethod
    def new(cls, name, text):
        soul = super().new(name)
        soul.body = text
        return soul

    @classmethod
    def make(cls, name, text, item=None):
        soul = item or cls.new(name, text)
        body = cls.object_(name, soul)
        return _real(body, soul)


