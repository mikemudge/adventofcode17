
def main():
    steps = 349

    # For testing.
    # steps = 3

    values = [0]
    current_position = 0

    print steps

    for i in range(2017):
        current_position = (current_position + steps) % len(values)

        values.insert(current_position + 1, i + 1)

        # Set to the newly inserted values position
        current_position = current_position + 1

    idx = values.index(2017)
    print idx
    print 'Part 1:', values[idx + 1]

    # Now the spinner is up to 50,000,000 and we need to know the number after 0 in it.
    # We don't really want to build a list that large, so its lucky that 0 will always be in position 0.
    # All we need to track is the current value in position 1, the current position and the length of the "list"

    current_position = 0
    current_length = 1
    value_after_zero = 0
    for i in range(50000000):
        current_position = (current_position + steps) % current_length

        # "insert" a new value at current_position
        current_length += 1
        if current_position == 0:
            # The new value will be placed after 0, and we need to remember that.
            value_after_zero = i + 1

        # Set to the newly inserted values position
        current_position += 1

    print 'Part 2:', value_after_zero


main()
