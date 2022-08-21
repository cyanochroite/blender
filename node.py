import bpy
import bmesh
import time

for mesh in bpy.data.meshes:
    bpy.data.meshes.remove(
        mesh,
        do_unlink=True,
        do_id_user=True,
        do_ui_user=True
    )



class make_mesh():
    def __init__(self):
        self.bmesh = bmesh.new(use_operators=False)
        self.verts = self.bmesh.verts
        self.edges = self.bmesh.edges
        self.faces = self.bmesh.faces

    def vertex_add(self, x, y, z):
        coordinate = (x, y, z)
        self.verts.new(coordinate)

    def vertex_finalize(self):
        self.verts.ensure_lookup_table()

    def edge_add(self, a, b,):
        A = self.verts[a]
        B = self.verts[b]
        vertices = (A, B)
        self.edges.new(vertices)

    def edge_finalize(self):
        self.edges.ensure_lookup_table()

    def face_add(self, a, b, c, d):
        A = self.verts[a]
        B = self.verts[b]
        C = self.verts[c]
        D = self.verts[d]
        vertices = (A, B, C, D)
        self.faces.new(vertices)

    def face_finalize(self):
        self.faces.ensure_lookup_table()

    def uv_add(self, face, loop, x, y):
        uv = self.bmesh.loops.layers.uv.verify()
        self.faces[face].loops[loop][uv].uv = (x, y)

    def uv_finalize(self):
        pass

    def finalize(self, name):
        mesh = bpy.data.meshes.new(name)
        self.bmesh.to_mesh(mesh)
        self.bmesh.free()
        return mesh


def make_cube(x, y):
    x *= 2
    y *= 2
    box = make_mesh()

    box.vertex_add(x+1, y+1, +1)
    box.vertex_add(x-1, y+1, +1)
    box.vertex_add(x-1, y-1, +1)
    box.vertex_add(x+1, y-1, +1)
    box.vertex_add(x+1, y+1, -1)
    box.vertex_add(x-1, y+1, -1)
    box.vertex_add(x-1, y-1, -1)
    box.vertex_add(x+1, y-1, -1)

    box.vertex_finalize()

    box.edge_add(0, 1)
    box.edge_add(1, 2)
    box.edge_add(2, 3)
    box.edge_add(3, 0)

    box.edge_add(4, 5)
    box.edge_add(5, 6)
    box.edge_add(6, 7)
    box.edge_add(7, 4)

    box.edge_add(0, 4)
    box.edge_add(1, 5)
    box.edge_add(2, 6)
    box.edge_add(3, 7)

    box.edge_finalize()

    box.face_add(0, 1, 2, 3)
    box.face_add(4, 5, 6, 7)
    box.face_add(0, 4, 5, 1)
    box.face_add(1, 5, 6, 2)
    box.face_add(2, 6, 7, 3)
    box.face_add(3, 7, 4, 0)

    box.face_finalize()

    box.uv_add(0, 0, 1, 1)
    box.uv_add(0, 1, 0, 1)
    box.uv_add(0, 2, 0, 0)
    box.uv_add(0, 3, 1, 0)

    box.uv_add(1, 0, 1, 1)
    box.uv_add(1, 1, 0, 1)
    box.uv_add(1, 2, 0, 0)
    box.uv_add(1, 3, 1, 0)

    box.uv_add(2, 0, 1, 1)
    box.uv_add(2, 1, 0, 1)
    box.uv_add(2, 2, 0, 0)
    box.uv_add(2, 3, 1, 0)

    box.uv_add(3, 0, 1, 1)
    box.uv_add(3, 1, 0, 1)
    box.uv_add(3, 2, 0, 0)
    box.uv_add(3, 3, 1, 0)

    box.uv_add(4, 0, 1, 1)
    box.uv_add(4, 1, 0, 1)
    box.uv_add(4, 2, 0, 0)
    box.uv_add(4, 3, 1, 0)

    box.uv_add(5, 0, 1, 1)
    box.uv_add(5, 1, 0, 1)
    box.uv_add(5, 2, 0, 0)
    box.uv_add(5, 3, 1, 0)
    box.uv_finalize()

    return box.finalize("cube")


name = "cube"
mesh = bpy.data.meshes.new(name)
cube = bpy.data.objects.new(name, mesh)
bpy.context.scene.collection.objects.link(cube)
bm = bmesh.new()


maze = [True, True, True, True, True, True, True, False, True, True, True, None, True, False, True, False, False, False, False, False, False, False, True, None, True, False, True, False, True, True, True, False, True, False, True, None, True, False, False, False, False, False, True, False, True, False, True, None, True, True, True, False, True, False, True, False, True, False, True, None, True, False, False, False, True, False, True, False, True, False, True, None, True, False, True, False, True, False, True, False, True, False, True, None, True, False, True, False, True, False, True, False, True, False, True, None, True, False, True, True, True, False, True, True, True, True, True, None, True, False, True, False, False, False, False, False, False, False, True, None, True, True, True, True, True, True, True, False, True, True, True, None]

index_x = 0
index_y = 0
for cell in maze:
    if cell:
        bm.from_mesh(make_cube(index_x, index_y))
    index_x += 1
    if cell is None:
        index_x = 0
        index_y += 1

bm.to_mesh(mesh)
bm.free()
