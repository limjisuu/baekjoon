import sys
import math
num = int(sys.stdin.readline())
for i in range(num):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    if r1 > r2:
        tmp = x1
        x1 = x2
        x2 = tmp
        tmp = y1
        y1 = y2
        y2 = tmp
        tmp = r1
        r1 = r2
        r2 = tmp
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif r2 - r1 < distance < r2 + r1:
        print(2)
    elif r1 + r2 == distance or r2 - r1 == distance:
        print(1)
    elif r1 + r1 < distance or distance < r2 - r1:
        print(0)
