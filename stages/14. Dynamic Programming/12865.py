import sys
num, max_weight = map(int, sys.stdin.readline().split())
item = [[0 for _ in range(2)] for _ in range(num+1)]
dp = [[0 for _ in range(max_weight+1)] for _ in range(num+1)]
weight = 0
value = 1


def select_item(i, w):
    if dp[i][w] > 0:
        return dp[i][w]
    if i == num:
        return 0
    taken = 0
    if w + item[i][weight] <= max_weight:
        taken = item[i][value] + select_item(i+1, w+item[i][weight])
    not_taken = select_item(i+1, w)
    dp[i][w] = max(taken, not_taken)
    return dp[i][w]


for i in range(num):
    item[i] = list(map(int, sys.stdin.readline().split()))

print(select_item(0, 0))
