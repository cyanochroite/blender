"""Page object."""

from .package import data

from .container import Container


class Page(Container):
    """The page object."""

    def __init__(self, window, name, **kwargs):
        self.collection = data.collection.make(name)
        self.name = name
        self.turn = window.turn
        #
        self.session = window.session
        self.frame = self.collection
        #
        super().__init__(self, name, **kwargs)
        self.collection.hide()
