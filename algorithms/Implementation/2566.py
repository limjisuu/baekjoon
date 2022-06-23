matrix = [list(map(int, input().split())) for _ in range(9)]
answer, row, col = 0, 0, 0
for i in range(9):
    for j in range(9):
        if answer < matrix[i][j]:
            answer = matrix[i][j]
            row, col = i, j
print(answer)
print(row + 1, col + 1)
