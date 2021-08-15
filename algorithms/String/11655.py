string = input()
answer = ""
for char in string:
    if char.isalpha():
        if char.upper() < "N":
            answer += chr(ord(char) + 13)
        else:
            answer += chr(ord(char) - 13)
    else:
        answer += char
print(answer)
