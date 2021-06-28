from collections import deque
n = int(input())
normal_colors = [list(map(str, input())) for _ in range(n)]
normal_visited = [[0 for _ in range(n)] for _ in range(n)]
blind_colors = [["R" if color == "G" else color for color in colors] for colors in normal_colors]
blind_visited = [[0 for _ in range(n)] for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
normal_cnt = 0
blind_cnt = 0


def bfs(x, y, colors, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if colors[nx][ny] == colors[cx][cy]:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1


for i in range(n):
    for j in range(n):
        if normal_visited[i][j] == 0:
            bfs(i, j, normal_colors, normal_visited)
            normal_cnt += 1

for i in range(n):
    for j in range(n):
        if blind_visited[i][j] == 0:
            bfs(i, j, blind_colors, blind_visited)
            blind_cnt += 1

print(normal_cnt, blind_cnt)
