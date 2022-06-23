numbers = list(int(input()) for _ in range(7))
odd_numbers = [n for n in numbers if n % 2 == 1]
if odd_numbers:
    print(sum(odd_numbers))
    print(min(odd_numbers))
else:
    print(-1)
