import sys
dishes = sys.stdin.readline().rstrip()
answer = 10
for i in range(1, len(dishes)):
    if dishes[i] != dishes[i-1]:
        answer += 10
    else:
        answer += 5
print(answer)
