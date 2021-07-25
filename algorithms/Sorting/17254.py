n, m = map(int, input().split())
data = []
for _ in range(m):
    a, b, c = input().split()
    data.append([int(a), int(b), c])
data.sort(key=lambda x: (x[1], x[0]))
for keyboard in data:
    print(keyboard[-1], end="")
