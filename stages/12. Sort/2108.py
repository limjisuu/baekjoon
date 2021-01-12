import sys
from collections import Counter


def mode(number_list):
    cnt = Counter(number_list)
    mode_list = cnt.most_common(2)
    if len(mode_list) == 1:
        print(mode_list[0][0])
    else:
        if mode_list[0][1] == mode_list[1][1]:
            print(mode_list[1][0])
        else:
            print(mode_list[0][0])


n = int(sys.stdin.readline())
num_list = []

for i in range(n):
    num = int(sys.stdin.readline())
    num_list.append(num)

num_list.sort()
avg = round(sum(num_list) / n)
median = num_list[n // 2]
scope = num_list[n - 1] - num_list[0]

print(avg)
print(median)
mode(num_list)
print(scope)
