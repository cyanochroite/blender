grid = []
line = []

cell_width = 3
cell_height = 4
cell_size = cell_width * cell_height

width = cell_width * 2 + 1
height = cell_height * 2 + 1
size = width * height


NORTH = 1 << 0
SOUTH = 1 << 1
EAST = 1 << 2
WEST = 1 << 3

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
    f = str(hex(c))[2:3]
    grid.append(f if space else "#")
    if space:
        line.append(cell)


maze = grid


def draw():
    index = 0
    for cell in maze:
        print(cell, end="")
        index += 1
        if index % width == 0:
            print("")


print("=====================")

import random
random.seed(0)


def carve(cell, direction):
    pick = 0
    frog = line[cell]
    match direction:
        case 1:
            pick = frog - width
        case 2:
            pick = frog + width
        case 4:
            pick = frog + 1
        case 8:
            pick = frog - 1
    maze[frog] = " "
    maze[pick] = " "


enter = random.randrange(0, cell_width)
exit = random.randrange(cell_size - cell_width, cell_size)

carve(enter, NORTH)
carve(exit, SOUTH)

cat = len(line)
print(line)
for index in range(cat):
    cat = len(line)
    rando = random.randrange(cat)
    lookup = line[rando]
    thing = maze[lookup]
    del line[rando]
    print(cat, rando, lookup, thing, line)


draw()
