useless = ["i", "pa", "te", "ni", "niti", "a", "ali", "nego", "no", "ili"]
words = input().split()
answer = words[0][0].upper()
for word in words[1:]:
    if word not in useless:
        answer += word[0].upper()
print(answer)
