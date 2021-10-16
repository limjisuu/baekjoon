n = int(input())

for _ in range(n):
    string = input()
    odd = [char for char in string[::2]]
    even = [char for char in string[1::2]]
    if len(string) % 2 == 0:
        first = "".join(odd)
        second = "".join(even)
    else:
        first = "".join(odd + even)
        second = "".join(even + odd)
    print(first)
    print(second)
