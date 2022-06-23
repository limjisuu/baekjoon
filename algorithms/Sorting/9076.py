n = int(input())
cases = [list(map(int, input().split())) for _ in range(n)]

for case in cases:
    case.sort()
    numbers = case[1:4]
    print(sum(numbers)) if numbers[2] - numbers[0] < 4 else print("KIN")
