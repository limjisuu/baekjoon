import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


word = input()
number = 0
for char in word:
    if char.isupper():
        number += ord(char) - 38
    else:
        number += ord(char) - 96
print("It is a prime word.") if is_prime(number) else print("It is not a prime word.")
