import sys
num = int(sys.stdin.readline())

for i in range(num):
    start, finish = map(int, sys.stdin.readline().split())
    distance = finish - start
    temp = 0
    diff = 1
    cnt = 0
    breaker = False
    while 1:
        for j in range(2):
            temp += diff
            cnt += 1
            if distance <= temp:
                breaker = True
                break
        diff += 1
        if breaker:
            break
    print(cnt)
