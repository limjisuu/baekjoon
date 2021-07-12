n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
x = int(input())
left, right = 0, n-1
answer = 0
while left < right:
    total = numbers[left] + numbers[right]
    if total == x:
        answer += 1
        left += 1
    elif total < x:
        left += 1
    elif total > x:
        right -= 1
print(answer)
