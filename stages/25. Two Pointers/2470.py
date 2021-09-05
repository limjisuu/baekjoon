n = int(input())
solutions = list(map(int, input().split()))
solutions.sort()
left = 0
right = n-1
val = solutions[left] + solutions[right]
answer = [0, 0]
while left < right:
    temp = solutions[left] + solutions[right]
    if abs(temp) <= abs(val):
        answer = [solutions[left], solutions[right]]
        val = temp
        if abs(val) == 0:
            break
    if temp < 0:
        left += 1
    else:
        right -= 1
print(answer[0], answer[1])
