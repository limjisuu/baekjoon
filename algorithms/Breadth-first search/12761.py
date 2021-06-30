from collections import deque
a, b, n, m = map(int, input().split())
location = [0 for _ in range(100001)]


def bfs():
    queue = deque([n])
    while queue:
        cx = queue.popleft()
        if cx == m:
            print(location[cx])
            return
        for nx in (cx - 1, cx + 1, cx + a, cx - a, cx + b, cx - b, cx * a, cx * b):
            if 0 <= nx <= 100000 and not location[nx]:
                location[nx] = location[cx] + 1
                queue.append(nx)


bfs()
