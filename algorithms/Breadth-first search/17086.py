from collections import deque
n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [1, 0, -1, 1, -1, 1, 0, -1]


def bfs():
    while queue:
        cx, cy = queue.popleft()
        for i in range(8):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not data[nx][ny]:
                data[nx][ny] = data[cx][cy] + 1
                queue.append((nx, ny))


queue = deque()
for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            queue.append((i, j))
bfs()
print(max(map(max, data)) - 1)
