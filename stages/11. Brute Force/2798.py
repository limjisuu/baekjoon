import sys
from itertools import combinations
num, maximum = map(int, sys.stdin.readline().split())
card_list = list(map(int, sys.stdin.readline().split()))

combination_list = list(combinations(card_list, 3))
sum_list = []

for i in range(len(combination_list)):
    sum_list.append(sum(combination_list[i]))
sum_list.sort()

target = sum_list[0]
for i in range(len(sum_list)):
    if target <= sum_list[i] <= maximum:
        target = sum_list[i]
print(target)
