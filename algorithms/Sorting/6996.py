n = int(input())
for _ in range(n):
    a, b = input().split()
    if sorted(a) == sorted(b):
        print("{a} & {b} are anagrams.".format(a=a, b=b))
    else:
        print("{a} & {b} are NOT anagrams.".format(a=a, b=b))
