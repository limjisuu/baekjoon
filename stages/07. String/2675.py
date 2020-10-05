import sys
num = int(sys.stdin.readline())
for i in range(num):
    cnt, word = sys.stdin.readline().split()
    for j in range(len(word)):
        print(word[j] * int(cnt), end='')
    print()
