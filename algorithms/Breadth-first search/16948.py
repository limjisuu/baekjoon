from collections import deque
n = int(input())
r1, c1, r2, c2 = map(int, input().split())
board = [[0 for _ in range(n)] for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]


def bfs(r, c):
    queue = deque()
    queue.append((r, c))
    visited[r][c] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0:
                    queue.append([nx, ny])
                    visited[nx][ny] = 1
                    board[nx][ny] = board[x][y] + 1


bfs(r1, c1)
print(board[r2][c2]) if visited[r2][c2] else print(-1)
