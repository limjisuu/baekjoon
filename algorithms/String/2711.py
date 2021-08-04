n = int(input())
for _ in range(n):
    idx, word = map(str, input().split())
    idx = int(idx)
    print(word[:idx-1] + word[idx:])
