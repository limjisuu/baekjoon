from collections import deque
import sys
n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
parents = [0 for _ in range(n+1)]


def bfs():
    queue.append(1)
    while queue:
        cur = queue.popleft()
        for node in graph[cur]:
            if parents[node] == 0:
                parents[node] = cur
                queue.append(node)


for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
bfs()

for i in range(2, n+1):
    print(parents[i])
