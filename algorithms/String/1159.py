import sys
n = int(sys.stdin.readline())
names = [sys.stdin.readline().rstrip()[0] for _ in range(n)]
dic = {}
for name in names:
    if name in dic:
        dic[name] += 1
    else:
        dic[name] = 1
answer = []
for item in dic:
    if dic[item] >= 5:
        answer.append(item)
answer.sort()
print("".join(answer)) if answer else print("PREDAJA")
