from collections import deque
import sys
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
cnt_list = []


def bfs(x):
    visited = [0 for _ in range(n+1)]
    visited[x] = 1
    queue.append(x)
    cnt = 0
    while queue:
        cx = queue.popleft()
        for nx in graph[cx]:
            if not visited[nx]:
                visited[nx] = 1
                queue.append(nx)
                cnt += 1
    cnt_list.append(cnt)


for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)

queue = deque()
for i in range(1, n+1):
    bfs(i)

maximum = max(cnt_list)
answer = [idx + 1 for idx, cnt in enumerate(cnt_list) if cnt == maximum]
answer.sort()
print(" ".join(map(str, answer)))
