n, m = map(int, input().split())
numbers = list(map(int, input().split()))
answer = 0
start = 0
end = 0
total = numbers[0]
while end < n:
    if total == m:
        answer += 1
        total -= numbers[start]
        start += 1
    elif total > m:
        total -= numbers[start]
        start += 1
    elif total < m:
        end += 1
        if end < n:
            total += numbers[end]
print(answer)
