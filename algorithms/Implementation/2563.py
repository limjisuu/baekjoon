paper = [[0 for _ in range(101)] for _ in range(101)]
n = int(input())
answer = 0

for _ in range(n):
    w, h = map(int, input().split())
    for i in range(w, w+10):
        for j in range(h, h+10):
            paper[i][j] = 1

for i in range(101):
    for j in range(101):
        if paper[i][j] == 1:
            answer += 1

print(answer)
