with open('input') as f:
    lines = f.readlines()
    values = map(int, lines)
    values2 = map(int, lines)

    steps = 0
    i = 0
    totalInstructions = len(values)
    while i < totalInstructions:
        jump = values[i]
        values[i] += 1
        i += jump
        steps += 1

    steps2 = 0
    i = 0
    while i < totalInstructions:
        jump = values2[i]
        if values2[i] < 3:
            values2[i] += 1
        else:
            values2[i] -= 1
        i += jump
        steps2 += 1

    print 'Part 1', steps
    print 'Part 2', steps2
