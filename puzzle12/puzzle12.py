
class Program(object):
    def __init__(self, idx):
        self.idx = idx
        self.pipes_to = []

    def __repr__(self):
        return '%d' % self.idx

def main():
    with open('input') as f:
        lines = f.readlines()

        programs = []
        for i, line in enumerate(lines):
            a, b = line.split(' <-> ')
            if str(i) != a:
                raise Exception('no match')
            programs.append(Program(i))

        print 'Every Program has an i'

        for i, line in enumerate(lines):
            pipes = line.split(' <-> ')[1].split(', ')

            for pipe in pipes:
                programs[i].pipes_to.append(programs[int(pipe)])

        for p in programs:
            print p, '<->', ', '.join(map(str, p.pipes_to))

        # start at 0 and find all programs.
        visited = [None] * 2000
        visit_all(programs[0], visited)

        cnt = 0
        for v in visited:
            if v:
                cnt += 1

        print 'Part 1:', cnt

        groups = 1
        while True:
            p2 = next_unvisited_idx(visited)
            if not p2:
                break

            groups += 1
            visit_all(programs[p2], visited)

        print 'Part 2:', groups
        # 178 is too low.

def visit_all(start, visited):
    to_visit = [start]
    while len(to_visit) > 0:
        n = to_visit.pop()
        visited[n.idx] = True
        for p in n.pipes_to:
            if visited[p.idx]:
                continue
            to_visit.append(p)

def next_unvisited_idx(visited):
    for i, v in enumerate(visited):
        if not v:
            return i

    return None


main()
