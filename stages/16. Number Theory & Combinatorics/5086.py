import sys
num1, num2 = map(int, sys.stdin.readline().split())

while num1 != 0 or num2 != 0:
    if num2 % num1 == 0:
        print("factor")
    elif num1 % num2 == 0:
        print("multiple")
    else:
        print("neither")
    num1, num2 = map(int, sys.stdin.readline().split())
