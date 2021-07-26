n = int(input())
cards = list(map(int, input().split()))
cards.sort()
m = int(input())
targets = list(map(int, input().split()))
answer = []
for target in targets:
    left = 0
    right = n - 1
    found = False
    while left <= right:
        mid = (left + right) // 2
        if cards[mid] == target:
            found = True
            break
        elif cards[mid] < target:
            left = mid + 1
        elif cards[mid] > target:
            right = mid - 1
    answer.append(1) if found else answer.append(0)
print(" ".join(map(str, answer)))
