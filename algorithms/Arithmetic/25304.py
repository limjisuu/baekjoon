receipt = int(input())
n = int(input())

total = 0
for _ in range(n):
    cost, quantity = map(int, input().split())
    total += cost * quantity

if total == receipt:
    print("Yes")
else:
    print("No")
