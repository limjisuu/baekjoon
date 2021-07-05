numbers = [int(input()) for _ in range(9)]
found = False
for i in range(8):
    if found:
        break
    for j in range(i+1, 9):
        answer = sum(numbers) - numbers[i] - numbers[j]
        if answer == 100:
            dwarf1 = numbers[i]
            dwarf2 = numbers[j]
            numbers.remove(dwarf1)
            numbers.remove(dwarf2)
            found = True
            break
for number in numbers:
    print(number)
