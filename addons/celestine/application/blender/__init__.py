# <pep8-80 compliant>
"""Package blender."""
from celestine.application.blender import data
from celestine.application.blender import preferences


bl_info = {
    "name": "My Blender Plugin",
    "description": "Blnder stuff can do stuff wow cool.",
    "author": "Mem Dixy",
    "version": (0, 0, 4),
    "blender": (2, 91, 0),
    "location": "View 3D > Sidebar > Viewer",
    "warning": "Does not work. Work in progress. Not ready for publication.",
    "wiki_url": "https://mem-dixy.ch/",
    "tracker_url": "https://github.com/Mem-Dixy/Blender-Booru-Builder",
    "support": "COMMUNITY",
    "category": "3D View",
}


def register():
    """
    This is a function which only runs when enabling the add-on, this means the
    module can be loaded without activating the add-on.
    """
    data.register()
    preferences.register()


def unregister():
    """
    This is a function to unload anything setup by register, this is called
    when the add-on is disabled.
    """
    preferences.unregister()
    data.unregister()


def argument(argument):
    """Build up the argument."""
    verify = argument.subparser.add_parser(
        "verify",
        help="you are a fish",
    )

    return argument


def attribute():
    """Build up the attribute file."""
    return ()


def default():
    """Build up the default file."""
    return ()


def image_format():
    return [
        ".bmp",
        ".sgi",
        ".rgb",
        ".bw",
        ".png",
        ".jpg",
        ".jpeg",
        ".jp2",
        ".j2c",
        ".tga",
        ".cin",
        ".dpx",
        ".exr",
        ".hdr",
        ".tif",
        ".tiff",
        ".webp",
    ]
