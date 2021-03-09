import sys
from collections import deque
deque = deque([])


def push_front(num):
    deque.appendleft(num)


def push_back(num):
    deque.append(num)


def pop_front():
    if deque:
        removed = deque.popleft()
        print(removed)
    else:
        print(-1)


def pop_back():
    if deque:
        removed = deque.pop()
        print(removed)
    else:
        print(-1)


def size():
    print(len(deque))


def empty():
    if deque:
        print(0)
    else:
        print(1)


def front():
    if deque:
        print(deque[0])
    else:
        print(-1)


def back():
    if deque:
        print(deque[-1])
    else:
        print(-1)


n = int(sys.stdin.readline())
for i in range(n):
    command = sys.stdin.readline()
    command_type = command.split(' ')[0].rstrip()

    if command_type == "push_front":
        num = command.split(' ')[1].rstrip()
        push_front(num)

    if command_type == "push_back":
        num = command.split(' ')[1].rstrip()
        push_back(num)

    if command_type == "pop_front":
        pop_front()

    if command_type == "pop_back":
        pop_back()

    if command_type == "size":
        size()

    if command_type == "empty":
        empty()

    if command_type == "front":
        front()

    if command_type == "back":
        back()
