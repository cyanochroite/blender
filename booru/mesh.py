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


###
import mathutils
import math


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Vector():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Mesh():
    """Create a mesh in Blender."""

    def __init__(self):
        self.bmesh = bmesh.new(use_operators=False)
        self.verts = self.bmesh.verts
        self.edges = self.bmesh.edges
        self.faces = self.bmesh.faces

    def vertex_add(self, vector):
        """Add 'vertex' to the mesh."""
        coordinate = (vector.x, vector.y, vector.z)
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

    def uv_add(self, face, loop, point):
        """Add 'uv' to the mesh."""
        index_uv = self.bmesh.loops.layers.uv.verify()
        self.faces[face].loops[loop][index_uv].uv = (point.x, point.y)

    def uv_finalize(self):
        """Call this after adding all 'uv' to mesh."""

    def finalize(self, name):
        """Call this after adding all the stuff to mesh."""
        mesh = new.mesh(name)
        self.bmesh.to_mesh(mesh)
        self.bmesh.free()
        return mesh


class Quadrilateral(Mesh):
    def __init__(self):
        self.bmesh = bmesh.new(use_operators=False)
        self.verts = self.bmesh.verts
        self.edges = self.bmesh.edges
        self.faces = self.bmesh.faces

    def vertex(self, zero, one, two, three):
        self.vertex_add(zero)
        self.vertex_add(one)
        self.vertex_add(two)
        self.vertex_add(three)
        self.vertex_finalize()

    def edge(self):
        self.edge_add(0, 1)
        self.edge_add(1, 2)
        self.edge_add(2, 3)
        self.edge_add(3, 0)
        self.edge_finalize()

    def face(self):
        self.face_add(0, 1, 2, 3)
        self.face_finalize()

    def uv(self, zero, one, two, three):
        self.uv_add(0, 0, zero)
        self.uv_add(0, 1, one)
        self.uv_add(0, 2, two)
        self.uv_add(0, 3, three)
        self.uv_finalize()

    def finalize(self, name="Plane"):
        return make.mesh(name, super().finalize(name))

# square


class Plane(Mesh):
    def __init__(self):
        self.bmesh = bmesh.new(use_operators=False)
        self.verts = self.bmesh.verts
        self.edges = self.bmesh.edges
        self.faces = self.bmesh.faces

    def vertex_add_rotate(self, vector, normal):
        my_normal = mathutils.Vector((+0, +0, +1))
        rotation = my_normal.rotation_difference(normal)
        vector.rotate(rotation)
        self.vertex_add(vector)

    def vertex(self):
        normal = mathutils.Vector((+0, +1, +0))

        vector_a = mathutils.Vector((+1, +1, +0))
        vector_b = mathutils.Vector((-1, +1, +0))
        vector_c = mathutils.Vector((-1, -1, +0))
        vector_d = mathutils.Vector((+1, -1, +0))

        self.vertex_add_rotate(vector_a, normal)
        self.vertex_add_rotate(vector_b, normal)
        self.vertex_add_rotate(vector_c, normal)
        self.vertex_add_rotate(vector_d, normal)

        self.vertex_finalize()

    def edge(self):
        self.edge_add(0, 1)
        self.edge_add(1, 2)
        self.edge_add(2, 3)
        self.edge_add(3, 0)
        self.edge_finalize()

    def face(self):
        self.face_add(0, 1, 2, 3)
        self.face_finalize()

    def uv(self, uv_x=0, uv_y=0):
        self.uv_add(0, 0, Point(1 + uv_x, 1 + uv_y))
        self.uv_add(0, 1, Point(0 - uv_x, 1 + uv_y))
        self.uv_add(0, 2, Point(0 - uv_x, 0 - uv_y))
        self.uv_add(0, 3, Point(1 + uv_x, 0 - uv_y))
        self.uv_finalize()

    def finalize(self, name="Plane"):
        return make.mesh(name, super().finalize(name))


def plane(uv_x=0, uv_y=0):
    box = Plane()
    box.vertex()
    box.edge()
    box.face()
    box.uv(uv_x, uv_y)
    return box.finalize()


def image(image):
    # why do we have duplicate code above?
    size = image.size
    x = size[0]
    y = size[1]
    y_to_x = _offset(y, x)
    x_to_y = _offset(x, y)
    (x, y) = (y_to_x, x_to_y)

    return plane(x, y)


