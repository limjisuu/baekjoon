import sys
coordinate_list = []
num = int(sys.stdin.readline())

for i in range(num):
    coordinate = list(map(int, sys.stdin.readline().split()))
    coordinate_list.append(coordinate)

sorted_coordinate = sorted(coordinate_list, key=lambda n: (n[0], n[1]))

for i in range(num):
    print(sorted_coordinate[i][0], sorted_coordinate[i][1])
