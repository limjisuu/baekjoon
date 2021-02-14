import sys
n = int(sys.stdin.readline())


def push(string):
    stack.append(string)


def pop():
    if stack:
        removed = stack.pop(-1)
        if removed == "(":
            return True
    return False


for i in range(n):
    stack = []
    result = True
    test_case = sys.stdin.readline()

    for parenthesis in test_case:
        if parenthesis == "(":
            push(parenthesis)
        elif parenthesis == ")":
            if not pop():
                result = False
                break
    if stack:
        result = False

    print("YES") if result else print("NO")
