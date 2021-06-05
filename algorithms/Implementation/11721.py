import sys
word = sys.stdin.readline()
idx = 0
while idx < len(word):
    print(word[idx:idx+10])
    idx += 10
