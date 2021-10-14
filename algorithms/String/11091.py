n = int(input())

for _ in range(n):
    sentence = input().lower()
    alphabets = [0 for _ in range(26)]
    missing = []
    for char in sentence:
        if char.isalpha():
            alphabets[ord(char) - 97] += 1
    for i in range(26):
        if alphabets[i] == 0:
            missing.append(chr(i + 97))
    if missing:
        print("missing", "".join(sorted(missing)))
    else:
        print("pangram")
