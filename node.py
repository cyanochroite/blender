"""Generate a maze in Blender with 1000 dead ends."""
import bpy
import bmesh

NORTH = 1
SOUTH = 2
EAST = 4
WEST = 8
WALL = -1
HOLE = -2

maze = [9, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, None, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, None, 14, -1, 11, 3, 5, -1, 9, 3, 5, -1, 12, None, -1, -1, -1, -1, 12, -1, 12, -1, 12, -1, 12, None, 13, -1, 13, -1, 10, 3, 6, -1, 10, 3, 6, None, 12, -1, 12, -1, -1, -1, -1, -1, -1, -1, -1, None, 12, -1, 10, 3, 3, 3, 5, -1, 13, -1, 13, None, 12, -1, -1, -1, -1, -1, 12, -1, 12, -1, 12, None, 12, -1, 13, -1, 13, -1, 12, -1, 10, 3, 4, None, 12, -1, 12, -1, 12, -1, 12, -1, -1, -1, 12, None, 10, 3, 2, 3, 2, 3, 2, 3, 3, 3, 6, None]


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
        mesh = bpy.data.meshes.new(name)
        self.bmesh.to_mesh(mesh)
        self.bmesh.free()
        return mesh


def mesh_remove():
    """Remove all mesh data from scene."""
    for mesh in bpy.data.meshes:
        bpy.data.meshes.remove(
            mesh,
            do_unlink=True,
            do_id_user=True,
            do_ui_user=True
        )


def make_cube(position_x, position_y, wall):
    """Make a cube with optional walls."""
    mesh = Mesh()

    mesh.vertex_add(position_x + 1, position_y + 1, +1)
    mesh.vertex_add(position_x - 1, position_y + 1, +1)
    mesh.vertex_add(position_x - 1, position_y - 1, +1)
    mesh.vertex_add(position_x + 1, position_y - 1, +1)
    mesh.vertex_add(position_x + 1, position_y + 1, -1)
    mesh.vertex_add(position_x - 1, position_y + 1, -1)
    mesh.vertex_add(position_x - 1, position_y - 1, -1)
    mesh.vertex_add(position_x + 1, position_y - 1, -1)

    mesh.vertex_finalize()

    mesh.edge_add(0, 1)
    mesh.edge_add(1, 2)
    mesh.edge_add(2, 3)
    mesh.edge_add(3, 0)

    mesh.edge_add(4, 5)
    mesh.edge_add(5, 6)
    mesh.edge_add(6, 7)
    mesh.edge_add(7, 4)

    mesh.edge_add(0, 4)
    mesh.edge_add(1, 5)
    mesh.edge_add(2, 6)
    mesh.edge_add(3, 7)

    mesh.edge_finalize()

    mesh.face_add(0, 1, 2, 3)
    mesh.face_add(4, 7, 6, 5)

    if wall & NORTH:
        mesh.face_add(0, 4, 5, 1)
    if wall & WEST:
        mesh.face_add(1, 5, 6, 2)
    if wall & SOUTH:
        mesh.face_add(2, 6, 7, 3)
    if wall & EAST:
        mesh.face_add(3, 7, 4, 0)

    mesh.face_finalize()

    mesh.uv_add(0, 0, 1, 1)
    mesh.uv_add(0, 1, 0, 1)
    mesh.uv_add(0, 2, 0, 0)
    mesh.uv_add(0, 3, 1, 0)

    mesh.uv_add(1, 0, 1, 1)
    mesh.uv_add(1, 1, 0, 1)
    mesh.uv_add(1, 2, 0, 0)
    mesh.uv_add(1, 3, 1, 0)

    return mesh.finalize("cube")


def main():
    """The main function."""
    name = "cube"
    mesh = bpy.data.meshes.new(name)
    cube = bpy.data.objects.new(name, mesh)
    bpy.context.scene.collection.objects.link(cube)
    beemesh = bmesh.new()

    index_x = 0
    index_y = 0
    for cell in maze:
        if cell is None:
            index_x = -1
            index_y += 1
        elif cell >= 0:
            cube = make_cube(index_x * 2, -index_y * 2, cell)
            beemesh.from_mesh(cube)
        index_x += 1

    beemesh.to_mesh(mesh)
    beemesh.free()


mesh_remove()
main()
