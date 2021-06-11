import sys
n = int(sys.stdin.readline())
dp = [0 for _ in range(1001)]
dp[2] = dp[4] = 1
for i in range(5, n+1):
    if dp[i-1] and dp[i-3] and dp[i-4]:
        dp[i] = 0
    else:
        dp[i] = 1
print("SK") if dp[n] else print("CY")
