import sys
num = int(sys.stdin.readline())
cnt = 0
candidates = list(map(int, sys.stdin.readline().split()))
for candidate in candidates:
    is_prime = True
    divisor = 2
    for i in range(candidate - 2):
        if candidate % divisor == 0:
            is_prime = False
            break
        divisor += 1
    if candidate != 1 and is_prime:
        cnt += 1
print(cnt)
