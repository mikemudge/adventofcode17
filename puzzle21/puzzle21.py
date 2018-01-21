class Pattern(object):

    def __init__(self, rows):
        self.rows = rows
        self.key = ''.join(self.rows)

    def __repr__(self):
        return '%s' % self.rows

    @classmethod
    def parse_from_string(cls, data):
        return Pattern(data.split('/'))

    def get_keys(self):
        # return rotate and flipped versions.
        keys = []
        key = self.rows
        keys.append(''.join(key))
        # Add the 3 rotations.
        for i in range(3):
            key = self.rotate(key)
            keys.append(''.join(key))

        # Now add the flipped version and its rotations.
        key = self.rows[::-1]
        keys.append(''.join(key))
        # Add the 3 rotations.
        for i in range(3):
            key = self.rotate(key)
            keys.append(''.join(key))

        return keys

    # Rotates a 2d array clockwise by 90 degrees.
    def rotate(self, pattern):
        # Keeps each row as a string.
        return [''.join(a) for a in zip(*pattern[::-1])]

def iterate(pattern, pattern_map):
    if len(pattern) % 2 == 0:
        size = 2
        patterns = len(pattern) / 2
    else:
        size = 3
        patterns = len(pattern) / 3

    # Need to pre make this the right size?
    next_pattern = ['' for i in range(len(pattern) + patterns)]
    for y in range(0, len(pattern) / size):
        for x in range(0, len(pattern), size):
            # Inject result into next_pattern
            key = ''.join([pattern[y * size + i][x:x + size] for i in range(size)])
            result = pattern_map[key].rows
            for i in range(size + 1):
                next_pattern[y * (size + 1) + i] += result[i]

    return next_pattern


def main():

    with open('input') as f:
        lines = f.readlines()

        pattern_map = {}
        for line in lines:
            if line != lines[len(lines) - 1]:
                line = line[:-1]

            (pattern, result) = line.split(' => ')
            pattern = Pattern.parse_from_string(pattern)

            enhancement = Pattern.parse_from_string(result)

            print 'Pattern input =', pattern.key
            for key in pattern.get_keys():
                print key
                pattern_map[key] = enhancement

        for k, pattern in pattern_map.items():
            print k, '=>', pattern.rows

        initial_pattern = Pattern(['.#.', '..#', '###'])

        # iterate on current pattern matching for 5 iterations.
        pattern = initial_pattern.rows

        # when the input is 6x6 it should split into 2x2 not 3x3 as it currently is doing.
        # Will need to join the grids and then seperate them after each iteration.

        for iteration in range(5):
            print 'Iteration', iteration + 1
            print '\n'.join(pattern)
            print len(pattern)
            pattern = iterate(pattern, pattern_map)

        print 'Result'
        print '\n'.join(pattern)
        print len(pattern)

        count = 0
        for row in pattern:
            for a in row:
                if a == '#':
                    count += 1
                elif a != '.':
                    raise Exception('Bad value')

        print 'Part 1', count
        # 121 is too low
        # 152 right

        for iteration in range(5, 18):
            print 'Iteration', iteration + 1
            print '\n'.join(pattern)
            print len(pattern)
            pattern = iterate(pattern, pattern_map)

        print 'Result'
        print '\n'.join(pattern)
        print len(pattern)

        count = 0
        for row in pattern:
            for a in row:
                if a == '#':
                    count += 1
                elif a != '.':
                    raise Exception('Bad value')

        print 'Part 2', count


main()
