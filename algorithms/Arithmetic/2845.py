cnt, area = map(int, input().split())
numbers = list(map(int, input().split()))
total = cnt * area
answers = [n - total for n in numbers]
print(*answers)
