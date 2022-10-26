from celestine.package.master.window import Window as master

from . import package
from .page import Page


# <pep8-80 compliant>
import bpy  # pylint: disable=import-error

from celestine.application.blender import data
from celestine.application.blender import mesh
from celestine.application.blender import UV

from booru import preferences

import sys
import celestine

ready = False


class BOORU_mesh_make(bpy.types.Operator):
    bl_label = "Plane"
    bl_idname = "celestine.mesh_make"

    def __init__(self):
        self.spot = 0

    def _new_object(self, context, image):
        mush = mesh.image(image)
        box = data.mesh.make("image", mush)
        box.location = (self.spot, 0, 0)
        self.spot += 2.5
        return box

    def execute(self, context):
        print("start")
        self.spot = 0
        from .plugin import OS
        content = preferences.content()
        (path, file) = OS.walk_directory(content.root)
        images = []
        for (filenames) in file:
            (dirpath, name) = filenames
            ext = OS.file_extension(name).lower()
            if ext in Image_Formats:
                merge = OS.join(dirpath, name)
                images.append(merge)
        for file in images:
            print("convert " + file)
            image = data.image.load(file)
            material = UV.material("pretty", image)
            object = self._new_object(context, image)
            object.data.materials.append(material)
        print("done")
        return {'FINISHED'}


class BOORU_main(bpy.types.Panel):
    bl_category = "Tab Name"
    bl_context = ""
    bl_idname = "BOORU_PT_main_panel2"
    bl_label = "Main Panel"
    bl_options = {'DEFAULT_OPEN'}
    bl_order = 0
    bl_owner_id = ""
    bl_parent_id = ""
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_translation_context = "*"
    bl_ui_units_x = 0

    bl_label = "Select a TAG"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    #bl_context = 'object'
    # bl_context = "OBJECT"
    bl_options = {'DEFAULT_CLOSED'}
    ###
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "ccc"
    bl_label = "Landmarks yay"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        global ready
        if not ready:
            self.layout.operator("celestine.register")
        else:
            self.layout.operator("celestine.mesh_make")


class BOORU_register(bpy.types.Operator):
    bl_label = "Startup"
    bl_idname = "celestine.register"

    def execute(self, context):
        global ready
        data.register()
        ready = True
        argv = ["blender", "main"]
        celestine.main(sys.path[0], argv, False)
        return {'FINISHED'}


class BOORU_unregister(bpy.types.Operator):
    bl_label = "Shutdown"
    bl_idname = "celestine.unregister"

    def execute(self, context):
        global ready
        data.unregister()
        ready = False
        return {'FINISHED'}


def register():
    bpy.utils.register_class(BOORU_main)
    bpy.utils.register_class(BOORU_mesh_make)
    #
    bpy.utils.register_class(BOORU_unregister)
    bpy.utils.register_class(BOORU_register)


def unregister():
    bpy.utils.unregister_class(BOORU_mesh_make)
    bpy.utils.unregister_class(BOORU_main)
    #
    bpy.utils.unregister_class(BOORU_register)
    bpy.utils.unregister_class(BOORU_unregister)


class Window(master):
    def page(self, document):
        index = len(self.item)
        self.item_set(index, document)
        page = Page(self)
        self.frame = page
        return page

    def turn(self, page):
        self.frame.frame.clear()
        self.frame = Page(self)
        self.item_get(page)(self.frame)
        self.stdscr.noutrefresh()
        self.background.noutrefresh()
        self.frame.frame.noutrefresh()
        package.doupdate()

    def __enter__(self):
        super().__enter__()
        self.stdscr = package.initscr()
        package.noecho()
        package.cbreak()
        self.stdscr.keypad(1)
        package.start_color()

        # start

        self.background = package.window(0, 0, self.width, self.height)
        self.background.box()

        header1 = package.subwindow(self.background, 0, 0, self.width, 1)
        header1.addstr(self.session.language.APPLICATION_TITLE)

        header2 = package.subwindow(
            self.background, 0, self.height - 1, self.width, 1)
        header2.addstr(self.session.language.CURSES_EXIT)

        self.stdscr.noutrefresh()
        self.background.noutrefresh()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)
        while True:
            key = self.stdscr.getch()
            match key:
                case 258 | 259 | 260 | 261 as key:
                    match key:
                        case package.KEY_UP:
                            self.cord_y -= 1
                        case package.KEY_DOWN:
                            self.cord_y += 1
                        case package.KEY_LEFT:
                            self.cord_x -= 1
                        case package.KEY_RIGHT:
                            self.cord_x += 1

                    self.cord_x %= self.width
                    self.cord_y %= self.height
                    self.stdscr.move(self.cord_y, self.cord_x)
                case package.KEY_Q:
                    break
                case package.KEY_SPACE as key:
                    for key, thing in self.frame.item.items():
                        if thing.select(self.cord_x - 1, self.cord_y - 1):
                            if thing.type == "button":
                                self.turn(thing.action)

        self.stdscr.keypad(0)
        package.echo()
        package.nocbreak()
        package.endwin()
        return False

    def __init__(self, session, **kwargs):
        super().__init__(session, **kwargs)
        self.cord_x = 0
        self.cord_y = 0
        self.height = 24
        self.width = 80

        self.window = 0
        self.frame = None
