import sys
have, need = map(int, sys.stdin.readline().split())
lan_list = [int(sys.stdin.readline()) for _ in range(have)]

left = 1
right = max(lan_list)
while left <= right:
    cnt = 0
    mid = (left + right) // 2
    for lan in lan_list:
        cnt += (lan // mid)
    if cnt >= need:
        left = mid + 1
    else:
        right = mid - 1

print(right)
