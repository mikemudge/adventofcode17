from collections import deque

def main():

    with open('input') as f:
        lines = f.readlines()

        registers = {}

        last_frequency = 0

        i = 0
        while i < len(lines):
            line = lines[i]
            parts = line.split()
            ins = parts[0]

            print i, ins

            if ins == 'snd':
                last_frequency = getValue(parts[1], registers)
                print 'play sound', last_frequency
            elif ins == 'set':
                # Assign regX = Y
                x = parts[1]
                registers[x] = getValue(parts[2], registers)
            elif ins == 'add':
                # Assign regX += Y
                x = parts[1]
                value = registers.setdefault(x, 0)
                registers[x] = value + getValue(parts[2], registers)
            elif ins == 'mul':
                # Assign regX *= Y
                x = parts[1]
                value = registers.setdefault(x, 0)
                registers[x] = value * getValue(parts[2], registers)
            elif ins == 'mod':
                # Assign regX %= Y
                x = parts[1]
                value = registers.setdefault(x, 0)
                registers[x] = value % getValue(parts[2], registers)
            elif ins == 'rcv':
                x = parts[1]
                value = registers.setdefault(x, 0)
                # Recover?
                if value != 0:
                    break
            elif ins == 'jgz':
                x = parts[1]
                value = registers.setdefault(x, 0)
                if value > 0:
                    # Jump by some number of instructions?
                    jump = getValue(parts[2], registers)
                    i += jump
                    # Prevent the normal i increment.
                    continue
            else:
                print ins
                raise Exception('Bad instruction')

            i += 1

        print registers
        print 'Part 1:', last_frequency

        # Part 2
        program1_idx = 0
        program2_idx = 0
        registers1 = {'p': 0}
        registers2 = {'p': 1}
        messages1 = deque([])
        messages2 = deque([])

        count = 0
        while True:
            (d1, _) = parse_instruction(lines[program1_idx], registers1, messages1, messages2)
            (d2, sent) = parse_instruction(lines[program2_idx], registers2, messages2, messages1)
            if d1 == 0 and d2 == 0:
                print 'DEADLOCK'
                break

            if sent:
                count += 1

            print 'jump', d1, d1, len(messages1), len(messages2)

            program1_idx += d1
            program2_idx += d2

        print registers1
        print registers2
        print 'Part 2:', count
        # 6985 too high, was counting messages sent from the wrong program.


def parse_instruction(line, registers, message_in, message_out):
    parts = line.split()
    ins = parts[0]

    if ins == 'snd':
        value = getValue(parts[1], registers)
        message_out.append(value)
        return 1, True
    elif ins == 'set':
        # Assign regX = Y
        x = parts[1]
        registers[x] = getValue(parts[2], registers)
    elif ins == 'add':
        # Assign regX += Y
        x = parts[1]
        value = registers.setdefault(x, 0)
        registers[x] = value + getValue(parts[2], registers)
    elif ins == 'mul':
        # Assign regX *= Y
        x = parts[1]
        value = registers.setdefault(x, 0)
        registers[x] = value * getValue(parts[2], registers)
    elif ins == 'mod':
        # Assign regX %= Y
        x = parts[1]
        value = registers.setdefault(x, 0)
        registers[x] = value % getValue(parts[2], registers)
    elif ins == 'rcv':
        if len(message_in) == 0:
            # Nothing to consume, wait and don't move forward an instruction.
            return 0, False
        value = message_in.popleft()
        x = parts[1]
        registers[x] = value
    elif ins == 'jgz':
        value = getValue(parts[1], registers)
        if value > 0:
            # Jump by some number of instructions?
            jump = getValue(parts[2], registers)
            return jump, False
    else:
        print ins
        raise Exception('Bad instruction')

    return 1, False

def getValue(reg, registers):
    if reg.lstrip('-').isdigit():
        return int(reg)
    else:
        return registers.setdefault(reg, 0)


main()
