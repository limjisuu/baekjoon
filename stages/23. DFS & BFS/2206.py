from collections import deque
n, m = map(int, input().split())
data = [list(map(int, input())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    queue = deque()
    queue.append((0, 0, 0))
    visited[0][0][0] = 1
    while queue:
        cx, cy, wall = queue.popleft()
        if cx == n-1 and cy == m-1:
            return visited[cx][cy][wall]
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if data[nx][ny] == 0 and not visited[nx][ny][wall]:
                    visited[nx][ny][wall] = visited[cx][cy][wall] + 1
                    queue.append((nx, ny, wall))
                elif data[nx][ny] == 1 and wall == 0:
                    visited[nx][ny][1] = visited[cx][cy][wall] + 1
                    queue.append((nx, ny, 1))
    return -1


answer = bfs()
print(answer)
