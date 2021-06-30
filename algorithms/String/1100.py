board = [list(map(str, input())) for _ in range(8)]
answer = 0
for i in range(8):
    for j in range(8):
        if board[i][j] == "F":
            if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                answer += 1
print(answer)
