grid = []
line = []

width = 3
height = 3

width = width * 2 +1
height = height * 2+1
size = width * height


NORTH = 1 << 0
SOUTH = 1 << 1
EAST = 1 << 2
WEST = 1 << 3


for cell in range(size):
    if cell == 12:
        pass
    x = cell % width
    y = cell // width
    odd_x = x % 2
    odd_y = y % 2
    space = odd_x and odd_y
    n = cell - width >= 0
    s = cell + width < size
    e = x - 1 >= 0
    w = x + 1 < width
    c = 0
    c |= NORTH if n else 0
    c |= SOUTH if s else 0
    c |= EAST if e else 0
    c |= WEST if w else 0
    f = str(hex(c))[2:3]
    grid.append(f if c else "+")

maze = grid
index = 0
for cell in maze:
    print(cell, end="")
    index += 1
    if index % width == 0:
        print("")



