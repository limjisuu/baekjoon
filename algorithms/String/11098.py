n = int(input())
for _ in range(n):
    p = int(input())
    info = []
    for _ in range(p):
        cost, name = input().split()
        info.append((int(cost), name))
    info.sort(key=lambda x: x[0], reverse=True)
    print(info[0][1])
