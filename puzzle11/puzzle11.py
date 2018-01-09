

def main():
    with open('input') as f:
        lines = f.readlines()
        path = lines[0].lower().split(',')

        print path

        # start at 0,0
        x = 0
        y = 0
        i = 0
        max_d = 0
        # Represent hexes as a square grid.
        for step in path:
            if step == 'n':
                y -= 1
            elif step == 's':
                y += 1
            elif step == 'ne':
                if x % 2 == 0:
                    # when on an even column, moving ne goes up a row.
                    y -= 1
                x += 1
            elif step == 'se':
                if x % 2 == 1:
                    # when on an odd column, moving se goes down a row.
                    y += 1
                x += 1
            elif step == 'nw':
                if x % 2 == 0:
                    # when on an even column, moving nw goes up a row.
                    y -= 1
                x -= 1
            elif step == 'sw':
                if x % 2 == 1:
                    # when on an odd column, moving sw goes down a row.
                    y += 1
                x -= 1

            print '%s: %s' % (str(i), step)
            print x, y
            # i += 1
            # if i > 10:
            #     break
            x2, y2, z2 = oddq_to_cube(x, y)
            d = (abs(x2) + abs(y2) + abs(z2)) / 2
            if d > max_d:
                max_d = d

        x1, y1, z1 = oddq_to_cube(x, y)
        distance = (abs(x1) + abs(y1) + abs(z1)) / 2

        print 'Part 1: %s' % distance
        print 'Part 1: %s' % max_d

def oddq_to_cube(col, row):
    x = col
    z = row - (col - (col & 1)) / 2
    y = -x - z

    return x, y, z


main()
