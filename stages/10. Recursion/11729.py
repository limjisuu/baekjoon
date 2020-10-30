import sys
num = int(sys.stdin.readline())
def hanoi(start, finish, intermediate, num):
    if num == 1:
        print(start, finish)
    else:
        hanoi(start, intermediate, finish, num - 1)
        print(start, finish)
        hanoi(intermediate, finish, start, num - 1)
print(2 ** num - 1)
hanoi(1, 3, 2, num)
