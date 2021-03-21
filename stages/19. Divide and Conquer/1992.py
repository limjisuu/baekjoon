import sys
n = int(sys.stdin.readline())
dots = []
result = []


def quad_tree(x, y, n):
    color = dots[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if dots[i][j] != color:
                result.append("(")
                quad_tree(x, y, n // 2)
                quad_tree(x, y + n // 2, n // 2)
                quad_tree(x + n // 2, y, n // 2)
                quad_tree(x + n // 2, y + n // 2, n // 2)
                result.append(")")
                return
    if color == 0:
        result.append("0")
    else:
        result.append("1")


for _ in range(n):
    dots.append(list(map(int, str(sys.stdin.readline().rstrip()))))

quad_tree(0, 0, n)

for val in result:
    print(val, end="")
