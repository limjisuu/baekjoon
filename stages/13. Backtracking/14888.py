import sys
import itertools
n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
plus, minus, multiply, divide = map(int, sys.stdin.readline().split())
operator_list = []

for i in range(plus):
    operator_list.append("+")

for i in range(minus):
    operator_list.append("-")

for i in range(multiply):
    operator_list.append("*")

for i in range(divide):
    operator_list.append("/")

permutation_list = list(set(itertools.permutations(operator_list, n - 1)))


def calculate_plus(num1, num2):
    return num1 + num2


def calculate_minus(num1, num2):
    return num1 - num2


def calculate_multiply(num1, num2):
    return num1 * num2


def calculate_divide(num1, num2):
    if (num1 < 0) and (num2 > 0):
        return -((-num1) // num2)
    return num1 // num2


maximum = -1000000001
minimum = 1000000001
for permutation in permutation_list:
    for i in range(n - 1):
        global result
        if i == 0:
            result = num_list[0]
        if permutation[i] == "+":
            result = calculate_plus(result, num_list[i+1])
        if permutation[i] == "-":
            result = calculate_minus(result, num_list[i+1])
        if permutation[i] == "*":
            result = calculate_multiply(result, num_list[i+1])
        if permutation[i] == "/":
            result = calculate_divide(result, num_list[i+1])
    if result > maximum:
        maximum = result
    if result < minimum:
        minimum = result

print(maximum)
print(minimum)
