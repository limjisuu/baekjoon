import sys
from itertools import combinations
n, k = map(int, sys.stdin.readline().split())

binomial_coefficient = list(combinations([_ for _ in range(1, n+1)], k))
print(len(binomial_coefficient))
