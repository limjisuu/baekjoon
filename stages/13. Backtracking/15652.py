import sys
from itertools import combinations_with_replacement
n, m = map(int, sys.stdin.readline().split())
num_list = []

for i in range(1, n + 1):
    num_list.append(i)

cwr_list = combinations_with_replacement(num_list, m)

for cwr in cwr_list:
    for i in range(m):
        if i == m - 1:
            print(cwr[i])
        else:
            print(cwr[i], end=" ")
