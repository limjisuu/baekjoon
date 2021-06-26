from collections import deque
m, n, h = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
dx = [0, 0, 1, -1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]
dz = [1, -1, 0, 0, 0, 0]


def bfs():
    while queue:
        cz, cx, cy = queue.popleft()
        for i in range(6):
            nx = cx + dx[i]
            ny = cy + dy[i]
            nz = cz + dz[i]
            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
                if box[nz][nx][ny] == 0 and visited[nz][nx][ny] == 0:
                    box[nz][nx][ny] = box[cz][cx][cy] + 1
                    visited[nz][nx][ny] = 1
                    queue.append((nz, nx, ny))


queue = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                queue.append((i, j, k))
                visited[i][j][k] = 1
bfs()
answer = 0
is_ripe = True
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 0:
                is_ripe = False
                break
            answer = max(answer, box[i][j][k])
if is_ripe:
    if answer == -1:
        print(0)
    else:
        print(answer - 1)
else:
    print(-1)
