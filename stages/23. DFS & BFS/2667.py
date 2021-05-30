import sys
n = int(sys.stdin.readline())
data = [list(map(int, input())) for _ in range(n)]
cnt = 0
answer = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    global cnt
    cnt += 1
    data[x][y] = 0
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if 0 <= next_x < n and 0 <= next_y < n:
            if data[next_x][next_y] == 1:
                dfs(next_x, next_y)


for x in range(n):
    for y in range(n):
        if data[x][y] == 1:
            cnt = 0
            dfs(x, y)
            answer.append(cnt)

print(len(answer))
answer.sort()
for house_cnt in answer:
    print(house_cnt)
