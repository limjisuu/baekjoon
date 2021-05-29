import sys
sys.setrecursionlimit(10000)
n = int(sys.stdin.readline())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    arr[x][y] = 0
    for k in range(4):
        next_x = x + dx[k]
        next_y = y + dy[k]
        if 0 <= next_x < width and 0 <= next_y < height:
            if arr[next_x][next_y] == 1:
                dfs(next_x, next_y)


for _ in range(n):
    width, height, cnt = map(int, sys.stdin.readline().split())
    cabbages = [list(map(int, sys.stdin.readline().split())) for _ in range(cnt)]
    arr = [[0 for _ in range(height)] for _ in range(width)]
    answer = 0
    for cabbage in cabbages:
        x = cabbage[0]
        y = cabbage[1]
        arr[x][y] = 1
    for i in range(width):
        for j in range(height):
            if arr[i][j] == 1:
                dfs(i, j)
                answer += 1
    print(answer)
