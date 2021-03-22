import sys
n = int(sys.stdin.readline())
numbers = []
result = []


def check_paper(x, y, n):
    num = numbers[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if numbers[i][j] != num:
                new_len = n // 3
                check_paper(x, y, new_len)
                check_paper(x, y + new_len, new_len)
                check_paper(x, y + new_len * 2, new_len)
                check_paper(x + new_len, y, new_len)
                check_paper(x + new_len, y + new_len, new_len)
                check_paper(x + new_len, y + new_len * 2, new_len)
                check_paper(x + new_len * 2, y, new_len)
                check_paper(x + new_len * 2, y + new_len, new_len)
                check_paper(x + new_len * 2, y + new_len * 2, new_len)
                return
    if num == -1:
        result.append(-1)
    elif num == 0:
        result.append(0)
    elif num == 1:
        result.append(1)


for _ in range(n):
    numbers.append(list(map(int, sys.stdin.readline().split())))

check_paper(0, 0, n)
print(result.count(-1))
print(result.count(0))
print(result.count(1))
