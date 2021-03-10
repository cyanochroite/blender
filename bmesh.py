
import bpy


def offset(numerator, denominator):
    ratio = numerator / denominator
    unit = 1
    maximum = max(ratio, unit)
    normalization = maximum - unit
    half = 1 / 2
    halving = normalization * half
    return halving
    #  return (max(numerator / denominator, 1) - 1) / 2


def image_offset(image, mesh):
    loops = mesh.faces[0].loops
    uv = mesh.loops.layers.uv.verify()

    size = image.size
    x = size[0]
    y = size[1]
    y_to_x = offset(y, x)
    x_to_y = offset(x, y)
    (x, y) = (y_to_x, x_to_y)

    loops[0][uv].uv = (0 - x, 0 - y)
    loops[1][uv].uv = (1 + x, 0 - y)
    loops[2][uv].uv = (1 + x, 1 + y)
    loops[3][uv].uv = (0 - x, 1 + y)


def shader_image(nodes, image):
    # inputs
    # "Vector"
    # outputs
    # "Color"
    # "Alpha"
    node = nodes.new('ShaderNodeTexImage')
    node.image = image
    node.interpolation = 'Cubic'
    node.projection = 'FLAT'
    node.extension = 'CLIP'
    return node


def shader_diffuse(nodes):
    # inputs
    # "Color"
    # "Roughness"
    # "Normal"
    # outputs
    # "BSDF"
    node = nodes.new('ShaderNodeBsdfDiffuse')
    return node


def shader_output(nodes):
    # inputs
    # "Surface"
    # "Volume"
    # "Displacement"
    # outputs
    node = nodes.new('ShaderNodeOutputMaterial')
    node.target = 'ALL'
    return node


def material(name, image):
    material = new.material(name)
    material.use_nodes = True

    tree = material.node_tree
    nodes = tree.nodes
    nodes.clear()

    aa = shader_image(nodes, image)
    aa.location = (000, 000)

    bb = shader_diffuse(nodes)
    bb.location = (300, 000)

    cc = shader_output(nodes)
    cc.location = (500, 000)

    tree.links.new(aa.outputs["Color"], bb.inputs["Color"])
    tree.links.new(bb.outputs["BSDF"], cc.inputs["Surface"])

    return material


import numpy


name = 'cow'
image = bpy.data.images[0]
vertices = [
    (+1, +1, 0),
    (-1, +1, 0),
    (-1, -1, 0),
    (+1, -1, 0)
]
edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0)
]
faces = [
    (0, 1, 2, 3)
]
uv = [
    (1, 1),
    (0, 1),
    (0, 0),
    (1, 0)
]


import bmesh


def QQ(bmesh, indexes):
    list = []
    for index in indexes:
        vert = bmesh.verts[index]
        list.append(vert)
    return tuple(list)


def QQ(bmesh, indexes):
    list = []
    for index in indexes:
        list.append(bmesh.verts[index])
    return tuple(list)


def make_vertex(bmesh, verts):
    for co in verts:
        bmesh.verts.new(co)
    bmesh.verts.ensure_lookup_table()


def make_edge(bmesh, edges):
    for edge in edges:
        verts = QQ(bmesh, edge)
        bmesh.edges.new(verts)
    bmesh.edges.ensure_lookup_table()


def make_face(bmesh, faces):
    for face in faces:
        verts = QQ(bmesh, face)
        bmesh.faces.new(verts)
    bmesh.faces.ensure_lookup_table()



# mesh
mesh = bpy.data.meshes.new(name)
# bmesh
bmesh = bmesh.new(use_operators=False)


make_vertex(bmesh, vertices)
make_edge(bmesh, edges)
make_face(bmesh, faces)


loops = bmesh.faces[0].loops
uv = bmesh.loops.layers.uv.verify()

loops[0][uv].uv = (+1, +1)
loops[1][uv].uv = (+0, +1)
loops[2][uv].uv = (+0, +0)
loops[3][uv].uv = (+1, +0)


bmesh.to_mesh(mesh)
bmesh.free()


# object
object = bpy.data.objects.new(name, mesh)
bpy.context.scene.collection.objects.link(object)


class bbmesh():
    def __init__(self, name):
        self.name = name
        self.mesh = bpy.data.meshes.new(name)
        self.bmesh = bmesh.new(use_operators=False)
        self.verts = self.bmesh.verts
        self.edges = self.bmesh.edges
        self.faces = self.bmesh.faces

    def verts_new(self, x, y, z):
        co = (x, y, z)
        self.verts.new(co)

    def verts_set(self):
        self.verts.ensure_lookup_table()

    def edges_new(self, a, b,):
        A = self.verts[a]
        B = self.verts[b]
        verts = (A, B)
        self.edges.new(verts)

    def edges_set(self):
        self.edges.ensure_lookup_table()

    def faces_new(self, a, b, c, d):
        A = self.verts[a]
        B = self.verts[b]
        C = self.verts[c]
        D = self.verts[d]
        verts = (A, B, C, D)
        self.faces.new(verts)

    def faces_set(self):
        self.faces.ensure_lookup_table()

    def uv_new(self, vertex, x, y):
        A = vertex[a]
        B = vertex[b]
        C = vertex[c]
        D = vertex[d]
        verts = (A, B, C, D)
        self.faces.new(verts)

    def uv_new(self, face, loop, x, y):
        uv = self.bmesh.loops.layers.uv.verify()
        self.faces[face].loops[loop][uv].uv = (x, y)

    def uv_set(self):
        self.bmesh.to_mesh(self.mesh)
        self.bmesh.free()
        object = bpy.data.objects.new(self.name, self.mesh)
        bpy.context.scene.collection.objects.link(object)


cow = bbmesh('cat')
cow.verts_new(+1, +1, +0)
cow.verts_new(-1, +1, +0)
cow.verts_new(-1, -1, +0)
cow.verts_new(+1, -1, +0)
cow.verts_set()

cow.edges_new(0, 1)
cow.edges_new(1, 2)
cow.edges_new(2, 3)
cow.edges_new(3, 0)
cow.edges_set()

cow.faces_new(0, 1, 2, 3)
cow.faces_set()

cow.uv_new(0, 0, 1, 1)
cow.uv_new(0, 1, 0, 1)
cow.uv_new(0, 2, 0, 0)
cow.uv_new(0, 3, 1, 0)
cow.uv_set()
