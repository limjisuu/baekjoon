import sys
n = int(sys.stdin.readline())
rgb = [[0 for i in range(3)] for j in range(n)]
red = 0
green = 1
blue = 2

for i in range(n):
    rgb[i] = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    rgb[i][red] += min(rgb[i-1][blue], rgb[i-1][green])
    rgb[i][green] += min(rgb[i - 1][red], rgb[i - 1][blue])
    rgb[i][blue] += min(rgb[i - 1][red], rgb[i - 1][green])

print(min(rgb[n-1][red], rgb[n-1][green], rgb[n-1][blue]))
