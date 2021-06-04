import sys
n, k = map(int, sys.stdin.readline().split())
arr = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(k+1):
        if j == 0 or i == j:
            arr[i][j] = 1
        else:
            arr[i][j] = (arr[i-1][j-1] + arr[i-1][j]) % 10007
print(arr[n][k])
