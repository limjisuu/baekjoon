import sys
num = int(sys.stdin.readline())


def padovan(n):
    padovan_list = [0 for _ in range(n + 1)]
    for i in range(1, n+1):
        if 1 <= i <= 3:
            padovan_list[i] = 1
        else:
            padovan_list[i] = padovan_list[i-2] + padovan_list[i-3]
    print(padovan_list[n])


for i in range(num):
    test_case = int(sys.stdin.readline())
    padovan(test_case)
