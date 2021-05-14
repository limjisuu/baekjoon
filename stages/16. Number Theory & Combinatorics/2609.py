import sys
a, b = map(int, sys.stdin.readline().split())


def calculate_gcd(a, b):
    global gcd
    if a < b:
        a, b = b, a
    if a % b == 0:
        gcd = b
    else:
        calculate_gcd(b, a % b)


calculate_gcd(a, b)
print(gcd)
print(a * b // gcd)
