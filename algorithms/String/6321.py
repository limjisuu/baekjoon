n = int(input())
for i in range(1, n+1):
    name = input()
    answer = ["A" if char == "Z" else chr(ord(char) + 1) for char in name]
    print("String #{idx}".format(idx=i))
    print("".join(answer))
    print()
