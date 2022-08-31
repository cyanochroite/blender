"""Generate a maze in Blender with 1000 dead ends."""

import random
import mathutils

from blender.mesh import Mesh

import blender.data

blender.data.register()

cell_width = 80
cell_height = 45

cell_size = cell_width * cell_height

width = cell_width * 2 + 1
height = cell_height * 2 + 1
size = width * height


NORTH = 1
SOUTH = 2
EAST = 4
WEST = 8
WALL = -1
HOLE = -2

UNNORTH = 14
UNSOUTH = 13
UNEAST = 11
UNWEST = 7

VERTICAL = 2 * width
HORIZONTAL = 2

maze = []
grid = []
line = []
copy = []


def draw():
    """Draws the map in ascii characters."""
    index = 0
    for cell in maze:
        value = "@" if cell == WALL else " "
        print(value, end="")
        index += 1
        if index % width == 0:
            # print newline at end of line
            print("")


def north_cell(cell):
    """Return the cell north of this cell."""
    return cell - width - width


def south_cell(cell):
    """Return the cell south of this cell."""
    return cell + width + width


def east_cell(cell):
    """Return the cell east of this cell."""

    return cell + 1 + 1


def west_cell(cell):
    """Return the cell west of this cell."""
    return cell - 1 - 1


def north_wall(cell):
    """Return the cell north of this cell."""
    return cell - width


def south_wall(cell):
    """Return the cell south of this cell."""
    return cell + width


def east_wall(cell):
    """Return the cell east of this cell."""
    return cell + 1


def west_wall(cell):
    """Return the cell west of this cell."""
    return cell - 1


def move(cell, direction):
    """Move to a neighboring cell from the selected direction."""
    if direction == NORTH:
        neighbor = north_cell(cell)
    if direction == SOUTH:
        neighbor = south_cell(cell)
    if direction == EAST:
        neighbor = east_cell(cell)
    if direction == WEST:
        neighbor = west_cell(cell)
    return neighbor


def uncarved_neighbor(cell_start, direction):
    """Tell our neighbors to not carve into us anymore."""
    cell = move(cell_start, direction)
    value = grid[cell]  # grid shows neighbors

    if direction & NORTH:
        maze[cell] &= UNSOUTH
    if direction & SOUTH:
        maze[cell] &= UNNORTH
    if direction & EAST:
        maze[cell] &= UNWEST
    if direction & WEST:
        maze[cell] &= UNEAST

    if value & NORTH:
        pick = north_cell(cell)
        oppsite = UNSOUTH
        maze[pick] &= oppsite
    if value & SOUTH:
        pick = south_cell(cell)
        oppsite = UNNORTH
        maze[pick] &= oppsite
    if value & EAST:
        pick = east_cell(cell)
        oppsite = UNWEST
        maze[pick] &= oppsite
    if value & WEST:
        pick = west_cell(cell)
        oppsite = UNEAST
        maze[pick] &= oppsite


def carve(cell, direction, inside=True):
    """Carve into a neighobring cell based off the direction."""
    if direction == NORTH:
        maze[north_wall(cell)] = HOLE

    if direction == SOUTH:
        maze[south_wall(cell)] = HOLE

    if direction == EAST:
        maze[east_wall(cell)] = HOLE

    if direction == WEST:
        maze[west_wall(cell)] = HOLE

    if inside:
        uncarved_neighbor(cell, direction)

    return move(cell, direction)


def carve_random(cell):
    """Pick a random direction to carve from the valid directions."""
    direction = maze[cell]
    choice = []

    if direction & NORTH:
        choice.append(NORTH)

    if direction & SOUTH:
        choice.append(SOUTH)

    if direction & EAST:
        choice.append(EAST)

    if direction & WEST:
        choice.append(WEST)

    direction = random.choice(choice)

    return carve(cell, direction)


def random_from_list():
    """Return a random cell from the list of unfinished cells."""
    length = len(line)
    index = random.randrange(length)
    cell = line[index]
    return cell


