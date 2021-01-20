import sys
from itertools import combinations
n = int(sys.stdin.readline())
num_list = [_ for _ in range(n)]
ability_list = []

for i in range(n):
    ability_list.append(list(map(int, sys.stdin.readline().split())))

combination_list = list(combinations(num_list, n // 2))

result_list = []
for combination in combination_list:
    result = 0
    pair_list = list(combinations(combination, 2))
    for pair in pair_list:
        result += ability_list[pair[0]][pair[1]] + ability_list[pair[1]][pair[0]]
    result_list.append(result)

min_diff = 10000
for i in range(len(result_list) // 2):
    diff = abs(result_list[i] - result_list[len(result_list) - 1 - i])
    if diff < min_diff:
        min_diff = diff
print(min_diff)
