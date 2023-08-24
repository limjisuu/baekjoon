t = int(input())

for _ in range(t):
    c = int(input())
    answer = []
    for i in [25, 10, 5, 1]:
        answer.append(c // i)
        c %= i
    print(*answer)
