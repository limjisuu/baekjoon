import sys
from collections import deque
vertex_num, edge_num, start_vertex = map(int, sys.stdin.readline().split())
matrix = [[0 for _ in range(vertex_num + 1)] for _ in range(vertex_num + 1)]
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(edge_num)]
visited = [0 for _ in range(vertex_num + 1)]

for edge in edges:
    matrix[edge[0]][edge[1]] = 1
    matrix[edge[1]][edge[0]] = 1


def dfs(vertex):
    print(vertex, end=" ")
    visited[vertex] = 1
    for i in range(1, vertex_num + 1):
        if visited[i] == 0 and matrix[vertex][i]:
            dfs(i)


def bfs(vertex):
    queue = deque([vertex])
    print(vertex, end=" ")
    visited[vertex] = 0
    while queue:
        num = queue.popleft()
        for i in range(1, vertex_num + 1):
            if visited[i] == 1 and matrix[num][i] == 1:
                visited[i] = 0
                print(i, end=" ")
                queue.append(i)


dfs(start_vertex)
print(end="\n")
bfs(start_vertex)
