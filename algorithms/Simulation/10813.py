n, m = map(int, input().split())
baskets = [_ for _ in range(n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    basket_i = baskets[i]
    baskets[i] = baskets[j]
    baskets[j] = basket_i

print(*baskets[1:])
