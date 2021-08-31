from collections import deque
import sys
m, n, k = map(int, sys.stdin.readline().split())
data = [[1 for _ in range(n)] for _ in range(m)]
visited = [[0 for _ in range(n)] for _ in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    queue.append((x, y))
    visited[x][y] = 1
    size = 1
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < m and 0 <= ny < n and data[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = 1
                size += 1
    return size


for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            data[i][j] = 0

queue = deque()
sizes = []
cnt = 0
for x in range(m):
    for y in range(n):
        if data[x][y] == 1 and not visited[x][y]:
            size = bfs(x, y)
            sizes.append(size)
sizes.sort()
print(len(sizes))
print(" ".join(map(str, sizes)))
