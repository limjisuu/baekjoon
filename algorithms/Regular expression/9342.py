import re
n = int(input())
p = re.compile("[A-F]?A+F+C+[A-F]?$")
for _ in range(n):
    word = input()
    if p.match(word):
        print("Infected!")
    else:
        print("Good")
