import sys
n, m = map(int, sys.stdin.readline().split())
targets = list(map(int, sys.stdin.readline().split()))
elements = [_ for _ in range(1, n+1)]
cnt = 0

while targets:
    if targets[0] == elements[0]:
        targets.pop(0)
        elements.pop(0)
    else:
        target_idx = elements.index(targets[0])
        if target_idx < len(elements) / 2:
            while elements[0] != targets[0]:
                removed = elements.pop(0)
                elements.append(removed)
                cnt += 1
        else:
            while elements[0] != targets[0]:
                removed = elements.pop(-1)
                elements.insert(0, removed)
                cnt += 1
print(cnt)
