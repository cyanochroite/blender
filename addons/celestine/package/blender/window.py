from celestine.package.master.window import Window as master

from celestine.package.master.collection import Rectangle

from . import package
from .page import Page


class Window(master):
    def page(self, document):
        index = len(self.item)
        self.item_set(index, document)
        rectangle = Rectangle(0, 0, 640, 480, 0, 0)
        page = Page(self, rectangle)
        self.frame = page
        return page

    def turn(self, page):
        rectangle = Rectangle(0, 0, 640, 480, 0, 0)
        page2 = Page(self, rectangle)
        self.frame = page2
        self.item_get(page)(page2)

    def __enter__(self):
        super().__enter__()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)
        return False

    def __init__(self, session, **kwargs):
        super().__init__(session, **kwargs)
        self.frame = None
        self.width = 640
        self.height = 480
