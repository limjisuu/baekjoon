b, n = input().split()
n = int(n)
e, answer = 0, 0

for digit in b[::-1]:
    if digit.isalpha():
        digit = ord(digit) - 55
    else:
        digit = int(digit)
    answer += digit * n ** e
    e += 1

print(answer)
