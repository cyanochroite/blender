maze = []
grid = []
line = []
copy = []

cell_width = 75
cell_height = 50
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



def draw():
    print("=====================")
    index = 0
    for cell in maze:
        value = str(hex(cell))[2:3]
        if cell == WALL:
            value = "@"
        if cell == HOLE:
            value = " "
        if cell == 0:
            value = " "
        print(value, end="")
        index += 1
        if index % width == 0:
            print("")





def go_north(cell):
    value = cell - width - width
    return value


def go_south(cell):
    value = cell + width + width
    return value


def go_east(cell):
    value = cell + 1 + 1
    return value


def go_west(cell):
    value = cell - 1 - 1
    return value


def int_from_cell(cell):
    value = maze[cell]
    return value


def move(cell, direction):
    match direction:
        case 1:  # NORTH
            pick = go_north(cell)
        case 2:  # SOUTH
            pick = go_south(cell)
        case 4:  # EAST
            pick = go_east(cell)
        case 8:  # WEST
            pick = go_west(cell)
    return pick


def uncarved_neighbor(cell_start, direction):
    cell = move(cell_start, direction)
    value = grid[cell] # grid shows neighbors

    if direction & NORTH:
        maze[cell] &= UNSOUTH
    if direction & SOUTH:
        maze[cell] &= UNNORTH
    if direction & EAST:
        maze[cell] &= UNWEST
    if direction & WEST:
        maze[cell] &= UNEAST


    if value & NORTH:
        pick = go_north(cell)
        oppsite = UNSOUTH
        maze[pick] &= oppsite
    if value & SOUTH:
        pick = go_south(cell)
        oppsite = UNNORTH
        maze[pick] &= oppsite
    if value & EAST:
        pick = go_east(cell)
        oppsite = UNWEST
        maze[pick] &= oppsite
    if value & WEST:
        pick = go_west(cell)
        oppsite = UNEAST
        maze[pick] &= oppsite


def carve(cell, direction, insede=True):
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
    if insede:
        uncarved_neighbor(cell, direction)
    return move(cell, direction)


def carve_random(cell):
    direction = int_from_cell(cell)
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
    #direction = secrets.choice(choice)

    return carve(cell, direction)

import random
random.seed(7)
enter = random.randrange(0, cell_width)
exit = random.randrange(cell_size - cell_width, cell_size)

#import secrets
#enter = secrets.randbelow(cell_width)
#exit = secrets.randbelow(cell_width) + cell_size - cell_width

enter = line[enter]
exit = line[exit]

carve(enter, NORTH, False)
carve(exit, SOUTH, False)


def remove_from_list():
    length = len(line)
    index = random.randrange(length)
    cell = line[index]
    del line[index]
    return cell

fail = 100000
line = [enter]
cat = len(line)


def random_from_list():
    length = len(line)
    index = random.randrange(length)
    cell = line[index]
    return cell

def random_from_list2():
    length = len(line)
    change = 8
    if length > change:
        index = random.randrange(change)
    else:
        index = random.randrange(length)

    index = length - 1
    cell = line[index]
    return cell

while fail > 0 and cat > 0:
    fail -= 1
    #draw()
    
    cell = random_from_list()
    where = carve_random(cell)
    line.append(where)

    line = [item for item in line if maze[item] > 0]

    cat = len(line)

if fail <= 0:
    print("FAILFAILFAILFAILFAIL")

draw()


def count():
    count = 0
    for cell in copy:
        walls = 0
        walls += 1 if maze[cell - width] == WALL else 0
        walls += 1 if maze[cell + width] == WALL else 0
        walls += 1 if maze[cell + 1] == WALL else 0
        walls += 1 if maze[cell - 1] == WALL else 0
        count += 1 if walls == 3 else 0
    return count

print(fail)
print(count())
