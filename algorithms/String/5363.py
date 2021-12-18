n = int(input())

for _ in range(n):
    sentence = input().split()
    yoda = sentence[2:] + sentence[:2]
    print(" ".join(yoda))
