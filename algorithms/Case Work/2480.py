numbers = list(map(int, input().split()))
cnt = [0 for _ in range(6)]
answer = 0

for n in numbers:
    cnt[n-1] += 1

for i in range(6):
    if cnt[i] == 3:
        answer = 10000 + (i+1) * 1000
        break
    elif cnt[i] == 2:
        answer = 1000 + (i+1) * 100
        break
    elif cnt[i] == 1:
        answer = (i+1) * 100

print(answer)
