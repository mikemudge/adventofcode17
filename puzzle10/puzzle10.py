

def main():
    with open('input') as f:
        lines = f.readlines()

        parts = map(int, lines[0].split(','))

        (_, _, values) = knot_hash(parts)

        print 'Part 1', values[0] * values[1]
        # 60270 was too high.
        # 2352 was too low.
        # 9288 is wrong.
        # 16256 is wrong.
        # 4114 is right. 121 * 34

        # Part 2, read line as ascii bytes instead
        print lines[0]

        # for testing
        print full_knot_hash('')
        print full_knot_hash('AoC 2017')
        print full_knot_hash('1,2,3')
        print full_knot_hash('1,2,4')

        print full_knot_hash(lines[0])

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
