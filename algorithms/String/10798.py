words = [list(input()) for _ in range(5)]
answer = ""
for i in range(15):
    for word in words:
        if i < len(word):
            answer += word[i]
print(answer)
