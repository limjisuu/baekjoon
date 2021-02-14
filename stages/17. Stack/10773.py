import sys
stack = []
n = int(sys.stdin.readline())


def push(num):
    stack.append(num)


def pop():
    if stack:
        stack.pop(-1)


for i in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        pop()
    else:
        push(num)

print(sum(stack))
