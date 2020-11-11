import sys
num = int(sys.stdin.readline())
height_list = []
weight_list = []
rank_list = []

for i in range(num):
    weight, height = map(int, sys.stdin.readline().split())
    weight_list.append(weight)
    height_list.append(height)


for i in range(num):
    rank = 1
    for j in range(num):
        if weight_list[i] < weight_list[j] and height_list[i] < height_list[j]:
            rank += 1
    rank_list.append(rank)

for i in range(num):
    print(rank_list[i], end=" ")
