numbers = list(map(int, input().split()))
square_numbers = list(n ** 2 for n in numbers)
answer = sum(square_numbers) % 10
print(answer)
