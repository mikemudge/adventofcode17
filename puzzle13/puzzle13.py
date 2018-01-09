
class Firewall(object):
    def __init__(self, idx, depth):
        self.idx = idx
        self.depth = depth

    def __repr__(self):
        return '%d: %d' % (self.idx, self.depth)

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

        for l in layers:
            print l


main()
