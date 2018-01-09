with open('input') as f:
    lines = f.readlines()
    successes = 0
    successes2 = 0
    for line in lines:
        line = line[:-1]
        words = line.split()
        seenBefore = {}
        anagramSeen = {}
        fail = False
        fail2 = False
        for word in words:
            if seenBefore.get(word):
                fail = True
            seenBefore[word] = True

            orderedWord = ''.join(sorted(word))
            if anagramSeen.get(orderedWord):
                fail2 = True
            anagramSeen[orderedWord] = True

        if not fail:
            successes += 1

        if not fail2:
            successes2 += 1

    print('Part 1', successes)
    print('Part 2', successes2)
