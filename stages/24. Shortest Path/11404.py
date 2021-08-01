import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
INF = float("inf")
distances = [[INF for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
        distances[i][i] = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    distances[a][b] = min(distances[a][b], c)


def floyd_warshall():
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])


floyd_warshall()
for i in range(1, n+1):
    for j in range(1, n+1):
        print(distances[i][j], end=" ") if distances[i][j] != INF else print(0, end=" ")
    print()
