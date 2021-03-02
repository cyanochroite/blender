import bpy

print(len(bpy.data.actions), "actions")
print(len(bpy.data.armatures), "armatures")
print(len(bpy.data.brushes), "brushes")
print(len(bpy.data.cache_files), "cache_files")
print(len(bpy.data.cameras), "cameras")
print(len(bpy.data.collections), "collections")
print(len(bpy.data.curves), "curves")
print(len(bpy.data.filepath), "filepath")
print(len(bpy.data.fonts), "fonts")
print(len(bpy.data.grease_pencils), "grease_pencils")
print(len(bpy.data.images), "images")
print(len(bpy.data.lattices), "lattices")
print(len(bpy.data.libraries), "libraries")
print(len(bpy.data.lightprobes), "lightprobes")
print(len(bpy.data.lights), "lights")
print(len(bpy.data.linestyles), "linestyles")
print(len(bpy.data.masks), "masks")
print(len(bpy.data.materials), "materials")
print(len(bpy.data.meshes), "meshes")
print(len(bpy.data.metaballs), "metaballs")
print(len(bpy.data.movieclips), "movieclips")
print(len(bpy.data.node_groups), "node_groups")
print(len(bpy.data.objects), "objects")
print(len(bpy.data.paint_curves), "paint_curves")
print(len(bpy.data.palettes), "palettes")
print(len(bpy.data.particles), "particles")
print(len(bpy.data.scenes), "scenes")
print(len(bpy.data.screens), "screens")
print(len(bpy.data.shape_keys), "shape_keys")
print(len(bpy.data.sounds), "sounds")
print(len(bpy.data.speakers), "speakers")
print(len(bpy.data.texts), "texts")
print(len(bpy.data.textures), "textures")
print(len(bpy.data.version), "version")
print(len(bpy.data.volumes), "volumes")
print(len(bpy.data.window_managers), "window_managers")
print(len(bpy.data.workspaces), "workspaces")
print(len(bpy.data.worlds), "worlds")


# mesh
mesh = bpy.data.meshes.new(name)
# bmesh
bmesh = bmesh.new(use_operators=False)


bmesh_verts = bmesh.verts
for vertex in vertices:
    bmesh_verts.new(vertex)

bmesh_verts.ensure_lookup_table()

bmesh_edges = bmesh.edges
for edge in edges:
    (a, b) = edge
    A = bmesh_verts[a]
    B = bmesh_verts[b]
    edge = (A, B)
    bmesh_edges.new(edge)

bmesh_edges.ensure_lookup_table()


bmesh_faces = bmesh.faces
for face in faces:
    (a, b, c, d) = face
    A = bmesh_verts[a]
    B = bmesh_verts[b]
    C = bmesh_verts[c]
    D = bmesh_verts[d]
    face = (A, B, C, D)
    bmesh_faces.new(face)

bmesh_faces.ensure_lookup_table()


loops = bmesh.faces[0].loops
uv = bmesh.loops.layers.uv.verify()


loops[0][uv].uv = (0, 0)
loops[1][uv].uv = (1, 0)
loops[2][uv].uv = (1, 1)
loops[3][uv].uv = (0, 1)

loops[0][uv].uv = (+1, +1)
loops[1][uv].uv = (+0, +1)
loops[2][uv].uv = (+0, +0)
loops[3][uv].uv = (+1, +0)


bmesh.to_mesh(mesh)
bmesh.free()


# object
object = bpy.data.objects.new(name, mesh)
bpy.context.scene.collection.objects.link(object)

