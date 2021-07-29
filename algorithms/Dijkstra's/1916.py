import sys
import heapq
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
INF = float("inf")
distances = [INF for _ in range(n+1)]

for i in range(m):
    u, v, c = map(int, sys.stdin.readline().split())
    graph[u].append((v, c))


def dijkstra():
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        cur_cost, cur_node = heapq.heappop(queue)
        if distances[cur_node] < cur_cost:
            continue
        for node, cost in graph[cur_node]:
            new_cost = cur_cost + cost
            if new_cost < distances[node]:
                distances[node] = new_cost
                heapq.heappush(queue, (new_cost, node))


start, end = map(int, sys.stdin.readline().split())
dijkstra()
print(distances[end])
