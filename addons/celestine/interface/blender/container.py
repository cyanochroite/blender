""""""

from celestine.window.collection import Rectangle

from .button import Button
from .image import Image
from .label import Label


class Container(Rectangle):
    """"""

    def make(self, tag, offset_x, offset_y, **kwargs):
        """Make a new Container."""
        (x_min, y_min, x_max, y_max) = self.get_next()
        return Container(
            self.page,
            tag,
            x_min=x_min,
            y_min=y_min,
            x_max=x_max,
            y_max=y_max,
            offset_x=offset_x,
            offset_y=offset_y,
            **kwargs,
        )

    def drop(self, tag, **kwargs):
        """Elements go down. Like a <div> tag."""
        return self.make(tag, 0, -2.5, **kwargs)

    def grid(self, tag, width, **kwargs):
        """Elements go in a grid. Like the <table> tag."""
        (x_min, y_min, x_max, y_max) = self.get_next()
        return Grid(
            self.page,
            tag,
            width,
            x_min=x_min,
            y_min=y_min,
            x_max=x_max,
            y_max=y_max,
            offset_x=+2.5,
            offset_y=-2.5,
            **kwargs,
        )

    def span(self, tag, **kwargs):
        """Elements go sideways. Like a <span> tag."""
        return self.make(tag, 10, 0, **kwargs)

    def action(self):
        pass

    def select(self, cord_x, cord_y):
        if self.inside(cord_x, cord_y):
            self.action()
            for child in self.children():
                child.select(cord_x, cord_y)

    def button(self, tag, text, action):
        (x_min, y_min, x_max, y_max) = self.get_next()
        return self.item_set(
            tag,
            Button(
                self.collection,
                text,
                lambda: self.turn(action),
                x_min=x_min,
                y_min=y_min,
                x_max=x_max,
                y_max=y_max,
            ),
        )

    def image(self, tag, image):
        (x_min, y_min, x_max, y_max) = self.get_next()
        return self.item_set(
            tag,
            Image(
                self.collection,
                image,
                x_min=x_min,
                y_min=y_min,
                x_max=x_max,
                y_max=y_max,
            ),
        )

    def label(self, tag, text):
        (x_min, y_min, x_max, y_max) = self.get_next()
        return self.item_set(
            tag,
            Label(
                self.collection,
                text,
                x_min=x_min,
                y_min=y_min,
                x_max=x_max,
                y_max=y_max,
            ),
        )

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return False

    def __init__(self, page, name, **kwargs):
        self.page = page
        self.collection = page.collection
        self.tag = name
        self.turn = page.turn
        super().__init__(**kwargs)


class Grid(Container):
    """"""

    def get_next(self):
        """"""
        x_min = self.move_x_min + self.offset_x * (self.index_x + 0)
        y_min = self.move_y_min + self.offset_y * (self.index_y + 0)
        x_max = self.move_x_min + self.offset_x * (self.index_x + 1)
        y_max = self.move_y_min + self.offset_y * (self.index_y + 1)

        self.index_x += 1
        if self.index_x >= self.width:
            self.index_x = 0
            self.index_y += 1

        return (x_min, y_min, x_max, y_max)

    def get_x_min(self):
        """"""

    def get_tag(self, name):
        """"""
        return F"{name}_{self.index_x}-{self.index_y}"

    def __init__(self, page, name, width, **kwargs):
        self.index_x = 0
        self.index_y = 0
        self.width = width
        super().__init__(page, name, **kwargs)

