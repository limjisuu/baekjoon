n = int(input())
nicknames = [list(map(str, input().split())) for _ in range(n)]

for nickname in nicknames:
    answer = "god" + "".join(map(str, nickname[1:]))
    print(answer)
