import sys
n = int(sys.stdin.readline())
stars = [[" " for _ in range(n)] for _ in range(n)]


def add_star(x, y, size):
    if size == 3:
        for i in range(x, x + 3):
            for j in range(y, y + 3):
                if not (i == x + 1 and j == y + 1):
                    stars[i][j] = "*"
    else:
        new_size = size // 3
        add_star(x, y, new_size)
        add_star(x + new_size, y, new_size)
        add_star(x + new_size * 2, y, new_size)
        add_star(x, y + new_size, new_size)
        add_star(x + new_size * 2,  y + new_size, new_size)
        add_star(x, y + new_size * 2, new_size)
        add_star(x + new_size, y + new_size * 2, new_size)
        add_star(x + new_size * 2, y + new_size * 2, new_size)


add_star(0, 0, n)
for line in stars:
    for char in line:
        print(char, end="")
    print("")
