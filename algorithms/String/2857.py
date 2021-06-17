import sys
names = [sys.stdin.readline().rstrip() for _ in range(5)]
answer = []
for i in range(5):
    if "FBI" in names[i]:
        answer.append(i+1)
print(" ".join(map(str, answer))) if answer else print("HE GOT AWAY!")
