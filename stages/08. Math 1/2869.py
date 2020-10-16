import sys
up, down, goal = map(int, sys.stdin.readline().split())
diff = up - down
days = (goal - up) // diff
if (goal - up) % diff == 0:
    print(days + 1)
else:
    print(days + 2)
