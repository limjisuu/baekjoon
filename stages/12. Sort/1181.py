import sys
num = int(sys.stdin.readline())
word_list = []
check_duplicate = []

for i in range(num):
    word = sys.stdin.readline()
    word_list.append(word)

sorted_list = sorted(word_list, key=lambda x: (len(x), x))

for i in range(num):
    if sorted_list[i] not in check_duplicate:
        print(sorted_list[i], end="")
    check_duplicate.append(sorted_list[i])
