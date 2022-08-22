"""Generate a maze in Blender with 1000 dead ends."""
import random

cell_width = 80
cell_height = 45

#cell_width = 5
#cell_height = 5

cell_size = cell_width * cell_height

width = cell_width * 2 + 1
height = cell_height * 2 + 1
size = width * height


WALL = -1
HOLE = -2

NORTH = 1 << 0
SOUTH = 1 << 1
EAST = 1 << 2
WEST = 1 << 3

NORTH = 1
SOUTH = 2
EAST = 4
WEST = 8

UNNORTH = 14
UNSOUTH = 13
UNEAST = 11
UNWEST = 7

VERTICAL = 2 * width
HORIZONTAL = 2


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
    """Return the wall value north of this cell."""
    return maze[cell - width]


def south_wall(cell):
    """Return the wall value south of this cell."""
    return maze[cell + width]


def east_wall(cell):
    """Return the wall value east of this cell."""
    return maze[cell + 1]


def west_wall(cell):
    """Return the wall value west of this cell."""
    return maze[cell - 1]


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
    pick = 0
    frog = cell
    oppsite = 0
    match direction:
        case 1:  # NORTH
            pick = frog - width
        case 2:  # SOUTH
            pick = frog + width
        case 4:  # EAST
            pick = frog + 1
        case 8:  # WEST
            pick = frog - 1
    maze[pick] = HOLE
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
    count = 0
    # loop over each cell from a copy of cells from the maze
    for cell in copy:
        walls = 0
        walls += 1 if north_wall(cell) == WALL else 0
        walls += 1 if south_wall(cell) == WALL else 0
        walls += 1 if east_wall(cell) == WALL else 0
        walls += 1 if west_wall(cell) == WALL else 0
        count += 1 if walls == 3 else 0
    return count


def mazeit(seed):
    global line
    global maze
    global copy
    global grid

    maze = []
    grid = []
    line = []
    copy = []

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
    exit = random.randrange(cell_height) * cell_width + cell_width - 1

    enter = copy[enter]
    exit = copy[exit]

    carve(enter, WEST, False)
    carve(exit, EAST, False)

    fail = 100000
    line = [enter]
    cat = len(line)

    while fail > 0 and cat > 0:
        fail -= 1
        # draw()

        cell = random_from_list()
        where = carve_random(cell)
        line.append(where)

        line = [item for item in line if maze[item] > 0]

        cat = len(line)

    if fail <= 0:
        print("FAILFAILFAILFAILFAIL")

    return count()


def finish():
    final = []
    index = 0
    for cell in maze:
        if cell == WALL:
            has_north_wall = (index - width) >= 0
            has_south_wall = (index + width) < size
            has_east_wall = ((index + 1) % width) != 0
            has_west_wall = ((index + 0) % width) != 0

            direction = 0
            if not has_north_wall or north_wall(index) != WALL:
                direction |= NORTH

            if not has_south_wall or south_wall(index) != WALL:
                direction |= SOUTH

            if not has_east_wall or east_wall(index) != WALL:
                direction |= EAST

            if not has_west_wall or west_wall(index) != WALL:
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


# find_seed()

print(mazeit(360))
draw()

maze = finish()
print(maze)

