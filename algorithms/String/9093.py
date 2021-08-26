n = int(input())

for _ in range(n):
    words = input().split()
    answer = [word[::-1] for word in words]
    print(" ".join(answer))
