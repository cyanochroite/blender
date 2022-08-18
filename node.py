import bpy

obj = bpy.context.active_object
node_group = obj.modifiers['GeometryNodes'].node_group
nodes = node_group.nodes

for node in nodes:
    nodes.remove(node)

geom_out = nodes.get('Group Output')


size = nodes.new("FunctionNodeInputVector")
size.location = (-200, 200)
size.vector = (1, 1, 1)

vertices = nodes.new("FunctionNodeInputInt")
vertices.location = (-200, 40)
vertices.integer = 2

join = nodes.new("GeometryNodeJoinGeometry")
join.location = (3200, 50)

for index_x in range(20):
    for index_y in range(50):
        cube = nodes.new("GeometryNodeMeshCube")
        cube.location = (160 * index_x, 40 * index_y)
        cube.hide = True
        node_group.links.new(size.outputs["Vector"], cube.inputs["Size"])
        node_group.links.new(vertices.outputs["Integer"], cube.inputs["Vertices X"])
        node_group.links.new(vertices.outputs["Integer"], cube.inputs["Vertices Y"])
        node_group.links.new(vertices.outputs["Integer"], cube.inputs["Vertices Z"])
        node_group.links.new(cube.outputs["Mesh"], join.inputs["Geometry"])

group_output = nodes.new("NodeGroupOutput")
group_output.location = (600, 000)

node_group.links.new(join.outputs["Geometry"], group_output.inputs["Geometry"])

#node_group.links.new(string.outputs['String'], geom_out.inputs[-1])
