import sys
import math
num = int(sys.stdin.readline())
prime_list = []
for i in range(2, 10000 + 1):
    is_prime = True
    for divisor in range(2, int(math.sqrt(i)) + 1):
        if i % divisor == 0:
            is_prime = False
            break
    if is_prime:
        prime_list.append(i)
for i in range(num):
    even_num = int(sys.stdin.readline())
    half = even_num // 2
    for j in range(half, even_num):
        if half in prime_list:
            if even_num - half in prime_list:
                print(even_num - half, half)
                break
        half += 1
