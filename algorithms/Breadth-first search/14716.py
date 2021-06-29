from collections import deque
m, n = map(int, input().split())
numbers = [list(map(int, input().split())) for _ in range(m)]
visited = [[0 for _ in range(n)] for _ in range(m)]
dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]
answer = 0


def bfs(x, y):
    queue.append((x, y))
    while queue:
        cx, cy = queue.popleft()
        for i in range(8):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if numbers[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))


queue = deque()
for i in range(m):
    for j in range(n):
        if numbers[i][j] == 1 and not visited[i][j]:
            bfs(i, j)
            answer += 1
print(answer)
