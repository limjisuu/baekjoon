import sys
n = int(sys.stdin.readline())
scores = [[0 for _ in range(2)] for _ in range(n+2)]
one = 0
two = 1

for i in range(1, n+1):
    stair = int(sys.stdin.readline())
    scores[i][0] = stair
    scores[i][1] = stair

scores[1][two] = 0
scores[2][one] += scores[1][one]

for i in range(3, n+1):
    scores[i][one] += scores[i-1][two]
    scores[i][two] += max(scores[i-2][one], scores[i-2][two])

print(max(scores[n][one], scores[n][two]))
