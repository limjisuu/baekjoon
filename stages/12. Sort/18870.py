import sys
n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
sorted_list = sorted(num_list)

compressed = {}
val = 0
for num in sorted_list:
    if num not in compressed.keys():
        compressed[num] = val
        val += 1

for num in num_list:
    print(compressed[num], end=" ")
