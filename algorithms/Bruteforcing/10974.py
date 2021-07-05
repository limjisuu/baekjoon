from itertools import permutations
n = int(input())
permutation_list = permutations([_ for _ in range(1, n+1)], n)
for permutation in permutation_list:
    print(" ".join(map(str, permutation)))
