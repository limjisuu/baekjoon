n = int(input())
m = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
answer = 0
left = 0
right = n - 1
while left < right:
    total = numbers[left] + numbers[right]
    if total > m:
        right -= 1
    elif total < m:
        left += 1
    elif total == m:
        answer += 1
        left += 1
print(answer)
