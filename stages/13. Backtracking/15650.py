import sys
from itertools import combinations
n, m = map(int, sys.stdin.readline().split())
num_list = []

for i in range(1, n + 1):
    num_list.append(i)

combination_list = combinations(num_list, m)

for combination in combination_list:
    for i in range(m):
        if i == m - 1:
            print(combination[i])
        else:
            print(combination[i], end=" ")
