class Direction(object):

    def __init__(self, dx, dy, name):
        self.dx = dx
        self.dy = dy
        self.name = name

    def __repr__(self):
        return self.name

    def left(self):
        if self == NORTH:
            return WEST
        elif self == WEST:
            return SOUTH
        elif self == SOUTH:
            return EAST
        else:
            return NORTH

    def right(self):
        if self == NORTH:
            return EAST
        elif self == EAST:
            return SOUTH
        elif self == SOUTH:
            return WEST
        else:
            return NORTH


NORTH = Direction(0, -1, 'North')
SOUTH = Direction(0, 1, 'South')
EAST = Direction(1, 0, 'East')
WEST = Direction(-1, 0, 'West')

def main():

    with open('input') as f:
        lines = f.readlines()

        size = 500
        grid = [[None for x in range(size)] for y in range(size)]
        count = 0
        print len(lines)

        # Test lines
        # lines = [
        #     '..#\n',
        #     '#..\n',
        #     '...',
        # ]
        sy = (len(grid) - len(lines)) / 2
        sx = (len(grid[0]) - len(lines[0])) / 2

        for y, line in enumerate(lines):
            if line != lines[len(lines) - 1]:
                line = line[:-1]

            for x, v in enumerate(line):
                print x, y, v
                grid[sy + y][sx + x] = v

        print '\n'.join([''.join([v if v else '.' for v in row[size / 2 - 20:size / 2 + 20]]) for row in grid[size / 2 - 20:size / 2 + 20]])

        x = (len(grid[0]) - 1) / 2
        y = (len(grid) - 1) / 2
        d = NORTH
        # Iterate x, y turning as virus is created or destroyed?
        for i in range(10000):
            # Turn left if clean
            print x, y
            if grid[y][x] != '#':
                d = Direction.left(d)
                count += 1
                grid[y][x] = '#'
            else:
                d = Direction.right(d)
                grid[y][x] = '.'
            x += d.dx
            y += d.dy

            if i in [0, 1, 69]:
                print 'Iteration', i
                print '\n'.join([''.join([v if v else '.' for v in row[size / 2 - 20:size / 2 + 20]]) for row in grid[size / 2 - 20:size / 2 + 20]])

        print 'Part 1:', count


main()
