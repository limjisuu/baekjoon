import sys
case_num = int(sys.stdin.readline())
cases = [list(map(int, sys.stdin.readline().split())) for _ in range(case_num)]
dp = [[0 for _ in range(31)] for _ in range(31)]


def combination(n, r):
    for i in range(n+1):
        for j in range(r+1):
            if i == j or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]


for case in cases:
    n = case[1]
    r = case[0]
    combination(n, r)
    print(dp[n][r])
