import sys
num = int(sys.stdin.readline())
cnt = 0
while num > 0:
    if num % 5 == 0:
        while num > 0:
            num -= 5
            cnt += 1
    else:
        num -= 3
        cnt += 1
    if num < 0:
        print(-1)
        sys.exit()
print(cnt)
