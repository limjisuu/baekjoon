n = int(input())
words = list(input() for _ in range(n))
answer = 0
for word in words:
    stack = []
    for char in word:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    if not stack:
        answer += 1
print(answer)
