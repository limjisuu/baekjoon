import sys
a, b, c = map(int, sys.stdin.readline().split())
answer = sorted([a, b, c])[1]
print(answer)
