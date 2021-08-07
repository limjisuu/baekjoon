n = int(input())

for _ in range(n):
    number = input()
    part1, part2 = number.split("-")
    idx = 0
    num1 = 0
    for char in reversed(part1):
        num1 += (ord(char) - 65) * 26 ** idx
        idx += 1
    num2 = int(part2)
    result = abs(num1 - num2)
    print("nice") if result <= 100 else print("not nice")
