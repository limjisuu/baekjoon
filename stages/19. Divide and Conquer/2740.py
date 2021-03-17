import sys
matrix_a = []
matrix_b = []

n, m = map(int, sys.stdin.readline().split())
for i in range(n):
    matrix_a.append(list(map(int, sys.stdin.readline().split())))

m, k = map(int, sys.stdin.readline().split())
for i in range(m):
    matrix_b.append(list(map(int, sys.stdin.readline().split())))

result = [[0 for _ in range(k)] for _ in range(n)]
for x in range(n):
    for y in range(k):
        temp = 0
        for z in range(m):
            temp += matrix_a[x][z] * matrix_b[z][y]
        result[x][y] = temp

for i in range(n):
    for num in result[i]:
        print(num, end=" ")
    print(end="\n")
