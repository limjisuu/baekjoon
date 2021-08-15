numbers = list(map(int, input()))
numbers.sort(reverse=True)
if numbers[-1] == 0:
    if sum(numbers) % 3 == 0:
        print("".join(map(str, numbers)))
    else:
        print(-1)
else:
    print(-1)
