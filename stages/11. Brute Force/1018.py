import sys
height, width = map(int, sys.stdin.readline().split())
board = []
cnt_list = []

for i in range(height):
    board.append(list(map(str, sys.stdin.readline().rstrip())))

for i in range(height - 7):
    for j in range(width - 7):
        b_cnt = 0
        w_cnt = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if k % 2 == l % 2:
                    if board[k][l] == 'W':
                        b_cnt += 1
                    if board[k][l] == 'B':
                        w_cnt += 1
                else:
                    if board[k][l] == 'B':
                        b_cnt += 1
                    if board[k][l] == 'W':
                        w_cnt += 1
        cnt_list.append(b_cnt)
        cnt_list.append(w_cnt)

cnt_list.sort()
print(cnt_list[0])
