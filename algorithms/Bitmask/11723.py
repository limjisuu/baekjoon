import sys
n = int(sys.stdin.readline())
s = [0] * 21

for _ in range(n):
    operation = sys.stdin.readline().split()
    command = operation[0]
    if len(operation) > 1:
        x = int(operation[1])
        if command == "add":
            s[x] = 1
        elif command == "remove":
            s[x] = 0
        elif command == "check":
            print(1) if s[x] else print(0)
        elif command == "toggle":
            s[x] = 1 - s[x]
    else:
        if command == "all":
            s = [1] * 21
        elif command == "empty":
            s = [0] * 21
