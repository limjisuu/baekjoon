target = input()
n = int(input())
rings = [input() for _ in range(n)]
answer = 0

for ring in rings:
    ring += ring[0:10]
    if target in ring:
        answer += 1
print(answer)
