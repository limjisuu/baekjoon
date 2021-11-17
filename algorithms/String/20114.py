n, h, w = map(int, input().split())
strings = [input() for _ in range(h)]
answer = ["?" for _ in range(n)]

for string in strings:
    idx = 0
    for i in range(n):
        for char in string[idx:idx+w]:
            if char != "?":
                answer[i] = char
        idx += w
print("".join(answer))
