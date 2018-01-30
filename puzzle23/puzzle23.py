
def main():

    with open('input') as f:
        lines = f.readlines()

        registers = {}

        i = 0
        count = 0
        iterations = 0
        while i < len(lines):
            iterations += 1
            if iterations % 1000 == 0:
                print iterations
            line = lines[i]
            parts = line.split()
            ins = parts[0]

            if ins == 'set':
                # Assign regX = Y
                x = parts[1]
                registers[x] = getValue(parts[2], registers)
            elif ins == 'sub':
                # Assign regX += Y
                x = parts[1]
                value = registers.setdefault(x, 0)
                registers[x] = value - getValue(parts[2], registers)
            elif ins == 'mul':
                # Assign regX *= Y
                x = parts[1]
                value = registers.setdefault(x, 0)
                registers[x] = value * getValue(parts[2], registers)
                count += 1
            elif ins == 'jnz':
                value = getValue(parts[1], registers)
                if value != 0:
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
        print 'Part 1:', count

        print 'Part 2:', part2()
        # 904 is too low

# Part 2 involves understanding the program and simplifying it.
def part2():
    c = 123700
    h = 0
    # The check for b == c is before the increment.
    for b in range(106700, c + 17, 17):
        for d in range(2, b):
            if b % d == 0:
                print b, d
                h += 1
                break
    return h

def getValue(reg, registers):
    if reg.lstrip('-').isdigit():
        return int(reg)
    else:
        return registers.setdefault(reg, 0)


main()
