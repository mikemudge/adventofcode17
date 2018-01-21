class Direction(object):

    def __init__(self, dx, dy, name):
        self.dx = dx
        self.dy = dy
        self.name = name

    def __repr__(self):
        return self.name


NORTH = Direction(0, -1, 'North')
SOUTH = Direction(0, 1, 'South')
EAST = Direction(1, 0, 'East')
WEST = Direction(-1, 0, 'West')

def main():

    with open('input') as f:
        lines = f.readlines()

        # Need to find where the line starts.
        x = -1
        y = 0
        for i, letter in enumerate(lines[0]):
            if letter == '|':
                x = i

        d = SOUTH
        print 'start', x, y, d

        print 'grid %dx%d' % (len(lines[0]), len(lines))

        values = []
        steps = 0

        while True:
            # Move
            x += d.dx
            y += d.dy
            steps += 1

            # Check location for a change of direction.
            loc = lines[y][x]
            if loc == '+':
                # Turn
                if d == NORTH or d == SOUTH:
                    # Check east and west. for a -
                    if x > 0 and lines[y][x - 1] == '-':
                        d = WEST
                    elif lines[y][x + 1] == '-':
                        d = EAST
                    else:
                        print 'Got stuck at', x, y
                        break
                else:
                    # Check up and down for a |
                    if y > 0 and x < len(lines[y - 1]) and lines[y - 1][x] == '|':
                        d = NORTH
                    elif lines[y + 1][x] == '|':
                        d = SOUTH
                    else:
                        print 'Got stuck at', x, y
                        break
                # print 'turned', d, 'at', x, y
            elif loc != '|' and loc != '-':
                print 'found', loc, 'at', x, y
                if loc == ' ':
                    # End of the line.
                    break
                values.append(loc)

        print 'ended at', x, y, d
        print 'Part 1:', ''.join(values)

        # We skip the first step into the grid, but also count the last step off the end of the line so steps is accurate.
        print 'Part 2:', steps


main()
