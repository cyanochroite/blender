""""""

from celestine.window.collection import Box


class Element(Box):
    """"""

    def action(self):
        """"""
        raise NotImplementedError()

    def draw(self, mesh):
        """"""
        (x_dot, y_dot) = self.center_float()
        mesh.location = (x_dot, y_dot, 0)

    def select(self, x_dot, y_dot):
        """"""
        if self.inside(x_dot, y_dot):
            self.action()
