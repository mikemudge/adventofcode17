
class Firewall(object):
    def __init__(self, idx, depth):
        self.idx = idx
        self.depth = depth

    def __repr__(self):
        return '%d: %d' % (self.idx, self.depth)

    def caught_at_time(self, t):
        return self.position_at_time(t) == 0

    def position_at_time(self, t):
        # Need to figure out the position of the scanner at t.
        position = t % (self.depth * 2 - 2)
        # Going backwards?
        if position >= self.depth:
            # E.g 2 should go 0, 1
            # 3 should go 0, 1, 2, 1
            # 4 should go 0, 1, 2, 3, 2, 1
            position = self.depth * 2 - 2 - position
        return position

def main():
    with open('input') as f:
        lines = f.readlines()

        layers = []
        max_a = 0
        for line in lines:
            a, b = line.split(': ')
            max_a = max(int(a), max_a)

        print max_a
        layers = [None] * (max_a + 1)
        for line in lines:
            a, b = line.split(': ')
            layers[int(a)] = Firewall(int(a), int(b))

        value = 0
        for l in layers:
            if not l:
                continue
            if l.caught_at_time(l.idx):
                value += l.idx * l.depth
                print 'Caught at', l
            else:
                print 'Missed at', l

        print 'Part 1:', value

        # Part 2 find, the lowest start time where you can avoid being caught?
        # Iterate up from 0 and check each layer is safe?
        # TODO This is not the most efficient way to eliminate these, but it is easier.
        # There will be an elimination pattern we could use. Something like prime factorization or combining layers of the same depth?

        # Remove missing layers to speed this up a little.
        real_layers = [l for l in layers if l]
        for i in range(10000000):
            caught = False
            for l in real_layers:
                if not l:
                    continue
                if l.caught_at_time(i + l.idx):
                    # print 'Caught at', i, l
                    caught = True
                    break
            if caught:
                continue
            print 'Part 2: ', i
            break


main()
