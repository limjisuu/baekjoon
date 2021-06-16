import sys
n = int(sys.stdin.readline())
votes = list(map(str, sys.stdin.readline().rstrip()))
a = votes.count("A")
b = votes.count("B")
if a > b:
    print("A")
elif a < b:
    print("B")
else:
    print("Tie")
