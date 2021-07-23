n = int(input())
numbers = set(map(int, input().split()))
result = sorted(list(numbers))
for number in result:
    print(number, end=" ")
