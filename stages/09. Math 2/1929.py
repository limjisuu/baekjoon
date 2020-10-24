import sys
import math
start, end = map(int, sys.stdin.readline().split())
prime_list = []
for num in range(start, end + 1):
    is_prime = True
    for divisor in range(2, int(math.sqrt(num)) + 1):
        if num % divisor == 0:
            is_prime = False
            break
    if num != 1 and is_prime:
        prime_list.append(num)
for prime_num in prime_list:
    print(prime_num)
