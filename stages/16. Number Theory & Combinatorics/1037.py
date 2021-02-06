import sys
n = int(sys.stdin.readline())
divisors = list(map(int, sys.stdin.readline().split()))

print(max(divisors) * min(divisors))
