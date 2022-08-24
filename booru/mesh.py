# <pep8-80 compliant>
import bmesh

from . import new
from . import make


class Mesh():
    """Create a mesh in Blender."""

    def __init__(self):
        self.bmesh = bmesh.new(use_operators=False)
        self.verts = self.bmesh.verts
        self.edges = self.bmesh.edges
        self.faces = self.bmesh.faces

    def vertex_add(self, position_x, position_y, position_z):
        """Add 'vertex' to the mesh."""
        coordinate = (position_x, position_y, position_z)
        self.verts.new(coordinate)

    def vertex_finalize(self):
        """Call this after adding all 'vertex' to mesh."""
        self.verts.ensure_lookup_table()

    def edge_add(self, vertex_a, vertex_b,):
        """Add 'edge' to the mesh."""
        vert_a = self.verts[vertex_a]
        vert_b = self.verts[vertex_b]
        vertices = (vert_a, vert_b)
        self.edges.new(vertices)

    def edge_finalize(self):
        """Call this after adding all 'edge' to mesh."""
        self.edges.ensure_lookup_table()

    def face_add(self, vertex_a, vertex_b, vertex_c, vertex_d):
        """Add 'face' to the mesh."""
        vert_a = self.verts[vertex_a]
        vert_b = self.verts[vertex_b]
        vert_c = self.verts[vertex_c]
        vert_d = self.verts[vertex_d]
        vertices = (vert_a, vert_b, vert_c, vert_d)
        self.faces.new(vertices)

    def face_finalize(self):
        """Call this after adding all 'face' to mesh."""
        self.faces.ensure_lookup_table()

    def uv_add(self, face, loop, position_x, position_y):
        """Add 'uv' to the mesh."""
        index_uv = self.bmesh.loops.layers.uv.verify()
        self.faces[face].loops[loop][index_uv].uv = (position_x, position_y)

    def uv_finalize(self):
        """Call this after adding all 'uv' to mesh."""

    def finalize(self, name):
        """Call this after adding all the stuff to mesh."""
        mesh = new.mesh(name)
        self.bmesh.to_mesh(mesh)
        self.bmesh.free()
        return mesh


def plane():
    box = Mesh()

    box.vertex_add(+1, +1, +0)
    box.vertex_add(-1, +1, +0)
    box.vertex_add(-1, -1, +0)
    box.vertex_add(+1, -1, +0)
    box.vertex_finalize()

    box.edge_add(0, 1)
    box.edge_add(1, 2)
    box.edge_add(2, 3)
    box.edge_add(3, 0)
    box.edge_finalize()

    box.face_add(0, 1, 2, 3)
    box.face_finalize()

    box.uv_add(0, 0, 1, 1)
    box.uv_add(0, 1, 0, 1)
    box.uv_add(0, 2, 0, 0)
    box.uv_add(0, 3, 1, 0)
    box.uv_finalize()

    return_ = box.finalize("plane")
    return make.mesh("plane", return_)  # move this up a level to caller


def _offset(numerator, denominator):
    ratio = numerator / denominator
    unit = 1
    maximum = max(ratio, unit)
    normalization = maximum - unit
    half = 1 / 2
    halving = normalization * half
    return halving
    #  return (max(numerator / denominator, 1) - 1) / 2


def image(image):
    box = Mesh()

    box.vertex_add(+1, +1, +0)
    box.vertex_add(-1, +1, +0)
    box.vertex_add(-1, -1, +0)
    box.vertex_add(+1, -1, +0)
    box.vertex_finalize()

    box.edge_add(0, 1)
    box.edge_add(1, 2)
    box.edge_add(2, 3)
    box.edge_add(3, 0)
    box.edge_finalize()

    box.face_add(0, 1, 2, 3)
    box.face_finalize()

    # why do we have duplicate code above?
    size = image.size
    x = size[0]
    y = size[1]
    y_to_x = _offset(y, x)
    x_to_y = _offset(x, y)
    (x, y) = (y_to_x, x_to_y)

    box.uv_add(0, 0, 1 + x, 1 + y)
    box.uv_add(0, 1, 0 - x, 1 + y)
    box.uv_add(0, 2, 0 - x, 0 - y)
    box.uv_add(0, 3, 1 + x, 0 - y)
    box.uv_finalize()

    return_ = box.finalize("plane")
    return make.mesh("plane", return_)  # move this up a level to caller

