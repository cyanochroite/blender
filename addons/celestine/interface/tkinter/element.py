""""""

from celestine import load
from celestine.typed import (
    TA,
    TY,
    B,
    N,
    S,
    U,
)
from celestine.window.element import Abstract as Abstract_
from celestine.window.element import Button as Button_
from celestine.window.element import Image as Image_
from celestine.window.element import Label as Label_

from . import package

BUTTON: TA = package.Button
FRAME: TA = package.Frame
LABEL: TA = package.Label

ITEM: TA = U[TY[BUTTON], TY[LABEL]]


class Abstract(Abstract_):
    """"""

    def render(self, item: ITEM, view: FRAME, **star) -> N:
        """"""
        self.item = item(view, **star)

        width = self.x_max - self.x_min
        height = self.y_max - self.y_min
        self.item.place(
            x=self.x_min,
            y=self.y_min,
            width=width,
            height=height,
        )


class Button(Abstract, Button_):
    """"""

    def callback(self) -> N:
        """"""
        self.call(self.action, **self.argument)

    def draw(self, view: FRAME, *, draw: B, **star) -> N:
        """"""
        if not draw:
            return

        item = package.Button
        star.update(command=self.callback)
        star.update(text=f"button:{self.text}")
        self.render(item, view, **star)


class Image(Abstract, Image_):
    """"""

    def draw(self, view: FRAME, *, draw: B, **star) -> N:
        """"""
        if not draw:
            return

        file = self.image or load.asset("null.png")

        item = package.Label
        self.cache = package.PhotoImage(file=file)
        star.update(image=self.cache)
        self.render(item, view, **star)

    def update(self, *, image: S, **star) -> B:
        """"""
        if not super().update(image=image, **star):
            return False

        self.cache = package.PhotoImage(file=self.image)
        self.item.configure(image=self.cache)
        self.item.image = self.cache
        return True


class Label(Abstract, Label_):
    """"""

    def draw(self, view: FRAME, *, draw: B, **star) -> N:
        """"""
        if not draw:
            return

        item = package.Label
        star.update(fg="blue")
        star.update(height=4)
        star.update(text=f"label:{self.text}")
        star.update(width=100)
        self.render(item, view, **star)
