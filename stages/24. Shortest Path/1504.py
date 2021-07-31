import sys
import heapq
n, e = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
INF = float("inf")

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, sys.stdin.readline().split())


def dijkstra(start, end):
    distances = [INF for _ in range(n+1)]
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
    return distances[end]


option1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
option2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)
answer = min(option1, option2)
print(answer) if answer != INF else print(-1)
