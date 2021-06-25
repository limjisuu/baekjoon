from collections import deque
m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
days = []


def bfs():
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if box[nx][ny] == 0 and visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    box[nx][ny] = box[cx][cy] + 1
    return max(map(max, box)) - 1


queue = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((i, j))
            visited[i][j] = 1
days = bfs()
if all(0 not in line for line in box):
    print(days)
else:
    print(-1)
