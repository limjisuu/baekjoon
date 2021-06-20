import sys
n = int(sys.stdin.readline())
for _ in range(n):
    sentence = sys.stdin.readline().rstrip()
    answer = sentence[0].upper() + sentence[1:]
    print(answer)
