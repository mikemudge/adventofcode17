
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
                    print 'jump', jump
                    i += jump
                    # Prevent the normal i increment.
                    continue
            else:
                print ins
                raise Exception('Bad instruction')

            i += 1

        print registers
        print 'last_frequency', last_frequency

def getValue(reg, registers):
    if reg.lstrip('-').isdigit():
        return int(reg)
    else:
        return registers.setdefault(reg, 0)


main()
