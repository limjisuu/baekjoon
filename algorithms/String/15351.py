n = int(input())

for _ in range(n):
    word = input()
    answer = 0
    for char in word:
        if char.isalpha():
            answer += ord(char) - 64
    if answer == 100:
        print("PERFECT LIFE")
    else:
        print(answer)
