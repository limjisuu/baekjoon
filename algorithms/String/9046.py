n = int(input())
sentences = [input() for _ in range(n)]

for sentence in sentences:
    alphabets = [0 for _ in range(26)]
    for char in sentence.replace(" ", ""):
        alphabets[ord(char) - 97] += 1
    if alphabets.count(max(alphabets)) > 1:
        print("?")
    else:
        print(chr(alphabets.index(max(alphabets)) + 97))
