def check_palindrome(words):
    for i in range(len(words)):
        for j in range(len(words)):
            if i == j:
                continue
            word = words[i] + words[j]
            if word == word[::-1]:
                return word
    return 0


test_num = int(input())
for _ in range(test_num):
    n = int(input())
    words = [input() for _ in range(n)]
    answer = check_palindrome(words)
    print(answer)
