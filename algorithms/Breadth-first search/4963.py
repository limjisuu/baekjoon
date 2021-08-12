from collections import deque
dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [1, 0, -1, 1, -1, 1, 0, -1]


def bfs(x, y):
    visited[x][y] = 1
    queue.append((x, y))
    while queue:
        cx, cy = queue.popleft()
        for i in range(8):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < h and 0 <= ny < w and data[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx, ny))


while 1:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    queue = deque()
    data = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0 for _ in range(w)] for _ in range(h)]
    answer = 0
    for i in range(h):
        for j in range(w):
            if data[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                answer += 1
    print(answer)
