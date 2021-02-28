import sys
from collections import deque
test_num = int(sys.stdin.readline())


def push(n):
    queue.append(n)


def pop():
    if queue:
        removed = queue.popleft()
        return removed


for i in range(test_num):
    cnt = 0
    num, idx = map(int, sys.stdin.readline().split())
    queue = deque(list(map(int, sys.stdin.readline().split())))
    target = queue[idx]
    while queue:
        if queue[0] != max(queue):
            removed = pop()
            push(removed)
        else:
            removed = pop()
            cnt += 1
            if removed == target and idx == 0:
                print(cnt)
                break
        if idx == 0:
            idx = len(queue) - 1
        else:
            idx -= 1
