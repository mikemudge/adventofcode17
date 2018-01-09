with open('input') as f:
    lines = f.readlines()

    values = map(int, lines[0].split())

    print values

    registers = len(values)

    visited = {}

    ii = 0
    while(True):
        ii += 1
        idx = 0
        high = values[0]
        for i in range(registers):
            if values[i] > high:
                idx = i
                high = values[i]

        # redistibute.
        rem = high % registers
        add = high / registers
        values[idx] = 0
        for i in range(registers):
            values[i] += add
        for i in range(idx + 1, idx + rem + 1):
            values[i % registers] += 1

        # An easy but inefficient hash function.
        key = ''.join(map(str, values))

        if visited.get(key):
            break

        visited[key] = ii
    print 'Part 1', ii
    print 'Part 2', ii - visited.get(key)
