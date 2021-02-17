import sys
from collections import deque
n = int(sys.stdin.readline())
queue = deque([])


def push(num):
    queue.append(num)


def pop():
    if not queue:
        print(-1)
    else:
        removed = queue.popleft()
        print(removed)


def size():
    print(len(queue))


def empty():
    if queue:
        print(0)
    else:
        print(1)


def front():
    if not queue:
        print(-1)
    else:
        print(queue[0])


def back():
    if not queue:
        print(-1)
    else:
        print(queue[-1])


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

    elif command_type == "front":
        front()

    elif command_type == "back":
        back()
