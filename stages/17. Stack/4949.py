import sys
sentence = sys.stdin.readline()


def push(string):
    stack.append(string)


def pop():
    if stack:
        removed = stack.pop(-1)
        return removed


while sentence.rstrip() != ".":
    stack = []
    result = True
    for letter in sentence:
        if letter == "(" or letter == "[":
            push(letter)
        elif letter == ")":
            if not pop() == "(":
                result = False
                break
        elif letter == "]":
            if not pop() == "[":
                result = False
                break
    if stack:
        result = False

    print("yes") if result else print("no")
    sentence = sys.stdin.readline()
