import bpy
import time

obj = bpy.context.active_object
node_group = obj.modifiers['GeometryNodes'].node_group
nodes = node_group.nodes

for node in nodes:
    nodes.remove(node)

geom_out = nodes.get('Group Output')


join = nodes.new("GeometryNodeJoinGeometry")
join.location = (3200, 50)

maze = [True, False, None, True, True]

index_x = 0
index_y = 0
for cell in maze:
    if cell == None:
        index_x = 0
        index_y += 1

    transform = nodes.new("GeometryNodeTransform")
    transform.location = (160 + 320 * index_x, 40 * index_y)
    transform.hide = True
    transform.inputs["Translation"].default_value = (1, 2, 3)
    transform.inputs["Rotation"].default_value = (0, 0, 0)
    transform.inputs["Scale"].default_value = (1, 1, 1)
    node_group.links.new(transform.outputs["Geometry"], join.inputs["Geometry"])

    cube = nodes.new("GeometryNodeMeshCube")
    cube.location = (320 * index_x, 40 * index_y)
    cube.hide = True
    cube.inputs["Size"].default_value = (1, 1, 1)
    cube.inputs["Vertices X"].default_value = 2
    cube.inputs["Vertices Y"].default_value = 2
    cube.inputs["Vertices Z"].default_value = 2
    node_group.links.new(cube.outputs["Mesh"], transform.inputs["Geometry"])

    time.sleep(0.001)

group_output = nodes.new("NodeGroupOutput")
group_output.location = (600, 000)

node_group.links.new(join.outputs["Geometry"], group_output.inputs["Geometry"])

#node_group.links.new(string.outputs['String'], geom_out.inputs[-1])
