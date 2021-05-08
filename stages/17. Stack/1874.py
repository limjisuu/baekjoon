import sys
n = int(sys.stdin.readline())
sequence = [int(sys.stdin.readline()) for _ in range(n)]
stack = []
result = []

for num in range(1, n + 1):
    stack.append(num)
    result.append("+")
    while stack and sequence and stack[-1] == sequence[0]:
        result.append("-")
        stack.pop()
        sequence.pop(0)

if sequence:
    print("NO")
else:
    print("\n".join(result))
