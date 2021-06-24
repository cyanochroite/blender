limit = 65536
b0 = 0b0000000000000001
b1 = 0b0000000000000010
b2 = 0b0000000000000100
b3 = 0b0000000000001000
b4 = 0b0000000000010000
b5 = 0b0000000000100000
b6 = 0b0000000001000000
b7 = 0b0000000010000000
b8 = 0b0000000100000000
b9 = 0b0000001000000000
bA = 0b0000010000000000
bB = 0b0000100000000000
bC = 0b0001000000000000
bD = 0b0010000000000000
bE = 0b0100000000000000
bF = 0b1000000000000000

book = {}

if False:
    for x in range(limit):
        book[x] = []

    if book[0]:
        print("hi")

    book[1].append(5)
    book[1].append(3)
    book[4].append(54)

    if book[1]:
        print("hooi")
    print(book)

    for index in range(limit):
        if book[index]:
            print(book[index])


def moo0(bit):
    # do nothing
    new = 0
    if bit & b0:
        new |= b0
    if bit & b1:
        new |= b1
    if bit & b2:
        new |= b2
    if bit & b3:
        new |= b3
    if bit & b4:
        new |= b4
    if bit & b5:
        new |= b5
    if bit & b6:
        new |= b6
    if bit & b7:
        new |= b7
    if bit & b8:
        new |= b8
    if bit & b9:
        new |= b9
    if bit & bA:
        new |= bA
    if bit & bB:
        new |= bB
    if bit & bC:
        new |= bC
    if bit & bD:
        new |= bD
    if bit & bE:
        new |= bE
    if bit & bF:
        new |= bF
    return new


def moo1(bit):
    # rotate CC 90
    new = 0
    if bit & b0:
        new |= bC
    if bit & b1:
        new |= b8
    if bit & b2:
        new |= b4
    if bit & b3:
        new |= b0
    if bit & b4:
        new |= bD
    if bit & b5:
        new |= b9
    if bit & b6:
        new |= b5
    if bit & b7:
        new |= b1
    if bit & b8:
        new |= bE
    if bit & b9:
        new |= bA
    if bit & bA:
        new |= b6
    if bit & bB:
        new |= b2
    if bit & bC:
        new |= bF
    if bit & bD:
        new |= bB
    if bit & bE:
        new |= b7
    if bit & bF:
        new |= b3
    return new


def moo2(bit):
    # rotate CC 180
    new = 0
    if bit & b0:
        new |= bF
    if bit & b1:
        new |= bE
    if bit & b2:
        new |= bD
    if bit & b3:
        new |= bC
    if bit & b4:
        new |= bB
    if bit & b5:
        new |= bA
    if bit & b6:
        new |= b9
    if bit & b7:
        new |= b8
    if bit & b8:
        new |= b7
    if bit & b9:
        new |= b6
    if bit & bA:
        new |= b5
    if bit & bB:
        new |= b4
    if bit & bC:
        new |= b3
    if bit & bD:
        new |= b2
    if bit & bE:
        new |= b1
    if bit & bF:
        new |= b0
    return new


def moo3(bit):
    # rotate CC 270
    new = 0
    if bit & b0:
        new |= b3
    if bit & b1:
        new |= b7
    if bit & b2:
        new |= bB
    if bit & b3:
        new |= bF
    if bit & b4:
        new |= b2
    if bit & b5:
        new |= b6
    if bit & b6:
        new |= bA
    if bit & b7:
        new |= bE
    if bit & b8:
        new |= b1
    if bit & b9:
        new |= b5
    if bit & bA:
        new |= b9
    if bit & bB:
        new |= bD
    if bit & bC:
        new |= b0
    if bit & bD:
        new |= b4
    if bit & bE:
        new |= b8
    if bit & bF:
        new |= bC
    return new


def moo4(bit):
    # flip X
    new = 0
    if bit & b0:
        new |= b3
    if bit & b1:
        new |= b2
    if bit & b2:
        new |= b1
    if bit & b3:
        new |= b0
    if bit & b4:
        new |= b7
    if bit & b5:
        new |= b6
    if bit & b6:
        new |= b5
    if bit & b7:
        new |= b4
    if bit & b8:
        new |= bB
    if bit & b9:
        new |= bA
    if bit & bA:
        new |= b9
    if bit & bB:
        new |= b8
    if bit & bC:
        new |= bF
    if bit & bD:
        new |= bE
    if bit & bE:
        new |= bD
    if bit & bF:
        new |= bC
    return new


def moo5(bit):
    # flix X rotate CC 90
    new = 0
    if bit & b0:
        new |= bF
    if bit & b1:
        new |= bB
    if bit & b2:
        new |= b7
    if bit & b3:
        new |= b3
    if bit & b4:
        new |= bE
    if bit & b5:
        new |= bA
    if bit & b6:
        new |= b6
    if bit & b7:
        new |= b2
    if bit & b8:
        new |= bD
    if bit & b9:
        new |= b9
    if bit & bA:
        new |= b5
    if bit & bB:
        new |= b1
    if bit & bC:
        new |= bC
    if bit & bD:
        new |= b8
    if bit & bE:
        new |= b4
    if bit & bF:
        new |= b0
    return new


