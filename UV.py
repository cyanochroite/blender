# <pep8-80 compliant>
# 234567890123456789012345678901234567890123456789012345678901234567890123456789
# 23456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF
import bpy
from . import new


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
