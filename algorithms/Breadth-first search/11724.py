from collections import deque
import sys
n, m = map(int, sys.stdin.readline().split())
matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
answer = 0


def bfs():
    while queue:
        x = queue.popleft()
        visited[x] = 1
        for y in range(n+1):
            if matrix[x][y] == 1 and not visited[y]:
                visited[y] = 1
                queue.append(y)


for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    matrix[u][v] = matrix[v][u] = 1

queue = deque()
for i in range(1, n+1):
    if not visited[i]:
        queue.append(i)
        bfs()
        answer += 1
print(answer)
