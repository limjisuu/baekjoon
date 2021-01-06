import sys
num = int(sys.stdin.readline())
num_list = []
for i in range(num):
    n = int(sys.stdin.readline())
    num_list.append(n)

num_list.sort()
for i in range(num):
    print(num_list[i])
