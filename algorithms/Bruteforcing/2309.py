from itertools import combinations
dwarfs = [int(input()) for _ in range(9)]
dwarfs.sort()

for combination in combinations(dwarfs, 7):
    if sum(combination) == 100:
        print("\n".join(map(str, combination)))
        break
