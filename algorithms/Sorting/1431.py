n = int(input())
numbers = [input() for _ in range(n)]
info = [(len(number), sum(int(digit) for digit in number if digit.isdigit()), number) for number in numbers]
info.sort(key=lambda x: (x[0], x[1], x[2]))
for record in info:
    print(record[2])
