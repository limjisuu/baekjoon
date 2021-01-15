import sys
from itertools import permutations
n, m = map(int, sys.stdin.readline().split())
permutation_list = list(permutations(range(1, n+1), m))

for permutation in permutation_list:
    for num in permutation:
        print(num, end=" ")
    print(end="\n")
