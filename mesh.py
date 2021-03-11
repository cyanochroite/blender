class mesh():
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
        self.bmesh.to_mesh(self.mesh)
        self.bmesh.free()
        object = bpy.data.objects.new(self.name, self.mesh)
        bpy.context.scene.collection.objects.link(object)

    def finalize(self, name):
        mesh = bpy.data.meshes.new(name)
        self.bmesh.to_mesh(mesh)
        self.bmesh.free()
        object = bpy.data.objects.new(name, mesh)
        bpy.context.scene.collection.objects.link(object)
        return object


def plane():
    box = mesh()

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
    return box.finalize("plane")
