import sys
num = int(sys.stdin.readline())
dividend = num
divisor = 2
if num != 1:
    while 1:
        if dividend % divisor == 0:
            dividend = dividend / divisor
            print(divisor)
        else:
            divisor += 1
        if dividend == 1:
            break
