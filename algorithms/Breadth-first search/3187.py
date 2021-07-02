from collections import deque
r, c = map(int, input().split())
data = [list(map(str, input())) for _ in range(r)]
visited = [[0 for _ in range(c)] for _ in range(r)]
total_sheep = sum(row.count("k") for row in data)
total_wolf = sum(row.count("v") for row in data)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    global total_sheep, total_wolf
    sheep = 0
    wolf = 0
    queue.append((x, y))
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < r and 0 <= ny < c and data[nx][ny] != "#" and not visited[nx][ny]:
                visited[nx][ny] = 1
                if data[nx][ny] == "k":
                    sheep += 1
                elif data[nx][ny] == "v":
                    wolf += 1
                queue.append((nx, ny))
    if sheep > wolf:
        total_wolf -= wolf
    else:
        total_sheep -= sheep


queue = deque()
for i in range(r):
    for j in range(c):
        if data[i][j] != "#" and not visited[i][j]:
            bfs(i, j)
print(total_sheep, total_wolf)
