import sys
num = int(sys.stdin.readline())

diff = 1
init = 0
numerator = 0
denominator = 0

for i in range(num):
    if init < num <= init + diff:
        temp = init + diff - num
        if diff % 2 == 0:
            numerator = diff - temp
            denominator = temp + 1
        else:
            numerator = temp + 1
            denominator = diff - temp
        break
    init = init + diff
    diff += 1

print('%d/%d' % (numerator, denominator))
