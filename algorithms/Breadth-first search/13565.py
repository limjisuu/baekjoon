from collections import deque
m, n = map(int, input().split())
data = [list(map(int, input())) for _ in range(m)]
visited = [[0 for _ in range(n)] for _ in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(y, x):
    visited[y][x] = 1
    queue.append((y, x))
    while queue:
        cy, cx = queue.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0 <= ny < m and 0 <= nx < n and data[ny][nx] == 0 and not visited[ny][nx]:
                queue.append((ny, nx))
                visited[ny][nx] = 1


queue = deque()
for i in range(n):
    if data[0][i] == 0 and not visited[0][i]:
        bfs(0, i)
print("YES") if 1 in visited[m-1] else print("NO")
