import sys
num = int(sys.stdin.readline())
cnt = 0
for i in range(num):
    group_word = True
    word = sys.stdin.readline().rstrip('\n')
    for j in range(len(word)):
        if j != len(word) - 1:
            if word[j] != word[j+1]:
                if word[j] in word[j+1:]:
                    group_word = False
    if group_word:
        cnt += 1
print(cnt)
