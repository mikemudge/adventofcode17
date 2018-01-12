
def main():

    key_input = 'jxqlasbh'

    used = 0
    grid = []
    for i in range(128):
        row = []
        grid.append(row)
        hex_value = create_hash('%s-%d' % (key_input, i))
        for c in hex_value:
            v = int(c, 16)
            row.append(v & 8 == 8)
            row.append(v & 4 == 4)
            row.append(v & 2 == 2)
            row.append(v & 1 == 1)
            used += bin(int(c, 16)).count("1")

    # Print as a #. map?
    print 'Part 1:', used

    visited = [[None] * 128 for i in range(128)]

    x = 0
    y = 0
    if visited[y][x]:
        print 'hi'

    group_count = 0
    for y, row in enumerate(grid):
        print y
        for x, v in enumerate(row):
            if not visited[y][x] and v:
                # Start a new group.
                group_count += 1
                # Find neighbours
                broadcast(grid, visited, group_count, x, y)

    print 'Part 2:', group_count
    # 1235 is too high

    for row in visited:
        print ''.join([((str(v % 10) if v > 1230 else '*') if v else '.') for v in row])


def broadcast(grid, visited, group, x, y):
    if x < 0 or y < 0 or x >= 128 or y >= 128:
        # Out of bounds of grid.
        return
    if visited[y][x]:
        return
    if not grid[y][x]:
        # Not a used square, so can't be part of a region.
        return

    # Mark yourself as visited, and track which group you are in.
    visited[y][x] = group

    # Now visit neighbours and update them.
    broadcast(grid, visited, group, x + 1, y)
    broadcast(grid, visited, group, x - 1, y)
    broadcast(grid, visited, group, x, y + 1)
    broadcast(grid, visited, group, x, y - 1)

def create_hash(value):
    return full_knot_hash(value)

def full_knot_hash(value):

    parts = [ord(c) for c in value]

    # Just because the problem says to add these.
    parts += [17, 31, 73, 47, 23]

    skip = 0
    currentIdx = 0
    values = None
    for i in range(64):
        (currentIdx, skip, values) = knot_hash(parts, skip=skip, currentIdx=currentIdx, values=values)

    dense_hash = []
    for i in range(16):
        dense = 0
        for ii in range(16):
            dense ^= values[i * 16 + ii]
        dense_hash.append(dense)

    result = ''.join(format(d, '02x') for d in dense_hash)
    return result

def knot_hash(parts, currentIdx=0, skip=0, values=None):
    if not values:
        values = range(256)

    for p in parts:
        values = rotate(values, currentIdx)
        # reverse the first p numbers.
        # print values[:p]
        values[:p] = values[:p][::-1]
        # rotate back to 0 based.
        values = rotate(values, -currentIdx)

        currentIdx = (currentIdx + p + skip) % len(values)
        skip += 1

    return currentIdx, skip, values

def rotate(l, n):
    return l[n:] + l[:n]


main()
