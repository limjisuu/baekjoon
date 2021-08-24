from collections import deque
n, m, k = map(int, input().split())
data = [[0 for _ in range(m)] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    size = 1
    queue.append((x, y))
    visited[x][y] = 1
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = 1
                size += 1
    return size


for _ in range(k):
    r, c = map(int, input().split())
    data[r-1][c-1] = 1

answer = 0
queue = deque()
for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            size = bfs(i, j)
            if size > answer:
                answer = size
print(answer)
