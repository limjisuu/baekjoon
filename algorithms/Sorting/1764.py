n, m = map(int, input().split())
not_seen = set(input() for _ in range(n))
not_heard = set(input() for _ in range(m))
not_seen_and_heard = list(not_seen & not_heard)
not_seen_and_heard.sort()
print(len(not_seen_and_heard))
for name in not_seen_and_heard:
    print(name)
