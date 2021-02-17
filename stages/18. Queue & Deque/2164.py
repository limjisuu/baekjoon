import sys
from collections import deque
queue = deque([])


def push(num):
    queue.append(num)


def pop():
    if queue:
        removed = queue.popleft()
        return removed


n = int(sys.stdin.readline())
for i in range(1, n+1):
    queue.append(i)

cnt = n
while cnt != 1:
    pop()
    cnt -= 1
    removed = pop()
    push(removed)

print(queue[0])
