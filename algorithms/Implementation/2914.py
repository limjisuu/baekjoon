import sys
songs, average = map(int, sys.stdin.readline().split())
answer = songs * (average - 1) + 1
print(answer)
