import sys
import heapq
n = int(sys.stdin.readline())
absolute_heap = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(absolute_heap, (abs(num), num))
    else:
        if absolute_heap:
            print(heapq.heappop(absolute_heap)[1])
        else:
            print(0)
