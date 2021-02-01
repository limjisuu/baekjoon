import sys
n = int(sys.stdin.readline())
ring_list = list(map(int, sys.stdin.readline().split()))


def calculate_gcd(a, b):
    number = max(a, b)
    divisor = min(a, b)
    if divisor == 0:
        return number
    return calculate_gcd(divisor, number % divisor)


for i in range(1, n):
    numerator = ring_list[i]
    denominator = ring_list[0]
    gcd = calculate_gcd(numerator, denominator)
    print(denominator//gcd, "/", numerator//gcd, sep="")
