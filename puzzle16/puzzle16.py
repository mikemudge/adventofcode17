
def main():
    with open('input') as f:
        lines = f.readlines()

        instructions = lines[0].split(',')
        dancers = list('abcdefghijklmnop')

        dancers = dance(dancers, instructions)

        print 'Part 1:', ''.join(dancers)

        # Part 2 is to repeat the dance a billion times.
        # Doing that would be very slow.
        # Instead we will try and find a loop which we can use to find the answer without repeating so many times.
        size = 1000000000
        cache = {}
        cache2 = []
        dancers = list('abcdefghijklmnop')
        danceloop = 0

        # Need to iterate up to a high enough number to find a dance loop???
        # but range(1,000,000,000) needs a lot of memory.
        i = 0
        while i < size:
            i += 1
            key = ''.join(dancers)
            if cache.get(key):
                # Found a dance loop.
                print 'Dance loop from', i, 'to', cache[key]
                danceloop = i - cache[key]
                break
            cache[key] = i
            cache2.append(key)

            dancers = dance(dancers, instructions)

        # Found a dance loop, which means we only need to find out where the dancers are after the remainder.
        size = size % danceloop

        print 'dance', size, 'times after finding a loop of ', danceloop
        dancers = cache2[size]
        print 'Part 2:', ''.join(dancers)

def dance(dancers, instructions):
    for ins in instructions:
        # Deal with it?
        if ins[0] == 'p':
            # Partner swap
            # Need to look up letters?
            p1 = ins[1]
            p2 = ins[3]
            # Swap p1 and p2
            idx1 = dancers.index(p1)
            idx2 = dancers.index(p2)
            dancers[idx1] = p2
            dancers[idx2] = p1
        elif ins[0] == 'x':
            # Exchange positions
            (x, y) = ins[1:].split('/')
            x = int(x)
            y = int(y)
            tmp = dancers[x]
            dancers[x] = dancers[y]
            dancers[y] = tmp
        elif ins[0] == 's':
            # Swap
            num = int(ins[1:])

            # Rotate the last num dancers to the front.
            dancers = dancers[-num:] + dancers[:-num]
        else:
            raise Exception('Bad instruction' + ins)

        # print ins
        # print dancers

    return dancers


main()