def moo6(bit):
    new = 0
    if bit & b0:
        new |= bC
    if bit & b1:
        new |= bD
    if bit & b2:
        new |= bE
    if bit & b3:
        new |= bF
    if bit & b4:
        new |= b8
    if bit & b5:
        new |= b9
    if bit & b6:
        new |= bA
    if bit & b7:
        new |= bB
    if bit & b8:
        new |= b4
    if bit & b9:
        new |= b5
    if bit & bA:
        new |= b6
    if bit & bB:
        new |= b7
    if bit & bC:
        new |= b0
    if bit & bD:
        new |= b1
    if bit & bE:
        new |= b2
    if bit & bF:
        new |= b3
    return new


def moo7(bit):
    new = 0
    if bit & b0:
        new |= b0
    if bit & b1:
        new |= b4
    if bit & b2:
        new |= b8
    if bit & b3:
        new |= bC
    if bit & b4:
        new |= b1
    if bit & b5:
        new |= b5
    if bit & b6:
        new |= b9
    if bit & b7:
        new |= bD
    if bit & b8:
        new |= b2
    if bit & b9:
        new |= b6
    if bit & bA:
        new |= bA
    if bit & bB:
        new |= bE
    if bit & bC:
        new |= b3
    if bit & bD:
        new |= b7
    if bit & bE:
        new |= bB
    if bit & bF:
        new |= bF
    return new


test = False
if test:
    for index in range(limit):
        assert(moo0(index) == index)

    for index in range(limit):
        assert(moo1(moo1(moo1(moo1(index)))) == moo0(index))

    for index in range(limit):
        assert(moo2(index) == moo1(moo1(index)))

    for index in range(limit):
        assert(moo3(index) == moo1(moo2(index)))

    for index in range(limit):
        assert(moo4(index) == moo4(moo0(index)))

    for index in range(limit):
        assert(moo5(index) == moo4(moo1(index)))

    for index in range(limit):
        assert(moo6(index) == moo4(moo2(index)))

    for index in range(limit):
        assert(moo7(index) == moo4(moo3(index)))


if False:
    # find all super symetry objects
    cool = []
    for index in range(limit):
        if moo0(index) == moo1(index) == moo2(index) == moo3(index) == moo4(index) == moo5(index) == moo6(index) == moo7(index):
            cool.append(index)
    print(cool)


# setup
grid2d = []
X = 8 * 4
Y = 8 * 4
for y in range(Y):
    grid1d = []
    for x in range(X):
        grid1d.append(0)
    grid2d.append(grid1d)


# prestuff
def output(z):
    if z > 0:
        return 'X'
    else:
        return 'O'


def make_block(z, b):
    return ((((z & b) > 0) * 2) - 1)


def can_insert_block(x, y, z, b):
    return grid2d[y][x] == make_block(z, b)


def can_insert_tile(x, y, z):
    w = True
    w &= can_insert_block(x + 0, y + 0, z, b0)
    w &= can_insert_block(x + 1, y + 0, z, b1)
    w &= can_insert_block(x + 2, y + 0, z, b2)
    w &= can_insert_block(x + 3, y + 0, z, b3)
    w &= can_insert_block(x + 0, y + 1, z, b4)
    w &= can_insert_block(x + 1, y + 1, z, b5)
    w &= can_insert_block(x + 2, y + 1, z, b6)
    w &= can_insert_block(x + 3, y + 1, z, b7)
    w &= can_insert_block(x + 0, y + 2, z, b8)
    w &= can_insert_block(x + 1, y + 2, z, b9)
    w &= can_insert_block(x + 2, y + 2, z, bA)
    w &= can_insert_block(x + 3, y + 2, z, bB)
    w &= can_insert_block(x + 0, y + 3, z, bC)
    w &= can_insert_block(x + 1, y + 3, z, bD)
    w &= can_insert_block(x + 2, y + 3, z, bE)
    w &= can_insert_block(x + 3, y + 3, z, bF)
    return w


def insert_block(x, y, z, b):
    grid2d[y][x] = make_block(z, b)


def insert_tile(x, y, z):
    insert_block(x + 0, y + 0, z, b0)
    insert_block(x + 1, y + 0, z, b1)
    insert_block(x + 2, y + 0, z, b2)
    insert_block(x + 3, y + 0, z, b3)
    insert_block(x + 0, y + 1, z, b4)
    insert_block(x + 1, y + 1, z, b5)
    insert_block(x + 2, y + 1, z, b6)
    insert_block(x + 3, y + 1, z, b7)
    insert_block(x + 0, y + 2, z, b8)
    insert_block(x + 1, y + 2, z, b9)
    insert_block(x + 2, y + 2, z, bA)
    insert_block(x + 3, y + 2, z, bB)
    insert_block(x + 0, y + 3, z, bC)
    insert_block(x + 1, y + 3, z, bD)
    insert_block(x + 2, y + 3, z, bE)
    insert_block(x + 3, y + 3, z, bF)


def count_blanks():
    count = 0
    for y in range(Y):
        for x in range(X):
            if grid2d[y][x] == ' ':
                count += 1
    return count


# work
insert_tile(1, 2, 38505)
# display
for y in range(Y - 1, -1, -1):
    print('|', end='')
    for x in range(X):
        z = grid2d[y][x]
        o = '.'
        if z > 0:
            o = 'X'
        if z < 0:
            o = 'O'
        print(o, end='')
    print('|')

print(count_blanks())
print(can_insert_tile(1, 2, 0))
print(can_insert_tile(1, 2, 38505))

print((15 > 1) * 2 - 1)
# w |= grid2d[y + 0][x + 0] == (z & b0) > 0
