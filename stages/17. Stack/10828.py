import sys
n = int(sys.stdin.readline())
stack = []


def push(num):
    stack.append(num)


def pop():
    if not stack:
        print(-1)
    else:
        removed = stack.pop(-1)
        print(removed)


def size():
    print(len(stack))


def empty():
    if not stack:
        print(1)
    else:
        print(0)


def top():
    if not stack:
        print(-1)
    else:
        print(stack[-1])


for i in range(n):
    command = sys.stdin.readline()
    command_type = command.split(' ')[0].rstrip()

    if command_type == "push":
        num = int(command.split(' ')[1])
        push(num)

    elif command_type == "pop":
        pop()

    elif command_type == "size":
        size()

    elif command_type == "empty":
        empty()

    elif command_type == "top":
        top()
