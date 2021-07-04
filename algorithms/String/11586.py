n = int(input())
data = [list(map(str, input())) for _ in range(n)]
k = int(input())

if k == 1:
    for row in data:
        print("".join(map(str, row)))
elif k == 2:
    for row in data:
        print("".join(map(str, row[::-1])))
elif k == 3:
    for row in data[::-1]:
        print("".join(map(str, row)))
