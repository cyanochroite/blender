""" bpy.types.Collection"""
import bpy

from .spawn import _imaginary


class _collection(_imaginary):
    """Collection of Object data-blocks."""

    @classmethod
    def make(cls, name, item=None):
        soul = item or cls.new(name)
        bpy.context.scene.collection.children.link(soul)
        return cls(soul)

    def __init__(self, soul):
        self.soul = soul
        self.soul.hide_select = True

    def hide(self):
        self.soul.hide_render = True
        self.soul.hide_viewport = True

    def show(self):
        self.soul.hide_render = False
        self.soul.hide_viewport = False

    def link(self, item):
        self.soul.objects.link(item.body)

