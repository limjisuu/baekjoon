n = int(input())
answer = 0
start = 1
end = 1
total = 1
while start <= end:
    if total < n:
        end += 1
        total += end
    elif total > n:
        total -= start
        start += 1
    else:
        answer += 1
        end += 1
        total += end
        total -= start
        start += 1
print(answer)
