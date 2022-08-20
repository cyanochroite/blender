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


def new_mesh(name, location):
    mesh = bpy.data.meshes.new(name)
    object = bpy.data.objects.new(name, mesh)
    bpy.context.scene.collection.objects.link(object)

    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    bm.to_mesh(mesh)
    bm.free()

    object.location = location

    return object


maze = [True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, None, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, True, None, True, False, True, True, True, False, True, False, True, False, True, False, True, True, True, True, True, True, True, False, True, None, True, False, True, False, False, False, True, False, True, False, True, False, False, False, False, False, False, False, False, False, True, None, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, True, True, True, True, None, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, False, False, False, False, True, None, True, False, True, False, True, False, True, False, True, True, True, False, True, True, True, False, True, True, True, False, True, None, True, False, True, False, True, False, True, False, True, False, False, False, False, False, True, False, False, False, True, False, True, None, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, True, True, True, True, False, True, None, True, False, True, False, True, False, True, False, True, False, True, False, True, False, False, False, True, False, False, False, True, None, True, False, True, True, True, False, True, False, True, True, True, True, True, False, True, False, True, True, True, False, True, None, True, False, False, False, True, False, True, False, False, False, True, False, False, False, True, False, True, False, False, False, True, None, True, False, True, True, True, False, True, False, True, False, True, True, True, False, True, False, True, False, True, False, True, None, True, False, False, False, True, False, True, False, True, False, False, False, True, False, True, False, True, False, True, False, True, None, True, False, True, False, True, True, True, False, True, False, True, True, True, False, True, False, True, True, True, False, True, None, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True, None, True, False, True, True, True, True, True, True, True, False, True, False, True, False, True, True, True, True, True, False, True, None, True, False, True, False, False, False, True, False, True, False, True, False, True, False, False, False, True, False, True, False, True, None, True, False, True, False, True, True, True, False, True, False, True, False, True, True, True, True, True, False, True, True, True, None, True, False, False, False, False, False, False, False, True, False, True, False, False, False, False, False, False, False, False, False, True, None, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, None]



index_x = 0
index_y = 0
for cell in maze:
    if cell:
        new_mesh(F"{index_x},{index_y}", (index_x, index_y, 0))
    index_x += 1
    if cell is None:
        index_x = 0
        index_y += 1

