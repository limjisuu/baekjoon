from collections import deque
n, k = map(int, input().split())
position = [0 for _ in range(100001)]


def bfs():
    queue = deque([n])
    while queue:
        cx = queue.popleft()
        if cx == k:
            print(position[k])
            return
        for nx in (cx - 1, cx + 1, cx * 2):
            if 0 <= nx <= 100000 and not position[nx]:
                position[nx] = position[cx] + 1
                queue.append(nx)


bfs()
