import sys
word = sys.stdin.readline().rstrip()
reverse = word[::-1]
print(1) if reverse == word else print(0)
