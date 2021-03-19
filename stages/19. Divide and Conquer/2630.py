import sys
length = int(sys.stdin.readline())
colors = []
white_cnt = 0
blue_cnt = 0


def check_paper(x, y, n):
    global white_cnt
    global blue_cnt
    color = colors[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if colors[i][j] != color:
                check_paper(x, y, n // 2)
                check_paper(x, y + n // 2, n // 2)
                check_paper(x + n // 2, y, n // 2)
                check_paper(x + n // 2, y + n // 2, n // 2)
                return
    if color == 0:
        white_cnt += 1
    elif color == 1:
        blue_cnt += 1


for i in range(length):
    colors.append(list(map(int, sys.stdin.readline().split())))

check_paper(0, 0, length)
print(white_cnt)
print(blue_cnt)
