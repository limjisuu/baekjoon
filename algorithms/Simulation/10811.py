n, m = map(int, input().split())
baskets = [_ for _ in range(n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    baskets[i:j+1] = reversed(baskets[i:j+1])

print(*baskets[1:])
