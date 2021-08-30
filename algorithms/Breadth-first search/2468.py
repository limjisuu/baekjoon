from collections import deque
import sys
n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    queue.append((x, y))
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and temp[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx, ny))


queue = deque()
maximum = max(map(max, data))
answer = 0
for num in range(maximum):
    cnt = 0
    temp = [[1 if data[i][j] > num else 0 for j in range(n)] for i in range(n)]
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if temp[x][y] == 1 and not visited[x][y]:
                bfs(x, y)
                cnt += 1
    if cnt > answer:
        answer = cnt
print(answer)
