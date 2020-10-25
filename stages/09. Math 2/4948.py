import sys
import math
num = int(sys.stdin.readline())
compare_list = [0 for _ in range(123456 * 2)]
for i in range(2, 123456 * 2 + 1):
    is_prime = True
    for divisor in range(2, int(math.sqrt(i)) + 1):
        if i % divisor == 0:
            is_prime = False
            break
    if is_prime:
        compare_list[i - 1] = 1
while num != 0:
    cnt = 0
    for i in range(num + 1, 2 * num + 1):
        if compare_list[i - 1] == 1:
            cnt += 1
    print(cnt)
    num = int(sys.stdin.readline())
