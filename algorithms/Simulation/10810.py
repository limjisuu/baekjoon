n, m = map(int, input().split())
baskets = [0 for _ in range(n+1)]

for _ in range(m):
    i, j, k = map(int, input().split())
    for l in range(i, j+1):
        baskets[l] = k

print(*baskets[1:])
