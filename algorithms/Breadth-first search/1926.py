from collections import deque
n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 0
maximum = 0


def bfs(x, y):
    global maximum
    queue.append((x, y))
    visited[x][y] = 1
    width = 1
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = 1
                data[nx][ny] = data[cx][cy] + 1
                width += 1
    if width > maximum:
        maximum = width


queue = deque()
for i in range(n):
    for j in range(m):
        if data[i][j] == 1 and not visited[i][j]:
            bfs(i, j)
            cnt += 1
print(cnt)
print(maximum)
