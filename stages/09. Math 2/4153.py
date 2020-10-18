import sys
num = list(map(int, sys.stdin.readline().split()))
while sum(num) != 0:
    num.sort()
    if num[0] ** 2 + num[1] ** 2 == num[2] ** 2:
        print("right")
    else:
        print("wrong")
    num = list(map(int, sys.stdin.readline().split()))
