""""""

from celestine.window.collection import Rectangle

from .button import Button
from .image import Image
from .label import Label


class Container(Rectangle):
    """"""

    def make(self, tag, offset_x, offset_y, **kwargs):
        """Make a new Container."""
        return Container(
            self.page,
            tag,
            x_min=self.get_x_min(),
            y_min=self.get_y_min(),
            x_max=self.get_x_max(),
            y_max=self.get_y_max(),
            offset_x=offset_x,
            offset_y=offset_y,
            **kwargs,
        )

    def drop(self, tag, **kwargs):
        """Elements go down. Like a <div> tag."""
        return self.make(tag, 0, -2.5, **kwargs)

    def grid(self, tag, **kwargs):
        """Elements go in a grid. Like the <table> tag."""
        return self.make(tag, 10, -2.5, **kwargs)

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
        return self.item_set(
            tag,
            Button(
                self.collection,
                text,
                lambda: self.turn(action),
                x_min=self.get_x_min(),
                y_min=self.get_y_min(),
                x_max=self.get_x_max(),
                y_max=self.get_y_max(),
            ),
        )

    def image(self, tag, image):
        return self.item_set(
            tag,
            Image(
                self.collection,
                image,
                x_min=self.get_x_min(),
                y_min=self.get_y_min(),
                x_max=self.get_x_max(),
                y_max=self.get_y_max(),
            ),
        )

    def label(self, tag, text):
        return self.item_set(
            tag,
            Label(
                self.collection,
                text,
                x_min=self.get_x_min(),
                y_min=self.get_y_min(),
                x_max=self.get_x_max(),
                y_max=self.get_y_max(),
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
