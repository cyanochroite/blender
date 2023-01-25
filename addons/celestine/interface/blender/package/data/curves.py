""" bpy.types.Curves"""
from .spawn import _real


class _curves(_real):
    """Hair data-block for hair curves."""
    area = None
    point = None
    spot = None
    sun = None


class _font(_curves):
    """Vector font for Text objects."""
    type_ = "FONT"

    @classmethod
    def new(cls, name, text):
        item = super().new(name)
        item.body = text
        return item

    @classmethod
    def make(cls, name, text, item=None):
        fake = item or cls.new(name, text)
        real = cls.object_(name, fake)
        return _real(real, fake)


setattr(_curves, "font", _font)