def count():
    """Count all the walls in the current maze."""
    counted = 0
    # loop over each cell from a copy of cells from the maze
    for cell in copy:
        walls = 0
        walls += 1 if maze[north_wall(cell)] == WALL else 0
        walls += 1 if maze[south_wall(cell)] == WALL else 0
        walls += 1 if maze[east_wall(cell)] == WALL else 0
        walls += 1 if maze[west_wall(cell)] == WALL else 0
        counted += 1 if walls == 3 else 0
    return counted


def mazeit(seed):
    """Generate a maze based off the given seed value."""
    global line
    global maze
    global copy
    global grid

    maze = []  # holds the maze data as it is being built
    grid = []  # a grid holding all valid neighbors
    line = []  # a list of positions for cells in the maze
    copy = []  # a copy of the line list used for counting dead ends

    random.seed(seed)

    for cell in range(size):
        if cell == 12:
            pass
        x = cell % width
        y = cell // width
        odd_x = x % 2
        odd_y = y % 2
        space = odd_x and odd_y
        north = cell >= VERTICAL
        south = VERTICAL < size - cell
        east = x + HORIZONTAL < width
        west = x - HORIZONTAL >= 0
        c = 0
        c |= NORTH if north else 0
        c |= SOUTH if south else 0
        c |= EAST if east else 0
        c |= WEST if west else 0
        grid.append(c if space else WALL)
        maze.append(c if space else WALL)
        if space:
            copy.append(cell)
            line.append(cell)

    enter = random.randrange(cell_height) * cell_width
    finish = random.randrange(cell_height) * cell_width + cell_width - 1

    enter = copy[enter]
    finish = copy[finish]

    carve(enter, WEST, False)
    carve(finish, EAST, False)

    line = [enter]
    length = len(line)

    while length > 0:
        line.append(
            carve_random(
               random_from_list()
            )
        )

        line = [item for item in line if maze[item] > 0]

        length = len(line)

    return count()


def finalize():
    """
    Prepare maze for use in blender.
    Positive numbers indicate which cells have walls.
    Negative numbers indicate holes.
    """
    final = []
    index = 0
    for cell in maze:
        if cell == WALL:
            has_north_wall = (index - width) >= 0
            has_south_wall = (index + width) < size
            has_east_wall = ((index + 1) % width) != 0
            has_west_wall = ((index + 0) % width) != 0

            direction = 0
            if not has_north_wall or maze[north_wall(index)] != WALL:
                direction |= NORTH

            if not has_south_wall or maze[south_wall(index)] != WALL:
                direction |= SOUTH

            if not has_east_wall or maze[east_wall(index)] != WALL:
                direction |= EAST

            if not has_west_wall or maze[west_wall(index)] != WALL:
                direction |= WEST

            final.append(direction)
        else:
            final.append(HOLE)
        index += 1
        if index % width == 0:
            # end of line marker
            final.append(None)
    return final


def find_seed():
    """Look through 1000 mazes to find a maze with 1000 dead ends."""
    for seed in range(1000):
        many = mazeit(seed)
        if many == 1000:
            print(seed)
            draw()
    print("End of seed search.""")


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

    mesh.vertex_add(mathutils.Vector((position_x + 1, position_y + 1, +1)))
    mesh.vertex_add(mathutils.Vector((position_x - 1, position_y + 1, +1)))
    mesh.vertex_add(mathutils.Vector((position_x - 1, position_y - 1, +1)))
    mesh.vertex_add(mathutils.Vector((position_x + 1, position_y - 1, +1)))
    mesh.vertex_add(mathutils.Vector((position_x + 1, position_y + 1, -1)))
    mesh.vertex_add(mathutils.Vector((position_x - 1, position_y + 1, -1)))
    mesh.vertex_add(mathutils.Vector((position_x - 1, position_y - 1, -1)))
    mesh.vertex_add(mathutils.Vector((position_x + 1, position_y - 1, -1)))

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


# find_seed()  # generate a bunch of mazes and hope we find a good one

mazeit(360)  # generate a maze with the given seed

draw()  # draw it to the screen

maze = finalize()  # get the maze ready for blender

# print(maze) # peak at what the final list looks like

# this part only works in blender
import bpy
import bmesh

mesh_remove()  # remove all meshes from the scene

main()  # draw the maze into the scene
