import re
n = int(input())
p = re.compile("(100+1+|01)+")
for _ in range(n):
    wave = input()
    if p.fullmatch(wave):
        print("YES")
    else:
        print("NO")
