n, k = map(int, input().split())
divisors = []

for i in range(1, n+1):
    if n % i == 0:
        divisors.append(i)

print(divisors[k-1]) if len(divisors) >= k else print(0)
