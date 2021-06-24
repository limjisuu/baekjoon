from collections import deque
n = int(input())
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]


def bfs(x, y, target_x, target_y, size):
    board = [[0 for _ in range(size)] for _ in range(size)]
    visited = [[0 for _ in range(size)] for _ in range(size)]
    visited[x][y] = 1
    queue = deque()
    queue.append((x, y))
    while queue:
        cx, cy = queue.popleft()
        for i in range(8):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < size and 0 <= ny < size:
                if not visited[nx][ny]:
                    board[nx][ny] = board[cx][cy] + 1
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
    print(board[target_x][target_y])


for _ in range(n):
    size = int(input())
    x, y = map(int, input().split())
    target_x, target_y = map(int, input().split())
    bfs(x, y, target_x, target_y, size)
