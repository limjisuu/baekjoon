import sys
n, target_price = map(int, sys.stdin.readline().split())
values = []
cnt = 0

for i in range(n):
    value = int(sys.stdin.readline())
    values.append(value)

for i in reversed(range(n)):
    while target_price >= values[i]:
        num = target_price // values[i]
        target_price -= num * values[i]
        cnt += num
print(cnt)
