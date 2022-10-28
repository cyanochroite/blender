# <pep8-80 compliant>
import bmesh
import mathutils

from celestine.package.blender.package import data


class Mesh():
    def main(self, verts, edges, faces, layers):
        for vert in verts:
            self.verts.new(vert)
        self.verts.ensure_lookup_table()

        for (one, two) in edges:
            self.edges.new((self.verts[one], self.verts[two]))
        self.edges.ensure_lookup_table()

        for face in faces:
            self.faces.new(map(lambda vert: self.verts[vert], face))
        self.faces.ensure_lookup_table()

        layer = self.bmesh.loops.layers.uv.verify()
        for (face, loop, one, two) in layers:
            self.faces[face].loops[loop][layer].uv = (one, two)

    def __init__(self):
        self.bmesh = bmesh.new(use_operators=False)
        self.verts = self.bmesh.verts
        self.edges = self.bmesh.edges
        self.faces = self.bmesh.faces

    def finalize(self, name):
        """Call this after adding all the stuff to mesh."""
        mesh = data.mesh.new(name)
        self.bmesh.to_mesh(mesh)
        self.bmesh.free()
        return mesh


class Quadrilateral(Mesh):
    def mymain(self, verts, layers):
        edges = [
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 0),
        ]

        faces = [
            (0, 1, 2, 3),
        ]

        self.main(verts, edges, faces, layers)


class Planar(Quadrilateral):
    def __init__(self):
        super().__init__()
        self.normal = mathutils.Vector((+0, +0, +1))

    def vertex_new(self, vector, normal):
        vector = mathutils.Vector(vector)
        vector.resize_3d()
        rotation = self.normal.rotation_difference(normal)
        vector.rotate(rotation)
        return vector


class Plane(Planar):
    def verts_list(self, normal=(+1, +1, +1)):
        normal = mathutils.Vector(normal)

        vector_a = self.vertex_new((+1, +1), normal)
        vector_b = self.vertex_new((-1, +1), normal)
        vector_c = self.vertex_new((-1, -1), normal)
        vector_d = self.vertex_new((+1, -1), normal)

        return [vector_a, vector_b, vector_c, vector_d]

    def layers_list(self, uv_x=0, uv_y=0):
        return [
            (0, 0, 1 + uv_x, 1 + uv_y),
            (0, 1, 0 - uv_x, 1 + uv_y),
            (0, 2, 0 - uv_x, 0 - uv_y),
            (0, 3, 1 + uv_x, 0 - uv_y),
        ]


def plane(uv_x=0, uv_y=0):
    box = Plane()
    verts = box.verts_list()
    layers = box.layers_list(uv_x, uv_y)
    box.mymain(verts, layers)

    name = "Plane"
    return box.finalize(name)


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
    size = image.size
    x = size[0]
    y = size[1]
    y_to_x = _offset(y, x)
    x_to_y = _offset(x, y)
    (x, y) = (y_to_x, x_to_y)

    return plane(x, y)
