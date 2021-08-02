import sys
v, e = map(int, sys.stdin.readline().split())
INF = float("inf")
distances = [[INF for _ in range(v+1)] for _ in range(v+1)]
answer = INF

for i in range(1, v+1):
    distances[i][i] = 0

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    distances[a][b] = c


def floyd_warshall():
    for k in range(1, v+1):
        for i in range(1, v+1):
            for j in range(1, v+1):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])


floyd_warshall()
for i in range(1, v):
    for j in range(i, v+1):
        if i != j and distances[i][j] + distances[j][i] < answer:
            answer = distances[i][j] + distances[j][i]
print(answer) if answer != INF else print(-1)
