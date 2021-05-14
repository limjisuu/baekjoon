import sys
n = int(sys.stdin.readline())
cases = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


def calculate_gcd(a, b):
    global gcd
    if a < b:
        a, b = b, a
    if a % b == 0:
        gcd = b
    else:
        calculate_gcd(b, a % b)


for case in cases:
    a = case[0]
    b = case[1]
    calculate_gcd(a, b)
    print(a * b // gcd)
