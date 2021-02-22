# <pep8 compliant>

import os
import bpy


def _setattr(self, name, val):
    print(self, name, val)
    setattr(self, name, val)


def default_global_dict():
    from os.path import expanduser
    home = expanduser("~")
    return home + os.sep + 'blenderkit_data'


def save_prefs(self, context):
    # first check context, so we don't do this on registration or blender startup
    if not bpy.app.background:  # (hasattr kills blender)
        user_preferences = bpy.context.preferences.addons['booru'].preferences
        # we test the api key for length, so not a random accidentally typed sequence gets saved.
        lk = len(user_preferences.api_key)
        if 0 < lk < 25:
            # reset the api key in case the user writes some nonsense, e.g. a search string instead of the Key
            user_preferences.api_key = ''
            props = get_search_props()
            props.report = 'Login failed. Please paste a correct API Key.'

        prefs = {
            'API_key': user_preferences.api_key,
            'API_key_refresh': user_preferences.api_key_refresh,
            'global_dir': user_preferences.global_dir,
        }
        try:
            fpath = paths.BLENDERKIT_SETTINGS_FILENAME
            if not os.path.exists(paths._presets):
                os.makedirs(paths._presets)
            f = open(fpath, 'w')
            with open(fpath, 'w') as s:
                json.dump(prefs, s)
        except Exception as e:
            print(e)


class BooruAddonPreferences(bpy.types.AddonPreferences):
    bl_idname = "booru"
    bl_option = {'REGISTER'}

    image_root: bpy.props.StringProperty(
        name="Root Image Folder",
        description="Location of your image collection.",
        subtype='DIR_PATH',
        default=default_global_dict,
        update=save_prefs
    )

    def draw(self, context):
        layout = self.layout
        layout.label(text="WARNING: preferences are lost when add-on is disabled, be sure to use \"Save Persistent\" "
                          "if you want to keep your settings!")
        layout.prop(self, "image_root")


class ExampleAddonPreferences(bpy.types.AddonPreferences):
    # this must match the add-on name, use '__package__'
    # when defining this in a submodule of a python package.
    bl_idname = __name__

    filepath: bpy.props.StringProperty(
        name="Example File Path",
        subtype='FILE_PATH',
    )
    number: bpy.props.IntProperty(
        name="Example Number",
        default=4,
    )
    boolean: bpy.props.BoolProperty(
        name="Example Boolean",
        default=False,
    )

    def draw(self, context):
        layout = self.layout
        layout.label(text="This is a preferences view for our add-on")
        layout.prop(self, "filepath")
        layout.prop(self, "number")
        layout.prop(self, "boolean")


class OBJECT_OT_addon_prefs_example(bpy.types.Operator):
    """Display example preferences"""
    bl_idname = "object.addon_prefs_example"
    bl_label = "Add-on Preferences Example"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        preferences = context.preferences
        addon_prefs = preferences.addons[__name__].preferences

        info = ("Path: %s, Number: %d, Boolean %r" %
                (addon_prefs.filepath, addon_prefs.number, addon_prefs.boolean))

        self.report({'INFO'}, info)
        print(info)
        print(__name__)

        return {'FINISHED'}
