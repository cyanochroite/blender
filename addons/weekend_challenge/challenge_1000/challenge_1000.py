"""Generate a MAZE in Blender with 1000 dead ends."""
import random

import bpy  # pylint: disable=import-error
import bmesh  # pylint: disable=import-error
import mathutils  # pylint: disable=import-error


from blender.mesh import Mesh

import blender.data

blender.data.register()

CELL_WIDTH = 80
CELL_HEIGHT = 45

CELL_SIZE = CELL_WIDTH * CELL_HEIGHT

WIDTH = CELL_WIDTH * 2 + 1
HEIGHT = CELL_HEIGHT * 2 + 1
SIZE = WIDTH * HEIGHT


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

VERTICAL = 2 * WIDTH
HORIZONTAL = 2

MAZE = []
GRID = []
LINE = []
COPY = []


def draw():
    """Draws the map in ascii characters."""
    index = 0
    for cell in MAZE:
        value = "@" if cell == WALL else " "
        print(value, end="")
        index += 1
        if index % WIDTH == 0:
            # print newLINE at end of LINE
            print("")


def north_cell(cell):
    """Return the cell north of this cell."""
    return cell - WIDTH - WIDTH


def south_cell(cell):
    """Return the cell south of this cell."""
    return cell + WIDTH + WIDTH


def east_cell(cell):
    """Return the cell east of this cell."""

    return cell + 1 + 1


def west_cell(cell):
    """Return the cell west of this cell."""
    return cell - 1 - 1


def north_wall(cell):
    """Return the cell north of this cell."""
    return cell - WIDTH


def south_wall(cell):
    """Return the cell south of this cell."""
    return cell + WIDTH


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
    value = GRID[cell]  # GRID shows neighbors

    if direction & NORTH:
        MAZE[cell] &= UNSOUTH
    if direction & SOUTH:
        MAZE[cell] &= UNNORTH
    if direction & EAST:
        MAZE[cell] &= UNWEST
    if direction & WEST:
        MAZE[cell] &= UNEAST

    if value & NORTH:
        pick = north_cell(cell)
        oppsite = UNSOUTH
        MAZE[pick] &= oppsite
    if value & SOUTH:
        pick = south_cell(cell)
        oppsite = UNNORTH
        MAZE[pick] &= oppsite
    if value & EAST:
        pick = east_cell(cell)
        oppsite = UNWEST
        MAZE[pick] &= oppsite
    if value & WEST:
        pick = west_cell(cell)
        oppsite = UNEAST
        MAZE[pick] &= oppsite


def carve(cell, direction, inside=True):
    """Carve into a neighobring cell based off the direction."""
    if direction == NORTH:
        MAZE[north_wall(cell)] = HOLE

    if direction == SOUTH:
        MAZE[south_wall(cell)] = HOLE

    if direction == EAST:
        MAZE[east_wall(cell)] = HOLE

    if direction == WEST:
        MAZE[west_wall(cell)] = HOLE

    if inside:
        uncarved_neighbor(cell, direction)

    return move(cell, direction)


def carve_random(cell):
    """Pick a random direction to carve from the valid directions."""
    direction = MAZE[cell]
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
    length = len(LINE)
    index = random.randrange(length)
    cell = LINE[index]
    return cell


def count():
    """Count all the walls in the current MAZE."""
    counted = 0
    # loop over each cell from a COPY of cells from the MAZE
    for cell in COPY:
        walls = 0
        walls += 1 if MAZE[north_wall(cell)] == WALL else 0
        walls += 1 if MAZE[south_wall(cell)] == WALL else 0
        walls += 1 if MAZE[east_wall(cell)] == WALL else 0
        walls += 1 if MAZE[west_wall(cell)] == WALL else 0
        counted += 1 if walls == 3 else 0
    return counted


def mazeit(seed):
    """Generate a MAZE based off the given seed value."""
    global LINE  # pylint: disable=global-statement
    global MAZE  # pylint: disable=global-statement
    global COPY  # pylint: disable=global-statement
    global GRID  # pylint: disable=global-statement

    MAZE = []  # holds the MAZE data as it is being built
    GRID = []  # a GRID holding all valid neighbors
    LINE = []  # a list of positions for cells in the MAZE
    COPY = []  # a COPY of the LINE list used for counting dead ends

    random.seed(seed)

    for cell in range(SIZE):
        position_x = cell % WIDTH
        position_y = cell // WIDTH
        odd_x = position_x % 2
        odd_y = position_y % 2
        space = odd_x and odd_y
        north = cell >= VERTICAL
        south = VERTICAL < SIZE - cell
        east = position_x + HORIZONTAL < WIDTH
        west = position_x - HORIZONTAL >= 0
        direction = 0
        direction |= NORTH if north else 0
        direction |= SOUTH if south else 0
        direction |= EAST if east else 0
        direction |= WEST if west else 0
        GRID.append(direction if space else WALL)
        MAZE.append(direction if space else WALL)
        if space:
            COPY.append(cell)
            LINE.append(cell)

    enter = random.randrange(CELL_HEIGHT) * CELL_WIDTH
    finish = random.randrange(CELL_HEIGHT) * CELL_WIDTH + CELL_WIDTH - 1

    enter = COPY[enter]
    finish = COPY[finish]

    carve(enter, WEST, False)
    carve(finish, EAST, False)

    LINE = [enter]
    length = len(LINE)

    while length > 0:
        LINE.append(
            carve_random(
               random_from_list()
            )
        )

        LINE = [item for item in LINE if MAZE[item] > 0]

        length = len(LINE)

    return count()


def finalize():
    """
    Prepare MAZE for use in blender.
    Positive numbers indicate which cells have walls.
    Negative numbers indicate holes.
    """
    final = []
    index = 0
    for cell in MAZE:
        if cell == WALL:
            has_north_wall = (index - WIDTH) >= 0
            has_south_wall = (index + WIDTH) < SIZE
            has_east_wall = ((index + 1) % WIDTH) != 0
            has_west_wall = ((index + 0) % WIDTH) != 0

            direction = 0
            if not has_north_wall or MAZE[north_wall(index)] != WALL:
                direction |= NORTH

            if not has_south_wall or MAZE[south_wall(index)] != WALL:
                direction |= SOUTH

            if not has_east_wall or MAZE[east_wall(index)] != WALL:
                direction |= EAST

            if not has_west_wall or MAZE[west_wall(index)] != WALL:
                direction |= WEST

            final.append(direction)
        else:
            final.append(HOLE)
        index += 1
        if index % WIDTH == 0:
            # end of LINE marker
            final.append(None)
    return final


def find_seed():
    """Look through 1000 MAZEs to find a MAZE with 1000 dead ends."""
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
    for cell in MAZE:
        if cell is None:
            index_x = -1
            index_y += 1
        elif cell >= 0:
            cube = make_cube(index_x * 2, -index_y * 2, cell)
            beemesh.from_mesh(cube)
        index_x += 1

    beemesh.to_mesh(mesh)
    beemesh.free()


# find_seed()  # generate a bunch of MAZEs and hope we find a good one

mazeit(360)  # generate a MAZE with the given seed

draw()  # draw it to the screen

MAZE = finalize()  # get the MAZE ready for blender

# print(MAZE) # peak at what the final list looks like

mesh_remove()  # remove all meshes from the scene

main()  # draw the MAZE into the scene
