idx, answer = 0, 0
for i in range(5):
    score = list(map(int, input().split()))
    if answer < sum(score):
        answer = sum(score)
        idx = i + 1
print(idx, answer)
