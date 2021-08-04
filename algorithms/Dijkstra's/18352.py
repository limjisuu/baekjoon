import sys
import heapq
n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
INF = float("inf")
distances = [INF for _ in range(n+1)]
answer = []

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)


def dijkstra(start):
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        cur_cost, cur_node = heapq.heappop(queue)
        if cur_cost < distances[cur_node]:
            continue
        for node in graph[cur_node]:
            new_cost = cur_cost + 1
            if new_cost < distances[node]:
                distances[node] = new_cost
                heapq.heappush(queue, (new_cost, node))


dijkstra(x)
for i in range(n+1):
    if distances[i] == k:
        answer.append(i)
answer.sort()
print("\n".join(map(str, answer))) if answer else print(-1)
