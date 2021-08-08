document = input()
word = input()
answer = 0
while word in document:
    answer += 1
    document = document.replace(word, "찾았다!", 1)
print(answer)
