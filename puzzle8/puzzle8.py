
def main():
    with open('input') as f:
        lines = f.readlines()

        registers = {}
        maxK2 = None
        maxV2 = 0

        for line in lines:
            print line

            parts = line.split()
            register = parts[0]
            instruction = parts[1]
            amount = int(parts[2])
            # if = parts[3]
            conditionRegister = parts[4]
            conditionCompare = parts[5]
            conditionValue = int(parts[6])

            registers.setdefault(conditionRegister, 0)
            registers.setdefault(register, 0)

            registerValue = registers[conditionRegister]
            print conditionRegister, registerValue, conditionCompare, conditionValue

            update = False
            if conditionCompare == '<' and registerValue < conditionValue:
                update = True
            if conditionCompare == '<=' and registerValue <= conditionValue:
                update = True
            if conditionCompare == '>' and registerValue > conditionValue:
                update = True
            if conditionCompare == '>=' and registerValue >= conditionValue:
                update = True
            if conditionCompare == '==' and registerValue == conditionValue:
                update = True
            if conditionCompare == '!=' and registerValue != conditionValue:
                update = True

            if instruction == 'inc' and update:
                registers[register] += amount
            if instruction == 'dec' and update:
                registers[register] -= amount

            for k, v in registers.items():
                if v > maxV2:
                    maxK2 = k
                    maxV2 = v

        maxK, maxV = registers.items()[0]
        for k, v in registers.items():
            print k, v
            if v > maxV:
                maxK = k
                maxV = v

        print 'Part 1: ', maxK, maxV
        print 'Part 2: ', maxK2, maxV2


main()
