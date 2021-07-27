import sys
n = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(n)]
numbers.sort(reverse=True)
for number in numbers:
    print(number)
