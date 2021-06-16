import sys
n = int(sys.stdin.readline())
for _ in range(n):
    string = sys.stdin.readline().rstrip()
    alphabets = [0 for _ in range(26)]
    answer = 0
    for char in string:
        alphabets[ord(char) - 65] += 1
    for i in range(26):
        if alphabets[i] == 0:
            answer += i + 65
    print(answer)
