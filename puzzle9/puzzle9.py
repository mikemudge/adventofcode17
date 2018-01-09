
class Group(object):
    def __init__(self, parent):
        self.parent = parent
        self.groups = []
        self.garbageLength = 0

    def __repr__(self):
        return '{%s}' % ''.join(map(str, self.groups))

def main():
    with open('input') as f:
        lines = f.readlines()

        group = groupParse(lines[0])

        score = calculateScore(group, 1)

        print 'Part 1', score
        # 11866 is too high.

        print 'Part 2', calculateGarbageLength(group)

def groupParse(values):
    group = Group(None)
    garbage = False
    ignore = False
    # Remove the { and } from the first group
    values = values[1:-1]
    for i in range(len(values)):
        if ignore:
            ignore = False
            continue

        if values[i] == '!':
            # The next value is ignored.
            ignore = True
            continue

        if garbage:
            # Only accept >
            if values[i] == '>':
                garbage = False
            else:
                group.garbageLength += 1
            continue

        if values[i] == '<':
            garbage = True
            continue

        if values[i] == '{':
            # start new group
            new_group = Group(group)
            group.groups.append(new_group)
            group = new_group
            continue

        if values[i] == '}':
            # group is complete
            if not group.parent:
                raise Exception('No parent for %d of %d' % (i, len(values)))
            group = group.parent
            continue
    return group

def calculateScore(group, value):
    score = value
    for g in group.groups:
        score += calculateScore(g, value + 1)
    return score

def calculateGarbageLength(group):
    garbageLength = group.garbageLength
    for g in group.groups:
        garbageLength += calculateGarbageLength(g)
    return garbageLength


main()
