
def main():

    gen_a_input = 722
    gen_b_input = 354
    gen_a_multiplier = 16807
    gen_b_multiplier = 48271
    size = 40000000

    # Part 2
    size2 = 5000000

    # Test input
    # gen_a_input = 65
    # gen_b_input = 8921
    # size = 5

    # Iterate and check bits.

    gen_a_value = gen_a_input
    gen_b_value = gen_b_input
    count = 0
    for i in range(size):
        if size < 100 or i % (size / 100) == 0:
            print str(i * 100 / size) + '%', i

        # This can most likely be made more efficient if we can use binary operators?
        gen_a_value = (gen_a_value * gen_a_multiplier) % 2147483647
        gen_b_value = (gen_b_value * gen_b_multiplier) % 2147483647

        if gen_a_value & 0xFFFF == gen_b_value & 0xFFFF:
            count += 1
            print i
            print format(gen_a_value, '#034b')
            print format(gen_b_value, '#034b')

    gen_a_value2 = gen_a_input
    gen_b_value2 = gen_b_input
    count2 = 0

    for i in range(size2):
        if size2 < 100 or i % (size2 / 100) == 0:
            print str(i * 100 / size2) + '%', i

        gen_a_value2 = (gen_a_value2 * gen_a_multiplier) % 2147483647
        gen_b_value2 = (gen_b_value2 * gen_b_multiplier) % 2147483647
        # Generate until it finds a multiple of 4
        while gen_a_value2 & 0b11 != 0:
            gen_a_value2 = (gen_a_value2 * gen_a_multiplier) % 2147483647

        # Generate until it finds a multiple of 8
        while gen_b_value2 & 0b111 != 0:
            gen_b_value2 = (gen_b_value2 * gen_b_multiplier) % 2147483647

        if gen_a_value2 & 0xFFFF == gen_b_value2 & 0xFFFF:
            count2 += 1
            print i
            print format(gen_a_value2, '#034b')
            print format(gen_b_value2, '#034b')

    print 'Part 1:', count
    print 'Part 2:', count2


main()
