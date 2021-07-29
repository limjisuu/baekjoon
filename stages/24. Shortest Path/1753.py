import sys
import heapq
v, e = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = [[] for _ in range(v+1)]
INF = float("inf")
distances = [INF for _ in range(v+1)]

for _ in range(e):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))


def dijkstra(start):
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        cur_weight, cur_vertex = heapq.heappop(queue)
        if distances[cur_vertex] < cur_weight:
            continue
        for vertex, weight in graph[cur_vertex]:
            new_weight = cur_weight + weight
            if new_weight < distances[vertex]:
                distances[vertex] = new_weight
                heapq.heappush(queue, (new_weight, vertex))


dijkstra(start)
for distance in distances[1:]:
    print("INF") if distance == INF else print(distance)
