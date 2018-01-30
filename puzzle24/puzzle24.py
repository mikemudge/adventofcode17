from heapq import heappush, heappop

class Port(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def other(self, v):
        if self.a == v:
            return self.b
        elif self.b == v:
            return self.a
        else:
            print v, self
            raise Exception('value not found')

    def __repr__(self):
        return '%d/%d' % (self.a, self.b)

    @classmethod
    def parse_from(cls, line):
        (a, b) = (map(int, line.split('/')))
        return Port(a, b)

class Path(object):
    def __init__(self, visited, value):
        self.visited = visited
        self.value = value

    def __repr__(self):
        return '%d - %d' % (len(self.visited), self.value)

def main():

    with open('input') as f:
        lines = f.readlines()

        values = [[] for x in range(100)]
        for line in lines:
            p = Port.parse_from(line)
            values[p.a].append(p)
            if p.b != p.a:
                values[p.b].append(p)
        print values

        starts = values[0]
        heap = []
        for v in starts:
            p = Path([v], v.b)
            heappush(heap, (-v.b, p))

        iterations = 0
        best = 0
        best_length = 0
        best_bridge_strength = 0
        while len(heap) > 0:
            (strength, next) = heappop(heap)
            # print strength, next
            best = min(strength, best)
            bridge_length = len(next.visited)
            if bridge_length == best_length:
                if strength < best_bridge_strength:
                    best_bridge_strength = strength
                    best_length = bridge_length
                # Check strength
            if bridge_length > best_length:
                best_bridge_strength = strength
                best_length = bridge_length

            for v in values[next.value]:
                if v not in next.visited:
                    # print 'adding', v
                    p = Path(next.visited[:] + [v], v.other(next.value))
                    value = strength - v.a - v.b
                    heappush(heap, (value, p))

            iterations += 1
            # print iterations, len(heap)

        print 'Part 1:', best

        print 'Part 2:', best_bridge_strength


main()
