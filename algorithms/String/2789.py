target = ["C", "A", "M", "B", "R", "I", "D", "G", "E"]
word = input().rstrip()
answer = ""
for char in word:
    if char not in target:
        answer += char
print(answer)
