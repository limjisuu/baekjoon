import sys
n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
target_list = list(map(int, sys.stdin.readline().split()))

num_list.sort()
for target in target_list:
    exist = False
    left = 0
    right = n - 1
    while right - left >= 0:
        mid = (left + right) // 2
        if target == num_list[mid]:
            exist = True
            break
        elif target > num_list[mid]:
            left = mid + 1
        elif target < num_list[mid]:
            right = mid - 1
    print(1) if exist else print(0)
