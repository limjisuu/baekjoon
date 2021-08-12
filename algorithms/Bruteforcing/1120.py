a, b = input().split()
answer = float("inf")

for i in range(len(b) - len(a) + 1):
    diff = 0
    for j in range(len(a)):
        if a[j] != b[i:][j]:
            diff += 1
    if diff < answer:
        answer = diff
print(answer)
