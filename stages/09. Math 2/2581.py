import sys
start = int(sys.stdin.readline())
end = int(sys.stdin.readline())
result = 0
prime_list = []
for num in range(start, end + 1):
    is_prime = True
    for divisor in range(2, num):
        if num % divisor == 0:
            is_prime = False
            break
    if num != 1 and is_prime:
        result += num
        prime_list.append(num)
if len(prime_list) == 0:
    print(-1)
else:
    print(result)
    print(prime_list[0])
