import sys
coordinate = []
num = int(sys.stdin.readline())

for i in range(num):
    x, y = map(int, sys.stdin.readline().split())
    coordinate.append([])
    coordinate[i].append(x)
    coordinate[i].append(y)

sorted_coordinate = sorted(coordinate, key=lambda n: (n[1], n[0]))

for i in range(num):
    print(sorted_coordinate[i][0], sorted_coordinate[i][1])
