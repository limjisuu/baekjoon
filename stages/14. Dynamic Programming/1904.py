import sys
n = int(sys.stdin.readline())
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    if i == 1:
        dp[1] = 1
    elif i == 2:
        dp[2] = 2
    else:
        dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[n])
