import sys
n = int(sys.stdin.readline())
dp = [0 for _ in range(1001)]
dp[1] = dp[3] = 1
for i in range(4, n+1):
    if dp[i-1] or dp[i-3]:
        dp[i] = 0
    else:
        dp[i] = 1
if dp[n]:
    print("SK")
else:
    print("CY")
