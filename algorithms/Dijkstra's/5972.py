import sys
import heapq
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
INF = float("inf")
distances = [INF for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra():
    distances[1] = 1
    queue = []
    heapq.heappush(queue, (0, 1))
    while queue:
        cur_cost, cur_node = heapq.heappop(queue)
        if distances[cur_node] < cur_cost:
            continue
        for node, cost in graph[cur_node]:
            new_cost = cur_cost + cost
            if new_cost < distances[node]:
                distances[node] = new_cost
                heapq.heappush(queue, (new_cost, node))


dijkstra()
print(distances[n])
