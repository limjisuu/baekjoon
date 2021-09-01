from collections import deque
import sys
n = int(sys.stdin.readline())
person1, person2 = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
distances = [0 for _ in range(n+1)]


def bfs():
    queue = deque([person1])
    while queue:
        x = queue.popleft()
        if x == person2:
            return distances[person2]
        for nx in graph[x]:
            if distances[nx] == 0:
                queue.append(nx)
                distances[nx] = distances[x] + 1
    return -1


for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

answer = bfs()
print(answer)
