import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
queue = deque([_ for _ in range(1, n+1)])
josephus = []


def push(num):
    queue.append(num)


def pop():
    if queue:
        removed = queue.popleft()
        return removed


while queue:
    for i in range(k-1):
        removed = pop()
        push(removed)
    removed = pop()
    josephus.append(removed)

print("<" + ', '.join(map(str, josephus)) + ">")
