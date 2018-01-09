

def main():
    with open('input') as f:
        lines = f.readlines()

        parts = map(int, lines[0].split(','))
        print parts
        values = range(256)
        # values = range(5)
        # parts = [3, 4, 1, 5]

        currentIdx = 0
        skip = 0
        for p in parts:
            # if p == 0 or p == 1:
            #     continue
            print values
            print skip, currentIdx, p

            values = rotate(values, currentIdx)
            # reverse the first p numbers.
            # print values[:p]
            values[:p] = values[:p][::-1]
            # rotate back to 0 based.
            values = rotate(values, -currentIdx)

            currentIdx = (currentIdx + p + skip) % len(values)
            skip += 1

        print 'Part 1', values
        print 'Part 1', values[0] * values[1]
        # 60270 was too high.
        # 2352 was too low.
        # 9288 is wrong.
        # 16256 is wrong.

def rotate(l, n):
    return l[n:] + l[:n]


# def old_way():
#     if currentIdx + p > 255:
#         # TODO figure out the shorter length???
#         dis_from_end = 256 - currentIdx
#         x = currentIdx
#         y = currentIdx + p - 256
#         print x, '->', y, dis_from_end

#         if dis_from_end > y:
#             # More at end than start
#             # x: x + y: 256/0: y

#             # reverse and save the first part to put at the start.
#             temp1 = values[x:x + y][::-1]

#             # reverse the last part and put it at the start.
#             values[x:x + y] = values[:y][::-1]

#             # reverse the middle.
#             values[dis_from_end + y:] = values[dis_from_end + y:][::-1]

#             values[:y] = temp1
#         else:
#             # More at the start than at the end.
#             # x: 256/0: dis_from_end: y

#             # reverse and save the first part to put at the start.
#             temp1 = values[x:][::-1]

#             # reverse the last part and put it at the start.
#             values[x:] = values[dis_from_end:y][::-1]

#             # reverse the middle.
#             values[:dis_from_end] = values[:dis_from_end][::-1]

#             values[dis_from_end:y] = temp1
#     else:
#         # Normal reverse.
#         values[currentIdx:currentIdx + p] = values[currentIdx:currentIdx + p][::-1]


main()
