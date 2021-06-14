import sys
word = sys.stdin.readline().rstrip()
alphabets = [0 for _ in range(26)]
for char in word:
    alphabets[ord(char) - 97] += 1
print(" ".join(map(str, alphabets)))
