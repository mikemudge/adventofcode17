class Update(object):
    def __init__(self, write, direction, next):
        self.write = write
        self.direction = direction
        self.next = next

    def __repr__(self):
        return '%d %s %s' % (self.write, '<-' if self.direction == -1 else '->', self.next)

def main():

    states = {
        'A': [
            Update(1, 1, 'B'),
            Update(0, -1, 'C'),
        ],
        'B': [
            Update(1, -1, 'A'),
            Update(1, -1, 'D'),
        ],
        'C': [
            Update(1, 1, 'D'),
            Update(0, 1, 'C'),
        ],
        'D': [
            Update(0, -1, 'B'),
            Update(0, 1, 'E'),
        ],
        'E': [
            Update(1, 1, 'C'),
            Update(1, -1, 'F'),
        ],
        'F': [
            Update(1, -1, 'E'),
            Update(1, 1, 'A'),
        ]
    }
    diagnostic_iterations = 12172063
    print states
    state = 'A'
    current_index = 0
    tape = {}
    print diagnostic_iterations
    for iteration in range(diagnostic_iterations):
        if iteration % 1000 == 0:
            print iteration, state
        val = tape.setdefault(current_index, 0)
        update = states[state][val]
        tape[current_index] = update.write
        current_index += update.direction
        state = update.next

    print 'Part 1', sum(tape.values())


main()
