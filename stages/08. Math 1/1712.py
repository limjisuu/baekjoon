import sys
fixed, variable, cost = map(int, sys.stdin.readline().split())
if cost - variable <= 0:
    print(-1)
else:
    break_even_point = fixed // (cost - variable) + 1
    print(break_even_point)
