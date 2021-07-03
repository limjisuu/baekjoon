from collections import deque
n, m = map(int, input().split())
data = [list(map(str, input())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    person = 0
    queue.append((x, y))
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and data[nx][ny] != "X" and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = 1
                if data[nx][ny] == "P":
                    person += 1
    print(person) if person > 0 else print("TT")


queue = deque()
for i in range(n):
    for j in range(m):
        if data[i][j] == "I":
            bfs(i, j)
