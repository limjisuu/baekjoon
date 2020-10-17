import sys
x_coordinate = []
y_coordinate = []
x4, y4 = 0, 0
for i in range(3):
    x, y = map(int, sys.stdin.readline().split())
    x_coordinate.append(x)
    y_coordinate.append(y)
for j in range(3):
    if x_coordinate.count(x_coordinate[j]) == 1:
        x4 = x_coordinate[j]
    if y_coordinate.count(y_coordinate[j]) == 1:
        y4 = y_coordinate[j]
print(x4, y4)
