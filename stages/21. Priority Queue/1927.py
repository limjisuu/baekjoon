import sys
import heapq
n = int(sys.stdin.readline())
min_heap = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if num > 0:
        heapq.heappush(min_heap, num)
    elif num == 0:
        if min_heap:
            print(heapq.heappop(min_heap))
        else:
            print(0)
