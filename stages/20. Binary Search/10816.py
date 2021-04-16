import sys
n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))
result = {}

for card in cards:
    if card in result.keys():
        result[card] += 1
    else:
        result[card] = 1

for target in targets:
    print(result[target], end=" ") if target in result.keys() else print(0, end=" ")
