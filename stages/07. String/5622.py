import sys
word = sys.stdin.readline().rstrip('\n')
time = 0
for i in range(len(word)):
    if 65 <= ord(word[i]) <= 67:
        time += 3
    if 68 <= ord(word[i]) <= 70:
        time += 4
    if 71 <= ord(word[i]) <= 73:
        time += 5
    if 74 <= ord(word[i]) <= 76:
        time += 6
    if 77 <= ord(word[i]) <= 79:
        time += 7
    if 80 <= ord(word[i]) <= 83:
        time += 8
    if 84 <= ord(word[i]) <= 86:
        time += 9
    if 87 <= ord(word[i]) <= 90:
        time += 10
print(time)
