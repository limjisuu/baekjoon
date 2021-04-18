import sys
n, target = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

left = 0
right = max(trees)
while left <= right:
    mid = (left + right) // 2
    result = sum(tree - mid if mid < tree else 0 for tree in trees)
    if result >= target:
        left = mid + 1
    else:
        right = mid - 1
print(right)
